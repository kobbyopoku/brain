---
type: entity
title: OpenAI Agents SDK
entity_type: product
created: 2026-05-02
updated: 2026-06-06
website: https://github.com/openai/openai-agents-python
aliases: [openai-agents]
tags: [agent-framework, openai, sdk]
---

# OpenAI Agents SDK

> OpenAI's official SDK for building agents — Python package `openai-agents`. Launched March 11, 2025 alongside the Responses API and built-in tools for web search, file search, and computer use. v0.13.1 in March 2026 (per [[wiki/sources/hooeem-build-an-ai-agent-today]]).

## Profile

The OpenAI Agents SDK is the official OpenAI-authored toolkit for building agents wrapping the [[agentic-loop]] with OpenAI's function-tool conventions. It is named in [[wiki/sources/hooeem-build-an-ai-agent-today]] as one of the canonical agent frameworks (alongside [[wiki/entities/anthropic-agent-sdk|Anthropic Agent SDK]], [[wiki/entities/langgraph|LangGraph]], [[wiki/entities/crewai|CrewAI]]). Recommendation in that source: pick OpenAI-first if you want a clean developer SDK with hosted tools, handoffs between specialist agents, guardrails, tracing, and a simple path to production.

## Key facts

- **Python package**: `openai-agents`
- **Maintainer**: OpenAI (organization not yet ingested as an entity in this wiki).
- **Launched**: March 11, 2025 (alongside Responses API + built-in tools).
- **Built-in tools**: web search, file search, computer use, code interpreter.
- **Mar 2026 version**: v0.13.1.
- **Tool format**: function object with parameters schema.
- **Notable abstractions** (per source): handoffs, guardrails, tracing.
- **Harness interface**: implements the harness via a `Runner` class with async, sync, and streamed modes (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Code-first**: workflow logic lives in native Python rather than graph DSLs (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Tool types**: function tools, hosted tools (WebSearch / CodeInterpreter / FileSearch), and MCP server tools (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Guardrails**: three levels — input, output, and tool guardrails — with a "tripwire" halt mechanism (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Composition**: supports agents-as-tools and handoffs for subagents (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Positions and claims

- **OpenAI-first when you want a clean SDK with hosted tools and a smooth path to production.** *(Per [[wiki/sources/hooeem-build-an-ai-agent-today]].)*

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — implements the harness through the `Runner` class.

## Related entities

- [[wiki/entities/anthropic-agent-sdk]] — sibling framework.
- [[wiki/entities/langgraph]] — alternative orchestration.
- [[wiki/entities/crewai]] — alternative multi-agent framework.
- [[wiki/entities/sam-altman]] — OpenAI CEO (relationship widely known but not directly cited in any source ingested here).

## Related concepts

- [[agentic-loop]]
- [[augmented-llm]]
- [[agent-workflow-patterns]]
- [[mcp-server]]
