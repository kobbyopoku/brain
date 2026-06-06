---
type: concept
title: Speculative decoding
created: 2026-06-06
updated: 2026-06-06
aliases: [speculative-decoding, speculative-sampling]
tags: [inference, llm-serving, decoding, stub]
---

# Speculative decoding

> An LLM inference optimization that drafts cheap candidate tokens and verifies them in parallel against the target model, accelerating generation without changing the output distribution.

## Definition

This page is a **stub**. Speculative decoding is introduced via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]. The page captures only what that source states.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as a technique that drafts cheap tokens and verifies them in parallel, and lists it as supported by llama.cpp, ExLlama, vLLM, SGLang, and TensorRT-LLM.

## Sub-claims and details

- Works by drafting cheap tokens and verifying them in parallel. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Supported by llama.cpp, ExLlama, vLLM, SGLang, and TensorRT-LLM. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- No primary source on draft-model selection or acceptance-rate tradeoffs yet ingested here.

## Related concepts

- [[wiki/concepts/continuous-batching]] — sibling inference-engine optimization.
- [[wiki/concepts/llm-serving-benchmarking]] — how speedup claims should be measured.
- [[wiki/concepts/tensor-parallelism]] — sibling inference-engine technique.

## Related entities

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
