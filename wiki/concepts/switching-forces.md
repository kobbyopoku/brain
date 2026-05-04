---
type: concept
title: Switching Forces
created: 2026-05-04
updated: 2026-05-04
aliases: [push pull habit anxiety, four switching forces]
tags: [marketing, cro, customer-research, framework]
---

# Switching Forces

> Four forces that explain why customers switch products and why they don't: **Push** (frustration with current solution), **Pull** (attraction to new solution), **Habit** (inertia keeping them stuck), **Anxiety** (fears about switching). Marketing that addresses only one (typically Pull) ignores three of the four reasons conversion fails.

## Definition

The **Switching Forces** framework identifies four discrete forces operating in every customer-switching decision:

| Force | Direction | Question |
|---|---|---|
| **Push** | Toward leaving the current solution | What's frustrating enough about what they have to make them start looking? |
| **Pull** | Toward adopting the new solution | What's attractive about your product that makes them want to switch? |
| **Habit** | Toward staying with the current solution | What keeps them stuck even when unhappy? |
| **Anxiety** | Toward not switching at all | What fears about switching hold them back even when they want to move? |

**Push** and **Pull** are progress-forces (they move the customer toward your product). **Habit** and **Anxiety** are friction-forces (they keep the customer where they are). The decision to switch happens only when progress-forces > friction-forces.

## Why it matters

Most marketing copy addresses only **Pull** — *"here's why our product is great."* This is a structural error: it leaves three of the four forces unaddressed, including the two most common reasons conversion fails (Habit and Anxiety).

A landing page that talks only about features ignores:
- The *push* — why the prospect is frustrated enough to be reading at all (the page should acknowledge it)
- The *habit* — why they've put up with the current solution this long (the page should address how easy it is to switch)
- The *anxiety* — what could go wrong if they switch (the page should preempt the specific fears)

The framework is especially powerful because it's *generative* — once you map the four forces for your product/market, you have explicit copy targets: *here's a Push line in the headline, a Pull section in the benefits block, a Habit-defeating line near the CTA, an Anxiety-defeating line in the FAQ.*

## Treatment across sources

- [[wiki/sources/noisyb0y1-marketingskills-repo]] — canonical wiki source. Documented in the [[wiki/entities/marketingskills-repo|marketingskills repo]]'s Switching Forces skill. Framed as *"the most underrated framework in the entire repo."* Origins predate this — typically attributed to Bob Moesta and Chris Spiek's Jobs-to-Be-Done research — but this source is the wiki's first ingest with the framework named.

## Sub-claims and details

### Mapping the four forces (a worked example for [[wiki/projects/vedge|Vedge]])

For Vedge's African healthcare facility audience, switching from paper records / fragmented systems to Vedge:

- **Push**: scattered paper notes lost between visits; NHIS claims taking 60+ days to reimburse; clinicians spending hours after hours rewriting orders; no visibility into pharmacy stock; lab results lost in WhatsApp.
- **Pull**: integrated EHR + billing + claims + lab + pharmacy in one system; faster NHIS reimbursement via electronic claims; mobile staff app; patient companion app; African-context-aware (Paystack, Flutterwave, NHIS).
- **Habit**: 30+ years of paper-based clinical workflow; staff trained on existing fragmented tools; clinicians' personal note systems; tribal knowledge of "how things work here."
- **Anxiety**: PHI security in a multi-tenant cloud system; training cost across all clinical staff; data migration risk from existing systems; what happens during downtime; regulatory exposure if something goes wrong.

For Vedge's marketing site to convert, copy must address all four. *Pull-only* messaging — "Vedge is the modern EHR for African healthcare" — would convert poorly because it leaves Habit and Anxiety untreated.

### Generic copy patterns by force

- **Push**: "Tired of [specific frustration]?" / "When [bad scenario] happens, you can't afford to [consequence]."
- **Pull**: "Get [specific outcome] in [timeframe]" / "[Product] gives you [feature] without [drawback]."
- **Habit**: "Switching takes [short time] / We import from [current solution] automatically / Keep your existing [workflow/tool] while we [extend it]."
- **Anxiety**: "Your data stays [where] / [Specific compliance certification] / 30-day money-back / [Real customer quote about successful switch]."

The CTA itself can address forces: *"Start with one [small commitment]"* (anxiety-killer); *"Migrate from [competitor] in 5 minutes"* (habit-killer); *"Get [outcome] this week"* (pull).

### Composition with other frameworks

- **Switching Forces + [[landing-page-patterns]]**: each of the 11 unicorn landing-page patterns can be mapped to which switching forces it addresses. Pattern 5 (social proof through scale) addresses Anxiety. Pattern 7 (audience personalization) helps with Push (we recognize your specific frustration). Pattern 8 (CTA is always free) addresses Anxiety.
- **Switching Forces + [[ai-seo]]**: AI search queries often surface Push and Anxiety language ("how do I stop losing track of...", "is it safe to switch from..."). Content optimized for AI citation should answer the specific Push/Anxiety questions, not just the Pull queries.

## Open questions and contradictions

- **Force interaction**: the framework treats forces as additive but in practice they interact. High Anxiety can override high Push (people stay frustrated rather than switch). High Habit can dampen Push perception (people stop noticing they're frustrated). No source ingested addresses these interactions formally.
- **Cross-cultural variance**: the framework was developed in Western B2B contexts. African healthcare facility owners may weight Habit and Anxiety differently than American SaaS buyers — habit is reinforced by intergenerational training; anxiety is amplified by data-protection regulatory uncertainty in young legal regimes.
- **The framework's origin** is typically attributed to Bob Moesta and Chris Spiek's Jobs-to-Be-Done research, but the marketingskills source presents it without attribution. Worth tracking when next ingest covers this lineage.

## Related concepts

- [[landing-page-patterns]] — Switching Forces tells you *what* to address; landing-page patterns tell you *how* to structure the page.
- [[ai-seo]] — content optimized for AI citation should answer Push and Anxiety queries, not just Pull.
- [[context-file]] — `product-marketing-context.md` should explicitly enumerate the four forces for the product.
- [[ai-automation-services]] — services builders should map their own four forces before pitching.

## Related entities

- [[wiki/entities/corey-haines]] — repo author who codified this framework into a Claude skill.
- [[wiki/entities/marketingskills-repo]] — where the framework lives as an executable skill.

## Mentioned in

- [[wiki/sources/noisyb0y1-marketingskills-repo]]
