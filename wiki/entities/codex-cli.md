---
type: entity
title: Codex CLI
entity_type: product
created: 2026-05-05
updated: 2026-06-06
website: https://github.com/openai/codex
aliases: [openai-codex-cli, codex]
tags: [ai-coding, agent-cli, openai, claude-code-alternative]
---

# Codex CLI

> OpenAI's coding-agent CLI — competitor to [[wiki/entities/claude-code|Claude Code]]. Listed as one of 15 auto-detected agent CLIs in [[wiki/entities/open-design|Open Design]]'s PATH-scan runtime. Distinct from the older "OpenAI Codex" model (now deprecated); the modern Codex CLI is a coding-agent product around GPT-5/o-series models.

## Profile

Codex CLI is OpenAI's terminal-based coding-agent product — its positional answer to [[wiki/entities/claude-code|Claude Code]]. It reads a project, plans a task, and executes file edits, and is described as strong at implementation, especially when given a clear spec (see [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]). Its project-config conventions deliberately mirror Claude Code's, which makes converting a Claude Code project to a Codex project a near-mechanical task (see [[wiki/sources/nateherk-claude-code-codex-same-project]]).

## Key facts

- **Publisher**: [[wiki/entities/openai]].
- **Role**: agent CLI for coding tasks — file reads, edits, command execution; "strong at implementation, especially given a clear spec" ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- **Open Design integration**: detected on user's PATH and invoked as a runtime alternative to [[wiki/entities/claude-code|Claude Code]].
- **Project-root lookup**: looks for three things — `AGENTS.md`, a `.codex` folder (config and agents), and a `.agents` folder (skills) ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Skills format**: reads skills from the `.agents` folder as markdown files with YAML frontmatter ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Sub-agent format**: uses TOML files for sub-agents, versus Claude Code's markdown ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Sub-agent invocation**: Codex sub-agents do not auto-invoke; they must be called explicitly by name ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Config split**: respects a global-vs-project config split the same way Claude Code does ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **AGENTS.md limit**: cascading `AGENTS.md` files have a 32 KiB limit ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **/goal command**: added `/goal` "a few weeks ago" (before Claude Code per Saboo's timeline); `/goal` gives Codex a spec with a defined done-state ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]], [[wiki/sources/nurijanian-goal-for-product-managers]]).

## Positions and claims

- All Codex surfaces share the same harness, which is why "Codex models feel better on Codex surfaces than a generic chat window" — argued in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]].
- A Claude Code project can be converted to a Codex project in a single prompt — by mirroring `CLAUDE.md` and having the agent research the docs itself ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- Long-horizon Codex examples depend on externalised intent: spec files, plan files, runbooks, validation commands, status logs, and periodic proof ([[wiki/sources/nurijanian-goal-for-product-managers]]).

## Mentioned in

- [[wiki/sources/nexu-io-open-design]] — listed among 15 auto-detected agent CLIs.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — run in parallel with Claude Code; first behavioral facts (project-root lookup, skills/sub-agent formats, single-prompt conversion).
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — Codex harness; 32 KiB AGENTS.md limit; all surfaces share one harness.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — the builder role; OpenAI's coding CLI, strong at implementation given a clear spec; added `/goal` "a few weeks ago"; reached a passing build in ~15 minutes on SPEC.md.
- [[wiki/sources/nurijanian-goal-for-product-managers]] — cited as having a parallel `/goal` command and long-horizon examples.

## Related entities

- [[wiki/entities/openai]] — publisher.
- [[wiki/entities/claude-code]] — closest functional sibling.
- [[wiki/entities/cursor]] — adjacent in the IDE-agent space.
- [[wiki/entities/open-design]] — auto-detects this CLI on PATH.

## Related concepts

- [[claude-code-skills]] — adjacent (Codex CLI may have its own skill-equivalent mechanism; unsourced).
