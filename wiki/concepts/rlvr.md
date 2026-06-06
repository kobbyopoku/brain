---
type: concept
title: RLVR / verifiers
created: 2026-06-06
updated: 2026-06-06
aliases: [RLVR, verifiers, reinforcement learning from verifiable rewards, verifiable rewards]
tags: [agent-architecture, rl, reward-design, post-training]
---

# RLVR / verifiers

> Reinforcement learning from verifiable rewards — using execution-checkable verifiers, rather than judge models, to convert task execution into a training signal.

## Definition

A verifier turns execution into supervision: instead of asking a model to judge a completion, the environment runs it and checks the result. The source's minimal verifier is a `validate_completion()` function whose reward is a partial-credit decomposition over checks such as parse, schema, renderer-accept, entities-present, arrows, and layout. Code-checkable signals are preferred over judge-model signals wherever possible. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

Verifiable rewards are harder to game than judge-model rewards and provide objective, decomposable signals — making them a primary defense against reward hacking and a reliable substrate for the RL stage of agent training.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as "verifiers turn execution into supervision," using a toy `validate_completion()` as a minimal verifier and a partial-credit reward decomposition; code-checkable signals are preferred over judge-model signals.

## Sub-claims and details

- "Verifiers turn execution into supervision." ([[wiki/sources/athletickoder-building-agents-first-principles]])
- The toy `validate_completion()` is a minimal verifier whose reward decomposes over parse, schema, renderer-accept, entities-present, arrows, and layout checks. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Code-checkable signals are preferred over judge-model signals where possible. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/environment-design]] — verifiers are how an environment produces a code-checkable reward.
- [[wiki/concepts/reward-hacking]] — verifiable rewards are harder to game than judge-model rewards.
- [[wiki/concepts/grpo]] — verifier scores can supply the rewards GRPO ranks.
- [[wiki/concepts/teacher-trajectories]] — environment validation of traces is verifier-style filtering.
- [[wiki/concepts/agent-post-training]] — verifiers supply the reward signal for the RL stage.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
