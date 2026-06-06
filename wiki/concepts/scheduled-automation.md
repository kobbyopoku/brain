---
type: concept
title: Scheduled Automation
created: 2026-05-02
updated: 2026-06-06
aliases: [/schedule, scheduled tasks, cron automation, recurring agents]
tags: [claude-code, automation, mechanism]
---

# Scheduled Automation

> An automation that runs on a recurring schedule (or once at a specific future time) without any human triggering — a daily briefing, a weekly report, a monthly process — using Claude Code's `/schedule` mechanism to spawn an agent run at the chosen moment.

## Definition

A **scheduled automation** is a workflow registered to fire automatically at a defined time or interval. In Claude Code's idiom, the `/schedule` slash command (see [[claude-code-slash-commands]]) registers a routine — typically a one-line goal or a reference to a skill — that runs unattended. The agent wakes, performs the work, files the result somewhere persistent (PR, document, Slack message, wiki page), and exits.

## Why it matters

Two reasons matter, captured by the two ingested sources:

1. **Time-shifting (regent0x_)**: a scheduled automation does at 3am what the human used to do at 3pm. The human's productive hours are reclaimed.
2. **Highest-value automation class for services (Khairallah)**: the automations that deliver compounding value to a client are precisely the ones that run unattended — daily briefings, weekly reports, monthly financial processing. These run dozens or hundreds of times after the build, with zero marginal effort. *"The highest-value automations are the ones that run without anyone pressing a button."*

Scheduled automations also make the [[lint]] operation in this wiki concrete — the weekly Monday-9am-UTC remote routine that lints the wiki is itself a scheduled automation.

## Treatment across sources

- [[wiki/sources/khairallah-ai-automations-10k-month]] — names scheduled-automation design as one of four core technical competencies for an AI automation services builder. Practice prescription: build 3 scheduled automations on the builder's own workflow (daily briefing, weekly review, monthly summary), let them run for 2 weeks, fix issues. Highlights graceful handling of missing data as a key design concern.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — implicit but central. The "agents work while you sleep" argument depends on scheduled automations as much as on parallel orchestration; orchestration is *how many* run in parallel, scheduling is *when* they run.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational tradeoff matrix for three cadence options:
  - **Cloud Routines** (Anthropic infrastructure, laptop can be off): Pro 5/day, Max 15/day, Team/Enterprise 25/day. Gotchas: cloned-repo only (no local files); `.env` not pushed (use cloud env vars); explicit prompt to use env vars not `.env`; default network = "trusted" (Anthropic-vetted only — switch to "full" for ClickUp etc.); each run stateless; minimum interval 1 hour.
  - **Local Scheduled Tasks** (desktop app): can catch up on missed runs; needs app open + computer awake.
  - **Loop**: one-off recurring runs in a single session; 3-day expiry then auto-deletes; great for "every 5 minutes check if my deploy is done"; wrong for weekly recurring jobs.
  Author's framing: *"Routines basically inject a prompt into a real Claude Code session. The same prompt you'd type yourself. So write specific, one-shot prompts; the routine isn't going to ask clarifying questions."*
- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it via Buzz's once-a-day learning run that aggregates feedback and opens a PR, plus scheduled-job triggers via Oz — instances of scheduled agent automation.
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] frames it via Blueprints 02/03: weekly batch generation (Sunday evening) plus scheduled posting at algorithm-optimal times (Tue–Thu, 8–10 AM / 6–8 PM in the audience timezone, per the source's rule of thumb).
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] frames it indirectly via the ROI volume gate: agents must run on lengthy, high-volume automations (not ~5x/month) to be worth deploying.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] frames it as Layer 7, instantiated via Cowork Scheduled Tasks / Claude Code Routines with three concrete jobs (6:30 AM Morning Briefing, Friday Weekly Report, Sunday Content Plan). The Morning Briefing is the same shape as Khairallah's 7 AM and Shruti's 6 AM briefings — recurring pattern.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] frames it via the N8N 6 AM cron as the orchestration trigger that runs the briefing unattended and deposits it before the user starts the day.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] frames it implicitly via the Weekly Report Generator automation idea, but notably omits the explicit /schedule unattended-automation emphasis of the sibling $10K/mo source.
- [[wiki/sources/cyrilxbt-personal-operating-system]] frames it via the N8N cron layer firing five workflows unattended (6AM briefing, 8PM capture processor, Sun 7PM weekly review, every-2-hours queue processor, Mon 7AM project health monitor) — scheduled automation layered onto an LLM-maintained vault.
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] frames it via cron/jobs.json + output/ with a gateway daemon ticking every 60s to run due jobs in isolated sessions; plain-English schedules converted by Hermes — a concrete instance of native agent scheduling.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it via Step 6: Claude Routines on "Anthropic's cloud" on a daily/weekly schedule ("Set the schedule. Walk away.").
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] frames it as goals running as background workers tracked on a durable Kanban board; "setup is just another goal" extends orchestrator scope to environment provisioning.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] frames it via Setup 5 (one daily scheduled task: research brief / inbox summary / status writeup); "the moment Claude starts producing while you're not at the keyboard."
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]] frames it via the "machine that studies the market while you sleep" framing and the Auto-Post (Drive → socials) loop — unattended scheduled-automation instances.

## Sub-claims and details

- **Trigger primitive**: `/schedule` slash command in Claude Code. Registers either a recurring (cron-like) or one-time (`run_once_at`) routine.
- **Cadence**: minimum interval typically 1 hour (per the Claude Code routines API). Common cadences: daily, weekly, monthly.
- **Execution context**: typically an isolated session — the scheduled run does not share state with the user's interactive session unless deliberately wired (e.g. via writing to a shared store).
- **Failure handling**: a scheduled automation must handle missing data, network failures, downstream tool outages. Khairallah specifically calls out "graceful handling of missing data" as a design concern; without it, scheduled automations fail loudly and create alert fatigue.
- **Common scheduled automation classes**:
  - **Briefings** — daily pull of relevant info from multiple [[mcp-server|MCP sources]] into a single digest.
  - **Reports** — weekly synthesis of prior period's work.
  - **Maintenance/sweeps** — periodic cleanup, reconciliation, audit (e.g. lint passes).
  - **Triggered follow-ups** — checking on a long-running task and reporting status (e.g. a feature flag rollout, a soak window).
- **Self-reference**: the wiki itself uses a scheduled automation (the weekly remote lint at https://claude.ai/code/routines/trig_01B2UPxfQ6m7S2LX7bUweEsJ, Mondays 09:00 UTC). The lint workflow defined in [[CLAUDE]] § Workflows → Lint is the work the scheduled automation performs. See [[lint]].

## Open questions and contradictions

- **Drift over long horizons**: a scheduled automation registered today may be running unchanged a year from now. How does it stay aligned with evolving conventions, tools, and APIs? Versioning and review-on-stale-output are unsolved.
- **Cost transparency**: an automation running daily eats tokens daily. Total cost is not summarized at registration time.
- **Failure notification**: by default, a failed scheduled run may be silent. Routines should expose a notify-on-failure surface; current sources don't address this.
- **Human-in-the-loop scheduling**: some automations should produce a *draft* for review, not a final output. The default semantics of `/schedule` don't distinguish.

## Related concepts

- [[claude-code-slash-commands]] — `/schedule` is the entry point.
- [[lint]] — this wiki's weekly lint is itself a scheduled automation.
- [[mcp-server]] — most scheduled automations call multiple MCP-mediated tools.
- [[ai-automation-services]] — the highest-value automation class in this services business.
- [[multi-agent-orchestration]] — scheduled automations may themselves spawn parallel subagents.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/hermes-agent]] — ships native cron scheduler with SQLite-backed durable jobs (3-min hard interrupts) + atomic-task-claiming kanban for multi-agent work queues. The most architecturally complete scheduled-automation primitive in the wiki.

## Mentioned in

- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/nousresearch-hermes-agent]] — Hermes ships native cron + kanban as durable-by-default primitives.
- [[wiki/sources/petradonka-agents-need-feedback-loops]] — daily learning run + Oz scheduled-job triggers.
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] — weekly batch generation + scheduled algorithm-optimal posting.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — ROI volume gate: high-volume automations only.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — Layer 7 Scheduled Tasks/Routines (Morning Briefing, Weekly Report, Content Plan).
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — N8N 6 AM cron as the briefing orchestration trigger.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] — Weekly Report Generator; omits explicit /schedule emphasis.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — N8N cron layer firing five unattended workflows on a vault.
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — cron/jobs.json + 60s gateway daemon; plain-English schedules.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — Step 6 Claude Routines on Anthropic's cloud.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — goals as background workers on a durable Kanban board.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] — Setup 5 one daily scheduled task.
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]] — "studies the market while you sleep" + Auto-Post loop.
