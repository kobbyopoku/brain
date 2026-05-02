---
type: source
title: Stripe Design System (DESIGN.md from Refero)
created: 2026-05-02
updated: 2026-05-02
source_url: https://styles.refero.design/style/48e5de76-05d5-4c4e-a269-c7c245b291ec
source_type: design-md
author: Refero
source_date: 2026-05-02
raw_path: raw/stripe-design-md.md
tags: [design-md, design-tokens, stripe, refero, foundational-example]
---

# Stripe Design System (DESIGN.md from Refero)

> The brain's **first ingested DESIGN.md** — Stripe's design tokens (colors, typography, spacing, shapes, components, philosophy) as published in [[wiki/entities/refero|Refero]]'s curated catalog. Validates the [[design-md]] format with concrete content; demonstrates one cell of the [[wiki/concepts/landing-page-patterns|landing-page-patterns]] / [[design-md]] / [[markdown-as-agent-contract]] design-systems thesis.

## TL;DR

Stripe's design system, captured from Refero, documents 18 named colors (5 brand + 3 gradients + 7 neutrals), a 7-step type scale on the proprietary `sohne-var` typeface, a 4px-base spacing system with five border-radius values and four named shadows, five component patterns (3 buttons + 2 cards) with full token-level specs, and a one-paragraph design philosophy. The aesthetic is **"architectural blueprint on white marble"** — serene white background, structured grid layouts, a single vibrant violet (#533afd) as the brand accent. Substantive enough to inform an agent generating UI in Stripe's voice.

## Key takeaways

### Brand identity is one violet
Stripe's identity hangs on a single saturated color: **Deep Violet `#533afd`**. Used for primary actions, brand moments, and accent text on the outlined button. Three sibling violets (Washed `#b9b9f9`, Soft `#8087ff`) and an off-key Accent Green (`#81b81a`) and Vibrant Orange (`#ff6118`) round out the brand palette but never compete with the primary violet for attention. **The single-color brand discipline is the design system's load-bearing decision.**

### Neutrals are blue-tinted, not gray
Every neutral has a blue component: Midnight Ink `#061b31`, Slate Blue `#50617a`, Ghost Gray `#64748d`, Powder Blue `#e5edf5`, Porcelain White `#f8fafd`. Even "white" is `#f8fafd` — slightly cool. This is what makes the system feel "architectural" rather than "warm" — a deliberate cool-temperature backdrop against which the violet accent reads as decisive.

### Typography is light and tight
Display weight is **300** (light) at line-height **1.03** with letter spacing **-0.03em**. Body weight is 400 at line-height 1.2. The combination produces tightly-packed display text and confidently-spaced body — large headings feel architectural, body feels readable. The proprietary `sohne-var` is the secret sauce; the system-ui/sans-serif fallback assumes it loads cleanly.

### Spacing is 4px-based, gaps are 8x
Base unit is 4px. Element gap is 8px (2x base). Card padding is 12px (3x). Section gap is 64px (16x). The 16:1 ratio between section-gap and base-unit creates the *roomy* feeling Stripe pages have without ambiguity in inter-element spacing. The spacing system is consistent enough that an agent generating UI can compose units without measuring.

### Border radius differentiates layout from interaction
- **Buttons / inputs / tags / images: 4px** (interactive things; subtle softening).
- **Cards: 6px** (layout containers; gentler curve).

The 4-vs-6 split is small but consistent. An agent generating a card with a 4px radius would be subtly "off."

### Components are token-level specified
The five named components (Primary Filled, Ghost, Outlined buttons + Default and Feature Cards) are specified in tokens, not percentages or pixels-from-nowhere:

- Primary Filled Button: `Deep Violet` bg, `Platinum White` fg, `4px` radius, `15.5px / 24px` padding.
- Ghost Button: transparent bg, `Midnight Ink` fg, `0px` border, `12px / 0px` padding.
- Outlined Button: transparent bg, `Deep Violet` fg, `Washed Violet` border, `4px` radius, `14.5px / 24px` padding.
- Default Card: `Powder Blue` bg, `6px` radius, `12px` padding.
- Feature Card: `Porcelain White` bg, `6px` radius, the `xl` shadow.

The token-references-not-literals shape is what makes a DESIGN.md actionable — an agent can swap `Deep Violet` for `Vibrant Orange` and the button still has the right structural identity.

### Shadow vocabulary is named, not numbered
Four shadows: `xl`, `xl-2`, `xl-3`, `sm`. Three "xl" variants suggests Stripe distinguishes elevation by *quality* (rgba diffusion / spread / offset) rather than raw blur radius. The Feature Card uses `xl` (`rgba(0, 0, 0, 0.2) 0px 0px 32px 8px`) — a soft, diffuse halo that pushes the card forward without heavy shadowing.

### The design philosophy crystallizes the system
> *"Architectural blueprint on white marble — serene white background with structured grid layouts and a single vibrant violet. Emphasizes quiet efficiency, where information is paramount."*

This sentence resolves every token-level decision: the cool-temperature neutrals, the single-violet accent, the tight-spaced 300-weight display type, the soft 6px card radius, the diffuse xl shadow. An agent re-reading the philosophy and the tokens together can extrapolate to choices not in the tokens (e.g. what should an icon look like? — answer constrained by "blueprint on white marble").

## Notable quotes

> "Architectural blueprint on white marble"
> — design philosophy

> "Quiet efficiency, where information is paramount"
> — design philosophy

## Notes

- **The full extent of the original Refero `Copy.md` may be slightly larger** than what's captured here. The page is JavaScript-rendered with a clipboard-driven Copy.md button; the WebFetch agent extracted what was visible in the rendered HTML payload, but the official Copy.md export may include additional fields (icon definitions, motion tokens, additional component variants) that didn't surface. Treat this as the *substantive core* of the DESIGN.md, not a guaranteed exhaustive copy.
- **This is the first concrete instance of [[design-md]] in the brain.** Up until now, the [[design-md]] concept page was abstract — describing the format without showing one. This source closes that gap. Future DESIGN.md ingests should follow this shape.
- **Cross-cuts with [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]]**: clear_graphics analyzed Stripe's landing-page *structure* (category-defining headline, product-in-the-hero, footer-as-sitemap); this source captures Stripe's *visual tokens* (colors, typography, spacing). Two complementary axes of "what makes Stripe look like Stripe." Together they describe the whole.
- **Deep Violet `#533afd` is recognizably Stripe.** The brand has owned this color for years; an agent generating a payment UI with this hex code will produce something that reads as "Stripe-like" to a designer at twenty paces.
- **Sohne-var is proprietary.** Most agents generating UI in Stripe's voice will lack access to the typeface. The fallback (`system-ui, sans-serif`) covers, but the *exact* visual identity depends on the typeface being available. Worth flagging when delegating to agents that don't have font assets.
- **What's NOT in this DESIGN.md** is also informative: no icon system specs, no motion tokens, no breakpoint definitions, no z-index scale, no form-state colors (focus, error, disabled). A DESIGN.md is necessarily partial — it captures *what the brand wants enforced* and trusts the agent to fill in the rest.
- **An agent re-using this DESIGN.md** would do so by either (a) loading it as context and generating UI directly, or (b) treating it as the output spec for translation into Tailwind config / CSS variables / design-token JSON. The Refero page mentions Tailwind v4, CSS Variables, and Design Tokens as available export formats — those are the agent-consumption paths.

## Mentioned entities

- [[wiki/entities/stripe]] — the entity this DESIGN.md describes.
- [[wiki/entities/refero]] — publisher of the catalog this DESIGN.md sits in.

## Related concepts

- [[design-md]] — first concrete instance of this format ingested into the brain.
- [[markdown-as-agent-contract]] — DESIGN.md is one species of this meta-pattern.
- [[landing-page-patterns]] — adjacent: Stripe's landing-page *structure* documented from a different source.
- [[progressive-disclosure]] — a DESIGN.md is itself a Level-2 (or higher) reference document; agents load it on demand.

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — the catalog source page; described the format abstractly. This source provides the first concrete content.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — sibling Stripe analysis at the page-structure layer (vs. this source's token layer).
