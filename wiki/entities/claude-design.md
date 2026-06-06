---
type: entity
title: Claude Design
entity_type: product
created: 2026-05-05
updated: 2026-06-06
website: https://claude.com
aliases: [anthropic-claude-design]
tags: [anthropic, design-tooling, ai-design, artifacts, proprietary]
---

# Claude Design

> Anthropic's proprietary design-tooling product that introduced the **artifact-first workflow**: an agent emits a single `<artifact>` HTML, which renders in a preview surface, and exports flow from there. The closed-source antecedent that [[wiki/entities/open-design|Open Design]] replicates as an Apache-2.0 alternative.

## Profile

Two primary sources now document Claude Design directly: [[wiki/sources/nateherk-claude-design-tally-brand]] (an operator walkthrough) and [[wiki/sources/prajwaltomar-claude-design-workflow]] (a UI-and-workflow walkthrough). Per these, Claude Design is Anthropic's vision-first design surface released April 17, 2026 (the day after [[wiki/entities/opus-4-7|Opus 4.7]]), running on Opus 4.7, that builds prototypes, slide decks, landing pages, animated promos, mobile mockups, and short brand videos from natural language. It lives inside an existing Claude subscription at `claude.ai/design`, requires at least a Pro plan, and carries its own weekly usage quota separate from regular Claude and [[wiki/entities/claude-code|Claude Code]]. The product was originally surfaced in the wiki via [[wiki/sources/nexu-io-open-design|nexu-io/open-design]] (the open-source clone), which confirmed the ZIP-export format through its `POST /api/import/claude-design` endpoint.

## Key facts

- **Publisher**: [[wiki/entities/anthropic]].
- **Defining workflow**: artifact-first — agent emits a single `<artifact>...</artifact>` HTML block; the surface renders it in a preview.
- **Notable feature implied by Open Design**: ZIP export for porting work between Claude Design and other tools.
- **Claude Design ↔ Open Design relationship**: Open Design is the explicit open-source alternative ("Open Design is an Apache-2.0 licensed, open-source platform that replicates the artifact-first workflow of Anthropic's Claude Design without proprietary lock-in"). Open Design's `import/claude-design` endpoint exists specifically to migrate users.
- **Released**: April 17, 2026 — the day after [[wiki/entities/opus-4-7|Opus 4.7]] (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Model**: runs on [[wiki/entities/opus-4-7|Opus 4.7]] (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Access / pricing**: paid-only, inside an existing Claude subscription at `claude.ai/design`; requires at least a Pro plan. Pro / Max 5x / Max 20x get different weekly quotas, separate from regular Claude and Claude Code usage; a single high-fidelity design can consume a significant chunk of the weekly allowance (per [[wiki/sources/nateherk-claude-design-tally-brand]], [[wiki/sources/prajwaltomar-claude-design-workflow]]).
- **Verifier loop**: after every render it screenshots its own output, inspects it, and fixes broken elements before the user sees them (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Output types**: prototypes, slide decks/presentations, landing pages, animated websites, LinkedIn carousels/infographics, sales proposals/one-pagers, onboarding guides/PDFs, product UI/app designs, mobile mockups, and short brand videos (per both 2026 walkthroughs).
- **Opening modes**: Prototype, Slide deck, From template, Other; Prototype mode offers Wireframe (rough structure) and High Fidelity (polished) (per [[wiki/sources/prajwaltomar-claude-design-workflow]]).
- **Design.md / Design Systems**: generates a `Design.md` spec that becomes a reusable source of truth; has a Design Systems tab (right-side panel) where users create/name a design system and refine it via a "needs work" feedback loop (per both walkthroughs).
- **Templates**: an Examples tab offers pre-built designs to browse; templates are saved via Share → Duplicate as Template and reused via From Template (per [[wiki/sources/prajwaltomar-claude-design-workflow]]).
- **In-canvas editing tools**: Direct edit, Comments, Draw, and Tweaks panel (per both walkthroughs).
- **Hand-off to Claude Code**: via zip download or a generated/copied command to build the design into a real app (per both walkthroughs).
- **Mobile**: optimizes for desktop by default; does not auto-optimize for mobile (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **File uploads**: cap around 30–40MB (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Status**: described as still a research preview with bugs such as text overlap and weird rendering on certain layouts (as of May 2026, per [[wiki/sources/prajwaltomar-claude-design-workflow]]).

## Positions and claims

- **The artifact-first paradigm**: a single self-contained HTML output as the agent's primary artifact, rendered in a sandboxed preview, exportable to multiple formats (HTML, PDF, PPTX, ZIP, Markdown). This pattern predates and underlies Open Design's architecture. See [[artifact-first-workflow]].

## Open questions

- **Anthropic's roadmap**: how Claude Design fits with [[wiki/entities/anthropic-skills|Anthropic Skills]] and [[wiki/entities/claude-code|Claude Code]] strategically — unsourced.

*(Resolved 2026-06-06: the product surface, modes, in-canvas tools, and access/pricing model are now documented directly in [[wiki/sources/nateherk-claude-design-tally-brand]] and [[wiki/sources/prajwaltomar-claude-design-workflow]].)*

## Mentioned in

- [[wiki/sources/nexu-io-open-design]] — references Claude Design as the proprietary product Open Design replicates.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — the Anthropic product the entire source is about; vision-first design surface used to build the Tally brand end-to-end.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] — the subject tool; first primary source documenting its UI surfaces, modes, and workflow directly.

## Related concepts

- [[artifact-first-workflow]] — the canonical pattern Claude Design introduced.
- [[design-md]] — adjacent (Refero/Open Design DESIGN.md format is downstream of artifact-first thinking).

## Related entities

- [[wiki/entities/anthropic]] — publisher.
- [[wiki/entities/opus-4-7]] — the model Claude Design runs on.
- [[wiki/entities/sonnet-4-6]] — cheaper model operators switch to for in-canvas tweaks.
- [[wiki/entities/mike-krieger]] — Anthropic CPO cited as the product-pedigree reason Claude Design "landed so polished."
- [[wiki/entities/nateherk]] — operator who built a brand end-to-end in Claude Design.
- [[wiki/entities/open-design]] — the open-source alternative.
- [[wiki/entities/refero]] — adjacent design-tooling product, different positioning.
- [[wiki/entities/claude-code]] — Anthropic's coding-agent product.
- [[wiki/entities/anthropic-skills]] — Anthropic's skill collection.
