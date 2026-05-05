---
type: entity
title: Anthropic
entity_type: organization
created: 2026-05-02
updated: 2026-05-05
website: https://anthropic.com
aliases: []
tags: [ai-research, claude-code-ecosystem, refero-catalog, design-md-ingested]
---

# Anthropic

> AI research and safety company; maintainer of Claude and [[wiki/entities/claude-code|Claude Code]]; publisher of the official [[wiki/entities/anthropic-skills|skill collection]] and the Claude Code plugin marketplace. Operator of the agent that maintains this wiki.

## Profile

Anthropic is the AI research company that builds the Claude family of models and operates [[wiki/entities/claude-code|Claude Code]] — the platform on which this wiki is maintained and which is the central subject of multiple ingested sources. Anthropic also publishes the official open-source [[wiki/entities/anthropic-skills|skills]] repository (canonical reference for Claude Code skill authoring) and operates the plugin marketplace through which third-party plugins like [[wiki/entities/superpowers]] are distributed. Anthropic also appears in the [[wiki/entities/refero|Refero]] design-reference catalog ("Research journal printed on warm…"), which is the original reason an entity page existed before substantive sources were ingested.

## Key facts

- **Website**: https://anthropic.com
- **Operates**: [[wiki/entities/claude-code]] (CLI), Claude API, Claude.ai web/desktop apps, IDE extensions.
- **Publishes**: [[wiki/entities/anthropic-skills]] (`github.com/anthropics/skills`) — official skill collection covering PDF, DOCX, XLSX generation, data analysis.
- **Operates**: the Claude Code plugin marketplace (e.g. `claude-plugins-official` namespace).
- **Refero style page**: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
- **Refero mood descriptor**: "Research journal printed on warm stone."

## Design system summary

From [[wiki/sources/anthropic-design-md]]: *"Research journal printed on warm stone — authoritative typographic composition where word-level underlines replace color as the primary emphasis mechanism."*

- **Three custom typefaces**: Anthropic Sans (UI/body), Anthropic Serif (display/editorial), Anthropic Mono (technical labels). Most brands use one custom typeface; Anthropic has three.
- **Six accent colors as thematic tags** (Clay, Ember, Olive, Sky, Fig, Cactus) — rotated by section/category, not used for hierarchy.
- **Warm-stone neutrals** — Ivory `#faf9f5` page ground, Oat `#e3dacc` tertiary, Cloud `#87867f` secondary text. Genuinely warm vs. typical cool-temperature design systems.
- **Asymmetric "Try Claude" button** — radius `0px 0px 8px 8px` (flat top, rounded bottom). Brand signature.
- **Underline-as-emphasis** replaces color highlighting. *"Headline emphasis via underline only, never color."*
- **Zero box-shadows. Hard-edged surface transitions.**

## Positions and claims

- **Skill files are the canonical mechanism for teaching agents domain-specific workflows.** *(Implicit by virtue of publishing and curating the official skill collection; explicit articulation would require an Anthropic-authored primary source.)*
- **Plugin marketplace distribution is the right channel** for third-party agent capabilities at scale. *(Implicit by operating the marketplace.)*

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — repeatedly: as Claude Code maintainer, official skills publisher, and plugin marketplace operator.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — implicit Claude Code maintainer.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — featured brand in the Refero catalog.
- [[wiki/sources/anthropic-design-md]] — full DESIGN.md ingested 2026-05-02.
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. References Anthropic's [[wiki/entities/claude-design|Claude Design]] product as the proprietary antecedent that Open Design replicates as Apache-2.0.

## Related entities

- [[wiki/entities/claude-code]] — Anthropic's coding-agent product.
- [[wiki/entities/claude-design]] — Anthropic's design-tooling product (artifact-first workflow).
- [[wiki/entities/anthropic-skills]] — Anthropic's official skill collection.
- [[wiki/entities/superpowers]] — third-party plugin distributed via the Anthropic plugin marketplace.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — third-party skill collection complementing Anthropic's official one.
- [[wiki/entities/refero]] — design-reference catalog Anthropic appears in.
- [[wiki/entities/open-design]] — open-source alternative to Anthropic's Claude Design.

## Related concepts

- [[claude-code-skills]]
- [[markdown-as-agent-contract]]
- [[design-md]]
