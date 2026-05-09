---
type: entity
title: Model Context Protocol (MCP)
entity_type: product
created: 2026-05-09
updated: 2026-05-09
website: https://modelcontextprotocol.io/
aliases: [MCP]
tags: [protocol, anthropic, open-standard, mcp, stub]
---

# Model Context Protocol (MCP)

> Open standard created by [[wiki/entities/anthropic|Anthropic]] defining how AI models connect to external tools and data sources. *"USB for AI"* — build one MCP server and it works with Claude Code + Claude Desktop + Cursor + Windsurf + every MCP-compatible client. Spec at `modelcontextprotocol.io`. **Distinct from individual MCP servers** ([[mcp-server]]) — this entity is the *protocol*, not the implementations.

## Profile

This page is a thin **stub** because the wiki's substantive coverage of MCP lives in [[wiki/concepts/mcp-server|the concept page]] and the dozens of source treatments. This entity exists for cross-cite hygiene — when sources distinguish *the protocol* from *individual servers*.

## Key facts

- **Creator**: [[wiki/entities/anthropic|Anthropic]].
- **Spec home**: [`modelcontextprotocol.io`](https://modelcontextprotocol.io/).
- **3 capability types per server**: Tools (DO actions) / Resources (REFERENCE data) / Prompts (FOLLOW templates).
- **Compatible clients**: Claude Code, Claude Desktop, Cursor, Windsurf, and a growing list.

## Mentioned in

- [[wiki/sources/Ai_here202-mcp-opportunity]] — clearest articulation of MCP-as-protocol vs MCP-server-as-implementation.
- *(see [[mcp-server]] concept for the full source list)*

## Related entities

- [[wiki/entities/anthropic]] — protocol creator.
- [[wiki/entities/claude-code]], [[wiki/entities/claude-design]], [[wiki/entities/cursor]] — clients.

## Related concepts

- [[mcp-server]] — concept page covering implementations + reliability + cost.
