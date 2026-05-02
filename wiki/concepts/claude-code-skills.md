---
type: concept
title: Claude Code Skills
created: 2026-05-02
updated: 2026-05-02
aliases: [skills, claude skills, skill plugins]
tags: [claude-code, mechanism, agent-config]
---

# Claude Code Skills

> The mechanism by which Claude Code is taught domain-specific workflows — markdown files (and frontmatter) that define a single capability, when it activates, and the steps the agent follows when invoking it.

## Definition

A **skill** in Claude Code is a unit of domain-specific instruction packaged so the agent can selectively invoke it. The unit file format is a [[skill-md|SKILL.md]] (or equivalent) with frontmatter that includes at minimum a name and a description; the description determines when the agent decides the skill applies. Skills can be plugin-namespaced (e.g. `superpowers:writing-plans`, `pr-review-toolkit:code-reviewer`). Where [[CLAUDE]] is the project-wide contract, a skill is a **single capability** the agent picks up and uses on demand.

## Why it matters

Out of the box, Claude is a generalist. Skills turn it into a specialist for the workflows you care about — without losing the generality, because skills activate selectively based on description-matching against the current task. This lets a user stack many skills (security review, TDD enforcement, design taste, document generation, etc.) and still keep the agent's effective context tight: only the relevant skills actually load.

This concept is **distinct from the file format** captured in [[skill-md]]. SKILL.md is the *file*; this page is about the *mechanism* — invocation, activation, namespacing, composition with [[subagents]].

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — characterizes skills as transforming Claude Code "from 'write code when asked' into a complete development methodology." Names specific skill collections: [[wiki/entities/superpowers]] (workflow discipline), [[wiki/entities/trail-of-bits-claude-code-skills]] (security), [[wiki/entities/anthropic-skills]] (official PDF/DOCX/XLSX), [[wiki/entities/tdd-guard]] (TDD enforcement). Asserts skills don't conflict with each other and stack additively.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — frames skill-file authoring as one of four core competencies for an AI automation services business: "the skill file is the engine of every automation." The author's framing is implementation-side: a skill file is a process-spec the agent executes (process steps, output formats, edge case handling, quality checks, error recovery).

## Sub-claims and details

- **File format**: see [[skill-md]] — markdown plus frontmatter (name, description, when to invoke).
- **Activation**: based on description matching against the current task. The agent reads available skill descriptions as part of its context and invokes the matching one(s).
- **Namespacing**: plugin-prefixed (e.g. `posthog:querying-posthog-data`, `vercel:nextjs`) when distributed via plugin marketplaces.
- **Composition**: skills stack — multiple skills can apply to the same task. Reported (regent0x_) as non-conflicting; in practice ordering and interaction may matter for complex stacks.
- **Composition with [[subagents]]**: each subagent can have its own skill stack; e.g. the reviewer subagent + the trail-of-bits security skill collection.
- **Distribution**: open-source repos on GitHub; some via the Anthropic plugin marketplace (`/plugin install <name>@<source>`).
- **Two perspectives on the same artifact** (worth keeping straight):
  - From a **personal-productivity** angle (regent0x_), skills are pre-built collections you install to gain capabilities you didn't have to write yourself.
  - From a **services-business** angle (Khairallah), skill-file authoring is a billable craft — the value the AI automation provider delivers to a client is fundamentally a portfolio of well-designed skill files.

## Open questions and contradictions

- **Activation collision**: when two skills' descriptions both seem to match the task, who wins? Sources don't address this.
- **Skill versioning**: as skill files evolve, agents loading older or newer versions may behave differently. No skill-versioning convention captured yet.
- **Skill quality variance**: open-source skill repos vary widely in quality; "stack as many as you want" assumes the skills are well-authored, which is unsourced.

## Related concepts

- [[skill-md]] — the file format this concept builds on.
- [[markdown-as-agent-contract]] — skills are an instance of the meta-pattern.
- [[subagents]] — composes naturally with skills.
- [[context-file]] — adjacent concept (Khairallah's "context file" is to the *business* what a skill is to the *workflow*).
- [[claude-code-hooks]] — different mechanism, same Claude Code platform.
- [[claude-code-slash-commands]] — different mechanism, same platform.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/superpowers]] — workflow-discipline skill plugin.
- [[wiki/entities/anthropic-skills]] — official skill collection.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — security skill collection.
- [[wiki/entities/tdd-guard]] — TDD-enforcement skill.
- [[wiki/entities/anthropic]] — maintainer of Claude Code and the official skill collection.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/khairallah-ai-automations-10k-month]]
