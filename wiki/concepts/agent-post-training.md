---
type: concept
title: Agent post-training pipeline
created: 2026-06-06
updated: 2026-06-06
aliases: [agent post-training, post-training pipeline, SFT-then-RL]
tags: [agent-architecture, rl, post-training, fine-tuning, foundational]
---

# Agent post-training pipeline

> The canonical sequence for turning a base model into a working agent: base model → supervised fine-tuning on teacher traces → reinforcement learning on environment reward.

## Definition

A post-training pipeline that composes three stages, each solving a distinct problem. Teacher trajectories solve the cold start; supervised fine-tuning teaches the action language; reinforcement learning optimizes behavior against environment reward; and evaluation checks that the environment measures the right thing. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It supplies a first-principles mental model for *how* agents are actually built — separating imitation (SFT) from optimization (RL) and naming where each stage's leverage and failure modes live. This is foundational scaffolding for reasoning about agent training rather than treating it as a single opaque step.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as the canonical first-principles statement: base model → SFT on teacher traces → RL on environment reward; teacher trajectories solve cold start, SFT teaches the action language, RL optimizes behavior, and evaluation checks that the environment measures the right thing.

## Sub-claims and details

- The pipeline has four conceptual roles: teacher trajectories (cold start), SFT (action language), RL (behavior optimization), and evaluation (does the environment measure the right thing). ([[wiki/sources/athletickoder-building-agents-first-principles]])
- SFT is an initialization step, not the final model — it moves the policy into a region where RL can productively explore. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/supervised-fine-tuning]] — the SFT stage of the pipeline.
- [[wiki/concepts/teacher-trajectories]] — supplies the cold-start data for SFT.
- [[wiki/concepts/environment-design]] — defines the reward signal the RL stage optimizes against.
- [[wiki/concepts/grpo]] — a concrete RL algorithm used in the optimization stage.
- [[wiki/concepts/rlvr]] — verifier-based reward, a way to supply the RL signal.
- [[wiki/concepts/reward-hacking]] — the dominant failure mode of the RL stage.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
