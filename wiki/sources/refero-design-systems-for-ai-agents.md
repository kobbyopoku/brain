---
type: source
title: Design Systems for AI Agents — Refero
created: 2026-05-02
updated: 2026-05-02
source_url: https://styles.refero.design/
source_type: webpage
author: Refero
source_date: 2026-05-02
raw_path: raw/Design Systems for AI Agents.md
tags: [design-systems, ai-agents, mcp, design-md, clipping]
---

# Design Systems for AI Agents — Refero

> Landing page for Refero, a curated library that extracts design tokens (colors, typography, spacing, components) from well-known product websites into a [[design-md]] format that AI coding agents can read before generating UI.

## TL;DR

Refero is a curated catalog of design references — colors, typography, spacing, and component patterns scraped and structured from real product websites (Linear, Stripe, Apple, Anthropic, Cursor, ElevenLabs, Raycast, Mercury, Superhuman, and others). Each style is published with a [[design-md|DESIGN.md]] file an AI coding agent can ingest. The service also ships an MCP server ("Refero MCP") so AI coding tools like Cursor, Claude, and Windsurf can search and reference designs natively. The interesting structural claim — read between the lines of this landing page — is that markdown files are emerging as a general configuration/contract layer between humans and AI agents (see [[markdown-as-agent-contract]]).

## Key takeaways

- **Refero exists** and frames itself as "design taste, extracted" — a service that turns aesthetic decisions from top product teams into machine-readable references.
- **Search dimensions**: by brand, mood, color, typography, or URL. Implies a hand-curated catalog rather than a raw crawl.
- **DESIGN.md is the unit of output.** Every style page produces a markdown file an agent can consume. See [[design-md]].
- **Refero MCP** is the agent-facing interface — it advertises connections to Cursor, Claude, Windsurf, "and other AI coding tools." This is meaningful: Refero is not just a website, it's an MCP-distributed knowledge source.
- **Brands featured** on the landing page (representative, not exhaustive): ElevenLabs, Cursor, Linear, Mercury, Stripe, Apple, Superhuman, monopo saigon, Hyperstudio, Family, Antimetal, General Intelligence Company, Titan, Raycast, Anthropic, Dia Browser, Minimalissimo, Column, Acctual, Base44.
- **Each style ships a one-line poetic descriptor** — e.g. Linear is "Midnight Command Center: A dark…", Apple is "Gallery wall at natural light", Raycast is "Obsidian command terminal — a…". These read more like art-direction prompts than design-system descriptions, which is a deliberate framing choice: design taste expressed in plain language for agents to absorb.
- **The pattern this source instantiates**: markdown as a contract between humans and AI agents. CLAUDE.md, AGENTS.md, DESIGN.md, SKILL.md all belong to the same family — see [[markdown-as-agent-contract]]. Refero is one product in this category; the [[llm-wiki-pattern]] is another.
- **What this source does NOT contain**: actual contents of any brand's DESIGN.md, MCP setup instructions, pricing, or who's behind the service. Those would live on per-brand pages or docs not captured in this clipping.

## Notable quotes

> "Design taste, extracted."
> — landing page tagline

> "Search a curated DESIGN.md library for AI agents: colors, typography, spacing, and component patterns from top websites. Part of Refero."
> — page meta description

> "Thousands of real product screens and full user flows your coding agent can search and study before it builds."
> — Refero MCP section

## Notes

- This is a thin clipping — a directory landing page, not deep content. The substantive value is the **existence** of the service and the **DESIGN.md pattern** it instantiates, not the per-brand entries (which are linked but not included). If a specific brand's design system becomes load-bearing for the wiki later, ingest that brand's per-style page directly.
- The brand list functions as a **taste signal** about what design references this vault might want to study: tools that ship to developer-adjacent audiences (Linear, Cursor, Stripe, Raycast, Anthropic, Superhuman) dominate. Useful prior when prioritizing future ingests.
- **Open question**: How is each DESIGN.md structured? Color tokens vs. CSS variables vs. raw hex? Components as JSX, MDX, or just descriptive prose? Without ingesting an actual DESIGN.md, the wiki can only describe the pattern at one level of abstraction.
- **Worth following up**: Refero's MCP server documentation. If we want this vault's agent to search Refero designs directly during UI work, that's a one-MCP-config away.

## Mentioned entities

- [[wiki/entities/refero]] — the service publishing this catalog.

### Featured brands in the catalog (stubs)

The landing page features the following brands as cataloged design references. Each has a stub entity page; substantive content will arrive when a primary source about that brand is ingested.

- [[wiki/entities/acctual]] — "Architectural blueprint on white…"
- [[wiki/entities/anthropic]] — "Research journal printed on warm…"
- [[wiki/entities/antimetal]] — "Electric storm over a blueprint —…"
- [[wiki/entities/apple]] — "Gallery wall at natural light —…"
- [[wiki/entities/base44]] — "Softly Lit Gradient Canvas"
- [[wiki/entities/column]] — "Architectural blueprint on white…"
- [[wiki/entities/cursor]] — "Warm ivory software studio."
- [[wiki/entities/dia-browser]] — "Prism on white stationery — light…"
- [[wiki/entities/elevenlabs]] — "Architect's blueprint on warm…"
- [[wiki/entities/family]] — "Pixar storyboard on cream paper —…"
- [[wiki/entities/general-intelligence-company]] — "Architectural Night Sky"
- [[wiki/entities/hyperstudio]] — "Monochrome terminal with amber…"
- [[wiki/entities/linear]] — "Midnight Command Center: A dark,…"
- [[wiki/entities/mercury]] — "Mountain Top Command Center"
- [[wiki/entities/minimalissimo]] — "White gallery canvas."
- [[wiki/entities/monopo-saigon]] — "Shifting gradient depths on…"
- [[wiki/entities/raycast]] — "Obsidian command terminal — a…"
- [[wiki/entities/stripe]] — "Architectural blueprint on white…"
- [[wiki/entities/superhuman]] — "Cinematic cockpit behind warm…"
- [[wiki/entities/titan]] — "monochrome financial ledger"

## Related concepts

- [[wiki/concepts/design-md]] — the markdown format Refero outputs.
- [[wiki/concepts/markdown-as-agent-contract]] — the meta-pattern this source belongs to.
- [[wiki/concepts/llm-wiki-pattern]] — sibling instance of the same meta-pattern (markdown as agent contract).

## Related sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — the foundational source on markdown-as-agent-contract for personal knowledge bases; Refero is a cousin pattern in the design-tokens domain.
