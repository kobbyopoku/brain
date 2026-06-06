---
type: source
title: zodchiii — The 10 Claude Code agents nobody told you to build
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/zodchiii/status/2054137878968439247
source_type: x-thread
author: zodchiii (darkzodchi)
source_date: 2026-05-12
raw_path: raw/The 10 Claude Code agents nobody told you to build..md
content_status: substantive-verbatim
tags: [claude-code, agents, slash-commands, hooks, claude-agent-sdk, automation]
---

# zodchiii — The 10 Claude Code agents nobody told you to build

> zodchiii (darkzodchi) frames Claude Code agents as **job description + trigger + output** — not chat sessions. *"Your Claude Code is 10% of what it could be. The other 90% is 10 agents running in parallel: reviewing your PRs, writing your tests, hunting bugs, triaging your inbox, repurposing your content."* Three host surfaces: **slash commands** (`.claude/commands/<name>.md`) / **hooks** (`.claude/hooks/<event>.sh`) / **hosted scripts** via Claude Agent SDK. zodchiii's 3rd substantive wiki post.

## TL;DR — the 10 agents

| # | Agent | Type | Trigger | Output |
|---|---|---|---|---|
| 1 | **PR Reviewer** | Slash + GitHub hook | `/review` on demand or PR opened | Comment with bugs / missing tests / security / style; <90 seconds |
| 2 | **Test Writer** | Slash | `/test` | Tests for the diff |
| 3 | **Bug Hunter** | Hook (PostToolUse) | After edits | Flags new issues |
| 4 | **Inbox Triager** | Hosted script (SDK) | Cron | Categorized inbox summary |
| 5 | **Content Repurposer** | Slash | `/repurpose` | Long-form → X/LinkedIn/etc. |
| 6 | **Migration Engineer** | Slash | `/migrate` | DB schema diff + Liquibase/Flyway migration |
| 7 | **Doc Generator** | Hook (PostToolUse) | After file edits | Updates docs |
| 8 | **Security Auditor** | Hook (PreToolUse / pre-commit) | Before commits | Flags secrets / SQL injection / etc. |
| 9 | **Deployer** | Slash + hosted | `/deploy <env>` | Runs pipeline |
| 10 | **Status Reporter** | Hosted (SDK + cron) | Weekly | Multi-project status summary |

(The 10 agents themselves vary in detail in the source; the **mental shift** that an agent = trigger + prompt + output is the load-bearing claim.)

## The mental shift

> *"A Claude Code agent isn't a chat session. It's a **job description + a trigger + an output**. 'PR Reviewer' isn't a person you talk to. It's a hook that fires on every PR, runs Claude with a specific prompt, and drops a comment."*

This is the architectural deconstruction that maps Claude Code agents onto the [[wiki/concepts/do-framework|DOE framework]]: **Directive** (the prompt at `.claude/commands/<name>.md`) + **Orchestration** (slash / hook / SDK-cron) + **Execution** (Claude + tools).

## The three host surfaces

```
.claude/commands/<name>.md   → slash commands (on-demand: /name)
.claude/hooks/<event>.sh     → hooks (automatic: PreToolUse / PostToolUse / git events)
Claude Agent SDK             → hosted scripts (24/7, cron, webhooks)
```

Each surface is a different *deployment pattern*; the agent's core (prompt + tools) stays the same.

## Sample prompt (PR Reviewer)

> *"You are a senior code reviewer. Read the staged diff. Flag: hardcoded secrets, missing tests, type errors, obvious bugs. Be terse, max 5 comments."*

Strikingly short. Per zodchiii's earlier ingest ([[wiki/sources/zodchiii-x-claude-code-settings]]), this matches the cost-discipline aesthetic: small prompts, scoped MCPs, explicit limits.

## How this composes with the wiki

- [[wiki/concepts/claude-code-skills]] — slash commands at `.claude/commands/` are the canonical skill-pack pattern; zodchiii names 10 specific candidates worth filing.
- [[wiki/concepts/claude-code-hooks]] — hooks at `.claude/hooks/<event>.sh` get strong validation. Adds PR-review / doc-generator / security-auditor as practical PostToolUse / PreToolUse examples.
- [[wiki/entities/anthropic-agent-sdk]] — hosted-script pattern; zodchiii's status-reporter + inbox-triager use this.
- [[wiki/projects/helm]] — Helm's 6 agents (Lead Mgmt / Sales / Marketing / Operations / PM / Analytics) follow the same mental model. The host surface is FastAPI + APScheduler instead of slash/hook/SDK, but the *trigger + prompt + output* abstraction is identical.
- [[wiki/concepts/do-framework|DOE framework]] — *"job description + trigger + output"* is DOE in prose.

## Notable quotes

> *"Your Claude Code is 10% of what it could be. The other 90% is 10 agents running in parallel."*

> *"A Claude Code agent isn't a chat session. It's a job description + a trigger + an output."*

> *"Three places these agents live: slash commands, hooks, hosted scripts."*

## Mentioned entities

- [[wiki/entities/zodchiii]] — author (3rd substantive post — update entity).
- [[wiki/entities/claude-code]], [[wiki/entities/anthropic-agent-sdk]] — primary platform.

## Related concepts

- [[claude-code-skills]] — slash command host.
- [[claude-code-hooks]] — event-triggered host.
- [[doe-framework]] — *trigger + prompt + output* maps to DOE.
- [[markdown-as-agent-contract]] — prompts as markdown contracts at `.claude/commands/`.
- [[reasoning-execution-split]] — Claude reasons, tools execute, output is the result.

## Related sources

- [[wiki/sources/zodchiii-x-claude-code-settings]] — same author's 15 Claude Code settings tutorial.
- [[wiki/sources/zodchiii-x-2052368125480354000]] — same author's Teamly content-marketing post (ethical_flag).
- [[wiki/sources/dabit3-agent-hooks-in-depth]] — companion hooks deep-dive.
