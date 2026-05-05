---
type: concept
title: Visual Directions
created: 2026-05-05
updated: 2026-05-05
aliases: [deterministic-design-directions, visual-direction-presets]
tags: [design-systems, ai-design, deterministic-generation, presets]
---

# Visual Directions

> A small set of pre-defined palette + font-stack combinations that an AI design agent picks from instead of improvising. Codified by [[wiki/entities/open-design|Open Design]] as five named directions: **Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm**. Each provides an OKLch palette + font stack — no model improvisation. Distinct from brand-specific [[design-md|DESIGN.md]] files (which capture *one specific brand*); visual directions capture *aesthetic categories*.

## Definition

**Visual directions** are *deterministic aesthetic presets* an AI design agent applies when no specific brand context exists. Each direction specifies:

- A **palette** (OKLch values for backgrounds, surfaces, text, accents).
- A **font stack** (display + body + monospace).
- An **archetype name** that signals mood (e.g. "Editorial Monocle" = magazine restraint).
- *Optionally*: opinionated component defaults (button rounding, border weight, shadow philosophy).

The discipline: the agent is **forbidden from improvising** outside the chosen direction. If the user picks "Brutalist," the agent uses raw concrete colors + system fonts + sharp corners, not whatever the model's training suggests is "brutalist." This forces consistency.

## Why it matters

Unconstrained AI design generation produces predictable failure modes:

1. **Drift toward AI-cliché aesthetics** (purple gradients, generic SaaS-template look).
2. **Inconsistency within a single output** (hero uses one type style, footer uses another).
3. **Inconsistency across iterations** (regenerating a page produces a different aesthetic each time).

Visual directions solve all three:

1. **Cliché avoidance**: the named directions are deliberately *not* AI-cliché. Editorial Monocle, Brutalist, Soft Warm are specific aesthetics, not the generic "modern professional" default.
2. **Within-output consistency**: pinning a single OKLch palette + font stack means *every element* inherits the same tokens.
3. **Across-iteration consistency**: regenerating with the same direction produces the same aesthetic.

The pattern is also **decision-aiding**: a non-designer user can pick "Brutalist" and immediately get a meaningful aesthetic without needing to articulate "raw concrete + system fonts + sharp corners."

## Treatment across sources

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source. Open Design ships **5 visual directions**: Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm. Each provides OKLch palette + font stack.
- *Adjacent treatments not yet ingested*: design-system starter kits (Tailwind UI, shadcn/ui themes) provide a similar function but without the explicit "no improvisation" discipline. Future ingests would clarify the lineage.

## Sub-claims and details

### Open Design's five directions

| Direction | Aesthetic | Likely palette base | Likely font stack |
|---|---|---|---|
| **Editorial Monocle** | Magazine restraint; serif + monospace; high white space | Off-white + warm dark + single accent | Serif display + sans body + mono |
| **Modern Minimal** | Neutral baseline; SaaS conventional | Pure white + cool grays + blue accent | System sans throughout |
| **Tech Utility** | Dev-tooling aesthetic; dark + monospace-heavy | Near-black + cool grays + green/cyan accent | Mono display + sans body + mono code |
| **Brutalist** | Raw concrete + system fonts + sharp corners | Off-white + black + red-orange | System fonts only, possibly Arial display |
| **Soft Warm** | Warm pastels + serif accents | Cream + warm pastel + warm accent | Serif display + sans body |

(Specific values are in Open Design's repo; this table reconstructs the archetype shape.)

### Why OKLch?

OKLch (lightness, chroma, hue in perceptually-uniform space) is a CSS Color 4 specification that produces *better gradients and color manipulation* than RGB or HSL. For agents generating hover states, button variants, and disabled states, OKLch's perceptual uniformity means programmatic adjustments produce consistent perceived changes — a 10% darker accent looks 10% darker, not "darker but also weirdly more saturated."

This is a deliberate technical choice: visual-direction palettes in OKLch are inherently *adjustable* in a way RGB hex palettes aren't. Open Design's agent can take a base direction and *derive* hover states / disabled states / dark-mode variants algorithmically rather than requiring every variant to be hand-specified.

### Distinction from brand-specific DESIGN.md

| | Visual direction | Brand DESIGN.md |
|---|---|---|
| **Scope** | Aesthetic category | One specific brand |
| **Number** | Small (~5 in Open Design) | Many (138 in Open Design) |
| **When applied** | No brand context | Brand context known |
| **Restraint** | High (no improvisation) | Specific to brand |
| **Example** | "Brutalist" | "Stripe" or "Linear" |

When a user has no brand assets, they pick a visual direction. When they do, they pick a DESIGN.md. Both gate the agent's aesthetic choices.

### Composition with other Open Design mechanisms

- **+ [[anti-ai-slop-machinery]]**: visual direction provides the positive aesthetic; anti-slop blacklist provides the negative (no purple gradients regardless of direction).
- **+ [[question-form-first]]**: the Turn-1 form's "tone" field maps to a visual-direction selection.
- **+ [[design-md]]**: when a brand DESIGN.md is selected, the visual direction becomes optional. When no brand exists, the visual direction is required.

### Why "no improvisation" matters

The discipline of "use only the OKLch values + font stack in the direction; nothing else" is a strong constraint. Without it, the agent might "tweak" the palette for the specific page or "borrow" a typeface that feels appropriate for the surface. Each tweak is reasonable in isolation; cumulatively they produce the inconsistency that visual directions exist to prevent.

The constraint mirrors [[reasoning-execution-split]]: the LLM reasons about which direction fits ("this is a developer tool, use Tech Utility") but the *application* of the direction is deterministic — copy the OKLch values, set the font stack, don't deviate.

## Open questions and contradictions

- **Five is a small number.** Real design taste covers far more aesthetic categories (industrial, art-deco, retro-pixel, hand-drawn, pastoral, etc.). Five is enough for most B2B/SaaS surfaces but limiting for creative work.
- **Direction selection is itself a design decision** — picking "Brutalist" vs "Editorial Monocle" is a meaningful choice the user may not be qualified to make. Surface decision-aid (sample images? mood boards? "if your brand is X, pick Y") is needed.
- **Directions can become dated.** Brutalist felt fresh in 2022; by 2026 it's an AI-cliché. The named directions need periodic refresh.
- **OKLch isn't yet universally supported.** Older browsers (Safari pre-15.4) don't support it natively; CSS preprocessing or runtime fallback is needed.
- **The "no improvisation" rule is brittle.** Real design needs occasional improvisation — a one-off illustration, a custom hero, a unique component. Strict enforcement may rule out genuine creative work.

## Related concepts

- [[anti-ai-slop-machinery]] — composes with visual directions.
- [[question-form-first]] — selects a direction via Turn-1 form.
- [[design-md]] — the brand-specific alternative.
- [[reasoning-execution-split]] — direction application is the deterministic-execution side.
- [[markdown-as-agent-contract]] — visual directions are agent contracts at the aesthetic-preset layer.

## Related entities

- [[wiki/entities/open-design]] — codifies the five directions.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]]
