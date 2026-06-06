---
type: entity
title: Shopify dev MCP server
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [shopify-dev-mcp, "@shopify/dev-mcp"]
tags: [mcp, shopify, claude-code, developer-tools]
---

# Shopify dev MCP server

> Shopify's open-source Model Context Protocol server that connects Claude Code to Shopify docs, GraphQL schemas, and store operations.

## Profile

The Shopify dev MCP server is an open-source [[wiki/entities/model-context-protocol|MCP]] server published by [[wiki/entities/shopify|Shopify]] in April 2026. It connects [[wiki/entities/claude-code|Claude Code]] to live Shopify platform data — documentation, GraphQL schemas, and store operations — so that the model works against real data rather than hallucinating API fields. It exposes seven tools spanning docs search, schema validation, store operations, and natural-language bulk operations.

## Key facts

- **Publisher**: [[wiki/entities/shopify|Shopify]], open-sourced April 2026 (per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Install command**: `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest` (per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Tool count**: 7 tools — current docs search, live GraphQL schema validation, store operations via Shopify CLI, product/metafield/theme management, and natural-language bulk operations (per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Stated benefit**: prevents Claude from hallucinating API fields by working against real platform data (per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).

## Positions and claims

- Grounding the model in real platform data (live docs and GraphQL schemas) eliminates hallucinated API fields — argued in [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].

## Mentioned in

- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — Shopify's open-source MCP server connecting Claude Code to Shopify docs, GraphQL schemas, and store operations.

## Related entities

- [[wiki/entities/shopify]] — publisher of the dev MCP server.
- [[wiki/entities/claude-code]] — the client the server is installed into.
- [[wiki/entities/model-context-protocol]] — the protocol this server implements.

## Related concepts
