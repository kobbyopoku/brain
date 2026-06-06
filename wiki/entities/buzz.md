---
type: entity
title: Buzz
entity_type: product
created: 2026-06-06
updated: 2026-06-06
website: ""
aliases: []
tags: [agentic, agent, community-management, self-improving]
---

# Buzz

> [[wiki/entities/warp|Warp]]'s self-improving community-engagement agent — it monitors mentions of Warp, decides whether to reply, drafts messages for human approval, and updates its own skill files from team feedback.

## Profile

Buzz is the internal agent built by [[wiki/entities/warp|Warp]] to help its Developer Experience team respond to community mentions. It monitors mentions of Warp across Twitter, LinkedIn, and other platforms, and for each mention decides whether to reply, like, note, or skip. When a reply is warranted it drafts a message and posts the suggestion into [[wiki/entities/slack|Slack]], where a Warp human writes the final reply. Buzz runs in the background via Warp's orchestration product [[wiki/entities/oz|Oz]], and improves itself: once a day it compares its recommendations against what the team actually did, extracts durable learnings, updates its skill files, and opens a PR.

## Key facts

- **Owner**: built by [[wiki/entities/warp|Warp]] (cited to [[wiki/sources/petradonka-agents-need-feedback-loops]])
- **Function**: monitors mentions of Warp across Twitter, LinkedIn, and other platforms; for each mention decides whether to reply, like, note, or skip
- **Drafting**: when a reply is warranted it drafts a message and posts the suggestion into [[wiki/entities/slack|Slack]]
- **Human-in-the-loop**: every reply is still written by a Warp human in the end
- **Volume**: processes thousands of mentions a month across Twitter, Reddit, Bluesky, LinkedIn, and other channels; about half of mentions do not need a reply
- **Skills**: runs on around 15 skills across triage, drafting, learning, analytics, and reporting
- **Runtime**: runs in the background via [[wiki/entities/oz|Oz]], triggered by scheduled jobs or incoming mentions

(All facts cited to [[wiki/sources/petradonka-agents-need-feedback-loops]].)

## Positions and claims

- **Principles over checklists** — Buzz's first version was a long checklist of rules; it was rewritten to use principles instead. (Argued in [[wiki/sources/petradonka-agents-need-feedback-loops]].)
- **Self-improvement via feedback loop** — once a day Buzz collects [[wiki/entities/slack|Slack]] reactions and thread feedback, compares its recommendations to what the team did, extracts durable learnings, updates skill files, and opens a PR. (See [[wiki/sources/petradonka-agents-need-feedback-loops]].)

## Mentioned in

- [[wiki/sources/petradonka-agents-need-feedback-loops]] — Warp's self-improving community-engagement agent and the central subject of the source.

## Related entities

- [[wiki/entities/warp]] — the company that built Buzz.
- [[wiki/entities/oz]] — Warp's orchestration product that runs Buzz in the background.
- [[wiki/entities/slack]] — where Buzz posts suggestions and reads team feedback.
- [[wiki/entities/petra-donka]] — author of the source; gave feedback to Buzz on its drafted replies.
