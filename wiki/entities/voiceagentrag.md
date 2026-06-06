---
type: entity
title: VoiceAgentRAG
entity_type: work
created: 2026-06-06
updated: 2026-06-06
aliases: []
tags: [voice-agent, rag, research-paper, salesforce]
---

# VoiceAgentRAG

> A Salesforce AI Research paper (March 1, 2026) introducing a dual-agent RAG cache for voice agents.

## Profile

VoiceAgentRAG is a research paper published by Salesforce AI Research on March 1, 2026. Its core insight is that in real conversation the next question is usually predictable from the current one, so two agents can run concurrently — one answering the current query and one pre-fetching for the predicted next query — to cut retrieval latency. The paper reports benchmark gains from caching predicted retrievals.

## Key facts

- **Publisher**: Salesforce AI Research (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])
- **Published**: March 1, 2026 (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])
- **Core insight**: in real conversation the next question is usually predictable from the current one, so two agents run concurrently (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])
- **Benchmark — cache hit rate**: 75% of queries hit the cache (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])
- **Benchmark — retrieval speedup**: 316x on cache hits (0.35ms vs 110ms) (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])
- **Benchmark — latency saved**: 16 seconds cumulative across 200 queries (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]])

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — Salesforce AI Research paper (March 2026) introducing the dual-agent RAG cache; source of the benchmark numbers.
