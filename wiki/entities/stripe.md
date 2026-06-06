---
type: entity
title: Stripe
entity_type: organization
created: 2026-05-02
updated: 2026-06-06
website: https://stripe.com
aliases: []
tags: [refero-catalog, yc-unicorn, payments, landing-page-patterns, design-md-ingested]
---

# Stripe

> Payments infrastructure company; YC unicorn ($65B market cap referenced); featured brand in the [[wiki/entities/refero|Refero]] design-reference catalog, analyzed in the [[wiki/sources/clear_graphics-yc-unicorn-landing-pages|YC unicorn landing-pages analysis]], and the **first brand whose full DESIGN.md has been ingested** into the brain ([[wiki/sources/stripe-design-md]]).

## Profile

Stripe is a payments infrastructure company. In this wiki it is the most substantively-treated brand entity — cited by **three independent sources** covering visual identity ([[wiki/entities/refero|Refero]]), page structure ([[wiki/sources/clear_graphics-yc-unicorn-landing-pages|clear_graphics]]), and design tokens ([[wiki/sources/stripe-design-md|the ingested DESIGN.md]]). Together they describe what Stripe *looks like*, *acts like*, and *is built on* at the design layer. *(Stripe's product surface, technical architecture, and business model still lack a primary-source ingest in this wiki — what's captured here is the design and brand-aesthetic axis.)*

## Design system summary

Per [[wiki/sources/stripe-design-md]] (full content in `raw/stripe/DESIGN.md`):

- **Identity color**: Deep Violet `#533afd`. The single load-bearing brand color.
- **Neutrals are blue-tinted, not gray** — Midnight Ink `#061b31`, Slate Blue `#50617a`, Powder Blue `#e5edf5`, Porcelain White `#f8fafd`.
- **Typography**: `sohne-var` (proprietary). Display weight 300 at line-height 1.03 with -0.03em letter spacing. Body weight 400 at line-height 1.2.
- **Spacing**: 4px base unit. 8px element gap. 12px card padding. 64px section gap.
- **Border radius**: 4px for interactive (buttons, inputs, tags, images); 6px for layout containers (cards).
- **Components specified**: Primary Filled / Ghost / Outlined buttons, Default and Feature cards — all in token references.
- **Design philosophy**: *"Architectural blueprint on white marble — serene white background with structured grid layouts and a single vibrant violet. Quiet efficiency, where information is paramount."*

## Key facts

- **Website**: https://stripe.com
- **Market cap referenced**: $65B (per [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]]).
- **Refero style page**: https://styles.refero.design/style/48e5de76-05d5-4c4e-a269-c7c245b291ec
- **Refero mood descriptor**: "Architectural blueprint on white…" *(truncated in [[wiki/sources/refero-design-systems-for-ai-agents]].)*

### Landing-page patterns exemplified
Per [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]]:
- **Category-defining headline**: "financial infrastructure for the internet".
- **Product-in-the-hero**: dashboard shown.
- **Social proof through scale**: "global GDP running on Stripe".
- **Minimal navigation**: 5 items.
- **Audience personalization**: developers vs. business owners.
- **Footer as navigation hub**: 50+ links organized by category.

### Product, infrastructure, and agent-commerce facts
*(the non-design axis the earlier ingests left open)*
- **Agent harness default**: Stripe's production harness caps retry attempts at two (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Micro-SaaS stack**: named as the payment layer in the [[wiki/entities/claude-code|Claude Code]] + Stripe + [[wiki/entities/supabase|Supabase]] + domain shipping stack; referenced via the "wake up to Stripe notifications" fantasy (per [[wiki/sources/exploraX_-5-solo-ai-business-models]]).
- **Payments-cost collapse**: cited as the technology that "made payments cheap," one collapsed dimension of operational overhead (per [[wiki/sources/kushwah-aaryan-future-of-work]]).
- **Agent-managed accounts prediction**: the essay predicts Stripe's agent-managed financial accounts cross 100,000 active accounts by end of 2026 (per [[wiki/sources/kushwah-aaryan-future-of-work]]).
- **Stablecoin rails**: Stripe's Bridge acquisition is named among stablecoin settlement rails (per [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- **Agent-to-merchant settlement**: Stripe Issuing provides virtual cards scoped to a single transaction with a single merchant (per [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- **Strategy-reference reflex**: named by Doshi as the company teams reflexively reference to sound strategic — "Someone will reference what Stripe did" (per [[wiki/sources/shreyas-get-to-the-core-of-the-thing]]).

## Positions and claims

- **A landing page should describe the category it owns, not what the product does technically** — Stripe's "financial infrastructure for the internet" is the canonical example of [[landing-page-patterns|category-defining headlines]]. *(Implicit by the source's analysis.)*

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]] — featured brand in the design-reference catalog.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — landing-page analyzed as an exemplar of multiple patterns.
- [[wiki/sources/stripe-design-md]] — full DESIGN.md (colors, typography, spacing, components, philosophy) ingested 2026-05-02.
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — named docs target for Context7.
- [[wiki/sources/shreyas-get-to-the-core-of-the-thing]] — cited as the archetypal "what [big company] did" reference reflex in strategy meetings.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — payment layer in the micro-SaaS stack; "wake up to Stripe notifications" framing.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — cited for a concrete production error-handling default (retry attempts capped at two).
- [[wiki/sources/kushwah-aaryan-future-of-work]] — prediction about agent-managed financial accounts; payments-cost-collapse example.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — Bridge acquisition (stablecoins) + Stripe Issuing virtual cards for agent-to-merchant settlement.

## Related entities

- [[wiki/entities/refero]] — publishes the catalog Stripe appears in.

YC unicorns analyzed alongside in clear_graphics:
- [[wiki/entities/airbnb]]
- [[wiki/entities/coinbase]]
- [[wiki/entities/instacart]]
- [[wiki/entities/doordash]]
- [[wiki/entities/dropbox]]
- [[wiki/entities/gitlab]]
- [[wiki/entities/gusto]]

## Related concepts

- [[design-md]]
- [[markdown-as-agent-contract]]
- [[landing-page-patterns]]
