---
type: source
title: Cursor Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
content_status: substantive
source_url: https://styles.refero.design/style/4e3b4717-84c8-4599-baaf-a343c3d619b6
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/cursor/DESIGN.md
tags: [design-md, design-tokens, cursor, refero, claude-code-ecosystem]
---

# Cursor Design System (DESIGN.md from Refero)

> *"Warm ivory software studio"* — parchment neutrals (`#f7f7f4` Canvas Parchment) with three muted accents (Onyx Outline `#f54e00`, Forest Green `#34785c`, Goldenrod `#c08532`) for outlined buttons and PR-like statuses. Custom CursorGothic display font. The shortest DESIGN.md in the catalog.

## TL;DR

Cursor's system is the **most compact** of the catalog so far — six neutrals, four accent colors, three typefaces (CursorGothic display, Berkeley Mono code, Lato secondary), one shadow token. The ivory-and-warm-stone palette differentiates it from competing AI coding tools (Linear's pitch-black, Raycast's void-black). Border-radius is small (4px cards/buttons, 8px prominent). Single complex shadow uses an oklab() color reference — modern color space adoption.

## Key takeaways

- **Compactest DESIGN.md so far** — fewer tokens than Stripe, Apple, or Linear.
- **Warm-ivory contra dark-mode**: Canvas Parchment `#f7f7f4` distinguishes Cursor from black-canvas competitors (Linear, Raycast).
- **CursorGothic** is custom — used at 72px display weight 400.
- **oklab() in shadow** — modern perceptual color space, rare in production design systems.
- **Three accent colors as semantic**: Onyx Outline (orange-red, outlined buttons + links), Forest Green (PR-related actions), Goldenrod (interactive states).
- **Berkeley Mono** for code — same monospace as Linear (independently chosen).

## Notes

- **Cross-cuts**: [[wiki/entities/cursor]] is also referenced in [[wiki/sources/realbrianmoran-making-money-online-2026]] as one of three build-your-own-app tools. This is the second source treating Cursor substantively.
- **Linear comparison**: same Berkeley Mono, opposite background palette. Linear is `#08090a` pitch black; Cursor is `#f7f7f4` parchment. Same dev-tools category, different mood.

## Mentioned entities

- [[wiki/entities/cursor]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
- [[wiki/sources/realbrianmoran-making-money-online-2026]] — Cursor as build-your-own-app tool.
