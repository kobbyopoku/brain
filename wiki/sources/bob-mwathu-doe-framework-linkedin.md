---
type: source
title: There's a new way to build AI agentic systems — Bob Mwathu (LinkedIn)
created: 2026-05-05
updated: 2026-05-05
content_status: substantive
source_url: https://www.linkedin.com/posts/bob-mwathu_theres-a-new-way-to-build-ai-agentic-systems-activity-7413147110675750912-cRU4
source_type: linkedin-post
author: Bob Mwathu
source_date: 2025-2026
raw_path: (none — fetched live via WebFetch)
tags: [doe-framework, agentic-workflows, derivative-source, n8n-comparison, self-annealing]
---

# There's a new way to build AI agentic systems — Bob Mwathu (LinkedIn)

> The LinkedIn post that surfaced Saraev's **DOE framework** for this wiki via Kobby's question. Derivative — paraphrases Saraev's late-2025/2026 follow-up content. Notable contributions: explicit **comparison with [[wiki/entities/n8n|n8n]] / Make** (no longer the orchestrator — agent autonomously routes), and the term **"self-annealing"** as a system-level property.

## TL;DR

Mwathu's framing: traditional drag-and-drop tools like [[wiki/entities/n8n|n8n]] and Make put *the user* in the orchestrator role. Saraev's DOE framework moves orchestration into the agent itself. Three-layer breakdown:

- **D — Directive**: instructions / SOPs / goals in natural language.
- **O — Orchestration**: the agent itself; reads directives, decides which tools to use and when. *"You're no longer the orchestrator — the agent handles routing and decision-making autonomously."*
- **E — Execution**: tools, typically Python scripts (lead-scraping, CRM updates, email-sending). *"Think of this as the actual nodes/modules but far more flexible."*

Three named advantages: **faster to build**, **more scalable**, **systems that can self-improve over time (what Nick calls self-annealing)**.

## Key takeaways

### Drag-and-drop workflow tools vs DOE

Mwathu's framing makes one comparison sharply: in n8n / Make, *the user* draws the routing graph. In DOE, the orchestrator (agent) decides routing at runtime. This is the same observation as [[wiki/concepts/agent-workflow-patterns|agent-workflow-patterns]]'s split between *workflows* (deterministic routing) and *agents* (LLM-decided routing) — Mwathu just frames it via the n8n contrast specifically, which lands well for builders coming from no-code automation.

### "Self-annealing" as a named property

The term *self-annealing* is the most substantive contribution of this post. *"Systems that can self-improve over time (what Nick calls self-annealing)."* The wiki has the underlying mechanism documented (DOE's 4-step error-recovery loop in [[wiki/sources/saraev-agentic-workflows-2026|Saraev's original course]]) but the term itself wasn't named there. This post named it; the wiki's [[self-annealing]] concept page tracks the term back to Saraev's later content via this LinkedIn citation.

### Derivative-content acknowledgment

Mwathu opens with explicit credit: *"Before diving in, credit where it's due: Nick Saraev is the mind behind this approach, and honestly — it's genius. I just finished his full YouTube course."* This is good sourcing-discipline — distinguishes the post from "thought leadership" pieces that don't credit upstream.

### Lead-magnet / engagement mechanism

The post ends with *"comment 'DOE' for the slide deck summary and link to Nick Saraev's YouTube course."* Standard LinkedIn lead-magnet format. Worth flagging because: (a) the post's reach is partially driven by engagement-bait, not just substance; (b) the slide-deck Mwathu offers is itself a derivative that may have additional content not in the post text.

## Notable quotes

> "Before diving in, credit where it's due: Nick Saraev is the mind behind this approach, and honestly — it's genius."

> "Unlike n8n or Make you're no longer the orchestrator. The agent handles routing and decision-making autonomously."

> "Systems that can self-improve over time (what Nick calls self-annealing)."

## Notes

- **Mwathu is a content-creator**, not an original-framework coiner. His role for this wiki is *naming the term self-annealing* (which Saraev uses but which wasn't in our original course ingest) and *framing the n8n contrast* sharply.
- **This post is what surfaced DOE for the wiki** — Kobby pasted parts of this post when asking *"do a research on this and ingest all you can find"*. Without this post, the wiki would still have Saraev's 2-layer DO framing as canonical and missed the public evolution to 3-layer DOE.
- **Adjacent LinkedIn posts** found in the search but not separately ingested: [Aditya Somani's post](https://www.linkedin.com/posts/aditya-somani-03631727b_ai-agenticworkflows-automation-activity-7416068668083728384-zW1f) ("Nick Saraev's AI Agent Workflows Revolutionize Automation"); [Morgan Phillips's post](https://www.linkedin.com/posts/morgan-phillips-060632317_agentic-workflows-6-hour-course-beginner-activity-7409331782333960192-ZfCF) ("Variability and Self-Annealing"); [Manthan Patel's post](https://www.linkedin.com/posts/leadgenmanthan_watch-this-and-youll-know-more-about-n8n-activity-7357753358574587904-rAAX). Each adds incremental framing but is derivative-of-derivative of Saraev. Worth noting they exist; not worth ingesting individually unless they introduce new claims.

## Mentioned entities

- [[wiki/entities/bob-mwathu]] — author.
- [[wiki/entities/nick-saraev]] — original framework coiner; explicitly credited in the post.
- [[wiki/entities/n8n]] — workflow-tool counterpoint.

## Related concepts

- [[doe-framework]] — the framework this source describes.
- [[self-annealing]] — the term this source introduces to the wiki.
- [[agent-workflow-patterns]] — the workflow-vs-agent distinction Mwathu's n8n-contrast operationalizes.
- [[ai-automation-services]] — Mwathu's audience are services-business builders.

## Related sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — original Saraev course Mwathu paraphrases.
- [[wiki/sources/prakash-bhandari-doe-framework]] — sibling derivative source with cleaner expository depth.
