---
type: concept
title: PagedAttention
created: 2026-06-06
updated: 2026-06-06
aliases: [paged attention]
tags: [local-ai, llm-serving, inference, memory]
---

# PagedAttention

> A KV-cache management technique that partitions the cache into fixed-size blocks to reduce memory fragmentation and support larger batches; originated in vLLM.

## Definition

PagedAttention partitions the [[wiki/concepts/kv-cache]] into blocks (analogous to OS memory paging) rather than allocating it as one contiguous region. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], this cuts fragmentation and enables larger batch sizes. It originated in vLLM and has been adopted broadly.

## Why it matters

PagedAttention is a concrete answer to the KV-cache memory problem — it is part of why production-serving [[wiki/concepts/inference-engine]] choices achieve high concurrency. Its broad adoption makes it a near-standard primitive in modern serving stacks.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as partitioning the KV cache into blocks to cut fragmentation and support larger batches; originated in vLLM and adopted broadly (SGLang, OpenVINO GenAI, ExLlamaV2).

## Sub-claims and details

- It partitions the KV cache into blocks to reduce fragmentation and allow larger batches. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- It originated in vLLM. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Adopted by SGLang, OpenVINO GenAI, and ExLlamaV2. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/kv-cache]] — what PagedAttention manages.
- [[wiki/concepts/inference-engine]] — engines that implement it.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
