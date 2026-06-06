---
type: concept
title: Quantization
created: 2026-06-06
updated: 2026-06-06
aliases: [model quantization, low-bit quantization, weight quantization]
tags: [local-ai, llm, inference, model-formats, ai-engineering]
---

# Quantization

> Representing model weights (and sometimes activations or the KV cache) in lower-bit formats to shrink memory footprint and speed inference, at some cost to precision.

## Definition

Quantization stores model weights in low-bit numeric formats instead of full precision, reducing memory use and enabling models to run on smaller hardware. Per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]], named formats include GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4/NVFP4/MXFP4, INT8/INT4, MLX, and ONNX. Crucially, these formats are explicitly **not** interchangeable across engines.

## Why it matters

Quantization is what makes self-hosting large models feasible on consumer or unified-memory hardware, and it is tightly coupled to engine choice: the right format is the one your [[wiki/concepts/inference-engine]] has optimized kernels for. It also appears in AI-engineering curricula as a core skill for working with local models.

## Treatment across sources

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] frames it as low-bit weight formats (GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4/NVFP4/MXFP4, INT8/INT4, MLX, ONNX) that are explicitly NOT interchangeable across engines — the right format is the one your engine has optimized kernels for.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] treats it as a Phase 4 concept and cites it as a reason local models / Ollama matter (a wiki-novel concept candidate in that source).

## Sub-claims and details

- Named formats: GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4/NVFP4/MXFP4, INT8/INT4, MLX, ONNX. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- Quantization formats are not interchangeable across inference engines. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- The correct format is dictated by which engine has optimized kernels for it. ([[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]])
- In an AI-engineering roadmap, quantization sits in Phase 4 and underpins running local models via Ollama. ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]])

## Open questions and contradictions

- 

## Related concepts

- [[wiki/concepts/inference-engine]] — engines optimize kernels per format.
- [[wiki/concepts/unified-memory]] — quantized models fit large in unified memory.
- [[wiki/concepts/kv-cache]] — KV quantization is a related cache-shrinking technique.
- [[wiki/concepts/self-hosted-llm]] — quantization is core to self-hosting.

## Related entities

- 

## Mentioned in

- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]
