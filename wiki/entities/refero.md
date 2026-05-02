---
type: entity
title: Refero
entity_type: product
created: 2026-05-02
updated: 2026-05-02
aliases: [Refero MCP]
website: https://styles.refero.design/
tags: [design-systems, mcp, ai-tooling, design-md]
---

# Refero

> A curated library of design references (colors, typography, spacing, component patterns) extracted from well-known product websites and packaged as [[design-md|DESIGN.md]] files that AI coding agents can consume directly.

## Profile

Refero publishes a searchable catalog of "design styles" — each scraped from a real product website (e.g. Linear, Stripe, Anthropic, Apple, Cursor, ElevenLabs) and structured into colors, typography, spacing, and component patterns. The output format for agents is a markdown file (DESIGN.md). Refero also distributes its catalog via an MCP server, so AI coding tools (Cursor, Claude, Windsurf, "and others") can search and reference these designs natively during UI generation, not just by following a URL. In this wiki, Refero appears as one concrete instance of the broader [[markdown-as-agent-contract]] pattern — a sibling to [[llm-wiki-pattern]] in the design-tokens domain rather than the personal-knowledge domain.

## Key facts

- **Domain**: https://styles.refero.design/ (cited in [[wiki/sources/refero-design-systems-for-ai-agents]])
- **Output format**: [[design-md]] — markdown file containing colors, typography, spacing, components.
- **Distribution channels**: web catalog + MCP server (Refero MCP).
- **MCP integrations advertised**: Cursor, Claude, Windsurf, and other AI coding tools.
- **Search dimensions**: brand, mood, color, typography, URL.
- **Tagline**: "Design taste, extracted."

## Positions and claims

- **AI coding agents can have "design taste" if they're given the right reference data.** Implicit thesis: aesthetic decisions made by top product teams are the right reference data, and a curated library beats letting an agent reason from first principles. Cited in [[wiki/sources/refero-design-systems-for-ai-agents]].
- **Markdown is the right format for that reference data.** Refero ships DESIGN.md, not JSON, not Figma. This is consistent with the broader claim in [[markdown-as-agent-contract]] — markdown is becoming the lingua franca between humans and agents.

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]] — landing page that introduces the service and lists featured brands.

## Featured brands in catalog

Brands appearing on the Refero landing page captured in [[wiki/sources/refero-design-systems-for-ai-agents]]. All are stubs awaiting substantive primary sources.

- [[wiki/entities/acctual]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/antimetal]]
- [[wiki/entities/apple]]
- [[wiki/entities/base44]]
- [[wiki/entities/column]]
- [[wiki/entities/cursor]]
- [[wiki/entities/dia-browser]]
- [[wiki/entities/elevenlabs]]
- [[wiki/entities/family]]
- [[wiki/entities/general-intelligence-company]]
- [[wiki/entities/hyperstudio]]
- [[wiki/entities/linear]]
- [[wiki/entities/mercury]]
- [[wiki/entities/minimalissimo]]
- [[wiki/entities/monopo-saigon]]
- [[wiki/entities/raycast]]
- [[wiki/entities/stripe]]
- [[wiki/entities/superhuman]]
- [[wiki/entities/titan]]

## Related entities

_(no non-catalog entities yet — when sources unrelated to Refero ingest entities that also appear in this catalog, link them here.)_

## Related concepts

- [[wiki/concepts/design-md]] — the file format Refero produces.
- [[wiki/concepts/markdown-as-agent-contract]] — the meta-pattern Refero participates in.
