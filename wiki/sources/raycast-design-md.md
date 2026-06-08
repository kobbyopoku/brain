---
type: source
title: Raycast Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
content_status: substantive
source_url: https://styles.refero.design/style/3b6a17f0-3bdf-418c-a95e-0b89e5a8b2f8
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/raycast/DESIGN.md
tags: [design-md, design-tokens, raycast, refero, claude-code-ecosystem]
---

# Raycast Design System (DESIGN.md from Refero)

> *"Obsidian command terminal"* — near-total darkness on Void Black `#040506`. Ten-step neutral scale, glassmorphic surfaces (backdrop-filter blur 36-48px), monochromatic shadows only (no color tints). 8px base unit. Inter for UI + GeistMono for code/commands.

## TL;DR

Raycast is the deepest dark-mode system in the catalog: Void Black `#040506` ground, 10-step graphite/slate ramp through Snow `#ffffff`. Glass-card pattern uses `backdrop-filter: blur(36-48px)` + `1px solid rgba(255,255,255,0.1)` border — distinct from Linear's solid-surface layered approach. Ember Red `#ff6363` reserved for status dots and logo only, never CTAs. Sky Signal gradient + Mint Signal `#59d499` for status. **Shadows must be monochromatic** (black/white only, no color tints). 8px base unit (vs typical 4px). Multiple "Nebula Glow" / "Violet Haze" radial gradients for atmospheric backgrounds.

## Key takeaways

- **Void Black `#040506`** is darker than Linear's `#08090a` Pitch Black. Raycast is the catalog's darkest system.
- **Glass surfaces via backdrop-filter blur** — identity move.
- **Monochromatic shadows rule** — no color-tinted shadows allowed.
- **Ember Red is status-only** — never primary CTA color (CTAs use neutral Ash 50 `#e6e6e6` background with dark text).
- **Inter is everywhere** — like Linear. Universal UI font.
- **8px base unit** + extensive scale (8/16/24/32/40/48/56/64/80/96/120/224px) — chunky.
- **Nebula Glow and Violet Haze** atmospheric radial gradients — used for hero backgrounds.

## Notable quotes

> "Obsidian command terminal — UI surfaces emerge like backlit glass panels."

> "Shadows must be monochromatic."

## Notes

- **Catalog dark-mode triad**: Linear (layered solid surfaces), Raycast (glass + atmospheric gradients), Mercury (twilight + light typography). Three takes on "dark mode" with distinct textures.

## Mentioned entities

- [[wiki/entities/raycast]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
- [[wiki/sources/linear-design-md]] — sibling dark-mode system; different texture.
