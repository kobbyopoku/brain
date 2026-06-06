---
type: concept
title: Prefill vs decode
created: 2026-06-06
updated: 2026-06-06
aliases: [prefill, decode, prefill and decode]
tags: [local-ai, llm-serving, inference, performance]
---

# Prefill vs decode

> The two distinct phases of LLM inference — prefill reads the prompt and builds the KV cache (compute-bound); decode generates tokens one at a time (memory-bandwidth-bound).

## Definition

LLM inference splits into two phases with opposite performance characteristics. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]: **prefill** reads the input prompt and builds the [[wiki/concepts/kv-cache]], a compute-intensive operation; **decode** generates one token at a time, a memory-bandwidth-bound operation.

## Why it matters

This distinction is the load-bearing primitive of the source — it predicts almost every engine recommendation and bottleneck. Whether a workload is prefill-heavy or decode-heavy determines which hardware and [[wiki/concepts/inference-engine]] suit it.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as a load-bearing primitive: prefill reads the prompt and builds the KV cache (compute-intensive); decode generates one token at a time (memory-bandwidth-bound). The distinction predicts almost every engine recommendation and bottleneck.

## Sub-claims and details

- Prefill is compute-intensive; decode is memory-bandwidth-bound. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Because decode is bandwidth-bound, [[wiki/concepts/memory-bandwidth]] (not raw compute) governs token-generation speed. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Prefill is the phase that constructs the KV cache that decode then reads. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/kv-cache]] — built during prefill, read during decode.
- [[wiki/concepts/memory-bandwidth]] — governs decode speed.
- [[wiki/concepts/inference-engine]] — schedules the two phases.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
