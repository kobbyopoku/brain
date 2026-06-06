---
type: concept
title: Conversation design
created: 2026-06-06
updated: 2026-06-06
aliases: [conversation design, writing for ears]
tags: [voice, conversation, prompting, ux]
---

# Conversation design

> The discipline of writing for ears, not eyes — authoring voice-agent turns and prompts for spoken interaction.

## Definition

Conversation design is "the discipline of writing for ears, not eyes." Its rules include short sentences (matched to an 8–10-second attention span), one question per turn, acknowledgment phrases, mirroring the caller's exact words, no markdown in prompts, spelling out numbers, and capping the system prompt at 800 tokens. It prescribes a three-act conversational structure: acknowledgment/orientation, resolution, and confirmation/close. It is framed as the discipline most builders skip.

## Why it matters

Conversation design is the human-facing craft layer of voice agents — the part that determines whether an interaction feels natural. It complements the technical latency and architecture concerns, and connects to Godwin's broader interest in prompt design and UX for AI systems.

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames it as "the discipline of writing for ears, not eyes" — with rules (short sentences for an 8–10s attention span, one question per turn, acknowledgment phrases, mirror the caller's exact words, no markdown, spell out numbers, cap the system prompt at 800 tokens) and a three-act structure (acknowledgment/orientation → resolution → confirmation/close), called the discipline most builders skip.

## Sub-claims and details

- Defined as "the discipline of writing for ears, not eyes." [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Rules: short sentences (8–10s attention span), one question per turn, acknowledgment phrases, mirror the caller's exact words, no markdown in prompts, spell out numbers, cap the system prompt at 800 tokens. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Three-act structure: acknowledgment/orientation → resolution → confirmation/close. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
- Framed as the discipline most builders skip. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]

## Open questions and contradictions

- The 800-token system-prompt cap and 8–10s attention span are the source's heuristics, not independently validated in the wiki.

## Related concepts

- [[wiki/concepts/voice-agent]] — conversation design is the authoring craft for voice agents.
- [[wiki/concepts/latency-budget]] — sibling discipline within voice-agent building.
- [[wiki/concepts/prompt-engineering]] — conversation design is a specialized, spoken-output prompting practice.

## Related entities

- (none yet in wiki)

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
