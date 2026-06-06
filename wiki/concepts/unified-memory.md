---
type: concept
title: Unified memory
created: 2026-06-06
updated: 2026-06-06
aliases: [unified memory architecture, Apple unified memory]
tags: [local-ai, hardware, inference, apple-silicon]
---

# Unified memory

> A shared memory pool accessible by both CPU and GPU, as on Apple Silicon — a capacity advantage for fitting large quantized models, with a bandwidth tradeoff against dedicated HBM.

## Definition

Unified memory is a single physical memory pool shared by CPU and GPU rather than separate dedicated VRAM. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], on Apple Silicon this is a capacity superpower — it can fit large quantized models that are impossible on 24 GB consumer VRAM — but carries a [[wiki/concepts/memory-bandwidth]] tradeoff versus HBM.

## Why it matters

Unified memory is the route by which Apple-Silicon machines self-host large models that consumer NVIDIA cards cannot fit, making it central to one of the four inference-engine families. It crystallizes the "capacity is not bandwidth" point: high fit, lower bandwidth.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as Apple Silicon's shared CPU/GPU memory pool — a capacity superpower (fit large quantized models impossible on 24 GB consumer VRAM) with a bandwidth tradeoff vs HBM.

## Sub-claims and details

- Unified memory is a shared CPU/GPU pool on Apple Silicon. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- It can fit large quantized models that 24 GB consumer VRAM cannot. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Its bandwidth is lower than dedicated HBM, a tradeoff for the capacity gain. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/memory-bandwidth]] — the dimension unified memory trades off.
- [[wiki/concepts/quantization]] — what makes large models fit in the pool.
- [[wiki/concepts/self-hosted-llm]] — unified memory as a self-hosting route.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
