---
type: concept
title: Voice agent
created: 2026-06-06
updated: 2026-06-06
aliases: [voice agent, voice ai agent]
tags: [voice, agents, audio, architecture]
---

# Voice agent

> A real-time, latency-constrained audio system of coordinating components — "not a chatbot with a microphone bolted on."

## Definition

A voice agent is a real-time, latency-constrained audio system composed of five coordinating components — streaming STT, RAG, an LLM, TTS, and functions. It is explicitly distinguished from "a chatbot with a microphone bolted on." Three architectures are identified: chained pipeline, half-cascade, and native speech-to-speech.

## Why it matters

Voice agents are a distinct agentic-architecture surface with hard real-time constraints, relevant to Godwin's interest in agentic systems and small-business automation (e.g. phone-answering use cases). The interruptibility requirement and latency budgeting make this a meaningfully different design problem from text agents.

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] is the canonical definition source — a voice agent is a real-time, latency-constrained audio system of five coordinating components (streaming STT, RAG, LLM, TTS, functions), "not a chatbot with a microphone bolted on," realizable in three architectures (chained pipeline, half-cascade, native speech-to-speech).

## Sub-claims and details

- Five coordinating components: streaming STT, RAG, LLM, TTS, and functions. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Three architectures: chained pipeline, half-cascade, and native speech-to-speech. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Interruptibility is definitional: "A voice agent that cannot be interrupted is not a voice agent. It is voicemail." [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- "Not a chatbot with a microphone bolted on." [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]

## Open questions and contradictions

- The source does not rank the three architectures for any specific deployment; trade-offs are left to the builder.

## Related concepts

- [[wiki/concepts/latency-budget]] — the real-time constraint a voice agent must meet.
- [[wiki/concepts/conversation-design]] — the discipline of authoring voice-agent prompts and turns.

## Related entities

- (none yet in wiki)

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
