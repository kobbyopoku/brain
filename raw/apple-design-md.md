---
title: "Apple Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/c9cabb96-32fa-4896-837a-f2497ce1c856
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Apple's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, apple, design-md, refero]
---

# Apple Design System — Complete Reference

## Color Palette

**Brand Colors:**
- Azure: `#0071e3` — "Primary CTA button fill, active nav 'Buy' button"
- Cobalt Link: `#0066cc` — "Inline text links, navigation anchor colors"

**Gradients:**
- Citrus: `linear-gradient(184deg, rgb(29, 29, 31) 0%, rgb(223, 231, 79) 33%, rgb(94, 156, 42) 66%, rgb(10, 134, 26) 95%)`
- Indigo: `linear-gradient(184deg, rgb(29, 29, 31) 20%, rgb(168, 211, 251) 43%, rgb(0, 18, 249) 76%, rgb(37, 53, 224) 95%)`
- Blush: `linear-gradient(184deg, rgb(29, 29, 31) 20%, rgb(243, 196, 246) 43%, rgb(245, 0, 180) 76%, rgb(204, 41, 188) 95%)`

**Product Swatches:**
- Citrus Finish: `#dddc8c`
- Blush Finish: `#e8d0d0`
- Indigo Finish: `#596680`

**Neutrals:**
- Obsidian: `#000000`
- Ink: `#1d1d1f`
- Ash: `#333333`
- Slate: `#474747`
- Graphite: `#707070`
- Silver Mist: `#e8e8ed`
- Fog: `#f5f5f7`
- Snow: `#ffffff`

**Semantic:**
- Caution: `#b64400`

## Typography

**SF Pro Display** (Display Headlines)
- Weights: 600, 700
- Sizes: 21–96px
- Line height: 1.04–1.20
- Letter spacing: -0.022em to +0.004px
- Fallback: Inter, system-ui

**SF Pro Text** (Body & UI)
- Weights: 300, 400, 500, 600
- Sizes: 12–44px
- Line height: 1.24–1.50
- Letter spacing: -0.022em to -0.003px
- Fallback: Inter, system-ui

**Type Scale:**
| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| caption | 12px | — | 1.33 | -0.26px |
| body-sm | 14px | — | 1.43 | -0.04px |
| body | 17px | 400 | 1.47 | -0.1px |
| subheading | 20px | 300 | 1.4 | -0.2px |
| heading-sm | 24px | 600 | 1.29 | -0.36px |
| heading | 40px | 600 | 1.17 | -0.6px |
| heading-lg | 56px | 700 | 1.07 | -0.9px |
| display | 96px | 700 | 1.04 | -2.11px |

## Spacing & Shape

**Base Unit:** 4px | **Max Width:** 1200px | **Section Gap:** 80–120px | **Card Padding:** 28px | **Element Gap:** 10px

**Border Radius:**
- Small buttons: 10px
- Cards: 28px
- Feature links: 28px
- Rounded buttons: 36px
- Nav items: 980px

## Core Design Principles

**Do:**
- "Use 28px border-radius for all feature cards — this exact value is the page's geometric signature"
- "Reserve #0071e3 exclusively for the primary 'Buy' CTA button"
- "Apply negative letter-spacing scaled to font size: -2.11px at 96px display, -0.9px at 56px"
- "Use #f5f5f7 as page canvas and #ffffff as card surface"
- "Set SF Pro Display weight 700 for all primary product headlines at 56px and above"
- "Use rgba(210,210,215,0.64) with backdrop-filter blur(20px) for temporary overlay controls"

**Don't:**
- "Do not add box-shadow to any card or container"
- "Do not use #0066cc for button backgrounds"
- "Do not use font weight 300 for headlines below 40px"
- "Do not place two rounded-pill buttons side by side"
- "Do not use product finish colors as semantic UI accents"
- "Do not use positive letter-spacing on SF Pro Display at sizes above 28px"
- "Do not center-align body paragraphs longer than 2 lines"
