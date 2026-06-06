---
type: concept
title: Latency budget
created: 2026-06-06
updated: 2026-06-06
aliases: [latency budget, voice latency budget]
tags: [voice, latency, performance, architecture]
---

# Latency budget

> The end-to-end conversational reply budget — roughly 700ms — apportioned across a voice agent's components.

## Definition

A latency budget is the end-to-end conversational reply target (~700ms) for a voice agent, split per component: transport, STT, end-of-turn detection, RAG, LLM time-to-first-token (TTFT), TTS time-to-first-audio, and network. A "fast lane" lands near 440ms; a "slow lane" runs 700–900ms. The framing emphasizes that "every millisecond of processing time is a millisecond of silence the caller sits inside."

## Why it matters

Latency budgeting is the operational core of building usable voice agents — the difference between a natural conversation and an awkward one. For Godwin's automation interests, it is the constraint that determines which model and architecture choices are viable.

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] introduces it as the ~700ms end-to-end reply budget split per component (transport, STT, end-of-turn, RAG, LLM TTFT, TTS time-to-first-audio, network), with a fast lane ~440ms and slow lane ~700–900ms, and names the two biggest 2026 unlocks as model-integrated end-of-turn detection and dual-agent cache prefetch.

## Sub-claims and details

- Target end-to-end conversational reply budget is ~700ms. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Budget is apportioned across transport, STT, end-of-turn detection, RAG, LLM TTFT, TTS time-to-first-audio, and network. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Fast lane ~440ms; slow lane ~700–900ms. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- "Every millisecond of processing time is a millisecond of silence the caller sits inside." [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- The two biggest 2026 unlocks cited: model-integrated end-of-turn detection and dual-agent cache prefetch. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]

## Open questions and contradictions

- The specific millisecond figures are the source's targets as of 2026 and will shift with model and infrastructure advances.

## Related concepts

- [[wiki/concepts/voice-agent]] — the system whose performance the latency budget governs.
- [[wiki/concepts/conversation-design]] — sibling discipline within voice-agent building.

## Related entities

- (none yet in wiki)

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
