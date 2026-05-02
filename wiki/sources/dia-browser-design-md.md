---
type: source
title: Dia Browser Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-02
source_url: https://styles.refero.design/style/b458ca1a-70f0-4f85-b745-f879a4d08457
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/dia-browser-design-md.md
tags: [design-md, design-tokens, dia-browser, refero]
---

# Dia Browser Design System (DESIGN.md from Refero)

> *"Prism on white stationery"* — 5-stop spectrum gradient as ambient brand element, ABC Oracle 300-weight display, large radii (30px buttons, 40px containers, 9999px ghost pills). One shadow only. **8px base unit** (most other brands are 4px).

## TL;DR

Dia Browser's identity is the spectrum gradient (pink → red-orange → marigold → ice blue → signal blue) used **only as ambient glow or decorative strip**, never as background fill. ABC Oracle (300/400/500) display with aggressive negative tracking (-2.88px at 72px). 8px base unit (vs. typical 4px) makes the system feel notably airier. Single shadow `rgba(0, 0, 0, 0.08) 0px 0px 8px 0px` for floating cards; backdrop-filter blur(24px) on elevated surfaces. Generous radii throughout — 30px on cards/buttons, 40px on containers, 9999px on ghost buttons.

## Key takeaways

- **8px base unit** is rare — 1.5-2x more spacious than 4px-base brands.
- **Spectrum gradient** is decorative-only. Buttons stay neutral (`#d9d9d9`) or transparent.
- **No font weight above 500** (rule), no border-radius below 10px (rule).
- **Single shadow** for the entire system.
- **ABC Oracle 300** for display sizes 50px+ with -0.04em tracking — light + tight.
- **Backdrop blur 24px** as elevation mechanism on white-translucent surfaces.

## Mentioned entities

- [[wiki/entities/dia-browser]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
