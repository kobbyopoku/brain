---
type: source
title: Igor Buzovskyi — Hermes /goal full guide (v0.14 Foundation Release)
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/IBuzovskyi/status/2056764150936748082
source_type: x-thread
author: Igor Buzovskyi (IBuzovskyi)
source_date: 2026-05-19
raw_path: raw/Hermes goal — THE FULL GUIDE.md
content_status: substantive-verbatim
tags: [hermes-agent, goal-command, autonomous-agents, agent-runtime, claude-code]
---

# Igor Buzovskyi — Hermes /goal full guide (v0.14 Foundation Release)

> Operational guide to **Hermes Agent's `/goal` command** — introduced in v0.14 (Foundation Release). `/goal` turns Hermes from a reactive chat-like agent into a **persistent background worker** that breaks down a long-term objective into sub-tasks, executes them with tools, iterates, and continues until completion (or the user stops it). Quote: *"transforms Hermes from a reactive chatbot into a background worker that can handle complex, multi-step tasks with minimal supervision."*

## TL;DR

**Seven commands** form the `/goal` interface:

| Command | Function |
|---|---|
| `/goal <description>` | Starts working on a long-term goal |
| `/goal` or `/goal status` | Shows current progress |
| `/goal pause` | Pauses the current goal |
| `/goal resume` | Resumes a paused goal |
| `/goal clear` | Clears the current goal |
| `/subgoal <text>` | Adds extra conditions or sub-objectives mid-execution |
| `/handoff <platform>` | Transfers the session to Telegram, Discord, etc. |

**Goal quality determines result quality**: *"the more clearly you can describe the final outcome and how to verify it, the better Hermes will perform."* Good goals are *specific + measurable + scoped + have clear success criteria*. Weak goals (*"make something cool"*, *"improve my code"*) fail.

**Configurable**: `hermes config set goals.max_turns 500` for long-running tasks.

## Recommended workflow

1. Provide project context first (tech stack, folder structure, prior decisions).
2. *(Optional)* meta-prompt: *"Based on what you know about me and my projects, suggest 3 strong /goal ideas that would run for a long time and create the most value."*
3. Launch the goal.
4. Manage with `/goal status` + `/subgoal` to steer mid-flight.
5. Review result — Hermes returns completed work, a summary, or an explanation if the goal couldn't be fully achieved.

## Use cases worked

- **Complex multi-step builds**: Flappy Bird HTML5 clone with physics + controls + scoring + collision detection.
- **Refactoring**: *"Refactor the main processing module, improve performance by 30%, add proper error handling, and ensure all tests pass."*
- **Research**: *"Research 5 competitors in the AI productivity space. Create a structured comparison table…"*
- **Websites**: *"Build a clean multi-page website… pass basic Lighthouse checks."*

## Best practices + traps

**Best practices**:
- Always make goals measurable with clear success criteria.
- Use `/subgoal` actively to steer.
- Increase `max_turns` for long-running tasks.
- Combine Hermes with Codex or Claude Code for better results.
- Run complex goals overnight.

**Common mistakes**:
- Vague goals without success criteria.
- Intervening too often instead of letting the agent work.
- Starting without enough project context.
- Goals too broad or open-ended.

**Not ideal for**: simple/quick tasks, situations needing full step-by-step control, undefined outcomes.

## How this composes with the wiki

- [[wiki/entities/hermes-agent]] — `/goal` is the v0.14 feature that promotes Hermes from chat-style to truly autonomous; aligns with the entity's *self-improving learning loop* description.
- [[wiki/projects/helm]] — Helm's Hermes Agent runtime gains the `/goal` primitive; the build-order Week 1 Lead Management agent can be initiated as a single `/goal` after the runtime is up.
- [[wiki/concepts/reasoning-execution-split]] — `/goal` decomposes the high-level objective (reasoning) into tool-calling steps (execution), the canonical pattern.
- [[wiki/concepts/do-framework|DOE framework]] — `/goal <description>` is the **Directive**; Hermes's internal task breakdown is the **Orchestration**; the tool calls are the **Execution**. Clean DOE composition at the user-command surface.
- [[wiki/concepts/self-annealing]] — Hermes's iteration loop ("breaks it down… iterates… continues until completed") is self-annealing on the per-goal scale.

## Notable quotes

> *"/goal turns Hermes into an autonomous agent. You set a long-term objective, and Hermes will break it down into smaller tasks, use tools, write and run code, iterate, and continue working until the goal is completed (or until you stop it)."*

> *"Start with a clear end result + verifiable criteria. You can always add more details later using /subgoal."*

## Mentioned entities

- [[wiki/entities/IBuzovskyi]] — *(new)* author.
- [[wiki/entities/hermes-agent]] — primary subject.

## Related concepts

- [[reasoning-execution-split]] — `/goal` is the canonical split surface.
- [[doe-framework]] — `/goal` is a DOE Directive at the command line.
- [[self-annealing]] — Hermes's iteration loop.
- [[scheduled-automation]] — *"Run complex goals overnight"* is the keystone use case.

## Related sources

- [[wiki/sources/shannholmberg-hermes-agent-operator]] — operator-level Hermes guide; reads as the architectural counterpart to this operational one.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — integrations layer Hermes plugs into.
- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — `/goal` applied to a clipping-business workflow.
