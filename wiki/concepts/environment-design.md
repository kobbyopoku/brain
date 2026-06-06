---
type: concept
title: Environment design (RL)
created: 2026-06-06
updated: 2026-06-06
aliases: [environment design, RL environment, reward environment]
tags: [agent-architecture, rl, reward-design, foundational]
---

# Environment design (RL)

> The practice of specifying the input prompt, action format, and reward function that an RL agent trains against — treated as the primary design decision, prior to choosing a training algorithm.

## Definition

An environment in this sense is the triple of an input prompt, an action format, and a reward function. The source's slogan is "environment design first, algorithm selection second": the environment decides *what signal exists*, while the trainer merely decides *how to use the signal*. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It relocates the hard part of RL from algorithm tuning to environment specification — arguing that the quality and shape of the reward signal, not the choice of optimizer, determines whether training produces useful behavior. This frames environment design as the central skill in building agents.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as the first-order design decision — "environment design first, algorithm selection second" — and gives the slogan "the trainer decides how to use the signal; the environment decides what signal exists."

## Sub-claims and details

- An environment = input prompt + action format + reward function. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Four properties of a good environment: partial credit, separation of syntax from semantics, hard-to-exploit reward, and inspectable logs. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- The environment determines *what signal exists*; the trainer only determines *how the signal is used*. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/agent-post-training]] — environment design supplies the reward stage of the pipeline.
- [[wiki/concepts/reward-hacking]] — the failure mode that "hard-to-exploit" environment design guards against.
- [[wiki/concepts/rlvr]] — verifier-based rewards are one way to give an environment a code-checkable signal.
- [[wiki/concepts/grpo]] — an algorithm that consumes the signal an environment defines.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
