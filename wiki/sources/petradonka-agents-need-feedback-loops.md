---
type: source
title: "Petra Donka — Agents Need Feedback Loops, Not Perfect Prompts"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/petradonka/status/2054897826149101588
source_type: article
author: Petra Donka (@petradonka)
source_date: 2026-05-14
raw_path: raw/Agents Need Feedback Loops, Not Perfect Prompts.md
content_status: substantive-verbatim
tags: [agent, feedback-loop, self-improving, principles-over-rules, skills-as-code, warp, human-in-the-loop, agent-skills]
---

# Petra Donka — Agents Need Feedback Loops, Not Perfect Prompts

> Warp's account of building **Buzz**, a self-improving community-engagement agent — and the thesis that for judgement-heavy work, the durable engineering problem is not the prompt but the *loop* that lets the agent keep learning from the team after it ships.

## TL;DR

[[wiki/entities/petra-donka|Petra Donka]] (of [[wiki/entities/warp|Warp]]) argues that the obsession with writing better prompts misses the real challenge: the best prompt today is not the best prompt a month from now, because products, users, team taste, and edge cases all drift. For agents doing work that requires judgement and taste (social replies, support, code review, recruiting, docs), there is no cheap external check to retry against, so the engineering problem shifts from *"how do we write the perfect prompt?"* to *"how do we build agents that keep learning from the team after they ship?"* Warp's answer is **Buzz**, a community-engagement agent built on **principles instead of rules**, a **separate skill that teaches the agent how to learn** (generalize feedback into transferable principles), a **low-friction Slack emoji feedback loop** that lives where the team already works, and **agent skills treated like code** — every durable self-improvement lands as a reviewed daily PR. The goal is **compounding judgement**: every correction makes the next run a little better.

## Key takeaways

- **The starting prompt is only the beginning.** For judgement-heavy agent work, no static prompt can cover everything the agent will need — product, users, team taste, and edge cases all change over time. The right question is how to build agents that *keep learning from the team after they ship*.
- **Judgement-heavy work lacks a cheap external check.** Coding agents can retry against tests, builds, browser checks, and command output; social replies (and support, outreach, code-review comments, product-feedback analysis, docs, recruiting) cannot — the feedback loop there is too long, too noisy, and too expensive.
- **The "almost works" trap.** Many agents are clearly capable and produce output good enough to raise hopes but not good enough to trust; teams respond by endlessly tweaking the prompt. Donka calls this the wrong level of abstraction — getting the agent to do the task *once* is not the hard part.
- **Buzz** is Warp's agent that monitors mentions of Warp across Twitter, LinkedIn, Reddit, Bluesky, and other platforms, decides whether to **reply / like / note / skip**, drafts a message when a reply is warranted, and posts the suggestion into Slack. Every reply is still written by a human in the end.
- **Principles beat rules.** Buzz v1 was a long checklist of case-by-case rules; it was brittle, the prompt kept growing, replies were robotic, and it broke on unanticipated situations. Rewriting the skill as durable principles (e.g. *"Be helpful, not defensive"*, *"Check factual claims against the docs"*, *"Sound like someone who builds the product"*) made the skill file smaller and the agent better, because instructions stopped being a giant decision tree.
- **Feedback is not learning unless the agent can generalize.** Buzz initially turned every correction into a new rule (e.g. *"Never mention pricing in the first sentence"*) when the transferable principle was broader (*"If someone is venting, lead with empathy, not a pitch"*). The agent had to be *taught how to learn from feedback*.
- **A dedicated learning skill.** Warp built a separate "reply-learning" skill (published on GitHub) that examines the agent's suggestion, what the human did instead, and the current instructions, then asks: *what principle is missing or unclear?* Its 7-step process: (1) identify what went wrong/right from specific feedback; (2) ask why — find the underlying cause; (3) zoom out to the pattern; (4) check against existing principles; (5) write it as a principle, not a rule; (6) put it in the right section; (7) edit and commit, keeping the skill tight and merging overlapping principles.
- **Teaching an agent surfaces implicit taste.** A useful side effect of giving feedback is that it forces the team to make their own judgement explicit — *"A lot of taste lives implicitly in people's heads. Teaching an agent forces it onto the page."*
- **The feedback loop must fit where the team already works.** Warp avoided recurring meetings or assigned tasks; instead the team reacts to Buzz's Slack suggestion with an emoji for what they actually did, optionally adding a thread note. *One click is enough signal; a thread is extra context.*
- **Daily learning PR.** Once a day Buzz collects reactions and thread feedback, compares its recommendations to what the team actually did, extracts durable learnings, updates the relevant skill files, and opens a PR.
- **Agent skills should be treated like code.** Instructions that determine production behaviour should live in a repo with version history, review, and rollbacks. The daily learning agent does not change production behaviour directly — it opens a PR showing the feedback reviewed, the principle it thinks should change, and the exact diff; a human reviews it like any other change. This gives self-improvement *without giving up control*.
- **Scale and tooling.** Buzz processes thousands of mentions a month across Twitter, Reddit, Bluesky, LinkedIn, and other channels; about half need no reply. It runs on ~15 skills spanning triage, drafting, learning, analytics, and reporting, and uses Warp's **Oz** for agent management and orchestration so it can run in the background, triggered by scheduled jobs or incoming mentions.
- **Three durable lessons.** (1) Principles beat rules, because rules overfit and principles transfer. (2) Agents need to learn *how to learn*, or feedback turns into brittle exceptions. (3) The feedback loop has to live where the team already works, or people stop participating.
- **The goal is compounding judgement.** Rather than remove human judgement, the aim is to make it compound — every correction should make the next run a little better, and *"the best teams will not just write better prompts. They will build better loops."*

## Notable quotes

> "Everyone is trying to write better prompts for agents. While that's useful, it misses an important challenge: the best prompt you write today will not be the best prompt a month from now."

> "Getting an agent to do the task once is not the hard part. It is building a system where the agent gets better from the way your team already does the work."

> "The transferable principle is closer to: 'If someone is venting, lead with empathy, not a pitch.' The agent needed to be taught how to learn from feedback."

> "The best way to get leverage from agents is not to turn everyone into prompt engineers. It is to design workflows where the team's normal judgement and taste become a training signal for the systems around them."

> "Over time, the agent becomes less like a prompt someone wrote once and more like a working memory of how the team thinks. The best teams will not just write better prompts. They will build better loops."

## Notes

- This is a **first-party engineering narrative from Warp** (a company already in the wiki only as a design-catalog stub), and it is one of the strongest concrete articulations in the wiki of *self-improvement-as-reviewed-PR* — a different point on the where-does-improvement-live axis than the existing wiki entries. Compare:
  - [[wiki/sources/nousresearch-hermes-agent|Hermes Agent]] encodes self-improvement in **agent-internal state** (autonomous, less observable, bound to the runtime).
  - [[wiki/concepts/self-annealing|self-annealing]] (Saraev) encodes it in **directive markdown files** (durable, version-controlled).
  - Buzz sits closest to self-annealing but adds an explicit **human-review gate** (the daily PR) and an explicit **meta-skill that does the generalization**. The novel piece is the *learning-how-to-learn* skill — the wiki's prior sources assume the human or the agent rewrites instructions directly; here a dedicated skill mediates feedback → principle.
- **"Principles beat rules"** is a candidate new concept page. It is adjacent to but distinct from [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] (which is about *where* instructions live) — this is about *how* instructions should be written (durable principles that transfer vs. brittle enumerated rules that overfit). It also resonates with the larger [[wiki/concepts/anti-ai-slop-machinery|anti-slop]] discipline.
- **"Skills as code"** (repo + version history + review + rollback for agent instructions) generalizes the wiki's recurring [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] and [[wiki/concepts/claude-code-skills|skills]] threads into an explicit *governance* claim. Worth a concept page; it is the operational answer to *"do you really want an agent rewriting its own instructions?"* — yes, but through PR review.
- **The Slack-emoji feedback loop** is a clean instance of [[wiki/concepts/human-in-the-loop|human-in-the-loop]] design optimized for *participation cost* — "one click is enough signal." This is a transferable design principle for any [[wiki/concepts/ai-automation-services|services]] agent the wiki owner might build (e.g. for [[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]] or [[wiki/projects/helm|Helm]]'s 6-agent fleet, where a low-friction correction channel turns team taste into a training signal).
- **Oz** (Warp's agent management/orchestration product, at warp.dev/oz) is named but not described in depth here; it is a thin-but-citable new entity (Warp's background-agent orchestrator, comparable in role to APScheduler/cron triggers + a fleet manager).
- **Buzz** itself is a citable product/agent entity — Warp's internal community-engagement agent, ~15 skills, human-final-reply, self-improving via daily PR.
- Author handle in the raw frontmatter is `@petradonka`; the byline name "Petra Donka" is inferred from the handle and is *not stated verbatim* in the body — flagged as a mild inference.
- The piece is a strong companion to the wiki's multi-agent / self-improvement cluster and could later anchor a synthesis comparing the three self-improvement mechanisms (Hermes internal-state vs. self-annealing markdown vs. Buzz reviewed-PR-with-learning-skill).

## Mentioned entities

- [[wiki/entities/warp|Warp]] — the company that built Buzz; previously a design-catalog stub, now has primary-source facts (Developer Experience team, community-engagement agent, Oz orchestrator).
- [[wiki/entities/petra-donka|Petra Donka]] — author; writes from Warp's perspective (`@petradonka`).
- [[wiki/entities/buzz|Buzz]] — Warp's self-improving community-engagement agent (~15 skills; human-final replies; daily learning PR).
- [[wiki/entities/oz|Oz]] — Warp's agent management + orchestration product used to run Buzz in the background.
- [[wiki/entities/slack|Slack]] — where Buzz posts suggestions and the team's emoji-reaction feedback loop lives.

## Related concepts

- [[principles-over-rules]] — the load-bearing thesis: durable principles transfer, enumerated rules overfit and break.
- [[skills-as-code]] — agent instructions live in a repo with version history, review, and rollbacks; self-improvement lands as a reviewed PR.
- [[agent-feedback-loop]] — the durable engineering problem is the loop, not the prompt; learning must fit where the team already works.
- [[self-annealing]] — sibling self-improvement mechanism (directive-markdown-encoded); Buzz adds a human-review gate and a learning meta-skill.
- [[human-in-the-loop]] — the Slack-emoji feedback interface minimizes participation cost ("one click is enough signal").
- [[markdown-as-agent-contract]] — Buzz's skill files are agent contracts; this source adds the *principles-not-rules* and *governed-like-code* refinements.
- [[claude-code-skills]] — Buzz runs on ~15 skills across triage/drafting/learning/analytics/reporting.
- [[scheduled-automation]] — Buzz's once-a-day learning run and scheduled-job triggers via Oz.
- [[compounding-judgement]] — the stated goal: make human judgement compound rather than removing it.

## Related sources

- [[wiki/sources/nousresearch-hermes-agent]] — sibling self-improving agent; encodes learning in agent-internal state rather than reviewed markdown PRs.
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]] — introduces *self-annealing*, the directive-markdown sibling of Buzz's reviewed-PR self-improvement.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — agents-as-job-description+trigger+output; Buzz is a worked, production-grade instance of that model.
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — agent-vs-automation mental model (agent reads situation + makes judgement); Buzz is exactly such a judgement agent.
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — adjacent on the *write better instructions* axis that this source argues is necessary-but-insufficient.
