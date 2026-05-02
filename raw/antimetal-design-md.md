---
title: "Antimetal Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/9f9a4a4f-1a27-47ca-a65b-68b9850a84e4
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Antimetal's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, antimetal, design-md, refero]
---

# Antimetal Design System - Complete Reference

## Brand Concept
"Electric storm over a blueprint — vivid neon signal cutting through deep navy atmosphere, then snapping to precise technical daylight."

The design operates in two coexisting visual modes: a dark navy-to-electric-blue hero and a near-white product surface, with a vivid chartreuse accent bridging both.

## Color Palette

**Brand Colors:**
- Midnight Navy: #1b2540
- Deep Cosmos: #001033
- Chartreuse Pulse: #d0f100
- Ice Veil: #e0f6ff

**Neutrals:**
- Ghost Canvas: #f8f9fc
- Pure Surface: #ffffff
- Storm Gray: #596075
- Slate Ink: #6b7184
- Ash Medium: #7c8293
- Fog Border: #b1b5c0

**Gradients:**
- Hero: linear-gradient(180deg, #001033 0%, #0050f8 55%, #5fbdf7 100%)
- Blue Glow Radial: radial-gradient with rgba(0, 128, 248, 0.32) to transparent

## Typography

**abcdFont (UI):**
- Weights: 400, 450, 480
- Sizes: 13–28px
- Letter-spacing: -0.016em to -0.005em (tighter at smaller sizes)
- Fallback: Inter Variable or DM Sans

**ivarTextFont (Display):**
- Weight: 400 only
- Sizes: 32px, 40px, 46px, 48px
- Letter-spacing: -0.010em uniformly
- OpenType features: ss04, ss06, ss09, ss10, ss11
- Fallback: Freight Display Pro or Fraunces

**Type Scale:**
- display: 48px, 1.04 line-height, -0.48px tracking
- heading-lg: 40px, 1.05, -0.4px
- heading: 28px, 1.17, -0.14px
- heading-sm: 22px, 1.29, -0.22px
- subheading: 18px, 1.33, -0.09px
- body: 16px, 1.5, -0.16px
- caption: 13px, 1.0, -0.21px

## Spacing & Layout

**Base Unit:** 4px
**Density:** Compact
**Page Max-width:** 1200px
**Section Gap:** 80px
**Card Padding:** 20px
**Element Gap:** 8px

**Spacing Scale:**
4px, 8px, 12px, 16px, 20px, 24px, 28px, 32px, 56px, 60px, 72px, 96px, 160px, 232px

## Border Radius

- buttons: 9999px (pill shape)
- cards: 20px
- cardsSmall: 6px
- cardsMedium: 16px
- badges: 16px
- pillLarge: 60px
- inputs: 0px

## Shadows

- md: rgba(0, 39, 80, 0.08) 0px 6px 16px -3px, rgba(0, 39, 80, 0.04) 0px 0px 0px 1px
- xl: rgba(0, 39, 80, 0.03) 0px 56px 72px -16px, rgba(0, 39, 80, 0.03) 0px 32px 32px -16px, rgba(0, 39, 80, 0.04) 0px 6px 12px -3px, rgba(0, 39, 80, 0.04) 0px 0px 0px 1px
- subtle: rgba(255, 255, 255, 0.72) 0px 1px 1px inset plus layered blue shadows
- md-2: rgba(255, 255, 255, 0.08) inset 4x layered
- subtle-2: color(srgb 0.878 0.965 1 / 0.24) inset
- subtle-3: rgba(24, 37, 66, 0.32) 0px 1px 3px plus 5-layer stack
- subtle-4: rgba(255, 255, 255, 0.88) inset plus 4-layer shadow stack

## Component Patterns

**Chartreuse CTA Button:** #d0f100 fill, #1b2540 text, 9999px radius, 0-24px padding, ~40px height. Used exclusively for primary conversion actions.

**Dark Ghost Button:** Transparent fill, #fafeff text/border, 9999px radius, inset white glow (4x layers). Secondary action on dark hero.

**Light Ghost Button:** Transparent fill, #1b2540 text/border, 9999px radius, 8-24px padding. Border via box-shadow with 1px outer ring.

**Feature Card:** #ffffff fill, 20px radius, 4-layer shadow stack including outer 1px ring.

**Badge Pill:** 16px radius, rgba(255,255,255,0.01) fill, #1b2540 text at 14px, 12-20px padding, md shadow + 1px ring.

**Text Input:** 0px radius, transparent background, #1b2540 text/border, 15-20px padding.

## Design Guidelines

**Do:**
- Use 9999px radius on all buttons and interactive pills
- Reserve #d0f100 exclusively for primary CTA fills
- Apply blue-tinted shadows rgba(0,39,80,...) for elevation
- Use ivarTextFont with OpenType features only at 32px+
- Maintain single dark hero section, rest on #f8f9fc
- Apply letter-spacing -0.016em to -0.005em on abcdFont
- Use 1px outer shadow ring as border substitute

**Don't:**
- Use #d0f100 in hero or for decorative fills
- Apply non-9999px radius to buttons
- Mix ivarTextFont below 32px
- Exceed two surface levels (#f8f9fc + #ffffff)
- Create additional dark sections beyond hero
- Use black-based text (#000000); use #1b2540
- Round input borders (0px by design)
