---
type: entity
title: Shopify
entity_type: product
created: 2026-05-05
updated: 2026-06-06
website: https://shopify.com
aliases: []
tags: [e-commerce, saas, retail-platform, design-md-available, open-design-catalog, stub]
---

# Shopify

> E-commerce SaaS platform — hosts and powers millions of online stores. Cataloged in [[wiki/entities/open-design|Open Design]] under E-Commerce & Retail with a *"dark-first cinematic, neon green accent, ultra-light type"* DESIGN.md.

## Key facts

- **Website**: https://shopify.com
- **Open Design DESIGN.md**: `raw/open-design/design-systems/shopify/DESIGN.md`
- **Engineering headcount**: ~23,000 engineers (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **AI-first target**: ~90–96% autonomous coding by Q3 2026 (source states 96% in opening, 90% in closing) (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Internal LLM proxy**: routes every AI request — Claude Code, [[wiki/entities/github-copilot|GitHub Copilot]], Cursor — through one gateway to OpenAI / Anthropic / Google models for cost control, usage analytics, and model swapping (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Dev MCP server**: open-sourced `@shopify/dev-mcp` in April 2026, exposing 7 tools to Claude Code (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Strategy/execution time ratio**: flipped from 30/70 (2024) to 70/30 (2026) (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Productivity estimate**: ~20% improvement attributed to exploring 10 approaches instead of 2, per [[wiki/entities/farhan-thawar|Farhan Thawar]]'s team (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).

## Positions and claims

- **Runs multiple Claude Code agents in parallel** on different codebase regions; engineers review and merge — described in [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].
- **Treats `CLAUDE.md` as git-committed team infrastructure** shared across all 23,000 engineers; the source's sample stack is Ruby on Rails, React, GraphQL, MySQL — per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].
- **Uses `settings.json` permission guardrails**: allow read/write/test/lint/commit; deny push/deploy/db:drop/`rm -rf`/`.env` reads; `defaultMode` acceptEdits — per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].

## Mentioned in
- [[wiki/sources/open-design-catalog]]
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — the enterprise subject; its 23,000 engineers and their Claude Code setup are the source's focus.

## Related entities
- [[wiki/entities/farhan-thawar]] — Shopify VP Engineering quoted in the source.
- [[wiki/entities/github-copilot]] — one of three AI coding tools Shopify routes through its internal LLM proxy.
- [[wiki/entities/bessemer]] — publisher of Shopify's full AI-first playbook the source repackages.

## Related concepts
- [[design-md]]
