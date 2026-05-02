---
title: "Linear Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Linear's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, linear, design-md, refero]
---

# Linear Design System - Complete Reference

## Color Palette

**Brand:**
- Neon Lime: `#e4f222` - Primary action indicators, active states, focus elements

**Accents:**
- Aether Blue: `#5e6ad2` - Decorative highlights, background elements
- Cyan Spark: `#02b8cc` - Informational highlights, icon fills
- Deep Violet: `#6366f1` - Background accents in content blocks
- Amethyst: `#8b5cf6` - Violet variant for backgrounds

**Neutrals:**
- Pitch Black: `#08090a` - Page background, primary surface
- Graphite: `#0f1011` - Elevated card backgrounds
- Deep Slate: `#161718` - Secondary elevated card backgrounds
- Charcoal Grey: `#23252a` - Borders, shadowed card surfaces
- Muted Ash: `#323334` - Subtle borders, dividers
- Gunmetal: `#383b3f` - Tertiary backgrounds, input borders
- Fog Grey: `#62666d` - Muted text for metadata
- Storm Cloud: `#8a8f98` - Tertiary text, descriptive labels
- Light Steel: `#d0d6e0` - Secondary text and borders
- Alabaster: `#e5e5e6` - Informational borders, code blocks
- Porcelain: `#f7f8f8` - Primary text and icons

**Semantic:**
- Forest Green: `#008d2c` - Positive status indicators
- Emerald: `#27a644` - Success/completion states
- Warning Red: `#eb5757` - Error/warning states

## Typography

**Primary Font:** Inter Variable
- Weights: 300, 400, 510, 590
- Sizes: 10–72px (14 values)
- Line height: 1–2.75 (11 values)
- Letter spacing: -0.22–-0.1px (6 values)
- Fallback: Inter

**Code Font:** Berkeley Mono
- Weight: 400
- Sizes: 12px, 13px, 14px
- Line height: 1.30, 1.40, 1.50, 1.71
- Letter spacing: -0.15
- Fallback: IBM Plex Mono

**Type Scale (Minor Third 1.2 from 16px base):**
| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| display | 72px | 510 | 1 | -0.22px |
| heading-lg | 48px | 510 | 1.2 | -0.22px |
| heading | 24px | 400 | 1.33 | -0.22px |
| 20px | 20px | 590 | 1.33 | — |
| 17px | 17px | 590 | 1.6 | — |
| body | 16px | 400 | 1.5 | -0.13px |
| 15px | 15px | 400 | 1.6 | — |
| caption | 10px | — | 1.4 | -0.1px |

## Spacing & Shape

**Base Unit:** 4px
**Density:** Compact

**Spacing Scale:**
4px, 8px, 12px, 16px, 20px, 24px, 28px, 32px, 36px, 40px, 48px, 56px, 64px, 80px, 96px, 128px

**Border Radius:**
- pill: 9999px
- tags: 2px
- badges: 4px
- cards: 6px
- inputs: 6px
- buttons: 6px
- default: 6px

**Layout Values:**
- Section gap: 24px
- Card padding: 12px
- Element gap: 8px

## Shadows

- sm: rgba(0, 0, 0, 0.4) 0px 2px 4px 0px
- md: rgba(0, 0, 0, 0.2) 0px 0px 12px 0px inset
- subtle: rgb(35, 37, 42) 0px 0px 0px 1px inset
- subtle-2: rgba(0, 0, 0, 0.2) 0px 0px 0px 1px
- subtle-3: rgba(0, 0, 0, 0.01) 0px 5px 2px 0px, rgba(0, 0, 0, 0.04) 0px 3px 2px 0px, rgba(0, 0, 0, 0.07) 0px 1px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 1px 0px
- xl: rgba(8, 9, 10, 0.6) 0px 4px 32px 0px
- subtle-4: rgba(0, 0, 0, 0.1) 0px 0px 0px 2px
- subtle-5: rgba(0, 0, 0, 0.33) 0px 0px 0px 1px
- subtle-6: rgba(255, 255, 255, 0.03) 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.04) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.6) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 4px 0px

## Design Philosophy

Linear embodies a "sophisticated and focused dark-mode experience, reminiscent of a command center dashboard." The system prioritizes "depth without harsh contrasts" through "subtle gradients and layered surfaces," with interaction guided by "a single vivid lime green (#e4f222), applied selectively to primary calls to action."

## Component Patterns

**Primary Action Button:** Neon Lime background, Pitch Black text, 6px border-radius, variable padding

**Ghost Navigation Button:** Transparent background, Porcelain text, no padding, 0px border-radius

**Subtle Link Button:** Transparent background, Light Steel text, 6px border-radius, minimal padding (6px horizontal)

**Navigation Item Button:** Transparent background, Storm Cloud text, 2px border-radius, no padding

**Default Card:** Graphite background, 6px border-radius, 8px padding, shadow-sm

**Elevated Card:** Deep Slate background, 12px top border-radius (0px bottom), 24px vertical padding, inset shadow

**Input Field:** Transparent background, Porcelain text, Charcoal Grey border, 6px border-radius, 12px/14px padding

**Badge:** Gunmetal background, Storm Cloud text, 4px border-radius, 0px/6px padding

## Key Guidelines

**Do:**
- Use Pitch Black for primary page backgrounds
- Apply Porcelain for all primary text and important icons
- Restrict Neon Lime to primary interactive elements exclusively
- Create depth through layered surfaces (Pitch Black, Graphite, Deep Slate)
- Use Inter Variable with specific letter-spacing adjustments
- Apply 6px border-radius consistently for buttons, cards, inputs
- Use Storm Cloud for secondary text

**Don't:**
- Introduce additional bright colors beyond Neon Lime
- Avoid harsh white backgrounds or light-themed patterns
- Don't deviate from specified typefaces
- Refrain from strong, diffuse shadows
- Don't apply broad decorative gradients
- Avoid generic border-radii
- Don't use large amounts of white space
