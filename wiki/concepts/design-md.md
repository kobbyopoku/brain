---
type: concept
title: DESIGN.md
created: 2026-05-02
updated: 2026-06-06
aliases: [design.md, DESIGN markdown]
tags: [design-systems, ai-agents, markdown, agent-config]
---

# DESIGN.md

> A markdown file format that codifies a product's design system — colors, typography, spacing, components — in a shape that AI coding agents can consume before generating UI.

## Definition

A `DESIGN.md` is a single markdown document that captures the visual and structural design conventions of a product (or a reference style) in plain text. The intent is to give an AI coding agent enough context to generate UI that "looks like" the target style without having to reason from screenshots, parse Figma files, or guess at design tokens. The format is associated most prominently with [[wiki/entities/refero]], which publishes DESIGN.md files extracted from real product websites.

## Why it matters

This concept is one concrete instance of [[markdown-as-agent-contract]] — the broader trend of using markdown as the configuration/contract layer between humans and agents. DESIGN.md is to coding agents what `CLAUDE.md` is to a Claude Code session and what `AGENTS.md` is to Codex: a place to dump the conventions that the agent should respect, in a format the agent natively understands.

For a knowledge worker building UIs with AI assistance, a curated DESIGN.md library (like [[wiki/entities/refero|Refero]]'s) is a way to skip the "describe what you want it to look like" step and instead say "build this in the style of Linear" or "Stripe" or "Anthropic" — pointing the agent at a DESIGN.md that already encodes the relevant choices.

## Schema variants

DESIGN.md is **not a single schema** — there are at least two meaningful variants in the wiki as of 2026-05-05:

### Refero 5-section schema (33 ingests, 2026-05-02 / 2026-05-04)

Refero's published DESIGN.md files use a 5-section structure:

1. Color palette (brand / gradients / neutrals)
2. Typography (family + scale)
3. Spacing & shapes (base unit + radius + shadows)
4. Components (token-referenced specs)
5. Design philosophy (one-paragraph mood)

### Open Design 9-section schema (138 ingests-available, 2026-05-05)

[[wiki/entities/open-design|Open Design]]'s DESIGN.md format extends Refero's with four additional sections:

1. Visual Theme & Atmosphere (narrative philosophy)
2. Color Palette & Roles (full token tables with semantic role per color)
3. Typography Rules (full size/weight/line-height/tracking tables, often 20+ rows)
4. Component Stylings (concrete buttons/cards/inputs/badges/navigation specs)
5. Layout Principles (spacing, grid, container, whitespace, radius scale)
6. **Depth & Elevation** *(new)* — multi-level treatment with shadow philosophy
7. **Do's and Don'ts** *(new)* — explicit Do/Don't rules
8. **Responsive Behavior** *(new)* — breakpoints, touch targets, collapsing
9. **Agent Prompt Guide** *(new)* — quick color reference + example prompts + iteration guide

The Open Design schema is **substantially richer**: a comparable brand DESIGN.md is ~2.5× the line count of the Refero version (Refero's Linear ~144 lines vs Open Design's Linear ~370 lines). For agents wanting maximum fidelity on overlapping brands (airbnb, apple, cursor, elevenlabs, linear, openai, raycast, stripe, superhuman), Open Design's version is preferred.

Sections 6-9 are the substantive contribution: explicit elevation philosophy, do/don't rules, responsive behavior, and a self-contained agent-prompt guide section meaning the DESIGN.md *is itself* an agent-readable spec without requiring external prompt engineering.

## Treatment across sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — names DESIGN.md as the unit of output for Refero's catalog. Asserts the contents are colors, typography, spacing, and component patterns, but does not include an actual DESIGN.md to inspect.
- [[wiki/sources/stripe-design-md]] — **first concrete DESIGN.md ingested into the brain** (2026-05-02). Validates the format with content: 18 named colors organized brand/gradients/neutrals, a 7-step type scale on `sohne-var`, 4px-base spacing system, 5-radius / 4-shadow vocabulary, 5 token-referenced components (3 buttons + 2 cards), and a one-paragraph design philosophy ("architectural blueprint on white marble").
- **The remaining 19 Refero brands** (acctual / anthropic / antimetal / apple / base44 / column / cursor / dia-browser / elevenlabs / family / general-intelligence-company / hyperstudio / linear / mercury / minimalissimo / monopo-saigon / raycast / superhuman / titan) — each ingested as its own `<brand>-design-md.md` source 2026-05-02. Refreshed with the official Refero Copy.md export 2026-05-04.
- **12 additional brands ingested 2026-05-04** (airbnb / all-in-one-salon / augen-pro / authkit / contractbook / customer-io / gleap / hyer-aviation / openai / perplexity-ai / ui / virtual) — plus the alternate Apple surface ([[wiki/sources/apple-design-md-alt]]). Catalog total: 32 brands, 33 DESIGN.md surfaces. With this much coverage the brain can now make stronger cross-brand observations (see Cross-brand patterns below; observations were drawn from the original 20 and remain broadly applicable, with deltas noted where the new brands extend or contradict them).
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. The most architecturally substantive design-systems source in the wiki. Surfaces **138 alternate DESIGN.md files** in [[wiki/entities/open-design|Open Design]]'s catalog, using a **richer 9-section schema** (adds Depth/Elevation + Do/Don't + Responsive + Agent-Prompt-Guide sections to Refero's 5-section schema). 10 brands overlap with the brain's 33 Refero ingests; the remaining 128 are not currently in the wiki. Significantly upgrades the wiki's understanding of what a "complete" DESIGN.md looks like — see Schema variants section above.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — *2026-06-06*. Claude Design generates a Design.md spec as the reusable source of truth across every asset — a **first-party Anthropic instance** of the DESIGN.md-for-AI-agents convention. Source treats the design-system-first move as the single highest-leverage practice.
- [[wiki/sources/open-design-catalog]] — *2026-05-05*. **Comprehensive catalog companion source**. Enumerates all 139 Open Design design systems (live count) across 20 categories — all raw DESIGN.md files fetched into `raw/open-design/design-systems/`. Adds a critical observation absent from the architectural source: Open Design's catalog **deliberately mixes real product brands with named aesthetic styles** (brutalism, claymorphism, doodle, retro). Refero is brand-only; Open Design adds 60+ named-style entries. Implication: an agent given *"design a brutalist landing page"* can use Open Design's `brutalism` DESIGN.md without needing to pick a real-world brand whose aesthetic happens to match. This is structurally distinct from Refero.

## Cross-brand patterns (across 32 ingested DESIGN.md files)

With every Refero brand's DESIGN.md in the brain, real comparative observations become possible:

### Common patterns
- **Most brands use 4px base unit.** Exceptions: Dia Browser and Raycast use 8px (more spacious feel).
- **"No box-shadows" is a recurring rule.** Apple, Anthropic, Mercury, Titan, Base44 (single subtle), Family (inset borders only), Minimalissimo, Hyperstudio. Box-shadow elevation is increasingly considered visually noisy in 2026 design culture.
- **Single-color brand identity** is dominant: one saturated color reserved for the primary CTA. Stripe (Deep Violet), Apple (Azure), Antimetal (Chartreuse), Linear (Neon Lime), Mercury (Mercury Blue), Acctual (Sky Teal), Titan (Highlight Orange), Hyperstudio (Amber Glow). The two-color exceptions (Family with 4 brand + 6 illustration accents) deliberately use color as identity differentiation.
- **Pill-radius for buttons** (`9999px` or large finite values like 32-160px) is more common than rounded rectangles. Stripe (4px) and Linear (6px) are notable counter-examples preferring "soft rectangles."
- **Achromatic-only neutrals** (no color tint) are now uncommon. Most brands use tinted neutrals — Stripe blue-tinted, Anthropic warm-stone, Linear pitch-black layered. Pure-grayscale neutrals appear only at Minimalissimo (whose entire system is grayscale) and a few others.
- **"Never pure white" as page background** appears across at least 8 brands: Anthropic (Ivory `#faf9f5`), Family (Warm Canvas `#fbfaf9`), ElevenLabs (Eggshell `#fdfcfc`), Cursor (Canvas Parchment `#f7f7f4`), Apple (Fog `#f5f5f7`), Superhuman (Parchment Canvas `#f2f0eb`), Minimalissimo (Canvas `#f5f5f5`). Slightly-warm or slightly-cool off-whites read as more deliberate than `#ffffff`.

### Distinctive signatures (one-of-a-kind moves)
- **Apple's 28px card radius** — explicitly named as "the page's geometric signature."
- **Antimetal & ElevenLabs's 0px input radius** — deliberate against a pill-heavy system.
- **Mercury's 0px card radius** — distinctive against a pill-heavy buttons set.
- **Anthropic's asymmetric "Try Claude" button** — flat top, rounded bottom (`0px 0px 8px 8px`).
- **monopo saigon's 225px display type** — far larger than any other brand.
- **Titan's 160px button radius** — largest specific (non-9999) pill in the catalog.
- **Family's 10 saturated colors** — most chromatic; identity through illustration not minimalism.
- **Linear's 9 shadow tokens** — most explicit shadow vocabulary; depth via layered surfaces.
- **Raycast's glass surfaces via `backdrop-filter: blur(36-48px)`** — atmospheric layering.
- **Anthropic's three custom typefaces** — Sans + Serif + Mono, where most brands use one.

### Philosophical archetypes (the catalog's "moods")
The 20 brands cluster into recognizable archetypes — useful as reference categories for an agent generating UI:

- **"Architectural blueprint on white marble"** — Stripe, Column. Cool restraint, single-color, structured.
- **"Architect's blueprint on warm vellum"** — ElevenLabs, Acctual (warm-toned). Editorial.
- **"Research journal printed on warm stone"** — Anthropic. Type-first, achromatic+thematic-tags.
- **"Gallery wall at natural light"** — Apple. Reductive, signature-radius driven.
- **"Midnight Command Center"** — Linear. Dark layered surfaces, single-color action.
- **"Mountain Top Command Center" / "Twilight"** — Mercury. Dark + light type + spacious.
- **"Obsidian command terminal"** — Raycast. Glass + atmospheric, deepest-dark.
- **"Monochrome terminal with amber accents"** — Hyperstudio, Titan. High-contrast, dev-aesthetic.
- **"Warm ivory software studio"** — Cursor. Light + warm tones for dev tools (counter to Linear).
- **"Pixar storyboard on cream paper"** — Family. Illustration-led, chromatic, warm.
- **"Softly Lit Gradient Canvas"** — Base44, Dia Browser. Pastel/airy gradient atmospheres.
- **"Cinematic cockpit behind warm light"** — Superhuman. Aubergine + glassmorphic + warm.
- **"Electric storm over a blueprint"** — Antimetal. Two-mode dark + light bridged by accent.
- **"Architectural Night Sky"** — General Intelligence Company. Dark hero + light UI.
- **"Shifting gradient depths on darkness"** — monopo saigon. Agency-extreme typography.
- **"White gallery canvas"** — Minimalissimo. Reductive achromatic.

Each archetype answers different design problems; an agent generating "a brand-distinct landing page" can reach for the archetype that matches the desired tone.

### Deltas from the 12 brands added 2026-05-04

The new brands extend several existing observations:

- **"Architectural blueprint on white marble" archetype is now triple-cited** — Stripe + Column + [[wiki/sources/augen-pro-design-md|Augen Pro]] all use the exact philosophy phrase but execute it differently (violet/single-typeface vs plum-orange/four-typeface vs blue/single-typeface-ultra-light).
- **AI-products converge on minimalist white**: [[wiki/sources/openai-design-md|OpenAI]] (pure white + OpenAI Sans), [[wiki/sources/perplexity-ai-design-md|Perplexity]] (off-white + pplxSans), and [[wiki/sources/anthropic-design-md|Anthropic]] (warm cream + Tiempos Headline) all share *typography-first restraint with near-zero chromatic chrome*. AI-product-restraint is becoming a category move.
- **Single-color-brand-identity** observation strengthens with new brands: [[wiki/sources/airbnb-design-md|Airbnb]]'s coral `#ff385c`, [[wiki/sources/gleap-design-md|Gleap]]'s magenta-purple, [[wiki/sources/contractbook-design-md|Contractbook]]'s dual-primary (yellow + blue) — most catalog brands continue the pattern.
- **Type-scale extremes**: [[wiki/sources/hyer-aviation-design-md|Hyer Aviation]] joins [[wiki/sources/monopo-saigon-design-md|monopo saigon]] at the giant-display end (131-187px), while [[wiki/sources/perplexity-ai-design-md|Perplexity]] and [[wiki/sources/virtual-design-md|Virtual]] sit at the minimal end (3 sizes only).
- **Unusual weights surface**: [[wiki/sources/customer-io-design-md|customer.io]]'s 475 weight and [[wiki/sources/augen-pro-design-md|Augen Pro]]'s 350 weight are non-standard increments — suggests both run custom variable fonts with weight granularity beyond the standard 100-step ladder.
- **Console / dashboard archetype** now has more entries: [[wiki/sources/authkit-design-md|AuthKit]] (frosted-glass dashboard) + [[wiki/sources/virtual-design-md|Virtual]] (minimalist console) join Linear / Mercury / Raycast / Hyperstudio in the dark-mode-tooling cluster.

## Sub-claims and details

### What's actually in a Refero DESIGN.md (per [[wiki/sources/stripe-design-md]])

A concrete DESIGN.md from Refero contains, in this rough order:

1. **Color palette** — split into Brand / Gradients / Neutrals subsections. Each color has a **descriptive name** (e.g. "Deep Violet", "Powder Blue") and a hex code. Gradients are CSS gradient strings.
2. **Typography** — font family + fallback + a per-step type scale specifying size, weight, line-height for ~7 named scale steps (display, heading-lg, heading, heading-sm, subheading, body, caption). Letter-spacing rules called out separately.
3. **Spacing & Shapes** — base unit (commonly 4px), a few named gaps (element / card-padding / section), border-radius per use case (interactive vs. layout), shadow vocabulary (named, e.g. xl / xl-2 / xl-3 / sm).
4. **Components** — a small set of token-referenced components (buttons, cards) specified as `<role>: <bg-token>, <fg-token>, <radius>, <padding>` strings. The components reference earlier-defined tokens, not raw values.
5. **Design philosophy** — one short paragraph. Provides the *why* the tokens decode to. *"Architectural blueprint on white marble — quiet efficiency, where information is paramount."*

The shape is consistent enough that an agent reading any Refero DESIGN.md can extract the same fields. Other DESIGN.md flavors (non-Refero) may differ, but Refero's instantiation is well-defined.

### General properties

- **Distribution**: viewable on the web; also distributable via MCP servers (Refero MCP) so agents can fetch them as a tool call.
- **Format is markdown, not JSON or design-token JSON**. This is a meaningful choice — it favors human-readable reference material agents can absorb in context, not machine-only token files.
- **Token references, not literals**: components reference named tokens (`Deep Violet`) rather than raw values (`#533afd`). This is what makes a DESIGN.md actionable for variant generation — swap the token, the component still has the right shape.
- **Necessarily partial**: Stripe's DESIGN.md has no icon system, no motion tokens, no breakpoint definitions, no z-index scale, no form-state colors. A DESIGN.md captures what the brand *wants enforced* and trusts the agent to fill in the rest from the philosophy.

## Open questions and contradictions

- **Refero shape is consistent across all 32 ingested brands**: same section order (color palette → typography → spacing/shape → components → philosophy), same field shapes (named colors with hex, type scale with size/weight/line-height/tracking, spacing with named tokens). Resolved across the catalog — for Refero specifically, yes.
- **A brand can have multiple DESIGN.md surfaces**: the wiki now has **two Apple DESIGN.md ingests** ([[wiki/sources/apple-design-md|MacBook Neo product page]] + [[wiki/sources/apple-design-md-alt|alternate Apple surface]]) that share core identity but diverge on accent palette and type scale. A future-design-md ingest for another large brand may reveal the same.
- **Is DESIGN.md a Refero-specific name or a general convention?** Likely the latter (analogous to AGENTS.md, CLAUDE.md, README.md), but unconfirmed from current sources outside Refero. A non-Refero DESIGN.md ingest would test this.
- **Relation to design-token standards** (W3C Design Tokens, Style Dictionary): DESIGN.md is plainer-text and seemingly not aimed at toolchain interop — it's aimed at LLMs reading prose. The Refero page mentions Tailwind v4, CSS Variables, and Design Tokens as alternate export formats — so the markdown is the human-readable surface and the structured exports are the toolchain surface.
- **Provenance** *(updated 2026-05-04)*: 32 of 33 raw files are now the official Refero Copy.md export (replacing earlier WebFetch extractions). The remaining 1 (Acctual) still uses the older WebFetch-extracted format. The 2026-05-04 batch upgrade resolved the prior "WebFetch may miss advanced fields" caveat — current raw files are 3-5× richer than the prior versions and contain full token specs, component specs, and philosophy text.

## Related concepts

- [[markdown-as-agent-contract]] — the broader pattern DESIGN.md instantiates.
- [[llm-wiki-pattern]] — sibling instance of the same meta-pattern in the personal-knowledge domain.

## Related entities

- [[wiki/entities/refero]] — primary publisher of DESIGN.md files.
- **32 brands have ingested DESIGN.md pages** (as of 2026-05-04). Original 20: [[wiki/entities/acctual]], [[wiki/entities/anthropic]], [[wiki/entities/antimetal]], [[wiki/entities/apple]], [[wiki/entities/base44]], [[wiki/entities/column]], [[wiki/entities/cursor]], [[wiki/entities/dia-browser]], [[wiki/entities/elevenlabs]], [[wiki/entities/family]], [[wiki/entities/general-intelligence-company]], [[wiki/entities/hyperstudio]], [[wiki/entities/linear]], [[wiki/entities/mercury]], [[wiki/entities/minimalissimo]], [[wiki/entities/monopo-saigon]], [[wiki/entities/raycast]], [[wiki/entities/stripe]], [[wiki/entities/superhuman]], [[wiki/entities/titan]]. Added 2026-05-04: [[wiki/entities/airbnb]], [[wiki/entities/all-in-one-salon]], [[wiki/entities/augen-pro]], [[wiki/entities/authkit]], [[wiki/entities/contractbook]], [[wiki/entities/customer-io]], [[wiki/entities/gleap]], [[wiki/entities/hyer-aviation]], [[wiki/entities/openai]], [[wiki/entities/perplexity-ai]], [[wiki/entities/ui]], [[wiki/entities/virtual]]. Plus the alternate Apple surface ([[wiki/sources/apple-design-md-alt]]).

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/stripe-design-md]] and 32 other `<brand>-design-md` source pages (Apple has two: MacBook Neo + alternate surface).
- [[wiki/sources/nexu-io-open-design]] — surfaces 138 alternate DESIGN.md files in Open Design's catalog using a richer 9-section schema.
- [[wiki/sources/open-design-catalog]] — companion catalog of all 139 Open Design DESIGN.md files (live count) across 20 categories.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — first-party Anthropic instance: Claude Design emits a Design.md spec as reusable source of truth across assets.
