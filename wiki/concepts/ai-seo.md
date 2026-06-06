---
type: concept
title: AI SEO
created: 2026-05-04
updated: 2026-06-06
aliases: [generative engine optimization, GEO, AI search optimization, citation SEO]
tags: [seo, ai-search, content, marketing]
---

# AI SEO

> Optimizing content to be **cited** by AI overviews (Google's AI Overview, ChatGPT, Perplexity, Claude, Gemini, Copilot) — distinct from traditional SEO's goal of being *ranked* by Google search. AI systems can cite a well-structured page even if it's not in position 1, because they evaluate quality, structure, and relevance at the passage level rather than the page level.

## Definition

**AI SEO** (sometimes called Generative Engine Optimization or GEO) is the discipline of structuring content for citation by LLM-based answer systems rather than for ranking by traditional keyword-based search engines. Where traditional SEO targets *visibility in a result list*, AI SEO targets *inclusion in a generated answer* — a different mechanism with different success criteria.

The three pillars (per the [[wiki/entities/marketingskills-repo|marketingskills repo]]):

1. **Structure** — make content extractable. AI systems pull discrete passages, not full pages. Content organized into addressable blocks (definitions, step-by-steps, comparisons) gets cited more often than wall-of-text content with the same information.
2. **Authority** — make content citable. AI systems prefer sources with clear authorship, recent updates, schema markup, and traceable provenance. Anonymous, undated content is harder to cite confidently.
3. **Presence** — be where AI systems look. This includes appearing in their training data (where archived web crawls are sources), in their retrieval indexes (where current search results inform answers), and in machine-readable formats they prefer (`/llms.txt`, `/pricing.md`).

## Why it matters

The economics of organic traffic are shifting. Users increasingly get answers from AI overviews instead of clicking through to source pages. Traditional SEO success ("we're #1 for X") translates poorly to AI-mediated answers — being position 1 is no longer enough if the AI cites a different page that's better-structured.

For B2B SaaS specifically, the implication is more pointed: **buying agents are coming.** When an AI agent compares your product to a competitor on behalf of a user, it reads what's machine-readable and cites what's well-structured. A landing page that hides pricing behind "contact sales" may simply be excluded from the comparison. A FAQ that uses paragraphs of marketing copy may lose to a competitor's structured Q&A list.

For the wiki itself, AI SEO is also an interesting reflexive case: the wiki *is* a structured-passage knowledge base optimized for an LLM (the brain consumer) to cite. The same architectural principles that make pages citable by AI overviews make pages citable by an LLM agent reading the wiki. *AI SEO is to public web what the [[llm-wiki-pattern]] is to personal knowledge.*

## Treatment across sources

- [[wiki/sources/noisyb0y1-marketingskills-repo]] — canonical wiki source. *"Traditional SEO gets you ranked. AI SEO gets you cited by Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini and Copilot. AI systems can cite a well-structured page even if it's not in position 1 because they evaluate quality, structure and relevance of individual passages."*
- [[wiki/sources/bloggersarvesh-20-seo-prompts]] — *2026-05-09*. **Strongest prompt-pack source.** 20 detailed Claude prompts across 4 parts (GBP / Website / Backlinks+Authority / Content+Tracking) with 12-week roll-out plan. Adds four sub-patterns the wiki was missing:
  - **Entity optimization** (Prompt 18) — Google ranks *entities*, not just websites. Schema.org LocalBusiness JSON-LD + Wikidata + brand mentions strengthen the entity. *"This is the SEO work that compounds for years and almost no local business is doing it."*
  - **Page 2 keyword goldmine** (Prompt 12) — every keyword ranking position 11-20 with ≥100 impressions/month is one optimization push from page 1. The wiki's clearest *prioritization-by-existing-signal* methodology.
  - **Review sentiment analysis** (Prompt 13) — reverse-engineer competitor reviews to extract the **emotional language customers use**, then rewrite GBP/website copy in that customer voice. Voice-profile extension at the *customer* level (vs creator-voice).
  - **4-stage buyer-journey keyword mapping** (Prompt 16) — categorize every keyword into Problem-unaware / Problem-aware / Solution-aware / Ready-to-hire. *"Stage 4 keywords have lower volume but they convert at 5-10× the rate."*
- [[wiki/sources/bloggersarvesh-x-2032130279494853118]] — *thesis* sibling: $10K/mo SEO agency replacement using Cowork. Compose with the prompt-pack source as *thesis* + *arsenal*.
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] frames it from the **destination side**: if AI answer engines intercept discovery (the [[answer-engine-discovery]] shift), optimizing to appear inside those answers (AI SEO) matters, and the website's residual job changes from learn-about-you to conversion / trust-verification.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] frames it as a **platform-side cause**: states *"SEO is evolving into AI optimization"* as a sector implication — the supply-side driver of the practitioner-side shift the wiki already covers.

## Sub-claims and details

### Content block patterns that get cited

The marketingskills repo enumerates structured-block formats AI systems preferentially cite:

- **Definition blocks** for *"What is X?"* queries — short, declarative, schema-tagged definitions.
- **Step-by-step blocks** for *"How to X?"* queries — numbered ordered lists with explicit step boundaries.
- **Comparison tables** for *"X vs Y"* queries — side-by-side structured tables with consistent column semantics.
- **Pros/cons blocks** for evaluation queries — explicit `Pros:` / `Cons:` headed lists.
- **FAQ blocks** for natural language questions — Q/A structure with `<dt>/<dd>` semantics or schema FAQPage markup.
- **Statistic blocks** with cited sources — claim + number + source link, quotable as a single unit.

### Machine-readable endpoints

The most underrated AI SEO move per the source: **add `/pricing.md` or `/pricing.txt`** to your site. *"If pricing is hidden behind JavaScript or 'contact sales' an AI agent may simply exclude your product from a comparison."* Same logic for:

- `/llms.txt` — machine-readable summary of what the site is, key resources, content licensing.
- `/pricing.md` — structured pricing table.
- `/changelog.md` — public update log (see Public Changelogs in the marketingskills 139 tactics).
- Schema markup for `Product`, `Service`, `Article`, `FAQPage`, `HowTo`.

### Authority signals AI systems weigh

- **Author attribution** with verifiable identity (`<meta name="author">`, schema `Person`, links to author page).
- **Last-updated dates** in HTML and schema (`dateModified`).
- **Source citations** for claims (especially statistics).
- **Inbound links** from authoritative domains (still matter; AI retrieval often piggybacks on existing search-index signals).
- **Brand recognition** — being mentioned by name across many sources increases citation probability even when the source page itself isn't cited.

### What AI SEO does NOT replace

Traditional SEO still matters because:
- AI answers cite *some* sources — usually the same handful — and traditional ranking signals influence which sources get crawled and indexed.
- Many users still click through to the cited sources for verification or deeper reading.
- AI systems train on web archives that traditional SEO populated.

The right framing: **AI SEO is additive to traditional SEO**, not a replacement. Same content, structured for both audiences (humans skimming and machines extracting).

## Open questions and contradictions

- **Citation algorithms are opaque and changing.** Each AI system (Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, Copilot) uses different retrieval and citation logic; what works in May 2026 may not work in November.
- **Gaming the system**: as AI SEO becomes practiced discipline, AI systems will adapt to penalize obvious optimization (the same arc traditional SEO went through). Definition-block stuffing is plausible 2027 spam.
- **Authority concentration**: AI systems disproportionately cite a small number of high-authority sources (Wikipedia, established publications, well-ranked SaaS brands). Newer entrants face a citation cold-start problem.
- **AI-only content** (sites optimized for citation but not for human reading) creates SEO-versus-UX tradeoffs the marketingskills source doesn't engage with. The discipline of writing once for both audiences is real work.
- **Buying agents are speculative as of 2026.** Saraev's [[wiki/sources/saraev-agentic-workflows-2026|definitive guide]] mentions agents calling other agents, but production-grade buying agents that read `/pricing.md` to make purchase decisions are rare. The pattern's value compounds if/when this becomes common.

## Related concepts

- [[landing-page-patterns]] — well-structured landing pages naturally rank well for AI SEO (the patterns overlap with structure-extractability).
- [[switching-forces]] — content optimized for AI citation should answer Push/Anxiety queries that surface in AI search ("how do I stop X"), not just Pull queries.
- [[markdown-as-agent-contract]] — `/pricing.md`, `/llms.txt`, and similar files are this meta-pattern applied to public-web buying-agent surfaces.
- [[claude-code-skills]] — the marketingskills repo packages AI SEO as an executable Claude skill.
- [[llm-wiki-pattern]] — adjacent: the wiki itself is structured for LLM citation, applying the same principles to personal knowledge.

## Related entities

- [[wiki/entities/marketingskills-repo]] — codifies AI SEO as a Claude skill.
- [[wiki/entities/corey-haines]] — repo author.

## Mentioned in

- [[wiki/sources/noisyb0y1-marketingskills-repo]]
- [[wiki/sources/bloggersarvesh-x-2032130279494853118]] — Cowork-for-SEO agency replacement thesis.
- [[wiki/sources/bloggersarvesh-20-seo-prompts]] — 20-prompt arsenal across GBP / Website / Backlinks / Content+Tracking.
- [[wiki/sources/exploraX_-google-maps-leadgen]] — adjacent (review automation as one of 3 productized small-business offers).
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] — destination-side framing of the answer-engine shift.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — *"SEO is evolving into AI optimization"* as a 2026 roadmap implication.
