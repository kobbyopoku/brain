---
type: source
title: nurijanian — /goal for Product Managers
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/nurijanian/status/2055927283991654775
source_type: x-thread
author: nurijanian (@nurijanian)
source_date: 2026-05-10
raw_path: raw/goal for Product Managers.md
content_status: substantive-verbatim
tags: [goal-command, product-management, claude-code, codex-cli, ralph-wiggum-loop, acceptance-criteria, executable-definition-of-done, pm-os, autonomous-agents, context-rot]
---

# nurijanian — /goal for Product Managers

> The native `/goal` command in [[wiki/entities/claude-code|Claude Code]] and [[wiki/entities/codex-cli|Codex CLI]] reframes product management around *executable definitions of done*: the more vague a requirement, the faster an unattended agentic loop converts it into the wrong thing — so PMs must now write observable behavior, negative cases, scope boundaries, validation evidence, and stop conditions, which is what [[wiki/entities/pm-os|PM OS]] aims to encode.

## TL;DR

nurijanian argues the native `/goal` command (Claude Code + Codex) is best understood not as new model autonomy but as **product design wrapped around the [[wiki/concepts/ralph-wiggum-loop|Ralph Wiggum loop]]** — a fresh-context agent that reloads durable files (spec, plan, task list, tests, status) each iteration while a separate evaluator judges whether the target is met from observable evidence. For PMs this collapses the gap between *prose requirements* and *target states*: a prompt asks for effort, a contract defines where effort stops. The core operating rule is **"define done, prove done, and keep the proof outside the chat."** [[wiki/entities/pm-os|PM OS]] exists to encode this product judgment (acceptance criteria, edge cases, validation evidence, stop conditions) as reusable workflows so each piece of work starts from a sharper [[wiki/concepts/executable-definition-of-done|definition of done]].

## Key takeaways

- **`/goal` is the Ralph Wiggum loop with product design around it** — not smarter models. The agent plans, edits, runs tests, repairs failures, updates status, and loops until the goal is met or hits a bound; a separate evaluator/harness checks whether the target is satisfied.
- **The useful part of Ralph was never a smarter model — it was fresh context at the start of each run.** Each iteration reloads durable files (spec, plan, task list, test suite, status notes) instead of trusting one bloated chat through compaction. "The conversation could rot, but the source of truth stayed outside the conversation."
- **A good Ralph loop has five durable artifacts**: a spec (target behavior), an ordered implementation plan, checkable acceptance criteria, tests/validation commands that prove progress, and a status file recording what changed/passed/still looks risky.
- **`/goal` separates doing the work from judging whether it's done.** The working agent must surface evidence *in the conversation* (test output, lint output, changed files, queue state) because the evaluator judges only from what it can see there.
- **The further out of the loop you go, the more leverage you get — but the more important setup and planning become.** When steering every turn, the plan can be loose because human attention fills gaps; stepping away forces the spec to do that work. Every Ralph iteration is a fresh agent instance with no memory of the last correction.
- **The spec and plan become the product surface.** PM work shifts from "write enough detail that an engineer understands the intent" toward "define done clearly enough that an agent can keep trying, a harness can inspect the evidence, and a human can tell whether the outcome is product-correct" — a much higher bar than a normal ticket.
- **The weak version of `/goal` reads like a wish** (`/goal improve onboarding`). With no way to know whether onboarding improved, the agent optimizes for whatever is easiest to *prove* (cleaner screenshots, passing tests, fewer steps) — none of which means the product got better. Same failure as vague PM tickets ("make activation easier", "reduce friction").
- **A one-shot mistake is annoying; a loop can spend 40 turns making the wrong thing more internally consistent.** That is where long-running agents get dangerous — humans rescue vague tickets through conversation; unattended agents keep converting vagueness into implementation.
- **The strong version gives the loop a finish line, a proof method, and a boundary** — a target state, source-of-truth files to read, acceptance criteria, validation commands (e.g. `npm test -- onboarding exits 0`), scope boundaries (only edit named paths), and a stop condition (e.g. stop after 20 turns with a status report if blocked).
- **Pair acceptance criteria with required validation evidence.** Each observable behavior maps to a proof (unit test for persisted state, integration test for first-time visibility, regression test for existing users, browser smoke test, DOM/screenshot evidence, analytics event-capture assertions) so "the evaluator can judge the transcript because the transcript contains proof instead of vibes."
- **Watch the first loops.** Don't write a giant spec, start the loop, and close the laptop. If the agent misunderstands the target, writes a test that blesses wrong behavior, touches unrelated files, or keeps asking the same question (a hidden ambiguity humans were silently resolving) — stop it, fix the spec/validation/boundaries, restart. The first loops are calibration; the loop becomes useful "after the spec survives contact with the model."
- **`/goal` is best where the target is concrete and validation is cheap**: migration work (`migrate all imports from legacyAuth to authClient`), backlog clearing (resolve every failing `@auth-regression` test), file splitting (split a file into modules under 250 lines, behavior unchanged), and brute-force testing (keep trying attack vectors, checkout paths, login flows until the queue is empty).
- **Exploration mode works if expectations differ** — the goal should produce *learning, not production code* (e.g. "explore three viable approaches… create a short note per approach… do not edit production code"). The dangerous version is asking an exploratory loop to silently become a production loop.
- **Agentic coding does not remove product thinking — it punishes vague product thinking faster.** The ticket is no longer enough on its own; the more useful artefact is an [[wiki/concepts/executable-definition-of-done|executable definition of done]]. "This has always been important, we just got sloppy, and with AI, even sloppier; so now we need to get back to the basics."
- **The status file is "your epic in JIRA, reimagined" — the durable memory layer.** It records what changed, which checks passed/failed, what decision the agent made, what remains risky, and what a human should inspect next. Every fresh turn reloads spec + status instead of reconstructing the project from a decaying conversation — this is how you avoid [[wiki/concepts/context-rot|context rot]].
- **Stop handing agents adjectives, vibes, and implementation-preferences-disguised-as-goals.** Replace "make it better/cleaner/easier/smarter" with observable states; replace "polish the onboarding flow" with named product behavior; replace "refactor into a cleaner architecture" with the specific pain the refactor must relieve. "This is the difference between delegating effort and delegating an outcome."
- **PM OS encodes the tacit PM work** that agent-ready acceptance criteria pull together: what user behavior matters, which edge cases are dangerous, which constraints are fake vs load-bearing, what validation evidence should count, when to stop an agent and ask for human judgment. It gives product work an operating layer — memory, context, workflows, assumptions, research, decisions, measurement, review.
- **Teams with good tests and crisp acceptance criteria get more useful loops; teams with mushy requirements get "longer, faster mush that burns their tokens."** "The tool is new, but the standard is old."
- **PM OS v2** (shipping "in a few days" as of the post) bundles improved memory, agents, and skill workflows, packaged with external skills the author uses: Ryan Singer's Shaping Skills (`/shaping`), and Matt Pocock's viral `/grill-me` skill for writing requirements with AI.

## A practical goal template

The author's recommended shape for goals handed to long-running agents:

```
/goal [specific target state]

Source of truth:
- read [spec file]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case]
- [non-regression condition]

Validation:
- [test command]
- [lint/typecheck/build command]
- [browser/visual/manual evidence if needed]

Boundaries:
- only edit [paths]
- do not change [systems]
- preserve [contract/data/API behavior]

Loop behavior:
- after each meaningful change, run the relevant validation
- update the status file with changed files, result, and remaining risk
- stop after [N turns/time] if blocked and report the blocker
```

## Notable quotes

> "That is the core idea behind the native /goal. The loop is only as good as the plan it reloads, the tests, the acceptance criteria, and the evidence it leaves behind."
> — nurijanian, "/goal for Product Managers"

> "A prompt asks for effort, while a contract defines the condition where effort stops."

> "A one-shot mistake is annoying. A loop can spend 40 turns making the wrong thing more internally consistent."

> "Agentic coding does not remove product thinking. It punishes vague product thinking faster."

> "The operating rule is simple: define done, prove done, and keep the proof outside the chat."

> "Teams with good tests and crisp acceptance criteria will get more useful loops. Teams with mushy requirements will get longer, faster mush that burns their tokens. The tool is new, but the standard is old."

## Notes

- **This is the PM-facing counterpart to the wiki's existing `/goal` cluster.** [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] and [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] cover `/goal` as an agent-runtime primitive (commands, Kanban, verification). nurijanian instead treats `/goal` as a *forcing function on product requirements* — the value is in the upstream spec/acceptance-criteria discipline, not the command mechanics. The two readings are complementary: the runtime executes the loop; the PM defines what the loop can inspect.
- **`/goal` as a native command claim.** The source frames `/goal` as native to both Claude Code and Codex (linking `code.claude.com/docs/en/goal` and an OpenAI cookbook example). The wiki's prior `/goal` sources attach the command primarily to Hermes Agent (v0.14) and a multi-runtime survey. Whether `/goal` is genuinely a first-party native command across all three runtimes, or whether the author is generalizing, is worth treating as **author's claim, not independently verified here** — flagged for the entity pages.
- **Strong fit with existing wiki concepts.** The "fresh context each iteration / source of truth outside the conversation" argument is the same mechanism as [[wiki/concepts/hot-cache|hot-cache]] and the [[wiki/concepts/llm-wiki-pattern|LLM Wiki pattern]] (durable external state vs decaying chat). The status-file-as-durable-memory point is the operational core of avoiding [[wiki/concepts/context-rot|context rot]].
- **Directly relevant to Godwin's work.** The status-file-as-reloadable-epic and executable-definition-of-done patterns map onto [[wiki/projects/helm|Helm]]'s agent-driven ops (each agent gets a trigger + prompt + output) and onto how acceptance criteria should be written for any of the ROAM products where agents do unattended work (e.g. Clarvyn's proactive HR agent, Kivora's RAG agent). The "define done, prove done, keep proof outside the chat" rule is a reusable spec-writing discipline.
- **`/grill-me` and `/shaping` are named external skills** (Matt Pocock, Ryan Singer) the author uses for requirement-writing with AI; both are GitHub skill repos. Worth tracking as candidates for the [[wiki/concepts/claude-code-skills|skills]] cluster.

## Mentioned entities

- [[wiki/entities/nurijanian]] — author; PM-OS builder; frames `/goal` as an executable-definition-of-done forcing function.
- [[wiki/entities/pm-os]] — the author's product (PM operating layer) that encodes agent-ready PM judgment into reusable workflows; v2 imminent at time of writing.
- [[wiki/entities/claude-code]] — names `/goal` as a native command.
- [[wiki/entities/codex-cli]] — OpenAI's coding-agent CLI; cited as having a parallel `/goal` and long-horizon examples.
- [[wiki/entities/ryan-singer]] — ex-Basecamp; author of Shaping (`/shaping`) skills bundled with PM OS.
- [[wiki/entities/matt-pocock]] — author of the viral `/grill-me` requirement-writing skill.

## Related concepts

- [[wiki/concepts/ralph-wiggum-loop]] — the bash-loop-with-fresh-context pattern `/goal` productizes.
- [[wiki/concepts/executable-definition-of-done]] — the artefact PMs must now produce; the central PM implication of the post.
- [[wiki/concepts/context-rot]] — the failure mode (decaying chat memory) the status file + reloaded spec defends against.
- [[wiki/concepts/hot-cache]] — same "durable state outside the conversation" mechanism, at the file layer.
- [[wiki/concepts/llm-wiki-pattern]] — Karpathy's external-markdown-as-source-of-truth pattern; sibling of the spec/status-file approach.
- [[wiki/concepts/claude-code-skills]] — `/shaping` and `/grill-me` are skill-pack instances for requirement-writing.
- [[wiki/concepts/reasoning-execution-split]] — `/goal` separates the working agent (does) from the evaluator (judges), a reasoning/judgment split.

## Related sources

- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — Hermes v0.14 `/goal` runtime command guide; the runtime-mechanics counterpart to this PM-facing reading.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — multi-runtime `/goal` survey (commands, Kanban, verification); shares the doing-vs-judging separation.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — *job description + trigger + output* framing; the agent-definition analogue to nurijanian's *target + proof + boundary*.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — origin of [[wiki/concepts/hot-cache|hot-cache]]; the file-layer ancestor of the status-file-as-durable-memory idea.
