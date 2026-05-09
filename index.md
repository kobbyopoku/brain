# index.md — Wiki catalog

The content-oriented index of this wiki. Read this first when answering a query, then drill into the linked pages. See [[CLAUDE]] for conventions and [[log]] for the chronological record of operations.

**Stats**: 90 sources · 300 entities · 48 concepts · 9 projects · 3 syntheses · last updated 2026-05-09

**Raw layout**: every design system lives at `raw/<brand>/DESIGN.md` (Refero) or `raw/open-design/design-systems/<brand>/DESIGN.md` (Open Design). 172 DESIGN.md files in this canonical folder layout. See [[wiki/sources/design-systems-master-index]] for the complete brand → path lookup.

---

## Sources

### LLM Wiki / pattern

- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's pattern for LLM-maintained personal knowledge bases; foundational for this vault.

### Claude Code / agent tooling

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — six-layer Claude Code stack (CLAUDE.md → memory → skills → subagents → hooks → orchestration); first wild citation of Karpathy's LLM Wiki.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — full course on building an AI agent from scratch; foundational for [[agentic-loop]], [[augmented-llm]], [[agent-workflow-patterns]], [[beginner-agent-types]].
- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — 10 open-source repos that replace each role of an engineering team.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — full AI OS playbook from a $3M/yr business; **second wild citation of Karpathy's LLM Wiki**; introduces [[hot-cache]].
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — instrumented 90-day study; 73% of tokens go to 9 named overhead patterns; ships an audit script.
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — architectural deep-dive on Anthropic Agent Skills; canonical for [[progressive-disclosure]] and [[reasoning-execution-split]].
- [[wiki/sources/HeyZaraKhan-anthropic-skills-announcement]] — secondary citation of Anthropic Skills as the "programmable, reusable AI systems" shift.
- [[wiki/sources/HeyZaraKhan-claude-certified-architect]] — resource list for the Claude Certified Architect program.

### AI services / business models

- [[wiki/sources/khairallah-ai-automations-10k-month]] — six-phase early-stage playbook for selling AI automations at $3-15k per build.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — scaled $7M ARR services-as-software agency playbook with explicit churn-at-scale math.
- [[wiki/sources/realbrianmoran-making-money-online-2026]] — 10 online business models that work in 2026 + 1 that's collapsing.
- [[wiki/sources/saraev-agentic-workflows-2026]] — 5h+ definitive course; coins the DO framework (now DOE in later content), horizontal-leverage thesis, reliability-decay-math. The architectural companion to the three economic playbooks above.
- [[wiki/sources/prakash-bhandari-doe-framework]] — cleanest 3-layer DOE framing (Directive + Orchestration + Execution); adds the *Act → Observe → Think → Act* runtime loop.
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]] — derivative LinkedIn post that surfaced DOE for this wiki; introduces the term *self-annealing*.
- [[wiki/sources/heynavtoor-10k-claude-automation-business-90-days]] — 5th source on the AI automation services model; functionally a derivative of Khairallah with new niche (law firms), Cowork as Claude Code alternative, three-trap framing.

### Prompts and prompt-engineering

- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — 20 detailed Claude prompts across deep research, writing, career, daily life, learning.
- [[wiki/sources/godofprompt-paul-graham-startup-prompts]] — 6 Paul Graham-style startup-evaluation prompts.

### Design systems / UI

- [[wiki/sources/refero-design-systems-for-ai-agents]] — Refero's curated DESIGN.md catalog for AI coding agents; landing-page clipping.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — 11 patterns shared by 8 YC unicorn landing pages.

### Marketing / CRO / SEO

- [[wiki/sources/noisyb0y1-marketingskills-repo]] — surfaces [[wiki/entities/marketingskills-repo|coreyhaines31/marketingskills]]: a free Claude Code skill-pack with 139 growth tactics, 12 SEO playbooks, CRO/A/B/pricing/AI-SEO frameworks, and a 16-tool tool registry.

### AI design tooling (open-source platforms)

- [[wiki/sources/nexu-io-open-design]] — Apache-2.0 open-source alternative to Anthropic's [[wiki/entities/claude-design|Claude Design]]. 138 design systems with a 9-section schema, 64 SKILL.md bundles, 15 auto-detected agent CLIs, BYOK proxy, sandboxed preview, MCP server. The most architecturally substantive design-tooling source in the wiki.
- [[wiki/sources/open-design-catalog]] — companion catalog source. Full inventory of all 139 design systems (live count) across 20 categories + 71 skills + 9 craft discipline docs. All raw content (227 markdown files, 2.5MB) fetched into `raw/open-design/`.
- [[wiki/sources/design-systems-master-index]] — canonical lookup table for **all 172 DESIGN.md files** in the brain (33 Refero + 139 Open Design). One row per brand with absolute path. Use this to find any specific brand's design tokens.

### Open-source autonomous agents

- [[wiki/sources/nousresearch-hermes-agent]] — MIT-licensed self-improving multi-platform AI agent by [[wiki/entities/nous-research|Nous Research]]. Built-in learning loop (creates skills from experience, persists across sessions, builds user model). Multi-platform messaging gateway (Telegram + Discord + Slack + WhatsApp + Signal + Email + CLI). Model-agnostic (200+ models via [[wiki/entities/openrouter|OpenRouter]] + Nous Portal + AWS Bedrock + others). 23k+ stars.

### X-thread batch ingest (2026-05-08 — 17 posts queued from mobile share; 5 substantive + 12 URL-only stubs)

Mobile-share clipping produces URL-only stubs (X.com returns HTTP 402 to bot fetches). Substantive ingest possible only where aggregator coverage exists (Simon Willison, blog posts, prior author content). Re-clip via Obsidian Web Clipper desktop to recover bodies for the URL-only stubs.

**Substantive (5)**:
- [[wiki/sources/trq212-x-html-effectiveness]] — Thariq Shihipar (Anthropic Claude Code lead): *"The Unreasonable Effectiveness of HTML"* — HTML beats Markdown as agent output format. Reconstructed via Simon Willison's blog. Strongest first-party Anthropic argument for [[artifact-first-workflow]] yet ingested.
- [[wiki/sources/_avichawla-x-2052326975034048754]], [[wiki/sources/_avichawla-x-2053049489963811135]] — two Avi Chawla threads (DS/ML educator at Daily Dose of DS).
- [[wiki/sources/bloggersarvesh-x-2032130279494853118]] — Sarvesh Shrivastava on Claude Cowork for SEO ($10K/mo agency replacement).
- [[wiki/sources/kylejeong-x-2052103973377867913]] — Kyle Jeong on Browserbase web-agent infrastructure.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — Khairallah's three-session Cowork daily architecture (Morning Briefing 7AM / Midday Production / End-of-Day Wrap-up 5PM). **Body upgraded 2026-05-09 from Web Clipper.**

**URL-only stubs (12)**:
- [[wiki/sources/itsalexvacca-x-2052740083820958072]] — Alex Vacca (existing-author follow-up)
- [[wiki/sources/noisyb0y1-x-2044692412061425748]] — noisyb0y1 (existing-author earlier post)
- [[wiki/sources/cyrilxbt-x-2052235121416188114]] — CyrilXBT 3K likes (highest-engagement of 3 queued)
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — CyrilXBT 377 likes
- [[wiki/sources/cyrilxbt-x-2052923836090167526]] — CyrilXBT 205 likes
- [[wiki/sources/jaynitx-x-2052734499319091384]] — Jaynit 2K likes
- [[wiki/sources/zodchiii-x-2052368125480354000]] — darkzodchi 1K likes
- [[wiki/sources/rohit4verse-x-2050968031493550202]] — Rohit 555 likes
- [[wiki/sources/ashwingop-x-2052777467732283817]] — Ashwin Gopinath 361 likes
- [[wiki/sources/creatorpascal-x-2053034511726756159]] — Pascal (creatorpascal) 134 likes
- [[wiki/sources/neil_xbt-x-2052733885906051118]] — NeilXbt 79 likes

### Web-Clipper batch ingest (2026-05-09 — 7 substantive bodies; 5 new + 2 upgrades)

Full Web-Clipper desktop captures with verbatim bodies (vs the URL-only mobile-share stubs from 2026-05-08). Each is 10-22KB of substantive content.

**New (5)**:
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — *"You're doing RAG wrong."* The chunk is the structural bug, not retrieval algorithm tuning. IdeaBlock alternative: question + validated answer + typed governance fields. Blockify benchmark: 2.29× retrieval-distance reduction, 13.55% vector-accuracy improvement after dedup, 40× corpus compression. Major refresh to [[retrieval-augmented-generation]].
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — 21 specific CLAUDE.md instructions across 5 parts (how Claude talks / behaves / context / memory / for developers); closes with Karpathy's viral 4 rules + 65→94% coding-accuracy claim. Strongest checklist articulation of the [[markdown-as-agent-contract]] meta-pattern.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — Guri Singh's Cowork onboarding guide. Folder structure (`ABOUT ME/` + `PROJECTS/` + `TEMPLATES/` + `CLAUDE OUTPUTS/`). Paste-ready Global Instructions. AskUserQuestion as most-transformative feature. 11 official Anthropic plugins. Substantial upgrade to [[cowork]].
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — 7-step tool-calling reliability roadmap: Protocol / Tool definitions / Error handling / Parallelization / Catalog size / Security / Evaluation. *"Reliable agents treat the model as a reasoning engine — not an execution engine."* Strongest tool-layer reliability articulation in the wiki.
- [[wiki/sources/ig_claims-x-meta-retargeting]] — Zack's 5-stage conviction-layered Meta retargeting funnel for service businesses. Conviction Gap Model (10/100 → 85-90/100). Specific metrics: $43 cold CPL → $12 retargeting CPC; 4.2× conversion rate.

**Body upgrades (2)**:
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — 5-agents-replace-5-employees. **Now verbatim** with full system prompts for all 5 agents (Research / Content / Communication / Operations / Analytics), master CLAUDE.md template, cost breakdown ($105/mo = Claude Max $100 + N8N $5 + Supabase free + Obsidian free), and 6-week build order.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — three-session Cowork daily architecture. **Rewrite** of earlier author-context-only stub now that the verbatim body is captured. 7AM Morning Briefing + Midday Production Block + 5PM End-of-Day Wrap-up; 4-tier email urgency system; 15-min Friday refinement loop; 1-3 hours/day saved.

### Web-Clipper batch ingest #2 (2026-05-09 — 10 substantive bodies; mixed long-form + technical + lead-gen)

10 additional Web-Clipper captures, with 8 new authors and 2 existing-author follow-ups. Mix of theoretical (1), technical (2), personal-knowledge architecture (1), business-model/lead-gen (4), prompt-arsenal (1), image-only stub (1).

**Theoretical (1)**:
- [[wiki/sources/iroha1203-attractor-engineering]] — Hiroyuki Nakahata's *Attractor Engineering*: codebase-as-field, PR-as-force, CI/CD-as-dissipative-system, ArchSig-as-observer. 47KB dev.to article with Lean formalization (Algebraic Architecture Theory). **Adds new concept page [[attractor-engineering]].** Strongest theoretical anchor for AI-era software architecture in the wiki.

**Personal-knowledge architecture (1)**:
- [[wiki/sources/Shruti_0810-self-improving-obsidian]] — Shruti's 4-layer Obsidian + AI vault with 5-folder structure + 6AM Daily AI Briefing. **Fourth wild secondary citation of [[llm-wiki-pattern]]** (regent0x_ → nateherk → CyrilXBT → Shruti). *"Externalized cognition"* framing.

**Technical / Claude Code (2)**:
- [[wiki/sources/zodchiii-x-claude-code-settings]] — zodchiii's 15 Claude Code settings tour. Load-bearing claim: *"Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026"* (Boris Cherny on HN; unverified). One-minute setup: 2 env vars + permissions in `settings.json`. **2nd post from existing author** (first was Teamly content-marketing).
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — *(already in batch #1)*.

**Business model + lead-gen (4)**:
- [[wiki/sources/exploraX_-google-maps-leadgen]] — m0h's 5-step Google Maps + Instant Data Scraper + Claude Code lead-gen playbook for AI services. **Fills wiki's biggest pre-existing gap** in [[ai-automation-services]] coverage (how to find first 20 paying clients).
- [[wiki/sources/Ai_here202-mcp-opportunity]] — MCP-server-builds as $5K-$15K business opportunity. *"USB for AI"* analogy. App-Store-2009 framing. 3-capability framing (Tools / Resources / Prompts) + 3 monetization paths.
- [[wiki/sources/rubenhassid-claude-certifications]] — exactly 3 free Anthropic-issued Claude certs at `anthropic.skilljar.com` (most marketed certs are scams). PwC 56% AI-skill wage premium (up from 25%).
- [[wiki/sources/e_opore-system-design-roadmap]] — 12-phase AI-era system design career roadmap. Promotional weight (Dhanian ebook landing).

**Prompt-arsenal / content (2)**:
- [[wiki/sources/shannholmberg-content-os]] — Shann's Content OS framework (5M impressions in 2 weeks; 11M / 100K bookmarks in 2 months). 6-folder workspace + 4 content routes + 12-point bookmarkability rubric + 4 verbatim production-grade prompts + Hermes-Agent-or-Claude-Code-on-VPS runtime + Postiz publish layer.
- [[wiki/sources/bloggersarvesh-20-seo-prompts]] — Sarvesh's 20 detailed Claude prompts for local SEO across 4 parts (GBP / Website / Backlinks+Authority / Content+Tracking) with 12-week roll-out plan. **Strongest [[ai-seo]] prompt-pack source in the wiki.** **2nd post from existing author** (first was the Cowork-for-SEO thesis).

**Image-only stub (1)**:
- [[wiki/sources/wizofecom-x-2045182674130837681]] — wizofecom's *"Millions of views on X as a SaaS founder, 90 days"* — body is in 3 Twitter media images that aren't OCR'd. Recovery: re-clip with OCR.

#### DESIGN.md ingests (32 brands, 33 surfaces — initial 20 ingested 2026-05-02; +12 brands and Apple alt added 2026-05-04)

Initial 20:

- [[wiki/sources/stripe-design-md]] — *"Architectural blueprint on white marble."*
- [[wiki/sources/acctual-design-md]] — multi-typeface pill-everything system.
- [[wiki/sources/anthropic-design-md]] — *"Research journal printed on warm stone."*
- [[wiki/sources/antimetal-design-md]] — two-mode dark/light bridged by chartreuse.
- [[wiki/sources/apple-design-md]] — *"Gallery wall at natural light."* 28px card radius signature (MacBook Neo).
- [[wiki/sources/base44-design-md]] — pastel gradients on Canvas Pearl.
- [[wiki/sources/column-design-md]] — same-philosophy as Stripe, different execution.
- [[wiki/sources/cursor-design-md]] — *"Warm ivory software studio."*
- [[wiki/sources/dia-browser-design-md]] — 8px base, 5-stop spectrum gradient.
- [[wiki/sources/elevenlabs-design-md]] — most chromatically restrained.
- [[wiki/sources/family-design-md]] — most chromatically rich; illustration-led.
- [[wiki/sources/general-intelligence-company-design-md]] — bi-modal dark hero + light UI.
- [[wiki/sources/hyperstudio-design-md]] — most spartan; monochrome with amber.
- [[wiki/sources/linear-design-md]] — *"Midnight Command Center."* Reference dark-mode.
- [[wiki/sources/mercury-design-md]] — twilight palette; cards at 0px radius.
- [[wiki/sources/minimalissimo-design-md]] — most reductive; achromatic-only.
- [[wiki/sources/monopo-saigon-design-md]] — agency-extreme typography; 225px display.
- [[wiki/sources/raycast-design-md]] — deepest dark; glass via backdrop-blur.
- [[wiki/sources/superhuman-design-md]] — Aubergine + Iris brand pair; Super Sans VF.
- [[wiki/sources/titan-design-md]] — 160px button radius; largest specific pill.

Added 2026-05-04 (12 new brands + Apple alt surface):

- [[wiki/sources/airbnb-design-md]] — *"Vacation photos pinned to a white corkboard."* Single coral `#ff385c` brand color.
- [[wiki/sources/all-in-one-salon-design-md]] — GlossGenius beauty-software; *"Crisp digital ledger, with neon highlights."*
- [[wiki/sources/apple-design-md-alt]] — alternate Apple presentation surface; adds Sky Teal + Royal Violet accents.
- [[wiki/sources/augen-pro-design-md]] — third *"blueprint on white marble"* brand; ultra-light 350/400 weights.
- [[wiki/sources/authkit-design-md]] — *"Midnight Command Center"* frosted-glass dashboard; three custom typefaces.
- [[wiki/sources/contractbook-design-md]] — *"Playful professionalism"*; vibrant yellow + strong blue dual primaries.
- [[wiki/sources/customer-io-design-md]] — *"Architectural Blueprint on Frosted Glass."* Custom 475 weight.
- [[wiki/sources/gleap-design-md]] — *"Crisp canvas, magenta highlight."* Editorial PP New + functional Switzer.
- [[wiki/sources/hyer-aviation-design-md]] — *"Monochromatic luxury."* 187px display sizes.
- [[wiki/sources/openai-design-md]] — *"Blank page before the first word."* OpenAI Sans only.
- [[wiki/sources/perplexity-ai-design-md]] — *"Ivory Desk, Graphite Tools."* Smallest type scale (3 sizes).
- [[wiki/sources/ui-design-md]] — *"Monochromatic architectural blueprint."* Geist + Geist Mono.
- [[wiki/sources/virtual-design-md]] — *"Minimalist digital console."* Single weight (500) only.

## Entities

### People — authors

- [[wiki/entities/Ai_here202]] — MCP-server business-opportunity author (USB-for-AI analogy; App-Store-2009 framing).
- [[wiki/entities/akshay_pachaar]] — author of *"You're doing RAG wrong"*; chunk-as-unit-is-the-bug thesis.
- [[wiki/entities/anatoli-kopadze]] — author of the 20 Claude Prompts catalog.
- [[wiki/entities/andrej-karpathy]] — author of the LLM Wiki pattern.
- [[wiki/entities/alex-vacca]] — author of the services-as-software $7M agency playbook.
- [[wiki/entities/ashwingop]] — *(stub)* X creator; URL-only post queued in 2026-05-08 batch.
- [[wiki/entities/avi-chawla]] — DS/ML educator; author of Daily Dose of DS newsletter; substantive 2026-05-08 batch ingest.
- [[wiki/entities/bloggersarvesh]] — Sarvesh Shrivastava; SEO consultant; *Claude Cowork for SEO* niche.
- [[wiki/entities/bob-mwathu]] — *(stub)* LinkedIn creator who surfaced Saraev's DOE framing; introduces *self-annealing*.
- [[wiki/entities/brian-moran]] — author of the 10 online business models for 2026.
- [[wiki/entities/clear_graphics]] — author of the YC unicorn landing-pages analysis.
- [[wiki/entities/corey-haines]] — *(stub)* maintainer of the marketingskills Claude Code skill-pack.
- [[wiki/entities/creatorpascal]] — *(stub)* X creator; URL-only post queued in 2026-05-08 batch.
- [[wiki/entities/cyrilxbt]] — X creator; agentic-AI + personal-knowledge-vault content; 3 batch posts (2 substantive, 1 unretrievable).
- [[wiki/entities/e_opore]] — *(stub)* AI-era system design roadmap promoter.
- [[wiki/entities/eng-khairallah]] — author of the AI Automations $10K/mo playbook + three-session Cowork daily architecture.
- [[wiki/entities/exploraX_]] — m0h; Google Maps lead-gen for AI services (4 signals + Instant Data Scraper + Claude Code outreach playbook).
- [[wiki/entities/godofprompt]] — author of the Paul Graham startup-eval prompts.
- [[wiki/entities/heygurisingh]] — Guri Singh; Cowork onboarding specialist; folder-as-contract sub-pattern.
- [[wiki/entities/HeyZaraKhan]] — author of two Claude-ecosystem posts (Skills, Certified Architect).
- [[wiki/entities/heynavtoor]] — author of the 10-repos-replace-eng-team thesis.
- [[wiki/entities/hooeem]] — author of the build-an-AI-agent-today course.
- [[wiki/entities/ig_claims]] — Zack; paid-acquisition specialist; 5-stage Meta retargeting funnel + Conviction Gap Model.
- [[wiki/entities/iroha1203]] — Hiroyuki Nakahata; coiner of [[attractor-engineering]]; AAT Lean library author.
- [[wiki/entities/jaynitx]] — *(stub)* X creator; URL-only post queued in 2026-05-08 batch (2K likes).
- [[wiki/entities/kylejeong]] — Browserbase growth engineer; web-agent infrastructure focus.
- [[wiki/entities/mnilax]] — author of the 430-hours instrumented Claude Code study.
- [[wiki/entities/nainsi-dwiv]] — author of two production-AI architecture deep-dives (Agent Skills + tool-calling reliability).
- [[wiki/entities/nateherk]] — author of the AI OS playbook; runs a $3M/yr business on Claude Code.
- [[wiki/entities/neil_xbt]] — *(stub)* X creator; URL-only post queued in 2026-05-08 batch.
- [[wiki/entities/nick-saraev]] — author of the 5h+ Agentic Workflows course; coined the DO framework (now publicly framed as DOE).
- [[wiki/entities/noisyb0y1]] — *(stub)* author who surfaced the marketingskills skill-pack.
- [[wiki/entities/prakash-bhandari]] — *(stub)* author of the cleanest DOE framework expository.
- [[wiki/entities/regent0x]] — author of the Claude Code 24/7 dev team stack.
- [[wiki/entities/rohit4verse]] — coiner of [[cognitive-debt]]; X creator with order-of-use AI thesis.
- [[wiki/entities/rubenhassid]] — Ruben; Claude-certifications + claude101.com curator; PwC AI-skill wage premium data point.
- [[wiki/entities/shannholmberg]] — Shann; Lunar Strategy co-founder; Content OS architect (5M impressions in 2 weeks).
- [[wiki/entities/Shruti_0810]] — Shruti; 4th wild citation of LLM Wiki pattern; "externalized cognition" framing.
- [[wiki/entities/theaiworld22]] — author of the 21 CLAUDE.md instructions checklist (5 parts).
- [[wiki/entities/trq212]] — Thariq Shihipar (Claude Code lead at Anthropic); HTML-as-output thesis; substantive 2026-05-08 batch ingest.
- [[wiki/entities/wizofecom]] — *(stub)* SaaS-founder X-growth post (image-only stub).
- [[wiki/entities/zodchiii]] — darkzodchi; 2 substantive posts (Teamly content-marketing flag + 15 Claude Code settings tutorial).

### People — referenced

- [[wiki/entities/boris-cherny]] — *(stub)* Anthropic Claude Code engineer; cited as HN source for the silently-lowered-effort claim.
- [[wiki/entities/dhanian]] — *(stub)* author of the System Design ebook the e_opore thread promotes.
- [[wiki/entities/paul-graham]] — invoked as named persona in startup-eval prompts.
- [[wiki/entities/sam-altman]] — Worldcoin founder; OpenAI CEO (widely known, partially sourced).
- [[wiki/entities/vannevar-bush]] — 1945 originator of the [[memex]]; conceptual ancestor of the LLM Wiki.

### People — wiki owner

- [[wiki/entities/godwin-opoku-duah]] — **owner of this wiki**; founder of [[wiki/entities/roam-labs|ROAM Labs]]; co-founder of Brolly Africa; PM/CTO Key Expert on the [[wiki/projects/cpc-rtbvd|CPC RTBVD]] subcontract; *"Kobby"* informally.

### Organizations — wiki owner's

- [[wiki/entities/roam-labs]] — Godwin's AI products + services company. Houses Vedge / Kivora (ROAM GRC) / Clarvyn / _roamlabs as owned products plus client work for Coffee Break With Big Sis and StaceSprouts.
- [[wiki/entities/softtech-solutions]] — *(stub)* prime contractor on CPC RTBVD; subcontracts ROAM Labs for technical delivery.

### Organizations

- [[wiki/entities/agora]] — billion-dollar yearly-newsletter publishing empire (model #3 exemplar).
- [[wiki/entities/alventra-marketing]] — *(stub)* Sarvesh's local-SEO agency; runs the 20-prompt Claude Cowork system as managed service.
- [[wiki/entities/anthropic]] — AI research company; maintainer of Claude and Claude Code.
- [[wiki/entities/coldiq]] — Alex Vacca's $7M ARR services-as-software agency.
- [[wiki/entities/iternal-technologies]] — *(stub)* maintainer of [[wiki/entities/blockify|Blockify]]; enterprise RAG preprocessing focus.
- [[wiki/entities/lunar-strategy]] — *(stub)* Shann Holmberg's content-strategy agency; deploys Content OS for clients.
- [[wiki/entities/nous-research]] — open-weight AI research collective; publisher of Hermes-series models and [[wiki/entities/hermes-agent|Hermes Agent]].
- [[wiki/entities/samcart]] — Brian Moran's checkout/e-commerce platform; data source for the 2026 catalog.
- [[wiki/entities/trail-of-bits]] — security firm publishing claude-code-skills.
- [[wiki/entities/worldcoin]] — Sam Altman's iris-scanning identity company.

### Knowledge tooling

- [[wiki/entities/obsidian]] — local-first markdown editor; the working environment for this vault, also the persistent-memory layer in regent0x_'s stack.
- [[wiki/entities/qmd]] — local hybrid search engine for markdown wikis at scale.
- [[wiki/entities/refero]] — curated DESIGN.md library + MCP server for AI coding agents.
- [[wiki/entities/readwise]] — *(stub)* highlights/capture aggregator (articles, Kindle, tweets, newsletters).

### Open-source skill-packs

- [[wiki/entities/marketingskills-repo]] — coreyhaines31/marketingskills: 139 growth tactics + 12 SEO playbooks + CRO/A/B/pricing/AI-SEO frameworks + 16-tool tool registry. Marketing-domain analogue to Refero.
- [[wiki/entities/open-design]] — nexu-io/open-design: Apache-2.0 design platform with 64 SKILL.md bundles + 138 DESIGN.md systems + 15 agent-CLI runtime + BYOK proxy + MCP server. Largest skill-pack in the wiki.
- [[wiki/entities/nexu-io]] — *(stub)* maintainer org of Open Design.
- [[wiki/entities/claude-design]] — Anthropic's proprietary design-tooling product (artifact-first workflow); the antecedent Open Design replicates.
- [[wiki/entities/huashu-design]], [[wiki/entities/guizang-ppt-skill]], [[wiki/entities/open-codesign]], [[wiki/entities/multica]] — *(4 stubs)* lineage projects credited by Open Design.

### Claude Code ecosystem

- [[wiki/entities/claude-code]] — Anthropic's CLI; the central platform.
- [[wiki/entities/anthropic-agent-sdk]] — Anthropic's official agent SDK.
- [[wiki/entities/anthropic-cookbook]] — Anthropic's curated patterns repository.
- [[wiki/entities/anthropic-skills]] — Anthropic's official skill collection.
- [[wiki/entities/aiagency-io]] — Alex Vacca's 12-week services-as-software program.
- [[wiki/entities/ais-os]] — nateherk's AI OS starter repo.
- [[wiki/entities/claude-certified-architect]] — Anthropic's certification program.
- [[wiki/entities/claude101-com]] — *(stub)* Ruben Hassid's free-Claude-guides aggregator.
- [[wiki/entities/skilljar]] — *(stub)* Anthropic's official cert-delivery platform (`anthropic.skilljar.com`).
- [[wiki/entities/claude-flow]] — enterprise-grade multi-agent orchestration framework.
- [[wiki/entities/claude-mem]] — session-end memory compression and carry-forward.
- [[wiki/entities/claude-squad]] — terminal multiplexer for parallel Claude Code agents.
- [[wiki/entities/claude-subconscious]] — continuous background memory builder.
- [[wiki/entities/claude-task-master]] — long-build task scaffold.
- [[wiki/entities/davepoon-subagents-collection]] — drop-in subagent collection.
- [[wiki/entities/superpowers]] — workflow-discipline plugin (brainstorm → spec → plan → TDD → implement → review).
- [[wiki/entities/tdd-guard]] — TDD-enforcement skill / pre-commit hook.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — Trail of Bits's security audit skill collection.
- [[wiki/entities/wshobson-agents]] — production subagent collection.
- [[wiki/entities/wshobson-commands]] — production slash command collection.

### AI OS connections layer (referenced)

Tools named in [[wiki/sources/nateherk-claude-code-os-3m-business]] as connection-layer integrations.

- [[wiki/entities/clickup]] — task / comms backend.
- [[wiki/entities/fireflies]] — meeting transcription.
- [[wiki/entities/glaido]] — voice-input tool.
- [[wiki/entities/notion]] — knowledge / tasks platform.
- [[wiki/entities/quickbooks]] — accounting.
- [[wiki/entities/skool]] — community platform.

### AI coding tools (other)

- [[wiki/entities/aider]] — terminal pair programmer (mid-level dev replacement per heynavtoor).
- [[wiki/entities/browserbase]] — *(stub)* managed-browser infrastructure for AI agents; the "AWS for headless browsers."
- [[wiki/entities/ecc]] — *(stub)* hackathon-winning Claude Code automation tool (38 agents / 156 skills / 72 commands + AgentShield security audit). Surfaced via noisyb0y1.
- [[wiki/entities/teamly]] — *(stub)* managed-AI-team platform with Pixel Department visual monitoring. Surfaced via darkzodchi (content-marketing flag).
- [[wiki/entities/cline]] — VS Code autonomous agent.
- [[wiki/entities/codex-cli]] — *(stub)* OpenAI's coding-agent CLI; auto-detected by Open Design.
- [[wiki/entities/cowork]] — Anthropic's Claude Code mode for non-developer automation infrastructure; substantial coverage from Guri Singh (setup) + Khairallah (three-session daily architecture).
- [[wiki/entities/cursor]] — AI-assisted code editor.
- [[wiki/entities/deepseek-cli]] — *(stub)* DeepSeek's coding-agent CLI; auto-detected by Open Design.
- [[wiki/entities/devin]] — *(stub)* Cognition Labs autonomous SWE agent; auto-detected by Open Design.
- [[wiki/entities/gemini-cli]] — *(stub)* Google's coding-agent CLI; auto-detected by Open Design.
- [[wiki/entities/hermes-agent]] — Nous Research's MIT-licensed self-improving multi-platform agent; persistent memory + 200+ providers + 15+ messaging surfaces. Substantive entity.
- [[wiki/entities/opencode-cli]] — *(stub)* SST's open-source coding-agent CLI; auto-detected by Open Design.
- [[wiki/entities/openhands]] — autonomous SWE agent (junior dev replacement per heynavtoor).
- [[wiki/entities/qwen-cli]] — *(stub)* Alibaba Qwen-Coder CLI; auto-detected by Open Design.
- [[wiki/entities/replit]] — browser dev environment with AI coding.

### Agent frameworks

- [[wiki/entities/crewai]] — multi-agent role coordination framework.
- [[wiki/entities/langgraph]] — graph orchestration framework for production AI systems.
- [[wiki/entities/openai-agents-sdk]] — OpenAI's official agent SDK.

### Self-hosted / open-source ops tools

- [[wiki/entities/chatwoot]] — omnichannel customer support.
- [[wiki/entities/coolify]] — self-hosted Heroku/Vercel.
- [[wiki/entities/n8n]] — workflow automation.
- [[wiki/entities/posthog]] — product analytics.

### MCP integrations

- [[wiki/entities/anymailfinder]] — *(stub)* email enrichment tool; MCP-candidate per Saraev's worked example.
- [[wiki/entities/gmail]] — email MCP integration.
- [[wiki/entities/google-drive]] — file-storage MCP integration.
- [[wiki/entities/slack]] — communications MCP integration.
- [[wiki/entities/tavily]] — web search MCP server.

### Multi-provider LLM aggregators

- [[wiki/entities/openrouter]] — *(stub)* multi-provider LLM API aggregator; single endpoint fronts 200+ models. Used by [[wiki/entities/hermes-agent|Hermes Agent]].

### RAG / retrieval infrastructure

- [[wiki/entities/blockify]] — Iternal Technologies' open-source preprocessing layer that sits between document parser and vector store. Implements IdeaBlocks (typed Q-A packets with governance fields). 7-stage pipeline; 2.29× retrieval-distance reduction; 13.55% vector-accuracy improvement after dedup.

### Protocols / standards

- [[wiki/entities/model-context-protocol]] — *(stub)* Anthropic's open standard for AI-tool integration (distinct from individual MCP servers; see [[mcp-server]] concept).

### SEO / lead-gen / publish tooling

- [[wiki/entities/google-business-profile]] — *(stub)* primary surface for local-SEO prompts (Sarvesh's prompts 1-8) and m0h's lead-gen 4-signals.
- [[wiki/entities/google-maps]] — *(stub)* prospect-discovery surface for AI-services lead-gen.
- [[wiki/entities/google-search-console]] — *(stub)* used in Sarvesh's prompts 10, 12, 20.
- [[wiki/entities/semrush]] — *(stub)* keyword-gap and content-gap analysis tool.
- [[wiki/entities/ahrefs]] — *(stub)* backlink audit tool.
- [[wiki/entities/instant-data-scraper]] — *(stub)* free Chrome extension for bulk-extracting tabular data; used in m0h's lead-gen workflow.
- [[wiki/entities/postiz]] — *(stub)* open-source self-hostable social scheduler; publish layer in Shann's Content OS.

### Theoretical / formal methods

- [[wiki/entities/algebraic-architecture-theory]] — *(stub)* Hiroyuki Nakahata's Lean library; theoretical scaffolding under [[attractor-engineering]].

### Upcoming / waitlist products

- [[wiki/entities/bookmarkable-io]] — *(stub)* Shann Holmberg's upcoming Content OS blueprint product.

### YC unicorns analyzed (landing-page patterns)

- [[wiki/entities/airbnb]] — also has DESIGN.md ingest (graduated 2026-05-04).
- [[wiki/entities/coinbase]]
- [[wiki/entities/doordash]]
- [[wiki/entities/dropbox]]
- [[wiki/entities/gitlab]]
- [[wiki/entities/gusto]]
- [[wiki/entities/instacart]]
- [[wiki/entities/stripe]] — also in Refero catalog; first cross-source-cited entity.

### Brands in Refero catalog (design-md-ingested)

20 brands with substantive DESIGN.md ingests from the original 2026-05-02 batch (raw files refreshed with official Copy.md exports 2026-05-04):

- [[wiki/entities/acctual]]
- [[wiki/entities/antimetal]]
- [[wiki/entities/apple]] — two surfaces (MacBook Neo + alt).
- [[wiki/entities/base44]]
- [[wiki/entities/column]]
- [[wiki/entities/dia-browser]]
- [[wiki/entities/elevenlabs]]
- [[wiki/entities/family]]
- [[wiki/entities/general-intelligence-company]]
- [[wiki/entities/hyperstudio]]
- [[wiki/entities/linear]]
- [[wiki/entities/mercury]]
- [[wiki/entities/minimalissimo]]
- [[wiki/entities/monopo-saigon]]
- [[wiki/entities/raycast]]
- [[wiki/entities/superhuman]]
- [[wiki/entities/titan]]

11 new brands added 2026-05-04 (Airbnb listed above under YC unicorns also has a DESIGN.md ingest):

- [[wiki/entities/all-in-one-salon]] — GlossGenius beauty-software.
- [[wiki/entities/augen-pro]] — *(stub)* third "blueprint on white marble" brand.
- [[wiki/entities/authkit]] — WorkOS hosted-auth UI; dark frosted-glass.
- [[wiki/entities/contractbook]] — contract management; vibrant yellow + blue.
- [[wiki/entities/customer-io]] — lifecycle-marketing platform.
- [[wiki/entities/gleap]] — customer feedback / live chat tooling.
- [[wiki/entities/hyer-aviation]] — private aviation booking; 187px display sizes.
- [[wiki/entities/openai]] — AI products; *"Blank page before the first word."*
- [[wiki/entities/perplexity-ai]] — AI answer engine; smallest type scale.
- [[wiki/entities/ui]] — *(stub)* uncertain identity; Geist family.
- [[wiki/entities/virtual]] — *(stub)* uncertain identity; minimalist console.

### Brands in Open Design catalog (added 2026-05-05)

27 new brand entity stubs created from the [[wiki/sources/open-design-catalog|Open Design catalog]] ingest. 29 brands already existed in the wiki from prior Refero ingests (overlap with Open Design's catalog). All Open Design DESIGN.md raw files are at `raw/open-design/design-systems/`.

**AI & LLM** — [[wiki/entities/cohere]], [[wiki/entities/huggingface]], [[wiki/entities/mistral-ai]], [[wiki/entities/ollama]] *(stubs; 4)*

**Developer tools / hosting** — [[wiki/entities/vercel]], [[wiki/entities/github]], [[wiki/entities/supabase]] *(3)*

**Productivity & SaaS** — [[wiki/entities/discord]], [[wiki/entities/duolingo]], [[wiki/entities/zapier]], [[wiki/entities/arc]] *(4)*

**Backend & data** — [[wiki/entities/mongodb]], [[wiki/entities/sentry]], [[wiki/entities/hashicorp]] *(3)*

**Fintech & crypto** — [[wiki/entities/mastercard]], [[wiki/entities/revolut]], [[wiki/entities/wise]] *(3)*

**Media & consumer** — [[wiki/entities/nvidia]], [[wiki/entities/spotify]], [[wiki/entities/uber]], [[wiki/entities/pinterest]] *(4)*

**Design tools** — [[wiki/entities/figma]], [[wiki/entities/canva]], [[wiki/entities/framer]] *(3)*

**E-commerce / retail** — [[wiki/entities/nike]], [[wiki/entities/shopify]] *(2)*

**Automotive** — [[wiki/entities/tesla]] *(1)*

**As of 2026-05-05** — every Open Design brand is now a wiki entity. The 99 brands beyond the 27 above-listed were graduated together in a batch operation; see the section below.

### Open Design catalog brands graduated 2026-05-05 (99 stubs)

All 139 Open Design brands are now reachable as wiki entities. The 27 most-cross-citable brands were graduated 2026-05-05 (listed under their relevant categories above). The remaining 99 brands span real products + named-aesthetic styles, grouped here by Open Design category.


**AI & LLM** (7)
- [[wiki/entities/minimax]] — AI model provider. Bold dark interface with neon accents.
- [[wiki/entities/opencode-ai]] — AI coding platform. Developer-centric dark theme.
- [[wiki/entities/replicate]] — Run ML models via API. Clean white canvas, code-forward.
- [[wiki/entities/runwayml]] — AI video generation. Cinematic dark UI, media-rich layout.
- [[wiki/entities/together-ai]] — Open-source AI infrastructure. Technical, blueprint-style design.
- [[wiki/entities/voltagent]] — AI agent framework. Void-black canvas, emerald accent, terminal-native.
- [[wiki/entities/x-ai]] — Elon Musk's AI lab. Stark monochrome, futuristic minimalism.

**Productivity & SaaS** (4)
- [[wiki/entities/cal]] — Open-source scheduling. Clean neutral UI, developer-oriented simplicity.
- [[wiki/entities/intercom]] — Customer messaging. Friendly blue palette, conversational UI patterns.
- [[wiki/entities/mintlify]] — Documentation platform. Clean, green-accented, reading-optimized.
- [[wiki/entities/resend]] — Email API. Minimal dark theme, monospace accents.

**Developer Tools** (3)
- [[wiki/entities/expo]] — React Native platform. Dark theme, tight letter-spacing, code-centric.
- [[wiki/entities/lovable]] — AI full-stack builder. Playful gradients, friendly dev aesthetic.
- [[wiki/entities/warp]] — Modern terminal. Dark IDE-like interface, block-based command UI.

**Backend & Data** (3)
- [[wiki/entities/clickhouse]] — Fast analytics database. Yellow-accented, technical documentation style.
- [[wiki/entities/composio]] — Tool integration platform. Modern dark with colorful integration icons.
- [[wiki/entities/sanity]] — Headless CMS. Red accent, content-first editorial layout.

**Fintech & Crypto** (2)
- [[wiki/entities/binance]] — Crypto exchange. Bold yellow accent on monochrome, trading-floor urgency.
- [[wiki/entities/kraken]] — Crypto trading. Purple-accented dark UI, data-dense dashboards.

**Media & Consumer** (7)
- [[wiki/entities/ibm]] — Enterprise technology. Carbon design system, structured blue palette.
- [[wiki/entities/playstation]] — Gaming console retail. Three-surface channel layout, quiet-authority display type, cyan....
- [[wiki/entities/spacex]] — Space technology. Stark black and white, full-bleed imagery, futuristic.
- [[wiki/entities/theverge]] — Tech editorial media. Acid-mint and ultraviolet accents, Manuka display, rave-flyer sto....
- [[wiki/entities/vodafone]] — Global telecom brand. Monumental uppercase display, Vodafone Red chapter bands.
- [[wiki/entities/wired]] — Tech magazine. Paper-white broadsheet density, custom serif display, mono kickers, ink-....
- [[wiki/entities/xiaohongshu]] — Lifestyle UGC social platform. Singular brand red, generous radius, content-first.

**E-Commerce & Retail** (2)
- [[wiki/entities/meta]] — Tech retail store. Photography-first, binary light/dark surfaces, Meta Blue CTAs.
- [[wiki/entities/starbucks]] — Global coffee retail brand. Four-tier green system, warm cream canvas, full-pill buttons.

**Automotive** (5)
- [[wiki/entities/bmw]] — Luxury automotive. Dark premium surfaces, precise German engineering aesthetic.
- [[wiki/entities/bugatti]] — Hypercar brand. Cinema-black canvas, monochrome austerity, monumental display type.
- [[wiki/entities/ferrari]] — Luxury automotive. Chiaroscuro editorial, Ferrari Red accents, cinematic black.
- [[wiki/entities/lamborghini]] — Supercar brand. True black surfaces, gold accents, dramatic uppercase typography.
- [[wiki/entities/renault]] — French automotive. Vibrant aurora gradients, NouvelR typography, bold energy.

**Design & Creative** (4)
- [[wiki/entities/airtable]] — Spreadsheet-database hybrid. Colorful, friendly, structured data aesthetic.
- [[wiki/entities/clay]] — Creative agency. Organic shapes, soft gradients, art-directed layout.
- [[wiki/entities/miro]] — Visual collaboration. Bright yellow accent, infinite canvas aesthetic.
- [[wiki/entities/webflow]] — Visual web builder. Blue-accented, polished marketing site aesthetic.

**Editorial & Print** (1)
- [[wiki/entities/kami]] — Editorial paper system: warm parchment canvas, ink-blue accent, serif-led hierarchy. Bu....

**Editorial · Studio** (1)
- [[wiki/entities/atelier-zero]] — A magazine-grade, collage-driven visual system: warm paper canvas, surreal.

**Modern & Minimal** (10)
- [[wiki/entities/clean]] — Simplicity-focused design with ample whitespace, legible typography, and a limited colo....
- [[wiki/entities/contemporary]] — Current-era minimalist design with bento grids, dark mode support, and high-performance....
- [[wiki/entities/flat]] — Two-dimensional minimalist style with vibrant colors, clean typography, and no 3D effec....
- [[wiki/entities/minimal]] — Stripped-back design emphasizing whitespace, clean typography, and restrained color for....
- [[wiki/entities/modern]] — Contemporary editorial style with serif typography, minimal palettes, and clean layouts....
- [[wiki/entities/mono]] — Monospace-driven, matrix-inspired design with high-contrast elements, compact density, ....
- [[wiki/entities/refined]] — Carefully curated, modern minimal style with elegant serif typography and understated, ....
- [[wiki/entities/shadcn]] — Shadcn/ui-inspired design with minimal, clean components, monochrome palette, and utili....
- [[wiki/entities/simple]] — Straightforward, no-frills design with clean typography, neutral colors, and intuitive ....
- [[wiki/entities/sleek]] — Modern minimalist aesthetic with clean lines, intentional color palette, subtle interac....

**Bold & Expressive** (8)
- [[wiki/entities/bold]] — Strong visual presence with heavyweight typography, high-contrast colors, and commandin....
- [[wiki/entities/brutalism]] — Raw, anti-design aesthetic inspired by concrete architecture with unadorned elements, j....
- [[wiki/entities/colorful]] — Vibrant, high-contrast palettes and gradients for engaging, memorable, and modern user ....
- [[wiki/entities/dramatic]] — High-contrast, theatrical design with bold layouts, immersive visuals, and unconvention....
- [[wiki/entities/energetic]] — Dynamic, vibrant style with thick borders, geometric shapes, high-contrast colors, and ....
- [[wiki/entities/expressive]] — Vibrant, personality-driven design with bold colors, playful graphics, and dynamic layo....
- [[wiki/entities/neobrutalism]] — Modern take on brutalism with bold borders, vivid accent colors, and raw, high-contrast....
- [[wiki/entities/vibrant]] — Lively, colorful design with bold playful typography, warm accents, and dynamic visual ....

**Creative & Artistic** (11)
- [[wiki/entities/artistic]] — High-contrast, expressive style with creative typography and bold color choices for vis....
- [[wiki/entities/cafe]] — Cozy cafe-inspired interface with warm tones, soft typography, and clean layouts for a ....
- [[wiki/entities/cosmic]] — Futuristic sci-fi aesthetic with dark themes, vibrant neon accents, and immersive spati....
- [[wiki/entities/creative]] — Playful, character-driven design with expressive typography and bold graphics for landi....
- [[wiki/entities/doodle]] — Hand-drawn, sketch-like style with doodles, handwritten fonts, and imperfect lines for ....
- [[wiki/entities/editorial]] — Magazine-inspired editorial layout with refined serif typography, structured grids, and....
- [[wiki/entities/fantasy]] — Game-inspired fantasy aesthetic with bold, premium visuals, rich color palettes, and im....
- [[wiki/entities/friendly]] — Approachable, intuitive design with rounded elements, ample whitespace, and soft pastel....
- [[wiki/entities/lingo]] — Playful, minimal design with bright colors, rounded shapes, tactile 3D borders, and fri....
- [[wiki/entities/publication]] — Print-inspired visual language for books, magazines, and reports with editorial grids a....
- [[wiki/entities/storytelling]] — Narrative-driven design using visuals, copy, and interaction to guide users through eng....

**Professional & Corporate** (10)
- [[wiki/entities/ant]] — Structured, enterprise-focused design system emphasizing clarity, consistency, and effi....
- [[wiki/entities/application]] — App dashboard with purple-themed aesthetic, top-bar navigation, card-based layouts, and....
- [[wiki/entities/corporate]] — Professional, brand-aligned design with structured grids, minimalist layouts, and consi....
- [[wiki/entities/dashboard]] — Dark-themed cloud-platform aesthetic with modular grids, glass-like panels, and strong ....
- [[wiki/entities/elegant]] — Graceful, refined aesthetic with delicate typography, minimal palettes, and polished la....
- [[wiki/entities/enterprise]] — Clean, high-contrast enterprise design for data-driven workflows with intuitive drag-an....
- [[wiki/entities/luxury]] — High-end dark aesthetic with bold headings, monochromatic palette, and premium feel for....
- [[wiki/entities/material]] — Google's Material Design with layered surfaces, dynamic theming, built-in motion, and r....
- [[wiki/entities/premium]] — Apple-inspired premium aesthetic with precise spacing, modern typography, and a refined....
- [[wiki/entities/professional]] — Polished, business-ready design with modern typography, structured layouts, and a trust....

**Layout & Structure** (4)
- [[wiki/entities/bento]] — Modular grid layout with card-like blocks, clear hierarchy, soft spacing, and subtle vi....
- [[wiki/entities/levels]] — Conversion-focused design that removes friction and guides users toward action through ....
- [[wiki/entities/perspective]] — Spatial depth design with isometric views, vanishing points, and layered elements that ....
- [[wiki/entities/spacious]] — Generous whitespace, consistent padding, and grid-based layouts for clean, readable, an....

**Morphism & Effects** (6)
- [[wiki/entities/claymorphism]] — Soft, rounded 3D-like shapes mimicking malleable clay with playful, puffy elements and ....
- [[wiki/entities/glassmorphism]] — Frosted glass effect with translucent layers, subtle blur, and luminous borders for dep....
- [[wiki/entities/gradient]] — Smooth color transitions and gradient-rich surfaces for modern, playful interfaces with....
- [[wiki/entities/neon]] — Electric neon glow effects with high-contrast color pairings for bold, attention-grabbi....
- [[wiki/entities/neumorphism]] — Soft, extruded UI elements with inner and outer shadows on monochromatic surfaces for a....
- [[wiki/entities/skeumorphism]] — Real-world mimicry with textured surfaces, 3D effects, and familiar physical metaphors ....

**Retro & Nostalgic** (4)
- [[wiki/entities/dithered]] — Dot-pattern rendering technique that simulates shades with a limited palette for nostal....
- [[wiki/entities/paper]] — Paper-textured, print-inspired design with minimal colors, clean serif/sans typography,....
- [[wiki/entities/retro]] — Throwback design with vintage-inspired typography, high-contrast retro palettes, and no....
- [[wiki/entities/vintage]] — 1950s-1990s nostalgia with skeuomorphic touches, grainy textures, retro color palettes,....

**Themed & Unique** (5)
- [[wiki/entities/agentic]] — Conversational AI-first interface with minimal controls, clear outcomes, and delegated ....
- [[wiki/entities/futuristic]] — Forward-looking design with tech-inspired typography, modern layouts, and a sleek, inno....
- [[wiki/entities/pacman]] — Retro arcade-inspired design with pixel fonts, dotted borders, playful high-contrast co....
- [[wiki/entities/tetris]] — Classic block-game inspired design with playful colors, bold display fonts, and compact....
- [[wiki/entities/totality-festival]] — Surface: web.

**Starter** (2)
- [[wiki/entities/default]] — A clean, product-oriented default. Use when the brief doesn't call for a.
- [[wiki/entities/warm-editorial]] — A serif-led magazine aesthetic. Terracotta accent on warm off-white paper —.

*Section count: 99 brands listed.*

## Concepts

### Operations of the LLM Wiki

- [[wiki/concepts/ingest]] — the write path: process a new raw source into wiki pages.
- [[wiki/concepts/lint]] — periodic health check across the wiki.
- [[wiki/concepts/query]] — the read path: answer questions against the wiki with citations.

### Agent foundations

- [[wiki/concepts/agentic-loop]] — the runtime substrate of every agent.
- [[wiki/concepts/agent-workflow-patterns]] — five Anthropic-documented patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- [[wiki/concepts/augmented-llm]] — LLM + tools + retrieval + memory.
- [[wiki/concepts/beginner-agent-types]] — research, content, workflow, personal-knowledge, operator.

### Patterns and meta-patterns

- [[wiki/concepts/attractor-engineering]] — *(new 2026-05-09)* Hiroyuki Nakahata's design theory for AI-era software development: codebase as field, PR as force, CI/CD as dissipative system, ArchSig as observer.
- [[wiki/concepts/dual-write-rollout]] — additive parallel-write migration pattern: new path runs next to legacy, failures swallowed, observed for a window, then ownership flips. Worked example: Kivora's 2026-05-08 Finding-schema migration.
- [[wiki/concepts/llm-wiki-pattern]] — persistent, LLM-maintained markdown wiki built on top of curated raw sources. **4 wild citations now.**
- [[wiki/concepts/markdown-as-agent-contract]] — meta-pattern: markdown files as the contract layer between humans and AI agents.
- [[wiki/concepts/memex]] — Vannevar Bush's 1945 vision of a personal, associative knowledge store.
- [[wiki/concepts/retrieval-augmented-generation]] — per-query retrieval over raw documents; contrast case + chunk-as-unit-is-the-bug critique (Akshay/Blockify, 2026-05-08).

### Claude Code mechanisms

- [[wiki/concepts/claude-code-hooks]] — lifecycle automation (pre-commit, session-start, pre-push).
- [[wiki/concepts/claude-code-overhead-patterns]] — 9 measured token-waste patterns + fixes.
- [[wiki/concepts/claude-code-skills]] — the skill mechanism; markdown-defined invokable capabilities.
- [[wiki/concepts/claude-code-slash-commands]] — user-defined invocation shortcuts.
- [[wiki/concepts/multi-agent-orchestration]] — running multiple Claude Code agents in parallel against isolated workspaces.
- [[wiki/concepts/scheduled-automation]] — `/schedule`-registered routines running unattended.
- [[wiki/concepts/subagents]] — multi-agent role specialization (architect/coder/reviewer/tester/ops).

### Agent architecture

- [[wiki/concepts/ai-os-pattern]] — Three Ms + Four Cs framework for treating Claude Code as an OS.
- [[wiki/concepts/cognitive-debt]] — Rohit's framing: *"AI before independent thinking builds debt; AI after independent thinking amplifies."* Failure mode where AI-augmented work erodes underlying competence over time.
- [[wiki/concepts/do-framework]] — Saraev's DOE framework (Directive + Orchestration + Execution; previously framed as 2-layer DO). The deterministic-agentic-workflow architecture.
- [[wiki/concepts/self-annealing]] — system-level property of DOE workflows: directives accumulate fixes via the orchestrator's error-recovery loop, getting more reliable with use.
- [[wiki/concepts/hot-cache]] — `_hot.md`: 500-token active-state file extending the LLM Wiki pattern.
- [[wiki/concepts/progressive-disclosure]] — load metadata first, content on demand.
- [[wiki/concepts/reasoning-execution-split]] — LLM reasons; deterministic code executes.
- [[wiki/concepts/reliability-decay-math]] — chained-probability problem that motivates separation-of-concerns architectures.

### Integration & data layer

- [[wiki/concepts/mcp-server]] — Model Context Protocol server; the tool-integration layer.

### Agent-contract markdown files

- [[wiki/concepts/agents-md]] — *(stub)* AGENTS.md — Codex-flavored project contract.
- [[wiki/concepts/context-file]] — per-client business voice/standards file (paired with skill files).
- [[wiki/concepts/design-md]] — DESIGN.md — design-system reference for AI coding agents.
- [[wiki/concepts/readme-md]] — *(stub)* README.md — older convention being absorbed into the agent-contract family.
- [[wiki/concepts/skill-md]] — *(stub)* SKILL.md — single-capability instructions.

### Business models

- [[wiki/concepts/ai-automation-services]] — services-business model for selling AI automations.
- [[wiki/concepts/services-as-software]] — scaled agency-shape with software-margin accelerator layer.
- [[wiki/concepts/churn-at-scale]] — the agency-growth math that motivates the accelerator layer.
- [[wiki/concepts/horizontal-leverage]] — automating 90% of many roles is 9,000× more valuable than 100% of one.
- [[wiki/concepts/online-business-models-2026]] — Brian Moran's 10-models-that-work catalog.

### Design / UI

- [[wiki/concepts/landing-page-patterns]] — 11 patterns shared by YC unicorn landing pages.

### Marketing / CRO / SEO

- [[wiki/concepts/ai-seo]] — optimizing for AI citation rather than keyword ranking; three pillars (Structure / Authority / Presence) + machine-readable endpoints (`/llms.txt`, `/pricing.md`).
- [[wiki/concepts/switching-forces]] — push/pull/habit/anxiety: the four forces that explain why customers switch and why they don't. Worked example mapped for Vedge.

### AI design tooling architecture

- [[wiki/concepts/anti-ai-slop-machinery]] — five-mechanism stack (brand-spec extraction protocol + 5-dim self-critique + P0/P1/P2 + blacklist + honest placeholders) for preventing AI-generated design slop. Generalizes to PRDs, marketing copy, runbooks.
- [[wiki/concepts/artifact-first-workflow]] — single-`<artifact>`-HTML emission rendered in sandboxed `srcdoc` iframe; exports flow from there. Originated in Claude Design.
- [[wiki/concepts/byok-proxy]] — multi-provider LLM proxy with SSE chunk normalization + SSRF blocking. BYOK trust model.
- [[wiki/concepts/question-form-first]] — Turn-1 mandatory structured-intake form (locks surface/audience/tone/brand/scale) preventing 80% of design redirects.
- [[wiki/concepts/visual-directions]] — small set of deterministic OKLch palette + font-stack presets (Editorial Monocle / Modern Minimal / Tech Utility / Brutalist / Soft Warm) for "no improvisation" generation.

### Personal productivity / prompts

- [[wiki/concepts/personal-claude-prompts]] — curated personal prompt libraries as a productivity multiplier.

## Projects

Add a project from inside its directory with `/brain-add-project` in any Claude Code session. Pages live at `wiki/projects/<slug>.md` and group here by status.

### Active

> **Affiliation key**: 🏢 = ROAM Labs owned product · 🤝 = ROAM Labs client work · 🛡️ = Brolly Africa owned platform · 🌂 = Brolly Africa client work · 🏛️ = SoftTech subcontract / government · 📣 = ROAM Labs corporate self. See [[wiki/syntheses/godwin-portfolio]] for the full landscape.

- 🌂 [[wiki/projects/asanti-brokers]] — *(Brolly Africa client work)* marketing website for *Asanti Brokers Limited*, a Ghana NIC-registered insurance brokerage; Next.js 16 App Router + React 19 + Tailwind v4 static-shaped site with one route per product line (motor / property / business-liability / fire & perils / marine cargo / travel / personal accident / group employee benefits); WhatsApp CTA + cookie consent + NIC trust badge; deployed at `asanti.insure` on Vercel.
- 🛡️ [[wiki/projects/brolly]] — *(Brolly Africa owned platform)* African insurtech / digital-insurance platform (Brolly Africa) with vehicle-insurance roots in the Bolt-driver market; multi-repo workspace at `~/Brolly` holding a JHipster 7.5 Spring Boot backend (`backend-service`) being rewritten in Kotlin + Spring Boot 3.5 (`core-backend`), a React 18 admin dashboard (`admin-portal`), a Next.js 13 customer portal (`customer-portal`), a fresh Vite / React 19 landing (`landing-page`), and a shared `insurtech-platform` UI template; Azure Postgres + PayStack + AWS S3; canonical repos on GitHub `Brolly-Africa/`, legacy mirrors on GitLab `brolly1/`.
- 🏢 [[wiki/projects/clarvyn]] — *(ROAM Labs owned product)* AI-first HR platform for startup founders; the Claude agent *is* the HR department (proactive payroll, reviews, hiring, employee 1:1s). Five-service stack: Spring Boot 3.3.5 HRIS + FastAPI Claude agent (Sonnet+Haiku, pgvector RAG, MCP layer) + React 19 portal + React Native / Expo 54 mobile + landing. Wave 6 (Slack bot, MCP, proactive Expo Push, Integrations UI) shipped week of 2026-05-09.
- 🤝 [[wiki/projects/coffee-break-with-big-sis]] — *(ROAM Labs client work)* multi-tenant networking + mentorship SaaS for institutions (universities, alumni chapters, professional bodies); schema-per-tenant Spring Boot 3.4 / Java 17 backend + React 19 / Vite 7 / Tailwind v4 frontend; weighted-Jaccard mentor↔mentee matching across 6 dimensions. Editorial Café Zine redesign of landing + 3 auth pages shipped 2026-04-11.
- 🏛️ [[wiki/projects/cpc-rtbvd]] — *(SoftTech subcontract; ROAM delivers)* bid-stage React 19 + Tailwind v4 dashboard prototype + full QCBS bid package for the **Cocoa Processing Company Plc** "Real-Time Business Visibility" tender (RFP CPC/PRO/CS/1/26, deadline 8 Apr 2026); GHS 2.98M firm 12-week build for SoftTech Solutions; no VAT, no maintenance, no training scope (handover model); 4 named Key Experts (Godwin/Lilian/Richmond/Christian); bid finalized 2026-05-09 awaiting CPC award.
- 🏢 [[wiki/projects/kivora]] — *(ROAM Labs owned product; brand: ROAM GRC)* AI-powered multi-tenant SaaS GRC platform (product name **ROAM GRC**); 13-module Spring Boot backend + React/Vite frontend + FastAPI Claude agent with pgvector RAG; named as Vedge's GRC of record. **Tier 1 of the Finding-schema migration** shipped end of 2026-05-08, dual-writing in production behind a toggle pending 2-week observation; worked example of [[wiki/concepts/dual-write-rollout]].
- 📣 [[wiki/projects/roamlabs]] — *(ROAM Labs corporate self)* corporate marketing site for the **_roamlabs** AI agency (sister brand to ROAM GRC / Vedge under the **ROAM** umbrella); single Next.js 14 App Router site with custom NeuralNetwork canvas hero. Visual direction unsettled — editorial-quarterly and mission-control aesthetics both prototyped + reverted on 2026-05-09.
- 🤝 [[wiki/projects/stacesprouts]] — *(ROAM Labs client work)* omni-channel commerce platform (storefront + admin + Flutter POS) for a Ghana baby/kids fashion retailer; Spring Boot + React 19 + Flutter; mirrors [[wiki/projects/vedge|Vedge]]'s `vedge_staff` Flutter architecture; Flutterwave + mnotify integrations; deployed on Vercel + Railway.
- 🏢 [[wiki/projects/vedge]] — *(ROAM Labs owned product)* multi-tenant healthcare OS for African hospitals, clinics, labs, pharmacies; modular-monolith Spring Boot backend + Next.js web + Flutter mobile (patient + staff).

### Paused

_(none yet)_

### Exploring

_(none yet)_

### Completed / archived

_(none yet)_

## Syntheses

- [[wiki/syntheses/agent-review-framework]] — reusable five-lens framework for auditing LLM agent codebases against architectural first principles (agentic-loop, augmented-llm, reasoning-execution-split, agent-workflow-patterns, retrieval-augmented-generation). Worked example: 2026-05-08 review of [[wiki/projects/kivora|Kivora]]'s Python agent.
- [[wiki/syntheses/refero-open-design-claude-design-comparison]] — three strategic bets in AI design tooling: Refero (curated SaaS catalog) vs Open Design (open-source full-stack platform) vs Claude Design (proprietary Anthropic surface). Includes adoption-fit decision matrix and Vedge-specific recommendation.
- [[wiki/syntheses/godwin-portfolio]] — *2026-05-09*. **One-page map of every project Godwin owns or delivers**, organized by *who owns the IP* and *who holds the client relationship*. 4 buckets: ROAM Labs owned products (Vedge / Kivora / Clarvyn / _roamlabs) / ROAM client work (Coffee Break / StaceSprouts) / Brolly client work (Asanti) / SoftTech subcontract (CPC RTBVD).

---

## Reading paths

A few suggested entry points into the wiki:

- **"What is this vault and how does it work?"** → [[CLAUDE]] → [[wiki/concepts/llm-wiki-pattern]] → [[wiki/sources/llm-wiki-pattern-karpathy]].
- **"Why this approach over RAG?"** → [[wiki/concepts/retrieval-augmented-generation]] → [[wiki/concepts/llm-wiki-pattern]].
- **"Where does this idea come from historically?"** → [[wiki/concepts/memex]] → [[wiki/entities/vannevar-bush]].
- **"How do markdown files fit into AI tooling more broadly?"** → [[wiki/concepts/markdown-as-agent-contract]] → [[wiki/concepts/design-md]] → [[wiki/entities/refero]].
- **"How do I get the most out of Claude Code?"** → [[wiki/sources/regent0x-claude-code-247-dev-team]] → [[wiki/entities/claude-code]] → [[wiki/concepts/subagents]] → [[wiki/concepts/multi-agent-orchestration]].
- **"How do I build an AI agent from scratch?"** → [[wiki/sources/hooeem-build-an-ai-agent-today]] → [[wiki/concepts/agentic-loop]] → [[wiki/concepts/augmented-llm]] → [[wiki/concepts/agent-workflow-patterns]] → [[wiki/concepts/beginner-agent-types]].
- **"What open-source repos should I know about?"** → [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] → [[wiki/entities/openhands]], [[wiki/entities/aider]], [[wiki/entities/cline]], [[wiki/entities/crewai]], [[wiki/entities/langgraph]], [[wiki/entities/n8n]], [[wiki/entities/coolify]], [[wiki/entities/posthog]], [[wiki/entities/chatwoot]].
- **"How do I sell AI automations as a service?"** → [[wiki/sources/khairallah-ai-automations-10k-month]] → [[wiki/concepts/ai-automation-services]] → [[wiki/concepts/context-file]] → [[wiki/concepts/mcp-server]].
- **"How do I scale a services-as-software agency?"** → [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] → [[wiki/concepts/services-as-software]] → [[wiki/concepts/churn-at-scale]].
- **"What online business models still work in 2026?"** → [[wiki/sources/realbrianmoran-making-money-online-2026]] → [[wiki/concepts/online-business-models-2026]].
- **"How do I get more out of my $20 Claude subscription?"** → [[wiki/sources/AnatoliKopadze-20-claude-prompts]] → [[wiki/concepts/personal-claude-prompts]].
- **"What MCP servers should I know about?"** → [[wiki/concepts/mcp-server]] → [[wiki/entities/tavily]], [[wiki/entities/gmail]], [[wiki/entities/google-drive]], [[wiki/entities/slack]].
- **"What makes a great landing page?"** → [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] → [[wiki/concepts/landing-page-patterns]].
- **"Why isn't my landing page converting?"** → [[wiki/concepts/switching-forces]] (push/pull/habit/anxiety) → [[wiki/concepts/landing-page-patterns]] (the 11 patterns) → [[wiki/entities/marketingskills-repo]] (CRO 7-question audit + skill-pack).
- **"How do I show up in AI overview answers?"** → [[wiki/concepts/ai-seo]] → [[wiki/entities/marketingskills-repo]] → [[wiki/sources/noisyb0y1-marketingskills-repo]].
- **"What's the open-source alternative to Claude Design?"** → [[wiki/sources/nexu-io-open-design]] → [[wiki/entities/open-design]] → architecture deep-dives: [[wiki/concepts/anti-ai-slop-machinery]] / [[wiki/concepts/artifact-first-workflow]] / [[wiki/concepts/question-form-first]] / [[wiki/concepts/byok-proxy]] / [[wiki/concepts/visual-directions]].
- **"How do I prevent AI design slop?"** → [[wiki/concepts/anti-ai-slop-machinery]] (the five mechanisms) → [[wiki/concepts/visual-directions]] (deterministic presets) → [[wiki/concepts/question-form-first]] (Turn-1 intake).
- **"What's the agent equivalent of an LLM Wiki?"** → [[wiki/concepts/llm-wiki-pattern]] (external-markdown approach) → [[wiki/concepts/hot-cache]] (extension) → [[wiki/sources/nousresearch-hermes-agent]] (agent-internal alternative — same goal, different mechanism).
