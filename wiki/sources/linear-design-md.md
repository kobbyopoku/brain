---
type: source
title: Linear Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-02
source_url: https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/linear-design-md.md
tags: [design-md, design-tokens, linear, refero]
---

# Linear Design System (DESIGN.md from Refero)

> *"Midnight Command Center: A dark, sophisticated dark-mode experience reminiscent of a command center dashboard."* The catalog's reference dark-mode system: Pitch Black `#08090a` ground, Neon Lime `#e4f222` as the single bright action color, twelve-step neutral scale, nine shadow tokens, Inter Variable + Berkeley Mono.

## TL;DR

Linear is the canonical dark-mode reference: "depth without harsh contrasts" through layered surfaces (Pitch Black → Graphite → Deep Slate → Charcoal Grey). Neon Lime `#e4f222` is the single load-bearing brand color for primary CTAs and active states; four other accent colors (Aether Blue, Cyan Spark, Deep Violet, Amethyst) are decorative-only. Inter Variable with weights 300/400/510/590 — non-standard 510 and 590 weights suggest custom variable axis sweeping. Berkeley Mono for code (12-14px). 6px universal border-radius for cards/buttons/inputs, 9999px pills. Nine shadow tokens — most in the catalog.

## Key takeaways

- **Single bright color**: Neon Lime `#e4f222` for primary actions only.
- **Layered dark surfaces**: Pitch Black `#08090a` → Graphite `#0f1011` → Deep Slate `#161718` → Charcoal Grey `#23252a`. Depth via background, not shadow.
- **Inter Variable 510/590** — non-standard variable-font weights for fine typographic control.
- **Berkeley Mono** — same code typeface as Cursor (independent convergence on this monospace).
- **Twelve-step neutral scale** for grays from `#08090a` to `#f7f8f8` Porcelain.
- **9 shadow tokens**: subtle/sm/md/xl/subtle-2 through subtle-6. Includes inset shadows for depth.
- **Three semantic colors** explicitly named (Forest Green, Emerald, Warning Red) — uncommon in DESIGN.md.

## Notable quotes

> "Sophisticated and focused dark-mode experience, reminiscent of a command center dashboard."

> "Depth without harsh contrasts."

## Notes

- **Comparison with Raycast** (also in catalog, ingested): both are dark, both use Inter, both reserve a single accent color (Lime for Linear, Red for Raycast as status only). Linear has more shadow tokens; Raycast pushes deeper into pure black `#040506`.
- **Linear's dev-tool peers**: Linear `#08090a` vs Cursor `#f7f7f4` parchment. Same category, opposite philosophy on surface color.

## Mentioned entities

- [[wiki/entities/linear]]
- [[wiki/entities/refero]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]]
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — Linear is a YC unicorn analyzed there.
