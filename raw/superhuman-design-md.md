---
title: "Superhuman Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/418b374a-be64-44f0-b17e-1d45308c7e62
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Superhuman's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, superhuman, design-md, refero]
---

# Superhuman Design System — Complete Reference

## Color Palette

**Brand Colors:**
- Aubergine: #421d24 (announcement banner, footer)
- Aubergine Deep: #4e242c (SVG icons, borders)
- Iris: #714cb6 (ghost buttons, links, focus rings)
- Indigo Glow: #353088 (focus shadow on CTAs)
- Lavender Chip: #d4c7ff (sign-up button fill)
- Hero Dusk Gradient: linear-gradient(to left bottom, rgba(168,164,216,0.5), rgba(107,165,232,0.5), rgba(176,112,192,0.6), rgba(144,136,208,0.5))

**Neutrals:**
- Ink: #292827 (primary text, borders)
- Graphite: #666666 (secondary body text)
- Driftwood: #dcd7d3 (dividers, rules)
- Fog: #e3e3e2 (UI dividers, light borders)
- Parchment Canvas: #f2f0eb (primary page background)
- Bone: #ffffff (card surfaces, hero text)

## Typography

**Font:** Super Sans VF (weights: 460, 500, 540, 600, 700; fallback: Inter Variable)

**Type Scale (Minor Third 1.2):**
- Display: 64px, weight 540, line-height 0.96, letter-spacing -0.028em
- Heading-lg: 48px, weight 460, line-height 0.96
- Heading: 28px, weight 540, line-height 1.14
- Heading-sm: 22px, weight 460, line-spacing -0.022em
- Subheading: 18px, weight 540, line-height 1.5
- Body: 16px, weight 460, line-height 1.5
- Caption: 12px, weight 460

## Spacing & Shape

- Base unit: 4px
- Section gap: 64px
- Card padding: 16px
- Element gap: 8px
- Max-width: 1200px

**Border Radius:**
- Buttons: 8px
- Links: 12px
- Cards: 16px
- Cards Large: 24px
- Pills/floating chips: 999px
- Announcement Banner: 16px

## Elevation

- Outlined Ghost Button (Iris focus): rgb(113, 76, 182) 0px 0px 0px 1px inset

## Key Guidelines

**Do:**
- Use #f2f0eb as canvas (never pure white)
- Apply Super Sans VF weight 600–700 for headings with letter-spacing -0.022em to -0.028em
- Use #714cb6 exclusively for outlined borders and links
- Reserve #421d24 for announcement banner and footer only
- Apply backdrop-filter: blur(12px) on glassmorphic panels
- Pair 64px display with line-height 0.96

**Don't:**
- Use #ffffff as page background
- Apply #714cb6 as filled button background
- Use zero or positive letter-spacing on headings
- Mix typefaces beyond Super Sans VF
- Use standard box-shadow elevation
- Place #421d24 in mid-page content
- Use border-radius smaller than 8px on interactive elements
