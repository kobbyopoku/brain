---
type: source
title: Apple Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-04
content_status: substantive
source_url: https://styles.refero.design/style/c9cabb96-32fa-4896-837a-f2497ce1c856
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/apple/DESIGN.md
tags: [design-md, design-tokens, apple, refero]
---

# Apple Design System (DESIGN.md from Refero)

> The canonical *"gallery wall at natural light"* aesthetic — minimal accent palette (one Azure CTA color, one Cobalt link color), eight-step neutral scale, SF Pro Display + SF Pro Text, **zero box-shadows**, and a 28px card radius that the source explicitly calls out as *"the page's geometric signature."*

## TL;DR

Apple's system is the most palette-disciplined in the catalog — only **two non-neutral colors**: Azure `#0071e3` for the "Buy" CTA, Cobalt Link `#0066cc` for inline links. Eight-step achromatic neutrals from Obsidian to Snow. Three product gradients (Citrus, Indigo, Blush) used decoratively, never structurally. SF Pro Display/Text with extreme negative letter-spacing scaled to size (-2.11px at 96px display). Critical signature: **28px card border-radius** is "the page's geometric signature" — explicitly named as identity-load-bearing.

## Key takeaways

- **One Azure, one Cobalt**: `#0071e3` exclusively for the Buy CTA, `#0066cc` for inline links. Nothing else gets non-neutral fill.
- **8-step achromatic neutrals**: Obsidian `#000000` → Snow `#ffffff` with 6 steps between.
- **28px card radius is the identity** — *"this exact value is the page's geometric signature."*
- **Letter-spacing scales aggressively** with size: -2.11px at 96px display, -0.9px at 56px, -0.6px at 40px.
- **Zero box-shadows**. Elevation via background and surface color only.
- **Three product gradients** (Citrus/Indigo/Blush) are decorative — the rule explicitly forbids using them as semantic UI accents.
- **No two pill-shape buttons side-by-side** — a hierarchy rule preventing visual conflict.
- **Caution color** `#b64400` is the only semantic non-neutral. No green for success, no red beyond caution.

## Notable quotes

> "Use 28px border-radius for all feature cards — this exact value is the page's geometric signature."

> "Reserve #0071e3 exclusively for the primary 'Buy' CTA button."

> "Do not add box-shadow to any card or container."

## Mentioned entities

- [[wiki/entities/apple]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
