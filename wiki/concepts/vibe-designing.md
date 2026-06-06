---
type: concept
title: Vibe Designing
created: 2026-06-06
updated: 2026-06-06
aliases: [vibe-design, cold-prompt-design]
tags: [design, ai-design, claude-design, anti-pattern, workflow]
---

# Vibe Designing

> A named anti-pattern in AI design: issuing a single cold prompt that asks the tool to decide colors, fonts, layout, copy, and structure all at once, producing generic, shifting output and an endless token-burning iteration loop.

## Definition

**Vibe designing**, per [[wiki/sources/prajwaltomar-claude-design-workflow]], is the failure mode of asking an AI design tool (Claude Design) to make every design decision at once from a single under-specified prompt — colors, fonts, layout, copy, and structure simultaneously. The result is generic output that shifts unpredictably between iterations, driving an endless, token-burning refinement loop. The entire purpose of the source's workflow is to replace vibe designing with up-front pre-establishment of a [[design-system]]. It is the design-domain analogue of [[vibe-coding]].

## Why it matters

Vibe designing names *why* the structured workflow exists. By isolating the anti-pattern — one cold prompt deciding everything — the source makes the corrective concrete: establish the brand blueprint first so the tool is not improvising every decision per output. It also extends the "vibe X" family from coding into design.

## Treatment across sources

- [[wiki/sources/prajwaltomar-claude-design-workflow]] frames it as a named anti-pattern: a single cold prompt asking Claude Design to decide colors, fonts, layout, copy, and structure at once, producing generic shifting output and an endless token-burning iteration loop. The workflow's entire purpose is to replace it with pre-establishment. Described as the design-domain analogue of vibe coding.

## Sub-claims and details

- It is a single cold prompt that asks the tool to decide colors, fonts, layout, copy, and structure at once. ([[wiki/sources/prajwaltomar-claude-design-workflow]])
- It produces generic output that shifts between iterations. ([[wiki/sources/prajwaltomar-claude-design-workflow]])
- It causes an endless, token-burning iteration loop. ([[wiki/sources/prajwaltomar-claude-design-workflow]])
- The workflow's entire purpose is to replace it with pre-establishment of a design system. ([[wiki/sources/prajwaltomar-claude-design-workflow]])
- It is the design-domain analogue of vibe coding. ([[wiki/sources/prajwaltomar-claude-design-workflow]])

## Open questions and contradictions

- The boundary between "vibe designing" and legitimate exploratory prompting is not sharply drawn by the source — early-stage divergence may resemble the anti-pattern.

## Related concepts

- [[design-system]] — contrasted with: pre-establishing a design system is the corrective for vibe designing.
- [[vibe-coding]] — the coding-domain analogue from which the term is derived.
- [[prompt-engineering]] — the discipline whose absence the anti-pattern exemplifies.

## Related entities

- (Claude Design — referenced in source; not yet cited as a wiki entity here)

## Mentioned in

- [[wiki/sources/prajwaltomar-claude-design-workflow]]
