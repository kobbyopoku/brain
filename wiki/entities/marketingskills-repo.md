---
type: entity
title: marketingskills (coreyhaines31/marketingskills)
entity_type: product
created: 2026-05-04
updated: 2026-05-04
website: https://github.com/coreyhaines31/marketingskills
aliases: [marketingskills, coreyhaines31/marketingskills]
tags: [claude-code-skills, marketing, open-source, skill-pack, free]
---

# marketingskills (coreyhaines31/marketingskills)

> Free, open-source Claude Code skill-pack by [[wiki/entities/corey-haines|Corey Haines]] containing 139 growth tactics, 12 SEO playbooks, and frameworks for copywriting, CRO, pricing, A/B testing, and AI SEO. The wiki's most substantive non-design [[claude-code-skills|claude-code-skills]] application — analogous to [[wiki/entities/refero|Refero]] but for marketing tactics rather than design tokens.

## Profile

The marketingskills repo packages everything an experienced marketer would know into markdown files an AI agent reads and executes. Its architectural pattern: every skill begins by reading `product-marketing-context.md` (ICP, personas, pain points, customer language, proof points) before any other action. This makes the repo's output product-aware in a way that generic prompts cannot match.

The repo claims to replace a $10,000/month marketing agency through proper application across the full marketing surface — copywriting, CRO, A/B testing, pricing, AI SEO, programmatic content. The execution chain: agent skill → tool registry → CLI → measurement.

## Key facts

- **Repo**: https://github.com/coreyhaines31/marketingskills
- **Maintainer**: [[wiki/entities/corey-haines]]
- **License**: free / open-source (per source).
- **Cost claim**: replaces $10,000/month marketing agency.
- **Inventory**:
  - **139 growth tactics** (the "growth idea library").
  - **12 programmatic SEO playbooks** (Templates / Curation / Comparisons / Examples / Locations / Personas / Integrations / Glossary / Translations / Directory / Profiles / Conversions).
  - **Frameworks**: copywriting, CRO (7-question framework), A/B testing (ICE scoring + hypothesis structure), pricing (3 axes), AI SEO (3 pillars), [[switching-forces]] (push/pull/habit/anxiety).
  - **Tool registry**: GA4, Google Search Console, Mixpanel, Amplitude, [[wiki/entities/posthog|PostHog]], Semrush, Ahrefs, HubSpot, Salesforce, [[wiki/entities/stripe|Stripe]], Mailchimp, Google Ads, Meta Ads, Hotjar, Optimizely — each with API/MCP/CLI/SDK availability noted.

## Architectural patterns

- **Context-first execution**: every skill reads `product-marketing-context.md` before doing anything else. *"Without this file the agent writes generic output. With it the agent knows your ICP, your objections, your proof points and your customer's exact words."*
- **Customer-language verbatim**: ICP language is pulled from real interviews, reviews, support tickets — not internal polished descriptions.
- **Skill-to-tool execution chain**: skill decides what to measure → tool registry finds the right tool → CLI runs the report.

## Positions and claims

- **Marketing has always been expensive because it required people who know what to do AND how to measure it. This repo packages both into agent-readable form.**
- **A page is a sequence of arguments, not a collection of blocks.** (CRO framing.)
- **100 strong pages beats 10,000 thin pages.** (Programmatic SEO framing.)
- **Add `/pricing.md` to your site.** AI buying agents will exclude pricing-hidden products from comparisons.

## Mentioned in

- [[wiki/sources/noisyb0y1-marketingskills-repo]] — canonical source describing the repo.

## Related entities

- [[wiki/entities/corey-haines]] — maintainer.
- [[wiki/entities/refero]] — sibling: design-tokens-as-skills. marketingskills is marketing-tactics-as-skills. Same shape, different domain.
- [[wiki/entities/posthog]], [[wiki/entities/stripe]] — referenced in the tool registry.
- [[wiki/entities/claude-code]] — the platform the repo builds on.

## Related concepts

- [[claude-code-skills]] — the mechanism this repo instantiates.
- [[switching-forces]] — codified as a skill.
- [[ai-seo]] — codified as a skill.
- [[markdown-as-agent-contract]] — meta-pattern.
- [[context-file]] — `product-marketing-context.md` is exactly this pattern, applied to product-marketing.
- [[landing-page-patterns]] — the repo's CRO 7-question framework is the evaluation companion.
