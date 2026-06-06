---
type: entity
title: Filesystem MCP
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [filesystem-mcp]
tags: [claude-code-ecosystem, mcp-server, ai-tooling]
---

# Filesystem MCP

> An MCP server that gives Claude full project (and vault) awareness by letting it navigate folders and read across many files.

## Profile

Filesystem MCP is presented as "Tool 4" in [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]]'s nine-plugin senior-engineer stack, where it gives [[wiki/entities/claude-code]] full project awareness. The same server recurs in CyrilXBT's Obsidian sources as the connector between Claude and an Obsidian vault — [[wiki/sources/cyrilxbt-personal-operating-system]] instructs installing Claude Desktop and pointing the Filesystem MCP at the vault as the "Layer 2 intelligence" connector, and [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] uses it to let Claude Code read a dashboard and write back property updates.

## Key facts

- **Type**: MCP server / Claude Code plugin. *(per [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]].)*
- **Capabilities**: navigate folders, read multiple files, refactor entire projects, trace dependencies, understand architecture.
- **Obsidian use**: configured (pointed at a vault) to connect Claude to the vault as the intelligence layer. *(per [[wiki/sources/cyrilxbt-personal-operating-system]] and [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]].)*

## Positions and claims

- Improves refactoring, debugging, migrations, cleanup, and large-scale edits. *(per [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]].)*
- Marks the line between "small context AI = assistant" and "full repo context AI = teammate." *(per [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]].)*

## Mentioned in

- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — Tool 4; gives Claude full project awareness.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — the connector pointed at the Obsidian vault for the Layer 2 intelligence layer.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — connects Claude Code to the dashboard to read referenced files and write back property updates.

## Related entities

- [[wiki/entities/claude-code]] — the platform it extends.

## Related concepts

- [[mcp-server]]
