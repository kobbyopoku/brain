---
type: entity
title: Figma
entity_type: product
created: 2026-05-05
updated: 2026-06-06
website: https://figma.com
aliases: []
tags: [design-tool, collaborative-design, design-md-available, mcp-integration, design-systems-tooling, open-design-catalog]
---

# Figma

> Browser-based collaborative design tool. The de facto standard for product UI design (vs Sketch / Adobe XD / Penpot). Founded 2012 by Dylan Field + Evan Wallace. Acquired by Adobe attempt fell through in late 2023 (regulatory blocking). Cataloged in [[wiki/entities/open-design|Open Design]] under Design & Creative with a *"vibrant multi-color, playful yet professional"* DESIGN.md. Ships an MCP server (`figma:figma-use` and the figma-* skill family) and a code-design-link feature (Figma Code Connect) — both make Figma a meaningful endpoint for AI design / coding agents.

## Profile

Figma is positioned in two axes the wiki cares about:

1. **Design-tooling category** — the canonical product designers use; Open Design's catalog includes it as a brand whose visual identity (the Figma marketing site / app chrome) is itself a DESIGN.md target.
2. **AI-agent integration target** — Figma's MCP server makes Figma files queryable by AI coding agents. The figma-* skills in the user's Claude Code setup (figma-implement-design, figma-create-design-system-rules, figma-use, figma-code-connect, figma-generate-library, etc.) are agent contracts pointing at Figma artifacts. Adjacent to but distinct from [[wiki/entities/open-design|Open Design]]'s skill model.

## Key facts

- **Founded**: 2012. Headquartered in San Francisco.
- **Founder/CEO**: Dylan Field (CEO), Evan Wallace (CTO, departed).
- **Website**: https://figma.com
- **Category** (per Open Design): Design & Creative.
- **Open Design DESIGN.md**: `raw/open-design/design-systems/figma/DESIGN.md`
- **Notable**: 2022 Adobe acquisition agreement ($20B) blocked by UK CMA / EU regulators in late 2023; Figma remained independent.
- **Products**: Figma (UI design), FigJam (whiteboard), Dev Mode (handoff-to-engineering surface), Figma Slides, Figma Make (AI-powered design generation).

## Product surface (AI-agent-relevant)

### Figma MCP server

Figma exposes an MCP server (`figma:figma-use`) that AI coding agents can connect to. Tools include reading file contents, generating designs from prompts, creating diagrams, and Code Connect template authoring. The user's Claude Code installation has multiple figma-* skills (figma-use, figma-implement-design, figma-generate-design, figma-generate-diagram, figma-code-connect, figma-create-design-system-rules, figma-generate-library) that are agent contracts pointing at this MCP. Material for the [[wiki/concepts/mcp-server|MCP server]] concept page — Figma is one of the higher-value brand-side MCPs.

### Figma Code Connect

Maps Figma components to code snippets. Each component carries a `figma.connect()` call linking it to an actual implementation in TSX / Vue / Swift / Compose. Then the design tool surfaces "this is the canonical code for this component." Structurally this is an instance of [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] applied to Figma — the connect-template files are designer-engineer contracts that AI agents can consume to produce on-spec code.

### Figma Make

Figma's AI-powered design generation feature (analogous to [[wiki/entities/open-design|Open Design]] / [[wiki/entities/claude-design|Claude Design]] / Vercel v0). Generates Figma frames from natural language prompts. Different positioning from Open Design: Figma Make produces *Figma artifacts* (vectors / components in the Figma file format), Open Design produces *HTML artifacts*.

### Dev Mode

Bridges design (Figma) and engineering (code). Surfaces design tokens, measurements, asset exports, Code Connect snippets. The most material part for AI coding agents — Dev Mode is the read-side of Figma where agents extract design specs to produce code.

## Positions and claims

- **The browser is the right runtime for design tools.** Figma's bet vs Sketch/Adobe XD's native-desktop default. Won decisively.
- **Real-time multi-user collaboration is the table-stakes feature.** Figma's multiplayer editing was a category-defining capability that competitors took years to match.
- **Design-system tooling sits inside the design tool, not separate.** Variables, modes, components, libraries — Figma's architectural bet that brand systems are built and maintained in Figma rather than in a separate design-token tool.
- **AI design generation is part of the design tool, not a sibling product.** Figma Make's positioning vs Vercel v0 / Open Design / Claude Design.

## Mentioned in

- [[wiki/sources/open-design-catalog]] — Open Design catalog entry.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — the incumbent design tool [[wiki/entities/claude-design|Claude Design]] is positioned against; nateherk frames Claude Design as not replacing Figma but replacing the gap between an idea and a shipped brand.

## Related entities

- [[wiki/entities/canva]], [[wiki/entities/framer]], [[wiki/entities/miro]] — sibling design / creative tools.
- [[wiki/entities/open-design]], [[wiki/entities/claude-design]] — AI-design-tooling siblings (different output formats: HTML vs Figma).
- [[wiki/entities/vercel]] — v0 (Vercel's AI UI generator) is a Figma Make competitor.
- [[wiki/entities/refero]] — adjacent: Refero extracts DESIGN.md from web; Figma is where many design teams maintain *the source* the web inherits.

## Related concepts

- [[design-md]] — Figma maintains design tokens that DESIGN.md files enumerate.
- [[markdown-as-agent-contract]] — Code Connect templates are an instance of the meta-pattern.
- [[mcp-server]] — Figma's MCP server is a higher-value brand-side MCP for AI agents.
