# index.md — Wiki catalog

The content-oriented index of this wiki. Read this first when answering a query, then drill into the linked pages. See [[CLAUDE]] for conventions and [[log]] for the chronological record of operations.

**Stats**: 146 sources · 671 entities · 214 concepts · 12 projects · 6 syntheses · last updated 2026-07-13 *(weekly lint pass 2026-07-13)*

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

### Wave ingest (2026-05-21) — Cluster 1: Helm/Hermes/multi-agent (8 of 54)

First cluster of a 54-source wave. Focus: agents that compose directly into [[wiki/projects/helm|Helm]]'s 6-agent build + the Hermes-Agent ecosystem maturation.

- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — **Hermes v0.14 `/goal` command** full guide. 7 commands (`/goal` / `/goal status` / `/goal pause` / `/goal resume` / `/goal clear` / `/subgoal` / `/handoff`). Promotes Hermes from reactive chat to autonomous background worker.
- [[wiki/sources/shannholmberg-hermes-agent-operator]] — **Hermes operator playbook**. 4-level fleet model (one agent → direct specialists → orchestrator → automated team). Agent-control-room pattern (`/root/vps-agents/` side control plane). 5-layer SEO agent architecture (one Docker container, 21 steps). Hermes at **150K stars / #1 on OpenRouter**.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — **4-job integration model** (Research / Action / Workspace / Memory). 12 specific integrations + 3 stacked-workflow worked examples. **5th wild citation of [[llm-wiki-pattern]]** (explicit *"Karpathy-style LLM wiki second-brain maxxing"*).
- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — **Commercial Hermes use case ($10K/mo clipping pages)**. Hermes orchestrates Vugola (clip-extraction) + Postiz (publish) from one Telegram message. Consumer-content-scale variant of [[ai-automation-services]].
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — **The mental-model post**: agent vs automation. Automation executes fixed sequence; agent reads situation + context + makes judgment. Sequel framing under the 5-agent implementation.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — **10 Claude Code agents to build**, framed as *job description + trigger + output*. Three host surfaces: slash commands / hooks / hosted scripts (Claude Agent SDK).
- [[wiki/sources/Mnilax-9-cowork-prompt-templates]] — **9 Cowork slash-command templates** that pulled back 34 hours/week (47-min median active-supervision in a former 8-hour workday). *"The plugin is the kitchen, the slash command is the recipe."*
- [[wiki/sources/dabit3-agent-hooks-in-depth]] — **Canonical agent-hooks deep-dive**. 6 lifecycle points (`SessionStart` / `UserPromptSubmit` / `PreToolUse` / `PostToolUse` / `Stop` / `SessionEnd`). Operating model: *event → matcher → handler → outcome*. *"Use prompts for guidance. Use hooks for behavior that should run every time."*

### Batch backlog ingest (2026-06-06) — 47 sources from the un-ingested raw backlog

Bulk workflow ingest of the remaining raw backlog. 47 source pages, ~351 new entities, ~158 new concepts. Spans quant open-source, Claude Code tooling, AI-engineer roadmaps, agentic memory + harness theory, voice agents, backend scalability, AI business models, inference engines, and agentic capital markets.

- [[wiki/sources/zostaff-22-hedge-fund-quant-open-source-repos]] — 22 open-source repos from 7 elite quant firms (Two Sigma, Man Group, Jane Street, D.E. Shaw, HRT, Optiver, WorldQuant); thesis: open vs closed source maps onto whether a firm's moat is talent or alpha.
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — 9 Claude Code plugins/MCP servers (Context7, GitHub, Playwright, Filesystem, Sequential Thinking, Browser Tools, Database, Terminal, Memory) framed as "tooling > prompting."
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — 7-stage AI-engineer roadmap (Python → dev tools → LLMs → frameworks → projects → advanced skills → LLMOps); thesis: AI engineering is still software engineering.
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] — founder thesis (pitch for Interact Labs): the static website is AI's trillion-dollar blind spot; replace it with a conversational, self-assembling interface; discovery is moving into AI answer engines.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — agentic-memory reference: continuity/context/learning; 4 memory types (in-context, external, episodic, parametric); ChromaDB+OpenAI+Claude code; decay/importance/consolidation. "20% storage, 80% retrieval."
- [[wiki/sources/petradonka-agents-need-feedback-loops]] — Warp's Petra Donka on building Buzz, a self-improving community-engagement agent: principles over rules, a learn-how-to-learn skill, a low-friction Slack feedback loop, and self-improvement shipped as reviewed daily PRs — the loop matters more than the prompt.
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] — reverse-engineers xAI's (claimed) open-sourced For You feed into a 14-signal weighted-sum model; 3 Claude-Code blueprints for a voice-cloning personal X agent (Session / Approval-Telegram / Autonomous feedback-loop).
- [[wiki/sources/nateherk-claude-design-tally-brand]] — nateherk builds a full fictional brand ("Tally") end-to-end in Claude Design — deck, landing page, mobile, video, live to Vercel — plus a weekly-quota-stretching playbook (plan in chat, execute in Design, ship from Code).
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — definitive guide to the Forward Deployed Engineer (FDE) role: why Applied AI firms need FDEs, the Audit/Evals/Deployment lifecycle, and a 30-day break-in roadmap. Varick recruiting funnel.
- [[wiki/sources/shreyas-get-to-the-core-of-the-thing]] — Shreyas Doshi: refuse high-altitude product binaries (wide/deep, CAC/LTV) as theater; the real question is one level down — specific bets on specific features grounded in customer insight.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — interpretive X thread reframing Google I/O 2026 as a decade strategy: Gemini as Google's AI operating layer; agentic AI, AI-native Android, browser/YouTube/XR; the real contest is the interface layer.
- [[wiki/sources/retrochainer-claude-700k-musk-tweets]] — case study: trader "Aniki" nets $700K market-making Polymarket Musk-tweet markets + tail "lottery" bets (Taleb barbell + Kelly), with Claude used as infrastructure to author the trading-bot logic; promotional.
- [[wiki/sources/insomnia_vip-ai-models-that-make-money]] — building monetizable AI influencer / virtual-persona accounts; consistency-over-tooling thesis + ~10 income streams (incl. automated "relationship-style" content). Off-cluster; ethical flag; no audited figures.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] — 18-step consumer Claude.ai playbook (Projects + Custom Instructions + thinking-partner reframe + token hygiene + 5 ready prompts); shares the "10% of potential" thesis.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — heynavtoor's 7-layer ~60-min no-code recipe for a persistent personal Claude (Preferences → Projects → Memory → voice → file uploads → connectors → scheduled tasks); compound-effect thesis.
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — ~6,000-word voice-agent build guide: real-time five-component pipeline (STT/RAG/LLM/TTS/functions) inside a ~700ms latency budget, dual-agent RAG cache (VoiceAgentRAG), conversation design, two-checkpoint safety, four-layer eval.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — CyrilXBT's full Dataview "read not store" Obsidian dashboard (6 live-query sections) + Claude Code/MCP 6 AM morning briefing & property writeback.
- [[wiki/sources/akintola-steve-backend-1-million-users]] — 10-section 2026 blueprint for a backend at 1M users: scale cube, modular monolith, edge layer, stateless services, sharded polyglot DBs, multi-layer caching, observability, Outbox/Saga/idempotency, zero-trust + chaos engineering.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] — Khairallah's beginner-facing 7-step AI-automation-services playbook: niche → workflow → 5-min POC demo → 3 tiered offers ($500-$5k + retainer) → first 3 clients → templates.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — m0h's survey of 5 solo AI business models (influencer / engineer / automation / websites / micro-SaaS), each with a named receipt; unifying thesis: distribution is the moat.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — CyrilXBT's anti-breakdown Obsidian "personal OS": 3 layers (Obsidian + Claude/MCP + N8N), 8-folder vault, 1 CLAUDE.md, 5 self-running workflows.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — nateherk's portability playbook: a Claude Code project converts to Codex in one prompt because the shared markdown knowledge layer is tool-agnostic; only thin config + sub-agent format (md vs TOML) differ. Run both in parallel, hand off with a session-handoff skill. Anti-lock-in thesis.
- [[wiki/sources/rork-scale-mobile-app-50k]] — Rork's 4-step playbook to take a vibe-coded mobile app to $50k+/mo: pick one app, obsess distribution (self-content → influencers → UGC → paid ads), nail 3-act onboarding, then scale. "Building is easy, distribution is the moat."
- [[wiki/sources/leopardracer-one-person-business-2026-ai]] — fundamentals-first one-person-business-to-$1M playbook (Brand/Content/Offer) using AI as accelerator, not autonomous agent; anti-agent-hype, Eden/Dan Koe templates.
- [[wiki/sources/mattgittleson-vibecoded-b2c-375k-exit]] — non-technical solo founder's guide to vibecoding a B2C web app (CiteSure), scaling via self-made organic UGC, and exiting to Jenni AI for $375K in 6 months; distribution-is-the-moat thesis.
- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — Ahmad Osman's Part-3 guide to LLM inference engines (llama.cpp/MLX/ExLlama/vLLM/SGLang/TensorRT-LLM/Dynamo); engine follows hardware+workload+serving model; prefill-vs-decode + memory-movement-plus-scheduling thesis.
- [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]] — X-thread reframing the viral CLAUDE.md ruleset as cost-math: 3 categories (DEFAULTS/BEHAVIOR/MEMORY+STACK) = $975/week per dev; same 21 rules + Karpathy 4-rules + 65→94% as TheAIWorld22 sibling.
- [[wiki/sources/tricalt-memory-skills-same-harness]] — tricalt (Cognee/topoteretes) argues memory and skills are one "world model" harness; Cognee stores both in one graph with a self-improvement loop.
- [[wiki/sources/athletickoder-building-agents-first-principles]] — Anshuman Mishra's first-principles agent post-training walkthrough (toy text-to-diagram agent): environment → teacher trajectories → SFT (syntax) → RL/GRPO (optimization); "environment design first, algorithm selection second."
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — Akshay Pachaar's walkthrough of Hermes Agent's ~/.hermes home dir — SOUL.md identity, MEMORY/USER.md, self-evolving skills/, state.db (FTS5) tier-2 memory, cron/; names three-tier memory + GEPA.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — Charlie Hills's 6-step ladder (Install → Context → Memory → Skills → Agents → Routines) for turning Claude Code into a self-running agent system; names Claude Routines (Anthropic cloud scheduling) + Opus/Sonnet/QA-gate tiering.
- [[wiki/sources/gregisenberg-36-startup-opportunities]] — Greg Isenberg's market map of 36 startup opportunities; through-line is "reactions to AI" (loneliness, verification, analog) vs agentic-AI verticals; #2 = managed AI employees.
- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — pgGraph launch + comparison: Apache-2.0 pgrx/Rust Postgres extension compiling FK relationships into in-memory CSR for sub-50ms deep graph traversal; vs recursive CTEs & pgRouting; LDBC benchmark, ~34x less memory than Neo4j.
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]] — Alex Vacca's spine → agents → loop build-order for the AI fulfilment layer; ColdIQ worked example; two agents pay back first, the loop compounds, judgment stays human.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — the agent harness systematized: 12 components + 7 architectural decisions wrapping an LLM; "if you're not the model, you're the harness"; harness > model for production perf.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — zodchiii's verbatim repackaging of Bessemer's Shopify AI-first playbook: 6 copy-paste Claude Code patterns (LLM proxy, parallel agents, critique loops, dev MCP, lean committed CLAUDE.md, permission guardrails) across 23,000 engineers targeting ~90% autonomous coding by Q3 2026.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] — 4-step pre-establishment workflow for Claude Design (design system → templates → copy skill → build); anti-vibe-designing, token-discipline, Claude Code handoff.
- [[wiki/sources/kushwah-aaryan-future-of-work]] — historical-economics essay: AI agents collapse all business operational overhead at once, making the one-person company the default and returning to a nation of small operators; thesis behind result.dev. 36-month falsifiable predictions.
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] — manifesto thread: Claude Code mastery is system design, not prompting; 7-stage Context→Constraints→Reasoning→Execution→Validation→Memory→Refinement pipeline; execution → orchestration.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — awrigh01's market-infrastructure thesis: a 3-plane (trust/market/control), 10-layer stack for autonomous-agent marketplaces; ERC-8004 as connective trust substrate; "own identity, settlement, governance, own the marketplace."
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]] — 8-step Claude Code onboarding guide reframing it as an AI coworker; coins the "context engineering, not prompt engineering" slogan ("infrastructure for intelligence").
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — argues /goal is a cross-vendor agent primitive (prompting → assigning); Codex builds, Claude Code reviews, Hermes orchestrates + verifies; "trust the verifier, not the worker's self-report."
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] — 7 reusable Claude setups built in one weekend (CLAUDE.md / Project / Skill / 2 Connectors / daily scheduled task / model routing / /goal); 90/10 fluency rule; Gumroad funnel.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — Shruti's ~14-week free-resource AI-engineer learning path (env → fundamentals → ML → deep learning from scratch via Karpathy → LLM eng/RAG → agents/MCP → deploy+evaluate). Thesis: best AI education is already free; the scarce resource is correct order + building over consuming. Near-twin of Tech With Tim's roadmap.
- [[wiki/sources/nurijanian-goal-for-product-managers]] — /goal reframes PM work around executable definitions of done — Ralph-loop-with-product-design; "define done, prove done, keep proof outside the chat." Author behind PM OS.
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]] — 8xgrowth's 5-phase 100-day "restart to $10k/mo" via content-clipping reward campaigns (Content Rewards) + AI agents (Adaptive) that decode viral Shorts and auto-post; consumer-content cousin of the AI-services playbooks.
- [[wiki/sources/everestchris6-100m-ai-opportunity]] — opportunity-framing X-thread: the $100M AI play is automating one painful workflow for "boring" small businesses, not raising for an AI wrapper. 3 build examples (voice agent, invoicing dashboard, AI-rendered church postcards).

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
- [[wiki/sources/dnb-duns-number-outreach]] — inbound D&B sales email offering a free [[wiki/entities/d-u-n-s-number|D-U-N-S® Number]] (9-digit global business identifier, ~30 working days); document checklist + address-consistency requirements; "value-added services" upsell flagged. First business-operations source in the wiki.
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
- [[wiki/entities/dabit3]] — Nader Dabit; canonical agent-hooks reference (6 lifecycle points + operating model).
- [[wiki/entities/IBuzovskyi]] — Igor Buzovskyi; Hermes /goal v0.14 full guide.
- [[wiki/entities/itsolelehmann]] — Ole Lehmann; 4-job integration model for agents (Research / Action / Workspace / Memory); aisolo.beehiiv.com newsletter; 5th wild citation of LLM Wiki pattern.
- [[wiki/entities/VadimStrizheus]] — Vadim Strizheus; commercial Hermes use case ($10K/mo clipping pages).
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
- [[wiki/entities/shariq-quraishi]] — *(stub)* Dun & Bradstreet SAMEA rep; sent Godwin the D-U-N-S® Number outreach.
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
- [[wiki/entities/dun-and-bradstreet]] — global business-data company; issuer of the [[wiki/entities/d-u-n-s-number|D-U-N-S® Number]]. Reached out to Godwin via its SAMEA region.
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
- [[wiki/entities/d-u-n-s-number]] — Dun & Bradstreet's unique 9-digit business identifier (Data Universal Numbering System); used for global business verification and due diligence. Free standard issuance.

### SEO / lead-gen / publish tooling

- [[wiki/entities/google-business-profile]] — *(stub)* primary surface for local-SEO prompts (Sarvesh's prompts 1-8) and m0h's lead-gen 4-signals.
- [[wiki/entities/google-maps]] — *(stub)* prospect-discovery surface for AI-services lead-gen.
- [[wiki/entities/google-search-console]] — *(stub)* used in Sarvesh's prompts 10, 12, 20.
- [[wiki/entities/semrush]] — *(stub)* keyword-gap and content-gap analysis tool.
- [[wiki/entities/ahrefs]] — *(stub)* backlink audit tool.
- [[wiki/entities/instant-data-scraper]] — *(stub)* free Chrome extension for bulk-extracting tabular data; used in m0h's lead-gen workflow.
- [[wiki/entities/postiz]] — *(stub)* open-source self-hostable social scheduler; publish layer in Shann's Content OS.
- [[wiki/entities/vugola]] — AI clip-extraction + captioning. Ships MCP server (`vugola-mcp@1.3.1`) with 8 tools. Used in Vadim Strizheus's $10K/mo clipping pages stack.
- [[wiki/entities/firecrawl]] — *(stub)* agent-optimized web search; Hermes Research-job integration per Ole Lehmann.
- [[wiki/entities/bland]] — *(stub)* voice/phone-call API for agents.
- [[wiki/entities/twilio]] — *(stub)* voice + SMS + comms API; Bland alternative.
- [[wiki/entities/google-workspace]] — *(stub)* Gmail + Calendar + Drive + Docs + Sheets unified connector.
- [[wiki/entities/granola]] — *(stub)* searchable meeting transcripts; agent Memory integration.
- [[wiki/entities/devin-cli]] — *(stub)* Cognition Labs coding-agent CLI; implements lifecycle hooks.

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

### Batch backlog ingest entities (2026-06-06)

New entity pages from the 47-source backlog ingest, grouped by `entity_type`. Stubs marked *(stub)*.

**People**

- [[wiki/entities/zostaff]] — *(stub)* compiler of the 22 quant-firm open-source repos thread.
- [[wiki/entities/suryanshti777]] — *(stub)* author of the 9-Claude-Code-plugins + stop-prompting design-systems threads.
- [[wiki/entities/techwithtimm]] — Tech With Tim; author of the 2026 AI-engineer roadmap.
- [[wiki/entities/suyashkarn2]] — *(stub)* Interact Labs founder; "static website is AI's blind spot" thesis.
- [[wiki/entities/techwith-ram]] — *(stub)* author of the agentic-memory detailed breakdown.
- [[wiki/entities/petra-donka]] — Warp engineer; built Buzz; "agents need feedback loops, not perfect prompts."
- [[wiki/entities/doublenickk]] — *(stub)* author of the personal-X-agent + 14-signal algorithm thread.
- [[wiki/entities/vasuman]] — *(stub)* author of Forward Deployed Engineering 101; Varick.
- [[wiki/entities/shreyas-doshi]] — product-strategy thinker; "get to the core of the thing."
- [[wiki/entities/shabnam-774]] — *(stub)* author of the Google 2026 roadmap keynote thread.
- [[wiki/entities/retrochainer]] — *(stub)* author of the Claude/$700K Musk-tweet trading case study.
- [[wiki/entities/aniki]] — *(stub)* trader in the RetroChainer case study ($700K market-making Musk tweets).
- [[wiki/entities/elon-musk]] — *(stub)* xAI/X founder; subject of the Polymarket tweet markets.
- [[wiki/entities/nassim-taleb]] — *(stub)* origin of the barbell strategy invoked in the trading case study.
- [[wiki/entities/insomnia-vip]] — *(stub)* author of the AI-models-that-make-money thread.
- [[wiki/entities/av1dlive]] — author of the full voice-agent build guide.
- [[wiki/entities/akintola-steve]] — *(stub)* author of the 1M-user backend blueprint.
- [[wiki/entities/leopardracer]] — author of the one-person-business-2026-with-AI playbook.
- [[wiki/entities/mattgittleson]] — Matt Gittleson; vibecoded CiteSure and exited for $375K.
- [[wiki/entities/ahmad-osman]] — author of the inference-engines + local-AI-hardware guide.
- [[wiki/entities/0xdepressionn]] — *(stub)* author of the Karpathy-CLAUDE.md-as-cost-math thread.
- [[wiki/entities/tricalt]] — *(stub)* Cognee/topoteretes; "memory and skills are the same harness."
- [[wiki/entities/sarah-wooders]] — *(stub)* referenced agentic-memory researcher (Letta).
- [[wiki/entities/harrison-chase]] — *(stub)* LangChain founder; referenced in agent-harness discourse.
- [[wiki/entities/anshuman-mishra]] — author of "On Building Agents From First Principles."
- [[wiki/entities/mert-loves-ai]] — *(stub)* AI architect referenced in the agent-harness/Claude-Design discourse.
- [[wiki/entities/odyzhou]] — *(stub)* ody (@odyzhou); referenced creator.
- [[wiki/entities/charlie-hills]] — author of the 6-step full Claude Code agent system.
- [[wiki/entities/gregisenberg]] — Greg Isenberg; the 36-biggest-startup-opportunities map.
- [[wiki/entities/howard-lerman]] — *(stub)* referenced in the startup-opportunities thread.
- [[wiki/entities/josephmiclaus]] — *(stub)* Joseph Miclaus; referenced creator.
- [[wiki/entities/thomaspower]] — *(stub)* Thomas Power; referenced creator.
- [[wiki/entities/nickvasiles]] — *(stub)* Nick Vasilescu; referenced creator.
- [[wiki/entities/daleverett]] — *(stub)* author of the pgGraph "Postgres as a graph database" launch.
- [[wiki/entities/awrigh01]] — author of the 3-plane / 10-layer autonomous-agent stack thesis.
- [[wiki/entities/saboo-shubham]] — Shubham Saboo; "the ultimate guide to /goal."
- [[wiki/entities/zephyr-hg]] — Zephyr; "7 setups and one weekend" Claude-fluency thread.
- [[wiki/entities/nurijanian]] — author of "/goal for Product Managers"; PM OS.
- [[wiki/entities/8xgrowth]] — *(stub)* author of the 100-days-to-$10k content-clipping thread.
- [[wiki/entities/everestchris6]] — *(stub)* author of the $100M-AI-opportunity thread.
- [[wiki/entities/prajwal-tomar]] — author of the Claude Design workflow thread; IgnytLabs.
- [[wiki/entities/ben-ai]] — *(stub)* referenced in the Claude Design / design-system discourse.
- [[wiki/entities/kushwah-aaryan]] — *(stub)* Aaryan Kushwah; "The Future of Work" essay; result.dev.
- [[wiki/entities/riley-brown]] — referenced vibecoding/AI-app creator.
- [[wiki/entities/sajjaad-khader]] — referenced AI-app/automation creator.
- [[wiki/entities/pavlo]] — *(stub)* referenced creator.
- [[wiki/entities/marc-lou]] — *(stub)* referenced indie-hacker/micro-SaaS creator.
- [[wiki/entities/deronin]] — *(stub)* referenced creator.
- [[wiki/entities/kallaway]] — *(stub)* referenced content/personal-brand creator.
- [[wiki/entities/dan-koe]] — *(stub)* one-person-business writer; referenced in leopardracer playbook.
- [[wiki/entities/martin-kleppmann]] — *(stub)* DDIA author; referenced in backend-scalability blueprint.
- [[wiki/entities/beren-millidge]] — *(stub)* referenced in agent-post-training / RL discourse.
- [[wiki/entities/vivek-trivedy]] — *(stub)* referenced in agent-post-training discourse.
- [[wiki/entities/farhan-thawar]] — *(stub)* Shopify VP Eng; cited in the 23,000-engineers playbook.
- [[wiki/entities/mike-krieger]] — *(stub)* Anthropic CPO; referenced re Claude Design.
- [[wiki/entities/haegeon]] — *(stub)* referenced creator (Claude Design / branding).
- [[wiki/entities/ryan-singer]] — *(stub)* Shape Up author; referenced in /goal-for-PMs.
- [[wiki/entities/matt-pocock]] — *(stub)* referenced creator.
- [[wiki/entities/william-whyte]] — *(stub)* author of *The Organization Man*; referenced in Future of Work.
- [[wiki/entities/john-maynard-keynes]] — *(stub)* economist; referenced in Future of Work.
- [[wiki/entities/wassily-leontief]] — *(stub)* input-output economist; referenced in Future of Work.
- [[wiki/entities/daniel-pink]] — *(stub)* author of *Free Agent Nation*; referenced in Future of Work.
- [[wiki/entities/mlabonne]] — *(stub)* Maxime Labonne; LLM-course author referenced in AI-engineer roadmaps.
- [[wiki/entities/teknium]] — Nous Research founder; ships Hermes updates almost daily.
- [[wiki/entities/daniel-bitton]] — *(stub)* operator of Content Rewards; the clipping-economy payout platform.
- [[wiki/entities/mrbeast]] — *(stub)* YouTuber running a 1,000+ clipper army; clipping-economy market context.

**Organizations**

- [[wiki/entities/two-sigma]] — quant hedge fund; ArcticDB / flint / marbles / cook open-source.
- [[wiki/entities/man-group]] — quant asset manager; ArcticDB / dtale / notebooker / PyBloqs.
- [[wiki/entities/jane-street]] — quant trading firm; OCaml core / magic-trace / async / hardcaml.
- [[wiki/entities/d-e-shaw]] — quant hedge fund; pyflyby / pjrmi.
- [[wiki/entities/hudson-river-trading]] — HFT firm; versioned-hdf5 / nbstripout-fast.
- [[wiki/entities/optiver]] — market maker; corral / optiver-asyncpg.
- [[wiki/entities/worldquant]] — quant firm; alpha101 code / slang-server / heracles-ql / timestamp9.
- [[wiki/entities/renaissance-technologies]] — quant fund; named in the talent-vs-alpha moat thesis.
- [[wiki/entities/citadel]] — *(stub)* hedge fund; named in the closed-source-moat camp.
- [[wiki/entities/citadel-securities]] — *(stub)* market maker; Applied-AI/FDE reference.
- [[wiki/entities/bridgewater-associates]] — *(stub)* hedge fund; named in the quant thread.
- [[wiki/entities/millennium-management]] — *(stub)* multi-strat fund; named in the quant thread.
- [[wiki/entities/point72]] — *(stub)* hedge fund; named in the quant thread.
- [[wiki/entities/aqr-capital]] — *(stub)* quant fund; named in the quant thread.
- [[wiki/entities/bloomberg]] — *(stub)* financial-data platform; referenced in quant tooling.
- [[wiki/entities/quansight-labs]] — *(stub)* open-source-infra firm; referenced re ArcticDB/PyData.
- [[wiki/entities/interact-labs]] — *(stub)* SuyashKarn2's conversational-website startup.
- [[wiki/entities/salesforce]] — *(stub)* CRM/enterprise-software company.
- [[wiki/entities/salesforce-ai-research]] — *(stub)* research lab referenced in the voice-agent guide.
- [[wiki/entities/deepgram]] — *(stub)* speech-to-text provider; voice-agent stack.
- [[wiki/entities/google]] — referenced as the AI-operating-layer subject of the 2026 roadmap thread.
- [[wiki/entities/times-of-india]] — *(stub)* outlet cited in the Google roadmap thread.
- [[wiki/entities/economic-times]] — *(stub)* outlet cited in the Google roadmap thread.
- [[wiki/entities/android-central]] — *(stub)* outlet cited in the Google roadmap thread.
- [[wiki/entities/varick]] — *(stub)* Applied-AI recruiting firm behind the FDE 101 guide.
- [[wiki/entities/palantir]] — *(stub)* archetypal Forward-Deployed-Engineer firm.
- [[wiki/entities/topoteretes]] — *(stub)* maintainer org of Cognee.
- [[wiki/entities/intel]] — *(stub)* hardware vendor; OpenVINO inference path.
- [[wiki/entities/amd]] — *(stub)* GPU vendor; local-AI hardware.
- [[wiki/entities/microsoft]] — *(stub)* AutoGen maintainer; agent-framework reference.
- [[wiki/entities/jetbrains]] — *(stub)* IDE vendor; PyCharm.
- [[wiki/entities/bytebytego]] — *(stub)* system-design education brand; backend-blueprint reference.
- [[wiki/entities/highlevel]] — *(stub)* agency CRM/automation platform; AI-services reference.
- [[wiki/entities/amazon]] — *(stub)* referenced employer/FDE comparator.
- [[wiki/entities/georgia-tech]] — *(stub)* referenced credential/origin.
- [[wiki/entities/ignytlabs]] — Prajwal Tomar's studio; Claude Design workflow source.
- [[wiki/entities/jenni-ai]] — AI-writing company; acquirer of CiteSure.
- [[wiki/entities/myfitnesspal]] — *(stub)* comparator app in the vibecoded-B2C thread.
- [[wiki/entities/quizlet]] — *(stub)* comparator app in the vibecoded-B2C thread.
- [[wiki/entities/fiverr]] — *(stub)* freelance marketplace; AI-services distribution.
- [[wiki/entities/upwork]] — *(stub)* freelance marketplace; AI-services distribution.
- [[wiki/entities/acquire-marketplace]] — *(stub)* startup-acquisition marketplace.
- [[wiki/entities/flippa]] — *(stub)* website/app marketplace.
- [[wiki/entities/microns]] — *(stub)* micro-startup acquisition marketplace.
- [[wiki/entities/empire-flippers]] — *(stub)* online-business brokerage.
- [[wiki/entities/y-combinator]] — *(stub)* accelerator; referenced in opportunity framing.
- [[wiki/entities/bessemer]] — *(stub)* VC firm; author of the Shopify AI-first playbook.
- [[wiki/entities/general-motors]] — *(stub)* referenced in the Organization-Man Future-of-Work essay.
- [[wiki/entities/circle]] — *(stub)* stablecoin issuer; agent-settlement layer.
- [[wiki/entities/visa]] — *(stub)* payments network; agent-settlement layer.
- [[wiki/entities/brex]] — *(stub)* corporate-card/fintech; agent-spend reference.
- [[wiki/entities/column-bank]] — *(stub)* developer bank; agent-settlement layer.
- [[wiki/entities/cheqd]] — *(stub)* decentralized-identity network; agent-identity layer.
- [[wiki/entities/sphereon]] — *(stub)* verifiable-credentials vendor; agent-identity layer.
- [[wiki/entities/ethereum-foundation]] — *(stub)* steward of ERC-8004 / EIP-712 standards.
- [[wiki/entities/agentproof]] — *(stub)* agent-verification/attestation vendor.
- [[wiki/entities/turnkey]] — *(stub)* wallet-infrastructure vendor; agent settlement.
- [[wiki/entities/privy]] — *(stub)* embedded-wallet vendor; agent settlement.
- [[wiki/entities/fireblocks]] — *(stub)* digital-asset custody; agent settlement.
- [[wiki/entities/cordum]] — *(stub)* agent-governance/control vendor.
- [[wiki/entities/aegis-ai]] — *(stub)* agent-security/control vendor.
- [[wiki/entities/galileo-ai]] — *(stub)* Galileo Agent Control; agent-governance vendor.
- [[wiki/entities/airia]] — *(stub)* agent-governance/orchestration vendor.
- [[wiki/entities/arize]] — *(stub)* ML/agent observability vendor.
- [[wiki/entities/espressio]] — Shann Holmberg's Lisbon marketing-AI operation; stack built on Hermes Agent.
- [[wiki/entities/evokoa]] — *(stub)* GitHub owner hosting the pgGraph repository.
- [[wiki/entities/pika]] — *(stub)* company cited for the "agent eats the subscription stack" thesis.
- [[wiki/entities/whop]] — *(stub)* marketplace with a ~1M-person free clipping community; clipping-economy scale context.

**Products / tools**

- [[wiki/entities/arcticdb]] — *(stub)* Man Group/Two Sigma time-series DataFrame database.
- [[wiki/entities/dtale]] — *(stub)* Man Group visual pandas-DataFrame inspector.
- [[wiki/entities/notebooker]] — *(stub)* Man Group parametrized-notebook report runner.
- [[wiki/entities/pybloqs]] — *(stub)* Man Group composable HTML-report blocks.
- [[wiki/entities/flint]] — *(stub)* Two Sigma time-series library for Spark.
- [[wiki/entities/beakerx]] — *(stub)* Two Sigma polyglot Jupyter extensions.
- [[wiki/entities/marbles]] — *(stub)* Two Sigma open-source utility.
- [[wiki/entities/cook]] — *(stub)* Two Sigma open-source utility.
- [[wiki/entities/janestreet-core]] — *(stub)* Jane Street OCaml standard-library replacement.
- [[wiki/entities/magic-trace]] — *(stub)* Jane Street Intel-PT performance tracer.
- [[wiki/entities/janestreet-async]] — *(stub)* Jane Street OCaml async concurrency library.
- [[wiki/entities/hardcaml]] — *(stub)* Jane Street OCaml hardware-design library.
- [[wiki/entities/pyflyby]] — *(stub)* D.E. Shaw Python autoimport/productivity tools.
- [[wiki/entities/pjrmi]] — *(stub)* D.E. Shaw Python↔Java bridge.
- [[wiki/entities/versioned-hdf5]] — *(stub)* HRT versioned-HDF5 storage library.
- [[wiki/entities/nbstripout-fast]] — *(stub)* HRT fast notebook-output stripper.
- [[wiki/entities/corral]] — *(stub)* Optiver open-source tool.
- [[wiki/entities/optiver-asyncpg]] — *(stub)* Optiver async Postgres client fork/util.
- [[wiki/entities/slang-server]] — *(stub)* WorldQuant language-server tool.
- [[wiki/entities/heracles-ql]] — *(stub)* WorldQuant query-language tool.
- [[wiki/entities/timestamp9]] — *(stub)* WorldQuant nanosecond-timestamp Postgres extension.
- [[wiki/entities/apache-spark]] — *(stub)* distributed compute engine; quant data tooling.
- [[wiki/entities/jupyter]] — *(stub)* notebook environment; quant + ML tooling.
- [[wiki/entities/ocaml]] — *(stub)* functional language; Jane Street's core stack.
- [[wiki/entities/context7]] — up-to-date library-docs MCP server.
- [[wiki/entities/github-mcp]] — GitHub MCP server.
- [[wiki/entities/playwright-mcp]] — browser-automation MCP server.
- [[wiki/entities/filesystem-mcp]] — filesystem MCP server.
- [[wiki/entities/sequential-thinking-mcp]] — Sequential Thinking MCP server.
- [[wiki/entities/browser-tools-mcp]] — *(stub)* browser-tools MCP server.
- [[wiki/entities/database-mcp]] — *(stub)* database MCP server.
- [[wiki/entities/nextjs]] — Next.js React framework.
- [[wiki/entities/langchain]] — LLM application framework.
- [[wiki/entities/tailwind]] — *(stub)* utility-first CSS framework.
- [[wiki/entities/postgres]] — PostgreSQL relational database.
- [[wiki/entities/mysql]] — *(stub)* relational database.
- [[wiki/entities/sqlite]] — *(stub)* embedded relational database.
- [[wiki/entities/transformers]] — *(stub)* Hugging Face Transformers library.
- [[wiki/entities/docker-model-runner]] — *(stub)* Docker local-model runner.
- [[wiki/entities/numpy]] — *(stub)* numerical-computing library.
- [[wiki/entities/pandas]] — *(stub)* DataFrame library.
- [[wiki/entities/git]] — *(stub)* version control.
- [[wiki/entities/vs-code]] — *(stub)* code editor.
- [[wiki/entities/pycharm]] — *(stub)* Python IDE.
- [[wiki/entities/fastapi]] — *(stub)* Python async web framework.
- [[wiki/entities/docker]] — *(stub)* containerization platform.
- [[wiki/entities/kubernetes]] — *(stub)* container orchestration.
- [[wiki/entities/chatgpt]] — *(stub)* OpenAI consumer assistant.
- [[wiki/entities/chromadb]] — open-source vector database; agentic-memory store.
- [[wiki/entities/pinecone]] — *(stub)* managed vector database.
- [[wiki/entities/pgvector]] — *(stub)* Postgres vector-search extension.
- [[wiki/entities/qdrant]] — *(stub)* vector database.
- [[wiki/entities/redis]] — *(stub)* in-memory data store / cache.
- [[wiki/entities/buzz]] — Warp's self-improving community-engagement agent.
- [[wiki/entities/oz]] — Warp's agent-management/runtime surface.
- [[wiki/entities/x-corp]] — *(stub)* X platform; subject of the personal-X-agent build.
- [[wiki/entities/grok]] — *(stub)* xAI assistant.
- [[wiki/entities/telegram]] — *(stub)* messaging platform; agent approval/notify surface.
- [[wiki/entities/x-api]] — *(stub)* X posting/data API.
- [[wiki/entities/opus-4-7]] — Claude Opus 4.7 model.
- [[wiki/entities/sonnet-4-6]] — *(stub)* Claude Sonnet 4.6 model.
- [[wiki/entities/gpt-image-2]] — *(stub)* OpenAI image model.
- [[wiki/entities/kling]] — *(stub)* AI video-generation model.
- [[wiki/entities/hyperframes]] — *(stub)* AI video/animation tool.
- [[wiki/entities/max-20x]] — *(stub)* Claude Max 20x subscription tier.
- [[wiki/entities/gemini]] — *(stub)* Google's Gemini model family.
- [[wiki/entities/gemini-omni]] — *(stub)* multimodal Gemini variant.
- [[wiki/entities/gemini-3-5-flash]] — *(stub)* fast Gemini model variant.
- [[wiki/entities/gemini-spark]] — *(stub)* Gemini-powered product surface.
- [[wiki/entities/universal-cart]] — *(stub)* Google agentic-commerce cart.
- [[wiki/entities/ask-youtube]] — *(stub)* Gemini-in-YouTube feature.
- [[wiki/entities/android]] — Google's mobile OS; AI-native direction.
- [[wiki/entities/android-xr]] — Google's XR platform.
- [[wiki/entities/chrome]] — Google's browser; agentic direction.
- [[wiki/entities/youtube]] — Google video platform; AI features.
- [[wiki/entities/polymarket]] — *(stub)* prediction market; Musk-tweet trading venue.
- [[wiki/entities/claude-projects]] — Claude.ai Projects workspace feature.
- [[wiki/entities/google-calendar]] — *(stub)* calendar; personal-AI connector.
- [[wiki/entities/gpt-realtime-2]] — *(stub)* OpenAI realtime speech model; voice-agent stack.
- [[wiki/entities/voiceagentrag]] — dual-agent RAG-cache pattern/component in the voice-agent guide.
- [[wiki/entities/deepgram-flux]] — *(stub)* Deepgram streaming-STT product.
- [[wiki/entities/dataview]] — Obsidian Dataview plugin; read-not-store dashboard.
- [[wiki/entities/citus]] — *(stub)* Postgres sharding/scale-out extension.
- [[wiki/entities/cassandra]] — *(stub)* wide-column distributed database.
- [[wiki/entities/scylladb]] — *(stub)* high-performance Cassandra-compatible database.
- [[wiki/entities/dragonfly]] — *(stub)* Redis-compatible in-memory store.
- [[wiki/entities/kafka]] — *(stub)* distributed event-streaming platform.
- [[wiki/entities/pulsar]] — *(stub)* distributed messaging/streaming platform.
- [[wiki/entities/vitess]] — *(stub)* MySQL horizontal-scaling system.
- [[wiki/entities/pgbouncer]] — *(stub)* Postgres connection pooler.
- [[wiki/entities/cloudflare]] — *(stub)* edge/CDN platform.
- [[wiki/entities/fastly]] — *(stub)* edge/CDN platform.
- [[wiki/entities/prometheus]] — *(stub)* metrics/monitoring system.
- [[wiki/entities/jaeger]] — *(stub)* distributed tracing system.
- [[wiki/entities/loki]] — *(stub)* Grafana log-aggregation system.
- [[wiki/entities/grafana]] — *(stub)* observability dashboards.
- [[wiki/entities/opentelemetry]] — *(stub)* observability instrumentation standard.
- [[wiki/entities/alertmanager]] — *(stub)* Prometheus alert router.
- [[wiki/entities/pagerduty]] — *(stub)* incident-response platform.
- [[wiki/entities/k6]] — *(stub)* load-testing tool.
- [[wiki/entities/locust]] — *(stub)* load-testing tool.
- [[wiki/entities/go-language]] — *(stub)* Go programming language.
- [[wiki/entities/rust-language]] — *(stub)* Rust programming language.
- [[wiki/entities/nestjs]] — *(stub)* Node.js backend framework.
- [[wiki/entities/spring-boot]] — *(stub)* Java backend framework.
- [[wiki/entities/nodejs]] — *(stub)* JavaScript runtime.
- [[wiki/entities/python]] — *(stub)* programming language; AI-engineer stage 1.
- [[wiki/entities/vibecode]] — *(stub)* mobile-app vibecoding tool.
- [[wiki/entities/make]] — *(stub)* no-code automation platform.
- [[wiki/entities/manychat]] — *(stub)* chat-marketing automation tool.
- [[wiki/entities/rork]] — AI mobile-app builder; the $50k/mo scaling guide.
- [[wiki/entities/apple-app-store]] — *(stub)* iOS app distribution surface.
- [[wiki/entities/tiktok]] — short-video platform; UGC distribution.
- [[wiki/entities/instagram]] — social platform; UGC distribution.
- [[wiki/entities/youtube-shorts]] — *(stub)* short-video surface; clipping distribution.
- [[wiki/entities/eden]] — leopardracer's one-person-business template/product.
- [[wiki/entities/openclaw]] — *(stub)* referenced tool in the one-person-business stack.
- [[wiki/entities/citesure]] — Matt Gittleson's vibecoded B2C citation app.
- [[wiki/entities/cal-ai]] — *(stub)* AI calorie-tracking app comparator.
- [[wiki/entities/coconote]] — *(stub)* AI note-taking app comparator.
- [[wiki/entities/answers-ai]] — *(stub)* AI homework-help app comparator.
- [[wiki/entities/halo-ai]] — *(stub)* AI app comparator.
- [[wiki/entities/umax]] — *(stub)* AI looksmaxxing app comparator.
- [[wiki/entities/trustmrr]] — *(stub)* revenue-verification service for acquisitions.
- [[wiki/entities/llama-cpp]] — C/C++ LLM inference engine.
- [[wiki/entities/mlx]] — Apple-silicon ML framework.
- [[wiki/entities/mlx-lm]] — MLX LLM serving package.
- [[wiki/entities/exllamav2]] — quantized-LLM inference engine (GPU).
- [[wiki/entities/exllamav3]] — next-gen ExLlama inference engine.
- [[wiki/entities/vllm]] — high-throughput LLM serving engine (PagedAttention).
- [[wiki/entities/sglang]] — structured-generation LLM serving engine.
- [[wiki/entities/tensorrt-llm]] — NVIDIA TensorRT LLM inference engine.
- [[wiki/entities/tgi]] — Hugging Face Text Generation Inference server.
- [[wiki/entities/mlc-llm]] — cross-platform compiled LLM runtime.
- [[wiki/entities/onnx-runtime-genai]] — ONNX Runtime generative-AI inference.
- [[wiki/entities/openvino]] — Intel inference toolkit.
- [[wiki/entities/lmdeploy]] — *(stub)* LLM deployment/serving toolkit.
- [[wiki/entities/nvidia-dynamo]] — *(stub)* NVIDIA disaggregated-serving framework.
- [[wiki/entities/lm-studio]] — *(stub)* local-LLM desktop runner.
- [[wiki/entities/harbor]] — *(stub)* local-AI stack orchestrator.
- [[wiki/entities/tabbyapi]] — *(stub)* ExLlama-backed OpenAI-compatible server.
- [[wiki/entities/cognee]] — open-source memory+skills graph "world model" layer.
- [[wiki/entities/trl]] — *(stub)* Hugging Face RL/SFT training library.
- [[wiki/entities/unsloth]] — *(stub)* fast LLM fine-tuning library.
- [[wiki/entities/prime-rl]] — *(stub)* distributed RL training framework.
- [[wiki/entities/verl]] — *(stub)* volcano-engine RL training framework.
- [[wiki/entities/openrlhf]] — *(stub)* RLHF training framework.
- [[wiki/entities/tldraw]] — *(stub)* canvas/diagram library; agent text-to-diagram target.
- [[wiki/entities/qwen]] — open-weight LLM family; agent post-training base model.
- [[wiki/entities/pydantic]] — Python data-validation library; structured outputs.
- [[wiki/entities/claude-routines]] — *(stub)* Anthropic cloud-scheduled agent runs.
- [[wiki/entities/pggraph]] — Apache-2.0 pgrx/Rust Postgres graph-traversal extension.
- [[wiki/entities/pgrouting]] — Postgres routing/graph extension; pgGraph comparator.
- [[wiki/entities/postgis]] — *(stub)* Postgres spatial extension.
- [[wiki/entities/neo4j]] — *(stub)* native graph database; pgGraph comparator.
- [[wiki/entities/pgrx]] — *(stub)* Rust framework for Postgres extensions.
- [[wiki/entities/attio]] — *(stub)* modern CRM; AI-fulfilment-layer reference.
- [[wiki/entities/clay-com]] — *(stub)* GTM data-enrichment platform.
- [[wiki/entities/wiza]] — *(stub)* B2B contact-enrichment tool.
- [[wiki/entities/fullenrich]] — *(stub)* waterfall contact-enrichment tool.
- [[wiki/entities/prospeo]] — *(stub)* email-finder/enrichment tool.
- [[wiki/entities/instantly]] — *(stub)* cold-email sending platform.
- [[wiki/entities/predictleads]] — *(stub)* buying-signal data provider.
- [[wiki/entities/common-room]] — *(stub)* community-signal intelligence platform.
- [[wiki/entities/apollo]] — *(stub)* B2B sales-data/outreach platform.
- [[wiki/entities/autogen]] — Microsoft multi-agent framework.
- [[wiki/entities/deep-agents]] — *(stub)* LangChain deep-agents pattern/library.
- [[wiki/entities/manus]] — *(stub)* autonomous general-purpose agent product.
- [[wiki/entities/github-copilot]] — *(stub)* AI pair-programmer; Shopify-playbook comparator.
- [[wiki/entities/shopify-dev-mcp]] — Shopify dev MCP server.
- [[wiki/entities/ruby-on-rails]] — *(stub)* web framework; Shopify stack.
- [[wiki/entities/sorbet]] — *(stub)* Ruby type checker; Shopify stack.
- [[wiki/entities/dribbble]] — *(stub)* design-inspiration platform.
- [[wiki/entities/behance]] — *(stub)* design-portfolio platform.
- [[wiki/entities/result-dev]] — *(stub)* Aaryan Kushwah's one-person-company product.
- [[wiki/entities/whatsapp]] — *(stub)* messaging platform; agent surface.
- [[wiki/entities/midjourney]] — *(stub)* AI image generator.
- [[wiki/entities/erc-8004]] — Ethereum agent-trust standard (identity/reputation/validation).
- [[wiki/entities/a2a-protocol]] — *(stub)* agent-to-agent communication protocol.
- [[wiki/entities/eip-712]] — *(stub)* typed-structured-data signing standard.
- [[wiki/entities/metamask]] — *(stub)* Ethereum wallet; agent-settlement reference.
- [[wiki/entities/safe-wallet]] — *(stub)* Safe smart-account wallet; agent settlement.
- [[wiki/entities/assury-enforce]] — *(stub)* agent-policy enforcement product.
- [[wiki/entities/policylayer]] — *(stub)* agent-governance policy product.
- [[wiki/entities/complyedge]] — *(stub)* AI-compliance product.
- [[wiki/entities/modal]] — *(stub)* serverless compute/sandbox platform.
- [[wiki/entities/e2b]] — *(stub)* agent code-execution sandbox.
- [[wiki/entities/daytona]] — *(stub)* dev-environment/sandbox platform.
- [[wiki/entities/mem0]] — *(stub)* agent-memory layer.
- [[wiki/entities/letta]] — *(stub)* agent-memory framework (MemGPT lineage).
- [[wiki/entities/zep]] — *(stub)* agent-memory / temporal-knowledge-graph store.
- [[wiki/entities/langfuse]] — *(stub)* LLM observability/eval platform.
- [[wiki/entities/helicone]] — *(stub)* LLM observability/proxy.
- [[wiki/entities/braintrust]] — *(stub)* LLM eval platform.
- [[wiki/entities/langsmith]] — *(stub)* LangChain tracing/eval platform.
- [[wiki/entities/google-adk]] — *(stub)* Google Agent Development Kit.
- [[wiki/entities/kleros]] — *(stub)* decentralized dispute-resolution protocol.
- [[wiki/entities/gumroad]] — *(stub)* digital-product sales platform; creator funnels.
- [[wiki/entities/coursera]] — *(stub)* online-course platform; AI-engineer resources.
- [[wiki/entities/lancedb]] — *(stub)* embedded vector database.
- [[wiki/entities/gradio]] — *(stub)* ML demo-UI framework.
- [[wiki/entities/streamlit]] — *(stub)* data-app framework.
- [[wiki/entities/hugging-face-spaces]] — *(stub)* hosted ML-app platform.
- [[wiki/entities/deepeval]] — *(stub)* LLM evaluation framework.
- [[wiki/entities/ragas]] — *(stub)* RAG evaluation framework.
- [[wiki/entities/lora]] — *(stub)* low-rank adaptation fine-tuning method/tooling.
- [[wiki/entities/qlora]] — *(stub)* quantized LoRA fine-tuning method/tooling.
- [[wiki/entities/pm-os]] — nurijanian's PM operating-system product.
- [[wiki/entities/content-rewards]] — *(stub)* creator content-clipping reward platform.
- [[wiki/entities/adaptive-ai]] — *(stub)* Adaptive; AI auto-posting/clipping agent.
- [[wiki/entities/claude]] — Anthropic's assistant; referenced throughout the batch.

**Works**

- [[wiki/entities/worldquant-alpha101-code]] — *(stub)* WorldQuant 101 Formulaic Alphas reference code.
- [[wiki/entities/generative-agents]] — *(stub)* Park et al. (2023) generative-agents paper; episodic-memory ancestor.
- [[wiki/entities/x-algorithm-repo]] — *(stub)* claimed xai-org/x-algorithm For-You-feed repository.
- [[wiki/entities/ldbc-social-network-benchmark]] — *(stub)* graph-DB benchmark used in the pgGraph comparison.
- [[wiki/entities/free-agent-nation]] — *(stub)* Daniel Pink book; referenced in Future of Work.
- [[wiki/entities/claude-mastery]] — *(stub)* Zephyr's Gumroad Claude-fluency product/guide.
- [[wiki/entities/tally]] — *(stub)* fictional brand built end-to-end as a Claude Design demo.

**Other**

- [[wiki/entities/kano-model]] — *(stub)* product-prioritization framework; Shreyas product-strategy reference.
- [[wiki/entities/gepa]] — *(stub)* named optimization method (Akshay Pachaar's Hermes deep-dive); not yet explained.
- [[wiki/entities/meta-platforms]] — *(stub)* Meta (Facebook/Instagram parent); paid-ads + UGC distribution.
- [[wiki/entities/eu-ai-act]] — *(stub)* EU AI regulation; agent-governance/compliance reference.
- [[wiki/entities/atonomi]] — *(stub)* referenced org/protocol in the autonomous-agent stack.

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
- [[wiki/concepts/cross-env-publishing-infrastructure]] — *(new 2026-06-08)* Ed25519-signed manifest envelopes + 2-person approval + atomic upsert with stable codes + nonce replay protection + audit log; pattern for safely propagating shared content across environments. Worked example: Kivora's W2-W5 + Phase A-D rollouts.
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
- [[wiki/concepts/multi-agent-delegation-with-verifier]] — *(new 2026-06-08)* one persona synchronously delegates to specialized personas; an independent Verifier persona gates destructive side-effects with its own context. Separates "who decides" from "who confirms safe to do." Worked example: Kivora's Compass + Pulse + Autopilot + Verifier souls package.
- [[wiki/concepts/progressive-disclosure]] — load metadata first, content on demand.
- [[wiki/concepts/reasoning-execution-split]] — LLM reasons; deterministic code executes.
- [[wiki/concepts/reliability-decay-math]] — chained-probability problem that motivates separation-of-concerns architectures.
- [[wiki/concepts/helpful-assistant-theater]] — *(new 2026-07-22)* weak-model failure mode: agent narrates confident progress while invoking zero tools. Fix is model-tier + anti-fabrication instructions. From Helm's gpt-4o-mini incident.

### Integration & data layer

- [[wiki/concepts/hybrid-rag-retrieval]] — *(new 2026-06-08)* BM25 + dense vector candidate generation merged via Reciprocal Rank Fusion + cross-encoder reranker for the final top-N. Higher precision than single-method retrieval. Worked example: Kivora's Phase 2 Wave 3 RAG layer.
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

### Batch backlog ingest concepts (2026-06-06)

New concept pages from the 47-source backlog ingest, alphabetical. Stubs marked *(stub)*.

- [[wiki/concepts/abstraction-altitude-framing]] — refusing high-altitude product binaries; the real question is one level down.
- [[wiki/concepts/agent-evals]] — systematic evaluation of agent behavior; FDE deployment lifecycle pillar.
- [[wiki/concepts/agent-feedback-loop]] — closing the loop on agent behavior beats perfecting the prompt.
- [[wiki/concepts/agent-governance]] — control/policy plane for autonomous agents.
- [[wiki/concepts/agent-guardrails]] — safety constraints/checkpoints in agent execution.
- [[wiki/concepts/agent-harness]] — the 12-component, 7-decision scaffolding wrapping an LLM; "if you're not the model, you're the harness."
- [[wiki/concepts/agent-identity]] — Know-Your-Agent: verifiable agent identity in agentic markets.
- [[wiki/concepts/agent-post-training]] — environment → teacher trajectories → SFT → RL pipeline for agents.
- [[wiki/concepts/agent-reputation]] — on-chain/verifiable agent reputation layer.
- [[wiki/concepts/agent-settlement]] — payments/settlement rails for autonomous agents.
- [[wiki/concepts/agent-skills]] — *(stub)* reusable packaged agent workflows (e.g. `/grill-me`, `/shaping`) invoked as commands.
- [[wiki/concepts/agent-stack]] — *(stub)* 3-plane / 10-layer market infrastructure agents need to transact (trust / market / control).
- [[wiki/concepts/agent-verification]] — trust-the-verifier-not-the-worker's-self-report.
- [[wiki/concepts/agentic-ai]] — *(stub)* AI that reads situations and takes actions vs fixed automation.
- [[wiki/concepts/agentic-capital-markets]] — market infrastructure for autonomous-agent economies.
- [[wiki/concepts/agentic-memory]] — continuity/context/learning across 4 memory types; "20% storage, 80% retrieval."
- [[wiki/concepts/ai-as-infrastructure]] — *(stub)* AI as a substrate layer rather than a feature.
- [[wiki/concepts/ai-automation-agency]] — *(stub)* services model: automate one painful workflow for a "boring" small business and charge for it.
- [[wiki/concepts/ai-compliance]] — regulatory/audit posture for AI agents (EU AI Act etc.).
- [[wiki/concepts/ai-coworker]] — *(stub)* reframing Claude Code from tool to coworker.
- [[wiki/concepts/ai-engineer]] — the AI-engineer career path (roadmap target).
- [[wiki/concepts/ai-engineering]] — discipline of building LLM-powered systems; "still software engineering."
- [[wiki/concepts/ai-fulfillment-layer]] — spine → agents → loop build-order for services-as-software delivery.
- [[wiki/concepts/ai-influencer]] — monetizable AI/virtual-persona accounts.
- [[wiki/concepts/ai-native-os]] — *(stub)* operating systems rebuilt around AI as the operating layer.
- [[wiki/concepts/ai-overhang]] — *(stub)* AI-capability arbitrage window before adoption catches up.
- [[wiki/concepts/answer-engine-discovery]] — discovery moving from search to AI answer engines.
- [[wiki/concepts/backend-scalability-blueprint]] — 10-section 2026 blueprint for a backend at 1M users.
- [[wiki/concepts/barbell-strategy]] — *(stub)* Taleb safe-core + tail-bet allocation; the trading case study.
- [[wiki/concepts/chaos-engineering]] — deliberately injecting failure to validate resilience.
- [[wiki/concepts/claude-as-infrastructure]] — *(stub)* Claude used as build/runtime infrastructure, not chat.
- [[wiki/concepts/claude-fluency]] — practical mastery via a small set of reusable setups.
- [[wiki/concepts/claude-memory]] — Claude.ai persistent-memory feature.
- [[wiki/concepts/claude-projects]] — Claude.ai Projects as a knowledge/workspace primitive.
- [[wiki/concepts/competitive-moat]] — *(stub)* talent-vs-alpha framing of open vs closed source.
- [[wiki/concepts/compounding-judgement]] — *(stub)* human judgment compounding as agents take routine work.
- [[wiki/concepts/content-clipping]] — *(stub)* the content-clipping reward economy.
- [[wiki/concepts/content-os]] — *(stub)* systematized content-production operating system.
- [[wiki/concepts/content-waterfall]] — one long-form piece cascaded into many short-form posts.
- [[wiki/concepts/context-engineering]] — designing the agent's context as infrastructure; "not prompt engineering."
- [[wiki/concepts/context-management]] — *(stub)* managing what enters/leaves the context window.
- [[wiki/concepts/context-rot]] — degradation of long contexts; motivates context management.
- [[wiki/concepts/context-window]] — the model's working-context budget.
- [[wiki/concepts/continuous-batching]] — *(stub)* request-batching throughput technique in LLM serving.
- [[wiki/concepts/conversation-design]] — designing turn-taking/flows for voice + chat agents.
- [[wiki/concepts/conversational-website]] — generative interface replacing the static website.
- [[wiki/concepts/conversion-funnel]] — staged distribution → activation → conversion model.
- [[wiki/concepts/cosine-similarity]] — *(stub)* vector-similarity measure for retrieval.
- [[wiki/concepts/customer-avatar]] — sharply-defined target customer for offers/content.
- [[wiki/concepts/customer-insight]] — *(stub)* grounding product bets in real customer understanding.
- [[wiki/concepts/daily-ai-briefing]] — scheduled morning briefing generated by Claude/MCP over the vault.
- [[wiki/concepts/data-flywheel]] — *(stub)* usage → data → better product → more usage loop.
- [[wiki/concepts/data-moat]] — *(stub)* proprietary data as defensibility.
- [[wiki/concepts/database-sharding]] — horizontal partitioning of data across nodes.
- [[wiki/concepts/design-system]] — token/component foundation established before generation.
- [[wiki/concepts/distribution-as-moat]] — distribution, not building, is the defensible advantage.
- [[wiki/concepts/dual-agent-rag-cache]] — VoiceAgentRAG two-agent retrieval cache for latency.
- [[wiki/concepts/embeddings]] — vector representations of text; retrieval/memory foundation.
- [[wiki/concepts/environment-design]] — RL environment design first, algorithm second.
- [[wiki/concepts/episodic-memory]] — event/experience memory; one of the 4 agentic-memory types.
- [[wiki/concepts/evaluator-optimizer]] — *(stub)* self-critique loop where the agent generates, critiques, and revises ("argue with itself").
- [[wiki/concepts/executable-definition-of-done]] — defining + proving "done" outside the chat.
- [[wiki/concepts/extended-thinking]] — Claude's extended-thinking/reasoning mode.
- [[wiki/concepts/external-memory]] — out-of-context stored memory; one of the 4 agentic-memory types.
- [[wiki/concepts/fine-tuning]] — adapting a base model to a task/domain.
- [[wiki/concepts/firm-as-variable]] — the firm's size/existence as an economic variable that AI shrinks.
- [[wiki/concepts/format-first-product-ideation]] — designing the content/product format before the idea.
- [[wiki/concepts/forward-deployed-engineering]] — the FDE role: audit → evals → deployment with the customer.
- [[wiki/concepts/four-golden-signals]] — latency/traffic/errors/saturation observability signals.
- [[wiki/concepts/function-calling]] — LLMs invoking typed tools/functions.
- [[wiki/concepts/gepa]] — *(stub)* GEPA prompt/skill optimization.
- [[wiki/concepts/goal-command]] — /goal as a cross-vendor "assign, don't prompt" agent primitive.
- [[wiki/concepts/graph-traversal]] — deep relationship traversal; pgGraph CSR in-memory approach.
- [[wiki/concepts/grpo]] — Group Relative Policy Optimization for agent RL.
- [[wiki/concepts/harness-engineering]] — *(stub)* engineering the harness around the model.
- [[wiki/concepts/human-in-the-loop]] — human review/approval gates in agent loops.
- [[wiki/concepts/idempotency-keys]] — safe-retry keys preventing duplicate side effects.
- [[wiki/concepts/in-context-memory]] — memory held in the prompt/context; one of the 4 types.
- [[wiki/concepts/inference-engine]] — the runtime that serves an LLM; engine follows hardware+workload.
- [[wiki/concepts/interface-layer]] — *(stub)* control of the interface as the real strategic contest.
- [[wiki/concepts/kelly-criterion]] — *(stub)* optimal bet-sizing; the trading case study.
- [[wiki/concepts/kv-cache]] — attention key/value cache; central to decode-phase serving.
- [[wiki/concepts/latency-budget]] — the ~700ms end-to-end budget for real-time voice agents.
- [[wiki/concepts/lifestyle-business]] — small, profitable, owner-operated business model.
- [[wiki/concepts/llm-evaluation]] — measuring LLM/agent output quality.
- [[wiki/concepts/llm-proxy]] — central LLM-routing proxy (Shopify-playbook pattern).
- [[wiki/concepts/llm-serving-benchmarking]] — *(stub)* measuring throughput/latency across serving engines.
- [[wiki/concepts/llmops]] — operating LLM systems in production.
- [[wiki/concepts/local-ai]] — *(stub)* self-hosting LLM inference on local hardware; pick hardware + workload first, engine follows.
- [[wiki/concepts/market-making]] — *(stub)* providing two-sided liquidity; the Polymarket case study.
- [[wiki/concepts/memory-bandwidth]] — the binding constraint in LLM decode; hardware selection driver.
- [[wiki/concepts/memory-consolidation]] — decay/importance/consolidation of agentic memories.
- [[wiki/concepts/micro-saas]] — small, focused, solo-run SaaS business model.
- [[wiki/concepts/mixture-of-experts]] — *(stub)* MoE architecture; serving implications.
- [[wiki/concepts/mobile-app-distribution]] — self-content → influencers → UGC → paid-ads ladder.
- [[wiki/concepts/multi-layer-caching]] — layered client/edge/app/DB caching strategy.
- [[wiki/concepts/multimodal-ai]] — *(stub)* models spanning text/image/audio/video.
- [[wiki/concepts/observability]] — metrics + traces + logs for production systems.
- [[wiki/concepts/offer-creation]] — designing tiered, outcome-priced offers.
- [[wiki/concepts/onboarding-as-conversion]] — 3-act onboarding as the primary conversion lever.
- [[wiki/concepts/one-person-company]] — the AI-enabled one-person company as the default firm shape.
- [[wiki/concepts/open-source-as-recruiting]] — *(stub)* open-sourcing tooling to win talent.
- [[wiki/concepts/operational-overhead-collapse]] — AI collapsing all business operational overhead at once.
- [[wiki/concepts/organic-ugc-engine]] — founder-made organic UGC as the growth engine.
- [[wiki/concepts/organization-man]] — Whyte's mid-century corporate archetype the essay inverts.
- [[wiki/concepts/outbox-pattern]] — transactional outbox for reliable event publishing.
- [[wiki/concepts/paged-attention]] — vLLM's paged KV-cache memory management.
- [[wiki/concepts/parametric-memory]] — knowledge baked into weights; one of the 4 memory types.
- [[wiki/concepts/persistent-memory]] — *(stub)* memory surviving across sessions.
- [[wiki/concepts/persona-consistency]] — *(stub)* keeping an AI persona consistent across content.
- [[wiki/concepts/personal-ai-system]] — layered persistent personal Claude setup.
- [[wiki/concepts/personal-brand]] — distribution asset built around the individual.
- [[wiki/concepts/postgres-as-platform]] — extending Postgres to absorb adjacent workloads (graph, vector).
- [[wiki/concepts/prediction-markets]] — *(stub)* event-outcome markets (Polymarket).
- [[wiki/concepts/prefill-vs-decode]] — the two LLM-inference phases with different bottlenecks.
- [[wiki/concepts/principles-over-rules]] — give agents principles, not brittle rule lists.
- [[wiki/concepts/product-differentiation]] — *(stub)* differentiating on specific feature bets.
- [[wiki/concepts/product-strategy]] — specific bets on specific features grounded in insight.
- [[wiki/concepts/prompt-engineering]] — crafting prompts; framed as subordinate to context engineering.
- [[wiki/concepts/proof-of-authority]] — verifiable agent legal/acting authority.
- [[wiki/concepts/properties-as-metadata]] — Obsidian properties written back as queryable metadata.
- [[wiki/concepts/quantization]] — reducing weight precision to fit/serve models locally.
- [[wiki/concepts/ralph-loop]] — autonomous build-verify loop; /goal-with-product-design variant.
- [[wiki/concepts/ralph-wiggum-loop]] — the canonical Ralph (Wiggum) autonomous loop.
- [[wiki/concepts/reactions-to-ai-opportunities]] — the "reactions to AI" (loneliness/verification/analog) opportunity pattern.
- [[wiki/concepts/read-not-store-dashboard]] — Dataview live-query dashboard that reads rather than stores state.
- [[wiki/concepts/recommendation-algorithm]] — X For-You-feed 14-signal weighted-sum scoring model.
- [[wiki/concepts/reward-hacking]] — agents exploiting reward specs; RL failure mode.
- [[wiki/concepts/rlvr]] — RL with verifiable rewards / verifiers.
- [[wiki/concepts/saga-pattern]] — distributed-transaction orchestration via compensating steps.
- [[wiki/concepts/scaffolded-llm]] — an LLM wrapped in tools/loops/state (the harness view).
- [[wiki/concepts/scale-cube]] — x/y/z-axis scaling model for backends.
- [[wiki/concepts/selling-websites]] — AI-built local-business web-agency model.
- [[wiki/concepts/self-evolving-skills]] — skills the agent writes/improves for itself.
- [[wiki/concepts/self-hosted-llm]] — running open-weight LLMs on owned hardware.
- [[wiki/concepts/sequential-thinking]] — *(stub)* step-wise structured reasoning (MCP server).
- [[wiki/concepts/skills-as-code]] — agent skills shipped as reviewed code/PRs.
- [[wiki/concepts/soul-md]] — SOUL.md agent-identity file in ~/.hermes.
- [[wiki/concepts/specific-bets]] — *(stub)* concrete feature-level bets vs high-altitude binaries.
- [[wiki/concepts/speculative-decoding]] — *(stub)* draft-model speedup for decode.
- [[wiki/concepts/state-machine]] — explicit states for conversation/agent control flow.
- [[wiki/concepts/stateless-services]] — externalizing state so services scale horizontally.
- [[wiki/concepts/strategic-acquisition]] — building to be acquired; the CiteSure → Jenni exit.
- [[wiki/concepts/supervised-fine-tuning]] — SFT to teach an agent task syntax/format.
- [[wiki/concepts/teacher-trajectories]] — teacher-model rollouts used as SFT training data.
- [[wiki/concepts/tensor-parallelism]] — *(stub)* sharding a model across GPUs for serving.
- [[wiki/concepts/three-tier-memory]] — Hermes-style in-context / state.db / files memory tiers.
- [[wiki/concepts/time-series-data-engineering]] — *(stub)* time-series storage/compute; quant tooling.
- [[wiki/concepts/tool-scoping]] — restricting an agent's tool set to what the task needs.
- [[wiki/concepts/trading-bot]] — 24/7 API-connected automation that executes a trading strategy at scale; the product, not a shortcut.
- [[wiki/concepts/ugc-marketing]] — user/founder-generated content as a marketing channel.
- [[wiki/concepts/unified-memory]] — shared CPU/GPU memory (Apple silicon) for local inference.
- [[wiki/concepts/vector-database]] — store/query embeddings; memory + RAG substrate.
- [[wiki/concepts/verification-loops]] — *(stub)* verify-before-trust loops in agent workflows.
- [[wiki/concepts/vibe-coding]] — *(stub)* building software by prompting rather than hand-coding.
- [[wiki/concepts/vibe-designing]] — designing by vibes without a system; the anti-pattern.
- [[wiki/concepts/viral-content-system]] — repeatable system for producing viral short-form content.
- [[wiki/concepts/voice-agent]] — real-time five-component STT/RAG/LLM/TTS/functions pipeline.
- [[wiki/concepts/voice-matching]] — making an agent post/write in the user's own voice.
- [[wiki/concepts/voice-style-guide]] — captured voice/style guide driving voice-matched output.
- [[wiki/concepts/workflow-design]] — Context→Constraints→Reasoning→Execution→Validation→Memory→Refinement pipeline.
- [[wiki/concepts/world-model]] — *(stub)* unified memory+skills "world model" harness.
- [[wiki/concepts/zero-trust-security]] — never-trust-always-verify security posture.

## Projects

Add a project from inside its directory with `/brain-add-project` in any Claude Code session. Pages live at `wiki/projects/<slug>.md` and group here by status.

### Active

> **Affiliation key**: 🏢 = ROAM Labs owned product · ⚙️ = ROAM Labs internal tool · 🤝 = ROAM Labs client work · 🛡️ = Brolly Africa owned platform · 🌂 = Brolly Africa client work · 🏛️ = SoftTech subcontract / government · 📣 = ROAM Labs corporate self. See [[wiki/syntheses/godwin-portfolio]] for the full landscape.

- 🏢 [[wiki/projects/africart]] — *(ROAM Labs owned product — pre-implementation as of 2026-05-30; design spec + pitch PDF exist, no code yet)* **Instacart-style marketplace** aggregating existing Houston African-owned grocery stores under a unified canonical-product catalog with **split-fulfillment multi-store carts** (one cart → N suborders → N stores → N Uber Direct deliveries); Africart as **merchant of record** via Stripe Connect Standard (Texas marketplace facilitator law makes Africart responsible for sales tax remittance, not stores); **store staff picks** (not independent shoppers); **Uber Direct API** for delivery in v1, owned driver network deferred to Phase 2; **three customer surfaces** (Expo RN iOS+Android + Next.js 15 web + Twilio WhatsApp bot) on a single **NestJS modular monolith** with 9 bounded-context modules; catalog built by **field team + AI-assisted normalization** (Claude vision drafts entries from store-shelf photos); **daily availability + per-order confirm/substitute** for inventory accuracy (no POS integration). v1 scope: 3–5 pilot stores in Houston, ~20-week timeline for 2–4 engineers; Phase 2 (deliberately deferred): source produce in Africa + operate as vertically integrated importer. 12 architecture decisions locked + 9 open questions (sales-tax CPA, service-fee structure, pilot store identities, legal entity, lawyer + insurance engagements) captured in 2026-05-29 design spec at `docs/superpowers/specs/2026-05-29-africart-marketplace-design.md`.
- 🌂 [[wiki/projects/asanti-brokers]] — *(Brolly Africa client work)* marketing website for *Asanti Brokers Limited*, a Ghana NIC-registered insurance brokerage; Next.js 16 App Router + React 19 + Tailwind v4 static-shaped site with one route per product line (motor / property / business-liability / fire & perils / marine cargo / travel / personal accident / group employee benefits); WhatsApp CTA + cookie consent + NIC trust badge; deployed at `asanti.insure` on Vercel.
- 🛡️ [[wiki/projects/brolly]] — *(Brolly Africa owned platform)* African insurtech / digital-insurance platform (Brolly Africa) with vehicle-insurance roots in the Bolt-driver market; multi-repo workspace at `~/Brolly` holding a JHipster 7.5 Spring Boot backend (`backend-service`) being rewritten in Kotlin + Spring Boot 3.5 (`core-backend`), a React 18 admin dashboard (`admin-portal`), a Next.js 13 customer portal (`customer-portal`), a fresh Vite / React 19 landing (`landing-page`), and a shared `insurtech-platform` UI template; Azure Postgres + PayStack + AWS S3; canonical repos on GitHub `Brolly-Africa/`, legacy mirrors on GitLab `brolly1/`.
- 🏢 [[wiki/projects/clarvyn]] — *(ROAM Labs owned product)* AI-first HR platform for startup founders; the Claude agent *is* the HR department (proactive payroll, reviews, hiring, employee 1:1s). Five-service stack: Spring Boot 3.3.5 HRIS + FastAPI Claude agent (Sonnet+Haiku, pgvector RAG, MCP layer) + React 19 portal + React Native / Expo 54 mobile + landing. Wave 6 (Slack bot, MCP, proactive Expo Push, Integrations UI) shipped week of 2026-05-09.
- 🤝 [[wiki/projects/coffee-break-with-big-sis]] — *(ROAM Labs client work)* multi-tenant networking + mentorship SaaS for institutions (universities, alumni chapters, professional bodies); schema-per-tenant Spring Boot 3.4 / Java 17 backend + React 19 / Vite 7 / Tailwind v4 frontend; weighted-Jaccard mentor↔mentee matching across 6 dimensions. Editorial Café Zine redesign of landing + 3 auth pages shipped 2026-04-11.
- 🏛️ [[wiki/projects/cpc-rtbvd]] — *(SoftTech subcontract; ROAM delivers)* bid-stage React 19 + Tailwind v4 dashboard prototype + full QCBS bid package for the **Cocoa Processing Company Plc** "Real-Time Business Visibility" tender (RFP CPC/PRO/CS/1/26, deadline 8 Apr 2026); GHS 2.98M firm 12-week build for SoftTech Solutions; no VAT, no maintenance, no training scope (handover model); 4 named Key Experts (Godwin/Lilian/Richmond/Christian); bid finalized 2026-05-09 awaiting CPC award.
- 🏢 [[wiki/projects/glydr]] — *(ROAM Labs owned product — Phase 2 wiring complete 2026-05-11; brand name "Glydr" working only)* peer-to-peer **Point-A-to-Point-B carpooling** for Ghana with **dual pilot** (Accra ↔ Kumasi weekend trips + in-Accra commute — landing now diverges from PRD §3.3 which lists in-Accra as Year-1 non-goal); cost-sharing legal positioning (driver counts as occupant who pays own per-seat share, structurally not commercial transport); **multi-repo wrapper** (`github.com/kobbyopoku/{glydr_backend, glydr_landing, glydr_cc, glydr_mobile}`) — workspace folder at `~/ROAM/CascadeProjects/glydr` holds PRD + docs + infra; Flutter mobile (Android-first, scaffold only) + Spring Boot 3.5 / Java 21 backend + two Next.js 16 surfaces (`landing/` + `control-center/` operator console). **What's wired**: KYC manual approval flow end-to-end (R2 + LocalFS fallback, JWT operator auth, 14/14 backend tests), control-center Phase 2 (queue + detail + decision form against real backend, document proxy for LocalFS), landing waitlist → backend POST /v1/waitlist (idempotent on phone+source). Planned integrations Flutterwave (payments) + [[wiki/projects/brolly|Brolly Africa]] (per-trip insurance — doubles as anti-leakage moat) + Smile Identity (KYC, V1) + Resend (email — wired, env-gated) + mnotify (SMS, **replaces Hubtel from PRD §11.4** — wired, env-gated) + Google Maps. **Brand**: Quiet Corridor (Corridor Green primary, Sunrise Amber accent, Plus Jakarta + Inter + JetBrains Mono trio, no shadows discipline, Open Design 9-section DESIGN.md at `landing/DESIGN.md`). Closes PRD §16 Q6 (Java) + Q7 (R2) + Q9 (design system for landing/CC). Open: corporate structure (Q1), driver auth shape, workspace-shape (Q13 new), PRD divergence (Q14 new).
- ⚙️ [[wiki/projects/helm]] — *(ROAM Labs internal tool — 5 feature slices shipped on `feat/agents`; build active 2026-06-26)* multi-agent ops platform automating GTM + business operations across all ROAM products + client work. Single user (Godwin); [[wiki/entities/hermes-agent|Hermes Agent]] runtime (topology B — standalone container + per-agent `HERMES_HOME`); **multi-repo wrapper**, 4 repos now pushed to `github.com/godwin-roam/{helm-backend, helm-portal, helm-mcp, helm-docs}` (not the originally-planned `ROAM-Labs` org); FastAPI + SQLAlchemy 2.0 async on Railway + Next.js/React 19 + shadcn/ui on Vercel + PostgreSQL + pgvector; **pivoted from the fixed 6-agent GTM roster to a generic `Org → Workspace → Agents` platform** with UI-driven agent creation (AI Studio shell + playground), task execution engine + scheduling; one blocker — OpenRouter 402 (no credits) gates live runs; reusable blueprint at [[wiki/syntheses/multi-agent-ops-platform-blueprint]]; commercialization decision at [[wiki/syntheses/helm-commercialization-paths]] (internal-only for v1).
- 🏢 [[wiki/projects/kivora]] — *(ROAM Labs owned product; brand: ROAM GRC)* AI-powered multi-tenant SaaS GRC platform (product name **ROAM GRC**); 13-module Spring Boot backend + React/Vite frontend + FastAPI Claude agent with pgvector RAG; named as Vedge's GRC of record. **Tier 1 Finding-schema migration** shipped 2026-05-08 behind a toggle (worked example of [[wiki/concepts/dual-write-rollout]]); **Systems Inventory v1** shipped 2026-05-16/17 — 7 waves end-to-end via autonomous /loop, all merged to `main`.
- 📣 [[wiki/projects/roamlabs]] — *(ROAM Labs corporate self)* corporate marketing site for the **_roamlabs** AI agency (sister brand to ROAM GRC / Vedge under the **ROAM** umbrella); single Next.js 14 App Router site with custom NeuralNetwork canvas hero. Visual direction unsettled — editorial-quarterly and mission-control aesthetics both prototyped + reverted on 2026-05-09.
- 🤝 [[wiki/projects/stacesprouts]] — *(ROAM Labs client work)* omni-channel commerce platform (storefront + admin + Flutter POS) for a Ghana baby/kids fashion retailer; Spring Boot + React 19 + Flutter; mirrors [[wiki/projects/vedge|Vedge]]'s `vedge_staff` Flutter architecture; Flutterwave + mnotify integrations; deployed on Vercel + Railway.

### Paused

_(none yet)_

### Exploring

_(none yet)_

### Completed / archived

_(none yet)_

## Syntheses

- [[wiki/syntheses/agent-review-framework]] — reusable five-lens framework for auditing LLM agent codebases against architectural first principles (agentic-loop, augmented-llm, reasoning-execution-split, agent-workflow-patterns, retrieval-augmented-generation). Worked example: 2026-05-08 review of [[wiki/projects/kivora|Kivora]]'s Python agent.
- [[wiki/syntheses/refero-open-design-claude-design-comparison]] — three strategic bets in AI design tooling: Refero (curated SaaS catalog) vs Open Design (open-source full-stack platform) vs Claude Design (proprietary Anthropic surface). Includes adoption-fit decision matrix and Vedge-specific recommendation.
- [[wiki/syntheses/godwin-portfolio]] — *2026-05-09*. **One-page map of every project Godwin owns or delivers**, organized by *who owns the IP* and *who holds the client relationship*. 6 buckets: ROAM owned products (Vedge / Kivora / Clarvyn / _roamlabs) / ROAM internal tools (Helm) / ROAM client work (Coffee Break / StaceSprouts) / Brolly owned platform (Brolly) / Brolly client work (Asanti) / SoftTech subcontract (CPC RTBVD).
- [[wiki/syntheses/multi-agent-ops-platform-blueprint]] — *2026-05-09*. **Reusable 5-layer reference architecture** for building a multi-agent operations platform that automates a small business's GTM + business operations. Compresses 7+ wild-cited multi-agent system descriptions in the brain (CyrilXBT / Khairallah / regent0x_ / Nateherk / Shruti / Shann Holmberg) plus the architectural foundations (DOE / reasoning-execution-split / markdown-as-agent-contract / self-annealing). Worked example: [[wiki/projects/helm|Helm]].
- [[wiki/syntheses/helm-voice-profiles]] — *2026-05-09*. **Starter-draft voice profiles** for Helm's Marketing agent: Vedge (high confidence), Kivora / ROAM GRC (high), Clarvyn (medium), ROAM Labs corp (low / draft-only — brand unsettled). Extracted from existing landing-site copy via Shann Holmberg's brand-foundation-extraction methodology. Will migrate to `helm-repo/voice-profiles/` when the Helm repo exists; refine when 20-best-pieces curation is available.
- [[wiki/syntheses/helm-commercialization-paths]] — *2026-05-09*. **Strategic decision record**: Helm proceeds as ROAM Labs internal OS for v1; agent-marketplace shape explicitly deferred. 3 shapes considered (A: services-as-software / B: productized multi-tenant marketplace / C: open-source-core + commercial layer). Shape A chosen with 5+ wiki sources of supporting evidence. Re-evaluation trigger: 3-5 paying customers operating real volumes + concrete churn/implementation/distribution evidence. Data model carries `tenant_id` columns from day 1 to keep pivot tractable.

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
