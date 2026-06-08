---
type: source
title: Airbnb Design System (DESIGN.md from Refero)
created: 2026-05-04
updated: 2026-05-04
content_status: substantive
source_url: https://styles.refero.design/style/airbnb
source_type: design-md
author: Refero
source_date: 2026-05-04
raw_path: raw/airbnb/DESIGN.md
tags: [design-md, design-tokens, airbnb, refero]
---

# Airbnb Design System (DESIGN.md from Refero)

> *"Vacation photos pinned to a white corkboard"* — Airbnb's UI is a warm, airy marketplace built on near-white surfaces (`#f7f7f7` canvas + `#ffffff` cards) with photography doing the visual heavy lifting and a single coral-red `#ff385c` brand heartbeat appearing only on logo, active states, and the search button.

## TL;DR

Airbnb Cereal VF (custom variable font) carries the entire UI typography across weights 400-700. Compact 8-28px type scale with negative letter-spacing at large sizes. Single coral-red brand color rationed strictly. Card images bleed edge-to-edge with **20px rounded corners** — the only generous radius in an otherwise compact information-dense layout. Salt OpenType feature distinguishes Cereal from system sans-serifs.

## Key takeaways

- **One color is the brand**: `#ff385c` (coral red) appears only on logo, active states, the search button. Treated as a signature, not a system color.
- **Photography-first**: barely-there depth (paper on paper) — `#f7f7f7` canvas + `#ffffff` cards. Photography does the visual work; UI gets out of the way.
- **One typeface, one variable family**: Airbnb Cereal VF, weights 400-700. The `salt` feature activates alternate letterforms.
- **Compact information-dense type scale**: 8 / 11 / 12 / 13 / 14 / 16 / 20 / 21 / 22 / 28 px — denser than most catalog entries, suited to listing-heavy marketplace surfaces.
- **One generous radius among many tight ones**: card images at **20px** stand out in a layout where most other elements are tightly squared. Strategic geometric tension.
- **Negative letter-spacing at display sizes**: -0.02em pulls large numerals together — important for prices and rating numbers.

## Notable quotes

> "Vacation photos pinned to a white corkboard."

## Notes

- **Airbnb is now cited at two layers in the wiki**: structure (landing-page patterns) + tokens (DESIGN.md). Together they describe the full Airbnb brand surface.
- **Cereal VF is proprietary** — agents generating Airbnb-voice UI without the typeface will fall back to Inter Variable. Visual identity depends on the typeface being available.
- **Single-color brand discipline** parallels Stripe's single-violet rule and Apple's single-azure rule. Three different brands, same load-bearing decision.

## Mentioned entities

- [[wiki/entities/airbnb]] — graduated from YC-unicorn-stub to design-md-ingested.
- [[wiki/entities/refero]] — publisher of the catalog.

## Related concepts

- [[design-md]] — DESIGN.md format.
- [[markdown-as-agent-contract]] — meta-pattern.
- [[landing-page-patterns]] — companion structural-layer source for Airbnb.

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — catalog source.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — Airbnb's structural landing-page patterns (different layer of analysis on the same brand).
