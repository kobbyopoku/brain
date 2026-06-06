---
type: concept
title: Landing Page Patterns
created: 2026-05-02
updated: 2026-06-06
aliases: [unicorn landing patterns, conversion landing pages]
tags: [design, conversion, landing-pages, marketing]
---

# Landing Page Patterns

> Eleven recurring patterns observed on YC-unicorn-scale landing pages: category-defining headlines, hero simplicity, two-sided audience splits, product-in-the-hero, social proof through scale, minimal navigation, audience personalization, free CTAs, invisible speed, footer-as-sitemap, and design-system consistency. The wiki's reference catalog for product-page structure.

## Definition

A **landing page pattern** is a recurring design choice observed across high-converting product pages. The patterns are observed (not theorized): they emerged as YC-unicorn-scale companies converged on the same answers to the same constraints — millions of monthly visitors, dual-or-multi audiences, brand consistency across dozens of pages, a free-CTA-leads-to-sales-conversation funnel.

This concept is distinct from [[design-md|DESIGN.md]] — DESIGN.md captures **brand visual taste** (colors, typography, spacing, components); landing-page patterns capture **page-structural choices** (what goes in the hero, how navigation is sized, where CTAs live).

## Why it matters

For anyone building a product landing page, these patterns are a first-pass checklist that shortcuts hours of conversion-rate-research reading. The patterns also illuminate strategic constraints: at unicorn scale, certain page choices become forced (e.g. minimal nav because every nav item is a decision point at 10M monthly visits). For early-stage builders, the patterns are aspirational but partially adoptable — *"lead with whatever your biggest proof number is, even '500+ teams' beats no number."*

## Treatment across sources

- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — canonical wiki source. Analyzes landing pages of [[wiki/entities/stripe|Stripe]], [[wiki/entities/airbnb|Airbnb]], [[wiki/entities/coinbase|Coinbase]], [[wiki/entities/instacart|Instacart]], [[wiki/entities/doordash|DoorDash]], [[wiki/entities/dropbox|Dropbox]], [[wiki/entities/gitlab|GitLab]], [[wiki/entities/gusto|Gusto]] (combined ~$280B market cap) and extracts 11 patterns.
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] frames it as the **artifact to abandon, not optimize**: argues against optimizing the static landing page these patterns refine, betting instead on replacing it (per [[answer-engine-discovery]] and [[artifact-first-workflow]]). An opposing bet — *optimize the page* vs. *replace the page* — and a candidate for a future synthesis on that axis.
- [[wiki/sources/noisyb0y1-marketingskills-repo]] — the **evaluation companion** to clear_graphics's observation. Where clear_graphics catalogs *what unicorn pages do*, the [[wiki/entities/marketingskills-repo|marketingskills repo]]'s **CRO 7-question framework** is the diagnostic for *why a given page does or doesn't convert* — questions covering the 5-second test, primary CTA visibility, first-screen objection-handling, scroll-depth proof points, FAQ specificity, social-proof concreteness, and reading-difficulty grade level. Composes naturally with patterns: each pattern can be tested with the 7 questions. *The repo also frames CRO as **"a page is a sequence of arguments, not a collection of blocks"** — orthogonal to the patterns but useful as a copy-mental-model.* Adds [[switching-forces]] mapping: each unicorn pattern can be classified by which switching force it addresses (e.g. pattern 5 = anxiety-killer; pattern 8 = anxiety-killer; pattern 7 = push-acknowledger).

## The 11 patterns

### 1. Category-defining headline
Stake a claim to a category, don't describe what you do technically.
- Stripe: *"financial infrastructure for the internet"*
- Airbnb: *"belong anywhere"*
- Coinbase: *"the most trusted crypto platform"*
- DoorDash: *"your door to more"*
- Dropbox: *"keep life organized and work moving"*

### 2. Hero simplicity
Under 30 words total. The hero answers one question only — *"am I in the right place?"*

### 3. Two-sided marketplace splits
Marketplace unicorns split their hero into clearly labeled paths. Each audience gets its own CTA within 3 seconds.
- Airbnb: guests / hosts.
- DoorDash: order food / become a dasher.
- Instacart: consumer / shopper.

### 4. Product in the hero
At scale, the product is the selling point.
- Stripe shows its dashboard.
- Coinbase shows its wallet.
- GitLab shows its pipeline.
- Gusto shows its payroll dashboard.

### 5. Social proof through scale
Lead with whatever your biggest proof number is.
- *"Global GDP running on Stripe."*
- *"Join the 50+ million people already using GitLab."*
- For early stage: *"500+ teams"* beats no number.

### 6. Minimal navigation
Every additional nav item is a decision point.
- Stripe: 5 nav items.
- Airbnb: 3.
- Coinbase: 6.

### 7. Personalization by audience
- Stripe: developers vs. business owners.
- Coinbase: individual vs. institutional.
- Gusto: by company size.

### 8. The CTA is always free
- *"Get started"* (Stripe), *"sign up"* (Coinbase), *"try Dropbox free"*.
- Even enterprise sales pages lead with free self-serve. Enterprise sales happens after self-service adoption, not before.

### 9. Speed is invisible
Every unicorn page loads fast enough that you don't notice. Try loading a pre-seed startup's page after one of these — the difference is jarring.

### 10. Footer as navigation hub
At scale, the footer becomes a comprehensive sitemap.
- Stripe: 50+ links organized by category.
- Serves both SEO and discoverability.

### 11. Consistency across all pages
Identical design language site-wide. Result of rigorous design systems maintained by dedicated design teams.

## Sub-claims and details

- **Patterns 4 and 11 force investment in design infrastructure** — showing the product means keeping the product visual current; consistency means a design system. Both imply ongoing engineering / design cost.
- **Pattern 7's "audience personalization"** can be cheap (segment toggle) or expensive (server-side personalization based on visitor signals). The cheap version is easier and most of the value.
- **Pattern 5's "lead with biggest proof number"** scales down: *X enterprise logos*, *X teams*, *X power users*, *X countries* — anything that's a real number larger than 0 helps.
- **Patterns are not independent**: pattern 4 (product in hero) implies pattern 9 (speed) because product images need to load fast; pattern 11 (consistency) supports pattern 4 (the product visuals look like the marketing visuals).

## Open questions and contradictions

- **Are these patterns valid for B2B-only / enterprise-sales-only products?** The source's eight examples are all B2C-or-B2B-self-serve. A pure-enterprise product with no self-serve path may not follow pattern 8 (free CTA).
- **AI-era updates**: do AI-first companies follow these patterns or evolve them? Worth re-checking when AI-native company landing pages get analyzed in a future ingest.
- **Conversion data**: the patterns are observed at $280B+ companies. Whether they *cause* the conversion or merely correlate with the success isn't argued; the source assumes correlation is enough for prior-art use.

## Related concepts

- [[design-md]] — adjacent: per-brand visual tokens.
- [[markdown-as-agent-contract]] — adjacent: a landing page is a kind of human-facing contract.
- [[switching-forces]] — each pattern can be classified by which of the four forces (push/pull/habit/anxiety) it addresses; the patterns are *what* to do, switching forces explain *why*.
- [[ai-seo]] — pattern 4 (product in hero), pattern 5 (social proof), and well-structured FAQ blocks are the same artifacts that get cited by AI overviews; patterns naturally compose with AI SEO structural blocks.

## Related entities

The eight YC unicorns analyzed:
- [[wiki/entities/stripe]]
- [[wiki/entities/airbnb]]
- [[wiki/entities/coinbase]]
- [[wiki/entities/instacart]]
- [[wiki/entities/doordash]]
- [[wiki/entities/dropbox]]
- [[wiki/entities/gitlab]]
- [[wiki/entities/gusto]]

Plus:
- [[wiki/entities/clear_graphics]] — author.
- [[wiki/entities/marketingskills-repo]] — provides the CRO 7-question evaluation companion.
- [[wiki/entities/corey-haines]] — author of the CRO 7-question framework.

## Mentioned in

- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]]
- [[wiki/sources/noisyb0y1-marketingskills-repo]]
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] — opposing bet: replace the static page rather than optimize it.
