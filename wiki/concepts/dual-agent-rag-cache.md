---
type: concept
title: Dual-agent RAG cache
created: 2026-06-06
updated: 2026-06-06
aliases: [Slow Thinker Fast Talker, predictive RAG cache, speculative retrieval cache]
tags: [ai-agents, rag, voice-agents, latency, retrieval]
---

# Dual-agent RAG cache

> A retrieval pattern that hides vector-search latency in voice agents by running a background "Slow Thinker" that predicts likely follow-up questions and pre-fetches their chunks, while a foreground "Fast Talker" serves answers from an in-memory cache.

## Definition

The **dual-agent RAG cache** splits retrieval across two cooperating agents. A background **Slow Thinker** predicts the user's 3-5 most likely follow-up questions and pre-fetches the relevant chunks into an in-memory cache while the user is still listening. A foreground **Fast Talker** checks that cache first when a query arrives, falling back to a live vector call only on a miss. Cache hits are served in sub-millisecond time versus roughly 110ms for a vector call ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Why it matters

The pattern targets the defining constraint of voice agents — latency that breaks conversational flow — by treating idle time as a resource. Its governing principle is *"use the user's listening time as your computation time"* ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]). It earns wiki-shelf-space because it sits at the intersection of [[retrieval-augmented-generation|RAG]] and real-time agent architecture, both clusters of interest to the wiki owner.

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames it as a new pattern (referred to as "VoiceAgentRAG"): a background Slow Thinker predicts 3-5 likely follow-ups and pre-fetches chunks while the user listens; a foreground Fast Talker checks the in-memory cache first (sub-ms vs ~110ms vector call). Cited paper figures: 75% cache hit rate and 316x speedup on hits.

## Sub-claims and details

- **Slow Thinker** runs in the background, predicting the 3-5 most likely follow-up questions and pre-fetching their chunks ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Fast Talker** runs in the foreground and checks the in-memory cache before issuing any live vector call ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Latency**: cache hits resolve in sub-millisecond time versus ~110ms for a vector call ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Reported results**: 75% hit rate and 316x speedup on hits in the cited paper ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Governing principle**: "use the user's listening time as your computation time" ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Open questions and contradictions

- The 75% hit rate and 316x figures are drawn from the cited paper; how they hold up outside that benchmark is unaddressed.

## Related concepts

- [[retrieval-augmented-generation]] — the cache sits in front of a standard RAG retrieval step.
- [[agent-evals]] — infrastructure-layer latency metrics (p50/p95/p99) measure whether such caching is working.

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
