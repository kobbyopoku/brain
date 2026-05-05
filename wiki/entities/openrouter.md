---
type: entity
title: OpenRouter
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://openrouter.ai
aliases: []
tags: [llm-infrastructure, multi-provider-aggregator, byok, ai-tooling, stub]
---

# OpenRouter

> Multi-provider LLM API aggregator — single endpoint that fronts 200+ models from Anthropic, OpenAI, Google, Meta, Mistral, and many others. Enables cost-routing, failover, and provider-comparison from one API key. Referenced by [[wiki/entities/hermes-agent|Hermes Agent]] as a primary supported provider; structurally similar to [[wiki/concepts/byok-proxy|Open Design's BYOK proxy]] but at platform-scale.

## Profile

This page is a **stub**. OpenRouter appears in the wiki only via the Hermes Agent ingest (referenced as a primary model provider). No primary source about OpenRouter's product, pricing, or business model has been ingested directly.

## Key facts

- **Website**: https://openrouter.ai
- **Catalog scope**: 200+ models across major providers (per Hermes Agent's documentation).
- **Architectural role**: provider aggregator with single unified API surface — write code once, switch models / providers without code changes.
- **Supported by**: [[wiki/entities/hermes-agent|Hermes Agent]] as a primary provider option.
- **Sibling products**: [LiteLLM](https://github.com/BerriAI/litellm), [Portkey](https://portkey.ai), [Helicone](https://helicone.ai).

## Positions and claims

*(awaiting direct primary-source ingest. Inferred from how Hermes Agent uses it.)*

- **One API endpoint for many models** is the right shape for agent infrastructure.
- **BYOK with usage-based billing per call** scales cleanly across providers.

## Mentioned in

- [[wiki/sources/nousresearch-hermes-agent]] — Hermes Agent supports OpenRouter as a primary provider.

## Related concepts

- [[byok-proxy]] — OpenRouter is structurally a BYOK proxy at platform scale; Open Design's BYOK proxy is the application-scale instance of the same pattern.
- [[mcp-server]] — adjacent: OpenRouter handles model abstraction; MCP handles tool abstraction.

## Related entities

- [[wiki/entities/hermes-agent]] — primary integration.
- [[wiki/entities/anthropic]], [[wiki/entities/openai]] — among the providers OpenRouter aggregates.
- [[wiki/entities/nous-research]] — adjacent open-AI-tooling org.
