---
type: concept
title: Claude Code Hooks
created: 2026-05-02
updated: 2026-05-02
aliases: [hooks, lifecycle hooks]
tags: [claude-code, mechanism, automation]
---

# Claude Code Hooks

> Lifecycle automation for Claude Code: shell or program callbacks that fire automatically at specific moments (before/after a tool call, at session start, on commit) and either gate, modify, or augment what the agent does.

## Definition

A **hook** is configuration that ties a shell command to a specific event in Claude Code's lifecycle. When the event fires, the hook runs; the hook's exit code or output can block, modify, or simply observe the action that triggered it. Hooks are how a user encodes rules that the agent should follow without having to remind it: instead of telling the agent "always run tests before committing," a pre-commit hook *enforces* it by failing the commit if tests don't pass.

## Why it matters

Hooks shift the locus of rule-following from the agent's compliance ("please remember to run tests") to the runtime ("the runtime won't let you commit without tests"). This matters because LLMs are imperfect at consistent rule-following over long sessions; runtime enforcement is unconditional. The result, in regent0x_'s phrase: *"you stop reminding claude of your rules because the rules enforce themselves."*

Hooks complement [[claude-code-skills]] (which teach the agent how to perform tasks) and [[claude-code-slash-commands]] (which give the agent quick-callable workflows). Skills are *descriptive*; hooks are *imperative*; commands are *invocational*. Together they form the agent-control surface around the model.

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — names three concrete hook patterns: a **pre-commit hook** that enforces TDD via [[wiki/entities/tdd-guard]], a **session-start hook** that loads memory from Obsidian and recent session logs (priming context), a **pre-push hook** that runs security review before code hits the remote.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — **cost counterpoint**. UserPromptSubmit hook injection is the 3rd-largest [[claude-code-overhead-patterns|overhead pattern]] (~11% of tokens). Author had 4 plugins → 3 UserPromptSubmit hooks injecting context = 6,200 tokens *before Claude reads what you asked*. Cut to 1 hook (just git branch); saved 5,800 tokens per prompt. Plugin auto-update SessionStart hooks were a separate 9th pattern (~3% of tokens, just for "loaded successfully" notifications). The principle: audit every hook; if you can't articulate why this hook fires on every prompt, kill it.

## Sub-claims and details

- **Common hook events** (per regent0x_): session start, pre-commit, pre-push. Other events likely exist (pre-tool-use, post-tool-use) but aren't enumerated in current sources.
- **Hook actions**: gating (block the action), augmenting (inject context), observing (log).
- **Composition with skills**: a hook can invoke a skill (e.g. session-start hook calls a "load-memory" skill). The hook is the trigger; the skill is the work.
- **Composition with [[subagents]]**: hooks fire across subagent invocations; e.g. pre-commit fires regardless of which subagent commits.
- **Source of authority**: hooks are configured in the user's Claude Code settings (settings.json or equivalent). They are local to the machine / repo and don't travel with the agent across environments unless deliberately checked in.

## Open questions and contradictions

- **Sandbox semantics**: a hook is shell. What can it not do? What permissions? Sources don't address.
- **Failure modes**: if a session-start hook fails, does the session refuse to start, or proceed without context? Unclear.
- **Versioning**: as Claude Code evolves event names, hooks may break silently. A way to declare required event names would help.
- **Discoverability**: how does a user know which hooks are configured at any moment? UI surface vs. inspection of config file.

## Related concepts

- [[claude-code-skills]] — descriptive sibling; skills teach, hooks enforce.
- [[claude-code-slash-commands]] — invocational sibling; commands trigger workflows on demand, hooks trigger on lifecycle events.
- [[markdown-as-agent-contract]] — hook configuration is the *imperative* counterpart to the *declarative* CLAUDE.md.
- [[subagents]] — hooks fire across subagent invocations.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/tdd-guard]] — typical pre-commit hook target.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
