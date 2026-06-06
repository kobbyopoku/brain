---
type: concept
title: Dual-write rollout
created: 2026-05-08
updated: 2026-06-06
aliases: [parallel-write-rollout, additive-rollout, expand-and-contract-data-pipeline]
tags: [migration-pattern, data-engineering, deployment, safety, observability]
---

# Dual-write rollout

> A migration pattern where a new write path runs in parallel with the legacy one — observably, idempotently, and with failures swallowed — before being promoted to source of truth.

## Definition

Dual-write rollout is the application-data analogue of expand-and-contract: instead of replacing an existing write path in one deploy, you **add** the new path, **run both in parallel** for a defined observation window, then **flip ownership** of any side effects (state updates, downstream events, UI reads) once the new path has been validated against real production traffic.

Three properties together define the pattern:

1. **Additive, not replacing.** The legacy path keeps writing as it always did. The new path is wired in *next to* it. Both write to their own storage; neither blocks the other.
2. **Failures in the new path are swallowed.** Caught at the call site, logged at WARN, and **never** allowed to propagate as a customer-visible failure. The new path is invisible to customers by construction.
3. **Idempotency is non-negotiable.** Because the new path may be retried, replayed, or restarted, every write must be safe to repeat — typically via a unique index over a stable tuple plus an application-layer find-then-insert.

After 1–4 weeks of observation (count parity, no error spam, ideally one example of the new capability firing), ownership flips: downstream consumers (control state, dashboards, events) start reading from the new path, the legacy path becomes redundant, and the new write path can finally fail loudly because customers depend on it.

## Why it matters

The naïve alternative — "ship the new path; remove the old one in the same deploy" — couples three risks into one event:

- **Code risk** (the new path has a bug)
- **Data risk** (the new path produces subtly different data than the old one)
- **Operational risk** (the new path performs differently under real load)

Dual-write decouples them. Code risk is caught immediately by tests + the swallowed-failure pattern. Data risk is caught by an explicit count-parity / value-parity comparison during observation. Operational risk reveals itself over the observation window. Each risk class gets its own validation moment.

The pattern is also the **only honest way** to migrate a system that's already in production: the legacy path's behavior is the ground truth you're trying to match, and you can only know whether you've matched it by running both side-by-side against real traffic.

## When to use it

- You're replacing a load-bearing write path in a production system, and rolling back is expensive.
- The legacy path's exact behavior under production conditions isn't fully documented (which is almost always true).
- The migration changes the *shape* of the data, not just where it's stored — meaning consumers downstream will need to be updated too.
- The new path adds capability the old one didn't have (e.g. a new status value), and you need to prove the capability *appears* in real traffic before downstream consumers depend on it.

## When *not* to use it

- The two paths can't both write — they share an identifier or external resource where double-writes are themselves harmful (sending the same email twice, charging the same card twice). For those cases, prefer a feature flag with a single-path semantic.
- The migration is a pure schema rename / column add with no semantic change — that's an expand-and-contract migration, not a dual-write rollout. Strictly easier.
- You don't have observability infrastructure to compare the two paths. Without a count-parity query or equivalent, the "observation window" is just hope.

## Anatomy

```
┌──────────────────────┐
│  Legacy write path   │── still owns customer-facing state ──┐
│  (unchanged)         │                                       │
└──────────────────────┘                                       │
            │                                                  ▼
            │                                          ┌────────────────┐
            │                                          │ Customer-facing│
            │  ┌── new path called next to legacy ──┐  │ state, events, │
            ▼  │ (try { ingest() }                  │  │ dashboards     │
        Bridge │  catch (Exception) {               │  └────────────────┘
            │  │     log.warn();   // swallowed    │
            │  │  })                                │
            ▼  └────────────────────────────────────┘
┌──────────────────────┐
│  New write path      │── observed but inert during rollout
│  (idempotent, with   │── unique index + find-then-insert
│  conformance tests)  │
└──────────────────────┘
```

After cutover (a separate deploy after the observation window):
- Customer-facing state, events, dashboards switch to reading from the new path
- The legacy write path is removed (or left as belt-and-suspenders for one more cycle)
- The new path's swallowed-failure semantics are removed — failures become loud because customers now depend on them

## Sub-claims and details

- **The toggle should default to off in checked-in code.** A toggle that defaults to on means a fresh environment ships customers into the rollout without explicit operator intent. This is a recurring footgun in migrations.
- **The toggle is global, not per-tenant.** Per-tenant toggles complicate the rollback story — you can't say "the new path is healthy" if you've only run it for one customer. Per-tenant *focus* (which customer to monitor) is fine; per-tenant *scope* of writes is usually not.
- **Pick the pilot carefully.** The customer you watch most closely during observation should ideally have (a) high volume of the relevant operation, (b) tolerance for being a guinea pig, and (c) at least one historical example of the edge case the new path is supposed to handle better.
- **Count parity has tolerances.** "Within ±5%" or "within ±20%" depending on the workload. Don't expect exact match — runs in flight at window boundaries, retries, manual triggers, all introduce normal noise.
- **Observation needs an exit criterion stated up front.** "Watch for two weeks" without specific success conditions is just procrastination. State the conditions that move the rollout forward (e.g. "12 of 14 days within parity window, zero swallowed-exception spikes, at least one example of the new capability firing") and the conditions that stop it.
- **A synthetic harness shortens the runway.** A connector that emits known-good data on a schedule turns "wait until the rare edge case happens" into "verify the pipeline immediately." Worth the engineering cost.

## Related patterns

The dual-write rollout sits inside a small family of additive-migration patterns:

- **Expand-and-contract (database)**: schema-level cousin. Add a new column → backfill → switch reads → remove old column. Same shape, different layer.
- **Strangler fig (application)**: route-level cousin. New service handles new traffic alongside old service; cut over endpoint by endpoint. Same shape, different unit.
- **Parallel run / backtesting (analytics)**: read-side cousin. Run the new query/model alongside the old one; compare outputs; promote when they match. Same shape, no writes.
- **Canary deploy**: traffic-level cousin. New version handles a slice of traffic; expand the slice as confidence grows. Different — focuses on code behavior, not data shape.

What unifies them: **the new and old systems coexist long enough for the difference to be observed in production**, before the old one is removed.

## Open questions and contradictions

- **How long should the observation window be?** Conventional wisdom ranges from "until you've seen each rare edge case at least twice" (Hyrum's-Law-shaped) to fixed timeboxes (1, 2, or 4 weeks). The right answer depends on the operation's frequency and the cost of an undetected divergence.
- **Should the new path's failures stay swallowed forever?** No — but *when* to make them loud is a design call. Most teams flip swallow-off in the same deploy that flips ownership. Some keep belt-and-suspenders for one more cycle. Both are defensible.
- **Is dual-write a code smell or a feature?** A small school of thought argues that needing dual-write means the migration is too big — it should have been broken up. The counterargument: some migrations (data shape + downstream contract changes simultaneously) really are atomic units, and dual-write is the safe-by-design rollout for them.

## Related concepts

- *(Candidates to seed later: `expand-and-contract-migration`, `strangler-fig`, `canary-deploy`, `data-contract-evolution`. Each is a sibling pattern in the additive-migration family.)*

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]] — does not name the dual-write rollout, but its **Outbox pattern** is the transactional-event reliability primitive behind this migration pattern: writing the state change and the to-be-published event in the same transaction so a side effect is never lost on retry. Cross-link to the Outbox/transactional-event reliability mechanism that the new write path depends on.
- [[wiki/projects/kivora]] — the **2026-05-08 Tier 1 Finding-schema migration** is the worked example. `ComposioFindingsBridge` is the bridge; `kivora.findings.composio-emission-enabled` is the toggle (default off, flipped on in production for the 2-week observation window). Pilot tenant: Brolly Africa. The unique idempotency index is `uq_findings_idempotency` over `(tenant_id, workspace_id, run_id, resource_type, resource_id)`. Failures are swallowed in `ComposioFindingsBridge.ingestQuietly()`. Cutover (Tier 2A) explicitly deferred to after the observation window. ADR: `backend/docs/adr/0001-finding-schema.md`.
