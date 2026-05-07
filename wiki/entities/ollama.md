---
type: entity
title: Ollama
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://ollama.com
aliases: []
tags: [ai-llm, local-models, open-source, design-md-available, open-design-catalog, stub]
---

# Ollama

> Local LLM runtime — pull and run open-weight models on your own machine. Cataloged in [[wiki/entities/open-design|Open Design]] with a *"terminal-first, monochrome simplicity"* DESIGN.md.

## Profile

This page is a **stub**. Ollama appears via the Open Design catalog. The product is the canonical "run an LLM on your laptop" tool — `ollama pull llama3.1` then `ollama run llama3.1`.

## Key facts

- **Website**: https://ollama.com
- **Category** (per Open Design): AI & LLM.
- **Open Design DESIGN.md**: `raw/open-design/design-systems/ollama-design-md.md`.
- **Role**: local model runtime + REST API; backbone of many local-first AI workflows.
- **Adjacency**: serves as a model-provider endpoint for any agent CLI that accepts a custom OpenAI-compatible base URL — including [[wiki/entities/hermes-agent|Hermes Agent]] and [[wiki/entities/open-design|Open Design]]'s BYOK proxy.

## Mentioned in

- [[wiki/sources/open-design-catalog]]

## Related entities

- [[wiki/entities/nous-research]], [[wiki/entities/huggingface]], [[wiki/entities/mistral-ai]] — model sources.
- [[wiki/entities/hermes-agent]], [[wiki/entities/open-design]] — agents that can talk to local Ollama endpoints.

## Related concepts

- [[design-md]]
- [[byok-proxy]] — Ollama is a popular local endpoint behind BYOK proxies.
