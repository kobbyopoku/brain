---
type: entity
title: ClickUp
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://clickup.com
aliases: []
tags: [task-management, ai-os-connection, stub]
---

# ClickUp

> Task / project management platform referenced in [[wiki/sources/nateherk-claude-code-os-3m-business]] as a primary connections-layer integration in the author's AI OS. Used as the worked example for **separate API accounts per service** and the **clickup-searcher sub-agent** pattern.

## Profile

This page is a **stub**. ClickUp appears in this wiki only via [[wiki/sources/nateherk-claude-code-os-3m-business]], where it features prominently:

- Listed under **Comms** and **Tasks** tier-1 domains in the tools-mapping exercise.
- Author's worked example for "separate API account per service" — *"I made an account called Up at AI inside ClickUp and only gave that account's API key to Claude."*
- Author's example of "prefer API endpoints saved as markdown over MCPs" — original Pulse Check skill called the ClickUp MCP and searched every list ID; rewritten to hardcode list IDs into skill.md.
- Author's example for [[subagents]]: a `clickup-searcher` sub-agent wraps heavy ClickUp data so it doesn't blow the main context window.

No primary source about ClickUp's product surface is yet ingested.

## Key facts

- **Website**: https://clickup.com
- **Role per source**: primary task/comms backend in nateherk's AI OS.

## Mentioned in

- [[wiki/sources/nateherk-claude-code-os-3m-business]]

## Related concepts

- [[ai-os-pattern]] — Connections layer.
- [[subagents]] — `clickup-searcher` example.
- [[mcp-server]] — author argues for API-over-MCP using ClickUp as the worked case.
