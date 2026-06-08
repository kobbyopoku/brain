---
type: concept
title: Cross-environment publishing infrastructure
created: 2026-06-08
updated: 2026-06-08
aliases: [cross-env-content-promotion, signed-content-deploy, manifest-based-content-promotion]
tags: [pattern, security, deployment, multi-tenant, audit, ed25519]
---

# Cross-environment publishing infrastructure

> A pattern for safely propagating shared content (templates, catalogs, master data) from one environment to another using signed manifests, two-person approval, and atomic replay against stable cross-environment identifiers.

## Definition

Cross-environment publishing infrastructure is the application-data analogue of how AWS / GCP / Azure ship config to regions: instead of replicating rows opaquely, you **build a manifest** of what should land, **sign it** with an environment-pinned asymmetric key, **gate the publish** behind two-person approval, and **replay it atomically** on the receiver against stable cross-environment identifiers (codes / slugs / identifiers — never UUIDs, which differ per environment).

Five properties together define the pattern:

1. **Stable cross-env identifiers as the natural key.** UUIDs are environment-local; the receiver re-resolves to local UUIDs by looking up the stable identifier. A row's "identity" is its slug/code, not its primary key.
2. **Signed envelope on the wire.** The manifest is hashed (typically SHA-256 canonical JSON); the hash is signed with the source environment's private key (typically Ed25519); the receiver verifies with a pre-distributed public key. Nonce + timestamp included; replay protection via a seen-nonce table with a bounded window (e.g., 10 minutes).
3. **Two-person approval before signing.** The requester and approver are distinct users on the source environment; a DB CHECK constraint enforces this even if the application layer fails. State machine: `REQUESTED → APPROVED → EXECUTING → COMPLETED | FAILED | REJECTED | EXPIRED`.
4. **Atomic UPSERT-by-code + soft-delete via `deprecated_at`** on the receiver. Customer FKs into the canonical content tables survive content updates — a row's UUID never changes even if the source environment regenerates it. Removal is non-destructive (soft-delete preserves audit trail and customer references).
5. **Full audit log on both sides.** Direction (`OUTBOUND` on source, `INBOUND` on receiver), payload hash, who-requested/who-approved, completion timestamp, family-level row counts. The hash links the two log rows.

## Why it matters

Content updates are uniquely hazardous because they're typically the **canonical reference data customers depend on** — frameworks, control catalogs, risk libraries, questionnaire templates. A bad content change doesn't just break the source environment; it cascades through every tenant's adoption of that content. Naïve alternatives all fail:

- **Database dump → restore on receiver** — destroys customer FKs (UUIDs are environment-local), can't filter to "just this framework", no audit trail of who approved what.
- **REST API "push update"** — no signing, no replay protection, no two-person approval, no atomicity guarantee, identity vs uniqueness conflated.
- **Manual SQL on production** — works for a 5-person team; doesn't scale; auditor will reject.

The pattern solves all four with one mechanism: a content "release" is a structured, signed, approved, audited deploy event — same shape your code-deploy pipeline already is.

It's also the **only pattern that survives a hostile auditor question**: *"How do you control what content reaches your customers' tenants?"* The answer is: the source-env state machine, the asymmetric signature, the no-self-approval constraint, the seen-nonce replay window, the soft-delete preservation of customer references — all checkable on both sides.

## When to use it

- Shared/canonical content has a clear authoritative source environment (typically staging or "platform-admin") and one or more receiving environments (typically production).
- Content updates are infrequent but high-stakes — wrong content reaches every tenant.
- Customers have FKs into the content tables (adoptions, instances, mappings) that must survive content updates.
- The audit/compliance story for "how did this content reach customers" matters to the buyer.
- Multiple operators with publish permission exist (two-person approval has bite).

## When *not* to use it

- The content IS customer data — the pattern is for SHARED content. Customer data needs different rollout patterns (tenant-by-tenant, with feature flags).
- Only one operator has publish permission — the two-person rule degenerates. (You may still want signing + replay protection, but the approval part is theater.)
- The two environments share a database — there's nothing to publish across.
- Content changes daily — the cadence overhead (request → approve → execute) becomes friction. Consider a different mechanism (declarative config in source-of-truth repo, deployed with code).

## Anatomy

```
       SOURCE ENV (staging)                         RECEIVER ENV (prod)
       ┌─────────────────────────┐                 ┌─────────────────────────┐
       │ 1. Author requests      │                 │                         │
       │    "promote X"          │                 │                         │
       │ 2. State row inserted:  │                 │                         │
       │    REQUESTED            │                 │                         │
       │ 3. Approver clicks      │                 │                         │
       │    Approve              │                 │                         │
       │ 4. State: APPROVED      │                 │                         │
       │ 5. Build manifest       │                 │                         │
       │    (stable IDs only)    │                 │                         │
       │ 6. Hash + Ed25519 sign  │                 │                         │
       │ 7. State: EXECUTING     │                 │                         │
       │ 8. POST signed envelope │──── HTTPS ─────▶│ 9. Verify signature     │
       │                         │                 │ 10. Check nonce unseen  │
       │                         │                 │ 11. Check timestamp     │
       │                         │                 │ 12. @Transactional:     │
       │                         │                 │     UPSERT by code      │
       │                         │                 │     Soft-delete missing │
       │                         │                 │ 13. Write INBOUND log   │
       │                         │◀──── 200 OK ────│ 14. Return promotion id │
       │ 15. State: COMPLETED    │                 │                         │
       │ 16. Write OUTBOUND log  │                 │                         │
       └─────────────────────────┘                 └─────────────────────────┘
```

**Source-side tables**: `<content>_promotion_requests` (state machine), `<content>_promotion_log` (OUTBOUND audit), Ed25519 private key in env var.

**Receiver-side tables**: `<content>_promotion_log` (INBOUND audit), `promote_seen_nonces` (replay protection; can be shared across content types — nonces are envelope-level, content-agnostic), Ed25519 public key in env var.

**Manifest shape**: payload-hash, nonce, timestamp, signature header; body is canonical JSON keyed by stable identifiers. Family-level entries: e.g., `requirements: [...]`, `controls: [...]`, `requirementMappings: [...]`.

## Sub-claims and details

- **Ed25519 vs RSA / ECDSA.** Ed25519 is the right primitive for envelope signing: tiny keys (32-byte seed), tiny signatures (64 bytes), deterministic (no nonce-reuse footgun), constant-time implementations. JCA support landed in Java 15; Python via the stdlib `cryptography` library. Most other primitives have practical pitfalls; Ed25519 is the modern default.
- **Stable codes vs UUIDs.** The single most common mistake is using UUIDs as the cross-env key. UUIDs are environment-local — staging's `framework_id` for "SOC 2" is a different UUID than prod's. The manifest must use a stable identifier (`code`, `identifier`, `slug`); the receiver does a lookup-or-create by that identifier. If the catalog tables don't already have stable codes, a migration to add them is a prerequisite (Kivora's V135 did exactly this for platform master tables).
- **Soft-delete via `deprecated_at`, not DELETE.** Customer rows reference content rows. A DELETE breaks those references. A `deprecated_at` timestamp lets the receiver mark content as "no longer in the canonical set" without destroying customer FKs. The frontend reads `WHERE deprecated_at IS NULL` for active content; admin views can show deprecated rows.
- **Replay protection at the envelope, not the content.** The seen-nonces table is keyed on nonce alone, not (nonce, content-type). A nonce burned for a framework promote correctly refuses a platform-content envelope re-using it. The 10-min window matches the timestamp staleness window — anything older than 10 minutes is rejected as stale by timestamp check anyway, so the nonce table can prune at that cadence.
- **`@Transactional` on the receiver, full stop.** The receive-and-apply path runs in one transaction so partial-apply is impossible. If row 47 of 248 fails to UPSERT, the entire batch rolls back; the source side gets a FAILED response; nothing customer-visible mutated. This is the difference between "publishing" and "streaming updates."
- **Two-person approval enforced by DB CHECK, not just code.** A service-layer `if (requesterId == approverId) throw ...` is fine but deletable. A `CHECK (approver_user_id IS NULL OR approver_user_id != requested_by)` constraint at the table level survives application bugs and means an auditor can verify the property without reading code.
- **5-minute cooldown after each COMPLETED.** Prevents fat-finger double-publishes that would no-op due to idempotency but pollute the log. The exact value is arbitrary; the point is to make "I clicked twice" mechanically impossible.
- **24-hour auto-expire on `REQUESTED`.** Prevents stale unapproved requests from blocking the "one in flight" semaphore indefinitely. A request older than 24h is auto-marked EXPIRED on the next eligibility check.

## Treatment across sources

- This pattern is most explicitly named in **content distribution systems** (e.g., Apple Push Notification Service's `apns-id` envelope, AWS Systems Manager Parameter Store change-deploy flow, GitOps controllers like ArgoCD with signed commits).
- In the **GRC / compliance product** space the pattern is rarer — most platforms treat content updates as platform-engineer database migrations, not user-facing operations. Kivora's 2026-06 W2-W5 + Phase A-D rollouts are the first time I've seen the pattern instantiated end-to-end in a multi-tenant GRC platform, with both the framework-scoped and platform-content-scoped surfaces sharing the same signing infra.
- The pattern shares structural DNA with **dual-write rollout** ([[wiki/concepts/dual-write-rollout]]) but solves a different problem: dual-write is about migrating ONE environment from old path to new path; cross-env publishing is about propagating content FROM one environment TO another. Both rely on idempotency + observability; cross-env adds the cryptographic envelope.

## Open questions and contradictions

- **Public-key rotation cadence.** Once deployed, the asymmetric keypair has to rotate eventually (suspected leak, annual security policy, departed sysadmin). The rotation procedure isn't well-documented across implementations I've seen. Naive answers: roll forward (new KID, both old + new keys active for a window, deprecate old) work but are operationally fiddly. Kivora hasn't yet executed a rotation; the procedure is undocumented as of 2026-06-08.
- **What about three+ environments?** The pattern as described is point-to-point (source ↔ receiver). For a staging → preprod → prod chain, do you re-sign at each hop, or carry the original signature through? Re-signing is cleaner (each hop is an independent trust boundary) but requires each intermediate to also be a signing authority. Carrying through means an intermediate failure can't be retried without re-running the original approval. No clear consensus.
- **Manifest size limits.** A "full content" snapshot can be MBs of canonical JSON. At what point do you need streaming chunks vs a single envelope? Kivora's largest manifest to date is ~248 requirements + ~600 controls + ~95 questions ≈ 200 KB — well within HTTP body limits. A larger catalog might force chunked manifests with merkle-tree-style root signing.

## Related concepts

- [[wiki/concepts/dual-write-rollout]] — sibling pattern for in-environment migrations; shares idempotency + observability principles, differs in trust model (no signature needed, since one env).
- [[wiki/concepts/markdown-as-agent-contract]] — analogous "contract via signed artifact" pattern at the LLM agent layer.
- [[wiki/concepts/reasoning-execution-split]] — execution-side guarantees (CHECK constraint, signature verify) are the same shape as separating LLM reasoning from deterministic action.

## Worked example

- [[wiki/projects/kivora|Kivora]] — 2026-06 W2-W5 (per-framework promotion) + Phase A-D (platform content promotion) both instantiate the pattern. V134 + V137 schema, `PromoteSigner` + `PromoteVerifier` (Ed25519 wrapping), `MasterFrameworkPromotionService` + `MasterPlatformContentPromotionService` (state machine + cross-env POST), `MasterFrameworkImportTx` + `PlatformContentImportTx` (receiver atomic upsert), shared `promote_seen_nonces` table. M2M-mapped requirements support added as a manifest-field extension (`requirementMappings`) in the 2026-06-08 hotfix.
