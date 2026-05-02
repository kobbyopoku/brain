---
type: project
title: <Project name>
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active                    # active | paused | exploring | completed | archived
repo: <git URL or local path>
local_path: <where it lives on disk>
stack: []
started: YYYY-MM-DD
ended:                            # populate when status becomes completed/archived
aliases: []
tags: [project]
---

# <Project name>

> One-sentence framing: what this project is and why it exists.

## What and why

A short prose paragraph (3-6 sentences): what the project is, what problem it addresses, what the goal is, what success looks like.

## Stack and infrastructure

- **Languages / frameworks**: ...
- **Key dependencies / services**: ...
- **Repo / locations**: ...
- **Deployed at**: ...

## Current focus

What's being worked on this week / sprint / iteration. Update frequently — this is the section future-you will read most.

## Architecture decisions

Short, dated decisions with rationale. Higher-resolution decision logs can live in `<local_path>/.memory/decisions/` if the project warrants it; this section captures the durable ones.

- **YYYY-MM-DD** — chose X over Y because Z.
- ...

## Open questions

What's unresolved. What design choices haven't been made. What the project is blocked on.

## Lessons learned

Things that compound back into the wiki — patterns that worked, anti-patterns to avoid, surprises. **If a lesson generalizes beyond this project, file it as a concept page in `wiki/concepts/` and link to it from here.**

## Related

- **Concepts**: [[wiki/concepts/...]]
- **Entities**: [[wiki/entities/...]]
- **Sources**: [[wiki/sources/...]]
- **Other projects**: [[wiki/projects/...]]

## External links

- **Repo**: <URL>
- **Project's own CLAUDE.md** (if exists): `<path>/CLAUDE.md`
- **Project memory dir** (if exists): `<path>/.memory/`
