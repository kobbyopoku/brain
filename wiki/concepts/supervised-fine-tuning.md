---
type: concept
title: Supervised fine-tuning (SFT)
created: 2026-06-06
updated: 2026-06-06
aliases: [SFT, supervised fine-tuning, imitation learning]
tags: [agent-architecture, fine-tuning, post-training, rl]
---

# Supervised fine-tuning (SFT)

> An imitation-learning stage that pulls a student model toward demonstrated teacher trajectories so it learns the grammar of the action space — "buying you syntax" before reinforcement learning optimizes behavior.

## Definition

SFT is imitation learning that trains the student to reproduce demonstrated teacher trajectories. Its job is to teach the action space's syntax — moving the policy from a region where almost every rollout fails into one where rollouts are valid enough for RL to explore productively. It is the initialization for on-policy exploration, not the final model. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It explains the division of labor in agent post-training: SFT handles *syntax* (valid actions) while RL handles *semantics* (good behavior). Without it, RL starts in a region where rollouts almost always fail, so there is no useful gradient to learn from.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as imitation learning that "buys you syntax" — the initialization that makes productive on-policy RL exploration possible, not the final model.

## Sub-claims and details

- SFT pulls the student toward demonstrated teacher trajectories so it learns the grammar of the action space. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- It moves the policy from a region where almost every rollout fails into one where rollouts are valid enough for RL. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- It is an initialization step for RL, not the final model. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/agent-post-training]] — SFT is the middle stage of the pipeline.
- [[wiki/concepts/teacher-trajectories]] — supplies the demonstrations SFT imitates.
- [[wiki/concepts/grpo]] — the RL stage SFT initializes.
- [[wiki/concepts/fine-tuning]] — broader category of which SFT is an instance.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
