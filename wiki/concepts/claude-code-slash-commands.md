---
type: concept
title: Claude Code Slash Commands
created: 2026-05-02
updated: 2026-06-06
aliases: [slash commands, /commands, custom commands]
tags: [claude-code, mechanism, automation]
---

# Claude Code Slash Commands

> User-defined or plugin-distributed shortcuts in Claude Code: typing `/<name> [args]` invokes a pre-baked workflow that would otherwise require typing a paragraph of instructions.

## Definition

A **slash command** is an invocation shortcut in Claude Code. The user types `/<name>` (optionally with arguments) and the agent executes a pre-defined workflow associated with that name. Commands can be local to a project, user-global, or distributed via plugin marketplaces. They are the *imperative shortcuts* of the agent control surface, complementary to the *triggered actions* of [[claude-code-hooks]] and the *teachable capabilities* of [[claude-code-skills]].

## Why it matters

Slash commands eliminate the cost of typing out repetitive instructions. The trigger condition is regent0x_'s rule: *"every time you catch yourself typing the same instruction for the third time, that's a slash command waiting to happen."* The pattern compounds — once a command exists, it becomes a stable interface that other workflows (hooks, subagents, even other commands) can invoke.

Slash commands are also the **most user-visible part of the Claude Code agent surface**. CLAUDE.md is read silently, hooks fire silently, but a slash command shows up in the user's typing. It's where personal automation becomes muscle memory.

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — names concrete examples: `/fix-issue 456` (read GitHub issue → branch → fix with tests → open PR), `/review` (trigger reviewer subagent with security and coverage checks), `/deploy staging` (run full deployment pipeline through the ops subagent). References [[wiki/entities/wshobson-commands]] (1.7k+ stars per the post: "15 workflows + 42 tools").
- [[wiki/sources/khairallah-ai-automations-10k-month]] — references the `/schedule` command as the entry point to [[scheduled-automation]]; positions scheduled automations as the highest-value class of automation a service-provider can sell.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it as the invocation surface for a skill: Step 4's `/your-skill` is how the skill workflow gets called.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] frames it as the front of an autonomy loop: Setup 7's `/goal` is a slash command paired with a completion condition that drives 30-50 autonomous turns.

## Sub-claims and details

- **Format**: `/<name> [args]`. Names are kebab-case or single-word.
- **Distribution**: per-project (in repo), user-global (in `~/.claude/`), plugin-namespaced (e.g. `commit-commands:commit-push-pr`).
- **Composition with [[subagents]]**: a command often dispatches to a subagent (e.g. `/review` → reviewer subagent).
- **Composition with [[claude-code-skills]]**: a command can invoke a skill as part of its workflow.
- **Composition with [[claude-code-hooks]]**: a command is a *user-initiated* trigger; a hook is a *lifecycle* trigger. Same destination (a workflow), different on-ramp.
- **Two perspectives on the same artifact**:
  - From a **workflow-engineering** angle (regent0x_), commands are productivity multipliers.
  - From a **services-business** angle (Khairallah), `/schedule` specifically is the highest-value command class because scheduled automations run unattended and accrue value continuously.

## Open questions and contradictions

- **Argument schema**: how does a command declare its expected arguments? Examples in the sources show free-form args; a structured schema would help reliability.
- **Discovery**: how does a user know which commands exist in a session? UI surface (autocomplete) vs. listing.
- **Conflict resolution**: when two plugins ship a command with the same short name, who wins? Namespacing seems necessary but unspecified in current sources.

## Related concepts

- [[claude-code-skills]] — different mechanism, same platform.
- [[claude-code-hooks]] — different trigger model, same platform.
- [[scheduled-automation]] — `/schedule` is a notable command; scheduled automations are the highest-value class.
- [[markdown-as-agent-contract]] — command definitions live as markdown files in the repo.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/wshobson-commands]] — production slash command collection.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/charliejhills-full-agent-system-6-steps]]
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]]
