---
type: concept
title: Fail-open vs fail-safe gating
created: 2026-07-22
updated: 2026-07-22
aliases: [fail-open-fail-closed, gate-failure-direction, availability-vs-safety-gating]
tags: [agent-architecture, safety, reliability, agentic]
---

# Fail-open vs fail-safe gating

> When a gate that guards an agent action can't run its own check, it must fail in a chosen direction — *fail-open* (allow through, protect availability) or *fail-safe* (block, protect safety) — and the correct direction is picked per-gate from the cost of a wrong allow versus a wrong block.

## Definition

Agentic systems interpose gates around model behavior: input guards, output guards, per-turn tool-scoping, and an independent check before high-consequence tool calls. Each gate can itself become unavailable (LLM timeout, dependency down, parse failure). *Fail-open* means the gate defaults to allowing the guarded thing through when its check can't run; *fail-safe* (a.k.a. fail-closed) means it defaults to blocking. The decision is not global — it is made **per gate**, by comparing the blast radius of a false allow against the blast radius of a false block.

## Why it matters

If every gate fails the same way, the system is wrong in one of two directions: fail-everything-open and any outage silently waves dangerous actions through; fail-everything-closed and any outage locks legitimate users out of the whole product. Matching each gate's failure direction to what it actually protects is a load-bearing safety decision, not an implementation detail — and getting it wrong is invisible until the outage happens. This is the reliability-side complement to [[wiki/concepts/multi-agent-delegation-with-verifier]]: that concept says *who* confirms a destructive action; this one says *what happens when the confirmer is down*.

## Sub-claims and details

- **Availability-protecting guards fail OPEN.** An input injection/jailbreak guard or a per-turn [[wiki/concepts/progressive-disclosure|tool-scoping]] step sits in the path of every legitimate request; its outage must never lock users out, and the worst case of one missed guard is bounded. Clarvyn's input/output guardrails fail-open ([[wiki/projects/clarvyn]], 2026-07-22).
- **Consequence-protecting gates fail SAFE.** A Verifier that runs before destructive/irreversible tools (process payroll, deactivate employee, delete posting) must *block* when it can't render a verdict — the destructive action does not execute on a coin-flip. Clarvyn's Verifier fails-safe.
- **A fail-safe gate must have no silent bypass.** The failure mode is assuming *another* gate covers the tool: Clarvyn's Verifier, when unavailable, only lets a gated tool proceed if a human confirmation already covers it — otherwise it blocks. The invariant "a gated tool never executes without either a Verifier ALLOW or a passed human confirmation" has to be checked against *every* gated tool, not assumed.
- **Strict verdict parsing is part of failing safe.** `bool("false") === true` — a fail-safe gate must test `allow is True`, never coerce a truthy string. A permissive parse quietly converts fail-safe into fail-open.
- **Stacked gates compound** ([[wiki/concepts/reliability-decay-math]]): the more gates in series, the more the per-gate failure directions determine the system's aggregate behavior under partial outage.

## Treatment across sources

Project-derived concept (not from an ingested source). Worked example:

- [[wiki/projects/clarvyn]] — the 2026-07-22 agent safety framework makes the direction explicit per lever: input guard + output guard + tool-scoping fail **open** (availability); the Verifier before 17 destructive/approval tools fails **safe** (a review-caught bug had 4 tools bypassing both Verifier and confirmation on an API blip — the fix was to block unless human confirmation covers the tool).

## Open questions and contradictions

- **Observability of fail-safe blocks.** A fail-safe gate blocking because it's *down* looks, to the user, like it blocking because it *denied* — how do you alert on "gate unavailable, action refused" distinctly from "gate ran, action denied"?
- **Degradation UX.** When a fail-open guard is down, should the product run in a reduced-capability mode (fewer tools, extra confirmations) rather than silently unguarded?

## Related concepts

- [[wiki/concepts/multi-agent-delegation-with-verifier]] — names the independent confirmer; this concept governs its behavior under outage.
- [[wiki/concepts/review-gate-on-autonomous-learning]] — a fail-safe gate applied to the *learning* path rather than the *action* path.
- [[wiki/concepts/reliability-decay-math]] — why stacking gates makes per-gate failure direction matter more.
- [[wiki/concepts/reasoning-execution-split]] — the guards themselves are cheap-model checks separated from the reasoning loop.

## Related entities

- [[wiki/entities/anthropic]] — Claude Haiku/Sonnet run the guard + Verifier checks.

## Mentioned in

- [[wiki/projects/clarvyn]] — worked example (agent safety framework).
