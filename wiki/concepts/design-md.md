---
type: concept
title: DESIGN.md
created: 2026-05-02
updated: 2026-05-02
aliases: [design.md, DESIGN markdown]
tags: [design-systems, ai-agents, markdown, agent-config]
---

# DESIGN.md

> A markdown file format that codifies a product's design system — colors, typography, spacing, components — in a shape that AI coding agents can consume before generating UI.

## Definition

A `DESIGN.md` is a single markdown document that captures the visual and structural design conventions of a product (or a reference style) in plain text. The intent is to give an AI coding agent enough context to generate UI that "looks like" the target style without having to reason from screenshots, parse Figma files, or guess at design tokens. The format is associated most prominently with [[wiki/entities/refero]], which publishes DESIGN.md files extracted from real product websites.

## Why it matters

This concept is one concrete instance of [[markdown-as-agent-contract]] — the broader trend of using markdown as the configuration/contract layer between humans and agents. DESIGN.md is to coding agents what `CLAUDE.md` is to a Claude Code session and what `AGENTS.md` is to Codex: a place to dump the conventions that the agent should respect, in a format the agent natively understands.

For a knowledge worker building UIs with AI assistance, a curated DESIGN.md library (like [[wiki/entities/refero|Refero]]'s) is a way to skip the "describe what you want it to look like" step and instead say "build this in the style of Linear" or "Stripe" or "Anthropic" — pointing the agent at a DESIGN.md that already encodes the relevant choices.

## Treatment across sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — names DESIGN.md as the unit of output for Refero's catalog. Asserts the contents are colors, typography, spacing, and component patterns, but does not include an actual DESIGN.md to inspect.
- [[wiki/sources/stripe-design-md]] — **first concrete DESIGN.md ingested into the brain** (2026-05-02). Validates the format with content: 18 named colors organized brand/gradients/neutrals, a 7-step type scale on `sohne-var`, 4px-base spacing system, 5-radius / 4-shadow vocabulary, 5 token-referenced components (3 buttons + 2 cards), and a one-paragraph design philosophy ("architectural blueprint on white marble"). Resolves the open question "what does an actual DESIGN.md look like?" — at least for Refero's flavor.

## Sub-claims and details

### What's actually in a Refero DESIGN.md (per [[wiki/sources/stripe-design-md]])

A concrete DESIGN.md from Refero contains, in this rough order:

1. **Color palette** — split into Brand / Gradients / Neutrals subsections. Each color has a **descriptive name** (e.g. "Deep Violet", "Powder Blue") and a hex code. Gradients are CSS gradient strings.
2. **Typography** — font family + fallback + a per-step type scale specifying size, weight, line-height for ~7 named scale steps (display, heading-lg, heading, heading-sm, subheading, body, caption). Letter-spacing rules called out separately.
3. **Spacing & Shapes** — base unit (commonly 4px), a few named gaps (element / card-padding / section), border-radius per use case (interactive vs. layout), shadow vocabulary (named, e.g. xl / xl-2 / xl-3 / sm).
4. **Components** — a small set of token-referenced components (buttons, cards) specified as `<role>: <bg-token>, <fg-token>, <radius>, <padding>` strings. The components reference earlier-defined tokens, not raw values.
5. **Design philosophy** — one short paragraph. Provides the *why* the tokens decode to. *"Architectural blueprint on white marble — quiet efficiency, where information is paramount."*

The shape is consistent enough that an agent reading any Refero DESIGN.md can extract the same fields. Other DESIGN.md flavors (non-Refero) may differ, but Refero's instantiation is well-defined.

### General properties

- **Distribution**: viewable on the web; also distributable via MCP servers (Refero MCP) so agents can fetch them as a tool call.
- **Format is markdown, not JSON or design-token JSON**. This is a meaningful choice — it favors human-readable reference material agents can absorb in context, not machine-only token files.
- **Token references, not literals**: components reference named tokens (`Deep Violet`) rather than raw values (`#533afd`). This is what makes a DESIGN.md actionable for variant generation — swap the token, the component still has the right shape.
- **Necessarily partial**: Stripe's DESIGN.md has no icon system, no motion tokens, no breakpoint definitions, no z-index scale, no form-state colors. A DESIGN.md captures what the brand *wants enforced* and trusts the agent to fill in the rest from the philosophy.

## Open questions and contradictions

- **Variation between brands**: Stripe is one DESIGN.md. Linear, Apple, Anthropic etc. may follow the same Refero shape or differ. Worth ingesting a second one to compare.
- **Is DESIGN.md a Refero-specific name or a general convention?** Likely the latter (analogous to AGENTS.md, CLAUDE.md, README.md), but unconfirmed from current sources.
- **Relation to design-token standards** (W3C Design Tokens, Style Dictionary): DESIGN.md is plainer-text and seemingly not aimed at toolchain interop — it's aimed at LLMs reading prose. The Refero page mentions Tailwind v4, CSS Variables, and Design Tokens as alternate export formats — so the markdown is the human-readable surface and the structured exports are the toolchain surface.

## Related concepts

- [[markdown-as-agent-contract]] — the broader pattern DESIGN.md instantiates.
- [[llm-wiki-pattern]] — sibling instance of the same meta-pattern in the personal-knowledge domain.

## Related entities

- [[wiki/entities/refero]] — primary publisher of DESIGN.md files.
- [[wiki/entities/stripe]] — first brand whose DESIGN.md has been ingested.

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
