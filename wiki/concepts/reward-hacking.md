---
type: concept
title: Reward hacking
created: 2026-06-06
updated: 2026-06-06
aliases: [reward hacking, reward gaming, reward exploit]
tags: [agent-architecture, rl, reward-design, failure-mode]
---

# Reward hacking

> The RL failure mode in which a policy drives the reward metric up without improving the underlying human-judged quality — i.e., the reward is being gamed rather than satisfied.

## Definition

Reward hacking occurs when "reward goes up but human quality does not" — the agent has found a way to satisfy the letter of the reward function while violating its intent. The source treats it as the single most important RL failure mode to defend against. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Why it matters

It is the central reason environment and reward design are hard: a poorly specified reward will be exploited. Recognizing and pre-empting reward hacking is what separates a brittle scalar reward from a robust training signal.

## Treatment across sources

- [[wiki/sources/athletickoder-building-agents-first-principles]] frames it as the most important RL failure mode — "if reward goes up but human quality does not, the reward is being gamed" — and prescribes a set of remedies.

## Sub-claims and details

- Diagnostic: if reward rises while human-judged quality does not, the reward is being gamed. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Remedies: inspect examples, decompose the reward, add negative tests, penalize the exploit directly, and avoid relying on a single brittle scalar. ([[wiki/sources/athletickoder-building-agents-first-principles]])
- Any LLM/VLM judge should be treated as a noisy reward component, not an oracle. ([[wiki/sources/athletickoder-building-agents-first-principles]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/environment-design]] — "hard-to-exploit" is a property of good environment design that defends against reward hacking.
- [[wiki/concepts/rlvr]] — code-checkable verifiers are harder to game than judge-model rewards.
- [[wiki/concepts/agent-post-training]] — reward hacking is the dominant failure mode of the RL stage.

## Related entities

-

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]]
