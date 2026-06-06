---
type: concept
title: Ralph Loop
created: 2026-06-06
updated: 2026-06-06
aliases: [initializer-coding-agent-loop, two-phase-agent-loop]
tags: [agent-harness, agentic-loop, long-horizon-tasks, anthropic, agentic-ai]
---

# Ralph Loop

> An Anthropic two-phase agent pattern for tasks that span multiple context windows: an Initializer Agent sets up the environment once, then a Coding Agent re-enters each session, reconstructs state from the filesystem, picks the highest-priority incomplete work, executes, commits, and summarizes.

## Definition

The **Ralph Loop**, per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]], is a pattern for work too large for a single context window. It splits the work into two roles:

- **Initializer Agent** — runs once: sets up the environment, creates a progress file, enumerates a feature list, and makes the initial commit.
- **Coding Agent** — runs once per session: reads the git logs and progress file, picks the highest-priority incomplete feature, works on it, commits, and writes a summary of what it did.

The filesystem (git history + progress file) serves as the continuity mechanism across context windows, so each fresh session can reconstruct where the work stands without retaining prior context in-window.

## Why it matters

It is a concrete answer to the long-horizon problem in agent harnesses: how to make progress on a task that cannot fit in one context window. Rather than relying on ever-larger context or in-window memory, the Ralph Loop externalizes state to durable artifacts (git logs, a progress file) and makes each session stateless-but-resumable.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as an Anthropic two-phase pattern for tasks spanning multiple context windows. Initializer Agent sets up env + progress file + feature list + initial commit; Coding Agent each session reads git logs + progress, picks the highest-priority incomplete feature, works, commits, summarizes. Filesystem = continuity.

## Sub-claims and details

- Attributed to Anthropic as a two-phase pattern for multi-context-window tasks. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Initializer Agent (runs once): sets up environment, creates progress file, enumerates feature list, makes initial commit. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Coding Agent (each session): reads git logs + progress file, selects highest-priority incomplete feature, works, commits, writes a summary. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- The filesystem provides continuity across context windows. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])

## Open questions and contradictions

- The source does not specify how priority among incomplete features is decided, nor how conflicts or partial work are reconciled across sessions.

## Related concepts

- [[agentic-loop]] — the Ralph Loop is a specific multi-session instance of an agentic loop.
- [[agent-harness]] — the pattern is a harness-level design for long-horizon work.
- [[external-memory]] — the filesystem-as-continuity mechanism.
- [[context-window]] — the constraint the loop is built to work around.

## Related entities

- [[wiki/entities/anthropic]] — origin of the pattern as described.

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
