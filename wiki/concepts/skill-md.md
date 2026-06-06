---
type: concept
title: SKILL.md
created: 2026-05-02
updated: 2026-06-06
aliases: [skill.md]
tags: [agent-config, markdown, stub]
---

# SKILL.md

> Markdown file defining a Claude skill — its name, when it activates, and the instructions the agent follows when invoking it.

## Definition

This page is a **stub**. SKILL.md is mentioned in this wiki as one of the canonical instances of [[markdown-as-agent-contract]] — a markdown file that defines a single capability the agent can pick up and use. The wiki has not yet ingested a primary source about SKILL.md (e.g. the Claude Skills documentation), so the page only captures what neighboring pages say about it.

## Treatment across sources

- [[wiki/concepts/markdown-as-agent-contract]] — lists SKILL.md as an instance of the meta-pattern, with frontmatter that defines when and how the skill activates.
- [[wiki/sources/tricalt-memory-skills-same-harness]] frames it as a "procedure-level claim" ("to do task T, run X, Y, Z") and a "compressed procedure" — the narrow, what-to-do slice of the world model, inseparable from memory.

## Sub-claims and details

- Defines a **single capability** rather than a project-wide contract — narrower scope than [[CLAUDE]] or [[agents-md]].
- Frontmatter typically includes `name` and `description` fields that determine when an agent decides the skill applies.
- Skills are invokable via the `Skill` tool in Claude Code and can be plugin-namespaced (e.g. `superpowers:writing-plans`).
- A skill encodes a **procedure-level claim** of the form "to do task T, run X, Y, Z." ([[wiki/sources/tricalt-memory-skills-same-harness]])
- A skill is a **compressed procedure** — the narrow, what-to-do slice of the world model — and is inseparable from memory. ([[wiki/sources/tricalt-memory-skills-same-harness]])

## Open questions and contradictions

- **No primary source yet ingested.** The official Claude Skills spec, lifecycle, and authoring guidance are unsourced here.
- **Composition with CLAUDE.md**: when a skill's instructions conflict with CLAUDE.md, who wins? Probably CLAUDE.md (per "user instructions are highest priority"), but this is unsourced for SKILL.md specifically.

## Related concepts

- [[claude-code-skills]] — the **mechanism** that runs SKILL.md files. SKILL.md is the *file format*; claude-code-skills is the *runtime layer*. Use both: this page for "what's in the file?", that page for "how does it activate?".
- [[markdown-as-agent-contract]] — the meta-pattern SKILL.md instantiates.
- [[agents-md]] — sibling instance.
- [[design-md]] — sibling instance.
- [[context-file]] — sibling at the per-client scope.

## Mentioned in

- [[wiki/concepts/markdown-as-agent-contract]]
- [[wiki/sources/tricalt-memory-skills-same-harness]]
