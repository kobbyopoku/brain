---
type: entity
title: claude-subconscious
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/0xfurai/claude-subconscious
aliases: []
tags: [claude-code, memory, background-agent, stub]
---

# claude-subconscious

> A background agent that watches Claude Code sessions, reads project files, and builds memory passively over time — described by [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]] as "having a junior dev sitting behind you, taking notes on everything you do."

## Profile

This page is a **stub**. claude-subconscious appears in this wiki only via [[wiki/sources/regent0x-claude-code-247-dev-team]], which characterizes it as one of three tools in the persistent-memory layer. Unlike [[wiki/entities/claude-mem]] (which compresses at session boundaries), claude-subconscious operates continuously in the background.

## Key facts

- **Repo**: https://github.com/0xfurai/claude-subconscious (cited in [[wiki/sources/regent0x-claude-code-247-dev-team]])
- **Mechanism**: continuous background watcher; reads files and session activity; builds memory store without explicit user trigger.

## Positions and claims

_(none directly authored; framing cited from regent0x_.)_

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]

## Related entities

- [[wiki/entities/claude-mem]] — sibling tool in the persistent-memory layer (different cadence: session-end vs. continuous).
- [[wiki/entities/obsidian]] — third element of the memory layer.
- [[wiki/entities/claude-code]] — the platform.

## Related concepts

- [[llm-wiki-pattern]]
