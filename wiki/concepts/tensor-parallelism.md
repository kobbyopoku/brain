---
type: concept
title: Tensor parallelism
created: 2026-06-06
updated: 2026-06-06
aliases: [tensor-parallelism, tp]
tags: [inference, llm-serving, parallelism, gpu, stub]
---

# Tensor parallelism

> A model-sharding strategy that splits a single model's tensors across multiple GPUs, requiring frequent all-reduce collectives and therefore strong inter-GPU interconnect.

## Definition

This page is a **stub**. Tensor parallelism is introduced via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]. The page captures only what that source states.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as splitting a model across GPUs, needing frequent all-reduce collectives and strong interconnect (NVLink/NVSwitch); it names as a common mistake that, without NVLink, pipeline parallelism may outperform tensor parallelism.

## Sub-claims and details

- Splits a model across GPUs. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Requires frequent all-reduce collectives and strong interconnect (NVLink/NVSwitch). ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Common mistake: without NVLink, pipeline parallelism may outperform tensor parallelism. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- No primary source on the crossover point between tensor and pipeline parallelism yet ingested here.

## Related concepts

- [[wiki/concepts/mixture-of-experts]] — MoE stresses expert parallelism and interconnect in a related way.
- [[wiki/concepts/continuous-batching]] — sibling inference-engine technique.
- [[wiki/concepts/llm-serving-benchmarking]] — how interconnect-bound throughput should be measured.

## Related entities

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
