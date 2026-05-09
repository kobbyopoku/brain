---
type: entity
title: Hiroyuki Nakahata (iroha1203)
entity_type: person
created: 2026-05-09
updated: 2026-05-09
website: https://dev.to/iroha1203
aliases: [iroha1203]
tags: [author, dev-to, software-architecture, lean-formalization, attractor-engineering, theory]
---

# Hiroyuki Nakahata (iroha1203)

> Software-architecture theorist; coiner of **Attractor Engineering** as a design theory for software development in the AI era. Maintains the Lean library [`AlgebraicArchitectureTheoryV2`](https://github.com/iroha1203/AlgebraicArchitectureTheoryV2) (AAT) — formal vocabulary for treating architecture operations (compose / refine / abstract / replace / split / merge / isolate / protect / migrate / reverse / contract / repair / synthesize) as theorem packages with proof obligations. Distinguishes from most AI-coding sources in the wiki by writing *theoretical* rather than *operational* — the only practitioner so far who frames AI-assisted development as a problem of **field dynamics** rather than tool selection.

## Profile

Hiroyuki Nakahata writes long-form theoretical articles on dev.to. The wiki has one substantive ingest: *"Attractor Engineering: Seeing Software Development as Field Dynamics"* (2026-05-09; 47KB; ~1,000 lines). The article is bilingual in style — first half is practitioner-language ("a codebase is a field; a PR is a force"), second half formalizes the same intuition in Lean as Algebraic Architecture Theory.

The wiki ingests him for two reasons:

1. **Vocabulary**: *attractor / basin / dissipative system / trajectory / ArchSig / observability expansion shock* are useful labels for what we already do informally.
2. **Composition**: AAT vocabulary composes cleanly with [[markdown-as-agent-contract]], [[anti-ai-slop-machinery]], and [[wiki/concepts/dual-write-rollout|dual-write-rollout]]. Provides theoretical scaffolding for empirical patterns elsewhere in the wiki.

## Key facts

- **Dev.to handle**: [iroha1203](https://dev.to/iroha1203).
- **GitHub repo**: [`AlgebraicArchitectureTheoryV2`](https://github.com/iroha1203/AlgebraicArchitectureTheoryV2) — Lean implementation of AAT.
- **Posts in wiki**: 1 substantive (the Attractor Engineering article).
- **Genre**: theoretical software architecture; closer to academic than operational.

## Positions and claims

- **A codebase is a field that attracts changes; a PR is a force applied to that field.**
- **In the AI era, individual-agent capability is no longer the lever — the field's shape is.** AI imitates whatever local style is already present in the codebase; designing the field becomes more important, not less.
- **PRs become more important under AI**, not less, because their value as units of *observation, decomposition, dissipation, reversibility, and decision-making* increases as generation cost falls.
- **Endpoint-safe ≠ path-safe.** A trajectory `0 → 2 → 0` has zero endpoint-delta and zero net-delta but passes through unsafe state 2. Architecture observers must read trajectories, not snapshots.
- **Observability expansion shock**: when a previously-invisible axis becomes visible, the architecture didn't necessarily get worse — observation got better. ArchSig must distinguish `unmeasured` from `zero`.
- **Operations are non-commutative**: applying architecture operations in different orders produces different signatures. Step ordering in agent pipelines is itself a design lever.

## Mentioned in

- [[wiki/sources/iroha1203-attractor-engineering]] — sole substantive ingest.

## Related concepts

- [[markdown-as-agent-contract]] — agent contracts are field-shaping artifacts.
- [[anti-ai-slop-machinery]] — dissipative-system mechanisms.
- [[reasoning-execution-split]] — AI as engine, harness as guidance.
- [[reliability-decay-math]] — adjacent (probability-of-degradation framing).
- [[dual-write-rollout]] — deliberate trajectory through architectural state.
- [[lint]] — observability of trajectories at the wiki level.
