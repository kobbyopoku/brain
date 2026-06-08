---
type: source
title: The DOE Framework — How AI Agents Think, Plan & Act — Prakash Bhandari
created: 2026-05-05
updated: 2026-05-05
content_status: substantive
source_url: https://www.prakashbhandari.com.np/posts/doe-framework-how-ai-agents-think-plan-and-act/
source_type: blog-post
author: Prakash Bhandari
source_date: 2025-2026
raw_path: (none — fetched live via WebFetch)
tags: [doe-framework, agentic-workflows, ai-architecture, secondary-source]
---

# The DOE Framework — How AI Agents Think, Plan & Act — Prakash Bhandari

> Cleanest expository treatment of Saraev's 3-layer **DOE framework** (Directive + Orchestration + Execution) ingested into the wiki. Surfaced via Kobby's question about a LinkedIn post; this blog post is the most substantive primary-source-style writeup. Adds the *"Act → Observe → Think → Act"* runtime loop as orchestration's contract and a worked travel-booking example.

## TL;DR

Bhandari frames DOE as *"a three-layer architectural model for AI agents"*: Directive (the "what & why"), Orchestration (the "how & who"), Execution (the "doing"). Each layer is independently improvable, parallelizable, and debuggable. The orchestration layer's runtime is the *Act → Observe → Think → Act* loop, allowing real-time plan adaptation when execution results come back unexpected. The framework is positioned as foundational for *"reliable, real-world agentic systems rather than relying on single models attempting everything simultaneously."*

## Key takeaways

### Three layers, each with a "&" question

- **Directive — *"What & Why?"*** — the mission. Establishes the high-level goal handed to the system. *"A good directive captures intent. It doesn't need to say 'go to this URL, click this button, copy this text' — it simply states what needs to be accomplished."*
- **Orchestration — *"How & Who?"*** — the planning layer. Breaks goals into sub-tasks, routes them to appropriate tools, coordinates results. *"Handles failures gracefully, retries when needed, and adapts the plan when results come back unexpected."*
- **Execution — *"Doing"*** — specialized agents complete assigned actions and return results. Each executor is *"focused and specialised: it does one thing well and returns its result."*

### Act → Observe → Think → Act loop

Orchestration's runtime contract. Adds a meaningful addition to the Saraev original: the loop is *named explicitly* as orchestration's responsibility, distinct from execution's deterministic behavior. **Observation** in particular is called out — orchestration must read execution outputs and decide whether to proceed, retry, re-route, or abort.

### Modularity, parallelism, resilience, transparency

Bhandari surfaces four system-level properties of DOE:
- **Modularity** — each layer independently improvable.
- **Parallel execution** — orchestration can fan out independent sub-tasks.
- **Resilience via adaptive rerouting** — the orchestrator picks alternatives when an execution fails.
- **Transparency for debugging and alignment** — each layer has its own log; failures are localized.

### Travel-booking worked example

A directive *"find flights under $2,000"* flows through orchestration (search APIs, filter results, check user's calendar, book the chosen flight) into execution (HTTP calls, calendar reads, payment processing). When the orchestrator observes that all flights exceed $2,000, it adapts: re-route through alternate airports, check different dates, or report-back to the directive layer for re-spec.

## Notable quotes

> "A good directive captures intent. It doesn't need to say 'go to this URL, click this button, copy this text' — it simply states what needs to be accomplished."

> "Orchestration handles failures gracefully, retries when needed, and adapts the plan when results come back unexpected."

> "Foundational for building reliable, real-world agentic systems rather than relying on single models attempting everything simultaneously."

## Notes

- **Bhandari is a derivative-content author**, not an original framework coiner. The framework is Saraev's; Bhandari's contribution is the cleaner expository — naming the *Act → Observe → Think → Act* loop, the *"What & Why / How & Who / Doing"* mnemonic, and the four system-level properties. Worth reading in tandem with Saraev's original for understanding-by-pedagogy.
- **The wiki's pre-existing [[wiki/concepts/do-framework|DO framework page]] (now DOE)** captures the Saraev original (2-layer DO with implicit orchestrator) plus a "Framing evolution" section explaining how the concept shifted to 3-layer DOE. Bhandari is the cleanest source for the 3-layer framing.

## Mentioned entities

- [[wiki/entities/prakash-bhandari]] — author.
- [[wiki/entities/nick-saraev]] — original framework coiner.

## Related concepts

- [[doe-framework]] — the framework this source describes.
- [[self-annealing]] — implicit in Bhandari's *"adapts the plan when results come back unexpected"*; not named explicitly here but the mechanism is present.
- [[reasoning-execution-split]], [[reliability-decay-math]] — underlying motivations.
- [[markdown-as-agent-contract]] — directives are the meta-pattern instance.

## Related sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — original 5h+ course; the DO framing predecessor.
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]] — derivative LinkedIn post that surfaced this for the wiki.
