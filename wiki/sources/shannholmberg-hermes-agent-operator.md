---
type: source
title: Shann Holmberg — How to Become a Hermes Agent Operator
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/shannholmberg/status/2055335043904492011
source_type: x-thread
author: Shann Holmberg (shannholmberg)
source_date: 2026-05-15
raw_path: raw/How to Become a Hermes Agent Operator.md
content_status: substantive-verbatim
tags: [hermes-agent, agent-operations, control-room, multi-agent, fleet-management, vps, marketing-ops]
---

# Shann Holmberg — How to Become a Hermes Agent Operator

> Shann Holmberg's complete operational playbook for Hermes Agent — covering the **4-level fleet model** (one agent → direct specialists → orchestrator → automated team), the **agent control room** pattern (a side control-plane folder `/root/vps-agents/` documenting the whole fleet), the **prototype → production methodology**, and the **specific 5-layer SEO agent architecture** Shann ships at Espressio. Public template: [github.com/shannhk/hermes-agent-control-room](https://github.com/shannhk/hermes-agent-control-room). Quotes Hermes at **150,000 GitHub stars** (massive jump from earlier figures) and **#1 on OpenRouter** for global token usage.

## TL;DR

**Hermes Agent (per Shann's framing)**: autonomous agent that gets more capable the longer it runs. Three components:

- **Brain**: `~/.hermes/memories/` with `MEMORY.md` (stable business facts) + `USER.md` (stable facts about you). Inject at session start. Sessions stored in SQLite; recall is full-text searchable.
- **Personality**: `soul.md` per agent. Same brain underneath; different voice per role.
- **Skillset**: 123 bundled skills out-of-box (GitHub PRs / Obsidian / Google Workspace / Linear / Notion / Typefully / Perplexity / Deep Research / browser control / scraping / vision / voice / scheduling). Hermes **writes its own new skills as it works**.

**Plus**:
- Tool gateway: 300+ models, 70+ tools, MCP integration.
- 20+ messaging surfaces: Telegram / Discord / Slack / email / voice / CLI.
- 6 deployment targets: local / Docker / SSH / Daytona / Singularity / Modal.

**Hermes vs OpenClaw (Shann's framing)**: *"Hermes is rails. opinionated defaults, batteries included, productive on day one with minimal setup, the agent does more thinking for you. OpenClaw is Linux. primitives, guarantees, explicit control, the agent does exactly what you told it to and nothing more."* Both valid; he runs Hermes because *"bundled defaults compound."*

## The 4-level fleet model

The mental model has four parts:

1. **You** — the operator (direct access).
2. **Agent control room** — side control plane at `/root/vps-agents/` documenting the whole fleet (not where work happens).
3. **Hermes agents** — the workers; some are specialists, one optionally an orchestrator.
4. **Agent task bus** — optional handoff between orchestrator and specialists.

The four levels:

| Level | Shape | Best for |
|---|---|---|
| **1** | One agent. Control room (optional) documents that one. | Initial setup, personal Hermes, root install docs, simple Docker migration. |
| **2** | Multiple direct specialists, talk to each directly, no orchestrator yet. | Clear role separation; testing which agents are useful; avoid premature orchestration. |
| **3** | Add a Hermes orchestrator as a front door. Can still talk directly to specialists. Orchestrator reads the control room. | Cross-functional work; delegation; one main interface for multi-agent workflows. |
| **4** | Same shape as 3, plus recurring workflows on cron and automation. | Weekly SEO reports; content ops; server health; backup verification; scheduled cross-agent workflows. |

**Trap**: don't reach for an orchestrator before specialists prove useful. *"Spin up two or three, run them directly, and only add an orchestrator when you find yourself wanting one front door."*

## Storage split that matters

```
/root/vps-agents          → control room: docs, rules, runbooks, architecture (NO raw secrets)
/srv/<agent-name>/data    → live runtime: secrets, memory, skills, sessions, crons
```

> *"The control room is the brain that defines the system. The live runtime is the body that runs it. You can rebuild the body from the brain. You cannot rebuild the brain from the body."*

Control room structure: `README.md` / `CLAUDE.md` / `agents/<name>/{inventory,docker,env-map,runbook,backup}.md` / `shared/{security,commands}.md` / `api-keys-sop.md` / `orchestrator-and-fleet-skills.md`.

Per-agent runtime: `.env` / `config.yaml` / `SOUL.md` / `memories/` / `skills/` / `cron/` / `sessions/` / `logs/` / `state.db`.

## The 5-layer SEO agent (Shann's worked example, one Docker container, 21 steps)

```
Company brain (vision, brand, audience — every agent reads this)
  ↓
Orchestrator Hermes (routes topic/keyword to SEO agent)
  ↓
SEO brain (ranking playbook, voice rules, content formats, visual style)
  ↓
Three sub-agents in one Docker container:
  - Research + ideate (steps 01-07)
  - Production (steps 08-15)
  - Distribution (steps 16-21)
```

**Why one container, not three**: SEO work is sequential. Research feeds the brief; brief feeds production; production feeds distribution. Splitting boundaries breaks the chain.

Sub-profiles switch context per phase. One process, one filesystem, one set of credentials. Every other specialized agent (outbound / design / support) uses the same template — clone, swap the domain brain, ship.

## The prototype → production methodology

1. **Prototype in Hermes** — open your main agent, describe what you want, let it try. *"It will get most of it wrong on the first run. That's fine."*
2. **Run 2-3 times against real work**, correcting drift each time. *"The harness watches every correction and starts writing the skill as it learns the shape."*
3. **Fine-tune in a dedicated workspace** — pull the workflow into a separate Claude Code workspace or fresh Hermes agent. Tighten prompts, lock routing, add error handling, decide cron vs trigger.
4. **Deploy to a VPS on a schedule** — push to its own Docker container, set cron, walk away.

> *"You cannot write a production agent from scratch. You have to grow one. Hermes makes the growing part fast."*

## Model routing per agent

Shann runs:
- **Claude Opus 4.7** for creative work (copywriting, voice, hook generation, content drafting) — *"taste and writing quality matter"*.
- **Codex (GPT-5.5)** for structured work (coding, planning, browser automation, scraping) — *"steps need to be tight, output predictable"*.

Routed per-agent via the tool gateway. If only one: heavy-content/copy → Opus; heavy-infra/automation → Codex.

## Notable quotes

> *"Most AI tools answer questions. Hermes Agent runs your workflows end-to-end."*

> *"Memory isn't a plugin. Skills aren't a plugin. They're the same harness."* *(via Shann's framing of bundled defaults)*

> *"Level 4 is what a marketing department in your terminal looks like. It does not need you to start the day. It shows up to work on its own, files reports, checks itself, and only pings you for the decisions that need taste."*

> *"Do not try to write your own skills on day one. Run real work, let the agent watch, and let the harness write the skills."*

> *"Apply [Hermes] to the wrong-sized model and you get a confused team. Apply it to the right one and you get a team."*

## Honest trade-offs

1. **Bundled defaults are opinions** — heavy if you want primitive-level control (OpenClaw is the alternative).
2. **Level 3-4 have a real learning curve** — Docker / VPS / SSH / orchestrator-skills; not install-and-go.
3. **The model still matters** — a framework can't make a small model into a strategist; use the strongest models you can afford for the load-bearing work (orchestrator, strategy, brain).

## Hermes adoption metrics (per Shann's claims)

- **#1 on OpenRouter** for global token usage.
- **150,000 GitHub stars** on the Hermes repo *(was 23k+ in earlier 2026-05 ingest — 6× jump in ~2 weeks; verify against actual GitHub before relying)*.
- 123 bundled skills before the agent writes one of its own.
- 70+ built-in tools in the gateway, 300+ models, one subscription.
- 6 deployment targets; 20+ messaging surfaces.

## How this composes with the wiki

- [[wiki/entities/hermes-agent]] — **major refresh required**: star count + skill count + deployment targets + messaging surfaces all need updating.
- [[wiki/projects/helm]] — Shann's control-room pattern is **directly transferable** to Helm. Helm's repo topology (helm-backend / helm-portal / helm-mcp) maps to Shann's split: `helm-backend` ≈ runtime; brain wiki + master CLAUDE.md ≈ control room. Helm should adopt Shann's `MEMORY.md` + `USER.md` + `SOUL.md` per-agent convention.
- [[wiki/syntheses/multi-agent-ops-platform-blueprint]] — Shann's 5-layer SEO agent pattern (company brain → orchestrator → domain brain → 3 sub-agents → one container) **is a more specialized variant** of the blueprint's 6-agent pattern; worth absorbing as a sub-pattern.
- [[wiki/concepts/multi-agent-orchestration]] — Shann's 4-level model (one → direct specialists → orchestrator → automated) is the **operational maturity ladder**; promote to primary mental model.
- [[wiki/concepts/markdown-as-agent-contract]] — `SOUL.md` per agent + `MEMORY.md` + `USER.md` are 3 new instances at the per-agent / per-user scopes. Strongest articulation in the wiki of *agent personality as a markdown contract distinct from agent capability*.

## Mentioned entities

- [[wiki/entities/shannholmberg]] — author (existing; 2nd substantive post — update entity).
- [[wiki/entities/hermes-agent]] — primary subject (major refresh needed).
- [[wiki/entities/nous-research]] — Hermes maintainer.
- [[wiki/entities/openrouter]] — model routing layer.
- [[wiki/entities/anthropic]] — Claude Opus 4.7.
- [[wiki/entities/openai]] — *(stub candidate)* GPT-5.5 / Codex.
- [[wiki/entities/teknium]] — *(stub candidate)* Nous Research founder; "ships hermes updates almost daily."
- [[wiki/entities/espressio]] — *(stub candidate)* Shann's company; hosted Nous Research Hermes meetup in Lisbon.

## Related concepts

- [[multi-agent-orchestration]] — 4-level fleet model.
- [[markdown-as-agent-contract]] — SOUL.md / MEMORY.md / USER.md.
- [[reasoning-execution-split]] — Hermes's brain/personality/skillset triad.
- [[hot-cache]] — MEMORY.md + USER.md inject at session start.
- [[scheduled-automation]] — Level 4 cron-based fleet.
- [[mcp-server]] — Hermes's MCP integration confirmed.
- [[self-annealing]] — "closed learning loop" writing its own skills.

## Related sources

- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — `/goal` command primitive Shann's workflows depend on.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — Hermes integrations layer.
- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — Hermes commercial use case.
