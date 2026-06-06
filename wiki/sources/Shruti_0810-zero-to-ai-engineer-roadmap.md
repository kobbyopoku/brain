---
type: source
title: Shruti — Zero to AI Engineer — The Roadmap Nobody Explains Properly
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/Shruti_0810/status/2055676059480395990
source_type: x-thread
author: Shruti (@Shruti_0810)
source_date: 2026-05-16
raw_path: raw/Zero to AI Engineer — The Roadmap Nobody Explains Properly.md
content_status: substantive-verbatim
tags: [ai-engineering, roadmap, learning-path, free-resources, deep-learning, rag, ai-agents, mcp-server, llmops, local-models]
---

# Shruti — Zero to AI Engineer — The Roadmap Nobody Explains Properly

> A ~14-week free-resource learning path from absolute beginner to "production-grade AI systems," whose load-bearing claim is that **the best AI education is already free and almost nobody follows the resources in the correct order** — so people "jump into agents before understanding transformers, try building RAG apps without understanding embeddings, or copy-paste LangChain tutorials without knowing what's happening underneath."

## TL;DR

Shruti argues the bottleneck to becoming an AI engineer is not access to material (the free curricula from OpenAI, Anthropic, Google, NVIDIA, Microsoft + open-source repos already beat most paid bootcamps) but **sequencing** plus **building instead of consuming**. The roadmap runs: environment setup (Python 3.11+, VS Code, GitHub, Obsidian, Ollama) → AI fundamentals (Google AI cert + Anthropic AI Fluency + Microsoft generative-ai-for-beginners) → ML foundations (Microsoft ML-For-Beginners + IBM ML cert + mlabonne/llm-course for math) → deep learning (Karpathy's Neural Networks: Zero to Hero, built from scratch) → modern LLM engineering (RAG/fine-tuning/LoRA/QLoRA/quantization/vector DBs + prompt engineering from frontier labs) → AI agents (Microsoft ai-agents-for-beginners + Anthropic MCP courses) → deployment + evaluation + portfolio (DeepEval/RAGAS/LLM-as-a-Judge + Hugging Face Spaces/Gradio/Streamlit/Vercel). Closing thesis: *"the people who actually become AI engineers aren't the ones bookmarking 200 tutorials — they're the ones opening a terminal, breaking things, fixing them, deploying projects."*

## Key takeaways

- **The scarce resource is order, not access.** "The best AI education on the internet is already free" — the failure mode is following good resources in the wrong sequence (agents before transformers, RAG before embeddings, LangChain before fundamentals).
- **Targets ~14 weeks** from absolute beginner to building production-grade AI systems, framed as a "practical system" rather than "50 resources you'll never open."
- **The goal is understanding, not tool-use**: "not to become someone who simply uses AI tools" but to understand how modern AI works, build with it, and deploy systems that solve real problems.
- **Environment first**: Python 3.11+, [[wiki/entities/vs-code|VS Code]], [[wiki/entities/github|GitHub]], [[wiki/entities/obsidian|Obsidian]], and [[wiki/entities/ollama|Ollama]]. Ollama is singled out as "especially important" because running models locally becomes valuable later for LLMs, embeddings, quantization, and agents.
- **Free-account stack**: Anthropic Academy (`anthropic.skilljar.com`), OpenAI Academy, Google AI (`grow.google/ai`), Coursera. Trick: on Coursera always **"Audit this course"** — the full material is usually free.
- **Phase 1 — AI fundamentals**: Google's AI Professional Certificate (workflows/prompting/use-cases without front-loading math) → Anthropic Academy's **AI Fluency** course → `microsoft/generative-ai-for-beginners` (prompts, transformers, embeddings, chat apps, LLM production behavior). Phase goal: explain tokens, embeddings, transformers, and context windows in plain English.
- **Phase 2 — ML foundations** is "where most people quit" and "where beginners separate from future AI engineers." Resources: `microsoft/ML-For-Beginners` (regression/classification/clustering/evaluation/overfitting/gradient descent), IBM's ML Professional Certificate (audit mode), and `mlabonne/llm-course` for the *exact* linear algebra/calculus/probability needed (vs unnecessary academic theory). Deliverable: push at least one ML project to GitHub.
- **Phase 3 — Deep learning**: Karpathy's **Neural Networks: Zero to Hero** (`karpathy.ai/zero-to-hero.html` + `karpathy/nn-zero-to-hero`) is called "one of the greatest AI learning resources ever created" — it teaches NNs from scratch in raw Python/math (backprop, activations, tokenization, transformers, attention). Run `ollama run llama3` alongside to bridge theory and real systems.
- **Phase 4 — Modern LLM engineering**: RAG, fine-tuning, LoRA, QLoRA, quantization, vector databases, evaluation start "making sense." `mlabonne/llm-course` is called "the closest thing the AI world currently has to a complete open-source LLM engineering curriculum." Study prompt engineering directly from frontier labs (OpenAI Academy + Anthropic docs), because Anthropic "explains prompting like an engineering discipline rather than 'magic words.'" Project: a RAG system over personal notes using ChromaDB or LanceDB ("a searchable second brain").
- **Phase 5 — AI agents** ("changing the industry fastest"): `microsoft/ai-agents-for-beginners` (tool use, orchestration, memory, workflows, multi-agent) + Anthropic's MCP courses, because **MCP is "rapidly becoming the standard way AI systems connect to tools, APIs, and external environments."** Impressive projects here: autonomous research agents, AI file systems, browser agents, workflow automations, local assistants, memory-enabled systems.
- **Phase 6 — Deployment + evaluation + portfolio** is "the area most tutorials completely ignore." "A deployed AI system without evaluation is basically a hallucination machine waiting to fail." Evaluation tools: DeepEval, RAGAS, LLM-as-a-Judge. Deploy via Hugging Face Spaces / Gradio / Streamlit / Vercel. Every serious project ships evaluation + safety checks + architecture diagrams + GitHub documentation + public demos.
- **GitHub > résumé** in modern AI hiring — toy projects matter "not because recruiters care" but because building is the fastest way to learn why models fail.
- **The central anti-pattern is consuming without building**: "The people who actually become AI engineers aren't the ones bookmarking 200 tutorials. They're the ones opening a terminal, breaking things, fixing them, deploying projects, and repeating that process."

## Notable quotes

> "The best AI education on the internet is already free. Not beginner fluff. Not 'What is ChatGPT?' videos. Actual engineering knowledge from the companies building modern AI systems."

> "Almost nobody follows the resources in the correct order. That's why people jump into agents before understanding transformers, try building RAG apps without understanding embeddings, or copy-paste LangChain tutorials without knowing what's happening underneath."

> "A deployed AI system without evaluation is basically a hallucination machine waiting to fail."

> "In modern AI hiring, GitHub often matters more than résumés."

> "The people who actually become AI engineers aren't the ones bookmarking 200 tutorials. They're the ones opening a terminal, breaking things, fixing them, deploying projects, and repeating that process until the systems finally make sense."

## Notes

- **This is Shruti's second source in the wiki** (first: [[wiki/sources/Shruti_0810-self-improving-obsidian|the self-improving Obsidian vault]], the 4th wild citation of [[llm-wiki-pattern]]). The same Obsidian-centric instinct shows up here: Obsidian is in the day-1 environment stack, and the Phase-4 flagship project is a *RAG over personal notes* — i.e. a "searchable second brain." The two sources rhyme but this one is a curriculum, not an architecture.
- **Near-twin of [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026|Tech With Tim's AI-engineer roadmap]]** (ingested the same day, 2026-06-06). Both are "build in the right order" learning paths covering Python → LLM fundamentals → frameworks/RAG → agents → deployment. Key contrast: **Tim's is tooling-first and production/LLMOps-weighted**; **Shruti's is free-resource-first and theory-grounded** (she insists on building neural nets *from scratch* via Karpathy before touching frameworks, where Tim front-loads LangChain/LangGraph). Shruti also uniquely names *specific GitHub curricula* (the Microsoft `*-for-beginners` trilogy, `mlabonne/llm-course`, `karpathy/nn-zero-to-hero`) as the spine of the path.
- Also a sibling to [[wiki/sources/e_opore-system-design-roadmap|e_opore's system-design roadmap]] (career-roadmap genre) — but e_opore is infra/system-design-first; Shruti is model/LLM-internals-first.
- **Karpathy appears here in a different role than usual.** In this wiki he is the source of the [[llm-wiki-pattern]]; here he is cited as the author of *Neural Networks: Zero to Hero*, the deep-learning-from-scratch curriculum. Worth noting on his entity page: the wiki now references two distinct Karpathy artifacts.
- The "evaluation is non-optional" framing (DeepEval / RAGAS / LLM-as-a-Judge) is the same discipline as Tim's LLMOps stage and connects to the wiki's [[wiki/concepts/reliability-decay-math|reliability-decay-math]] — an unevaluated AI system is the failure mode both roadmaps warn against. Suggests a future `llm-evaluation` concept page (currently no page covers DeepEval/RAGAS/LLM-as-a-Judge directly).
- Several named items are wiki-novel and warrant stubs: **VS Code**, **Python**, **Coursera**, **ChromaDB**, **LanceDB**, **Gradio**, **Streamlit**, **Hugging Face Spaces**, **DeepEval**, **RAGAS**, **mlabonne** (Maxime Labonne, `llm-course` author), **LoRA**, **QLoRA**, **quantization**. Citable facts on each are thin (role-in-roadmap only) — most overlap with the parallel Tech-With-Tim ingest, which already created or queued `vs-code`, `python`, `git`, etc.
- **Microsoft and Google appear as *curriculum publishers* here** (generative-ai-for-beginners, ML-For-Beginners, ai-agents-for-beginners; Google AI Professional Certificate) — distinct from their usual product-vendor framing. NVIDIA and Microsoft are named in the intro as frontier-AI knowledge sources but no specific NVIDIA resource is given (intro-only mention).
- **Concept overlap with the wiki**: RAG and MCP-server already have pages; this source adds a *beginner-ordering* framing of both. `quantization`, `fine-tuning`, `embeddings`, `vector-database`, `deep-learning`, `machine-learning`, `prompt-engineering` are concept candidates (the latter several already queued via the Tech-With-Tim ingest).
- Squarely inside Godwin's interest cluster (AI products + agentic architecture + production AI). Useful as a reference onboarding curriculum for engineers across ROAM Labs products, and the "evaluation before deploy" rule maps directly onto [[wiki/projects/vedge|Vedge]]/[[wiki/projects/kivora|Kivora]] agent QA discipline.

## Mentioned entities

- [[wiki/entities/Shruti_0810|Shruti]] — author; 2nd source in the wiki (after the self-improving Obsidian vault).
- [[wiki/entities/andrej-karpathy]] — cited as author of *Neural Networks: Zero to Hero*, the Phase-3 deep-learning-from-scratch curriculum (`nn-zero-to-hero`).
- [[wiki/entities/microsoft]] — publisher of the `generative-ai-for-beginners`, `ML-For-Beginners`, and `ai-agents-for-beginners` GitHub curricula.
- [[wiki/entities/google]] — Google AI Professional Certificate (Phase 1) + Google AI portal (`grow.google/ai`).
- [[wiki/entities/openai]] — OpenAI Academy (frontier-lab prompt-engineering resource) + named as frontier-AI knowledge source.
- [[wiki/entities/anthropic]] — Anthropic Academy (AI Fluency course), MCP courses, and prompt-engineering docs ("prompting as an engineering discipline").
- [[wiki/entities/nvidia]] — named in the intro as a frontier-AI engineering-knowledge source (no specific resource given).
- [[wiki/entities/ibm]] — IBM Machine Learning Professional Certificate (Coursera, audit mode), Phase 2.
- [[wiki/entities/ollama]] — local-model runner; day-1 environment install; `ollama run llama3` used to bridge theory and real systems.
- [[wiki/entities/huggingface]] — Hugging Face Spaces named as a deployment target (Phase 6).
- [[wiki/entities/github]] — environment install + portfolio surface ("GitHub matters more than résumés").
- [[wiki/entities/obsidian]] — day-1 environment install; the Phase-4 RAG-over-notes "second brain" project target.
- [[wiki/entities/vercel]] — deployment target (Phase 6).
- [[wiki/entities/model-context-protocol]] — Anthropic's MCP, "rapidly becoming the standard way AI systems connect to tools, APIs, and external environments" (Phase 5).
- [[wiki/entities/skilljar]] — Anthropic Academy delivery surface (`anthropic.skilljar.com`).
- [[wiki/entities/vs-code]] — code editor in the day-1 environment stack.
- [[wiki/entities/python]] — Python 3.11+; base language of the entire path.
- [[wiki/entities/coursera]] — course platform; "Audit this course" unlocks free material (IBM ML cert).
- [[wiki/entities/mlabonne]] — Maxime Labonne; author of `mlabonne/llm-course`, the math-foundations + LLM-engineering curriculum spine of Phases 2 and 4.
- [[wiki/entities/chromadb]] — vector store option for the Phase-4 RAG-over-notes project.
- [[wiki/entities/lancedb]] — vector store option for the Phase-4 RAG-over-notes project.
- [[wiki/entities/gradio]] — demo/deployment UI framework (Phase 6).
- [[wiki/entities/streamlit]] — demo/deployment UI framework (Phase 6).
- [[wiki/entities/hugging-face-spaces]] — hosted-demo deployment target (Phase 6).
- [[wiki/entities/deepeval]] — LLM evaluation framework (Phase 6).
- [[wiki/entities/ragas]] — RAG evaluation framework (Phase 6).
- [[wiki/entities/lora]] — parameter-efficient fine-tuning technique (Phase 4).
- [[wiki/entities/qlora]] — quantized LoRA fine-tuning technique (Phase 4).

## Related concepts

- [[wiki/concepts/ai-engineering]] — the discipline this entire source sequences as a learning path.
- [[wiki/concepts/retrieval-augmented-generation]] — Phase 4 + the flagship Phase-4 project (RAG over personal notes); this source frames RAG as requiring embeddings understanding first.
- [[wiki/concepts/mcp-server]] — Phase 5; Anthropic MCP courses; "the standard way AI systems connect to tools."
- [[wiki/concepts/embeddings]] — explicitly named as the prerequisite people skip before building RAG apps.
- [[wiki/concepts/vector-database]] — Phase 4 (ChromaDB / LanceDB).
- [[wiki/concepts/context-window]] — Phase-1 plain-English-explanation target (alongside tokens/embeddings/transformers).
- [[wiki/concepts/fine-tuning]] — Phase 4 (with LoRA/QLoRA).
- [[wiki/concepts/quantization]] — Phase 4; also cited as a reason Ollama/local-models matter.
- [[wiki/concepts/prompt-engineering]] — Phase 4, studied from frontier labs as "an engineering discipline rather than 'magic words.'"
- [[wiki/concepts/llm-evaluation]] — *(candidate)* Phase 6; DeepEval / RAGAS / LLM-as-a-Judge; "a deployed AI system without evaluation is a hallucination machine."
- [[wiki/concepts/llmops]] — Phase 6 deployment + safety-checks + monitoring discipline (shared with Tech With Tim's framing).
- [[wiki/concepts/reliability-decay-math]] — the unevaluated-system failure mode this roadmap's Phase 6 guards against.
- [[wiki/concepts/llm-wiki-pattern]] — the Phase-4 "RAG-over-notes second brain" is a structural cousin; Shruti's first source is a wild citation of the pattern.

## Related sources

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — near-twin AI-engineer roadmap ingested the same day; tooling/LLMOps-first vs Shruti's free-resource/theory-first sequencing.
- [[wiki/sources/Shruti_0810-self-improving-obsidian]] — same author's first source; self-improving Obsidian vault, 4th wild citation of the LLM Wiki pattern.
- [[wiki/sources/e_opore-system-design-roadmap]] — sibling career-roadmap source; system-design-first vs Shruti's model-internals-first.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — build-an-agent-from-scratch course; complements Phase 5 (AI agents).
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — advanced RAG critique; counterpoint to this source's beginner RAG framing.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy as the LLM-Wiki author; this source cites a different Karpathy artifact (*Neural Networks: Zero to Hero*).
