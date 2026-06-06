---
type: entity
title: MLX
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [MLX, mlx]
tags: [inference-engine, local-ai, apple-silicon, array-framework, open-source]
---

# MLX

> Apple's array framework for Apple Silicon — the Mac-first ML stack and basis for MLX-LM.

## Profile

MLX is Apple's array framework built for Apple Silicon, where arrays live in unified memory and the device is chosen per operation rather than by moving arrays between separate memory spaces. Originally Mac-only, it has expanded to offer CUDA and CPU-only packages for Linux, and supports several distributed communication backends. Despite the capacity advantage of unified memory, it is generally slower than discrete-GPU CUDA engines. It is the foundation for [[wiki/entities/mlx-lm]] and appears in this wiki via [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Key facts

- **Vendor**: Apple; an array framework for Apple Silicon (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Memory model**: MLX arrays live in unified memory; the device is selected per operation rather than by moving arrays between memory spaces ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Platform reach**: no longer Mac-only — offers CUDA and CPU-only packages for Linux ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Distributed communication**: supports MPI, Ring over TCP, JACCL for RDMA over Thunderbolt, and NCCL for CUDA ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).

## Positions and claims

- Generally slower than discrete-GPU CUDA engines despite its unified-memory capacity advantage — noted in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — Apple's array framework for Apple Silicon; the Mac-first ML stack and basis for MLX-LM.

## Related entities

- [[wiki/entities/mlx-lm]] — the LLM package built on MLX.
- [[wiki/entities/apple]] — vendor of MLX.

## Related concepts

- 
