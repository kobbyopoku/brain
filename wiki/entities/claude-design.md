---
type: entity
title: Claude Design
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://claude.com
aliases: [anthropic-claude-design]
tags: [anthropic, design-tooling, ai-design, artifacts, proprietary]
---

# Claude Design

> Anthropic's proprietary design-tooling product that introduced the **artifact-first workflow**: an agent emits a single `<artifact>` HTML, which renders in a preview surface, and exports flow from there. The closed-source antecedent that [[wiki/entities/open-design|Open Design]] replicates as an Apache-2.0 alternative.

## Profile

This page is **partially substantive**. Claude Design appears in the wiki primarily through references in [[wiki/sources/nexu-io-open-design|nexu-io/open-design]] (the open-source clone). No primary source from Anthropic's Claude Design documentation has been ingested directly. What we know about it is inferred from Open Design's stated goals, architecture, and the existence of a `POST /api/import/claude-design` ZIP-import endpoint in Open Design (which confirms Claude Design has a ZIP-export format).

## Key facts

- **Publisher**: [[wiki/entities/anthropic]].
- **Defining workflow**: artifact-first — agent emits a single `<artifact>...</artifact>` HTML block; the surface renders it in a preview.
- **Notable feature implied by Open Design**: ZIP export for porting work between Claude Design and other tools.
- **Claude Design ↔ Open Design relationship**: Open Design is the explicit open-source alternative ("Open Design is an Apache-2.0 licensed, open-source platform that replicates the artifact-first workflow of Anthropic's Claude Design without proprietary lock-in"). Open Design's `import/claude-design` endpoint exists specifically to migrate users.

## Positions and claims

- **The artifact-first paradigm**: a single self-contained HTML output as the agent's primary artifact, rendered in a sandboxed preview, exportable to multiple formats (HTML, PDF, PPTX, ZIP, Markdown). This pattern predates and underlies Open Design's architecture. See [[artifact-first-workflow]].

## Open questions

- **What does Claude Design actually look like?** The wiki has only the open-source clone's perspective. A direct primary source — a Claude Design walkthrough, demo, or marketing page — would clarify the proprietary product's actual surface vs. what Open Design replicates.
- **Pricing and access model**: unsourced. Likely available to Claude.ai paid subscribers; details unverified here.
- **Anthropic's roadmap**: how Claude Design fits with [[wiki/entities/anthropic-skills|Anthropic Skills]] and [[wiki/entities/claude-code|Claude Code]] strategically — unsourced.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]] — references Claude Design as the proprietary product Open Design replicates.

## Related concepts

- [[artifact-first-workflow]] — the canonical pattern Claude Design introduced.
- [[design-md]] — adjacent (Refero/Open Design DESIGN.md format is downstream of artifact-first thinking).

## Related entities

- [[wiki/entities/anthropic]] — publisher.
- [[wiki/entities/open-design]] — the open-source alternative.
- [[wiki/entities/refero]] — adjacent design-tooling product, different positioning.
- [[wiki/entities/claude-code]] — Anthropic's coding-agent product.
- [[wiki/entities/anthropic-skills]] — Anthropic's skill collection.
