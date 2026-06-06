---
type: entity
title: llama.cpp
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [llama-cpp, llama.cpp, llama-server]
tags: [inference-engine, local-ai, llm, gguf, open-source]
---

# llama.cpp

> A portable, cross-platform local LLM inference runtime — the answer when target hardware is weird, constrained, offline, CPU-heavy, or edge-oriented.

## Profile

llama.cpp is a local inference engine for large language models that prioritizes portability across an exceptionally broad range of hardware backends. It runs on Apple Silicon, x86, RISC-V, NVIDIA CUDA, AMD, and several other targets, and supports CPU+GPU hybrid offload, making it the go-to runtime for constrained, offline, or edge deployments. Its bundled `llama-server` exposes OpenAI- and Anthropic-compatible APIs alongside features such as continuous batching, multimodal support, and speculative decoding. It is, however, explicitly not intended for serious multi-node production serving. It appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Key facts

- **Hardware backends**: Apple Silicon via ARM NEON/Accelerate/Metal; x86 via AVX/AVX2/AVX512/AMX; RISC-V; CUDA; AMD via HIP; MUSA; Vulkan; SYCL; and CPU+GPU hybrid offload (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **llama-server features**: OpenAI-compatible routes, Anthropic Messages API compatibility, reranking, continuous batching, multimodal support, JSON schema constraints, function calling, speculative decoding, and a web UI ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Format**: associated with GGUF model files ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Recommended for portability, offline operation, GGUF, or hybrid offload — argued in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- Not suitable for serious multi-node production serving; its RPC backend is documented as proof-of-concept, fragile, and insecure ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- Should not be used on multi-GPU setups; vLLM or ExLlamaV2 are preferred there ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — the portability-king local runtime; the answer when hardware is weird, constrained, offline, CPU-heavy, or edge-oriented.

## Related entities

- [[wiki/entities/vllm]] — production serving engine recommended over llama.cpp for multi-GPU.
- [[wiki/entities/exllamav2]] — single-GPU CUDA engine recommended over llama.cpp on consumer NVIDIA cards.

## Related concepts

- 
