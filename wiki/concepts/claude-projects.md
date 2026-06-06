---
type: concept
title: Claude Projects
created: 2026-06-06
updated: 2026-06-06
aliases: [claude projects, project workspaces]
tags: [claude, personal-ai-system, workspaces]
---

# Claude Projects

> Per-domain Claude workspaces — "separate brains" — each with their own custom instructions, files, memory, and conversations.

## Definition

Claude Projects are described as Layer 2 of a personal AI system: per-domain workspaces, each functioning as a separate brain with its own custom instructions, uploaded files, memory, and conversations. They are used to prevent context bleed between unrelated domains. Project instructions ("what this workspace is for") are distinct from global Personal Preferences ("who you are").

## Why it matters

Domain isolation is a practical pattern for keeping AI context clean across the multiple businesses and product lines Godwin runs. The distinction between per-project instructions and global preferences maps directly onto multi-tenant / multi-context architecture thinking.

## Treatment across sources

- [[wiki/sources/heynavtoor-personal-ai-system-claude]] frames it as Layer 2 — per-domain workspaces ("separate brains") each with their own custom instructions, uploaded files, memory, and conversations, used to prevent cross-domain context bleed.

## Sub-claims and details

- Each project is a separate workspace with its own custom instructions, uploaded files, memory, and conversations. [[wiki/sources/heynavtoor-personal-ai-system-claude]]
- Projects are used specifically to prevent cross-domain context bleed. [[wiki/sources/heynavtoor-personal-ai-system-claude]]
- Project instructions ("what this workspace is for") are distinct from global Personal Preferences ("who you are"). [[wiki/sources/heynavtoor-personal-ai-system-claude]]

## Open questions and contradictions

- The source does not specify limits on project count, file sizes, or per-project memory scope.

## Related concepts

- [[wiki/concepts/personal-ai-system]] — Claude Projects is one layer of the personal AI system stack.
- [[wiki/concepts/claude-memory]] — projects carry their own memory, distinct from account-level memory.
- [[wiki/concepts/voice-matching]] — voice samples are uploaded as Project Knowledge.

## Related entities

- [[wiki/entities/claude]]

## Mentioned in

- [[wiki/sources/heynavtoor-personal-ai-system-claude]]
