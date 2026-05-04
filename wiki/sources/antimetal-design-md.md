---
type: source
title: Antimetal Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
source_url: https://styles.refero.design/style/9f9a4a4f-1a27-47ca-a65b-68b9850a84e4
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/antimetal-design-md.md
tags: [design-md, design-tokens, antimetal, refero]
---

# Antimetal Design System (DESIGN.md from Refero)

> *"Electric storm over a blueprint."* Two-mode system: dark navy-to-electric-blue hero + near-white product surface, bridged by a single chartreuse `#d0f100` accent. Pill buttons (`9999px`) with a 1px-outer-ring shadow as border substitute.

## TL;DR

Antimetal runs **two visual modes** in one site: a dark gradient hero (`linear-gradient(180deg, #001033, #0050f8 55%, #5fbdf7 100%)`) and a near-white product surface (`#f8f9fc` ground, `#ffffff` cards). The chartreuse pulse `#d0f100` is the only color permitted in both modes — exclusively for primary CTAs. Two custom typefaces (abcdFont for UI 13-28px; ivarTextFont for display 32px+ with OpenType `ss04, ss06, ss09, ss10, ss11`). Distinctive shadow vocabulary: blue-tinted `rgba(0, 39, 80, ...)` instead of black. **Inputs have 0px radius** as a deliberate signature against the otherwise pill-heavy system.

## Key takeaways

- **Two-mode design**: dark hero + light product. One section dark, rest `#f8f9fc`.
- **Single bridge color**: Chartreuse Pulse `#d0f100` for primary CTAs only — never decorative.
- **Pill discipline**: all buttons `9999px`. **Except** inputs at `0px` — deliberate.
- **Blue-tinted shadows** `rgba(0, 39, 80, ...)` — not black. Reads cooler than typical drop shadows.
- **OpenType features** (`ss04, ss06, ss09, ss10, ss11`) used aggressively for display type. Most brands use 0-1.
- **1px outer ring as border**: borders are implemented as `box-shadow: 0px 0px 0px 1px`, not `border:`. Allows interaction with surface gradients without visible seams.

## Mentioned entities

- [[wiki/entities/antimetal]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
