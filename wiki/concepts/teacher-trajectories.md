---
type: concept
title: Teacher trajectories
created: 2026-06-06
updated: 2026-06-06
aliases: [teacher trajectories, teacher traces, distillation traces, cold-start traces]
tags: [agent-architecture, distillation, post-training, rl]
---

# Teacher trajectories

> Validated trajectories sampled from a stronger model and kept as supervised fine-tuning data — a distillation technique that solves the RL cold-start / state-distribution problem.

## Definition

Teacher trajectories are produced by sampling multiple completions from a stronger policy (e.g., Gemini), validating each in the environment, and keeping the survivors as the SFT dataset (rejects are retained for debugging). The source's framing: "not magic … keeping the traces that survive." ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It addresses the cold-start problem in agent training: a fresh student starts in a state distribution where rollouts almost never succeed, so there is nothing for RL to learn from. Distilling validated traces from a stronger model bootstraps the student into a region where learning is possible.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as stronger-model distillation that solves the RL cold-start / state-distribution problem — sample from a stronger policy, validate in the environment, keep the survivors — "not magic … keeping the traces that survive."

## Sub-claims and details

- Method: sample multiple completions from a stronger policy, validate them in the environment, and keep the ones that survive as the SFT dataset. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Rejected traces are kept for debugging rather than discarded. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Gemini is cited as an example of the stronger teacher policy. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/supervised-fine-tuning]] — teacher trajectories are the data SFT trains on.
- [[wiki/concepts/agent-post-training]] — supplies the cold-start stage of the pipeline.
- [[wiki/concepts/environment-design]] — the environment is what validates which traces survive.
- [[wiki/concepts/rlvr]] — validation-in-environment is a verifier-style filter.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
