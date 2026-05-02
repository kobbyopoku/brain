---
title: "ElevenLabs Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/031056ff-7af1-46db-8daa-115f731c5d26
author: Refero
published: 2026-05-02
created: 2026-05-02
description: ElevenLabs's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, elevenlabs, design-md, refero]
---

# ElevenLabs Design System Summary

## Core Philosophy
The design embodies "Architect's blueprint on warm vellum" — a type-first, museum-label aesthetic that "whispers where competitors shout" through restrained use of custom serif typography paired with an achromatic palette.

## Color Palette

**Neutrals:**
- Obsidian #000000 (primary text, CTAs)
- Cinder #57534 (mid-tone text)
- Gravel #777169 (secondary text, warm stone undertone)
- Slate #a59f97 (tertiary text, icon strokes)
- Fog #b1b0b0 (disabled states, placeholder)
- Chalk #e5e5e5 (universal border color)
- Powder #f5f3f1 (secondary surface, hover states)
- Eggshell #fdfcfc (page background, near-white warmth)

**Accents:**
- Signal Blue #0447ff (ElevenAgents avatar dots only)
- Ember #ff4704 (ElevenCreative avatar dots only)
- Voice Spectrum: conic-gradient logomark (blue-cyan wheel)

## Typography

**Waldenburg (Display Headlines)**
- Weight: 300 only
- Sizes: 32px, 36px, 48px
- Letter-spacing: -0.64px (32px), -0.72px (36px), -0.96px (48px)
- Line-height: 1.08–1.17
- Fallback: Cormorant Garamond 300 or Libre Baskerville 300

**WaldenburgFH (Product Labels)**
- Weight: 700 only
- Size: 14px
- Letter-spacing: 0.7px (0.05em)
- Line-height: 1.10
- Fallback: Inter 700 with 0.7px tracking

**Inter (Body & UI)**
- Weights: 400, 500
- Sizes: 10–20px (8 values)
- Letter-spacing: 0.1px–0.2px
- Line-height: 1.0–2.06

**Geist Mono (Technical Annotations)**
- Weight: 400
- Size: 13px
- Uses: [whispers], [sarcastic], code snippets

**Type Scale (Major Second 1.125 from 16px base):**
- Display: 48px, weight 300, line-height 1.08
- Heading-lg: 36px, weight 300, line-height 1.17
- Heading: 32px, weight 300, line-height 1.13
- Heading-sm: 20px, weight 400, line-height 1.35
- Subheading: 18px, weight 400, line-height 1.6
- Body-lg: 16px, weight 400, line-height 1.5
- Body (15px): 15px, weight 500, line-height 1.47
- Body: 14px, weight 500, line-height 1.5

## Spacing & Shape

**Base Unit:** 4px
**Density:** Comfortable
**Max Width:** 1200px

**Spacing Scale:**
4px, 8px, 12px, 16px, 20px, 24px, 28px, 32px, 36px, 40px, 48px, 56px, 64px, 72px, 96px, 160px

**Border Radius:**
- Inputs: 0px (editorial distinction)
- Badges: 12px
- Cards: 16px
- Panels: 20px
- Modals: 24px
- Buttons/Tags: 9999px (pill style)

**Section Gaps:** 80–120px vertical
**Card Padding:** 16–24px
**Element Gap:** 8–12px

## Shadows

- Subtle: rgba(0,0,0,0.075) 0px 0px 0px 0.5px inset
- Subtle-2: rgba(0,0,0,0.06) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 1px 2px, rgba(0,0,0,0.04) 0px 2px 4px
- Subtle-4: rgba(0,0,0,0.4) 0px 0px 1px 0px, rgba(0,0,0,0.04) 0px 4px 4px (card elevation limit)

## Key Components

**Primary Pill Button (Filled):** Background #000000, text #fdfcfc, 9999px radius, 0px 16px padding, 1px #e5e5e5 border

**Ghost Pill Button (Outline):** Background #ffffff, text #000000, 9999px radius, 0px 12px padding, 1px #e5e5e5 border

**Product Demo Card:** Background #ffffff, 16px radius, subtle-4 shadow, contains voice list (32px avatars, Inter 500 14px names, Inter 400 13px descriptors)

**Text Input (Transparent):** No background, 0px radius, bottom border only (1px #000000), Inter 400 14px

**Text Input (Contained):** Background #ffffff, 1px #e5e5e5 border, 0px radius, inset subtle shadow

## Design Imperatives

**Do:**
- Use Waldenburg 300 with -0.02em tracking for 32px+ headlines
- Apply 9999px radius to buttons/pills; 16–20px for cards/panels; 0px for inputs
- Keep palette near-zero saturation; reserve #ff4704 and #0447ff for avatar dots only
- Use inset shadow rgba(0,0,0,0.075) on white surfaces replacing borders
- Use Geist Mono 400 13px only for technical annotations/code
- Desaturate third-party logos to #b1b0b0 (Fog)
- Section gaps: 80–120px; element gaps: 8–12px

**Don't:**
- Never use Waldenburg weight above 300 for display (weight 700 reserved for WaldenburgFH product labels at 14px only)
- Never introduce saturated color for text, fills, or buttons
- Never apply box-shadow larger than rgba(0,0,0,0.4) 0px 0px 1.143px
- Never use pure white #ffffff for page surfaces; use #fdfcfc (Eggshell)
- Never place Inter below 13px (product UI) or 14px (marketing prose)
- Never mix more than two button variants per cluster
- Never apply border-radius to input fields

## Surfaces & Elevation

**Surface Levels:**
- Page ground: #fdfcfc (Eggshell)
- Powder: #f5f3f1 (hover, active states)
- Card white: #ffffff (interactive elements)
- Obsidian: #000000 (CTAs, logo)

"ElevenLabs uses only hairline elevation" — cards float by 1px shadow, not depth layering, "keeping all UI elements in the same perceptual plane."

## Layout Philosophy

"Max-width ~1200px centered on eggshell ground." Hero: asymmetric two-column (60% left headline/body + buttons, 40% right empty). Product card embedded below. Logo grid: 6 columns × 3 rows, 24–32px gaps. Feature blocks: 2-column typographic layout, no images. Navigation: 36px sticky bar, logo left, auth CTAs right. "Entire page is eggshell ground broken only by white card surfaces and #f5f3f1 subtle hover zones."

## Imagery & Visual Hierarchy

"Text-dominant: imagery occupies roughly 30% of visual space with product card; 70% is typographic." Only chromatic elements are 28–32px circular voice avatar gradients and the conic-gradient logomark. Social proof logos rendered in #b1b0b0 grayscale.
