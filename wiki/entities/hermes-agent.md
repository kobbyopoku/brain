---
type: entity
title: Hermes Agent
entity_type: product
created: 2026-05-05
updated: 2026-06-06
website: https://hermes-agent.nousresearch.com
aliases: [hermes, nousresearch-hermes-agent]
tags: [agent-cli, autonomous-agent, self-improving, open-source, mit, nous-research, persistent-memory, multi-platform]
---

# Hermes Agent

> MIT-licensed, self-hosted, model-agnostic autonomous AI agent by [[wiki/entities/nous-research|Nous Research]]. Released February 2026, **150,000+ GitHub stars as of May 2026** (per Shann Holmberg — verify before relying; this is a 6× jump from earlier 23k+ figure). **#1 on OpenRouter for global token usage**. The **only agent in the wiki with a built-in self-improving learning loop** — autonomously creates skills from experience, refines them in use, persists knowledge across sessions, searches its own past conversations, builds a deepening user model. Multi-platform (CLI + Telegram + Discord + Slack + WhatsApp + Signal + Email + 20+ surfaces from a single process). Listed as one of [[wiki/entities/open-design|Open Design]]'s 15 auto-detected agent CLIs.

## Profile

Hermes Agent is structurally distinct from other coding-agent CLIs in the wiki ([[wiki/entities/claude-code|Claude Code]], [[wiki/entities/codex-cli|Codex CLI]], [[wiki/entities/gemini-cli|Gemini CLI]], etc.) on three architectural axes:

1. **Persistent memory + self-improvement as core architecture, not a plugin.**
2. **Model-agnostic by design** — works with Nous Portal / OpenRouter / NVIDIA NIM / Xiaomi MiMo / Kimi / MiniMax / Hugging Face / OpenAI / Anthropic / AWS Bedrock / custom endpoints. `/model` switches mid-conversation.
3. **Multi-platform messaging gateway** — single process accessible from any of 15+ messaging platforms.

Plus: native cron scheduler, isolated subagents for parallel workstreams, durable SQLite-backed kanban for multi-agent work queues, plugin-first extension architecture, agentskills.io-compatible skills format.

## Key facts

- **Repo**: https://github.com/NousResearch/hermes-agent
- **Website**: https://hermes-agent.nousresearch.com
- **License**: MIT.
- **Maintainer**: [[wiki/entities/nous-research|Nous Research]].
- **Released**: February 2026.
- **Latest version (verified 2026-05-10)**: **v0.13.0** "The Tenacity Release" (2026-05-07). Earlier wiki note of v0.11.0 (full React/Ink CLI rewrite, pluggable transport architecture, native AWS Bedrock support, GPT-5.5 via Codex OAuth) was current at 2026-05-05 ingest; bumped 0.11 → 0.12 → 0.13 in the intervening days.
- **Stars**: 23,000+ (early May 2026) → **150,000+ (mid-May 2026 per Shann Holmberg)**. 6× growth in ~2 weeks; verify against actual GitHub before relying. **#1 on OpenRouter** for global token usage.
- **Stack**: Python ≥3.11, SQLite (cron / kanban / sessions), FTS5 (session search), Rich + prompt_toolkit (TUI), React/Ink (v0.11+ CLI).
- **Platforms**: Linux, macOS, WSL2, Termux (Android). Windows requires WSL2.
- **Distribution**: **Not on pypi.** Two install paths:
  - **Curl install script** (intended end-user path): `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash` (PowerShell variant for Windows).
  - **Pip from git** (programmatic-embedding path, e.g. for [[wiki/projects/helm|Helm]]): `pip install "hermes-agent @ git+https://github.com/NousResearch/hermes-agent.git@vX.Y.Z"`. The repo's own `pyproject.toml` declares the project as `hermes-agent` so this works without a fork.
- **Console scripts** (declared in repo `pyproject.toml`):
  - `hermes` → `hermes_cli.main:main` (interactive TUI).
  - `hermes-agent` → `run_agent:main` (non-interactive agent invocation).
  - `hermes-acp` → `acp_adapter.entry:main` (ACP adapter).
- **Top-level importable packages**: `agent`, `tools`, `hermes_cli`, `gateway`, `tui_gateway`, `cron`, `acp_adapter`, `plugins`, `providers`. Programmatic embedders import `agent.AIAgent` (or via `run_agent:main`).
- **Notable runtime deps** (heavy footprint to be aware of when embedding): `openai`, `anthropic`, `rich`, `prompt_toolkit`, `pydantic`, `httpx[socks]`, `exa-py`, `firecrawl-py`, `parallel-web`, `fal-client`, `edge-tts`, `croniter`, `PyJWT[crypto]`, `tenacity`, `jinja2`, `pyyaml`, `ruamel.yaml`. Pulling Hermes into a server image carries the full TUI + tool surface even if only `agent.AIAgent` is used.
- **Docs**: https://github.com/mudrii/hermes-agent-docs (community).
- **Awesome list**: https://github.com/0xNyk/awesome-hermes-agent.

## Architecture (per AGENTS.md)

Three core components:

- **AIAgent** (`run_agent.py`): synchronous conversation loop, ~60 init parameters, tool-calling iterations, budget tracking.
- **HermesCLI** (`cli.py`): interactive terminal interface using Rich panels and prompt_toolkit, animated spinners.
- **Gateway** (`gateway/`): multi-platform messaging adapter for Telegram/Discord/Slack/WhatsApp/Signal + 15+ others.

Plus pluggable subsystems:

- **Memory providers** (honcho, mem0, supermemory, etc.) — pluggable backends.
- **Context engines** — different retrieval strategies.
- **Image generation** — pluggable.
- **CLI subcommands** — extensible.
- **Toolset architecture** — two-step registration (definition + bundling per platform).
- **Skin system** — data-driven theming.

## Distinguishing capabilities

### Self-improving learning loop

The most architecturally distinctive feature:

- **Creates skills from experience** — observes successful task completions, abstracts them into reusable skills.
- **Refines skills during use** — updates skills based on new context.
- **Nudges itself to persist knowledge** — explicit prompts to "save this for later" trigger memory writes.
- **Searches past conversations** — FTS5-indexed full-text search over session history.
- **Builds user model** — accumulated profile carries across sessions.

Compare with [[wiki/concepts/hot-cache|hot-cache]] (external `_hot.md` file the agent reads) and [[wiki/concepts/llm-wiki-pattern|LLM Wiki pattern]] (external markdown wiki the agent maintains): Hermes is the **agent-internal** version of these external-markdown patterns.

### Profile isolation via `HERMES_HOME`

Multiple instances coexist on the same machine without cross-contamination of memory / skills / user models. Important for [[wiki/concepts/ai-automation-services|AI automation services]] use case — services builders can run isolated profiles per client.

### Prompt-cache preservation as architectural rule

The AGENTS.md elevates cache-validity to a first-class concern: state-changing commands default to *deferred* invalidation with optional `--now` flags. This is the structural answer to [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 430-hours measurement]] of cache-invalidation cost patterns.

### Multi-platform messaging gateway

Single Hermes process receives messages from Telegram / Discord / Slack / WhatsApp / Signal / Email / 15+ other platforms and routes them to the same agent. Conversation continuity across surfaces.

### Native cron + kanban

Durable SQLite-backed scheduled jobs (3-min hard interrupts) and atomic-task-claiming work queues. Both survive process restarts.

### agentskills.io-compatible skills

Hermes participates in the agentskills.io specification (cross-vendor skill format), distinct from Claude Code's vendor-specific [[wiki/concepts/skill-md|SKILL.md]].

## Provider list

- Nous Portal
- [OpenRouter](https://openrouter.ai) (200+ aggregated models)
- NVIDIA NIM (Nemotron)
- Xiaomi MiMo
- z.ai / GLM
- Kimi / Moonshot
- MiniMax
- Hugging Face
- OpenAI (GPT-5.5 via Codex OAuth)
- [[wiki/entities/anthropic|Anthropic]]
- AWS Bedrock (native, v0.11+)
- Custom endpoints

## Positions and claims

- **Self-improvement as core architecture, not plugin.** Other agent CLIs treat memory as add-on; Hermes makes it the spine.
- **Model-agnostic is not a feature, it's the default.** No vendor lock-in.
- **Plugin surface > core modification.** Developer doctrine: extend via `~/.hermes/plugins/`.
- **Cache-validity is sacred.** Default to deferred state changes; opt-in `--now` for immediate.
- **One agent, many surfaces.** Telegram + CLI + Slack are *user interfaces* to the same agent state, not separate bots.

## v0.14 Foundation Release — `/goal` command (per IBuzovskyi, 2026-05-19)

Hermes v0.14 introduced the **`/goal`** command, promoting the agent from reactive chat to **persistent autonomous worker**. User sets a long-term objective; Hermes breaks it down, executes tools, iterates, continues until completion (or `/goal pause` / `/goal clear`). Seven commands form the interface (`/goal` / `/goal status` / `/goal pause` / `/goal resume` / `/goal clear` / `/subgoal <text>` / `/handoff <platform>`). Configurable via `hermes config set goals.max_turns 500`. See [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]].

## Bundled skill count (per Shann Holmberg, 2026-05-15)

**123 bundled skills out-of-box** including: GitHub PRs / Obsidian / Google Workspace / Linear / Notion / Typefully / Perplexity / Deep Research / browser control / web scraping / vision / voice / scheduling — *plus the closed learning loop that writes new skills as the agent works*. Earlier wiki coverage estimated lower; Shann's number supersedes.

Plus: **70+ built-in tools in the gateway**, 300+ models via tool gateway, 6 deployment targets (local / Docker / SSH / Daytona / Singularity / Modal), **20+ messaging surfaces**.

## The `~/.hermes` home directory (per akshay_pachaar, 2026-05-13)

All of a Hermes agent's knowledge, memory, capabilities, automation, and state live in a single `~/.hermes` home directory. File-by-file anatomy:

- **`config.yaml`** — source of truth for non-secret settings: model choice, terminal backend, tool enablement, MCP servers.
- **Secret split** — `env` holds API keys and bot tokens; `auth.json` stores OAuth credentials.
- **`SOUL.md`** — occupies slot #1 in the system prompt, before anything else loads; defines the agent's identity (personality, tone, communication style, hard limits).
- **`memories/MEMORY.md`** (~2,200 chars) — project conventions, tool quirks, lessons learned. **`memories/USER.md`** (~1,375 chars) — the user profile. Both are injected into the system prompt as frozen snapshots at session start; when full, the agent consolidates them (merge entries, drop redundancy, keep dense/useful).
- **Skills** — each is self-contained: a `SKILL.md` procedure, a `references/` folder, and a `scripts/` folder of executable helpers. Three sources: bundled, downloaded from the hub via `hub/`, or created by the agent itself during sessions. **687 skills across 18 categories**; any GitHub repo can be added as a custom tap.
- **`sessions/`** — per-platform session metadata. **`state.db`** — SQLite database with FTS5 indexing that backs tier-2 memory and enables cross-CLI/messaging recall.
- **`cron/`** — scheduled jobs in `jobs.json`, outputs in `output/`; the gateway daemon ticks every 60 seconds and runs due jobs in isolated sessions; schedules are described in plain English.
- **`plugins/`, `hooks/`, `skins/`** — the user-customization surface. **`logs/`** — `agent.log`, `gateway.log`, `errors.log`.

## `/goal` orchestrator role (per Shubham Saboo)

Hermes has had `/goal` built in "for a while" (predating Codex and Claude Code adopting it). As orchestrator it creates goal cards on a Kanban board, picks the right worker per card, and runs goals in the background. Each Kanban card stores the process id/PID, repo, and done criteria. It **verifies** a worker's output by inspecting filesystem, tests, build, and git state rather than trusting self-reports. It can be instructed to install other tools (Codex, Claude Code) and log the user in — "setup is just another goal." See [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]].

## Mentioned in

- [[wiki/sources/nousresearch-hermes-agent]] — canonical wiki source.
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — anatomizes the `~/.hermes` home directory file-by-file (config / secrets / SOUL.md / memories / skills / sessions / state.db / cron / customization surface).
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — Hermes as `/goal` orchestrator: Kanban cards, worker selection, background goals, output verification.
- [[wiki/sources/nexu-io-open-design]] — listed as one of 15 auto-detected agent CLIs.
- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — `/goal` v0.14 operational guide.
- [[wiki/sources/shannholmberg-hermes-agent-operator]] — operator playbook + 4-level fleet model + control-room pattern + 5-layer SEO agent architecture.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — 4-job integration model + 12 specific integrations + stacked-workflow examples.
- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — commercial use case ($10K/mo clipping pages); Hermes orchestrates Vugola + Postiz.

## Related entities

- [[wiki/entities/nous-research]] — maintainer.
- [[wiki/entities/openrouter]] — primary multi-model aggregator Hermes integrates with.
- [[wiki/entities/open-design]] — auto-detects Hermes; complementary OSS stack.
- **Sibling agent CLIs** (different architectural bets): [[wiki/entities/claude-code]], [[wiki/entities/codex-cli]], [[wiki/entities/gemini-cli]], [[wiki/entities/opencode-cli]], [[wiki/entities/devin]], [[wiki/entities/qwen-cli]], [[wiki/entities/deepseek-cli]].
- **Providers**: [[wiki/entities/anthropic]], [[wiki/entities/openai]].

## Related concepts

- [[hot-cache]] — Hermes's built-in self-update is the *active* version of the external `_hot.md` pattern.
- [[llm-wiki-pattern]] — Hermes is the agent-internal version of the external-wiki pattern.
- [[claude-code-skills]] — adjacent (different skill format: agentskills.io vs SKILL.md).
- [[byok-proxy]] — Hermes IS a BYOK proxy at the agent layer.
- [[claude-code-overhead-patterns]] — Hermes's cache-discipline is the architectural answer to measured cost patterns.
- [[scheduled-automation]] — native cron support.
- [[multi-agent-orchestration]] — isolated subagents for parallel workstreams.
- [[markdown-as-agent-contract]] — Hermes's AGENTS.md is itself an instance.
- [[anti-ai-slop-machinery]] — Hermes's AGENTS.md anti-patterns section is the Do/Don't mechanism applied to development.
