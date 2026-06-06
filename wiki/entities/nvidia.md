---
type: entity
title: NVIDIA
entity_type: organization
created: 2026-05-05
updated: 2026-06-06
website: https://nvidia.com
aliases: []
tags: [hardware, gpu, ai-infrastructure, design-md-available, open-design-catalog, stub]
---

# NVIDIA

> GPU computing company — chips that power most AI training. Also publishes NVIDIA NIM (model inference microservices), Nemotron (open-weight LLM family), CUDA, etc. Cataloged in [[wiki/entities/open-design|Open Design]] under Media & Consumer with a *"green-black energy, technical power aesthetic"* DESIGN.md.

## Key facts

- **Website**: https://nvidia.com
- **Open Design DESIGN.md**: `raw/open-design/design-systems/nvidia/DESIGN.md`
- **AI products**: NVIDIA NIM (containerized inference) is one of [[wiki/entities/hermes-agent|Hermes Agent]]'s supported model providers (Nemotron family).

### Datacenter GPUs and serving stack

- **Datacenter GPU classes**: H100, H200, B200, GB200, GB300 — per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **H100 SXM memory bandwidth**: 3.35 TB/s — per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **Serving stack ownership**: Owns the TensorRT-LLM stack, the [[wiki/entities/nvidia-dynamo|NVIDIA Dynamo]] orchestration layer, and Triton Inference Server — per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **Interconnect**: NVLink/NVSwitch determines whether tensor parallelism beats pipeline parallelism — per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **Knowledge source**: Listed alongside OpenAI/Anthropic/Google/Microsoft as a company providing free AI engineering knowledge — per [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]].

## Mentioned in
- [[wiki/sources/open-design-catalog]]
- [[wiki/sources/nousresearch-hermes-agent]] — NIM is a supported provider.
- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — datacenter-GPU vendor whose hardware and stack (CUDA, NVLink, Dynamo, TensorRT-LLM) anchor the production-serving recommendations.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — named in the intro as a frontier-AI knowledge source.

## Related entities
- [[wiki/entities/hermes-agent]]
- [[wiki/entities/nvidia-dynamo]] — NVIDIA's distributed serving orchestration layer.

## Related concepts
- [[design-md]]
