---
type: entity
title: ExLlamaV2
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [ExLlamaV2, exllamav2, EXL2]
tags: [inference-engine, local-ai, llm, cuda, quantization, open-source]
---

# ExLlamaV2

> A local CUDA quantization engine for single consumer NVIDIA RTX cards using the EXL2 format.

## Profile

ExLlamaV2 is a local CUDA inference and quantization engine designed to make a single consumer NVIDIA GPU punch above its weight, using the EXL2 quantized model format. It supports a range of throughput and memory features including paged attention, dynamic batching, prompt caching, and speculative decoding. Its sweet spot is a single RTX 3090/4090/5090 workstation running local coding assistants, chat, or EXL2 models. It appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], which recommends it over [[wiki/entities/llama-cpp|llama.cpp]] on consumer NVIDIA hardware.

## Key facts

- **Class**: local CUDA quantization engine designed to make a consumer NVIDIA GPU punch above its weight (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Features**: paged attention, dynamic batching, prompt caching, KV cache deduplication, batched generation, streaming, and speculative decoding ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Best fit**: one RTX 3090/4090/5090 box, local coding assistant, local chat, EXL2 quantized models, prosumer workstation use ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Recommended on single consumer NVIDIA cards over [[wiki/entities/llama-cpp|llama.cpp]] — argued in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — local CUDA quantization engine for single consumer NVIDIA RTX cards using the EXL2 format.

## Related entities

- [[wiki/entities/exllamav3]] — successor extending toward multi-GPU and MoE-local inference.
- [[wiki/entities/llama-cpp]] — portability runtime; ExLlamaV2 preferred on single consumer NVIDIA cards.

## Related concepts

- 
