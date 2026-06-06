---
type: source
title: Inference Engines for LLMs & Local AI Hardware (2026 Edition)
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/TheAhmadOsman/status/2057183854444843202
source_type: x-thread
author: Ahmad Osman (@TheAhmadOsman)
source_date: 2026-05-20
raw_path: raw/Inference Engines for LLMs & Local AI Hardware (2026 Edition).md
content_status: substantive-verbatim
tags: [inference-engines, llm, local-ai-hardware, self-hosted-llm, quantization, kv-cache, vllm, llama-cpp, gpu]
---

# Inference Engines for LLMs & Local AI Hardware (2026 Edition)

> Part 3 of Ahmad Osman's self-hosted-LLM / local-AI series, arguing that the inference engine is the **software layer** that turns hardware into usable inference — and that you pick hardware + workload shape + serving model *first*, and the engine follows.

## TL;DR

Ahmad Osman's central thesis: *"You don't pick an inference engine first. You pick a hardware strategy, a workload shape, and a serving model. The engine follows."* The guide catalogs the major LLM inference engines as four families — portable local runtimes (llama.cpp, MLC LLM, ONNX Runtime GenAI, OpenVINO), Apple/unified-memory runtimes (MLX/MLX-LM), consumer CUDA quant engines (ExLlamaV2/V3), and production serving engines (vLLM, SGLang, TensorRT-LLM, TGI, LMDeploy) — plus orchestration layers like NVIDIA Dynamo. The recurring principle: **inference performance is memory movement plus scheduling**, with VRAM determining *fit* and memory bandwidth determining decode *speed*. It closes with a one-page decision guide, hardware-strategy recipes, a rigorous benchmarking checklist, and 10 questions to answer before choosing an engine.

## Key takeaways

- **The engine follows the hardware, not the reverse.** The choice is downstream of memory hierarchy, interconnect, quantization format, latency/throughput targets, model architecture, and operational maturity — not a first-class decision.
- **Inference has two phases with opposite bottlenecks.** *Prefill* (reads prompt, builds KV cache) is compute-intensive; *decode* (generates one token at a time) is memory-bandwidth-bound. Decode speed tracks memory bandwidth more than peak compute.
- **The workload-shape matrix predicts the bottleneck.** Short prompt/long answer → decode (bandwidth + batching); long prompt/short answer → prefill (attention kernels + chunked prefill); many users → scheduler quality; long context → KV cache (paged attention, KV quant, offload); MoE → expert routing/parallelism; multi-node → interconnect.
- **Five real bottlenecks:** (1) memory bandwidth not just VRAM size, (2) KV cache growth with batch×context, (3) interconnect cost once a model crosses GPU boundaries, (4) scheduler quality, (5) runtime overhead (CUDA graphs, kernel fusion, tokenizer, HTTP, LoRA switching, structured decoding).
- **Fit is not speed; capacity is not bandwidth.** Apple M3 Ultra offers up to 819 GB/s unified-memory bandwidth; NVIDIA H100 SXM lists 3.35 TB/s. Unified memory lets you *fit* models that wouldn't fit in consumer VRAM; HBM lets you *serve* them faster when they fit.
- **One-page decision guide:** laptop/edge/odd hardware → llama.cpp; Mac-first → MLX/MLX-LM; single RTX local → ExLlamaV2; 2-4+ NVIDIA GPUs → ExLlamaV3; general production serving → vLLM; long-context/MoE/routing → SGLang; NVIDIA max performance → TensorRT-LLM; cluster orchestration → NVIDIA Dynamo.
- **llama.cpp is the portability king** — runs on Apple Silicon (NEON/Accelerate/Metal), x86 (AVX/AMX), RISC-V, CUDA, AMD HIP, MUSA, Vulkan, SYCL, CPU+GPU hybrid offload. Its llama-server is OpenAI- and Anthropic-Messages-compatible. But its RPC multi-node backend is documented as proof-of-concept, fragile, and insecure.
- **MLX is the Apple Silicon weapon** but slower. Unified memory means MLX arrays live in one shared pool; the question shifts from "does it fit in VRAM?" to "does it fit in memory, and can the memory feed the GPU fast enough?" MLX-LM's server is explicitly not recommended for production.
- **ExLlamaV2/V3 make consumer NVIDIA cards punch above their weight.** V2 = local CUDA quant engine for one RTX 3090/4090/5090 (EXL2 format). V3 extends to multi-GPU + MoE-local with the EXL3 format (QTIP-based), tensor/expert parallelism, and TabbyAPI's OpenAI-compatible server.
- **vLLM is the default open-source production server** — PagedAttention KV management, continuous batching, chunked prefill, prefix caching, broad quantization (FP8/MXFP4/NVFP4/INT8/INT4/GPTQ/AWQ/GGUF), all parallelism modes, OpenAI + Anthropic Messages APIs. The trap: it doesn't remove the need for systems thinking.
- **SGLang is vLLM's systems-brained cousin** for ugly workloads — RadixAttention prefix caching plus prefill-decode disaggregation that splits compute-heavy prefill from memory-heavy decode into specialized instances, preventing long prefill batches from spiking decode latency.
- **TensorRT-LLM is NVIDIA-max-performance, not portable.** B200 loads FP4 weights with optimized kernels; H100+ FP8 can double performance and halve memory vs 16-bit. Awkward for AMD/Apple/Intel, fast-changing models, and small local setups.
- **The rest of the field:** TGI (HF production server), MLC LLM (compiler-first, ship-everywhere incl. browser/mobile), ONNX Runtime GenAI (powers Foundry Local / Windows ML / VS Code AI Toolkit), OpenVINO GenAI (Intel), LMDeploy (CUDA alternative to vLLM/SGLang/TRT-LLM), NVIDIA Dynamo (distributed orchestration above engines).
- **Explicit verdict: "DO NOT USE Ollama"** for production — and llama.cpp/Ollama should not be used on multi-GPU setups (use vLLM or ExLlamaV2 instead).
- **Good benchmarks specify model + weights + engine + hardware + workload + metrics** (TTFT, TPOT, p50/p95/p99, tok/s, req/s, KV cache hit rate, cost per 1M tokens). *"I got 180 tok/s"* is a bad benchmark. 10 benchmarking rules: never compare on single-user tok/s, test realistic concurrency, separate prefill from decode, track tails, etc.
- **Common mistakes:** choosing by VRAM alone, tensor parallelism on weak interconnect (test pipeline parallelism without NVLink), ignoring KV cache, treating local engines as production servers, assuming quantization formats are portable, ignoring model architecture, trusting benchmark charts without workload shape.

## Notable quotes

> "You don't pick an inference engine first. You pick a hardware strategy, a workload shape, and a serving model. The engine follows."

> "The inference engine is not 'the model.' It is the traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, API surface, and sometimes the deployment framework."

> "The recurring theme: inference performance is memory movement plus scheduling."

> "VRAM determines fit. Bandwidth determines decode speed. ... Fit is not speed. Capacity is not bandwidth."

> "Note: DO NOT USE Ollama."

## Notes

- This is the most technically deep hardware/serving source in the wiki to date. It complements the wiki's heavy lean toward *application-layer* AI (agents, Claude Code, services-as-software) by anchoring the *infrastructure layer* underneath self-hosted models. For Godwin's products — particularly [[wiki/projects/vedge|Vedge]] (healthcare, PHI, on-prem/data-residency pressure) and [[wiki/projects/kivora|Kivora]] (GRC) — the "can we serve open models privately?" question maps directly onto this guide's decision tree.
- The four-family taxonomy (portable local / Apple-unified / consumer-CUDA-quant / production-serving) is a clean mental model worth filing as its own concept page. Likewise the prefill-vs-decode distinction is the load-bearing primitive that explains nearly every other recommendation.
- The source is **Part 3** of a series; Parts 1 (GPU Memory Math for LLMs) and 2 (Memory Bandwidth for Local AI Hardware) are referenced but not ingested. Flagged as candidate ingests to complete the trilogy.
- Several existing wiki entities appear here in a *different* context than how they were first filed: `apple`, `nvidia`, `huggingface`, `ollama`, `openai`, `mistral-ai` were ingested as design-system brand stubs. This source gives them substantive hardware/AI-infrastructure facts. The "DO NOT USE Ollama" verdict is a notable hard claim about an existing entity.
- Some product version names in the source (e.g. "Qwen 3.6 27B", "Gemma 4 26B-A4B") reflect the source's 2026 timeframe; recorded verbatim, not independently verified.
- The "DO NOT use with Multi-GPUs" link points to the author's own blog (ahmadosman.com) — Ahmad Osman appears to be an independent self-hosted-LLM educator/blogger; no org affiliation stated in the source.

## Mentioned entities

- [[wiki/entities/ahmad-osman]] — author; self-hosted-LLM / local-AI educator; runs the multi-part series at ahmadosman.com.
- [[wiki/entities/llama-cpp]] — the portability-king local runtime (GGUF, hybrid CPU+GPU offload).
- [[wiki/entities/mlx]] — Apple's array framework for Apple Silicon; basis for MLX-LM.
- [[wiki/entities/mlx-lm]] — the LLM package built on MLX; HF Hub integration, quant, LoRA, distributed inference.
- [[wiki/entities/exllamav2]] — local CUDA quant engine for single consumer RTX cards (EXL2 format).
- [[wiki/entities/exllamav3]] — multi-GPU + MoE-local extension; EXL3/QTIP format, TabbyAPI server.
- [[wiki/entities/vllm]] — default open-source production serving engine (PagedAttention).
- [[wiki/entities/sglang]] — systems-brained serving engine (RadixAttention + prefill-decode disaggregation).
- [[wiki/entities/tensorrt-llm]] — NVIDIA-max-performance serving stack.
- [[wiki/entities/tgi]] — Hugging Face Text Generation Inference production server.
- [[wiki/entities/mlc-llm]] — compiler-first universal deployment engine (browser/mobile/native).
- [[wiki/entities/onnx-runtime-genai]] — generative loop over ONNX Runtime; powers Foundry Local / Windows ML.
- [[wiki/entities/openvino]] — Intel-optimized inference (Xeon/Arc/Core Ultra/NPU).
- [[wiki/entities/lmdeploy]] — CUDA toolkit (TurboMind + PyTorch backends).
- [[wiki/entities/nvidia-dynamo]] — distributed orchestration layer above engines.
- [[wiki/entities/ollama]] — local runner the source explicitly advises against for production/multi-GPU.
- [[wiki/entities/lm-studio]] — local-AI convenience GUI named in the final map.
- [[wiki/entities/harbor]] — local-AI convenience tooling (av/harbor) named in the final map.
- [[wiki/entities/tabbyapi]] — OpenAI-compatible server fronting ExLlamaV3.
- [[wiki/entities/nvidia]] — H100/H200/B200/GB200/GB300 datacenter GPUs; CUDA/NVLink/NVSwitch; Dynamo/Triton.
- [[wiki/entities/apple]] — Apple Silicon unified memory (M3 Ultra 819 GB/s); MLX origin.
- [[wiki/entities/huggingface]] — TGI maintainer; MLX-LM Hub integration; model ecosystem.
- [[wiki/entities/openai]] — OpenAI-compatible API surface is the de-facto serving interface across engines.
- [[wiki/entities/anthropic]] — Anthropic Messages API compatibility supported by llama.cpp and vLLM.
- [[wiki/entities/intel]] — Xeon/Arc/Core Ultra/NPU target for OpenVINO.
- [[wiki/entities/amd]] — ROCm/HIP support; MI300/MI325/MI350/MI355 datacenter GPUs.

## Related concepts

- [[wiki/concepts/inference-engine]] — the central subject; the software layer turning hardware into usable inference.
- [[wiki/concepts/self-hosted-llm]] — the broader practice this guide serves (Part 3 of a local-AI series).
- [[wiki/concepts/prefill-vs-decode]] — the two-phase workload distinction that predicts every bottleneck.
- [[wiki/concepts/kv-cache]] — grows with batch×context; the limiting factor at long context / high concurrency.
- [[wiki/concepts/paged-attention]] — partitions KV cache into blocks to cut fragmentation (vLLM origin).
- [[wiki/concepts/memory-bandwidth]] — determines decode speed; the under-appreciated hardware metric.
- [[wiki/concepts/unified-memory]] — Apple Silicon's shared CPU/GPU pool; capacity superpower with bandwidth tradeoff.
- [[wiki/concepts/quantization]] — low-bit weight formats (GGUF/EXL2/EXL3/AWQ/GPTQ/FP8/FP4); non-portable across engines.
- [[wiki/concepts/continuous-batching]] — scheduler technique for serving many concurrent users.
- [[wiki/concepts/speculative-decoding]] — drafts cheap tokens, verifies in parallel.
- [[wiki/concepts/tensor-parallelism]] — splits a model across GPUs; needs strong interconnect (NVLink).
- [[wiki/concepts/mixture-of-experts]] — MoE routing stresses expert parallelism and all-to-all interconnect.
- [[wiki/concepts/llm-serving-benchmarking]] — the rigorous what-to-measure checklist (TTFT/TPOT/tails/cost).

## Related sources

- *(Parts 1 & 2 of Ahmad Osman's series — GPU Memory Math, Memory Bandwidth for Local AI Hardware — not yet ingested; candidate companions.)*
