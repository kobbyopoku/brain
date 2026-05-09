---
type: source
title: bloggersarvesh — Top 20 Claude prompts for local SEO (4 parts × 12-week roll-out)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/bloggersarvesh/status/2036068241936896421
source_type: x-thread
author: Sarvesh Shrivastava (bloggersarvesh)
source_date: 2026-03-23
raw_path: raw/Top 20 Claude Prompts For SEO - The Only Stack You'll Ever Need..md
content_status: substantive-verbatim
tags: [ai-seo, local-seo, claude-cowork, claude-prompts, gbp, content-os, alventra-marketing]
---

# bloggersarvesh — Top 20 Claude prompts for local SEO (4 parts × 12-week roll-out)

> Sarvesh Shrivastava's complete pasteable prompt-library for local SEO using Claude Cowork. **20 detailed prompts across 4 parts**: Google Business Profile (8) / Website (5) / Backlinks + Authority (3) / Content + Tracking (4). Includes a master "business context loader" that runs once per Cowork project so subsequent prompts are sharper. Author runs Alventra Marketing (14 years home-services SEO; plumbers, HVAC, lawyers, cleaning). Sibling to his earlier [[wiki/sources/bloggersarvesh-x-2032130279494853118|Cowork-for-SEO ($10K/mo agency replacement)]] post — that one was the *thesis*; this is the *prompt arsenal under it*. **Strongest [[ai-seo]] prompt-pack source in the wiki by a wide margin.**

## TL;DR

20 prompts grouped into 4 parts:

| Part | Prompts | Domain |
|---|---|---|
| **1: Google Business Profile** | 1-8 | GBP category audit / attributes audit / competitor review teardown / review response strategy / GBP posts / services optimization / GBP description / photo audit |
| **2: Website** | 9-13 | Keyword gap audit / money page audit / service+city page builder / GSC analysis / review sentiment analysis |
| **3: Backlinks + Authority** | 14-16 | Competitor backlink audit / local citation audit / local search-intent mapping |
| **4: Content + Tracking** | 17-20 | Content gap analysis / entity optimization (knowledge-graph-level) / GBP posting-pattern analysis / monthly SEO performance report |

12-week roll-out plan:

- **Week 1**: prompts 1, 2 (categories + attributes — fastest fixes).
- **Week 2**: 3, 4, 5 (reviews + GBP posts).
- **Week 3**: 6, 7, 8 (services + description + photos).
- **Week 4**: 9, 12 (keyword gap + GSC).
- **Weeks 5-6**: 10, 11, 13 (website audit + city pages + sentiment).
- **Weeks 7-8**: 14, 15, 16 (backlinks + citations + intent mapping).
- **Weeks 9-10**: 17, 18, 19 (content gaps + entity + posting patterns).
- **Weeks 11-12**: 20 (monthly report).

## Key takeaways

### The "business context loader" pattern (run once per Cowork project)

> *"Here is everything you need to know about my business before we start any SEO work. Reference this every time I ask you to run an audit, build a strategy, or analyze competitors. Never ask me for this information again."*

A 7-section structured-intake template covering BUSINESS BASICS / SERVICES + MARKET / SEO GOALS / CURRENT STANDINGS / COMPETITORS / WHAT I'VE TRIED / HOW I WANT YOU TO WORK. Run once at the start of a Cowork project; every subsequent prompt becomes sharper because it inherits this context. **Direct application of [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] at workspace scope** — same shape as Khairallah's `ABOUT ME/` folder + Shann's `/strategy` files. Three independent sources now describe the *one-time business context as agent contract* pattern.

### Entity optimization (Prompt 18 — the most advanced)

> *"Most local SEOs don't even know this is a lever. Google doesn't just rank websites — it ranks entities. Your business needs to exist as a verified entity in Google's knowledge graph to unlock the highest level of local trust signals."*

Prompt 18 covers: knowledge-panel audit / Wikidata check / schema markup audit (LocalBusiness JSON-LD) / brand-mention consistency. Generates the exact JSON-LD code ready to paste. **Worth canonizing as a [[ai-seo]] sub-pattern**: *entity optimization* sits one layer beneath keyword optimization and is what compounds for years.

### Buyer-journey keyword mapping (Prompt 16)

Maps every keyword in a niche to one of 4 stages:

| Stage | Definition | Example | Where to optimize |
|---|---|---|---|
| **1: Problem-unaware** | Has problem, doesn't know name | *"water coming through ceiling"* | Educational content (low priority) |
| **2: Problem-aware** | Researching solutions | *"how to fix leaking roof"* | Blog content funneling to service pages |
| **3: Solution-aware** | Comparing options/providers | *"plumber vs DIY pipe repair"* | Comparison + FAQ pages |
| **4: Ready to hire** | Wants to book now | *"emergency plumber [city]"* | Service pages + GBP |

> *"Stage 4 keywords have lower volume but they convert at 5-10× the rate. Most businesses spend all their SEO budget on Stage 2 keywords that generate traffic but not calls."*

This is the **clearest mapping of keyword intent to revenue** in the wiki. Pairs with [[switching-forces]] (Stage 4 = active push + low anxiety) and [[wiki/sources/exploraX_-google-maps-leadgen|exploraX_'s]] mental model (find leaky-bucket businesses = local intent).

### Page 2 keyword goldmine (Prompt 12)

> *"Page 2 keywords are the lowest hanging fruit in all of SEO. Someone is already searching for exactly what you offer — you're just one optimization push away from being visible."*

Prompt 12 pulls every keyword ranking position 11-20 with ≥100 impressions/month, then for each: title-tag fixes / H1 fixes / first-100-words check / word-count / internal-link audit / meta-description rewrite. **30-day optimization sprint** with exact copy, not instructions. Strongest *prioritization-by-existing-signal* methodology in the wiki's SEO coverage.

### Review sentiment analysis (Prompt 13 — "the prompt most agencies don't know exists")

Reverse-engineers competitor reviews to extract:

- Top 20 emotional words customers use most frequently (e.g. *"relieved", "impressed", "finally", "trustworthy"*).
- Top 10 specific outcomes customers mention (e.g. *"fixed in one visit", "no mess left behind", "arrived on time"*).
- Top 5 fears or frustrations *before* the service (*"worried it would cost a fortune"*).
- Exact phrases customers use when recommending to others (*"the money phrases for your website"*).
- Language patterns in 5-star reviews that don't appear in 3-star reviews.

Then rewrites GBP description + homepage headline + review-request script + 3 social-proof statements **in the customer's own emotional language**. Extension of [[markdown-as-agent-contract]] / voice-profile-extraction at the *customer voice* level (vs Shann/CyrilXBT at the *creator voice* level). Worth flagging as a sub-pattern.

### Productized prompt-pack as a deliverable

The 20 prompts are explicitly *pasteable agency deliverables* — Sarvesh runs the full system at Alventra Marketing as a **service**. *"If you want my team to run this entire system for your business — every audit, every optimization, every month of execution — that's what we do at Alventra Marketing."* Composes with [[ai-automation-services]] / [[services-as-software]] — the prompt pack is *the IP that makes the service replicable*. Pairs with [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah's]] *"the skill file is the engine of every automation."*

### Why this is bloggersarvesh's 2nd wiki source

[[wiki/sources/bloggersarvesh-x-2032130279494853118]] (earlier post): the *Cowork-for-SEO $10K/mo agency replacement* thesis. This source: the **prompt arsenal that makes the thesis runnable**. The earlier post says *"replace agencies"*; this post is the *substance you'd hand a junior to actually do it.*

## Notable quotes

> "Wrong categories = invisible for high-intent searches. It's that simple."

> "10 reviews a month, each response mentioning your service and city — that's 120 pieces of keyword-rich content on your GBP per year that you didn't have before."

> "Google ranks pages not websites. If you don't have a page specifically about [service] in [city], you will not rank for that search."

> "Most businesses write their own website copy about themselves. The businesses that dominate write their copy in the language their customers actually use."

> "If you can't measure it you can't manage it. But measuring the wrong things is worse than measuring nothing. Calls and revenue from organic are the only numbers that actually matter."

> "90 days of consistent execution on this system and you will outrank businesses that have been established for years."

## How this composes with the wiki

- [[wiki/concepts/ai-seo]] — **strongest prompt-pack source**. Adds entity optimization, page-2 goldmine, review sentiment analysis, and 4-stage buyer-journey mapping. Material concept-page upgrade.
- [[wiki/concepts/markdown-as-agent-contract]] — *"business context loader"* is a textbook instance of one-time agent-contract installation at workspace scope.
- [[wiki/sources/bloggersarvesh-x-2032130279494853118]] — sibling thesis post; compose them as *thesis* + *prompt arsenal*.
- [[wiki/sources/exploraX_-google-maps-leadgen]] — adjacent (small-business local lead-gen). exploraX_ = *find prospects*; bloggersarvesh = *what to deliver after they say yes*.
- [[wiki/sources/shannholmberg-content-os]] — sibling Content OS for non-SEO content. Same architecture (workspace folder + voice profile + verified output rubric); different domain.
- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — sibling 20-prompts catalog; different niche (personal productivity vs local SEO).
- [[ai-automation-services]] — productized prompt-pack as service deliverable.
- [[switching-forces]] — Stage 4 keywords = active push + low anxiety.

## Mentioned entities

- [[wiki/entities/bloggersarvesh]] — Sarvesh Shrivastava (existing entity; gets 2nd post note).
- [[wiki/entities/alventra-marketing]] — *(stub candidate)* Sarvesh's local-SEO agency.
- [[wiki/entities/cowork]] — primary runtime.
- [[wiki/entities/anthropic]] — Claude provider.
- [[wiki/entities/google-business-profile]] — *(stub candidate)* primary surface for prompts 1-8.
- [[wiki/entities/semrush]] — *(stub candidate)* used in prompts 9, 16, 17.
- [[wiki/entities/ahrefs]] — *(stub candidate)* used in prompt 14.
- [[wiki/entities/google-search-console]] — *(stub candidate)* used in prompts 12, 20.

## Related concepts

- [[ai-seo]] — primary concept-page upgrade target.
- [[markdown-as-agent-contract]] — business-context-loader pattern.
- [[ai-automation-services]] — productized prompt-pack as deliverable.
- [[switching-forces]] — buyer-journey keyword mapping.
- [[claude-code-skills]] — adjacent (prompt-as-skill).

## Related sources

- [[wiki/sources/bloggersarvesh-x-2032130279494853118]] — sibling thesis post.
- [[wiki/sources/exploraX_-google-maps-leadgen]] — lead-gen counterpart.
- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — sibling 20-prompts catalog (different niche).
- [[wiki/sources/shannholmberg-content-os]] — sibling content-OS pattern.
