---
type: concept
title: Agent guardrails
created: 2026-06-06
updated: 2026-06-06
aliases: [guardrails, input guard, output guard, agent-guardrails, safety checkpoints]
tags: [ai-agents, safety, voice-agents, reliability, guardrails]
---

# Agent guardrails

> Paired safety checkpoints around an agent's LLM — an input guard before the model and an output guard before the response is delivered — each able to block, redact, or replace content and to log every trigger.

## Definition

**Agent guardrails** are validation checkpoints placed around an agent's LLM call. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] states the governing principle as *"safety is two checkpoints, not one"*: an **input guard** runs before the LLM and an **output guard** runs before the response reaches the user (TTS in the voice case). Each guard returns a `safe(bool)`, a category, and a replacement phrase, and logs every trigger.

## Why it matters

A single checkpoint catches either bad input or bad output but not both. Splitting the concern into two guards covers prompt injection and PII on the way in, and over-promising or unsupported claims on the way out — a structural reliability and trust mechanism for deployed agents ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames it as "safety is two checkpoints, not one." Input guard (prompt injection, PII redaction, topic blocklist) runs before the LLM; output guard (over-promise language, factual claims not in retrieved context, moderation) runs before TTS speaks. Each returns safe(bool)/category/replacement phrase and logs every trigger. One hardcoded ALL-CAPS escalation phrase covers refusal and fall-through.

## Sub-claims and details

- **Two-checkpoint principle**: "safety is two checkpoints, not one" — an input guard and an output guard ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Input guard** checks for prompt injection, redacts PII, and applies a topic blocklist, before the LLM ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Output guard** checks for over-promise language, factual claims not in the retrieved context, and moderation, before TTS speaks ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Guard contract**: each guard returns `safe(bool)`, a category, and a replacement phrase, and logs every trigger ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Escalation fallback**: one hardcoded ALL-CAPS escalation phrase covers refusal and fall-through ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Open questions and contradictions

- None recorded yet.

## Related concepts

- [[function-calling]] — output guards catch over-promise narration that masks a missed function call.
- [[state-machine]] — an orthogonal reliability layer; guards check content, the state machine constrains structure.
- [[agent-evals]] — guard triggers are logged and feed eval review.

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
