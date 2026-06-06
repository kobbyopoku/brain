---
type: concept
title: Inference engine
created: 2026-06-06
updated: 2026-06-06
aliases: [LLM inference engine, serving engine]
tags: [local-ai, llm-serving, inference, hardware]
---

# Inference engine

> The software layer that turns AI hardware into usable LLM inference — managing memory, dispatching kernels, scheduling requests, and exposing an API.

## Definition

An inference engine is the software that sits between raw hardware (GPU/CPU/unified memory) and a usable large-language-model endpoint. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], it acts as traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, API surface, and sometimes deployment framework.

## Why it matters

Hardware capacity and bandwidth set the ceiling, but the inference engine determines whether that ceiling is reached. Choosing the wrong engine for a given hardware/quantization combination wastes the hardware; the engine — not the GPU alone — decides real-world throughput and latency for self-hosted LLMs.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as the central subject — the software layer that turns hardware into usable inference (traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, API surface, and sometimes deployment framework), sorted into four families plus orchestration layers.

## Sub-claims and details

- The source sorts inference engines into four families: portable/local engines, Apple-unified-memory engines, consumer-CUDA + quantization engines, and production-serving engines — plus orchestration layers that sit above them. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- The engine owns the [[wiki/concepts/kv-cache]] accounting and the [[wiki/concepts/prefill-vs-decode]] split, which together predict most of its bottlenecks. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- [[wiki/concepts/quantization]] formats are not interchangeable across engines; the right format is the one the chosen engine has optimized kernels for. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- No second source yet covers inference engines; cross-source comparison pending.

## Related concepts

- [[wiki/concepts/self-hosted-llm]] — the practice the inference engine serves.
- [[wiki/concepts/prefill-vs-decode]] — primitive the engine schedules around.
- [[wiki/concepts/kv-cache]] — what the engine accounts for in memory.
- [[wiki/concepts/paged-attention]] — engine-level technique for KV-cache management.
- [[wiki/concepts/quantization]] — weight formats engines optimize kernels for.
- [[wiki/concepts/memory-bandwidth]] — hardware limit the engine works against.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
