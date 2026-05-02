---
title: "Dia Browser Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/b458ca1a-70f0-4f85-b745-f879a4d08457
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Dia Browser's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, dia-browser, design-md, refero]
---

# Dia Browser Design System — Complete Reference

## Color Palette

**Brand Spectrum Gradient:** `linear-gradient(90deg, rgb(198, 121, 196) 0%, rgb(250, 61, 29) 25%, rgb(255, 176, 5) 50%, rgb(225, 225, 254) 75%, rgb(3, 88, 247) 100%)`

**Accent Colors:**
- Rose Quartz: `#c679c4`
- Marigold: `#ffb005`
- Signal Blue: `#0358f7`
- Hot Pink: `#fd02f5`

**Neutrals:**
- Ink Black: `#000000`
- Graphite: `#636363`
- Ash: `#7c7c7c`
- Slate: `#959595`
- Steel: `#aeaeae`
- Pebble: `#d9d9d9`
- Fog: `#efefef`
- Canvas: `#f8f8f8`
- Snow: `#ffffff`

## Typography

**Typeface:** ABC Oracle (weights: 300, 400, 500)

**Scale (16px base, Minor Third 1.2):**
- Display: 72px, weight 300, line-height 1.17, tracking -2.88px
- Heading-lg: 54px, weight 300, line-height 1.11, tracking -2.16px
- Heading: 50px, weight 400, line-height 1.5, tracking -2px
- Heading-sm: 22px, weight 400, line-height 1.18, tracking -0.44px
- Subheading: 18px, weight 400, line-height 1.33
- Body: 16px, weight 400, line-height 1.25
- Body-sm: 14px, weight 400, line-height 1.21
- Caption: 13px, weight 400, line-height 1.23

## Spacing & Shape

**Base unit:** 8px
**Density:** Spacious
**Max-width:** 1200px
**Section gap:** 80–120px
**Card padding:** 32px
**Element gap:** 15–20px

**Border Radius:**
- Images: 10px
- Nav items: 16px
- Cards: 30px
- Buttons: 30px
- Containers: 40px
- Pill buttons: 9999px

**Shadow:** `rgba(0, 0, 0, 0.08) 0px 0px 8px 0px` (only shadow in system)

## Key Guidelines

**Do:**
- Use spectrum gradient exclusively as ambient glow or decorative strip
- Keep buttons neutral (`#d9d9d9`) or transparent
- Apply 30px radius to cards/buttons; 9999px for ghost buttons
- Use weight 300 display (50px+) with -0.04em tracking
- Apply `backdrop-filter: blur(24px)` with `rgba(255,255,255,0.9)` for elevated surfaces
- Maintain the single 8px blur shadow on floating cards
- Use `#636363` for body, `#959595` for tertiary text

**Don't:**
- Never use saturated colors as solid backgrounds
- No border-radius below 10px
- No font weights above 500
- No layered/colored shadows beyond the single 8px blur
- No dark section backgrounds
- No underlined links with color changes
- No secondary typeface
