---
type: concept
title: Local AI
created: 2026-06-06
updated: 2026-06-06
aliases: [local AI, self-hosted LLM, local-ai]
tags: [self-hosted-llm, inference, local-ai-hardware, stub]
---

# Local AI

> Running LLM inference on self-hosted / local hardware rather than via a hosted API, where the inference engine is the software layer that turns hardware into usable inference. Appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Definition

This is a **stub**. Local AI, as treated in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], is the practice of self-hosting LLM inference on local hardware. The recurring principle is that you pick a hardware strategy, a workload shape, and a serving model first, and the inference engine follows; inference performance is "memory movement plus scheduling," with VRAM determining fit and memory bandwidth determining decode speed.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] catalogs the major inference-engine families and local-AI hardware (including AMD and Intel targets), arguing the engine choice follows from hardware + workload + serving-model decisions.

## Related concepts

## Related entities

- [[wiki/entities/amd]] — GPU vendor target for local-AI inference (ROCm/HIP).
- [[wiki/entities/intel]] — hardware target for local-AI inference.

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
