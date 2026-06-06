---
type: entity
title: SGLang
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [SGLang]
tags: [inference-engine, llm-serving, local-ai]
---

# SGLang

> An LLM inference and serving engine, characterized as vLLM's systems-brained cousin for difficult serving workloads.

## Profile

SGLang is an LLM inference engine positioned for "ugly" serving workloads — structured outputs, long context, mixture-of-experts (MoE), and routing. It emphasizes systems-level optimizations including prefix caching, disaggregated prefill/decode, and broad hardware support, making it a peer to [[wiki/entities/vllm|vLLM]] for production serving.

## Key facts

- **Features**: offers RadixAttention prefix caching, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, and tensor/pipeline/expert/data parallelism (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Hardware support**: supports NVIDIA, AMD, Intel Xeon, Google TPUs, Ascend NPUs, and more (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Prefill-decode disaggregation**: separates compute-intensive prefill from memory-intensive decode into specialized instances, transferring KV cache between them to prevent long prefill batches from spiking token latency (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Targets difficult serving workloads — structured outputs, long context, MoE, and routing — as its differentiator versus general-purpose serving engines, per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — characterized as vLLM's systems-brained cousin for ugly serving workloads (structured outputs, long context, MoE, routing).

## Related entities

- [[wiki/entities/vllm|vLLM]] — peer inference/serving engine.
- [[wiki/entities/tensorrt-llm|TensorRT-LLM]] — peer serving stack with overlapping features (disaggregation, speculative decoding).

## Related concepts

