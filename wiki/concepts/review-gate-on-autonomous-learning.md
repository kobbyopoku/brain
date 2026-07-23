---
type: concept
title: Review-gate on autonomous learning
created: 2026-07-22
updated: 2026-07-22
aliases: [memory-review-gate, human-in-the-loop-learning, learned-memory-quarantine]
tags: [agent-architecture, memory, safety, self-learning, agentic]
---

# Review-gate on autonomous learning

> A control that lets a self-learning agent *propose* lessons but quarantines each auto-authored memory from influencing behavior until a human approves it — turning "the agent learned X" into "the agent proposes X; a human ratified it."

## Definition

A self-learning agent extracts durable memories from its own runs (reflect-and-remember) and later recalls them into its prompt. Left unchecked, that loop can entrench the agent's own mistakes, absorb manipulation, or learn from untrusted actors. A review-gate interposes human judgment between *extraction* and *recall*: auto-extracted memories are stored in a pending state and excluded from recall entirely until a reviewer approves them. The learning loop is preserved; what changes is that a proposed lesson is inert until ratified.

## Why it matters

Autonomous memory is the highest-leverage and highest-risk part of a self-improving agent — it changes future behavior without a code change or a prompt change. The naive version ("write what you learned straight into recall") makes the agent's competence drift silently, in whichever direction its recent inputs pushed. The review-gate keeps the compounding benefit of learning while capping the downside: no lesson becomes operative without a human ratifying it, and the ratification is cheap (approve/dismiss a short queue) relative to auditing behavior after the fact.

## Sub-claims and details

- **Pending by default, excluded from recall.** Auto-extracted memories are stored flagged unreviewed and are *entirely* excluded from recall/prompt-injection — not down-weighted, not partially surfaced — until approved. Clarvyn: `reviewed=false` rows are filtered out of `recall_memories`; a Team Memory "Pending review" queue exposes them to the founder ([[wiki/projects/clarvyn]], 2026-07-17 / 2026-07-22).
- **Trusted sources skip the queue.** A memory authored directly by a privileged human — a founder statement, or a reasoned thumbs-down that says exactly what was wrong — is stored pre-approved. The gate is for *machine-proposed* lessons, not human-authored ones.
- **Non-teaching by construction for untrusted actors.** Who may teach is enforced server-side from identity, never from client input: in Clarvyn only privileged roles are in the reflection set, so an employee's or anonymous user's feedback is recorded for analytics but can never reach memory extraction — the untrusted path has no route to the learning loop at all, gated *before* the review queue even applies.
- **It is a lifecycle, not a flag.** pending queue → human *approve* (flip to reviewed) enters recall, or *dismiss* (soft-delete) rejects it. Dedup must key on "seen", not "approved", or rejected items keep re-proposing.
- **Backfill must not retroactively un-inject.** Introducing the flag defaults existing live memories to reviewed=true, so shipping the gate doesn't suddenly blank the agent's established memory.

## Treatment across sources

Project-derived concept (not from an ingested source). Worked example:

- [[wiki/projects/clarvyn]] — self-learning (P1–P3, 2026-07-17) added reflect-and-remember + pgvector recall; the 2026-07-22 hardening added the review-gate (`reviewed` column, recall filter, founder approve queue) plus the multi-surface employee feedback loop that is non-teaching by construction and rolled up for founder visibility.

## Open questions and contradictions

- **Review at scale.** Human approval is cheap at low memory volume; as proposals grow, does it need batching, confidence-tiered auto-approval, or clustering of near-duplicate lessons?
- **Staleness of approved memories.** Approval gates entry to recall but not exit — how does a ratified lesson get re-examined or expired once the world changes?

## Related concepts

- [[wiki/concepts/multi-agent-delegation-with-verifier]] — same "interpose independent judgment before a consequential step" shape, applied to actions rather than learning.
- [[wiki/concepts/fail-open-vs-fail-safe-gating]] — the review-gate is a fail-safe gate on the learning path (unreviewed ⇒ excluded).
- [[wiki/concepts/augmented-llm]] — memory is one of the augmentation pillars; this governs how the memory pillar is *written*.
- [[wiki/concepts/retrieval-augmented-generation]] — recall is retrieval; the gate filters what is eligible to be retrieved.

## Related entities

- [[wiki/entities/anthropic]] — Claude models perform the reflect-and-extract step whose output is gated.

## Mentioned in

- [[wiki/projects/clarvyn]] — worked example (self-learning + review-gate).
