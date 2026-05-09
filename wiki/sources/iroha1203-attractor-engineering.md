---
type: source
title: Hiroyuki Nakahata — Attractor Engineering (codebase as field, PR as force)
created: 2026-05-09
updated: 2026-05-09
source_url: https://dev.to/iroha1203/attractor-engineering-seeing-software-development-as-field-dynamics-16g5
source_type: blog-post
author: Hiroyuki Nakahata
source_date: 2026-05-09
raw_path: raw/Attractor Engineering Seeing Software Development as Field Dynamics.md
content_status: substantive-verbatim
tags: [software-architecture, ai-assisted-development, dynamical-systems, theory, attractor-engineering, archsig, lean-formalization]
---

# Hiroyuki Nakahata — Attractor Engineering (codebase as field, PR as force)

> Theoretical dev.to article (47KB; ~1,000 lines) introducing **Attractor Engineering** as a design theory for software development in the AI era. Core reframe: a codebase is a *field that attracts changes*, a PR is a *force applied to that field*, CI/CD is a *dissipative system* that removes unwanted force, and ArchSig (Architecture Signature) is the *observer* that watches the trajectory. Half practitioner-language, half mathematical formalization in Lean (Algebraic Architecture Theory / AAT). The article's core claim: **with AI generating PRs faster, the design of the field they enter matters more, not less.**

## TL;DR

Five core terms worth absorbing into the wiki vocabulary:

- **Field** — the codebase + names + types + responsibility boundaries + tests + directory structure + previous implementation examples + review culture + design docs + standards. *Everything that shapes which next change feels natural.*
- **PR (force)** — a single proposed change applied to the field. Repeated PRs draw a trajectory.
- **Attractor** — the destination toward which changes are pulled. *Good attractor = good changes pulled in. Bad attractor = bad shortcuts repeated.* Technical debt is a bad basin.
- **Dissipative system** — CI/CD, tests, type checking, static analysis, review. *Removes unwanted components of the force entering the field.* Too weak → debt accumulates fast; too strong → nothing moves.
- **ArchSig (Architecture Signature)** — observer for reading PR-induced movement along multiple axes (static dependencies, boundary rules, abstraction leakage, semantic drift, test observability, per-PR change). *Does not collapse good/bad into one score.*

The article's three-mechanism prescription:

1. **Create the field** — design where good changes feel natural to propose (requirements, priorities, boundaries, types, APIs, examples, templates).
2. **Dissipate bad force** — harness/CI/tests/reviews/PR-granularity reject, weaken, or redirect bad proposals.
3. **Observe the trajectory** — ArchSig + drift reports show *direction of architectural motion over time*, not just snapshot quality.

## Key takeaways

### Why this matters more in the AI era

> *"The essence of AI-assisted development is not simply that code can be written faster. The more important change is that the distribution of selected change operations changes."*

When Claude (or any AI) reads existing code as context and produces the next PR, **it imitates the local style of the field**. If a good reference implementation is nearby, the AI uses it. If a bad shortcut already exists, the AI treats it as natural. *AI rapidly reproduces the local style already present in the field.* This means in the AI era, individual-agent capability is no longer the lever; **the field's shape is.**

This is the strongest articulation in the wiki of why [[markdown-as-agent-contract]] + [[anti-ai-slop-machinery]] *increase* in importance as agents get smarter, rather than decreasing. The field is the contract; AI is the change-engine working within it.

### PRs become more important, not less

Counterintuitive claim. AI lowers the cost of *generating* a PR; the value of PRs as **units of observation, decomposition, dissipation, reversibility, and decision-making** increases. A PR has five roles independent of who wrote it:

1. Cuts continuous change into observable units.
2. Lets us separate the directions in which a change acts.
3. Embeds the dissipative process of review, CI, approval.
4. Creates a boundary for rollback and reversibility.
5. Creates a unit for decision-making and discussion.

### Trajectory shapes (worth canonizing)

The article enumerates 6 trajectory types ArchSig can observe:

| Trajectory | Meaning |
|---|---|
| **Stable Orbit** | Returns to safe region after small changes. |
| **Drift** | Slowly shifts toward a bad region. |
| **Spiral Debt** | Appears to return, but over the long run moves closer to a bad basin. |
| **Sudden Phase Shift** | A signature changes sharply after a particular PR. |
| **Oscillation** | Feature additions and refactorings alternate good/bad. |
| **Basin Capture** | After some point, the system gets captured by a bad structure. |

These are useful labels for codebase health, especially under heavy AI-PR throughput. Pairs cleanly with [[wiki/concepts/dual-write-rollout]] (a deliberate trajectory; *not* drift) and [[reliability-decay-math]] (probability-of-degradation framing).

### "Endpoint safe + zero net delta ≠ path safe"

A theorem proved in the Lean formalization: *a trajectory `0 → 2 → 0` has zero endpoint delta and zero net delta but passes through an unsafe region (state 2)*. Empirical implication: **measuring only start and end states misses excursion damage**. Architecture observers must read trajectories, not snapshots.

This formalizes the intuition that "we ended up fine" doesn't mean "the codebase was safe along the way" — relevant when AI agents do high-volume short-lived churn that nets out clean.

### Observability expansion shock

> *"With coarse observation, a codebase may look safe. But if we add more observation axes, a hidden obstruction may suddenly appear as nonzero."*

ArchSig must distinguish `unmeasured` from `zero`. When a previously-invisible axis becomes measurable, the architecture didn't necessarily get worse — observation got better. **Worth absorbing as a wiki rule**: when adding new lint rules / observability dimensions, the visible-debt count will spike before it falls; this is good news mislabeled as bad.

### Algebraic Architecture Theory (AAT)

The mathematical half of the article formalizes 13 architecture operations: `compose / refine / abstract / replace / split / merge / isolate / protect / migrate / reverse / contract / repair / synthesize`. Each comes with a `ProofObligation` (state-witness pair with assumptions and a conclusion). Lean implementation lives at [`iroha1203/AlgebraicArchitectureTheoryV2`](https://github.com/iroha1203/AlgebraicArchitectureTheoryV2). For the wiki, the *vocabulary* is more useful than the proofs — it gives names to what we already do informally.

### Operations are non-commutative

A specific Lean theorem: applying operations in different orders produces different signatures. This is more than a merge-conflict observation — it formalizes why "review then CI" vs "CI then review" can produce different architectural states. **Particularly relevant for evaluating teams of AI agents** where step ordering in pipelines is itself a design lever.

## Notable quotes

> "A codebase is a field. A PR is a force. CI/CD is a dissipative system. Product managers, product owners, engineers, reviewers, and AI agents are participants in the field. ArchSig is an observer of the trajectory."

> "Architecture design in the era of AI-assisted development can be described as creating a field where future changes gather in good places and can escape bad places."

> "The safest AI coding environment is not the one with the strongest external harness. It is the one where good changes are natural, easy to imitate, observable, and less likely to fall into bad shortcuts."

> "What we need is a field with properties like these: small and observable PRs, fast feedback, reliable CI, a useful type system, architecture tests, carefully selected reference implementations, isolation of legacy code, clear demands, requirements, design boundaries, and human-designed boundaries for value and acceptance criteria."

> "Vague requirements can quickly become vague PRs."

## How this composes with the wiki

- [[markdown-as-agent-contract]] — Attractor Engineering provides the *theoretical foundation* for why CLAUDE.md / DESIGN.md / SKILL.md matter so much. They're field-shaping artifacts; the agent imitates what's nearby.
- [[anti-ai-slop-machinery]] — pre-emit gates / blacklists / P0/P1/P2 are dissipative-system mechanisms. The Open Design machinery is *one engineering instance of the theory*.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — the 5-role subagent stack (architect/coder/reviewer/tester/ops) is an architecture-of-dissipation: each role contributes to weakening or redirecting bad force before merge.
- [[wiki/concepts/dual-write-rollout]] — Kivora's Finding-schema migration is a *deliberate trajectory* through architecture state, with explicit safety properties. ArchSig vocabulary applies.
- [[wiki/concepts/reliability-decay-math]] — both treat architecture as a stochastic process that can degrade over time; AAT adds the *trajectory shape* taxonomy.

## Open questions

- **Is the AAT formalization worth the practical claims?** The article opens with practitioner language and the second half is heavy mathematics. The claims of the first half stand independently; the Lean formalization is a *labeling* of what was already empirically true. Worth treating the vocabulary as load-bearing and the theorems as supporting infrastructure.
- **Trajectory observation in practice.** The wiki has zero ArchSig-equivalent tooling. The closest is [[wiki/concepts/lint]]'s drift checks. Whether to build a real ArchSig-style observer for the brain is a design question for if/when the wiki grows past 500 sources.
- **Could "Attractor Engineering" become a wiki concept page?** Yes — the framing is novel enough and composes with multiple existing concepts. Plan: create [[attractor-engineering]] concept page with cross-cites to dual-write-rollout, anti-ai-slop-machinery, markdown-as-agent-contract.

## Mentioned entities

- [[wiki/entities/iroha1203]] — author *(new)*; Hiroyuki Nakahata.
- [[wiki/entities/algebraic-architecture-theory]] — *(new)* the Lean library; AlgebraicArchitectureTheoryV2 GitHub repo.

## Related concepts

- [[markdown-as-agent-contract]] — agent contracts are field-shaping artifacts.
- [[anti-ai-slop-machinery]] — dissipative-system mechanisms made concrete.
- [[reasoning-execution-split]] — AI as engine, harness as guidance.
- [[reliability-decay-math]] — adjacent (probability-of-degradation framing).
- [[dual-write-rollout]] — deliberate trajectory through architectural state.
- [[lint]] — observability of trajectories at the wiki level.
