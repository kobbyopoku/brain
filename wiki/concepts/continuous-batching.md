---
type: concept
title: Continuous batching
created: 2026-06-06
updated: 2026-06-06
aliases: [continuous-batching, dynamic-batching, in-flight-batching]
tags: [inference, llm-serving, scheduling, stub]
---

# Continuous batching

> A scheduler technique for LLM inference servers that admits, mixes, and evicts requests at the per-token level so a single GPU can serve many concurrent users efficiently — distinct from merely "supporting batching."

## Definition

This page is a **stub**. Continuous batching is introduced via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], which treats it as a scheduling discipline rather than a checkbox feature. The page captures only what that source states.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as a scheduler technique for serving many concurrent users, and stresses that "supporting batching" is not the same as having a good scheduler. Scheduler quality — admission policy, prefill/decode sharing, fairness, and anti-starvation — is named as one of the five real bottlenecks in LLM serving.

## Sub-claims and details

- The source distinguishes merely "supporting batching" from having a high-quality scheduler. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Scheduler quality is evaluated along admission, prefill/decode sharing, fairness, and anti-starvation. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Scheduler quality is one of the five real bottlenecks the source identifies in LLM serving. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- No primary source on the underlying algorithm (e.g. the originating Orca / vLLM literature) yet ingested here.

## Related concepts

- [[wiki/concepts/llm-serving-benchmarking]] — measuring whether a scheduler actually serves concurrent load well.
- [[wiki/concepts/speculative-decoding]] — sibling inference-engine optimization.
- [[wiki/concepts/tensor-parallelism]] — sibling inference-engine technique.

## Related entities

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
