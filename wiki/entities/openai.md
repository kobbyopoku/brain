---
type: entity
title: OpenAI
entity_type: organization
created: 2026-05-04
updated: 2026-06-06
website: https://openai.com
aliases: []
tags: [refero-catalog, design-md-ingested, ai-research, ai-products, light-mode]
---

# OpenAI

> AI research and product company; maker of ChatGPT, GPT-4, and o-series reasoning models. Founded 2015. Sam Altman serves as CEO. Cataloged in Refero with a *"Blank page before the first word"* light-mode philosophy — pure white canvas, near-zero chromatic saturation, OpenAI Sans carrying all visual weight.

## Profile

OpenAI appears in this wiki via two paths so far. Briefly named in [[wiki/entities/sam-altman]]'s entity page (Altman is OpenAI's CEO; mentioned but not the subject of an ingested source). Now substantively present via the Refero DESIGN.md ingest, which captures the openai.com marketing site's design system.

This page is **partially substantive**: the design-system summary is detailed (DESIGN.md is itself a primary source); other dimensions (model lineup, business model, research positions, controversies) await direct primary-source ingest.

## Design system summary

- **Theme**: light — pure white background, near-zero chromatic saturation (1%), typography carries everything.
- **Philosophy**: *"Blank page before the first word — a design that treats white space as the most powerful element, reserving all color for user-generated and editorial content."*
- **Typeface**: **OpenAI Sans** (single custom typeface for entire site — nav, body, headlines, buttons, inputs). Tightly tracked at -0.03em for large display text. Weights 400/500/600. `calt` and `liga` features for text composition.
- **Type sizes**: 13 / 14 / 16 / 17 / 18 / 22 / 28 / 48 px.
- **Color palette**: black `#000000` and border-gray `#e5e7eb` on the core UI. **No accent colors, no gradients, no decorative illustration on chrome.** Color arrives only through editorial imagery — soft-focus flower macros, pastel gradient thumbnails — which feel explosive against the white canvas.
- **Shape signature**: **9999px pills** for interactive chips and inputs sit inside a layout where cards use a precise **6.08px radius** — one extreme roundness paired with one near-flat radius. Distinctive.
- **Mood**: editorial restraint; near-monastic minimalism; carved typography.

## Key facts

- **Founded**: 2015 in San Francisco.
- **CEO**: Sam Altman.
- **Notable products**: ChatGPT, GPT-4 / GPT-4o / GPT-5 family, o-series reasoning models, Sora, DALL-E.
- **Competitive context**: primary commercial counterweight to [[wiki/entities/anthropic|Anthropic]] in the LLM-as-product market. Both are named in [[wiki/entities/refero]]'s catalog and both ship distinct DESIGN.md aesthetics — Anthropic warm/typographic, OpenAI white/typographic.
- **Embedding model**: `text-embedding-3-small` converts text to embedding vectors (~1,536 floats) in the reference MemoryStore — cited in [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- **OpenAI-compatible API** is the de-facto serving interface implemented across nearly every inference engine (llama.cpp, MLC LLM, vLLM, OpenVINO GenAI, ONNX-adjacent tools) — per [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **GPT-Realtime-2**: per [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]], OpenAI shipped it on May 7, 2026; the source states every major lab shipped a native speech-to-speech voice model in 2026.
- **Codex**: publisher of the Codex CLI ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]], [[wiki/sources/nateherk-claude-code-codex-same-project]]). OpenAI's Codex team explicitly equates the terms "agent" and "harness" for non-model infrastructure ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **OpenAI Academy** (academy.openai.com): free account + prompt-engineering study resource (Phase 4) — [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]].

## Facts from tooling, harness, and roadmap sources

- **As a model API provider**: named as a model API to learn to call from code, with GPT cited as the model for one class of task in model-choice decisions ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]); API source in the layer-2 "basic AI integration" tier ([[wiki/sources/exploraX_-5-solo-ai-business-models]]). OpenAI SDKs are a [[wiki/entities/context7|Context7]] docs target ([[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]]).
- **Forward-deployed engineering**: named among AI companies looking for FDEs; its tool-use tutorial and structured-outputs developer page are cited as references — [[wiki/sources/vasuman-forward-deployed-engineering-101]].
- **Codex harness architecture** (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]): a strict priority stack — server system message > tool definitions > developer instructions > user instructions (AGENTS.md, 32 KiB limit) > conversation history; a three-layer architecture of Codex Core, App Server (JSON-RPC), and client surfaces (CLI / VS Code / web).
- **As a model provider behind enterprise proxies**: one of the model providers Shopify's LLM proxy routes to — [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].
- **AI-influencer tooling**: ChatGPT cited as a core generation tool used to build the author's first AI-influencer character — [[wiki/sources/insomnia_vip-ai-models-that-make-money]].
- **The AI race framing**: cited as one of the three companies most people think the AI race is between (OpenAI vs Google vs Anthropic) — [[wiki/sources/shabnam-google-2026-roadmap-keynote]].
- **Karpathy affiliation**: described as the org [[wiki/entities/andrej-karpathy|Andrej Karpathy]] was a founding member of — [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]].

## Positions and claims

*(none yet beyond the design system; awaiting primary-source ingest about company strategy, research positions, or product philosophy.)*

## Mentioned in

- [[wiki/sources/openai-design-md]] — DESIGN.md ingest.
- [[wiki/entities/sam-altman]] — CEO entity page references OpenAI.
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — OpenAI SDKs named as a Context7 docs target.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — model API provider referenced for API calls and model choice (GPT).
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] — maker of ChatGPT, referenced as the answer engine displacing discovery.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — provider of the embedding model (`text-embedding-3-small`) used in the reference memory implementation.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — named as an AI company seeking FDEs; its tool-use and structured-output docs cited.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — named in the "real battle isn't chatbots" framing (OpenAI vs Google vs Anthropic).
- [[wiki/sources/insomnia_vip-ai-models-that-make-money]] — ChatGPT named as the core generation tool used to build the first AI character.
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — cited as shipping GPT-Realtime-2 (May 7, 2026); representative of labs shipping native speech-to-speech voice models in 2026.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — API source in the roadmap's layer-2 (basic AI integration).
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — vendor of Codex CLI, the second agent in nateherk's parallel setup.
- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — OpenAI-compatible API as the de-facto serving interface across engines.
- [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]] — referenced as the org Karpathy was a founding member of.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — Codex/Agents SDK; explicitly equates "agent" and "harness".
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — one of the model providers Shopify's LLM proxy routes to.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — publisher of the Codex CLI named as the builder tool.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — OpenAI Academy as a frontier-lab prompt-engineering resource.

## Related concepts

- [[design-md]] — DESIGN.md format.
- [[markdown-as-agent-contract]] — meta-pattern.

## Related entities

- [[wiki/entities/anthropic]] — competitor; both have ingested DESIGN.md pages.
- [[wiki/entities/sam-altman]] — CEO.
- [[wiki/entities/refero]] — publisher of the design-md catalog.
