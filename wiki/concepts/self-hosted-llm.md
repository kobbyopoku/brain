---
type: concept
title: Self-hosted LLM
created: 2026-06-06
updated: 2026-06-06
aliases: [local LLM, local AI, self-hosting LLMs]
tags: [local-ai, llm, inference, self-hosting]
---

# Self-hosted LLM

> The practice of running large language models on hardware you control rather than calling a hosted API.

## Definition

A self-hosted LLM is a model run on local or self-managed infrastructure — consumer GPUs, Apple Silicon, or owned servers — rather than via a third-party hosted endpoint. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], the practice involves a stack: hardware capacity and bandwidth at the bottom, an [[wiki/concepts/inference-engine]] above it, and quantized model weights running through it.

## Why it matters

Self-hosting governs control, cost, privacy, and capability ceiling for local AI workloads — central to Godwin's interest cluster in agentic architecture and AI products. It reframes model selection from "which API" to "what hardware + engine + quantization combination."

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as the broader practice the guide serves: the source is Part 3 of a self-hosted-LLM / local-AI series, covering the software layer (inference engines) above the hardware capacity/bandwidth math of Parts 1–2.

## Sub-claims and details

- The source positions itself as Part 3 of a multi-part series; Parts 1–2 cover hardware capacity and bandwidth, Part 3 covers the software layer. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- The recurring self-hosting principle is "fit is not speed, capacity is not bandwidth" — fitting a model into memory does not guarantee fast generation. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/inference-engine]] — the software layer that makes self-hosting work.
- [[wiki/concepts/quantization]] — how models are made to fit on owned hardware.
- [[wiki/concepts/memory-bandwidth]] — limit on self-hosted decode speed.
- [[wiki/concepts/unified-memory]] — Apple-Silicon route to self-hosting large models.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
