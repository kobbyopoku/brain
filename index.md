# index.md — Wiki catalog

The content-oriented index of this wiki. Read this first when answering a query, then drill into the linked pages. See [[CLAUDE]] for conventions and [[log]] for the chronological record of operations.

**Stats**: 55 sources · 151 entities · 44 concepts · 1 project · 1 synthesis · last updated 2026-05-05

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
- [[wiki/sources/saraev-agentic-workflows-2026]] — 5h+ definitive course; coins the DO framework, horizontal-leverage thesis, reliability-decay-math. The architectural companion to the three economic playbooks above.
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

### Open-source autonomous agents

- [[wiki/sources/nousresearch-hermes-agent]] — MIT-licensed self-improving multi-platform AI agent by [[wiki/entities/nous-research|Nous Research]]. Built-in learning loop (creates skills from experience, persists across sessions, builds user model). Multi-platform messaging gateway (Telegram + Discord + Slack + WhatsApp + Signal + Email + CLI). Model-agnostic (200+ models via [[wiki/entities/openrouter|OpenRouter]] + Nous Portal + AWS Bedrock + others). 23k+ stars.

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

- [[wiki/entities/anatoli-kopadze]] — author of the 20 Claude Prompts catalog.
- [[wiki/entities/andrej-karpathy]] — author of the LLM Wiki pattern.
- [[wiki/entities/alex-vacca]] — author of the services-as-software $7M agency playbook.
- [[wiki/entities/brian-moran]] — author of the 10 online business models for 2026.
- [[wiki/entities/clear_graphics]] — author of the YC unicorn landing-pages analysis.
- [[wiki/entities/corey-haines]] — *(stub)* maintainer of the marketingskills Claude Code skill-pack.
- [[wiki/entities/eng-khairallah]] — author of the AI Automations early-stage services playbook.
- [[wiki/entities/godofprompt]] — author of the Paul Graham startup-eval prompts.
- [[wiki/entities/HeyZaraKhan]] — author of two Claude-ecosystem posts (Skills, Certified Architect).
- [[wiki/entities/heynavtoor]] — author of the 10-repos-replace-eng-team thesis.
- [[wiki/entities/hooeem]] — author of the build-an-AI-agent-today course.
- [[wiki/entities/mnilax]] — author of the 430-hours instrumented Claude Code study.
- [[wiki/entities/nainsi-dwiv]] — author of the Agent Skills architectural deep-dive.
- [[wiki/entities/nateherk]] — author of the AI OS playbook; runs a $3M/yr business on Claude Code.
- [[wiki/entities/nick-saraev]] — author of the 5h+ Agentic Workflows course; coined the DO framework.
- [[wiki/entities/noisyb0y1]] — *(stub)* author who surfaced the marketingskills skill-pack.
- [[wiki/entities/regent0x]] — author of the Claude Code 24/7 dev team stack.

### People — referenced

- [[wiki/entities/paul-graham]] — invoked as named persona in startup-eval prompts.
- [[wiki/entities/sam-altman]] — Worldcoin founder; OpenAI CEO (widely known, partially sourced).
- [[wiki/entities/vannevar-bush]] — 1945 originator of the [[memex]]; conceptual ancestor of the LLM Wiki.

### Organizations

- [[wiki/entities/agora]] — billion-dollar yearly-newsletter publishing empire (model #3 exemplar).
- [[wiki/entities/anthropic]] — AI research company; maintainer of Claude and Claude Code.
- [[wiki/entities/coldiq]] — Alex Vacca's $7M ARR services-as-software agency.
- [[wiki/entities/nous-research]] — open-weight AI research collective; publisher of Hermes-series models and [[wiki/entities/hermes-agent|Hermes Agent]].
- [[wiki/entities/samcart]] — Brian Moran's checkout/e-commerce platform; data source for the 2026 catalog.
- [[wiki/entities/trail-of-bits]] — security firm publishing claude-code-skills.
- [[wiki/entities/worldcoin]] — Sam Altman's iris-scanning identity company.

### Knowledge tooling

- [[wiki/entities/obsidian]] — local-first markdown editor; the working environment for this vault, also the persistent-memory layer in regent0x_'s stack.
- [[wiki/entities/qmd]] — local hybrid search engine for markdown wikis at scale.
- [[wiki/entities/refero]] — curated DESIGN.md library + MCP server for AI coding agents.

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
- [[wiki/entities/cline]] — VS Code autonomous agent.
- [[wiki/entities/codex-cli]] — *(stub)* OpenAI's coding-agent CLI; auto-detected by Open Design.
- [[wiki/entities/cowork]] — *(stub)* Claude Code alternative named by heynavtoor.
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

The remaining 113 Open Design brands (mostly named-aesthetic styles like brutalism / claymorphism / doodle / retro and smaller real brands) are NOT individually stubbed — they exist as raw DESIGN.md files in `raw/open-design/design-systems/` and are enumerated in [[wiki/sources/open-design-catalog]]. They can be graduated to entity stubs on-demand when projects need them.

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

- [[wiki/concepts/llm-wiki-pattern]] — persistent, LLM-maintained markdown wiki built on top of curated raw sources.
- [[wiki/concepts/markdown-as-agent-contract]] — meta-pattern: markdown files as the contract layer between humans and AI agents.
- [[wiki/concepts/memex]] — Vannevar Bush's 1945 vision of a personal, associative knowledge store.
- [[wiki/concepts/retrieval-augmented-generation]] — per-query retrieval over raw documents; contrast case.

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
- [[wiki/concepts/do-framework]] — Saraev's Directives + Executions architecture for deterministic agentic workflows.
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

- [[wiki/projects/vedge]] — multi-tenant healthcare OS for African hospitals, clinics, labs, pharmacies; modular-monolith Spring Boot backend + Next.js web + Flutter mobile (patient + staff).

### Paused

_(none yet)_

### Exploring

_(none yet)_

### Completed / archived

_(none yet)_

## Syntheses

- [[wiki/syntheses/refero-open-design-claude-design-comparison]] — three strategic bets in AI design tooling: Refero (curated SaaS catalog) vs Open Design (open-source full-stack platform) vs Claude Design (proprietary Anthropic surface). Includes adoption-fit decision matrix and Vedge-specific recommendation.

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
