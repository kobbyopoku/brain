---
type: entity
title: Browserbase
entity_type: product
created: 2026-05-08
updated: 2026-05-08
website: https://browserbase.com
aliases: []
tags: [ai-infrastructure, browser-automation, web-agents, headless-browsers, stub]
---

# Browserbase

> Managed-browser infrastructure for AI agents — *"AWS for headless browsers"*. Lets agents drive real websites (read, click, fill forms, scrape, screenshot) without each developer spinning up their own Chromium fleet. Surfaced into the wiki via [[wiki/entities/kylejeong|Kyle Jeong]] (their growth engineer).

## Profile

This page is a **stub**. Browserbase appears in the wiki only via the Kyle Jeong batch ingest. No primary source from Browserbase about pricing, architecture, or competitive positioning has been ingested.

## Key facts

- **Website**: https://browserbase.com
- **Category**: AI infrastructure / browser automation.
- **Architectural role**: provides agents with managed browser sessions — analogous to what MCP servers do for tool calls but for browser actions.
- **Why it matters for the wiki**: complements MCP-as-tool-abstraction with browser-as-tool-abstraction. Many web tasks (research, form-filling, scraping price/inventory) require browser semantics that pure-API MCPs can't provide.

## Mentioned in

- [[wiki/sources/kylejeong-x-2052103973377867913]] — Kyle Jeong's thread about Browserbase / web-agent topics.

## Related entities

- [[wiki/entities/kylejeong]] — growth engineer there.
- [[wiki/entities/claude-code]] — common integration target.
- [[wiki/entities/anthropic]], [[wiki/entities/openai]] — providers of the LLMs that drive the browsers.

## Related concepts

- [[mcp-server]] — sibling architectural role (tool calls vs browser actions).
- [[agent-workflow-patterns]] — Browserbase fits the worker side of orchestrator-workers patterns.
