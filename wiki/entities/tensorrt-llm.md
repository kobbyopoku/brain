---
type: entity
title: TensorRT-LLM
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [TensorRT-LLM, TensorRT LLM]
tags: [inference-engine, llm-serving, nvidia, local-ai]
---

# TensorRT-LLM

> NVIDIA's maximum-performance LLM serving stack, trading portability for performance.

## Profile

TensorRT-LLM is NVIDIA's high-performance LLM serving stack. It provides Python APIs for building TensorRT engines along with Python and C++ runtimes, custom kernels, and advanced serving features, and integrates with NVIDIA's Dynamo and Triton Inference Server. It is optimized for NVIDIA GPUs and the latest low-precision formats, at the cost of portability to non-NVIDIA hardware.

## Key facts

- **APIs and runtimes**: provides Python APIs to build TensorRT engines plus Python and C++ runtimes (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Features**: custom kernels for attention, GEMMs, and MoE; prefill-decode disaggregation; Wide Expert Parallelism; speculative decoding (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Integrations**: integrated with NVIDIA Dynamo and Triton Inference Server (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Precision**: B200 GPUs can load FP4 weights with optimized kernels; H100 and later support FP8 that can double performance and halve memory versus 16-bit with minimal accuracy loss (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Limitations**: awkward for AMD/Apple/Intel portability, fast-changing experimental models, and small local setups (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Trades portability for performance — optimized for NVIDIA hardware at the expense of cross-vendor support, per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — NVIDIA-max-performance serving stack; trades portability for performance.

## Related entities

- [[wiki/entities/sglang|SGLang]] — peer serving stack with overlapping features.
- [[wiki/entities/vllm|vLLM]] — peer inference/serving engine.

## Related concepts

