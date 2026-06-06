---
type: concept
title: KV cache
created: 2026-06-06
updated: 2026-06-06
aliases: [key-value cache, KV-cache]
tags: [local-ai, llm-serving, inference, memory]
---

# KV cache

> The stored key/value tensors from prior tokens that an LLM reuses during generation; it grows with batch size and context length and can exhaust memory even when the weights fit.

## Definition

The KV cache holds the key and value tensors computed for tokens already processed, so the model does not recompute them on each new token. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], it grows with both batch size and context length, making it the limiting factor for long-context and high-concurrency workloads — it can exhaust memory even when model weights fit comfortably.

## Why it matters

The KV cache is why "the model fits" is not the same as "the workload fits." It is the central memory-management problem an [[wiki/concepts/inference-engine]] must solve, and the target of techniques like PagedAttention, prefix caching, and KV quantization.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as growing with batch size and context length — able to exhaust memory even when weights fit; the limiting factor for long-context / high-concurrency workloads. Addressed by PagedAttention, prefix caching, KV quantization, and disaggregation.

## Sub-claims and details

- KV-cache size scales with both batch size and context length. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- It can exhaust memory even when model weights fit. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Mitigations named: [[wiki/concepts/paged-attention]], prefix caching, KV quantization, and disaggregation. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- The cache is built during prefill (see [[wiki/concepts/prefill-vs-decode]]). ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/paged-attention]] — block-based KV-cache management.
- [[wiki/concepts/prefill-vs-decode]] — prefill builds the cache, decode reads it.
- [[wiki/concepts/quantization]] — KV quantization shrinks the cache.
- [[wiki/concepts/inference-engine]] — the cache accountant.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
