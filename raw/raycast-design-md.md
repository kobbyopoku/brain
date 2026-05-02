---
title: "Raycast Design System (DESIGN.md from Refero)"
source: https://styles.refero.design/style/3b6a17f0-3bdf-418c-a95e-0b89e5a8b2f8
author: Refero
published: 2026-05-02
created: 2026-05-02
description: Raycast's design system as published in Refero's curated DESIGN.md catalog. Captured via WebFetch on 2026-05-02.
tags: [clippings, design-system, raycast, design-md, refero]
---

# Raycast Design System Summary

## Core Philosophy
Raycast presents itself as an "obsidian command terminal" where "UI surfaces emerge like backlit glass panels, depth created by shadow layering rather than color contrast." The design lives in "near-total darkness" with a #040506 void canvas.

## Color Palette

**Neutrals:**
- Void Black: #040506 (canvas ground)
- Deep Charcoal: #07080a (primary surfaces)
- Graphite 700: #111214
- Graphite 600: #1b1c1e
- Graphite 500: #363739
- Graphite 400: #454647
- Slate 300: #6a6b6c
- Slate 200: #9c9c9d
- Ash 50: #e6e6e6 (primary CTA background)
- Snow: #ffffff

**Accent Colors:**
- Ember Red: #ff6363 (status signals, logo only—not CTAs)
- Ember Dark: #452324
- Mint Signal: #59d499
- Sky Signal: linear-gradient(135deg, #56c2ff 0%, #138af2 100%)

**Gradients:**
- Nebula Glow: radial-gradient(84.6% 73.49% at 50% 26.51%, rgba(4,63,150,0.7), rgba(6,18,37,0.25))
- Violet Haze: radial-gradient(86.88% 75.47% at 50% 24.53%, rgba(82,48,145,0.7), rgba(26,11,51,0.14))

## Typography

**Inter** (universal UI font):
- Weights: 400, 500, 600
- Sizes: 11px–64px across 12 scale steps
- Display (64px): weight 600, line-height 1.1, letter-spacing -0.13em
- Heading-lg (56px): weight 400, line-height 1.17, letter-spacing -0.11px
- Heading (32px): weight 500, line-height 1.15, letter-spacing -0.06px
- Body (16px): weight 400, line-height 1.5, letter-spacing 0.1px
- Caption (11px): weight varies, line-height 1.45, letter-spacing 0.8px

**GeistMono** (code/commands):
- Weights: 300, 400, 500
- Sizes: 10px, 12px, 14px
- Letter-spacing: +0.017em to +0.05em

## Spacing & Shapes

**Base Unit:** 8px
**Scale:** 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 120, 224px

**Border Radius:**
- Badges: 6px
- Inputs/Buttons: 8px
- Cards: 11px
- Modals: 16px
- Card Large: 20px
- Button Pill: 86px

## Shadows

Keyboard Key: rgba(0,0,0,0.4) 0px 1.5px 0.5px 2.5px, rgb(0,0,0) 0px 0px 0.5px 1px, rgba(0,0,0,0.25) 0px 2px 1px 1px inset, rgba(255,255,255,0.2) 0px 1px 1px 1px inset

Additional shadows: subtle-2 through subtle-11, sm, lg, xl, xl-2 (all using black or white rgba values only).

## Component Patterns

**Primary CTA:** #E6E6E6 background, #2F3031 text, 8px radius
**Badge:** #1b1c1e background, #fff text, 6px radius, Inter 12px weight 500
**Glass Product Card:** backdrop-filter blur(36–48px), 1px solid rgba(255,255,255,0.1) border
**Navigation:** Fixed top bar, #1b1c1e background, 11px radius pill shape

## Design Rules (Key Don'ts)

- Never use colored section backgrounds—only neutrals (#040506 to #1b1c1e)
- No border-radius above 20px on cards
- #FF6363 only for small status dots/accents, never large fills
- Shadows must be monochromatic (black/white only, no color tints)
- Negative letter-spacing required on display/heading text above 24px
