---
type: source
title: Anthropic Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
source_url: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/anthropic-design-md.md
tags: [design-md, design-tokens, anthropic, refero]
---

# Anthropic Design System (DESIGN.md from Refero)

> *"Research journal printed on warm stone — authoritative typographic composition where word-level underlines replace color as the primary emphasis mechanism."* The most editorial DESIGN.md in the Refero catalog so far. Notable because Anthropic is the maker of Claude — the platform this entire wiki runs on.

## TL;DR

Anthropic's system is type-first, color-light, and **explicitly anti-shadow** ("zero box-shadows throughout"). Three custom typefaces (Anthropic Sans, Serif, Mono) carry the load. Six accent colors (Clay, Ember, Olive, Sky, Fig, Cactus) function as **thematic tag/category variants**, not decorative. Neutrals are warm and stone-like (Ivory family `#faf9f5`/`#f0eee6`/`#e8e6dc`/`#e3dacc`; Cloud + Slate scales for mid-tones). Headline emphasis comes from word-level underlines, never color. The "Try Claude" button is asymmetric (flat top, rounded bottom) — a deliberate brand signature.

## Key takeaways

- **Three custom Anthropic typefaces** (Sans + Serif + Mono) — most brands use a single proprietary typeface plus fallbacks.
- **Display heading hierarchy**: 91px Serif weight 400 → 61px Sans weight 700 with -1.22px tracking → 24px Sans weight 600. Big jumps; no intermediate sizes.
- **Underline-as-emphasis** replaces color highlighting. *"Headline emphasis via underline only, never color."*
- **Asymmetric primary button**: flat top, rounded bottom (radius `0px 0px 8px 8px`) for "Try Claude" CTA. A real brand signature.
- **Warm-stone neutrals**: Ivory `#faf9f5` page ground, Oat `#e3dacc` tertiary surfaces, Cloud `#87867f` secondary text. Genuinely warm vs. Stripe's blue-tinted cool-temperature neutrals.
- **Six accent colors as thematic tags**, not as hierarchy. Clay/Ember/Olive/Sky/Fig/Cactus rotate by section/category, not by importance.
- **Zero shadows. Hard-edged transitions.** A counterpoint to most other Refero brands.

## Notable quotes

> "Research journal printed on warm stone."

> "Never use pure white or pure black as surfaces."

> "Headline emphasis via underline only, never color."

## Notes

- **Cross-cuts with the wider wiki**: Anthropic operates [[wiki/entities/claude-code]], the platform this brain runs on. The design system implicit in the brain's own claude.ai/Claude Code UI is consistent with this DESIGN.md (warm neutrals, serif display, underline-emphasis).
- **Comparison to Stripe**: both use a small accent palette with discipline, but Stripe has *one* identity color (Deep Violet), Anthropic has *six* thematic accents. Different strategies for the same problem (palette discipline at scale).
- **The asymmetric button** is the kind of detail that an LLM with this DESIGN.md loaded could reproduce exactly — `border-radius: 0 0 8px 8px` is unambiguous.

## Mentioned entities

- [[wiki/entities/anthropic]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]] — sibling for cross-comparison; opposite color-temperature philosophy.
