---
type: concept
title: Horizontal Leverage
created: 2026-05-03
updated: 2026-05-03
aliases: [horizontal automation leverage, automate-90-of-many]
tags: [ai-automation, economics, foundational]
---

# Horizontal Leverage

> The economic argument that automating **90% of many people's roles** is orders of magnitude more valuable than automating **100% of one person's role**. Because most of the wealth captured from AI agents at scale will go to operators who think horizontally, not vertically.

## Definition

**Horizontal leverage** is the principle that AI automation's economic value compounds across the breadth of roles it touches, not the depth of any single role. Concretely: an automation that takes over 90% of the repeatable work for 10,000 knowledge workers creates ~9,000 units of economic value. An automation that fully replaces one specialized worker creates ~1 unit. The math favors breadth.

The implication for builders: don't optimize for replacing the hardest job; optimize for replacing the most common 80% of many jobs. The 80/20 rule applied to labor markets.

## Why it matters

Most AI-automation discussions frame the question as *"can AI replace this job?"* — a vertical, depth-first framing. Saraev's framing inverts this: *"how much of this kind of work, across how many people, can AI partially automate?"* The horizontal question has a much larger answer.

This reframes who captures the wealth from AI:
- **Vertical operators** (replacing one job at a time, fully) are essentially staffing agencies with AI. Limited scaling.
- **Horizontal operators** (taking 90% of a category of work across many companies) are infrastructure providers. Compounding scaling.

For [[ai-automation-services|AI automation services]] businesses, horizontal leverage is the architectural choice that determines TAM. A bookkeeping-automation tool that does 90% of monthly close for 10,000 small businesses is a $X00M company; one that fully replaces one bookkeeper is a $50K consultancy.

## Treatment across sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — canonical wiki source. *"Automating 100% of one person's role is equivalent to basically providing one unit of economic value. Whereas, if you automate 90% of 10,000 people's, you're providing 9,000 units of economic value. ... I call this horizontal leverage and it's very, very strong."*
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — implicit corroboration. ColdIQ's services-as-software model captures horizontal leverage by template-izing per-niche workflows so each new client adds incremental cost, not full re-build.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — implicit corroboration via niche selection. Khairallah's "pick one niche and build the same 5 automations for everyone in it" is the horizontal-leverage strategy at the early-stage scale.

## Sub-claims and details

### The math

Let *N* be the number of people whose work the automation touches, and *p* be the percentage of each person's role automated. Total economic value created ≈ *N × p*.

| Strategy | N | p | Total |
|---|---:|---:|---:|
| Vertical (replace one specialist) | 1 | 100% | 1 |
| Vertical (replace ten specialists) | 10 | 100% | 10 |
| Horizontal (90% of 1,000 roles) | 1,000 | 90% | 900 |
| Horizontal (90% of 10,000 roles) | 10,000 | 90% | 9,000 |
| Horizontal (50% of 100,000 roles) | 100,000 | 50% | 50,000 |

The horizontal column dominates. Even partial coverage of large populations beats full coverage of small ones.

### Why this works for AI specifically
- **Marginal cost is near-zero.** Once a workflow is built, the 10,001st user costs the same as the 1st.
- **Generalization is cheap.** A bookkeeping workflow built for one small business needs minor parameterization to serve another. A specialized AI for a single role needs deep customization.
- **Distribution economies.** Horizontal automations can be sold via marketplaces, plugins, integrations — channels that don't exist for vertical replacements.

### Implications for builders
- **Pick wide categories of work**, not specialized roles. Bookkeeping, CRM data entry, customer support tier-1, content drafting, lead enrichment, scheduling.
- **Don't try to make the AI a "perfect" knowledge worker.** Make it a "good enough for 90%" of the cases that occur in 80% of the businesses.
- **Build on horizontal infrastructure.** Stripe (payments), Twilio (SMS), Sendgrid (email), Notion (docs) all captured horizontal leverage in their categories. AI automation has the same shape.

### Industrial revolution analogy
Saraev's framing: *"Back in the good old days, [the industrial revolution] didn't replace one craftsman with one factory worker — it took 90% of the work from a million craftsmen and pushed it into machines."* The wealth was created by the people who built the machines, not by the people who continued making things by hand.

The same dynamic is unfolding now with knowledge work. The horizontal-leverage operators are the new factory builders.

## Open questions and contradictions

- **The 90% boundary is empirical, not theoretical.** Why 90% specifically? Because that's where most current LLM-based automations cap out (the last 10% requires judgment). When models improve, this number moves; when they don't, it constrains the achievable leverage.
- **Quality vs quantity tradeoff**: 90% of a high-stakes role (medical diagnosis, legal contract review) is worse than 0% — partial automation introduces errors humans wouldn't make. Horizontal leverage is only safe in low-stakes domains. Healthcare and finance are exceptions where partial automation needs much higher reliability.
- **The wealth-transfer claim is normative as much as descriptive.** Saraev frames this as fait-accompli; whether actual wealth flows this way depends on regulation, antitrust, distribution access, and other factors his framing doesn't engage with.
- **Race-to-the-bottom risk**: if 100 operators all build the same horizontal automation, the price collapses. Horizontal leverage at scale requires moats — proprietary data, distribution lock-in, integration depth.

## Related concepts

- [[ai-automation-services]] — the business model that captures horizontal leverage.
- [[services-as-software]] — Vacca's specific framing for horizontal-leverage delivery.
- [[do-framework]] — the architectural pattern that makes horizontal automation reliable enough to monetize.
- [[reliability-decay-math]] — the technical constraint that bounds *p* (the per-role automation %).
- [[online-business-models-2026]] — places horizontal AI services as one of 10 viable models.
- [[reasoning-execution-split]] — adjacent: separating reasoning from execution is what enables 90% automation without full replacement.

## Related entities

- [[wiki/entities/nick-saraev]] — author of the canonical articulation.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]
