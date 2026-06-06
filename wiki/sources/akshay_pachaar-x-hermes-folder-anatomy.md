---
type: source
title: akshay_pachaar — The anatomy of the ~/.hermes folder
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/akshay_pachaar/status/2055629943891988719
source_type: x-thread
author: Akshay Pachaar (@akshay_pachaar)
source_date: 2026-05-13
raw_path: raw/Post by @akshay_pachaar on X.md
content_status: substantive-verbatim
tags: [hermes-agent, persistent-memory, three-tier-memory, soul-md, self-evolving-skills, cron, gepa, agent-filesystem, harness]
---

# akshay_pachaar — The anatomy of the ~/.hermes folder

> Akshay Pachaar's structural walkthrough of [[wiki/entities/hermes-agent|Hermes Agent]]'s `~/.hermes` home directory — the single folder that holds the agent's identity, memory, skills, automation, and runtime state — framed as the difference between treating Hermes as a black box and actually customizing it. Akshay's 2nd substantive post in the wiki (after *"You're doing RAG wrong"*).

## TL;DR

One folder, `~/.hermes`, controls everything a Hermes agent knows, remembers, and can do. The post maps its layout across six functional areas: **configuration** (`config.yaml`, `env`, `auth.json`, and the identity file `SOUL.md`), **knowledge** (`memories/` with `MEMORY.md` + `USER.md`), **capabilities** (`skills/` with the self-evolving learning loop), **runtime state** (`sessions/` + a FTS5-indexed `state.db` SQLite database), **automation** (`cron/`), and **extension + observability** (`plugins/`, `hooks/`, `skins/`, `logs/`). The load-bearing claim: understanding where identity, memory, skills, automation, and state physically live — and how they connect — is what makes Hermes customizable rather than opaque.

## Key takeaways

- `~/.hermes` is the single home directory that backs the entire agent — knowledge, memory, capabilities, automation, and state all live here.
- `config.yaml` is the **source of truth for everything non-secret**: model choice, terminal backend, tool enablement, MCP servers.
- Secrets are split out: `env` holds API keys and bot tokens; `auth.json` stores OAuth credentials.
- `SOUL.md` **occupies slot #1 in the system prompt, before anything else loads** — it defines the agent's identity (personality, tone, communication style, hard limits); everything the agent writes, creates, and remembers passes through this identity layer.
- `memories/` contains two small files: `MEMORY.md` (~2,200 chars — project conventions, tool quirks, lessons learned) and `USER.md` (~1,375 chars — the user's profile).
- Both memory files are **injected into the system prompt as frozen snapshots at session start**; when they fill up, the agent **consolidates** — merges entries, drops redundancy, keeps only what's dense and useful.
- `skills/` is "where the learning loop lives." Each skill is self-contained: a `SKILL.md` (the procedure), a `references/` folder (docs the agent reads), and `scripts/` (executable helpers).
- Skills come from three sources: **bundled** with Hermes, **downloaded from the hub** via `hub/`, or **created by the agent itself** during sessions.
- Hermes ships **687 skills across 18 categories**, and any GitHub repo can be added as a custom "tap."
- `sessions/` stores per-platform session metadata; `state.db` is a SQLite database with **FTS5 indexing that backs tier-2 memory** — this is what makes "what did we discuss three weeks ago?" work across CLI and messaging.
- `cron/` holds scheduled jobs in `jobs.json` and their outputs in `output/`; the **gateway daemon ticks every 60 seconds** and runs due jobs in isolated sessions. Schedules are described in plain English and Hermes converts them.
- `plugins/`, `hooks/`, and `skins/` are the user-customization surface; `logs/` provides `agent.log`, `gateway.log`, and `errors.log` for debugging.
- Most of these files are not manually edited — the value is knowing the layout, so you understand exactly where each subsystem lives and how it connects.
- The post points to a companion deep-dive (the quoted article) covering Hermes's architecture, memory system, self-evolving skills, **GEPA optimization**, and setting up multiple specialized agents.

## The ~/.hermes layout (as described)

| Area | Files / dirs | Role |
|---|---|---|
| Configuration | `config.yaml` | Non-secret source of truth: model, terminal backend, tools, MCP servers |
| | `env` | API keys, bot tokens |
| | `auth.json` | OAuth credentials |
| | `SOUL.md` | Identity layer — slot #1 in the system prompt |
| Knowledge | `memories/MEMORY.md` (~2,200 chars) | Project conventions, tool quirks, lessons learned |
| | `memories/USER.md` (~1,375 chars) | User profile |
| Capabilities | `skills/<name>/SKILL.md` + `references/` + `scripts/` | Self-contained abilities; learning loop |
| | `hub/` | Downloaded skills + custom GitHub taps |
| Runtime state | `sessions/` | Per-platform session metadata |
| | `state.db` | SQLite + FTS5; backs tier-2 searchable memory |
| Automation | `cron/jobs.json` + `cron/output/` | Scheduled jobs; gateway daemon ticks every 60s |
| Extension + observability | `plugins/`, `hooks/`, `skins/` | User-customization surface |
| | `logs/` (`agent.log`, `gateway.log`, `errors.log`) | Debugging |

## Notable quotes

> "one folder controls everything your hermes agent knows, remembers, and can do. understanding its layout is the difference between treating hermes as a black box and actually customizing it."

> "then there's SOUL.md. it occupies slot #1 in the system prompt, before anything else loads. it defines who the agent is: personality, tone, communication style, hard limits. everything the agent writes, creates, and remembers passes through this identity layer."

> "both get injected into the system prompt as frozen snapshots at session start. when they fill up, the agent consolidates: merges entries, drops redundancy, keeps only what's dense and useful."

> "skills/ is where the learning loop lives. each skill is a self-contained ability: a SKILL.md (the procedure), a references/ folder (docs the agent reads), and scripts/ (executable helpers)."

> *(reply to @odyzhou)* "The three-tier split is what makes it click. Tier 1 for always-in-context facts, Tier 2 for searchable history, external providers for deeper persistence."

> *(@MertLovesAI, in replies)* "the harness matters more than any single model behind it."

> *(reply to @MertLovesAI)* "Skills as self-contained units is the key design choice. It means you can swap the model underneath without rewriting your capabilities. The harness becomes the durable layer, the model becomes interchangeable."

## Notes

- This is the **filesystem-level companion** to the wiki's existing [[wiki/sources/nousresearch-hermes-agent|Hermes Agent repo source]]. Where the repo page describes the architecture conceptually (self-improving loop, plugin-first, `HERMES_HOME` isolation, prompt-cache discipline), this post walks the *physical directory* a user actually inspects. The two reconcile cleanly — `HERMES_HOME` is the env var that points at the `~/.hermes` directory anatomized here.
- The **three-tier memory model** is made explicit in Akshay's reply, not the post body: Tier 1 = always-in-context facts (the frozen `MEMORY.md` / `USER.md` snapshots + `SOUL.md`), Tier 2 = searchable history (`state.db` + FTS5), external providers = deeper persistence (the pluggable memory backends — honcho / mem0 / supermemory — noted in the repo source). This is the cleanest articulation of Hermes's memory layering in the wiki so far.
- `SOUL.md` is a notable design choice worth tracking: an explicit, slot-#1 identity file is the Hermes analogue of [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] applied to *persona* rather than *procedure*. It's adjacent to Karpathy's wiki-as-contract pattern but scoped to identity, and it co-evolves via the same consolidation mechanism as memory.
- The **consolidation behavior** ("when they fill up, the agent merges entries, drops redundancy, keeps only what's dense and useful") is the concrete mechanism behind Hermes's self-improving memory — and is structurally the same operation this wiki's [[CLAUDE]] schema prescribes for the human-maintained vault (refactor, merge, dedup). Hermes automates it; the wiki does it by hand.
- **687 skills across 18 categories** is a specific, citable count for the bundled skill library — higher than any prior Hermes skill-count in the wiki. Worth flagging as a moving number (the repo source cited a different figure; counts drift across versions).
- **GEPA optimization** is named but not explained in this post — only that the companion article covers it. GEPA (a reflective prompt-optimization method, per general knowledge) is *not yet a wiki concept*; flagged as a stub candidate. Do not assert specifics beyond "Hermes uses GEPA optimization, per Akshay's companion article" without ingesting that article.
- The `cron/` daemon **60-second tick** here differs from the repo source's mention of "3-minute hard interrupts" for cron jobs — these describe different things (scheduler poll interval vs per-job interrupt), but worth noting as a detail to reconcile if both are ingested as facts.
- **@MertLovesAI's "the harness matters more than any single model"** and Akshay's "swap the model underneath without rewriting your capabilities" are the same thesis as the repo source's model-agnostic framing and zodchiii's [[wiki/sources/zodchiii-10-claude-code-agents|trigger+prompt+output]] decomposition: the durable layer is the harness (skills, memory, identity, automation), the model is interchangeable. This recurs across the wiki's agent sources.
- For [[wiki/projects/helm|Helm]]: the `~/.hermes` layout is a reference design for an agent's persistent-state home directory — identity (`SOUL.md`) / memory / skills / cron / logs cleanly separated. Helm's FastAPI + APScheduler agents could borrow the directory taxonomy even if not the Hermes runtime.

## Mentioned entities

- [[wiki/entities/hermes-agent]] — the product whose home directory is anatomized.
- [[wiki/entities/akshay_pachaar]] — author (2nd substantive post — update entity).
- [[wiki/entities/nous-research]] — maintainer of Hermes Agent.
- [[wiki/entities/gepa]] — optimization method named as a topic of the companion article *(stub candidate)*.
- [[wiki/entities/mert-loves-ai]] — replier; "the harness matters more than any single model" + Pika agent-eats-the-subscription-stack thesis *(stub candidate)*.
- [[wiki/entities/odyzhou]] — replier; "stopped treating my agents like magic boxes" *(stub candidate)*.
- [[wiki/entities/pika]] — creative-tool company referenced in a quoted reply (agent-eats-the-interface bet) *(stub candidate)*.
- [[wiki/entities/model-context-protocol]] — `config.yaml` enables MCP servers.

## Related concepts

- [[three-tier-memory]] — Akshay's reply names the Tier 1 / Tier 2 / external-provider split directly *(stub candidate)*.
- [[soul-md]] — the slot-#1 identity file; persona-as-contract *(stub candidate)*.
- [[self-evolving-skills]] — the `skills/` learning loop (agent creates/refines its own skills) *(stub candidate)*.
- [[markdown-as-agent-contract]] — `SOUL.md` + `MEMORY.md` + `USER.md` are markdown contracts injected into the system prompt.
- [[hot-cache]] — the frozen-snapshot-at-session-start injection is the Hermes-internal analogue of the external `_hot.md` pattern.
- [[claude-code-skills]] — `SKILL.md` + `references/` + `scripts/` mirrors the Claude Code skill-pack structure.
- [[scheduled-automation]] — `cron/jobs.json` + 60s gateway daemon for unattended jobs.
- [[self-annealing]] — memory consolidation (merge/dedup/keep-dense) is the agent-internal version of self-improving directive files.

## Related sources

- [[wiki/sources/nousresearch-hermes-agent]] — the conceptual/architectural source for Hermes; this post is its filesystem-level companion.
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — same author's *"You're doing RAG wrong"* post.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — Hermes 4-job integration model + 5th wild LLM-wiki citation; pairs with the memory/skills layout here.
- [[wiki/sources/shannholmberg-hermes-agent-operator]] — Hermes operator playbook (fleet model, agent control room); operational layer above this folder anatomy.
- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — Hermes `/goal` command guide; the autonomous-worker layer that consumes this state.
