---
type: entity
title: Cowork
entity_type: product
created: 2026-05-04
updated: 2026-05-09
website: ""
aliases: [Claude Cowork]
tags: [claude-code, ai-coding, anthropic, automation-platform]
---

# Cowork

> Anthropic's Claude Code mode positioned as **non-developer-friendly automation infrastructure** — a way to run *systems* on Claude rather than have *conversations* with it. Operates on the user's actual local files (not chat-paste output), supports scheduled and manual task execution, and integrates with MCP connectors for Gmail / Calendar / Slack / Drive. The natural application surface for the [[markdown-as-agent-contract]] meta-pattern at the workspace-folder scope.

## Profile

Cowork is the Claude Code mode that runs tasks against the user's local filesystem, with schedulable triggers and shared MCP-connector access. Two strong source treatments now exist:

- **[[wiki/sources/heygurisingh-x-cowork-setup|Guri Singh's onboarding guide]]** — the *setup layer*: workspace folder structure (`ABOUT ME/` + `PROJECTS/` + `TEMPLATES/` + `CLAUDE OUTPUTS/`), paste-ready Global Instructions (per-user master agent contract), 11 official Anthropic plugins, AskUserQuestion as the most-transformative feature. The first source to articulate Cowork as *anyone-can-use-this* infrastructure rather than developer-only.
- **[[wiki/sources/eng_khairallah1-x-2052684086414852546|Khairallah's three-session daily architecture]]** — the *operational layer* on top of Guri's setup: 7AM Morning Briefing (scheduled) / Midday Production Block (manually triggered) / 5PM End-of-Day Wrap-up (scheduled), with carry-forward state passing between sessions. Quote: *"Claude Cowork is not a tool you use. It is infrastructure you build."*

The two compose perfectly: read Guri first to set up the workspace, then Khairallah to build the daily loop.

## Key facts

- **Vendor**: [[wiki/entities/anthropic]].
- **Relationship to [[wiki/entities/claude-code]]**: Cowork is a Claude Code mode (not a separate product). Claude Code is the engine; Cowork is the workspace.
- **Filesystem write capability**: Cowork operates on actual files — it creates documents, updates spreadsheets, compiles reports, saves to specified locations. This is the pivotal capability that distinguishes systems-mode from conversation-mode.
- **MCP integration**: shares Claude Desktop's connector configuration (`claude_desktop_config.json`); commonly-used connectors are Gmail, Google Calendar, Slack, Google Drive, Notion.
- **Scheduling**: supports `/schedule` slash command for cron-style task execution.
- **Sub-agent parallelization**: per Khairallah, *"a stack of 20 documents gets handled in minutes not hours"* via parallel sub-agents.
- **Plugins**: Guri names 11 official Anthropic plugins.
- **AskUserQuestion**: per Guri, the most-transformative built-in tool — Cowork pauses to ask the human for clarification when uncertain rather than guessing.

## Architecture conventions (from sources)

### Workspace folder structure (Guri)

```
~/Cowork/
├── ABOUT ME/         # who you are, voice, preferences (read by every session)
├── PROJECTS/         # one folder per active project
├── TEMPLATES/        # reusable task templates (production-block prompts)
└── CLAUDE OUTPUTS/   # everything Cowork writes lands here
```

The folder structure itself becomes a contract — the agent reads `ABOUT ME/` for context, writes to `CLAUDE OUTPUTS/` for output. **Folder-as-contract** is a sub-pattern of [[markdown-as-agent-contract]].

### Three-session daily architecture (Khairallah)

| Session | Trigger | Inputs | Outputs |
|---|---|---|---|
| Morning Briefing | 7AM scheduled | Gmail + Calendar + Slack | One markdown file in `Daily-Briefings/` with 4-tier urgency triage, meeting prep, top 3 priorities |
| Production Block | Manual | Templates + working folders | Documents/spreadsheets/reports written to specified save locations |
| End-of-Day Wrap-up | 5PM scheduled | Day's email + calendar + file modifications + morning briefing | Wrap-up doc with carry-forward section feeding tomorrow |

Daily savings (per Khairallah): 1-3 hours/day = 20-60 hours/month.

### Refinement loop

Both sources prescribe a weekly Friday refinement (Khairallah explicit at 15min; Guri implicit). Three questions:

1. What did Cowork miss that the human had to discover?
2. What did Cowork produce that the human had to redo?
3. What new recurring task should be automated next?

Manual [[self-annealing]] — the human is the optimizer. Composes with [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's automated Analytics-agent]] approach (autonomous prompt-rewriting); they're not in conflict.

## Positioning

- **Target audience**: knowledge workers and small-business operators, not just developers. Both Guri and Khairallah emphasize this: *"Not just developers. Not just technical people. Anyone."* (Khairallah).
- **Vs Claude chat**: Cowork is for systems; chat is for conversations. The distinction is durability and filesystem write.
- **Vs Claude Code (developer mode)**: same engine, different workspace conventions. Developer Cowork is rare in the wiki sources; non-developer Cowork is the dominant framing.
- **Vs ChatGPT custom GPTs / OpenAI Tasks**: Cowork's filesystem-write + MCP-connector combination is differentiating. Custom GPTs can't write to your Documents folder.

## Mentioned in

- [[wiki/sources/heynavtoor-10k-claude-automation-business-90-days]] — original mention as Claude Code alternative in 5-tool stack.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — Cowork onboarding setup.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — three-session daily architecture.

## Related concepts

- [[ai-automation-services]] — Cowork is the platform on which the service is delivered.
- [[markdown-as-agent-contract]] — Cowork is the strongest single instance of the meta-pattern (folder + Global Instructions + templates + master prompt all are agent contracts).
- [[doe-framework]] — Cowork sessions compose cleanly as DOE cycles.
- [[scheduled-automation]] — `/schedule` command.
- [[self-annealing]] — Friday refinement loop.
- [[claude-code-skills]] — Cowork plugins are skill-equivalent.

## Related entities

- [[wiki/entities/anthropic]] — vendor.
- [[wiki/entities/claude-code]] — the engine Cowork runs on.
- [[wiki/entities/heygurisingh]] — author of the Cowork onboarding guide.
- [[wiki/entities/eng-khairallah]] — author of the three-session daily architecture.
- [[wiki/entities/obsidian]] — common viewer for Cowork-written markdown files.
