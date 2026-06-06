---
type: entity
title: ExLlamaV3
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [ExLlamaV3, exllamav3, EXL3]
tags: [inference-engine, local-ai, llm, cuda, quantization, moe, open-source]
---

# ExLlamaV3

> The successor to [[wiki/entities/exllamav2|ExLlamaV2]], extending toward multi-GPU and MoE-local inference on consumer hardware.

## Profile

ExLlamaV3 extends [[wiki/entities/exllamav2|ExLlamaV2]] toward multi-GPU and mixture-of-experts (MoE) inference on consumer hardware. It introduces the EXL3 quantization format based on QTIP and offers flexible tensor-parallel and expert-parallel inference, an OpenAI-compatible server through TabbyAPI, continuous dynamic batching, and multimodal support. It is compelling for setups with two to four-plus consumer NVIDIA GPUs or local MoE workloads, though some models do not support its tensor or expert parallelism. It appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Key facts

- **Quantization format**: adds the EXL3 format based on QTIP (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Features**: flexible tensor-parallel and expert-parallel inference for consumer hardware, an OpenAI-compatible server through TabbyAPI, continuous dynamic batching, and multimodal support ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Best fit**: 2-4+ consumer NVIDIA GPUs or local MoE ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Compelling for multi-GPU or local-MoE consumer setups, but some models do not support tensor or expert parallelism in it — noted in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — extends ExLlamaV2 toward multi-GPU and MoE-local inference on consumer hardware.

## Related entities

- [[wiki/entities/exllamav2]] — the predecessor engine that ExLlamaV3 extends.

## Related concepts

- 
