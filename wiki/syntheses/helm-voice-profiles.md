---
type: synthesis
title: Helm Voice Profiles (Starter Drafts) — Vedge / Kivora / Clarvyn / ROAM Labs
created: 2026-05-09
updated: 2026-05-09
aliases: [helm-voice-profiles, voice-profiles-roam-labs, marketing-agent-voice-profiles]
tags: [synthesis, voice-profile, helm, marketing-agent, configuration, starter-draft]
---

# Helm Voice Profiles — Starter Drafts (Vedge / Kivora / Clarvyn / ROAM Labs)

> **Configuration artifact** for the Marketing agent in [[wiki/projects/helm|Helm]]. Four voice profiles extracted via the [[wiki/sources/shannholmberg-content-os|Shann Holmberg brand-foundation-extraction]] methodology applied to each product's landing-site content. **Starter quality** — extraction sources are *whatever already exists on disk* (intentional brand surfaces, but not 20 curated best pieces per product). Refine when curated samples are available. Migrate to `helm-repo/voice-profiles/<product>.md` when the Helm repo exists; until then, these live in the brain as the canonical reference.

## Scope and quality caveat

| Product | Source content read | Sample volume | Confidence |
|---|---|---|---|
| **Vedge** | `vedge_landing/app/page.tsx` (homepage hero + 4 numbered features) | ~600 words | **High** — distinctive editorial voice; landing copy is intentional and consistent |
| **Kivora (ROAM GRC)** | `Kivora/landing/src/components/home/HeroSection.tsx` + `WhyKivoraSection.tsx` + `BentoSection.tsx` + `AISection.tsx` | ~500 words | **High** — B2B SaaS voice is clear and consistent across sections |
| **Clarvyn** | `clarvyn/landing/src/pages/StartupLanding.tsx` (hero + features + stats) | ~400 words | **Medium** — startup-founder positioning is sharp on the Startup landing; Enterprise landing has different voice (not extracted here) |
| **ROAM Labs corp** | `roam/app/page.js` (hero + capabilities + metrics) | ~400 words | **Low** — voice is currently unsettled per [[wiki/projects/roamlabs]]; both editorial-quarterly and mission-control visual directions reverted on 2026-05-09. Profile reflects placeholder pre-revert state. **Re-extract when visual direction settles.** |

**Methodology** (per Shann Holmberg's verbatim *brand-foundation-extraction* prompt + CyrilXBT's *feed-20-pieces, extract-patterns* approach):

1. Read representative landing-site copy.
2. Note: average sentence length, capitalization habits, vocabulary register, structural tendencies, frequent phrases, banned patterns.
3. Capture 2-3 reference lines that exemplify the voice at its sharpest.
4. Output structured `# Voice profile` markdown that can be installed in the Marketing agent's per-product system prompt.

## Vedge voice profile

### What Vedge sounds like

- **Cadence**: editorial / quarterly-magazine, with occasional italic-display flourish for emphasis. Sentence rhythm alternates short declarative + longer technical explanation.
- **Average sentence length**: 14-22 words, deliberately varied.
- **Capitalization**: title-case for product surfaces (*"MAR · Medication Administration"*, *"Levey-Jennings QC"*, *"Pharmacy POS"*); sentence-case for body copy.
- **Vocabulary register**: clinical-technical with plainspoken anchors. NHIS, MAR, HL7 Lab Interfaces, Reagent Lot Tracking — but explained in terms operations people use, not consultants.
- **Structural tendencies**: numbered ordinal feature blocks (`01 / 02 / 03 / 04`); each feature is a *promise + operational specificity* pairing.
- **Frequent phrases**: *"the way Africa actually works"*, *"across Africa"*, *"load-shedding aware"*, *"insurers your patients carry"*, *"every facility type"*.
- **Geographic identity**: African-specific framing throughout. Edition metadata (*"Ed. 01 · Accra"*). Currency in cedis (₵). Operational realities specific to the market (load-shedding, generator failover, NHIS).
- **Tone**: anti-corporate, plainspoken, honest about the operational pain (*"no three-week reconciliation month-end headache"*).
- **Button text**: lowercase + minimal (*"Start free"*, *"See pricing"*, *"or book a demo →"* with trailing arrow).

### What Vedge never sounds like

- No *"revolutionary"*, *"groundbreaking"*, *"game-changing"*, *"transform"*.
- No *"AI-powered"* — say *"with Claude"* or *"with the AI assist module"*.
- No exclamation marks in product copy.
- No *"in today's fast-paced world"* or other generic openers.
- No emoji in marketing copy. (Emoji only in the staff-app chat.)
- No competitor names referenced directly.
- No US-centric framing or examples.
- No abstract claims without operational specificity. *"Reduces admin burden"* is wrong; *"No three-week reconciliation month-end headache"* is right.
- No corporate throat-clear: *"we believe"*, *"we're excited to"*, *"we're proud to"*.
- No *"industry-leading"*, *"best-in-class"*.

### Reference samples (the voice at its sharpest)

> *"A health operating system built for the way Africa actually works."*

> *"Load-shedding aware. Sync-to-cloud when power returns. Offline charting on the wards. Printable fall-back for every chart if the generator dies."*

> *"NHIS, private insurers, corporate health plans, community schemes — Vedge captures claims during the visit and submits them in the format each provider expects. No three-week reconciliation month-end headache."*

> *"Pricing that respects an African P&L. Free base tiers for every lab and every pharmacy in Africa. Hospitals start at ₵1,200/month."*

---

## Kivora (ROAM GRC) voice profile

### What Kivora sounds like

- **Cadence**: concise, declarative, B2B-confident. Headlines often pair two short phrases for rhythm.
- **Average sentence length**: 10-18 words. Headlines shorter (5-8 words).
- **Headline form**: tagline pairs — *"Compliance on autopilot. Risk under control."* Two related declaratives split across a `<br>`.
- **Kicker style**: wide-letter-spaced uppercase: *"Governance · Risk · Compliance"*, *"Why Kivora"*.
- **Vocabulary register**: domain-specific GRC. Control / framework / vendor / risk / compliance posture / evidence coverage / remediation / control IDs (*"CC7.2 — Access review overdue"*).
- **Numerical specificity**: percentages (94%), control counts (142/148), ratios. *Every claim has a number where one exists.*
- **AI presented as concrete actor**: not *"AI-powered automation"* but *"Kivora AI understands your compliance context. It maps controls, suggests remediation, ..."* — verb-leading.
- **Pricing transparency upfront**: *"Starting at $299/mo"* is in the hero. No "contact sales" gating for entry tier.
- **Frequent phrases**: *"on autopilot"*, *"under control"*, *"unified in one platform"*, *"AI-powered"* (current hero adjective for the platform), *"compliance posture"*.
- **Anti-marketing inversions**: *"AI that actually helps. Not just a chatbot."* — explicit category-distancing.
- **Sentence rhythm**: *outcome → mechanism → proof*. Outcome stated, mechanism explained, proof quantified.

### What Kivora never sounds like

- No vague promises: *"transform your business"*, *"unlock potential"*, *"empower your team"*.
- No exclamation marks.
- No emoji in marketing copy.
- No competitor names directly.
- No fear-mongering: *"avoid massive fines!"*, *"don't get breached"*.
- No customer-success-y language: *"delight"*, *"wow"*, *"thrilled to..."*.
- No filler superlatives: *"most advanced"*, *"world-class"*, *"cutting-edge"*.
- No claim without a number when a number is available.
- No throat-clearing: *"in today's compliance landscape"*, *"as organizations face..."*.

> **Note on "AI-powered" vs "AI-native"**: the current Kivora landing hero uses *"AI-powered governance, risk, compliance..."* (cited below as a reference sample). Earlier drafts of this voice profile banned *"AI-powered"* in favor of *"AI-native"* — that was prescriptive (what we wished it sounded like), not descriptive (what it actually sounds like). **The voice profile is descriptive**: it captures Kivora's voice as it currently is, not a future-state aspiration. If Godwin decides to migrate Kivora copy to *"AI-native"*, that's a separate **voice migration** action — file it as a refresh of this profile, not as a banned-pattern in the descriptive extraction.

### Reference samples (the voice at its sharpest)

> *"Compliance on autopilot. Risk under control."*

> *"AI-powered governance, risk, compliance, and vendor trust management — unified in one platform. Starting at $299/mo."*

> *"AI that actually helps. Not just a chatbot. Kivora AI understands your compliance context. It maps controls, suggests remediation, ..."*

> *"3 controls need attention. CC7.2 — Access review overdue. Recommended: auto-assign to J. Chen."*

---

## Clarvyn voice profile

### What Clarvyn sounds like

- **Cadence**: anti-category positioning. Massive declarative headlines. Short split-rhythm follow-up sentences.
- **Average sentence length**: 6-14 words. Punchy. Frequently fragmentary for effect.
- **Headline form**: inverted positioning — *"Your Startup / Doesn't Need HR"* (anti-category framing in the hero itself).
- **Audience direct address**: second-person, founders-specifically. *"Your startup"*, *"Focus on building"*, *"We handle the people ops"*.
- **Anti-tool framing**: agent IS the department, not a tool for the department. *"AI agent that handles recruiting, payroll, compliance, and culture"* — agent as direct replacement, not assistant.
- **Stats with personality**: pulse-style — *"95% No HR Needed"*, *"100% Compliance"*, *"0 Manual Entry"*. Numbers + descriptor labels.
- **Conclusive declaratives**: *"Set it once. Salaries, taxes, and compliance handled forever."* — period-then-period rhythm.
- **Capability lines + personality kicker**: *"Source, screen, and schedule candidates automatically. Your AI never sleeps."*
- **Trust signal**: named real startups (Stripe, Vercel, Linear, Notion, Figma, Slack) — peer-association rather than enterprise logos.
- **Visual signature in copy**: gradients in headlines, sparkles iconography, indigo/violet palette. Copy *follows the same energy* — bright, declarative, modern.
- **Vocabulary register**: founders, ops, autopilot, automated, recruiting agent, payroll, compliance, culture, sentiment, pulse surveys.

### What Clarvyn never sounds like

- No HR-industry jargon: *"synergies"*, *"talent acquisition"*, *"human capital management"*, *"workforce optimization"*.
- No corporate-template tropes: *"transform your workforce"*, *"empower your people"*.
- No *"AI-powered"* — say *"AI agent"* or *"AI-native"*.
- No hedged language: *"potentially"*, *"may help"*, *"designed to"*, *"can assist with"*.
- No emoji in marketing copy.
- No competitor naming.
- No traditional-HR concessions: *"we work alongside your HR team"*, *"complement your HR function"*. Clarvyn replaces HR; it doesn't augment HR.
- No *"as a service"* suffixes: just *"AI agent"*, not *"HR-as-a-service"*.
- No three-syllable abstract nouns where a concrete word works: *"engagement"* is fine; *"team-member-experience-optimization"* is not.
- No *"Powered by Claude"* on the marketing surface — Claude is implementation detail; Clarvyn is the brand.

### Reference samples (the voice at its sharpest)

> *"Your Startup / Doesn't Need HR"*

> *"An AI agent that handles recruiting, payroll, compliance, and culture. Focus on building. We handle the people ops."*

> *"Set it once. Salaries, taxes, and compliance handled forever."*

> *"Source, screen, and schedule candidates automatically. Your AI never sleeps."*

> *"95% No HR Needed. 100% Compliance. 0 Manual Entry."*

---

## ROAM Labs corp voice profile *(unsettled — provisional)*

### ⚠️ Stability flag

The current `/Users/kobbyopoku/ROAM/CascadeProjects/roam/` site is in flux per the [[wiki/projects/roamlabs|_roamlabs project page]]: two visual directions (editorial-quarterly with Instrument Serif + cream/oxblood, and mission-control with Bricolage Grotesque + warm-black/lime) were both prototyped end-to-end and reverted on 2026-05-09. The shipped surface is the *placeholder pre-revert state*. **This voice profile reflects the placeholder, not the eventual brand voice.** Re-extract when the visual direction settles.

The Marketing agent should treat the ROAM Labs corp profile as **draft-only** and route any ROAM Labs corporate content through Godwin for review (not auto-send) until the brand stabilizes.

### What ROAM Labs sounds like (current placeholder)

- **Cadence**: enterprise B2B / AI-agency. Capability-list driven.
- **Headline typography signature**: monospace + underscore prefix — *"_intelligent systems that {animate}"*. The underscore reads as a terminal-prompt or filename signature.
- **Vocabulary register**: enterprise procurement vocabulary. *"Sub-second response times"*, *"bank-grade encryption"*, *"SOC 2 Type II Certified"*, *"GDPR Compliant"*, *"99.9% Uptime SLA"*.
- **Outcome metrics with magnitude**: *"85% reduction in manual tasks"*, *"3.2x faster processing"*, *"$2.4M avg. annual savings"*, *"99.9% system uptime"*. Big numbers paired with descriptor labels.
- **Capability-list framing**: *"Autonomous AI Agents"*, *"Workflow Orchestration"*, *"Custom AI Development"*, *"Predictive Analytics"*, *"Enterprise Security"*, *"Real-time Processing"*. Title-case noun phrases.
- **Trust signal triad** in hero: *"SOC 2 Type II Certified · GDPR Compliant · 99.9% Uptime SLA"* — three short claims separated by middle-dots.
- **Voice**: third-person-plural ("We design and deploy AI agents that automate..."). Formal-corporate.

### What ROAM Labs *should not* sound like (current drift to fix when re-extracted)

The current site contains tropes the eventual voice should avoid. Flagged as **anti-patterns to fix** rather than canonical voice rules:

- **Generic fictional client names**: *"TechCorp, FinanceHub, DataStream, CloudNine, ScaleUp, InnovateCo"* — these are placeholder company names. Replace with real testimonials when shipped, or remove the section entirely.
- **Vague enterprise tropes**: *"transform"*, *"unlock"*, *"empower"*, *"synergies"*, *"streamline"*.
- **Superlatives without specificity**: *"best-in-class"*, *"industry-leading"*, *"cutting-edge"*, *"world-class"*.
- **Generic opener**: *"in today's rapidly evolving"*, *"as organizations face..."*.
- **Exclamation marks** in marketing copy.
- **Emoji** in marketing copy.
- **AI-powered**: be specific about the AI capability instead.
- **Powered by Claude** on the public marketing surface — Claude is implementation detail; ROAM Labs is the brand.

### Reference samples (currently strongest lines)

> *"_intelligent systems that {animate verb}"* — the typography signature is more distinctive than the words; the structure should survive revisions.

> *"We design and deploy AI agents that automate complex workflows, make intelligent decisions, and scale with your business."*

> *"85% reduction in manual tasks. 3.2x faster processing time. 99.9% system uptime."*

### Re-extraction priority

The ROAM Labs corp voice should be re-extracted **before** the Marketing agent ships content to ROAM Labs corporate channels. Practically: Helm Week 3 builds the Marketing agent with the three product profiles (Vedge / Kivora / Clarvyn) loaded; ROAM Labs corp content stays manual until the voice settles. Once the brand settles, swap in a finalized profile.

---

## Composition with Helm

These four profiles are intended to live at `helm-repo/voice-profiles/` once the Helm repo exists:

```
helm-repo/
├── voice-profiles/
│   ├── vedge.md           ← extracted from this synthesis
│   ├── kivora.md          ← extracted from this synthesis
│   ├── clarvyn.md         ← extracted from this synthesis
│   └── roam-labs-corp.md  ← extracted; flagged as draft-only
└── ...
```

The Marketing agent's per-product system prompt loads the relevant voice-profile.md before drafting. Per [[wiki/sources/shannholmberg-content-os|Shann's Content OS]] discipline: **the voice profile loads, the master avoid-slop document loads, then the writer model drafts**. The voice file is small (300-500 tokens) — well under the [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax 1,500-token CLAUDE.md cap]].

## How to refine these profiles when better samples are available

The right move when Godwin has 20 curated best pieces per product:

1. Identify the 20 strongest pieces per product (sales decks, customer emails, blog posts, README files, deck slides, testimonials Godwin has written).
2. Concatenate them into a single text file per product.
3. Re-run the same brand-foundation-extraction methodology against the larger sample set.
4. Diff the new profile against this starter draft. Promote what survives; revise what doesn't; flag what changed.
5. Update this synthesis page with the refined profiles + a refresh-log entry.

## Composition with the brain

- [[wiki/sources/shannholmberg-content-os]] — methodology source (verbatim brand-foundation-extraction prompt + master avoid-slop document concept).
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — independent corroboration of the *"feed 20 best pieces, extract patterns"* methodology.
- [[wiki/sources/bloggersarvesh-20-seo-prompts]] — adjacent (Sarvesh's review-sentiment-analysis prompt extracts customer-voice; this synthesis extracts brand-voice).
- [[wiki/concepts/anti-ai-slop-machinery]] — the avoid-slop discipline that Marketing agent should layer on top of these voice profiles.
- [[wiki/concepts/markdown-as-agent-contract]] — voice profiles are markdown agent contracts at the per-product / per-task scope.
- [[wiki/projects/helm]] — the project these profiles configure.

## Mentioned projects

- [[wiki/projects/vedge]] — source of Vedge voice samples.
- [[wiki/projects/kivora]] — source of Kivora voice samples.
- [[wiki/projects/clarvyn]] — source of Clarvyn voice samples.
- [[wiki/projects/roamlabs]] — source of ROAM Labs corp voice samples (currently unsettled).
- [[wiki/projects/helm]] — Marketing agent will consume these profiles in Week 3.
