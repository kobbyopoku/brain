# log.md — Operations log

Append-only chronological record. See [[CLAUDE]] for the format spec. Greppable: `grep "^## \[" log.md | tail -10`.

---

## [2026-05-02] schema-update | Initialize LLM Wiki vault
- pages created: [[CLAUDE]], [[index]], [[log]], `templates/source.md`, `templates/entity.md`, `templates/concept.md`, `templates/synthesis.md`, `raw/README.md`
- notes: Bootstrap of the vault following Karpathy's LLM Wiki pattern. Three-layer architecture (raw / wiki / schema) established. Four page templates created. Index and log initialized.

## [2026-05-02] ingest | LLM Wiki — Karpathy
- raw: `raw/llm-wiki-pattern-karpathy.md` (downloaded from gist)
- pages created: [[wiki/sources/llm-wiki-pattern-karpathy]], [[wiki/entities/andrej-karpathy]], [[wiki/entities/vannevar-bush]], [[wiki/entities/obsidian]], [[wiki/entities/qmd]], [[wiki/concepts/llm-wiki-pattern]], [[wiki/concepts/memex]], [[wiki/concepts/retrieval-augmented-generation]]
- pages updated: [[index]]
- notes: First ingest. This source is constitutive of the vault — it's the pattern the schema in [[CLAUDE]] instantiates. Future ingests will be more conventional (entities and concepts that don't appear in the schema itself).

## [2026-05-02] ingest | Design Systems for AI Agents — Refero
- raw: `raw/Design Systems for AI Agents.md` (Web Clipper from styles.refero.design)
- pages created: [[wiki/sources/refero-design-systems-for-ai-agents]], [[wiki/entities/refero]], [[wiki/concepts/design-md]], [[wiki/concepts/markdown-as-agent-contract]]
- pages updated: [[wiki/concepts/llm-wiki-pattern]] (added markdown-as-agent-contract to Related concepts; added agent-config tag), [[index]]
- notes: Thin landing-page clipping but yielded a high-value meta-pattern page ([[markdown-as-agent-contract]]) that retroactively reframes [[llm-wiki-pattern]] as one instance of a broader family. Did not create entity pages for the brands listed on the Refero landing page (Linear, Stripe, Apple, etc.) — they appear only as examples; defer until a brand becomes the subject of its own ingest.

## [2026-05-02] lint | First lint pass; 3 missing canonical concept pages found
- script run: `bin/wiki_lint.py` — initial naive version flagged 14 broken links across 6 unique targets
- false positives: `[[link]]`, `[[page-name]]`, `[[wikilinks]]` — all inside inline code or fenced code blocks; lint regex was naive
- real findings: `[[ingest]]`, `[[query]]`, `[[lint]]` — referenced in [[wiki/concepts/llm-wiki-pattern]] and [[wiki/entities/obsidian]] but no pages existed
- pages created: [[wiki/concepts/ingest]], [[wiki/concepts/query]], [[wiki/concepts/lint]] (operation pages, not stubs); [[wiki/concepts/agents-md]], [[wiki/concepts/skill-md]], [[wiki/concepts/readme-md]] (stub completions of the markdown-as-agent-contract family)
- pages updated: [[wiki/concepts/llm-wiki-pattern]] (Related concepts now lists all sibling agent-contract concepts), [[wiki/concepts/markdown-as-agent-contract]] (wikilinks each markdown-file mention; cleaned aliases)
- tooling: improved `bin/wiki_lint.py` to honor inline-code and fenced-code spans before parsing wikilinks; committed to repo for reuse by the weekly remote lint
- post-fix lint: clean (0 broken, 0 ambiguous, 0 orphans, 0 index drift, 0 frontmatter issues)
- notes: orphan-check, index-drift, and frontmatter-drift checks all clean on first run — surprising result given recent volume of writes; suggests the schema's discipline is paying off.

## [2026-05-02] ingest | How I Turned My Claude Code Into 24/7 Dev Team — regent0x_
- raw: `raw/How I Turned My Claude Code Into 247 Dev Team (Full Guide + Repos).md` (Web Clipper from x.com/regent0x_)
- pages created: [[wiki/sources/regent0x-claude-code-247-dev-team]], [[wiki/entities/regent0x]], [[wiki/entities/claude-code]], [[wiki/entities/trail-of-bits]], [[wiki/entities/superpowers]], [[wiki/entities/claude-mem]], [[wiki/entities/claude-subconscious]], [[wiki/entities/trail-of-bits-claude-code-skills]], [[wiki/entities/anthropic-skills]], [[wiki/entities/tdd-guard]], [[wiki/entities/wshobson-agents]], [[wiki/entities/davepoon-subagents-collection]], [[wiki/entities/wshobson-commands]], [[wiki/entities/claude-squad]], [[wiki/entities/claude-flow]], [[wiki/concepts/subagents]], [[wiki/concepts/claude-code-skills]], [[wiki/concepts/claude-code-hooks]], [[wiki/concepts/claude-code-slash-commands]], [[wiki/concepts/multi-agent-orchestration]]
- pages updated: [[wiki/entities/anthropic]] (promoted from stub to substantive entity — now central to the Claude Code ecosystem section, not just the Refero catalog), [[wiki/entities/obsidian]] (added "Use as a Claude Code memory layer (regent0x_)" section with the structured vault layout), [[wiki/concepts/llm-wiki-pattern]] (added to Treatment across sources — first wild secondary citation), [[wiki/concepts/markdown-as-agent-contract]] (added to Treatment with note on engineering-domain-specific scaling), [[wiki/concepts/skill-md]] (Related concepts now distinguishes file-format vs. mechanism), [[index]]
- notes: First source whose ingest *demonstrates compounding* — the source explicitly cites Karpathy's [[llm-wiki-pattern]] which is already in the wiki, so the cross-reference goes both ways immediately. Also flagged a URL discrepancy (the post links to `github.com/karpathy/llm-wiki` which doesn't appear to resolve; the actual gist URL is in [[wiki/sources/llm-wiki-pattern-karpathy]]). Rich source — the [[CLAUDE]] template the post recommends is reusable for any future engineering-vault work.

## [2026-05-02] ingest | How to Build & Sell AI Automations That Generate $10K Per Month — Khairallah
- raw: `raw/How to Build & Sell AI Automations That Generate $10K Per Month (Full Course).md` (Web Clipper from x.com/eng_khairallah1)
- pages created: [[wiki/sources/khairallah-ai-automations-10k-month]], [[wiki/entities/eng-khairallah]], [[wiki/entities/tavily]], [[wiki/entities/google-drive]], [[wiki/entities/gmail]], [[wiki/entities/slack]], [[wiki/concepts/ai-automation-services]], [[wiki/concepts/context-file]], [[wiki/concepts/mcp-server]], [[wiki/concepts/scheduled-automation]]
- pages updated: [[wiki/concepts/markdown-as-agent-contract]] (added context-file to the family; added Khairallah to Treatment), [[wiki/concepts/skill-md]] (Related concepts adds context-file as sibling), [[wiki/concepts/claude-code-skills]] (cross-cited from the regent0x_ ingest above; touched again to capture Khairallah's services-side framing), [[wiki/concepts/claude-code-slash-commands]] (Khairallah's `/schedule` cross-cite), [[index]]
- notes: This source pairs with the regent0x_ ingest above as **the same Claude Code primitives, opposite economic frame** — personal productivity vs. service-business. Several concepts (mcp-server, scheduled-automation, claude-code-skills) are cited by both sources; their pages capture both perspectives explicitly under "Treatment across sources." This is the kind of synthesis territory the wiki was built for. Pricing claims ($3-15k/build, $750/mo retainers, $165k/yr, 18-month window) are the author's prior, not market data.

## [2026-05-02] schema-update | Add Stubs convention; reference lint script
- pages updated: [[CLAUDE]] — added § Page conventions → Stubs (formalizes `tags: [stub]` shape and lifecycle); added tooling note in § Workflows → Lint pointing to `bin/wiki_lint.py`
- notes: Closes the schema gap flagged in the previous log entry. Stubs convention codifies Kobby's standing preference for completionist coverage. The Stubs subsection also tells future linters to flag long-stale stubs as candidates for expansion or deletion.

## [2026-05-02] refactor | Backfill stub entity pages for all Refero brands
- pages created: [[wiki/entities/acctual]], [[wiki/entities/anthropic]], [[wiki/entities/antimetal]], [[wiki/entities/apple]], [[wiki/entities/base44]], [[wiki/entities/column]], [[wiki/entities/cursor]], [[wiki/entities/dia-browser]], [[wiki/entities/elevenlabs]], [[wiki/entities/family]], [[wiki/entities/general-intelligence-company]], [[wiki/entities/hyperstudio]], [[wiki/entities/linear]], [[wiki/entities/mercury]], [[wiki/entities/minimalissimo]], [[wiki/entities/monopo-saigon]], [[wiki/entities/raycast]], [[wiki/entities/stripe]], [[wiki/entities/superhuman]], [[wiki/entities/titan]]
- pages updated: [[wiki/entities/refero]] (added "Featured brands in catalog" section linking all 20; added website frontmatter), [[wiki/sources/refero-design-systems-for-ai-agents]] (expanded "Mentioned entities" with all 20 backlinks), [[index]] (new "Brands in Refero catalog (stubs)" subsection; stats updated)
- notes: Per Kobby's standing preference — completionist entity coverage. All 20 pages tagged `stub` with consistent structure (one-line citable framing, no fabricated profile prose). When future ingests bring in a primary source about any of these brands, expand the corresponding stub. The schema-conventions section in [[CLAUDE]] should probably be updated to formalize the stub convention; flagging here for next schema-update pass.

## [2026-05-02] ingest | 10 GitHub Repos to Replace an Engineering Team — heynavtoor
- raw: `raw/Post by @heynavtoor on X.md` (Web Clipper from x.com/heynavtoor, 2026-04-22)
- pages created: [[wiki/sources/heynavtoor-10-repos-replace-eng-team]], [[wiki/entities/heynavtoor]], [[wiki/entities/openhands]], [[wiki/entities/aider]], [[wiki/entities/cline]], [[wiki/entities/claude-task-master]], [[wiki/entities/crewai]], [[wiki/entities/langgraph]], [[wiki/entities/n8n]], [[wiki/entities/coolify]], [[wiki/entities/posthog]], [[wiki/entities/chatwoot]]
- notes: Tool-discovery source. CrewAI and LangGraph cross-cite immediately with [[wiki/sources/hooeem-build-an-ai-agent-today]] (also ingested in this batch).

## [2026-05-02] ingest | 6 Paul Graham-Style Startup Evaluation Prompts — godofprompt
- raw: `raw/Post by @godofprompt on X.md` (2026-04-04)
- pages created: [[wiki/sources/godofprompt-paul-graham-startup-prompts]], [[wiki/entities/godofprompt]], [[wiki/entities/paul-graham]]
- notes: Prompt content is partially truncated in source. The `<role>...<task>` format is one stylistic alternative to AnatoliKopadze's markdown-structured prompts.

## [2026-05-02] ingest | Anthropic Just Open-Sourced Skills — HeyZaraKhan
- raw: `raw/Post by @HeyZaraKhan on X.md` (2026-03-22)
- pages created: [[wiki/sources/HeyZaraKhan-anthropic-skills-announcement]], [[wiki/entities/HeyZaraKhan]]
- notes: Secondary citation reinforcing existing [[claude-code-skills]] / [[wiki/entities/anthropic-skills]]. Comments on source flag the "BREAKING" overreach (feature was already months old).

## [2026-05-02] ingest | Claude Certified Architect Resource List — HeyZaraKhan
- raw: `raw/Post by @HeyZaraKhan on X 1.md` (2026-03-22)
- pages created: [[wiki/sources/HeyZaraKhan-claude-certified-architect]], [[wiki/entities/anthropic-cookbook]], [[wiki/entities/claude-certified-architect]]
- notes: Resource pointer source. Program is gated to corporate-email registrations (per comments).

## [2026-05-02] ingest | 8 YC Unicorn Landing Pages — clear_graphics
- raw: `raw/the anatomy of 8 YC unicorn landing pages and the exact patterns they share.md` (2026-04-24)
- pages created: [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]], [[wiki/entities/clear_graphics]], [[wiki/entities/airbnb]], [[wiki/entities/coinbase]], [[wiki/entities/instacart]], [[wiki/entities/doordash]], [[wiki/entities/dropbox]], [[wiki/entities/gitlab]], [[wiki/entities/gusto]], [[wiki/concepts/landing-page-patterns]]
- pages updated: [[wiki/entities/stripe]] — first cross-source-cited entity: previously a Refero-catalog stub, now substantively expanded with landing-page treatment. Removed `stub` tag.
- notes: 11 patterns observed across 8 unicorns ($280B+ combined market cap). Concept page captures all 11; brand pages are stubs except Stripe.

## [2026-05-02] ingest | The Truth About Making Money Online in 2026 — Brian Moran
- raw: `raw/The Truth About Making Money Online in 2026 (And What's About to Die).md` (2026-02-07)
- pages created: [[wiki/sources/realbrianmoran-making-money-online-2026]], [[wiki/entities/brian-moran]], [[wiki/entities/samcart]], [[wiki/entities/agora]], [[wiki/entities/replit]], [[wiki/concepts/online-business-models-2026]]
- pages updated: [[wiki/entities/cursor]] (added build-your-own-app treatment, removed stub tag), [[wiki/entities/claude-code]] (additional citations + new mentions section + entities), [[wiki/concepts/ai-automation-services]] (Brian Moran model #10 added to Treatment across sources)
- notes: Contains a falsifiable claim ("monthly $20-$200 communities are dying") worth tracking against future ingests. Triangulates with Khairallah and Vacca on the AI-services-for-businesses opportunity.

## [2026-05-02] ingest | $7M Services-as-Software Agency — Alex Vacca
- raw: `raw/How I Quit Working for Sam Altman and Built a $7M Services-as-Software Agency.md` (2026-05-01)
- pages created: [[wiki/sources/itsalexvacca-services-as-software-7m-agency]], [[wiki/entities/alex-vacca]], [[wiki/entities/coldiq]], [[wiki/entities/worldcoin]], [[wiki/entities/sam-altman]], [[wiki/entities/aiagency-io]], [[wiki/concepts/services-as-software]], [[wiki/concepts/churn-at-scale]]
- pages updated: [[wiki/concepts/ai-automation-services]] (added scaled-version Treatment); [[wiki/entities/claude-code]] (referenced for "internal tools that used to cost tens of thousands of dollars to build are weekend projects").
- notes: The most operationally substantive source on services-business economics yet. Churn-at-scale math is the standout contribution. Pairs with Khairallah (early stage) and Brian Moran (one of 10 viable 2026 models) — three vintages, same domain.

## [2026-05-02] ingest | 20 Claude Prompts — Anatoli Kopadze
- raw: `raw/20 Claude Prompts that turn a $20 Subscription into a personal Assistant, Editor, Coach, and Analyst.md` (2026-04-29)
- pages created: [[wiki/sources/AnatoliKopadze-20-claude-prompts]], [[wiki/entities/anatoli-kopadze]], [[wiki/concepts/personal-claude-prompts]]
- notes: 20 detailed prompt templates across 5 categories (deep research, writing, career, daily life, learning). Several prompts (Multi-Source Synthesis, Brutal Editor, Devil's Advocate, Mental Model Builder) are candidates to register as actual Claude Code skills for this vault.

## [2026-05-02] ingest | I Want to Build an AI Agent Today (Course) — hooeem
- raw: `raw/I want to build an AI agent today (full course).md` (2026 Q1; frontmatter date 2023-03-26 likely a metadata error — content references events through March 2026)
- pages created: [[wiki/sources/hooeem-build-an-ai-agent-today]], [[wiki/entities/hooeem]], [[wiki/entities/anthropic-agent-sdk]], [[wiki/entities/openai-agents-sdk]], [[wiki/concepts/agentic-loop]], [[wiki/concepts/augmented-llm]], [[wiki/concepts/agent-workflow-patterns]], [[wiki/concepts/beginner-agent-types]]
- pages updated: [[wiki/entities/claude-code]] (added anthropic-agent-sdk relation); [[wiki/entities/crewai]] and [[wiki/entities/langgraph]] (cross-cited from heynavtoor's ingest in same batch).
- notes: Foundational source on agent-building. Resolves multiple open questions across the wiki (e.g. regent0x_'s 5-role subagent setup is an instance of orchestrator-workers + evaluator-optimizer composed).

## [2026-05-02] skip | Post by @wizofecom — too thin to ingest
- raw: `raw/Post by @wizofecom on X.md` (2026-04-17)
- decision: NOT ingested. Source is one line + three image attachments not viewable from the captured clipping. No entity, concept, or claim survived a substantive read. Documenting the skip here so future audits know it was considered.

## [2026-05-02] schema-update | Add Read mode (consumption from other projects)
- pages updated: [[CLAUDE]] — added § Modes section distinguishing maintainer mode (default) from read mode (when the wiki is consumed from another project, e.g. via `~/brain` clone + `/brain` slash command). Read-mode rules: read-only, schema-first, cite specifically, silence-is-honest, substantive-answers-offered-for-filing, new-sources-via-/brain-ingest. Adjusted intro to reference mode-awareness.
- companion (outside the vault): added user-level slash commands `~/.claude/commands/brain.md` (read-mode query) and `~/.claude/commands/brain-ingest.md` (queue new source to raw/) so the wiki can be reached from any Claude Code session.
- notes: This addresses the schema gap flagged in the previous ingest's insight ("the brain's CLAUDE.md is written assuming the agent IS the brain's maintainer"). The wiki is now bidirectional — same file governs both maintainer and consumer agents.

## [2026-05-02] schema-update | Add Projects as fourth wiki page type
- pages created: `wiki/projects/README.md` (directory documentation), `templates/project.md`
- pages updated: [[CLAUDE]] — directory layout adds `wiki/projects/`; frontmatter `type` field accepts `project`; new § Workflows → Adding a project + Updating a project; index.md format mentions Projects grouped by status. [[index]] — new `## Projects` section with status subgroups; stats line includes `0 projects`. `bin/wiki_lint.py` — recognizes `wiki/projects/` and `type: project`; skips README.md files in WIKI_DIRS so directory documentation doesn't fail frontmatter checks.
- companion (outside the vault): added user-level slash commands `~/.claude/commands/brain-add-project.md` and `~/.claude/commands/brain-update-project.md` for surveying a project from its directory and writing/updating its page in the brain.
- notes: Projects are first-class now. The brain page holds the *durable summary* (status, stack, current focus, decisions, lessons learned); operational state (granular decisions, error postmortems, session notes) belongs in the project's own repo at `<project>/.memory/`. The two are linked by a gitignored `BRAIN.md` at the project root pointing at `~/brain/wiki/projects/<slug>.md`. First real project addition happens in a separate session inside the project (e.g. vedge) running `/brain-add-project`.

## [2026-05-02] add-project | Vedge
- page created: [[wiki/projects/vedge]]
- pages updated: [[index]] — Projects → Active now lists Vedge; stats line bumped to `1 project`.
- status: active
- repo: multi-repo at github.com/kobbyopoku/{vedge_backend, vedge_frontend, vedge_patient, vedge_staff, vedge_landing, vedge_emails, vedge_agent}
- local_path: /Users/kobbyopoku/ROAM/CascadeProjects/vedge
- project-side: BRAIN.md added at workspace root pointing to the brain page. Workspace root is not a git repo and has no .gitignore — the seven submodule repos each have their own; no .gitignore changes were necessary.
- notes: First project page in the wiki. Vedge is a multi-tenant healthcare OS for African facilities — modular-monolith Spring Boot backend (12 modules) + Next.js web + Flutter patient/staff apps. Surfaced candidates for future concept pages: `multi-tenant-ehr`, `modular-monolith`, `flyway-migration-safety`, `expert-led-implementation-protocol`. No existing brain entities map directly yet (Spring Boot, Flyway, Flutter, Paystack, Flutterwave, Kivora, Railway are all unrepresented).

## [2026-05-02] ingest | Equipping Agents for the Real World — NainsiDwiv50980
- raw: `raw/Equipping Agents for the Real World A Deeper Look at Agent Skills.md` (2026-05-02)
- pages created: [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]], [[wiki/entities/nainsi-dwiv]], [[wiki/concepts/progressive-disclosure]], [[wiki/concepts/reasoning-execution-split]]
- pages updated: [[wiki/concepts/claude-code-skills]] (architectural framing + risk surface)
- notes: Conceptual deep-dive contributing two named patterns (progressive disclosure, reasoning + execution split). Pairs with operational sources (regent0x_, Mnilax, nateherk) — gives them the *why* underneath the *what*.

## [2026-05-02] ingest | 430 Hours of Claude Code Usage — Mnilax
- raw: `raw/I tracked 430 hours of Claude Code usage. 73% was wasted on these 9 patterns..md` (2026-05-01)
- pages created: [[wiki/sources/Mnilax-430-hours-claude-code-waste]], [[wiki/entities/mnilax]], [[wiki/concepts/claude-code-overhead-patterns]]
- pages updated: [[wiki/concepts/claude-code-skills]] (cost counterpoint), [[wiki/concepts/claude-code-hooks]] (hook-injection-waste pattern), [[wiki/concepts/mcp-server]] (tool-definition overhead)
- notes: Instrumented 90-day study; 9 patterns; ships an audit script. Directly applicable to this wiki's own setup — worth running the audit on `~/.claude/CLAUDE.md` and `~/brain/CLAUDE.md` after this ingest.

## [2026-05-02] ingest | My Claude Code OS Runs My $3M/yr Business — nateherk
- raw: `raw/My Claude Code OS Runs my $3Myr Business. Steal This..md` (2026-05-01)
- pages created: [[wiki/sources/nateherk-claude-code-os-3m-business]], [[wiki/entities/nateherk]], [[wiki/entities/ais-os]], [[wiki/entities/skool]], [[wiki/entities/glaido]], [[wiki/entities/clickup]], [[wiki/entities/quickbooks]], [[wiki/entities/fireflies]], [[wiki/entities/notion]], [[wiki/concepts/ai-os-pattern]], [[wiki/concepts/hot-cache]]
- pages updated: [[wiki/concepts/llm-wiki-pattern]] (second wild secondary citation; hot-cache extension noted), [[wiki/concepts/scheduled-automation]] (Cloud Routines / Local / Loop tradeoff matrix), [[wiki/concepts/mcp-server]] (operational alternative: API-saved-as-markdown), [[wiki/concepts/multi-agent-orchestration]] (cadence framing), [[wiki/concepts/subagents]] (clickup-searcher context-isolation example), [[wiki/concepts/markdown-as-agent-contract]] (layered claude.md/skills/contexts/references), [[wiki/concepts/claude-code-skills]] (six-step authoring framework), [[wiki/concepts/progressive-disclosure]] (three-level loading model corroboration), [[wiki/concepts/reasoning-execution-split]] (boring-is-beautiful corollary)
- notes: **Second wild secondary citation of Karpathy's LLM Wiki**. Operationally rich — Three Ms + Four Cs frameworks coined. Hot-cache pattern is genuinely new and worth implementing on this brain. Cross-cuts with Mnilax (API-over-MCP = Mnilax's tool-def overhead pattern from a different angle) and Vacca (services-business-shape running on Claude Code).

## [2026-05-02] ingest | Stripe Design System (DESIGN.md from Refero)
- raw: `raw/stripe-design-md.md` (extracted via WebFetch from styles.refero.design — page is JS-rendered with a clipboard-driven Copy.md button so direct HTTP download not available; this is the substantive core, not a guaranteed-exhaustive Copy.md)
- pages created: [[wiki/sources/stripe-design-md]]
- pages updated: [[wiki/entities/stripe]] (added Design system summary section + design-md-ingested tag + third source citation), [[wiki/concepts/design-md]] (filled in concrete "What's actually in a Refero DESIGN.md" section using Stripe as the worked example; resolved the "what does an actual DESIGN.md look like?" open question), [[index]]
- notes: First brand DESIGN.md ingested into the brain. Demo for the user's Option A. Stripe is now cited by **three independent sources** (Refero brand catalog, clear_graphics landing-page analysis, this DESIGN.md) — the most cross-cited entity in the wiki. Validates that the same workflow works for the remaining 19 Refero brands when option B is wanted. Brain now has one concrete reference for what design tokens a real DESIGN.md captures: 18 named colors (5 brand + 3 gradients + 7 neutrals), 7-step type scale on `sohne-var`, 4px-base spacing, 5-radius / 4-shadow vocabulary, 5 token-referenced components, 1-paragraph philosophy.

## [2026-05-02] ingest | DESIGN.md for the remaining 19 Refero brands (batch)
- raw: 19 new files at `raw/<brand>-design-md.md` for Acctual, Anthropic, Antimetal, Apple, Base44, Column, Cursor, Dia Browser, ElevenLabs, Family, General Intelligence Company, Hyperstudio, Linear, Mercury, Minimalissimo, monopo saigon, Raycast, Superhuman, Titan. Captured via WebFetch from each brand's Refero style page.
- pages created: 19 source pages at `wiki/sources/<brand>-design-md.md` — one per brand. Compact format (mirror of Stripe's pattern but tighter).
- pages updated: 17 stub entity pages graduated from `[refero-catalog, stub]` to `[refero-catalog, design-md-ingested]` with Profile section replaced, "Design system summary" section added, and DESIGN.md source page linked under Mentioned in. 2 already-substantive entities (Anthropic, Cursor) gained a Design system summary section + DESIGN.md source linked. [[wiki/concepts/design-md]] gained a major "Cross-brand patterns" section with observations across all 20 ingested DESIGN.md files (common patterns, distinctive signatures, philosophical archetypes). [[index]] reorganized "Design systems / UI" section with all 20 DESIGN.md sources grouped together.
- notes: Completes the brain's coverage of Refero's catalog — every cataloged brand now has its DESIGN.md ingested as a substantive source. The brain can now answer cross-brand design questions ("which dark-mode systems use glass?", "which brands forbid box-shadows?") with citations across the catalog. Provenance caveat applies: WebFetch extraction from rendered HTML may differ slightly from the official Copy.md export. Worth re-validating any individual brand's DESIGN.md by pasting in a real Copy.md.

## [2026-05-03] ingest | Nick Saraev — AGENTIC WORKFLOWS: Build & Sell AI Automations (2026)
- raw: `raw/saraev-agentic-workflows-2026.md` — full 503KB transcript (10,974 segments, 341min) captured via youtube-transcript-api with timestamps. Source: https://www.youtube.com/watch?v=MxyRjL7NG18
- pages created: [[wiki/sources/saraev-agentic-workflows-2026]], [[wiki/concepts/do-framework]], [[wiki/concepts/horizontal-leverage]], [[wiki/concepts/reliability-decay-math]], [[wiki/entities/nick-saraev]], [[wiki/entities/anymailfinder]]
- pages updated: [[wiki/concepts/ai-automation-services]] (4th major source — architectural companion to the 3 economic), [[wiki/concepts/services-as-software]] (DO as delivery layer for the model), [[wiki/concepts/agent-workflow-patterns]] (workflow-vs-agent tradeoff via reliability decay), [[wiki/concepts/claude-code-overhead-patterns]] (3rd independent confirmation of MCP token cost — Mnilax + nateherk + Saraev), [[wiki/concepts/ai-os-pattern]] (DO as workflow-scope sibling), [[index]]
- notes: 5h 41min video — substantial. Saraev's contributions are architectural (DO framework) and economic (horizontal leverage thesis + reliability decay math) where Khairallah/Vacca/Moran were operational/business-model. Wiki now has comprehensive AI-automation-services coverage from 4 independent angles. Key cross-source compounding: (1) MCP overhead now triple-cited (Mnilax measurement + nateherk operational + Saraev observational), becoming a load-bearing wiki claim; (2) workflow-vs-agent tradeoff double-cited (hooeem framing + Saraev math); (3) reasoning-execution-split principle now has a named architectural pattern (DO framework). Worth filing a future synthesis comparing the four AI-automation-services sources side-by-side.

## [2026-05-04] ingest | heynavtoor 90-day playbook + noisyb0y1 marketingskills repo (batch)
- raw: `raw/How to Build a $10K Per Month Claude Automation Business in 90 Days [No Coding Required].md` (heynavtoor X-thread, 2026-05-03), `raw/139 marketing tactics + CRO framework — One repo $0..md` (noisyb0y1 X-thread, 2026-05-04)
- pages created:
  - sources: [[wiki/sources/heynavtoor-10k-claude-automation-business-90-days]], [[wiki/sources/noisyb0y1-marketingskills-repo]]
  - concepts: [[wiki/concepts/switching-forces]], [[wiki/concepts/ai-seo]]
  - entities: [[wiki/entities/corey-haines]], [[wiki/entities/marketingskills-repo]], [[wiki/entities/noisyb0y1]], [[wiki/entities/cowork]] (stub created during lint to clear broken link)
- pages updated: [[wiki/entities/heynavtoor]] (graduated from stub; second thread referenced; expanded positions/claims; tags updated). [[wiki/concepts/ai-automation-services]] (5th source — heynavtoor as derivative-but-confirming Khairallah; cross-source canon now solid). [[wiki/concepts/claude-code-skills]] (marketingskills as **most substantive non-design skill-pack** in the wiki — sibling to Refero). [[wiki/concepts/markdown-as-agent-contract]] (extended to public-web buying-agent surfaces — `/llms.txt`, `/pricing.md`, `/changelog.md`; 3 layers visible in one source). [[wiki/concepts/landing-page-patterns]] (CRO 7-question framework as evaluation companion to clear_graphics's observation; switching-forces mapping per pattern). [[wiki/projects/vedge]] (added Concepts/Entities Related cross-references — switching-forces worked example, AI SEO recommendations for `/pricing.md`/`/llms.txt`, marketingskills repo directly usable for `vedge_landing`). [[index]] (new sources, entities, concepts; 2 new reading paths; stats bumped to 39 sources / 97 entities / 39 concepts; anymailfinder added to MCP integrations to clear index drift from prior Saraev ingest).
- notes: Two-source batch with very different shapes. **heynavtoor 90-day** is a derivative of [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah's]] earlier playbook — same 6-phase structure, same niches, same pricing math ($13,750/mo target), same 18-month-window argument. The cross-source convergence strengthens canon: 5 independent sources now agree on the AI automation services model. Worth filing as a synthesis comparing all 5. **noisyb0y1 marketingskills** is highly substantive: surfaces [[wiki/entities/marketingskills-repo|coreyhaines31/marketingskills]] — 139 growth tactics + 12 SEO playbooks + frameworks for copywriting/CRO/A/B/pricing/AI-SEO + 16-tool tool registry. The repo is a marketing-domain analogue to Refero (design-tokens-as-skills) — same shape, different domain. Two new concepts: [[wiki/concepts/switching-forces]] (push/pull/habit/anxiety) and [[wiki/concepts/ai-seo]] (citation by AI vs ranking by Google). Notable cross-cuts: (1) [[markdown-as-agent-contract]] now extends to public-web *buying-agent* surfaces, not just user-side coding agents; (2) [[claude-code-skills]] now has two substantive non-Anthropic skill-packs in the wiki (Refero + marketingskills); (3) Vedge gets directly actionable guidance — switching-forces worked example, `/pricing.md` recommendation, marketingskills drop-in. Both threads come from the same author for heynavtoor (second post — confirms heynavtoor is a recurring producer of operationally-rich Claude Code listicles).

## [2026-05-04] ingest | DESIGN.md batch refresh — 19 brands upgraded to official Copy.md + 12 new brands + Apple alt surface (33 raw files / 32 brands total)
- raw: 32 raw files moved from `~/Downloads/DESIGN*.md` to `raw/<brand>-design-md.md` (renaming applied per brand identity in each file). Replaces 19 prior WebFetch extractions with official Refero Copy.md exports (3-5× richer in tokens/components). Adds 12 new brands and 1 alternate Apple surface. 3 byte-identical Mercury/Airbnb duplicates were deleted. Acctual is the single brand whose raw file remains in the older WebFetch format (not present in this download batch).
- pages created:
  - sources (13): [[wiki/sources/airbnb-design-md]], [[wiki/sources/all-in-one-salon-design-md]], [[wiki/sources/apple-design-md-alt]], [[wiki/sources/augen-pro-design-md]], [[wiki/sources/authkit-design-md]], [[wiki/sources/contractbook-design-md]], [[wiki/sources/customer-io-design-md]], [[wiki/sources/gleap-design-md]], [[wiki/sources/hyer-aviation-design-md]], [[wiki/sources/openai-design-md]], [[wiki/sources/perplexity-ai-design-md]], [[wiki/sources/ui-design-md]], [[wiki/sources/virtual-design-md]]
  - entities (11): [[wiki/entities/all-in-one-salon]], [[wiki/entities/augen-pro]], [[wiki/entities/authkit]], [[wiki/entities/contractbook]], [[wiki/entities/customer-io]], [[wiki/entities/gleap]], [[wiki/entities/hyer-aviation]], [[wiki/entities/openai]], [[wiki/entities/perplexity-ai]], [[wiki/entities/ui]], [[wiki/entities/virtual]]
- pages updated:
  - 19 existing source pages: bumped `updated:` to 2026-05-04. [[wiki/sources/stripe-design-md]] specifically had its provenance caveat replaced with a "raw refreshed with official Copy.md" note.
  - [[wiki/entities/airbnb]] graduated from YC-unicorn-stub to design-md-ingested (added Design system summary + new tags + reference to airbnb-design-md source).
  - [[wiki/entities/apple]] updated to reflect two distinct DESIGN.md surfaces (MacBook Neo + alternate) with composition warning for agents.
  - [[wiki/concepts/design-md]] updated: brand count 20 → 32, dropped pre-existing "WebFetch may miss advanced fields" provenance caveat, added new Cross-brand-patterns deltas section noting (a) "blueprint on white marble" archetype now triple-cited (Stripe/Column/Augen Pro), (b) AI-products converging on minimalist white (OpenAI/Perplexity/Anthropic), (c) unusual weights (475 customer.io, 350 Augen Pro), (d) console-dashboard archetype now broader.
  - [[wiki/sources/refero-design-systems-for-ai-agents]] updated: catalog count 20 → 32, brand list expanded to include all 12 new entries.
  - [[index]]: stats bumped to 52 sources / 108 entities / 39 concepts; DESIGN.md ingest section restructured into "initial 20" + "added 2026-05-04" subsections; Brands-in-Refero-catalog entity section graduated from "stubs awaiting primary sources" to "design-md-ingested" (with note that the Acctual stub remains).
- notes: Catalog-level upgrade. The 32 raw files are now authoritative — agents generating brand-voice UI off this wiki will get full token specs, full component specs, full philosophy text rather than the substantive-core summaries from the original WebFetch ingest. Several emerging patterns crystallized: (1) **AI-product brand restraint** is becoming a category move — OpenAI, Perplexity, Anthropic all share *typography-first + near-zero-chromatic-chrome*. (2) **A brand can have multiple DESIGN.md surfaces** (Apple has two; future-design-md ingests for other large brands may reveal the same). (3) The **"blueprint on white marble"** philosophy phrase is now an explicit Refero archetype (Stripe + Column + Augen Pro). The work to refresh existing source pages was lightweight — the original summaries remain accurate; the new raw files are richer but the substantive observations stand. New brands got fresh source pages following the established compact format.

