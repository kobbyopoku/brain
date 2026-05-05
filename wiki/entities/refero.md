---
type: entity
title: Refero
entity_type: product
created: 2026-05-02
updated: 2026-05-05
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

## Open-source alternative

As of 2026-05-05, the wiki contains an explicit open-source alternative to Refero: [[wiki/entities/open-design|nexu-io/open-design]] (Apache-2.0). Open Design is more architecturally substantial — full application stack (Next.js + Express daemon + multi-agent runtime + media generation) vs Refero's catalog + MCP server. Open Design's DESIGN.md format extends Refero's 5-section schema to **9 sections** (adds Depth/Elevation, Do/Don't, Responsive Behavior, Agent Prompt Guide). Open Design also publishes 138 design systems vs Refero's 32 (in our wiki).

For an end-to-end OSS workflow: Open Design + an open-source coding-agent CLI ([[wiki/entities/opencode-cli|OpenCode]] or [[wiki/entities/qwen-cli|Qwen]]) with [[wiki/entities/open-design|Open Design]]'s BYOK proxy fully replaces the Refero + Claude/Cursor stack. The tradeoff: Open Design adds a daemon dependency to the dev environment.

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]] — landing page that introduces the service and lists featured brands.
- [[wiki/sources/nexu-io-open-design]] — names Refero implicitly as the closest sibling positioning (curated catalog with MCP server) that Open Design supersedes via local-first OSS.

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

- [[wiki/entities/open-design]] — open-source alternative (Apache-2.0); 138 design systems with the richer 9-section DESIGN.md schema.
- [[wiki/entities/claude-design]] — the proprietary Anthropic product that introduced the artifact-first workflow Refero and Open Design both build around.
- [[wiki/entities/anthropic]] — featured brand in catalog + maintainer of Claude Design.

## Related concepts

- [[wiki/concepts/design-md]] — the file format Refero produces.
- [[wiki/concepts/markdown-as-agent-contract]] — the meta-pattern Refero participates in.
