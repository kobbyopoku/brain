---
type: entity
title: Model Context Protocol (MCP)
entity_type: product
created: 2026-05-09
updated: 2026-06-06
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
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — underlying standard for most of the named plugins (GitHub MCP, Playwright MCP, Filesystem MCP, [[wiki/entities/database-mcp|Database MCP]], [[wiki/entities/browser-tools-mcp|Browser Tools MCP]]).
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — Stage VI advanced skill: build/deploy MCP servers, write MCP clients, connect them to AI models, as systems move toward standard ways of connecting models with tools, data, APIs, files, and external services.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — named as "MCP connectors," the extension surface beyond the four first-party connectors (Gmail/Calendar/Drive/Slack).
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — the Filesystem MCP connects Claude Code to the Obsidian vault, giving read access (morning briefing) and write access (automatic property updates).
- [[wiki/sources/cyrilxbt-personal-operating-system]] — a Filesystem MCP, pointed at the vault directory during setup, gives Claude read/write access to the vault.
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — MCP servers are configured in Hermes via config.yaml alongside model choice, terminal backend, and tool enablement.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — named as an interop foundation (not a marketplace) for the discovery layer; the MCP server registry indexes tools, not autonomous services; ERC-8004 registration files reference MCP endpoints.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — Phase 5: "MCP is rapidly becoming the standard way AI systems connect to tools, APIs, and external environments"; Anthropic's MCP courses recommended for the agents phase.
- *(see [[mcp-server]] concept for the full source list)*

## Related entities

- [[wiki/entities/anthropic]] — protocol creator.
- [[wiki/entities/claude-code]], [[wiki/entities/claude-design]], [[wiki/entities/cursor]] — clients.

## Related concepts

- [[mcp-server]] — concept page covering implementations + reliability + cost.
