---
type: entity
title: vLLM
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [vLLM, vllm]
tags: [inference-engine, llm, serving, production, paged-attention, open-source]
---

# vLLM

> The default open-source production serving engine for LLMs — the first engine most teams should evaluate.

## Profile

vLLM is an open-source, high-throughput LLM serving engine built around PagedAttention-based KV memory management. It supports continuous batching, chunked prefill, prefix caching, speculative decoding, and extensive quantization, along with multiple parallelism strategies and OpenAI- and Anthropic-compatible APIs across a wide range of hardware. Positioned as the default production serving engine and the first one most teams should evaluate, it also figures in scaled reinforcement-learning systems as the inference component for distributed rollout generation. It appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] and [[wiki/sources/athletickoder-building-agents-first-principles]].

## Key facts

- **Core features**: PagedAttention-based KV memory management, continuous batching, chunked prefill, prefix caching, CUDA/HIP graphs, speculative decoding, torch.compile, and disaggregated prefill/decode/encode (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Quantization**: FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, GGUF ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Parallelism and APIs**: tensor/pipeline/data/expert/context parallelism; OpenAI-compatible and Anthropic Messages APIs; gRPC; multi-LoRA ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Hardware**: NVIDIA, AMD, x86/ARM/PowerPC CPUs, plus plugins for TPUs, Gaudi, Ascend, Apple Silicon ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- The default open-source production serving engine; the first engine most teams should evaluate — argued in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- Its docs note multi-node deployments typically use Ray, and that without NVLink, pipeline parallelism may beat tensor parallelism ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- Cited as part of what "real implementations add" to the bare RL loop: "distributed rollout generation, vLLM inference, caching, and many stability tricks," and listed among the real engineering concerns of scaled RL trainers ("vLLM serving") — [[wiki/sources/athletickoder-building-agents-first-principles]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — the default open-source production serving engine; first engine most teams should evaluate.
- [[wiki/sources/athletickoder-building-agents-first-principles]] — high-throughput inference engine referenced for distributed RL rollout generation in real trainers.

## Related entities

- [[wiki/entities/llama-cpp]] — portability runtime recommended over for offline/edge; vLLM preferred for multi-GPU production.
- [[wiki/entities/exllamav2]] — single-GPU consumer engine alternative.

## Related concepts

- 
