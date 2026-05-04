---
type: source
title: 139 Marketing Tactics + CRO Framework as Claude Skills (marketingskills repo) — noisyb0y1
created: 2026-05-04
updated: 2026-05-04
source_url: https://x.com/noisyb0y1/status/2050523761481285898
source_type: x-thread
author: noisyb0y1
source_date: 2026-05-02
raw_path: raw/139 marketing tactics and a full CRO framework that replace a $10,000month agency. One repo $0.md
tags: [marketing, cro, claude-code-skills, ai-seo, switching-forces, marketingskills]
---

# 139 Marketing Tactics + CRO Framework as Claude Skills (marketingskills repo) — noisyb0y1

> Showcases the [[wiki/entities/marketingskills-repo|coreyhaines31/marketingskills]] repository — a free, open-source skill-pack for Claude Code that replaces a $10K/month marketing agency. 139 growth tactics, 12 SEO playbooks, and frameworks for copywriting, CRO, pricing, A/B testing, AI SEO, and programmatic content. Notable as the most substantive non-design [[wiki/concepts/claude-code-skills|claude-code-skills]] application ingested in the wiki, with [[switching-forces]] as a distinctive new framework.

## TL;DR

The post documents [[wiki/entities/corey-haines|Corey Haines]]'s `marketingskills` repo — a Claude Code skill-pack that packages everything an experienced marketer would know into markdown files an AI agent can read and execute. Every skill begins by reading `product-marketing-context.md` (ICP, personas, pain points, objections, proof points, customer language). Frameworks in the repo: **Switching Forces** (push/pull/habit/anxiety), Headline formulas, CTA formulas, 7-question CRO framework, A/B test ICE scoring, Good-Better-Best pricing, **AI SEO** (cited-by-LLM as distinct from Google-ranked), 12 programmatic SEO playbooks, and a tool registry connecting skills to GA4/PostHog/Stripe/etc. via CLI. The architectural claim: marketing has always been expensive because it required people who know what to do AND how to measure it; this repo packages both into agent-readable form.

## Key takeaways

### The architectural pattern

- **Every skill reads `product-marketing-context.md` first.** Before any copy is written or page is analyzed. Without context the agent writes generic output; with context it knows your ICP, objections, proof points, and customer's exact words.
- **Customer language is verbatim**. Pulled from interviews, reviews, support tickets — not internal polished descriptions. *"Verbatim words from real customers ... are worth more than any polished internal description because they reflect how customers actually think and talk."*
- **The agent is positioned as a conversion copywriter** with four non-negotiable principles: clarity over cleverness, benefits over features, specificity over vagueness, customer language over company language.
- **Each skill connects to real tools** via a tool registry: GA4, GSC, Mixpanel, Amplitude, PostHog, Semrush, Ahrefs, HubSpot, Salesforce, Stripe, Mailchimp, Google Ads, Meta Ads, Hotjar, Optimizely. Each entry notes API, MCP, CLI, SDK availability. The execution chain: *"Agent skill → decides what needs to be measured → Tool registry → finds the right tool → CLI → runs the report."*

### The Switching Forces framework

[[switching-forces]] is the most distinctive contribution. Four forces that explain why customers change products and why they don't:

- **Push** — what's frustrating enough about the current solution to make someone start looking.
- **Pull** — what's attractive about the new solution that makes someone want to switch.
- **Habit** — what keeps people stuck even when unhappy.
- **Anxiety** — what fears about switching hold people back even when they want to move.

Most marketing focuses on Pull only. Skills in this repo are built to address all four. *"A landing page that only talks about features ignores the three forces that actually prevent conversion."*

### CRO: 7-question framework

A page is a sequence of arguments, not a collection of blocks. Every page should pass:

1. Is it clear in 5 seconds what this is and why it matters?
2. Does the headline communicate specific value?
3. Is there one primary CTA?
4. Can you scan the page visually?
5. Are there trust signals next to the CTA?
6. Are objections addressed?
7. Where is the friction — form, next steps, mobile, load time?

Combined with the **value-proposition / headline / CTA / visual hierarchy / trust signals / objections / friction** order-of-impact analysis sequence.

### A/B testing: hypothesis first

Structured hypothesis template: *"Because [observation/data], we believe [change] will cause [expected outcome] for [audience]. We'll know this is true when [primary metric + guardrails]."*

ICE scoring for prioritization: `(Impact + Confidence + Ease) / 3`.

Test duration formula: `Duration = (Sample per variant × variants) / (Daily traffic × % exposed)`. Heuristic: <14 days is feasible, >60 days reconsider.

### Pricing: three axes

- **Packaging** — what features and limits go in each tier.
- **Pricing metric** — what unit customers pay for.
- **Price point** — the actual number.

The principle: *"Price should be set based on value delivered, not cost to serve. It should sit between two numbers — the next best alternative and the perceived value of your product."*

Standard structure: Good-Better-Best with the Better tier as recommended; Best at 2-3x Better's price.

### AI SEO

Distinct discipline from Google-rank SEO. *"Traditional SEO gets you ranked. AI SEO gets you cited."* See [[ai-seo]] for the canonical wiki treatment.

Three pillars: **Structure** (make content extractable) + **Authority** (make content citable) + **Presence** (be where AI systems look).

Content block patterns that get cited:
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X?" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for natural language questions
- **Statistic blocks** with cited sources

The most underrated idea: **add `/pricing.md` or `/pricing.txt`** to your site so AI agents can programmatically read your pricing. *"In the near future your site is read not just by humans and search bots but by buying agents."*

### Programmatic SEO: 12 playbooks

Templates for creating pages at scale: Templates / Curation / Conversions / Comparisons / Examples / Locations / Personas / Integrations / Glossary / Translations / Directory / Profiles. The rule: *"100 strong pages beats 10,000 thin pages."*

### The 139 growth tactics — selected highlights

The interesting tactics aren't the obvious ones:

- **Glossary Marketing** — every industry term becomes an SEO page that ranks, brings exact-target audience, costs nothing after written.
- **Engineering as Marketing** — build a free calculator, generator, or tool. Attracts the right people, generates links, feeds acquisition funnel.
- **Importers as Marketing** — *"import from [competitor]"* as a feature reduces switching friction to near zero.
- **Proprietary Data Content** — data that only exists inside your product becomes a linkable asset when published.
- **Public Changelogs** — publishing what you ship signals momentum.
- **Reddit Keyword Research** — Reddit discussions contain the exact language customers use when no one is watching.
- **Founder Welcome Email** — personal email from the founder in first 24 hours has the highest open rate of any email in the sequence.

## Notable quotes

> "Marketing has always been expensive because it required people who know what to do AND how to measure it. This repo packages what those people know into markdown files that an AI agent reads and executes."

> "Without this file the agent writes generic output. With it the agent knows your ICP, your objections, your proof points and your customer's exact words."

> "100 strong pages beats 10,000 thin pages."

> "In the near future your site is read not just by humans and search bots but by buying agents."

## Notes

- **The repo is itself an instance of [[wiki/concepts/markdown-as-agent-contract]] applied to marketing.** Same pattern as Anthropic Skills, the AIS-OS template, the LLM Wiki — markdown files as the contract layer between humans and agents. Marketing-domain instantiation.
- **`product-marketing-context.md` is exactly the same shape as a [[wiki/concepts/context-file|context file]]** in [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah's]] AI-automation-services playbook. Different domain, identical pattern. The "context file as first-loaded asset" is becoming a load-bearing wiki convention.
- **Cross-cut with [[wiki/concepts/landing-page-patterns]]**: clear_graphics observed *which* patterns YC unicorns use; this repo provides the *evaluation framework* for testing whether a page exhibits them. Observation + evaluation = a complete CRO toolkit.
- **Directly applicable to [[wiki/projects/vedge|Vedge's]] `vedge_landing` site.** The 7-question CRO framework, headline formulas, and AI-SEO content blocks are immediately usable. The Switching Forces framework would be especially valuable for the African healthcare market — *push* (paper records / fragmented systems / no NHIS visibility), *pull* (Vedge's promise), *habit* (clinics doing things on paper for 30 years), *anxiety* (PHI security / training cost / regulatory exposure).
- **The "/pricing.md as machine-readable" idea is genuinely novel** in the wiki and worth tracking. As buying agents become real, structured-pricing endpoints become an SEO surface. Worth flagging on Vedge's landing-site design.
- **The repo is FREE** — `github.com/coreyhaines31/marketingskills`. Worth installing locally to inspect the actual skill files (this source is a *description*; the repo is the *artifact*).

## Mentioned entities

### People
- [[wiki/entities/noisyb0y1]] — post author.
- [[wiki/entities/corey-haines]] — repo creator.

### Products
- [[wiki/entities/marketingskills-repo]] — the artifact this source describes.

### Tools referenced (already in wiki or stub-worthy)
- GA4, GSC (Google Search Console), Mixpanel, Amplitude, PostHog (already in wiki), Semrush, Ahrefs, HubSpot, Salesforce, Stripe (already in wiki), Mailchimp, Hotjar, Optimizely. Not all created as entity pages — only PostHog and Stripe currently exist as wiki entities; the rest are referenced but un-stubbed.

## Related concepts

- [[switching-forces]] — canonical wiki source for the 4-force framework.
- [[ai-seo]] — canonical wiki source for citation-by-AI as a discipline.
- [[claude-code-skills]] — the marketingskills repo is a substantive instance.
- [[markdown-as-agent-contract]] — yet another instance of the meta-pattern.
- [[personal-claude-prompts]] — adjacent: marketingskills is the *registered-skills* version of personal-prompts.
- [[landing-page-patterns]] — observation companion to this source's evaluation framework.
- [[context-file]] — `product-marketing-context.md` is exactly this pattern.

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — sibling: Refero is design-tokens-as-skills; marketingskills is marketing-tactics-as-skills. Same shape, different domain.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — observed the patterns that this repo evaluates.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — same `context-file` pattern at a different domain (per-client business voice vs. per-product marketing context).
