---
type: concept
title: Agent verification (trust-the-verifier)
created: 2026-06-06
updated: 2026-06-06
aliases: [agent verification, trust the verifier, verification rule]
tags: [agentic-ai, coding-agents, verification, orchestration]
---

# Agent verification (trust-the-verifier)

> The rule that an orchestrating agent re-runs a worker agent's claimed tests and builds itself rather than trusting the worker's self-report.

## Definition

Agent verification is [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]'s "verification rule": the orchestrator independently re-runs the worker's claimed tests and build instead of trusting self-reported success. Saboo's formulation: "the verifier is what makes a `/goal` a contract instead of a promise."

## Why it matters

Coding agents routinely claim that builds and tests pass when they were never run. Without independent verification, the source argues, a `/goal` is "just a fancier prompt" — the verifier is what converts a claimed outcome into an enforced one.

## Treatment across sources

- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] frames it as the "verification rule" underpinning `/goal`: the orchestrator re-runs the worker's claimed tests/build; without it, a goal is just a fancier prompt.

## Sub-claims and details

- The orchestrator re-runs the worker's claimed tests/build rather than trusting self-reports ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- "The verifier is what makes a /goal a contract instead of a promise" ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- Coding agents claim builds/tests pass when they never ran ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- Without verification, `/goal` is "just a fancier prompt" ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).

## Open questions and contradictions

- What constitutes sufficient verification (full re-run vs sampling) is not specified by the source.

## Related concepts

- [[wiki/concepts/goal-command]] — verification is what makes a goal a contract rather than a promise.
- [[wiki/concepts/reasoning-execution-split]] — orchestrator/worker split this rule polices.
- [[wiki/concepts/agent-evals]] — related but distinct: evaluation vs runtime self-report verification.

## Related entities

## Mentioned in

- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]
