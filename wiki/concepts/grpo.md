---
type: concept
title: GRPO
created: 2026-06-06
updated: 2026-06-06
aliases: [GRPO, group-relative policy optimization, GRPOTrainer]
tags: [agent-architecture, rl, algorithm, post-training]
---

# GRPO

> Group-relative policy optimization — an RL algorithm that scores a group of sampled completions per prompt and updates the policy toward those that beat the group's average reward.

## Definition

GRPO samples G completions for each prompt, scores them, and computes a group-relative advantage A_i = (r_i − mean(r)) / (std(r) + eps); the loss is −advantage × logprob(tokens). Real implementations add PPO-style ratio clipping, a KL penalty, a reference model, and masking. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It is a concrete, demonstrable RL algorithm for the optimization stage of agent post-training — simple enough to derive from first principles yet the basis for production trainers, making it a useful anchor for understanding how reward signals become policy updates.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] demonstrates GRPO from first principles and runs it via TRL's `GRPOTrainer`.

## Sub-claims and details

- Core loop: sample G completions per prompt, score them, compute advantage A_i = (r_i − mean(r)) / (std(r) + eps), and take loss = −advantage × logprob(tokens). ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Production versions add PPO-style ratio clipping, a KL penalty, a reference model, and masks. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Worked in practice via the TRL library's `GRPOTrainer`. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/agent-post-training]] — GRPO is an RL algorithm for the optimization stage.
- [[wiki/concepts/environment-design]] — GRPO consumes the reward signal an environment defines.
- [[wiki/concepts/rlvr]] — verifier rewards can supply the scores GRPO ranks.
- [[wiki/concepts/reward-hacking]] — GRPO will optimize toward any exploitable reward.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
