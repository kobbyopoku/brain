---
title: "Anthropic Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Anthropic's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, anthropic, design-md, refero]
---

# Anthropic Design System - Complete Reference

## Color Palette

**Accent Colors:**
- Clay: `#d97757` – Accent CTAs, highlight states
- Accent Ember: `#c6613f` – Deeper accent state, hover/pressed
- Olive: `#788c5d` – Thematic tag/category variant
- Sky: `#6a9bcc` – Thematic tag/category variant
- Fig: `#c46686` – Thematic tag/category variant
- Cactus: `#bcd1ca` – Thematic tag/category variant

**Neutral Scale:**
- Slate Dark: `#141413` – Primary text, borders, icon fills
- Slate Medium: `#3d3d3a` – Mid-dark borders, focus rings
- Slate Light: `#5e5d59` – Tertiary text, captions
- Cloud Dark: `#87867f` – Secondary text, meta labels
- Cloud Medium: `#b0aea5` – Disabled borders, muted UI
- Cloud Light: `#d1cfc5` – Dividers, hairline borders
- Oat: `#e3dacc` – Tertiary surface backgrounds
- Ivory Dark: `#e8e6dc` – Body text on dark, dividers
- Ivory Medium: `#f0eee6` – Nav backgrounds, secondary surfaces
- Ivory Light: `#faf9f5` – Page background, button fills

## Typography

**Font Families:**
- Anthropic Sans (weights: 400, 500, 600, 700) – UI chrome, navigation, body
- Anthropic Serif (weights: 400, 600) – Display headlines, editorial content
- Anthropic Mono (weight: 400) – Technical labels, metadata

**Type Scale (Major Third 1.25 from 12px base):**
- Display: 91px, weight 400, line-height 1.1
- Heading-lg: 61px, weight 700, line-height 1.1, -1.22px tracking
- Heading: 24px, weight 600, line-height 1.3, -0.12px tracking
- Heading-sm: 20px, weight 400, line-height 1.4
- Subheading: 18px, weight 600, line-height 1.4
- 16px: weight 400, line-height 1.0
- Body-sm: 15px, weight 400, line-height 1.4
- Caption: 12px, weight 400, line-height 1.4

**Sans Letter Spacing:** -0.02em at 61px, -0.005em at 24px, -0.002em at 15-16px

## Spacing & Layout

- Base unit: 4px
- Max-width: 1200px
- Section gap: 61px
- Card padding: 31px
- Element gap: 8-16px

**Border Radius:**
- Cards: 8px
- Panels: 16px
- Featured Cards: 24px
- Buttons: 0px (except "Try Claude" CTA: 0px 0px 8px 8px asymmetric)

## Component Patterns

**Primary "Try Claude" Button:** Background `#faf9f5`, text `#141413`, 1px border `#141413`, asymmetric radius (flat top/rounded bottom), padding 12px 31px, Anthropic Sans 15px weight 500

**Dark Feature Card:** Background `#141413`, radius 24px, padding 31px, Anthropic Serif 91px weight 400 in `#faf9f5`

**Release Card Grid:** Background `#f0eee6` or `#e3dacc`, radius 8px, padding 31px, Anthropic Sans 20px weight 600 headline

**Metadata Labels:** "Anthropic Mono 16px for DATE, CATEGORY labels" in card footers

## Design Philosophy

"Research journal printed on warm stone — authoritative typographic composition where word-level underlines replace color as the primary emphasis mechanism."

**Key Principles:**
- Never use pure white or pure black as surfaces
- Headline emphasis via underline only, never color
- Zero box-shadows throughout
- Hard-edged surface transitions
- Serif reserved for dark card inversion at display scale
- Chromatic color deployed sparingly (one accent per section maximum)
