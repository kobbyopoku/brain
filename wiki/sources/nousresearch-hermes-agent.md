---
type: source
title: NousResearch/hermes-agent — Self-Improving Open-Source AI Agent
created: 2026-05-05
updated: 2026-07-22
content_status: substantive
source_url: https://github.com/NousResearch/hermes-agent
source_type: github-repo
author: Nous Research
source_date: 2026-05-05
raw_path: (none — fetched live README + AGENTS.md from GitHub)
tags: [agent-cli, autonomous-agent, self-improving, open-source, mit, nous-research, persistent-memory, multi-platform, foundational]
---

# NousResearch/hermes-agent — Self-Improving Open-Source AI Agent

> MIT-licensed, self-hosted, model-agnostic autonomous AI agent by [[wiki/entities/nous-research|Nous Research]]. Released February 2026, currently at v0.11.0 (May 2026), **150,000+ GitHub stars (per Shann Holmberg, mid-May 2026; verify before relying — was 23k+ early May 2026)**. The **only agent in the wiki with a built-in self-improving learning loop** — autonomously creates skills from experience, refines them during use, persists knowledge across sessions, searches its own past conversations, and builds a deepening user model. Multi-platform: CLI + Telegram + Discord + Slack + WhatsApp + Signal + Email + 15+ other surfaces from a single process. Listed as one of [[wiki/entities/open-design|Open Design]]'s 15 auto-detected agent CLIs.

## TL;DR

Hermes Agent is a structurally distinct entry in the agent-CLI category from products like [[wiki/entities/claude-code|Claude Code]], [[wiki/entities/codex-cli|Codex CLI]], or [[wiki/entities/gemini-cli|Gemini CLI]]. Three properties separate it:

1. **Persistent memory + self-improvement as core architecture, not a plugin** — every session contributes to the agent's accumulated skills and user model. Agent-curated retention with FTS5-indexed session search and LLM summarization.
2. **Model-agnostic by design** — works with Nous Portal, [OpenRouter](https://openrouter.ai) (200+ models), NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, AWS Bedrock, or any custom endpoint. Switching models mid-conversation via `/model` command.
3. **Multi-platform messaging gateway** — single agent process accessible from Telegram / Discord / Slack / WhatsApp / Signal / Email / CLI. Conversation continuity across surfaces.

Plus: native cron scheduler for unattended automation, isolated subagents for parallel workstreams, durable SQLite-backed kanban for multi-agent work queues, plugin-first extension architecture, agentskills.io-compatible skills format.

## Key takeaways

### The self-improving learning loop is the differentiating architectural choice

Most coding-agent CLIs are **stateless across sessions** — Claude Code reads `CLAUDE.md` + memory files at session start, but doesn't autonomously update them. Hermes inverts this:

- The agent **creates skills from experience** — observes its own successful task completions, abstracts them into reusable skill files, persists them to disk.
- The agent **refines skills during use** — when invoking a previously-created skill, it can update the skill based on the new context.
- The agent **nudges itself to persist knowledge** — explicit prompts to "should I save this for later?" trigger skill / memory writes.
- The agent **searches its own past conversations** — FTS5-indexed full-text search over session history; retrieval-augmented from prior interactions.
- The agent **builds a user model** — accumulated profile data (preferences, working style, project context) carries across sessions.

This is the closest agent in the wiki to the [[hot-cache]] + [[llm-wiki-pattern]] vision, but **built into the agent itself rather than an external markdown file the agent reads**. The wiki's existing concepts about "agent contract markdown" become a *passive* alternative to Hermes's *active* self-update.

**Sibling pattern in the wiki**: Saraev's [[self-annealing]] (the system-level property of [[doe-framework|DOE-framework]] workflows) achieves the same goal — *"systems that improve themselves over time without ongoing human intervention"* — via a different mechanism. Self-annealing encodes fixes into **directive markdown files** (durable, version-controlled, model-portable). Hermes encodes fixes into **agent-internal state** (autonomous, but bound to Hermes-as-runtime, less observable, harder to migrate). Both are valid; they make different trade-offs on the where-does-the-improvement-live axis.

### Plugin-first architecture (extension surface > core modification)

Per the AGENTS.md, the codebase explicitly warns developers to **prefer the plugin surface** (`~/.hermes/plugins/`) over modifying core files. Plugin systems exist for:

- General tools and lifecycle hooks
- Memory providers (honcho, mem0, supermemory, and others)
- Context engines and image generation
- CLI subcommands

This is Anthropic's [[wiki/entities/claude-code|Claude Code]] plugin pattern in spirit but more aggressively pushed — Claude Code allows plugins; Hermes architects *against* core modification.

### Profile isolation via `HERMES_HOME`

Strict isolation across multiple instances via the `HERMES_HOME` environment variable. Developers must use `get_hermes_home()` rather than hardcoding `~/.hermes`. This means **multiple Hermes profiles can coexist on the same machine** — one per project, per client, per user — without cross-contamination of memory, skills, or user models. Important for the [[ai-automation-services]] use case: a services builder running Hermes for multiple clients keeps each client's accumulated knowledge isolated.

### Prompt-cache preservation as a first-class concern

The AGENTS.md elevates **prompt-cache preservation** to an architectural rule:

> *"Caching validity is critical; changes to context, toolsets, or memory mid-conversation are prohibited except during explicit compression phases. Commands affecting system state default to deferred invalidation with optional `--now` flags."*

This is an explicit articulation of a discipline that's *implicit* in [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 430-hours study]]: prompt-cache invalidation is a major cost driver. Hermes builds the discipline directly into command semantics — by default, commands that modify state defer invalidation until natural cache-break points. Compare with the more naive default of "every state change invalidates immediately."

### Multi-platform messaging gateway

The Gateway component (`gateway/`) is a single Python process that receives messages from Telegram / Discord / Slack / WhatsApp / Signal / Email / 15+ other platforms and routes them all to the same agent. From the user's perspective: *"I sent the agent a message via Telegram on the train, then continued the conversation via CLI when I got home, and the agent had full context."*

This is structurally distinct from Anthropic's stack (Claude Desktop is one client per machine, Claude.ai is one cloud, no continuity between them). It's closer to a personal-Slack-bot model where the bot is your own AI agent with persistent memory.

### Toolset architecture (two-step registration)

Tools must be registered in **two steps**: definition via `tools/registry.py` (the tool exists) and exposure through `toolsets.py` (the tool is bundled into a specific platform's tool set). This separation ensures intentional capability bundling per platform. *Slack-context tools* aren't auto-available in *Telegram-context*; they must be explicitly bundled.

### Cron and Kanban for durable workstreams

Native cron scheduler: SQLite-backed scheduled jobs with 3-minute hard interrupts. Atomic task claiming for multi-agent work queues. Both are durable across restarts — important for the [[scheduled-automation]] use case where unattended tasks must survive process death.

### Agentskills.io-compatible skill format

Hermes skills follow the **agentskills.io** standards. This is a specification project (separate from Anthropic's Claude Code skills convention). Notable: Hermes positions itself as a participant in a *cross-vendor* skill-format standard, distinct from Claude-Code's vendor-specific [[wiki/concepts/skill-md|SKILL.md]] format. Worth tracking — if agentskills.io standardizes, Hermes / Open Design / others may converge on a common skill format.

### Migration path from OpenClaw

Hermes ships `hermes claw migrate` for users transitioning from OpenClaw — settings, memories, skills, API keys. The presence of this command implies OpenClaw is a meaningful predecessor product worth tracking; not currently in the wiki.

### Test discipline

The AGENTS.md mandates `scripts/run_tests.sh` for CI parity:

- Clears API keys (no leaked credentials).
- Redirects `HERMES_HOME` (no test-suite contamination of dev profile).
- Standardizes timezone/locale.
- Limits workers to 4 (matches cloud CI).

This is a tighter test-hermicity discipline than most coding-agent CLI repos. Worth flagging as a pattern for [[wiki/projects/vedge|Vedge]]'s test architecture.

## Notable quotes

> "The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

> *(AGENTS.md, on prompt-cache discipline)* "Caching validity is critical; changes to context, toolsets, or memory mid-conversation are prohibited except during explicit compression phases."

> *(AGENTS.md, on plugin-first development)* "Developers should prefer the plugin surface (`~/.hermes/plugins/`) for custom tools rather than modifying core files."

## Sub-claims and details

### Stack and runtime

- **License**: MIT.
- **Language**: Python (with React/Ink for the v0.11.0 CLI rewrite).
- **Persistence**: SQLite (cron, kanban, sessions).
- **Search**: FTS5 (SQLite full-text search) over session history.
- **Platforms**: Linux, macOS, WSL2, Android (via Termux). Windows requires WSL2.
- **Stars**: 150,000+ (mid-May 2026 per Shann Holmberg; verify before relying — was 23,000+ early May 2026; see [[wiki/entities/hermes-agent]]).
- **Latest release**: v0.11.0 — full React/Ink CLI rewrite, pluggable transport architecture, native AWS Bedrock support, five new inference paths, QQBot support, expanded plugins, GPT-5.5 via Codex OAuth, dashboard and reliability upgrades.

### CLI commands (partial)

- `hermes` — interactive CLI.
- `hermes setup` — full setup wizard.
- `hermes model` — choose / switch LLM provider.
- `hermes tools` — configure enabled tools.
- `hermes gateway` — start the messaging gateway (Telegram/Discord/Slack/WhatsApp/Signal/Email).
- `hermes claw migrate` — import from OpenClaw.

### Provider list (May 2026)

Documented model providers:
- Nous Portal
- [OpenRouter](https://openrouter.ai) (200+ aggregated models)
- NVIDIA NIM (Nemotron)
- Xiaomi MiMo
- z.ai / GLM
- Kimi / Moonshot
- MiniMax
- Hugging Face
- OpenAI (including GPT-5.5 via Codex OAuth)
- Anthropic
- AWS Bedrock (native, added v0.11.0)
- Custom endpoints

### Memory provider list

Hermes ships an abstract memory-provider interface with multiple implementations:
- honcho
- mem0
- supermemory
- (and others, per AGENTS.md)

This is genuinely interesting: rather than ship one memory backend, Hermes treats memory-as-pluggable, letting users pick the backend that fits their constraints (persistent SaaS / local SQLite / vector DB / etc.). Most other coding-agent CLIs hardcode a memory backend.

### Anti-patterns the AGENTS.md explicitly warns against

- Hardcoding `~/.hermes` paths (use `get_hermes_home()` instead).
- Introducing `simple_term_menu` (the AGENTS.md prefers `prompt_toolkit`).
- Using ANSI erase sequences in spinner code.
- Writing "change-detector" tests that fail on routine data updates.

The presence of named anti-patterns in the agent contract is itself an instance of [[anti-ai-slop-machinery]]'s Do/Don't discipline applied to a coding agent's own development.

## Open questions and contradictions

- **agentskills.io specification status**: Hermes claims compatibility with this skill format standard, but the specification's adoption beyond Hermes is unclear. If only Hermes implements it, "standard" is aspirational. If multiple agents implement it, this is a meaningful cross-vendor convergence worth tracking.
- **The "self-improving learning loop" is unmeasured**: Nous Research's claim is that the loop produces meaningful improvement over time; not validated against a baseline. A useful study: agent task-completion rate at week-1 vs week-4 of accumulated experience.
- **Memory contamination risk**: with persistent user-model + skill memory, an agent that learned bad patterns from past sessions may carry them forward. Hermes ships profile isolation but no documented "reset memory" workflow beyond manual.
- **Privacy implications of persistent multi-platform memory**: a single Hermes process with access to Telegram + Discord + Slack + WhatsApp + Signal + Email is a comprehensive personal data aggregator. The user trusts a self-hosted process more than a SaaS, but the data-aggregation surface is the same. Worth flagging for compliance-sensitive deployments (Vedge / clinical contexts).
- **Cross-platform conversation continuity** is a strong UX claim but the implementation likely has edge cases. What happens when Telegram and Slack messages arrive simultaneously? Conflict resolution semantics aren't documented in the README.
- **OpenClaw — the migration source — is not in the wiki**. The presence of `hermes claw migrate` implies OpenClaw is a meaningful predecessor / sibling. Worth investigating.
- **Hermes vs Open Design relationship**: Open Design auto-detects Hermes as one of 15 CLIs. The two products are architecturally complementary (Hermes provides agent runtime + persistent memory; Open Design provides design pipeline + skills + DESIGN.md catalog). Unclear if there's official integration beyond PATH-detection.

## Notes

- **Hermes is the closest agent in the wiki to the [[llm-wiki-pattern]] philosophy implemented as code.** Karpathy's pattern says "use a markdown wiki the LLM maintains"; Hermes says "the agent maintains its own evolving knowledge directly." The two approaches converge on the same goal (persistent agent learning across sessions) via different mechanisms (external markdown vs internal agent state).
- **The combination Hermes + Open Design is a fully-OSS, fully-local, persistent-memory, multi-agent, multi-platform AI workflow.** Hermes provides the agent runtime; Open Design provides the design pipeline and skill bundles. Both are MIT/Apache. Both run locally. Both BYOK across providers. For users wanting maximum architectural ownership, this is the pairing.
- **The prompt-cache discipline in AGENTS.md is unusually explicit.** Most agent codebases don't elevate cache validity to an architectural rule; Hermes does. Worth applying as a pattern: command semantics should default to *deferred* state changes with explicit `--now` opt-in, not immediate state changes.
- **Multi-provider via single command (`/model` to switch)** is a UX primitive most agents lack. Most agent CLIs require restart or config-file edit to switch providers. Hermes's `/model` is mid-conversation switching — useful for cost-routing (use cheap model for setup, expensive for the hard problem) and capability-routing (use Claude for reasoning, GPT for vision).
- **150k+ stars (per Shann Holmberg; verify) is exceptional traction** for an agent that's only ~3 months old (Feb 2026 release → May 2026 status). For comparison, Anthropic's [[wiki/entities/anthropic-skills|skill collection]] and [[wiki/entities/superpowers|superpowers]] have substantially smaller star counts. Hermes is a real entrant in the agent-CLI category, not a side project.
- **For [[wiki/projects/vedge|Vedge]] specifically**: Hermes is *promising but premature*. The persistent-memory model is great for clinical-knowledge retention but the multi-platform messaging gateway introduces a comprehensive personal-data-aggregation surface that's the wrong shape for PHI-bearing systems. Vedge should track Hermes for v2-v3 of internal tooling, not adopt today.
- **Comparison with Claude Code**: Hermes is *more autonomous* (self-improving loop, scheduled cron) but *less integrated* (no first-party Anthropic-stack alignment, no Claude.ai surface). Different bets on the agent-as-tool vs agent-as-employee spectrum. Claude Code is "tool you wield"; Hermes is "agent you delegate to."

## Mentioned entities

- [[wiki/entities/hermes-agent]] — the product.
- [[wiki/entities/nous-research]] — the maintainer.
- [[wiki/entities/openrouter]] — multi-model aggregator Hermes integrates with.
- [[wiki/entities/open-design]] — auto-detects Hermes as one of 15 CLIs.
- [[wiki/entities/claude-code]], [[wiki/entities/codex-cli]] — sibling agent CLIs (different architectural bets).
- [[wiki/entities/anthropic]], [[wiki/entities/openai]] — providers Hermes integrates with.

## Related concepts

- [[hot-cache]] — Hermes's built-in self-update is the active version of the external `_hot.md` pattern.
- [[self-annealing]] — Saraev's directive-encoded self-improvement; sibling mechanism to Hermes's agent-internal state. Same goal, different where-does-improvement-live trade-off.
- [[llm-wiki-pattern]] — Hermes is the agent-internal version of Karpathy's external-wiki pattern.
- [[claude-code-skills]] — Hermes uses agentskills.io-compatible skills (different format from Claude Code's SKILL.md).
- [[byok-proxy]] — Hermes's model-agnostic design IS a BYOK proxy at the agent layer.
- [[claude-code-overhead-patterns]] — Hermes's prompt-cache-preservation discipline is the architectural answer to the cache-invalidation cost pattern.
- [[scheduled-automation]] — Hermes ships a native cron scheduler with SQLite persistence.
- [[multi-agent-orchestration]] — Hermes spawns isolated subagents for parallel workstreams.
- [[markdown-as-agent-contract]] — Hermes's AGENTS.md is itself an instance.
- [[anti-ai-slop-machinery]] — Hermes's AGENTS.md "anti-patterns to avoid" section is structurally the Do/Don't mechanism applied to development.

## Related sources

- [[wiki/sources/nexu-io-open-design]] — Open Design auto-detects Hermes; the two products pair as fully-OSS local-first stack.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — Hermes's prompt-cache discipline is the structural answer to Mnilax's measured cost patterns.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — Hermes is the agent-internal alternative to Karpathy's external-markdown-wiki approach.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — nateherk's hot-cache `_hot.md` is the external-file ancestor of Hermes's internal-agent-state self-update.
