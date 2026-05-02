---
type: entity
title: AIS-OS
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/nateherkai/AIS-OS
aliases: [AIS OS, Nate's AI OS template]
tags: [claude-code, starter-repo, ai-os, stub]
---

# AIS-OS

> [[wiki/entities/nateherk|nateherk]]'s public starter repo for the [[ai-os-pattern]]. Clone, open in VS Code, and the AI OS scaffold is set up in five minutes. Ships with three skills: **Onboard**, **Audit**, and **Level Up**.

## Profile

AIS-OS is a Claude Code template repo published by nateherk. Cloning it gives a user a complete AI OS scaffold: contexts folder, decisions log, references library, archives, three pre-built skills, and a master claude.md prompt that ties them together. The repo is the operational starting point for the [[ai-os-pattern|Four Cs framework]] — running `/onboard` after cloning produces an About Me / About Business / Priorities trio that fills the Context layer in minutes.

## Key facts

- **Repo**: https://github.com/nateherkai/AIS-OS
- **Maintainer**: [[wiki/entities/nateherk]]
- **Setup time**: ~5 minutes (clone → VS Code → Claude Code → "I want to set up my AI operating system. Help me get onboarded.").
- **Folder layout**:
  - `.claude/skills/` — Onboard, Audit, Level Up.
  - `Archives/` — old documents, archived not deleted.
  - `Contexts/` — About Business, About Me, Priorities (the Context layer).
  - `Decisions/` — append-only decision log.
  - `References/` — Three Ms doc, tool API references, SOPs.
  - `claude.md` — master prompt (updated 2× a day per author).
  - `.env` — secrets, gitignored.

### Three shipped skills

- **Onboard** — 7-question interview that writes About Me / About Business / Priorities + a voice sample.
- **Audit** — scores the OS out of 100 across the Four Cs; returns top 3 gaps; saves history.
- **Level Up** — five-question capability-gap finder (repeated tasks, drudgery, smart-intern test, future constraint, growth lever).

## Mentioned in

- [[wiki/sources/nateherk-claude-code-os-3m-business]]

## Related entities

- [[wiki/entities/nateherk]] — maintainer.
- [[wiki/entities/claude-code]] — the platform the repo runs on.

## Related concepts

- [[ai-os-pattern]]
- [[claude-code-skills]]
- [[markdown-as-agent-contract]]
