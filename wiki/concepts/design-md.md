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

- [[wiki/sources/refero-design-systems-for-ai-agents]] — names DESIGN.md as the unit of output for Refero's catalog. Asserts the contents are colors, typography, spacing, and component patterns, but does not include an actual DESIGN.md to inspect. The wiki's understanding of the format is therefore at one level of abstraction; ingesting a real DESIGN.md would deepen it.

## Sub-claims and details

- **Contents (per Refero)**: colors, typography, spacing, component patterns. Possibly also voice/mood descriptors based on the poetic per-brand taglines on Refero's landing page.
- **Distribution**: viewable on the web; also distributable via MCP servers (Refero MCP) so agents can fetch them as a tool call.
- **Format is markdown, not JSON or design-token JSON**. This is a meaningful choice — it favors human-readable reference material agents can absorb in context, not machine-only token files.

## Open questions and contradictions

- **What does an actual DESIGN.md look like?** This wiki has not yet ingested one. Without that, claims about structure remain at the level of "Refero says it contains X, Y, Z." Worth ingesting one or two real examples.
- **Is DESIGN.md a Refero-specific name or a general convention?** Likely the latter (analogous to AGENTS.md, CLAUDE.md, README.md), but unconfirmed from current sources.
- **Relation to design-token standards** (W3C Design Tokens, Style Dictionary): DESIGN.md is plainer-text and seemingly not aimed at toolchain interop — it's aimed at LLMs reading prose. Not addressed in current sources.

## Related concepts

- [[markdown-as-agent-contract]] — the broader pattern DESIGN.md instantiates.
- [[llm-wiki-pattern]] — sibling instance of the same meta-pattern in the personal-knowledge domain.

## Related entities

- [[wiki/entities/refero]] — primary publisher of DESIGN.md files.

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]]
