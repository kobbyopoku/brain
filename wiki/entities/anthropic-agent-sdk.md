---
type: entity
title: Anthropic Agent SDK
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/anthropics/claude-agent-sdk
aliases: [Claude Agent SDK, Claude Code SDK]
tags: [agent-framework, anthropic, sdk]
---

# Anthropic Agent SDK

> Anthropic's official SDK for building agents with Claude. Originally released as the **Claude Code SDK** in February 2025; renamed to the **Claude Agent SDK** in September 2025; v0.1.50 in March 2026 (per [[wiki/sources/hooeem-build-an-ai-agent-today]]). Exposes tools via JSON schemas with `input_schema`.

## Profile

The Anthropic Agent SDK is the official Anthropic-authored toolkit for building agents that wrap the [[agentic-loop]] with Anthropic's tool conventions. It is named in [[wiki/sources/hooeem-build-an-ai-agent-today]] alongside [[wiki/entities/openai-agents-sdk|OpenAI Agents SDK]], [[wiki/entities/langgraph|LangGraph]], and [[wiki/entities/crewai|CrewAI]] as one of the canonical agent frameworks. The recommendation in that source: pick Anthropic-first if you want an agent that should read/write/edit files, run shell, search the web, use MCP tools, and feel like a capable operator.

## Key facts

- **Repo**: https://github.com/anthropics/claude-agent-sdk
- **Maintainer**: [[wiki/entities/anthropic]].
- **Naming history**:
  - **Feb 2025**: launched as Claude Code SDK.
  - **Sep 2025**: renamed to Claude Agent SDK.
  - **Mar 2026**: current release v0.1.50 (per source).
- **Tool format**: JSON schema with `input_schema` field.
- **Strength** (per source): file edit + shell + web + MCP + coding workflows.

## Positions and claims

- **Anthropic-first when you want operator-style agent capabilities** (files, shell, web, MCP, coding). *(Per [[wiki/sources/hooeem-build-an-ai-agent-today]].)*

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]

## Related entities

- [[wiki/entities/anthropic]] — maintainer.
- [[wiki/entities/claude-code]] — the CLI / IDE that builds on the same SDK.
- [[wiki/entities/openai-agents-sdk]] — sibling framework.
- [[wiki/entities/langgraph]] — alternative orchestration.
- [[wiki/entities/crewai]] — alternative multi-agent framework.

## Related concepts

- [[agentic-loop]]
- [[augmented-llm]]
- [[agent-workflow-patterns]]
- [[mcp-server]]
