---
title: "Column Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/a76ec6ba-20b3-495c-9d89-1e58281e79e7
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Column's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, column, design-md, refero]
---

# Column Design System - Complete Reference

## Color Palette

**Brand Colors:**
- Deep Plum: #111a4a
- Soft Horizon Gradient: linear-gradient(125deg, rgb(214, 86, 32) -3.16%, rgb(159, 122, 238) 14.55%, rgb(69, 117, 205) 32.26%, rgb(113, 210, 240) 49.97%, rgb(68, 180, 139) 67.68%, rgb(244, 223, 105) 85.39%)
- Faded Grid Blue: #023247
- Radial Twilight Gradient: radial-gradient(29.88% 184.91% at 6.55% -48.11%, rgb(119, 28, 134) 0%, rgb(17, 26, 74) 100%)

**Accent Colors:**
- Action Orange: #ec652b
- Callout Cyan: #167e6c
- Notification Teal: #88deeb

**Neutrals:**
- Code Black: #000000
- Ink Blue: #011821
- Graphite: #12161
- Charcoal Text: #232730
- Slate Text: #7c7f88
- Steel Gray: #e3e4e8
- Fog Gray: #f6f6f8
- Ghost White: #ffffff

**Semantic:**
- Success Moss: #44b48b
- Info Blue: #7ea7e9

## Typography

**Primary: SuisseIntl**
- Weights: 300, 400, 500, 600
- Sizes: 11–60px (12 values)
- Line height: 1–1.5 (8 values)
- Letter spacing: -0.03em, -0.02em, -0.01em
- Fallback: Inter
- Usage: "all main content, headings, and UI elements"

**Code: SFMono**
- Weight: 400
- Sizes: 10px, 12px
- Line height: 1.50
- Letter spacing: normal
- Fallback: IBM Plex Mono

**Body: Inter**
- Weights: 400, 500, 600
- Sizes: 10–24px (6 values)
- Line height: 1–1.5 (5 values)
- Letter spacing: -0.03em, -0.02em

**Secondary Monospace: SuisseIntlMono**
- Weight: 400
- Sizes: 10px, 12px, 14px
- Line height: 1.50
- Letter spacing: normal
- Fallback: IBM Plex Mono

### Type Scale
| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| caption | 10px | 400 | 1.5 | — |
| body | 14px | 400 | 1.5 | -0.28px |
| subheading | 18px | 400 | 1.4 | -0.36px |
| heading-sm | 24px | 500 | 1.33 | -0.48px |
| heading | 40px | 500 | 1.1 | -0.8px |
| display | 48px | 500 | 1.1 | -1.44px |

## Spacing & Shape

**Base unit:** 4px
**Density:** comfortable
**Section gap:** 48px

### Spacing Scale
4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 72px, 80px, 96px, 100px, 144px

### Border Radius
- subtle: 2px
- cards: 8px
- buttons: 8px
- default: 8px

### Shadows
- Shadow 1 (subtle): rgba(17, 26, 74, 0.1) 0px 1px 3px 0px, rgba(17, 26, 74, 0.05) 0px 1px 0px 0px, rgba(255, 255, 255, 0.5) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.5) 0px 1px 4px 0px inset
- Shadow 2 (subtle-2): rgba(87, 90, 100, 0.12) 0px 0px 0px 1px
- Shadow 3 (subtle-3): rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset
- Shadow 4 (xl): rgba(0, 0, 0, 0.02) 0px 40px 32px 0px, rgba(0, 0, 0, 0.03) 0px 22px 18px 0px, rgba(0, 0, 0, 0.03) 0px 12px 10px 0px, rgba(0, 0, 0, 0.04) 0px 7px 5px 0px, rgba(0, 0, 0, 0.07) 0px 3px 2px 0px
- Shadow 5 (sm): rgba(0, 0, 0, 0.05) 0px 4px 8px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px, rgba(0, 0, 0, 0.1) 0px 1px 1px 0px
- Shadow 6 (subtle-4): rgba(0, 0, 0, 0.1) 0px 1px 2px 0px, rgb(255, 255, 255) 0px 0px 0px 1px inset
- Shadow 7 (subtle-5): rgba(0, 0, 0, 0.1) 0px 1px 2px 0px

## Design Guidelines

**Do:**
- Use Fog Gray (#f6f6f8) for secondary section backgrounds
- Apply SuisseIntl with -0.02em to -0.03em letter-spacing for headlines 28px+
- Use Steel Gray (#e3e4e8) for interactive element borders
- Maintain 8px border-radius for cards and buttons
- Emphasize critical actions with Action Orange (#ec652b)
- Reserve Deep Plum (#111a4a) for non-primary interactive elements
- Use SFMono or SuisseIntlMono at 10-12px for numerical data and code
- Apply card shadow: "rgba(17, 26, 74, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 2px 0px, rgba(255, 255, 255, 0.5) 0px 0px 0px 1px inset"

**Don't:**
- Avoid generic blue for primary interactive elements
- Don't use vivid colors arbitrarily; reserve semantic colors
- Don't deviate from 8px border-radius for primary UI
- Avoid heavy, opaque box-shadows
- Don't use Code Black (#000000) for large text blocks
- Don't introduce new typefaces
- Don't break 48px section gap vertical rhythm

## Design Philosophy

"Architectural blueprint on white marble. Subtle background patterns convey structure beneath a pristine, luminous surface, punctuated by precise, high-contrast markers."

Column blends "corporate authority and digital precision" using "a very light, almost invisible dotted grid background to evoke a technical blueprint, while maintaining a clean, spacious feel."
