---
type: concept
title: Attractor Engineering
created: 2026-05-09
updated: 2026-05-09
aliases: [attractor-engineering, field-dynamics-software, archsig]
tags: [software-architecture, ai-assisted-development, dynamical-systems, theory, foundational]
---

# Attractor Engineering

> A design theory for software development in the AI era, coined by [[wiki/entities/iroha1203|Hiroyuki Nakahata (iroha1203)]]. **Reframes a codebase as a field that attracts changes; a PR as a force applied to that field; CI/CD as a dissipative system that removes unwanted force; and ArchSig (Architecture Signature) as the observer that watches the trajectory.** Core claim: *with AI generating PRs faster, the design of the field they enter matters more, not less.*

## Definition

Five core terms:

- **Field** — the codebase + names + types + responsibility boundaries + tests + directory structure + previous implementation examples + review culture + design docs + standards. *Everything that shapes which next change feels natural.*
- **PR (force)** — a single proposed change applied to the field. Repeated PRs draw a *trajectory*.
- **Attractor** — the destination toward which changes are pulled. *Good attractor = good changes pulled in. Bad attractor = bad shortcuts repeated.* Technical debt is a bad basin.
- **Basin** — the surrounding region from which things are likely to fall into a particular attractor.
- **Dissipative system** — CI/CD, tests, type checking, static analysis, review. *Removes unwanted components of the force entering the field.* Too weak → debt accumulates fast; too strong → nothing moves.
- **ArchSig (Architecture Signature)** — observer for reading PR-induced movement along multiple axes (static dependencies, boundary rules, abstraction leakage, semantic drift, test observability, per-PR change). *Does not collapse good/bad into one score.*

The theory's three-mechanism prescription:

1. **Create the field** — design where good changes feel natural to propose (requirements, priorities, boundaries, types, APIs, examples, templates).
2. **Dissipate bad force** — harness/CI/tests/reviews/PR-granularity reject, weaken, or redirect bad proposals.
3. **Observe the trajectory** — ArchSig + drift reports show *direction of architectural motion over time*, not just snapshot quality.

## Why it matters

Most "AI coding hygiene" advice is local: better prompts / smaller PRs / type tests / reviews. Attractor Engineering names what's actually different about the AI era at the *system* level: **AI rapidly reproduces the local style already present in the field**. If a good reference implementation is nearby, the AI uses it. If a bad shortcut already exists, the AI treats it as natural.

This means **individual-agent capability is no longer the dominant lever — the field's shape is**. The same Claude can produce excellent code in a well-shaped codebase and shortcuts-on-shortcuts in a poorly-shaped one. The leverage point shifts from *"hire better AI"* to *"design the field the AI enters."*

The wiki absorbs this for three reasons:

1. **Vocabulary**: *attractor / basin / dissipative system / trajectory / ArchSig / observability expansion shock* are useful labels for what the wiki already does informally.
2. **Composition**: Attractor Engineering composes cleanly with [[markdown-as-agent-contract]] (CLAUDE.md / DESIGN.md as field-shaping artifacts), [[anti-ai-slop-machinery]] (dissipative-system mechanisms made concrete), and [[dual-write-rollout]] (a deliberate trajectory through architectural state).
3. **Theoretical anchor**: many empirical patterns in the wiki ("specialized agents beat generalists" / "voice profile from 20 best pieces" / "field test before merge") become coherent when read through this lens.

## Treatment across sources

- [[wiki/sources/iroha1203-attractor-engineering]] — sole canonical source. 47KB dev.to article. First half practitioner language, second half formalizes in Lean as Algebraic Architecture Theory (AAT). Lean repo: [`iroha1203/AlgebraicArchitectureTheoryV2`](https://github.com/iroha1203/AlgebraicArchitectureTheoryV2).

## Sub-claims and details

### "Endpoint safe" ≠ "path safe"

A trajectory `0 → 2 → 0` has zero endpoint-delta and zero net-delta but passes through unsafe state 2. Architecture observers must read **trajectories**, not snapshots. Empirical implication: *"we ended up fine"* doesn't mean *"the codebase was safe along the way"* — relevant when AI agents do high-volume short-lived churn that nets out clean. Formalized as a Lean theorem in AAT.

### Trajectory shapes (the 6 named patterns)

| Trajectory | Meaning |
|---|---|
| **Stable Orbit** | Returns to safe region after small changes. |
| **Drift** | Slowly shifts toward a bad region. |
| **Spiral Debt** | Appears to return, but over the long run moves closer to a bad basin. |
| **Sudden Phase Shift** | A signature changes sharply after a particular PR. |
| **Oscillation** | Feature additions and refactorings alternate good/bad. |
| **Basin Capture** | After some point, the system gets captured by a bad structure. |

These are useful labels for codebase health, especially under heavy AI-PR throughput.

### Operations are non-commutative

Applying architecture operations in different orders produces different signatures. This is more than a merge-conflict observation — it formalizes why "review then CI" vs "CI then review" can produce different architectural states. **Particularly relevant for evaluating teams of AI agents** where step ordering in pipelines is itself a design lever.

### Observability expansion shock

> *"With coarse observation, a codebase may look safe. But if we add more observation axes, a hidden obstruction may suddenly appear as nonzero."*

ArchSig must distinguish `unmeasured` from `zero`. When a previously-invisible axis becomes measurable, the architecture didn't necessarily get worse — observation got better. **Wiki rule worth absorbing**: when adding new lint rules or observability dimensions, the visible-debt count will spike before it falls; this is good news mislabeled as bad.

### PRs become more important under AI

Counterintuitive claim. AI lowers the cost of *generating* a PR; the value of PRs as **units of observation, decomposition, dissipation, reversibility, and decision-making** increases. A PR has five roles independent of who wrote it:

1. Cuts continuous change into observable units.
2. Lets us separate the directions in which a change acts.
3. Embeds the dissipative process of review, CI, approval.
4. Creates a boundary for rollback and reversibility.
5. Creates a unit for decision-making and discussion.

### What "a good field" looks like

iroha1203 enumerates the properties of a field that can safely receive high-throughput AI changes:

- Small and observable PRs.
- Fast feedback.
- Reliable CI.
- A useful type system.
- Architecture tests.
- Carefully selected reference implementations.
- Isolation of legacy code.
- Clear demands, requirements, design boundaries.
- Human-designed boundaries for value and acceptance criteria.

This is operational guidance, not theory. Most of the wiki's sources on AI-assisted development implicitly assume some subset of these; Attractor Engineering names them as a single design surface.

### Algebraic Architecture Theory (AAT) operations vocabulary

Thirteen architecture operations are formalized in Lean: `compose / refine / abstract / replace / split / merge / isolate / protect / migrate / reverse / contract / repair / synthesize`. Each comes with a `ProofObligation` (state-witness pair with assumptions and a conclusion). Names alone prove nothing; theorem packages do. The vocabulary is more useful than the proofs for wiki purposes — it gives names to what we already do informally.

## How this composes with the wiki

- [[markdown-as-agent-contract]] — CLAUDE.md / DESIGN.md / SKILL.md / context files / ABOUT-ME folders are **field-shaping artifacts**. Attractor Engineering provides the theoretical foundation for why these matter so much: they are what shapes which next change feels natural for the AI to propose.
- [[anti-ai-slop-machinery]] — Open Design's pre-emit gates / blacklists / P0/P1/P2 are **dissipative-system mechanisms made concrete**. The Open Design machinery is one engineering instance of the theory's "dissipate bad force" prescription.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — the 5-role subagent stack (architect/coder/reviewer/tester/ops) is an architecture-of-dissipation: each role contributes to weakening or redirecting bad force before merge.
- [[dual-write-rollout]] — Kivora's Finding-schema migration is a *deliberate trajectory* through architecture state, with explicit safety properties. ArchSig vocabulary applies — the migration is a planned excursion through a specific basin to a target attractor.
- [[reliability-decay-math]] — both treat architecture as a stochastic process that can degrade over time; AAT adds the *trajectory shape* taxonomy.
- [[reasoning-execution-split]] — AI as engine, harness as guidance is the same shape as field/force/dissipation.
- [[cognitive-debt]] — codebase-level analogue: if the field has bad shortcuts, AI multiplies them.

## Open questions

- **Is AAT formalization worth the practical claims?** The article's first-half claims stand independently of the Lean. The formalization is a *labeling* of what's already empirically true. Treat the vocabulary as load-bearing and the theorems as supporting infrastructure.
- **Trajectory observation in practice.** The wiki has zero ArchSig-equivalent tooling. The closest is [[lint]]'s drift checks. Whether to build a real ArchSig-style observer for the brain is a design question for if/when the wiki grows past 500 sources.
- **How does Attractor Engineering compose with [[wiki/concepts/dual-write-rollout|dual-write-rollout]]?** Dual-write is *one named trajectory shape* (a deliberate Drift → Stable Orbit transition). The wiki should treat dual-write as an instance of the broader Attractor Engineering vocabulary; this would unify two existing wiki concepts.
- **Brain-applicability**: at what wiki size does *trajectory observation* (vs snapshot quality) become worth building tooling for? Not yet.

## Related concepts

- [[markdown-as-agent-contract]] — field-shaping artifacts.
- [[anti-ai-slop-machinery]] — dissipative-system mechanisms.
- [[reasoning-execution-split]] — engine + harness shape.
- [[reliability-decay-math]] — stochastic decay framing.
- [[dual-write-rollout]] — deliberate trajectory instance.
- [[lint]] — observability of trajectories at the wiki level.
- [[cognitive-debt]] — codebase-level analogue.

## Related entities

- [[wiki/entities/iroha1203]] — author.
- [[wiki/entities/algebraic-architecture-theory]] — *(stub candidate)* the Lean library.

## Mentioned in

- [[wiki/sources/iroha1203-attractor-engineering]]
