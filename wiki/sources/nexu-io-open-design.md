---
type: source
title: nexu-io/open-design — Open-Source Alternative to Claude Design
created: 2026-05-05
updated: 2026-05-05
content_status: substantive
source_url: https://github.com/nexu-io/open-design
source_type: github-repo
author: nexu-io
source_date: 2026-05-05
raw_path: (none — fetched live from GitHub)
tags: [design-systems, claude-design-alternative, open-source, multi-agent, anti-ai-slop, foundational]
---

# nexu-io/open-design — Open-Source Alternative to Claude Design

> Apache-2.0 open-source platform that replicates the artifact-first workflow of Anthropic's Claude Design without proprietary lock-in. Local-first three-layer system (Next.js web app + Node Express daemon + agent runtime) with **138 design systems**, **64 SKILL.md bundles**, **15 auto-detected agent CLIs**, BYOK multi-provider proxy, sandboxed iframe preview, SQLite project persistence, and an exposed MCP server. Functions as both a *product alternative* to Claude Design (and Refero) and a *concept-rich source* on AI-design tooling architecture.

## TL;DR

[Open Design](https://github.com/nexu-io/open-design) is a substantially complete open-source rebuild of [[wiki/entities/claude-design|Anthropic's Claude Design]]. The architecture: a Next.js 16 web frontend (chat + workspace + sandboxed preview + settings), a Node.js Express daemon with SQLite persistence (`.od/app.sqlite`), and a CLI runtime that auto-detects 15 coding agents on the user's PATH. The user picks a skill + design system + types a brief, the system surfaces a mandatory *question form* (Turn-1 discovery), then the chosen agent reads the SKILL.md + DESIGN.md + project metadata and emits a single `<artifact>` HTML rendered in a sandboxed iframe. Exports as HTML / PDF / PPTX / ZIP / Markdown.

The substantive intellectual contributions, beyond just being a working clone: the **anti-AI-slop machinery** (5-dimensional self-critique, P0/P1/P2 checklists, blacklists, brand-spec extraction protocol, honest placeholders), the **question-form-first workflow** (preventing 80% of design-redirect failures), the **9-section DESIGN.md schema** (richer than Refero's 5 sections), and the **BYOK proxy pattern** (SSE-normalizing across Anthropic/OpenAI/Azure/Google with SSRF blocking). Each is generalizable beyond design.

## Key takeaways

### Architecture is three-layer
- **Frontend** (Next.js 16 web app, Vercel-deployable): chat, file workspace, sandboxed `srcdoc` iframe preview, settings.
- **Daemon** (Node.js Express server, SQLite at `.od/app.sqlite`): manages projects, conversations, messages, tabs, templates.
- **Agent Runtime** (PATH-scan multi-agent): auto-detects 15 coding-agent CLIs (Claude Code, Codex, Devin, Cursor Agent, Gemini CLI, OpenCode, Qwen, Copilot, Hermes, Kimi, Pi, Kiro, Kilo, Mistral Vibe, DeepSeek), spawns whichever is available with real filesystem access.

The PATH-scan-agent-detection model is inherited from [[wiki/entities/multica|multica]] (lineage credit). The daemon-as-orchestrator model is the structural sibling of [[wiki/concepts/ai-os-pattern|nateherk's AI OS]] but specialized to design-artifact generation.

### 138 design systems with a 9-section DESIGN.md schema
Open Design ships **138 design systems** (the README's "129" is slightly stale; live count is 138 directories). Each follows a **9-section [[wiki/concepts/design-md|DESIGN.md]] schema**:

1. Visual Theme & Atmosphere — narrative philosophy
2. Color Palette & Roles — full token tables with hex + role semantics
3. Typography Rules — full size/weight/line-height/tracking tables, sometimes 20+ rows
4. Component Stylings — concrete buttons/cards/inputs/badges/navigation specs
5. Layout Principles — spacing system, grid, container, whitespace philosophy, border-radius scale
6. Depth & Elevation — multi-level treatment table with shadow philosophies
7. Do's and Don'ts — explicit Do/Don't rules
8. Responsive Behavior — breakpoint tables + touch-target rules + collapsing strategy
9. Agent Prompt Guide — quick color reference + example component prompts + iteration guide

This is **substantially richer than [[wiki/entities/refero|Refero]]'s 5-section schema** (color → typography → spacing/shape → components → philosophy). Sections 6-9 (depth, do/don't, responsive, agent-prompt-guide) are entirely new contributions to the format. Refero's Linear DESIGN.md is ~144 lines; Open Design's Linear DESIGN.md is ~370 lines — roughly 2.5× the content.

The 138 systems split roughly into three types:
- **~10 starters** (default, agentic, application, dashboard)
- **~70 product brands** (Apple, Stripe, Tesla, Linear, Vercel, Notion, Cohere, Discord, Figma, GitHub, Mistral AI, Mongo, OpenAI, PostHog, Raycast, Shopify, Spotify, Tesla, Uber, Vercel — plus many more)
- **~57 design styles/aesthetics** (brutalism, claymorphism, cosmic, doodle, editorial, futuristic, glassmorphism, minimal, mono, neobrutalism, neon, neumorphism, retro, vintage, etc.)

10 brands overlap with our 33 [[wiki/sources/refero-design-systems-for-ai-agents|Refero ingests]]: airbnb, apple, cursor, elevenlabs, linear-app, openai, raycast, stripe, superhuman, plus claude (Anthropic). For the overlapping brands, **Open Design's version is more thorough** — agents wanting maximum fidelity may prefer the Open Design DESIGN.md over the Refero Copy.md.

### 64 SKILL.md bundles spanning prototypes, decks, docs, and media
Skills follow [[wiki/concepts/claude-code-skills|Claude Code's]] `SKILL.md` convention. Drop a folder into `skills/` and it appears in the picker after daemon restart. Categories:

- **Prototypes**: web-prototype, web-prototype-taste-brutalist, web-prototype-taste-editorial, web-prototype-taste-soft, mobile-app, mobile-onboarding, gamified-app, dating-web, hatch-pet, saas-landing, kanban-board, dashboard, pricing-page, kami-landing, open-design-landing, wireframe-sketch, live-artifact, blog-post, docs-page
- **Decks** (HTML-PPT family): 21 different deck flavors — html-ppt-product-launch, html-ppt-pitch-deck, html-ppt-tech-sharing, html-ppt-weekly-report, html-ppt-knowledge-arch-blueprint, html-ppt-presenter-mode-reveal, html-ppt-graphify-dark-graph, html-ppt-hermes-cyber-terminal, html-ppt-obsidian-claude-gradient, html-ppt-taste-brutalist, html-ppt-taste-editorial, html-ppt-xhs-pastel-card, html-ppt-xhs-post, html-ppt-xhs-white-editorial, kami-deck, replit-deck, simple-deck, magazine-poster, image-poster, social-carousel, html-ppt-testing-safety-alert, html-ppt-dir-key-nav-minimal, html-ppt-course-module, open-design-landing-deck
- **Documents**: design-brief, pm-spec, eng-runbook, weekly-update, meeting-notes, hr-onboarding, finance-report, team-okrs, blog-post, docs-page, invoice, digital-eguide, email-marketing
- **Media**: hyperframes (HTML→MP4), motion-frames, sprite-animation, video-shortform, audio-jingle
- **Meta**: critique, tweaks, pptx-html-fidelity-audit

The catalog includes **guizang-ppt** (op7418's Magazine-style deck framework, bundled verbatim with attribution) and **hyperframes** (HeyGen OSS HTML→MP4 motion graphics with GSAP timeline composition).

### Anti-AI-slop machinery
The system enforces design discipline through five named mechanisms (see [[anti-ai-slop-machinery]]):

1. **Brand-spec extraction protocol**: locate → download → grep hex → codify → vocalize. Forces the agent to actually read brand assets, not infer.
2. **Five-dimensional self-critique** pre-emit gate: Philosophy / Hierarchy / Execution / Specificity / Restraint.
3. **P0/P1/P2 checklist enforcement** — priority gates on output.
4. **Blacklist** against AI-design clichés: purple gradients, generic icons, invented metrics.
5. **Honest placeholders** (em-dashes, grey blocks) over fake statistics.

This is the most explicit articulation in the wiki of "design discipline as agent contract." The mechanisms generalize beyond design (PRDs, runbooks, marketing copy could all use 5-dim self-critique + P0/P1/P2 + blacklists + honest placeholders).

### Question Form First (Turn 1 mandatory discovery)
Turn-1 mandatory: a discovery form locks **surface, audience, tone, brand context, and scale** before any design generation. The README claims this prevents "80% of redirects." See [[question-form-first]]. Connects to: clinical-form patterns, Cal.com booking forms, structured-input requirements in many domains. Generalizable beyond design.

### Visual Directions (5 deterministic directions)
Five preset palette+font-stack combinations the agent can adopt:
- **Editorial Monocle** — magazine-restraint
- **Modern Minimal** — neutral baseline
- **Tech Utility** — dev-tooling aesthetic
- **Brutalist** — raw concrete + system fonts
- **Soft Warm** — warm pastels + serif accents

Each provides an OKLch palette + font stack — *no model improvisation*. The agent picks one and stays consistent. See [[visual-directions]].

### BYOK Multi-Provider Proxy
SSE-normalizing proxy at `/api/proxy/{anthropic,openai,azure,google}/stream` with SSRF blocking (rejects loopback, link-local, RFC1918 destinations to prevent SSRF attacks via user-supplied URLs). See [[byok-proxy]]. Architectural sibling of [LiteLLM](https://github.com/BerriAI/litellm) and [Portkey](https://portkey.ai). Notable for its security-first design — an SSE proxy with SSRF blocking and SSE chunk normalization is a non-trivial piece of agent infrastructure.

### Artifact-First Workflow
The agent emits a single `<artifact>` HTML which renders in a sandboxed `srcdoc` iframe. Exports flow from there (HTML, PDF via Chrome headless, PPTX via html-to-pptx, ZIP, Markdown). See [[artifact-first-workflow]]. Inherited from Anthropic's Claude Design `<artifact>` convention; generalized here to any HTML output.

### MCP Server exposed for cross-repo agent queries
The daemon exposes an MCP server allowing coding agents in *other* repositories to query Open Design projects directly via `search_files`, `get_file`, `get_artifact` — without export-reimport loops. This is "design system as MCP-queryable knowledge." Sibling of [[wiki/entities/refero|Refero MCP]] but local-first.

### Lineage (4 named upstream projects)
Open Design explicitly credits four open-source antecedents:
- **huashu-design** (alchaincyf): design philosophy + Junior-Designer workflow + 5-step brand protocol.
- **guizang-ppt-skill** (op7418): magazine-style deck framework, bundled verbatim under `skills/guizang-ppt/`.
- **open-codesign** (OpenCoworkAI): streaming artifacts + sandboxed preview + todo progress + export formats.
- **multica** (multica-ai): daemon architecture + PATH-scan detection + agent-as-teammate model.

This explicit attribution is unusual and worth noting — most projects don't trace lineage like this. Implies an active "AI design tooling" OSS ecosystem worth tracking.

### Claude Design ZIP import
`POST /api/import/claude-design` ingests an Anthropic-originated Claude Design export ZIP — the migration path for users moving off the proprietary Anthropic product. Useful: confirms Claude Design has a ZIP export format, a fact not otherwise documented in this wiki.

## Notable quotes

> "Local-first, open-source alternative to Anthropic's Claude Design."

> "Question Form First… Turn 1 mandatory surfaces a discovery form locking surface, audience, tone, brand context, and scale before any design generation — preventing '80% of redirects' through upfront clarification."

> "Five deterministic directions (Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm) each providing OKLch palette + font stack — no model improvisation."

> "Brand-spec extraction protocol (locate → download → grep hex → codify → vocalize)."

## Sub-claims and details

### Live counts vs README counts (as of 2026-05-05)

The README claims 31 skills + 129 design systems; live counts via the GitHub API are higher:

| What | README says | Live count |
|---|---|---|
| Design systems | 129 | **138** |
| Skills | 31 | **64** |
| Agent CLIs detected | 15 | (matches) |
| Visual directions | 5 | (matches) |
| Device frames | 5 | (matches) |
| Media-gen prompts | 93 | (matches per README breakdown: 43 image + 39 Seedance + 11 HyperFrames) |

The README appears to lag behind the repo — worth re-fetching live counts when re-citing.

### Stack and runtime requirements

- Node ~24 + pnpm 10.33.x.
- Local: `pnpm tools-dev run web` (ephemeral or fixed ports).
- Vercel: web layer deployable; daemon must run locally.
- Electron: optional packaged desktop app for macOS (Apple Silicon) and Windows (x64).
- Desktop downloads at [open-design.ai](https://open-design.ai/).

### Media generation surfaces

- **gpt-image-2** (Azure/OpenAI): posters, avatars, infographics.
- **Seedance 2.0** (ByteDance): 15-second cinematic text-to-video and image-to-video.
- **HyperFrames** (HeyGen OSS): HTML→MP4 motion graphics with GSAP timeline composition.
- 93 ready-to-replicate prompts (43 image + 39 Seedance + 11 HyperFrames) with preview thumbnails and attribution.

### Repository structure

```
open-design/
├── apps/daemon/          Node.js Express server
├── apps/web/             Next.js 16 frontend
├── skills/               64 SKILL.md bundles
├── design-systems/       138 DESIGN.md systems
├── assets/frames/        5 shared device frames
├── prompt-templates/     93 media generation galleries
└── .od/                  Runtime data (gitignored)
```

### Five device frames

Pixel-accurate frames shared across skills: iPhone 15 Pro, Pixel, iPad Pro, MacBook, Browser Chrome. The "shared frames" convention prevents agents from re-drawing device chrome inconsistently — a small but useful discipline.

## Open questions and contradictions

- **README staleness**: counts are 8-33% off live. Suggests the project ships fast but the README isn't auto-generated. Worth re-fetching live counts on re-cite.
- **Brand attribution**: Open Design ships brand DESIGN.md files for many trademark-heavy brands (Apple, Tesla, BMW, Lamborghini, Bugatti, Ferrari, Nike, Mastercard, Starbucks, Spotify, Disney-adjacent characters). The legal status of these is unclear — Refero handles this through their own catalog approach, but Open Design's local-first model puts the trademark exposure on the user. Worth flagging when adopting for production work.
- **Agent CLI detection trust model**: PATH-scanning means *whichever agent is on PATH gets used*. Implication: an attacker who can place a malicious binary on a user's PATH ahead of the legitimate agent has full filesystem access. Standard PATH-trust limitations apply.
- **Anti-AI-slop generality**: the 5 mechanisms (5-dim self-critique, P0/P1/P2, blacklist, brand-spec extraction, honest placeholders) are specifically tuned to design output. Their portability to non-design domains (PRDs, marketing copy, code reviews, runbooks) is plausible but unproven.
- **The "Question Form First" effectiveness claim** (preventing "80% of redirects") is the project's prior, not measured. Worth re-testing as the project gains usage data.
- **138 brands is a lot**: ingesting all of them as brain entities would dilute the wiki. The brain's existing 33 Refero ingests stay authoritative for cited brands; specific Open Design brand DESIGN.md files should be ingested lazily when projects need them.

## Notes

- **This is the most architecturally substantive design-systems source in the wiki.** Where Refero is a curated *catalog* with an MCP server, Open Design is a *full application stack* — frontend + daemon + multi-agent runtime + media generation + MCP server. The wiki's design-tooling coverage is now a four-source cluster: [[wiki/sources/refero-design-systems-for-ai-agents|Refero]] (curated SaaS catalog), [[wiki/sources/clear_graphics-yc-unicorn-landing-pages|clear_graphics]] (YC landing-page patterns), [[wiki/sources/noisyb0y1-marketingskills-repo|marketingskills]] (marketing-tactic skill-pack), and Open Design (full open-source design platform).
- **The cross-cite with [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] is unusually rich**: Open Design instantiates the meta-pattern at *seven layers simultaneously* — SKILL.md (64 bundles), DESIGN.md (138 systems), claude.md/CLAUDE.md (project instructions), agent contract (per agent CLI), question-form output, artifact `<artifact>` HTML, MCP `get_file` responses. Each is markdown that a human wrote that an agent acts on.
- **For [[wiki/projects/vedge|Vedge]]**: Open Design is a viable replacement for relying on Refero MCP. Local-first + BYOK = no SaaS subscription. The Linear, Stripe, and Notion DESIGN.md files would each suffice for `vedge_landing` UI generation. The skill-pack for "saas-landing" is directly applicable to Vedge's landing site. The catch: Open Design adds a daemon dependency to the dev environment, so it's a heavier ask than just dropping a markdown file into `~/.claude/skills`.
- **Anti-slop machinery as a stand-alone export**: the brand-spec extraction protocol + 5-dim self-critique + P0/P1/P2 checklist + blacklist + honest placeholders could be extracted as a Claude Code skill in itself — applicable to *any* visual output task. Worth doing if Vedge's design work picks up.
- **Multi-agent CLI detection** (PATH scan + auto-spawn) is a powerful primitive that few systems implement. Most agent tools assume one specific agent (Claude Code only, or Cursor only); Open Design treats the agent as a runtime dependency picked at install time.

## Mentioned entities

- [[wiki/entities/open-design]] — the product.
- [[wiki/entities/nexu-io]] — the maintainer organization.
- [[wiki/entities/claude-design]] — Anthropic's proprietary product Open Design replicates.
- [[wiki/entities/refero]] — the closest sibling in the design-systems-for-AI-agents space.
- [[wiki/entities/anthropic]] — publisher of the proprietary Claude Design.
- **Lineage**: [[wiki/entities/huashu-design]], [[wiki/entities/guizang-ppt-skill]], [[wiki/entities/open-codesign]], [[wiki/entities/multica]].
- **Agent CLIs detected** (existing in wiki): [[wiki/entities/claude-code]], [[wiki/entities/cursor]].
- **Agent CLIs detected** (new stubs): [[wiki/entities/codex-cli]], [[wiki/entities/gemini-cli]], [[wiki/entities/opencode-cli]], [[wiki/entities/devin]], [[wiki/entities/qwen-cli]], [[wiki/entities/deepseek-cli]].

## Related concepts

- [[anti-ai-slop-machinery]] — the 5-mechanism design-discipline architecture this source codifies.
- [[question-form-first]] — Turn-1 mandatory discovery form pattern.
- [[byok-proxy]] — SSE-normalizing multi-provider proxy with SSRF blocking.
- [[visual-directions]] — 5 deterministic palette+font-stack alternatives.
- [[artifact-first-workflow]] — single-`<artifact>`-HTML emission + sandboxed-iframe rendering.
- [[design-md]] — the format extended here from 5 to 9 sections.
- [[claude-code-skills]] — the SKILL.md mechanism Open Design reuses for 64 skill bundles.
- [[markdown-as-agent-contract]] — Open Design instantiates the meta-pattern at seven layers.
- [[mcp-server]] — Open Design exposes one for cross-repo queries.

## Related sources

- [[wiki/sources/refero-design-systems-for-ai-agents]] — closest sibling source; curated SaaS catalog rather than full open-source platform.
- [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — landing-page-structure layer.
- [[wiki/sources/noisyb0y1-marketingskills-repo]] — sibling open-source skill-pack at the marketing-tactics layer.
