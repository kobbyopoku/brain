---
type: concept
title: Mixture of experts (MoE)
created: 2026-06-06
updated: 2026-06-06
aliases: [mixture-of-experts, moe, expert-routing]
tags: [inference, llm-serving, architecture, parallelism, stub]
---

# Mixture of experts (MoE)

> A model architecture in which a router activates a subset of expert sub-networks per token, shifting the serving bottleneck toward expert parallelism, interconnect, and all-to-all traffic.

## Definition

This page is a **stub**. Mixture of experts is introduced via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]. The page captures only what that source states.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as an expert-routing-dominated architecture that stresses expert parallelism, interconnect, and grouped GEMMs / all-to-all traffic, and uses these properties to drive recommendations toward SGLang, ExLlamaV3, and TensorRT-LLM Wide Expert Parallelism.

## Sub-claims and details

- Architecture is dominated by expert routing. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Stresses expert parallelism, interconnect, and grouped GEMMs / all-to-all traffic. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Drives engine recommendations toward SGLang, ExLlamaV3, and TensorRT-LLM Wide Expert Parallelism. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- No primary source on routing algorithms or expert-load-balancing yet ingested here.

## Related concepts

- [[wiki/concepts/tensor-parallelism]] — both are interconnect-bound sharding strategies.
- [[wiki/concepts/continuous-batching]] — sibling inference-engine technique.
- [[wiki/concepts/llm-serving-benchmarking]] — how all-to-all-bound throughput should be measured.

## Related entities

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
