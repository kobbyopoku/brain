---
type: concept
title: Memory bandwidth
created: 2026-06-06
updated: 2026-06-06
aliases: [bandwidth]
tags: [local-ai, hardware, inference, performance]
---

# Memory bandwidth

> The rate at which a processor can move data to/from memory; it determines decode (token-generation) speed and is distinct from memory size, which determines whether a model fits.

## Definition

Memory bandwidth measures how fast data moves between compute and memory. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], it determines decode speed — distinct from VRAM/memory size, which only determines whether a model fits. The source's recurring principle: "fit is not speed, capacity is not bandwidth."

## Why it matters

Because decode is bandwidth-bound (see [[wiki/concepts/prefill-vs-decode]]), bandwidth — not capacity and not raw compute — is the dominant predictor of token-generation speed for self-hosted LLMs. It explains why a high-capacity unified-memory machine can still generate tokens slowly.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as the determinant of decode speed (distinct from VRAM size, which determines fit). It contrasts Apple M3 Ultra ~819 GB/s unified memory vs NVIDIA H100 ~3.35 TB/s HBM, and states the recurring principle "fit is not speed, capacity is not bandwidth."

## Sub-claims and details

- Bandwidth determines decode speed; memory size determines whether a model fits. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Apple M3 Ultra: ~819 GB/s of unified-memory bandwidth. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- NVIDIA H100: ~3.35 TB/s of HBM bandwidth. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Recurring principle: "fit is not speed, capacity is not bandwidth." ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/prefill-vs-decode]] — decode is the bandwidth-bound phase.
- [[wiki/concepts/unified-memory]] — high capacity, bandwidth tradeoff vs HBM.
- [[wiki/concepts/self-hosted-llm]] — bandwidth as a self-hosting constraint.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
