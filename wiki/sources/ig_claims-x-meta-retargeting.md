---
type: source
title: Zack (ig_claims) — Meta retargeting for service businesses (5-stage conviction funnel)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/ig_claims/status/2052735264871899246
source_type: x-thread
author: Zack (ig_claims)
source_date: 2026-05-08
raw_path: raw/how i scale service-based businesses with meta retargeting campaigns.md
content_status: substantive
tags: [paid-acquisition, meta-ads, retargeting, service-business, conviction-model, b2b-marketing]
---

# Zack (ig_claims) — Meta retargeting for service businesses (5-stage conviction funnel)

> Zack documents a **5-stage conviction-layered retargeting funnel** for service businesses with measured results: $43 cost-per-lead on cold traffic vs $12 on retargeting (3.6× cost compression); 4.2× conversion rate; 23% of total bookings at 11% of total ad spend over 36 months. The substantive contribution is the **Conviction Gap Model** — psychology-stage segmentation rather than just behavior-stage segmentation. Composes cleanly with [[switching-forces]] (push/pull/habit/anxiety) at the operational layer.

## TL;DR

Most service businesses run retargeting as one campaign to anyone who visited the site. That's wrong. Conviction state matters more than visit state — *"someone who bounced after 8 seconds shouldn't see the same message as someone who watched 80% of your VSL and filled out half an application."* Zack's fix: 5 stages keyed on *what the prospect has and hasn't done*, with stage-specific creative that adds conviction points systematically.

## The Conviction Gap Model

A cold prospect lands at conviction 10/100. Closing a $5K-$15K/month retainer requires reaching 85-90/100. Each retargeting touchpoint is designed to add specific conviction points:

| Force | +Conviction |
|---|---|
| Authority proof | +15 |
| Social proof | +20 |
| Process clarity | +10 |
| Objection removal | +15 |
| Risk removal | +20 |
| Urgency | +10 |

Total possible: +90, exactly matching the gap from 10 to 100. A well-built funnel delivers all of these sequentially over 7-21 days, so by the time someone books a call they're at 80+ conviction *before you say a word*.

**Cross-cite to [[wiki/concepts/switching-forces]]**: authority + social proof = pull-strengthening; objection removal + risk removal = anxiety-defeating; urgency = push-amplifying. The two frameworks compose cleanly.

## The 5-stage retargeting funnel

| Stage | Audience | Conviction | Message | Creative format | Frequency goal |
|---|---|---|---|---|---|
| **1. Engaged cold** | Visited page, no opt-in | 10-20 | Education, no selling | 60-90s educational founder video | 2-3 exposures over 3-5 days |
| **2. Warm engaged** | Watched 50%+ VSL or consumed lead magnet | 30-45 | Specific social proof | Client testimonial video (story arc) | 2-3 exposures over 3-5 days |
| **3. Applied/partial** | Started application, didn't complete | 45-60 | Objection handling | Founder-direct video addressing the specific drop-off objection | 3-4 exposures in 48-72hrs |
| **4. Completed app, no booking** | Submitted full app, no calendar | 60-70 | Urgency + ease + social proof | "Someone like you booked last week" + friction removal | Daily for 5 days, then weekly for 2 more weeks |
| **5. Booked, no-show** | Calendar booking, no-show | 50 | Re-engagement without shame | **SMS over ads** (ad retargeting feels like being chased; SMS feels human) | 24h text → 48h case study → 72h ad retargeting |

### Specific creative examples (cited in thread)

- **Stage 1 (fractional CFO client)**: *"Most profitable agencies I know feel broke every month. Here's why — and it's not what you think."* CTR: 7.2% (~3× cold traffic CTR).
- **Stage 2 (fractional CFO)**: testimonial — *"I was spending 15 hours a week stressed about payroll even though we were profitable. CFO pulled our financials and found $140k we didn't know we had in unbilled work within 30 days. Now I check the dashboard once a week."* — specific time investment, specific finding, specific outcome, specific ongoing cadence.
- **Stage 3 (legal funding)**: *"If you stopped on question 3 — that's the question most people overthink. You don't need a perfectly summarized case. You just need to write what happened."* — recovered 23% of dropped applications.
- **Stage 5 (insurance brokerage)**: 31% of no-shows rebooked within 7 days using the SMS sequence.

## Audience segmentation in Meta Ads Manager

Zack's setup (custom audiences):
- **Stage 1**: website visitors all pages, 7-30 days, exclude buyers and converters.
- **Stage 2**: video viewers 50%+ VSL, 7-30 days, exclude buyers and converters.
- **Stage 3**: landing-page application starters (custom event when form opens but doesn't submit), 7 days.
- **Stage 4**: application completers who haven't booked (custom event on confirmation page; exclude calendar bookings), 7-14 days.
- **Stage 5**: calendar bookings without confirmation pixel (requires proper pixel setup on thank-you page), 3-7 days.

**Every exclusion matters.** Without exclusions, you show acquisition ads to existing clients — wastes money, confuses message.

## The economics

For Zack's fractional CFO client (36 months):

| | Cold traffic | Retargeting |
|---|---|---|
| Cost per lead/click | $43 (per lead) | $8 (per click) |
| Convert rate | 31% email→booking | 68% click→booking |
| Cost per booked call | $139 | **$12** |
| % of total bookings | 77% | 23% |
| % of total ad spend | 89% | **11%** |

**Headline rule**: if your retargeting budget is < 20-25% of your cold traffic budget, you're leaving closed deals on the table from leads you already paid to generate.

## What operators miss

The most common mistake: running retargeting to the *same landing page* as cold traffic. Cold traffic lands on an educational page designed to build trust from zero. Warm retargeting traffic already trusts you — they need a page designed to *convert*, not educate.

Zack's retargeting-specific landing pages: skip education, lead with most compelling proof, impossible-to-miss CTA, shorter form (qualified prospects need less screening), specific urgency (capacity / timeline / bonus). Result: 31% conversion vs 12% on cold-traffic page (2.6× delta).

## Notable quotes

> "Cold traffic converts once and then it's gone. Retargeting converts the same people multiple times - across multiple days, multiple touchpoints, and multiple conviction-building moments - until the decision to buy feels obvious and inevitable."

> "Retargeting done right is the highest-ROI lever in your entire meta ads account — because you're spending to close leads you already paid to generate."

> "Stage 5 SMS over ads, because ad retargeting feels like being chased, while a personal SMS feels like a human reaching out."

## Cross-cite with the wiki

- **[[switching-forces]]**: Zack's 6-conviction-force model (authority / social proof / process clarity / objection removal / risk removal / urgency) maps cleanly onto push/pull/habit/anxiety. Authority + social proof = pull-strengthening (+ habit-defeating); objection removal + risk removal = anxiety-defeating; urgency = push-amplifying. Worth a sub-pattern note in the switching-forces concept page.
- **[[ai-seo]]**: adjacent. Zack's funnel acquires; AI-SEO captures search intent. Different stages of the same problem.
- **[[landing-page-patterns]]**: Zack's *retargeting-specific landing pages* are a domain-specific extension. Worth a sub-pattern note: landing-page-patterns canon currently focuses on cold-traffic-first landing pages; retargeting pages have different optimal patterns (skip education, lead with proof, shorter form).
- **[[ai-automation-services]]**: Zack's content lives in the *paid-acquisition* lane — different from the wiki's existing AI-automation-services-services creators (Khairallah / Vacca / Sarvesh / CyrilXBT) who automate *delivery*. Zack automates *acquisition*. The two compose: Zack's funnel + Sarvesh's Cowork SEO = full funnel coverage.

## Notes

- **Vedge implication**: Vedge's `vedge_landing` is currently a single landing surface. If/when Vedge runs paid Meta ads (currently doesn't, AFAIK), the cold-traffic-vs-retargeting split + retargeting-specific landing pages are the right shape. The 5-stage conviction model is directly applicable: a hospital admin starts at conviction 10/100; a hospital admin who watched the demo video and partially completed sign-up is at 45-60 — *they need a different page than someone hitting `vedge.health/` for the first time*.
- **Self-attribution to verify**: $10M+ generated for service-based businesses through Meta ads funnels. Not independently verified — author's own claim.

## Mentioned entities

- [[wiki/entities/ig_claims]] — author.

## Related concepts

- [[switching-forces]] — composable framework; conviction-gap model maps onto push/pull/habit/anxiety.
- [[landing-page-patterns]] — retargeting-specific landing pages are a sub-pattern.
- [[ai-seo]] — adjacent at acquisition layer.
- [[ai-automation-services]] — adjacent (acquisition vs delivery).

## Related sources

- *(none in wiki at acquisition layer; this is the first.)*
