---
type: concept
title: State machine
created: 2026-06-06
updated: 2026-06-06
aliases: [finite state machine, FSM, state-machine, per-state tool scoping]
tags: [ai-agents, architecture, voice-agents, reliability]
---

# State machine

> An explicit model of an agent's conversation as a set of discrete states with defined transitions, where each state scopes which tools the agent may call — used as the primary safety rail instead of a long system prompt.

## Definition

A **state machine** structures an agent's conversation into discrete states with explicit transitions between them. In the voice-agent context, [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] treats **per-state tool scoping** — limiting the callable functions in each state — as the core safety mechanism, summarized as *"the state machine is the safety rail, not the system prompt."*

## Why it matters

A growing system prompt is an unreliable way to constrain agent behavior; a state machine makes constraints structural rather than textual. The source offers a concrete trigger: move to a real state machine the day the system prompt crosses 300 words ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames per-state tool scoping as the core safety mechanism: "the state machine is the safety rail, not the system prompt." Reports that moving a 12-step intake from speech-to-speech to a chained pipeline with a real state machine lifted completion from 61% to 89%. Heuristic: move to a real state machine the day the system prompt crosses 300 words.

## Sub-claims and details

- **Safety-rail principle**: "the state machine is the safety rail, not the system prompt" ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Per-state tool scoping** limits which functions are callable in each state ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Measured result**: moving a 12-step intake from speech-to-speech to a chained pipeline with a real state machine lifted completion from 61% to 89% ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Adoption heuristic**: move to a real state machine the day the system prompt crosses 300 words ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Open questions and contradictions

- The 300-word threshold is a heuristic; its generality across task types is unaddressed.

## Related concepts

- [[function-calling]] — per-state tool scoping constrains which functions are callable in each state.
- [[agent-guardrails]] — a second, orthogonal reliability layer (input/output checkpoints).

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
