---
type: entity
title: Nous Research
entity_type: organization
created: 2026-05-05
updated: 2026-05-05
website: https://nousresearch.com
aliases: [nousresearch]
tags: [ai-research, open-weight-models, ai-tooling, hermes-series]
---

# Nous Research

> AI research collective publishing the **Hermes** series of fine-tuned open-weight models and the [[wiki/entities/hermes-agent|Hermes Agent]] CLI / multi-platform agent product. Notable in the open-source AI community for steerable, function-calling-tuned models built on top of base models like Llama, Mistral, and Qwen.

## Profile

This page is **partially substantive**. Nous Research appears in the wiki via its [[wiki/entities/hermes-agent|Hermes Agent]] product (canonical wiki source: [[wiki/sources/nousresearch-hermes-agent]]) and the broader Hermes-series fine-tuned models. No primary source about the organization's broader research program, team, funding, or publications has been ingested directly.

## Key facts

- **Website**: https://nousresearch.com
- **Notable products**:
  - [[wiki/entities/hermes-agent|Hermes Agent]] — MIT-licensed self-improving multi-platform agent CLI (Feb 2026, 23k+ stars).
  - **Hermes-series models** (Hermes-2, Hermes-3, Hermes-4, etc.) — open-weight fine-tunes of base models (Llama, Mistral, Qwen) tuned for steerable behavior, function calling, and agentic workflows. Distributed via Hugging Face. *(Models referenced via the Hermes Agent's "Nous Portal" provider option but not separately ingested.)*
  - **Nous Portal** — provider endpoint for Nous Research's hosted model API.
- **Domain positioning**: open-weight AI tooling with a focus on agentic / function-calling workflows. Distinct from:
  - **Anthropic / OpenAI** (closed-weight frontier models)
  - **Hugging Face** (model distribution platform)
  - **Mistral / Meta** (base-model publishers)

  Nous sits in the *fine-tune-and-tool* layer — adding agentic discipline to base models others publish.

## Positions and claims

*(awaiting direct primary-source ingest about the org's research positions; current claims inferred from Hermes Agent's design choices.)*

- **Open-weight + steerable + function-calling tuned** is the right primitive for autonomous agents.
- **Persistent memory + self-improvement should be agent-internal, not external.** Reflected in Hermes Agent's architecture.
- **Model-agnostic agents** beat vendor-locked agents.

## Mentioned in

- [[wiki/sources/nousresearch-hermes-agent]] — canonical source via the Hermes Agent product.

## Related entities

- [[wiki/entities/hermes-agent]] — flagship product.
- [[wiki/entities/openrouter]] — sibling in the multi-model-aggregation space.
- [[wiki/entities/anthropic]], [[wiki/entities/openai]] — adjacent in the AI research category, different positioning (closed-weight frontier vs open-weight fine-tunes).

## Related concepts

- [[hot-cache]], [[llm-wiki-pattern]] — Nous's Hermes Agent is the agent-internal alternative to these external-markdown patterns.
- [[byok-proxy]] — Hermes Agent's model-agnostic design.
- [[markdown-as-agent-contract]] — Hermes AGENTS.md is an instance.
