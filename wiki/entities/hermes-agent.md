---
type: entity
title: Hermes Agent
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://hermes-agent.nousresearch.com
aliases: [hermes, nousresearch-hermes-agent]
tags: [agent-cli, autonomous-agent, self-improving, open-source, mit, nous-research, persistent-memory, multi-platform]
---

# Hermes Agent

> MIT-licensed, self-hosted, model-agnostic autonomous AI agent by [[wiki/entities/nous-research|Nous Research]]. Released February 2026, 23k+ GitHub stars. The **only agent in the wiki with a built-in self-improving learning loop** — autonomously creates skills from experience, refines them in use, persists knowledge across sessions, searches its own past conversations, builds a deepening user model. Multi-platform (CLI + Telegram + Discord + Slack + WhatsApp + Signal + Email + 15+ surfaces from a single process). Listed as one of [[wiki/entities/open-design|Open Design]]'s 15 auto-detected agent CLIs.

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
- **Latest version**: v0.11.0 (May 2026) — full React/Ink CLI rewrite, pluggable transport architecture, native AWS Bedrock support, GPT-5.5 via Codex OAuth.
- **Stars**: 23,000+ (May 2026).
- **Stack**: Python, SQLite (cron / kanban / sessions), FTS5 (session search), Rich + prompt_toolkit (TUI), React/Ink (v0.11+ CLI).
- **Platforms**: Linux, macOS, WSL2, Termux (Android). Windows requires WSL2.
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

## Mentioned in

- [[wiki/sources/nousresearch-hermes-agent]] — canonical wiki source.
- [[wiki/sources/nexu-io-open-design]] — listed as one of 15 auto-detected agent CLIs.

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
