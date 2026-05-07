---
type: source
title: Base44 Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
source_url: https://styles.refero.design/style/e869e214-f672-4ac3-bfc2-bd25de7b003b
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/base44/DESIGN.md
tags: [design-md, design-tokens, base44, refero]
---

# Base44 Design System (DESIGN.md from Refero)

> *"Softly lit gradient canvas"* — pastel-warm gradients on Canvas Pearl `#faf9f7`, Lime Spritz `#ade900` for CTAs, Wix-hosted custom font hashes ("wfont_343a2a_..."). Distinctly Wix-platform-flavored. Notable for **non-integer border-radii** (7.42183px, 9.89577px, 13.8541px, 741.445px) — likely Figma-export artifacts preserved in the system.

## TL;DR

Base44's identity is gentle gradients (Sky Dream, Warm Horizon) on a Canvas Pearl off-white ground. Two CTA accents: Lime Spritz `#ade900` for primary actions, Blazing Orange `#ff631f` and Sunset Orange `#d8723c` for accents. Type system uses Wix-platform custom fonts (`wfont_343a2a_*` hashes) plus wix-madefor-text-v2 with 0.1em letter-spacing. Border-radius values include strange decimals — looks like preserved-from-Figma values that someone never rounded. Only one shadow (`rgba(34, 40, 42, 0.04) 0px 3px 10px 0px`); explicit instruction to avoid prominent box shadows.

## Key takeaways

- **Wix-flavored typography**: `wfont_343a2a_*` hashed font names indicate this is a Wix-hosted site. Most other Refero brands use named typefaces.
- **Non-integer radii**: 7.42183px, 9.89577px, 13.8541px, 741.445px. These look like Figma px-equivalents that weren't rounded to integers.
- **Two-color accent strategy**: Lime Spritz `#ade900` for CTAs only; Sunset Orange for warm accents. Light Lime `#ebffb1` as a soft secondary.
- **Pastel gradients only**: explicit rule against saturated background colors.
- **999px buttons**: the most aggressive pill convention.
- **Single shadow** for the entire system. Explicit "no prominent box shadows."

## Mentioned entities

- [[wiki/entities/base44]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
