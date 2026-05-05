---
type: entity
title: Open Design
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://open-design.ai
aliases: [open-design, nexu-io/open-design]
tags: [design-systems, claude-design-alternative, open-source, apache-2, multi-agent, claude-code-skills, design-md, mcp-server]
---

# Open Design

> Apache-2.0 open-source platform that replicates the artifact-first workflow of [[wiki/entities/claude-design|Anthropic's Claude Design]] without proprietary lock-in. Local-first three-layer system (Next.js web + Node Express daemon + agent runtime), 138 design systems, 64 SKILL.md bundles, 15 auto-detected agent CLIs, BYOK multi-provider proxy, sandboxed iframe preview, SQLite project persistence, and an exposed MCP server. Maintained by [[wiki/entities/nexu-io|nexu-io]].

## Profile

Open Design is the most architecturally substantive design-tooling source in the wiki. Where [[wiki/entities/refero|Refero]] is a curated SaaS catalog plus MCP server, Open Design is a full application stack — frontend + daemon + multi-agent runtime + media generation surfaces + MCP server — implementing the artifact-first workflow Anthropic introduced with [[wiki/entities/claude-design|Claude Design]].

The project explicitly traces lineage to four upstream OSS projects ([[wiki/entities/huashu-design|huashu-design]], [[wiki/entities/guizang-ppt-skill|guizang-ppt-skill]], [[wiki/entities/open-codesign|open-codesign]], [[wiki/entities/multica|multica]]) — implying an active "AI design tooling" OSS ecosystem worth tracking.

## Key facts

- **Repo**: https://github.com/nexu-io/open-design
- **License**: Apache-2.0
- **Website**: https://open-design.ai
- **Maintainer**: [[wiki/entities/nexu-io]]
- **Stack**: Node ~24, pnpm 10.33.x, Next.js 16, Express, SQLite (`.od/app.sqlite`), Electron (optional packaged desktop for macOS Apple Silicon + Windows x64).
- **Live counts** (as of 2026-05-05; README is slightly stale):
  - **138 design systems** (~10 starters + ~70 product brands + ~57 design styles).
  - **64 SKILL.md bundles** (prototypes, decks, docs, media, meta).
  - **15 auto-detected agent CLIs**: Claude Code, Codex, Devin, Cursor Agent, Gemini CLI, OpenCode, Qwen, Copilot, Hermes, Kimi, Pi, Kiro, Kilo, Mistral Vibe, DeepSeek.
  - **5 visual directions**: Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm.
  - **5 device frames**: iPhone 15 Pro, Pixel, iPad Pro, MacBook, Browser Chrome.
  - **93 media-gen prompts**: 43 image (gpt-image-2) + 39 Seedance + 11 HyperFrames.

## Architecture

Three integrated layers:

1. **Frontend** (Next.js 16, Vercel-deployable): chat interface, file workspace, sandboxed `srcdoc` iframe preview, settings.
2. **Daemon** (Node.js Express + SQLite): manages projects, conversations, messages, tabs, templates at `.od/app.sqlite`.
3. **Agent Runtime** (PATH-scan multi-agent): auto-detects 15 CLIs and spawns whichever is available.

Plus:
- **BYOK multi-provider proxy** at `/api/proxy/{anthropic,openai,azure,google}/stream` — normalizes SSE chunks, blocks SSRF.
- **Exposed MCP server** with `search_files`, `get_file`, `get_artifact` for cross-repo agent queries.
- **Claude Design ZIP import** at `POST /api/import/claude-design` — migration path from Anthropic.

## Design system summary (it's the meta — 138 systems with a 9-section schema)

Each Open Design DESIGN.md follows a **9-section schema**:

1. Visual Theme & Atmosphere — narrative philosophy
2. Color Palette & Roles — full token tables with semantic roles
3. Typography Rules — full type scale tables (often 20+ rows)
4. Component Stylings — concrete buttons/cards/inputs/badges/navigation
5. Layout Principles — spacing, grid, container, whitespace, radius
6. Depth & Elevation — multi-level treatment with shadow philosophy
7. Do's and Don'ts — explicit Do/Don't rules
8. Responsive Behavior — breakpoints, touch targets, collapsing
9. Agent Prompt Guide — quick color reference + example prompts + iteration guide

This is **substantially richer than Refero's 5-section schema**. Sections 6-9 (depth, do/don't, responsive, agent-prompt-guide) are entirely new contributions to the format.

## Positions and claims

- **Local-first beats cloud-first for design tooling.** Sandboxed preview, SQLite persistence, BYOK proxy mean no data leaves the machine without explicit configuration.
- **The agent CLI is a runtime dependency picked at install time, not a build-time choice.** PATH-scan + auto-spawn means the system works with whatever agent the user has installed.
- **Question Form First prevents 80% of design redirects.** *(Author's claim, not measured.)*
- **Five deterministic visual directions beat unconstrained generation.** OKLch palette + font stack per direction, no model improvisation.
- **Anti-AI-slop machinery is a five-mechanism stack**: brand-spec extraction protocol + 5-dim self-critique + P0/P1/P2 checklist + blacklist + honest placeholders.
- **Skill-as-folder is the right primitive.** Drop `skills/<name>/SKILL.md` and the daemon picks it up after restart.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source.

## Related concepts

- [[anti-ai-slop-machinery]] — the discipline architecture this product codifies.
- [[question-form-first]] — the Turn-1 discovery pattern.
- [[byok-proxy]] — SSE-normalizing multi-provider proxy.
- [[visual-directions]] — deterministic palette+font alternatives.
- [[artifact-first-workflow]] — single-artifact-HTML emission.
- [[design-md]] — the format extended from 5 to 9 sections.
- [[claude-code-skills]] — the SKILL.md mechanism reused.
- [[markdown-as-agent-contract]] — instantiated at 7 layers simultaneously.
- [[mcp-server]] — exposed for cross-repo queries.

## Related entities

- [[wiki/entities/claude-design]] — the proprietary product Open Design replicates.
- [[wiki/entities/refero]] — closest sibling in the design-systems-for-AI-agents space.
- [[wiki/entities/anthropic]] — publisher of Claude Design.
- [[wiki/entities/nexu-io]] — maintainer.
- **Lineage**: [[wiki/entities/huashu-design]], [[wiki/entities/guizang-ppt-skill]], [[wiki/entities/open-codesign]], [[wiki/entities/multica]].
- **Agent CLIs**: [[wiki/entities/claude-code]], [[wiki/entities/cursor]], [[wiki/entities/codex-cli]], [[wiki/entities/gemini-cli]], [[wiki/entities/opencode-cli]], [[wiki/entities/devin]], [[wiki/entities/qwen-cli]], [[wiki/entities/deepseek-cli]], [[wiki/entities/hermes-agent]].
- **Sibling skill-packs**: [[wiki/entities/marketingskills-repo]] (marketing tactics), Refero (design tokens). Open Design is the third substantive non-Anthropic skill-pack in the wiki — and the largest.
