---
type: entity
title: nateherk
entity_type: person
created: 2026-05-02
updated: 2026-06-06
website: https://x.com/nateherk
aliases: [Nate Herkelman, Herk]
tags: [author, claude-code, ai-os, founder]
---

# nateherk

> Founder running a $3M/yr business on Claude Code as an "AI Operating System." Author of [[wiki/sources/nateherk-claude-code-os-3m-business]] — the wiki's canonical source on the [[ai-os-pattern]] and the [[hot-cache]] pattern. Coined the **Three Ms** (Default Shift / Function Breakdown / Curiosity Rule) and the **Four Cs** (Context / Connections / Capabilities / Cadence) frameworks.

## Profile

nateherk is a founder who runs a $3M/yr business operationally inside Claude Code. He ships a public starter repo ([[wiki/entities/ais-os|github.com/nateherkai/AIS-OS]]) that scaffolds his AI OS pattern in five minutes. He maintains two LLM Wikis (a YouTube transcripts vault with 36+ ingested videos, and a "Herk Brain" personal second-brain). His operational discipline is unusually crisp — claude.md updated 2× a day; weekly `/audit` + `/level-up` improvement loops; separate API accounts per service.

## Key facts

- **X handle**: @nateherk
- **Repo**: [[wiki/entities/ais-os|github.com/nateherkai/AIS-OS]]
- **Notable thread (2026-05-01)**: full AI OS playbook.
- **Business scale (per source, unverified)**: $3M/yr.
- **Vaults run**: YouTube transcripts vault (36+ videos) + "Herk Brain" personal vault.
- **Claude plan**: Max 20x at $200/mo; burned $500 in top-up usage on [[wiki/entities/claude-design|Claude Design]] (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Brand-spec workflow**: built a 372-line markdown brand spec for [[wiki/entities/tally|Tally]] in regular Claude before opening Design; built an "AI Automation Society" design system by handing Claude Design a website URL + GitHub repo (per [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Multi-agent setup**: does most work in [[wiki/entities/claude-code|Claude Code]] but keeps [[wiki/entities/codex-cli|Codex]] wired into the same project as a fallback; moved most work to the terminal over the VS Code extensions (per [[wiki/sources/nateherk-claude-code-codex-same-project]]).

## Positions and claims

- **Treat Claude Code as an operating system, not a chat tool** — the layer between the human and all their digital work.
- **The Three Ms and Four Cs are the durable layer** — tools change, models change; these don't.
- **Build order matters**: Context → Connections → Capabilities → Cadence. You can't have cadence without connections; can't have capability without context.
- **Productivity drops 20% before climbing 50%** — most people quit during the dip.
- **Prefer API endpoints saved as markdown over MCPs** — markdown is cheap to read; API docs are expensive to crawl every time. (Same insight as [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's MCP overhead pattern]] from a different starting point.)
- **Boring is beautiful** — deterministic workflows beat AI agents 9 times out of 10. Most business processes don't need autonomy; they need a Python script on a cron.
- **Failure is data** — every broken run becomes a permanent skill or doc update; nothing breaks twice.
- **Run Claude Code and Codex in parallel** — reports being "bailed out by Codex" when Claude Code loops; built a session-handoff skill that summarizes conversation, active files, decisions, and next steps to hand off between agents (argued in [[wiki/sources/nateherk-claude-code-codex-same-project]]).

## Mentioned in

- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/nateherk-claude-design-tally-brand]] — operator who built the Tally brand end-to-end in [[wiki/entities/claude-design|Claude Design]] and reverse-engineered the quota-stretching playbook.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — runs Claude Code and Codex in parallel daily; built the video's HTML cheat sheet with both agents collaborating on the same file.

## Related entities

- [[wiki/entities/ais-os]] — author's starter repo.
- [[wiki/entities/andrej-karpathy]] — cited as inspiration for the wiki layer.

## Related concepts

- [[ai-os-pattern]]
- [[hot-cache]]
- [[llm-wiki-pattern]]
- [[claude-code-skills]]
- [[progressive-disclosure]]
- [[scheduled-automation]]
- [[reasoning-execution-split]]
