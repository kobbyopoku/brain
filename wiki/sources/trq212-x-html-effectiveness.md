---
type: source
title: Using Claude Code — The Unreasonable Effectiveness of HTML — Thariq (@trq212)
created: 2026-05-08
updated: 2026-05-08
content_status: substantive
source_url: https://x.com/trq212/status/2052809885763747935
source_type: x-thread
author: Thariq Shihipar
source_date: 2026-05-08
raw_path: raw/Thariq (@trq212)\n8K likes · 492 replies.md (URL stub only — body retrieved via Simon Willison's blog post + thariqs.github.io/html-effectiveness)
secondary_source_url: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
tags: [claude-code, agent-output-formats, html-vs-markdown, anthropic, artifact-first-workflow]
---

# Using Claude Code — The Unreasonable Effectiveness of HTML — Thariq (@trq212)

> Thariq Shihipar (Claude Code lead at Anthropic) argues that **HTML is a better default output format for agentic Claude Code than Markdown**. The thread spawned a Simon Willison blog post (cited as secondary source), an HN front-page discussion, and a public examples gallery at [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness). Highest-engagement post in the 2026-05-08 batch ingest (8K likes / 492 replies).

## TL;DR

The argument: when an agent's output is meant to be reviewed / clicked / compared / edited / shared, **HTML is closer to the real workspace than Markdown**. Markdown won the GPT-4-era token-budget race; with modern context windows, HTML's richer affordances (SVG diagrams, interactive widgets, collapsible sections, side-by-side comparisons, inline annotations on diffs) materially improve handoff. Thariq published 20 worked examples at thariqs.github.io/html-effectiveness — each one trades *"a wall of text you'd skim"* for *"a document you'd actually read."*

## Key takeaways

### The core thesis: handoff > execution

Thariq's framing: *"the hard part of agentic work is not only execution — it is handoff, where a model may finish a task but a human still has to judge risks, split follow-ups, share context, record decisions, and decide what happens next. HTML works as a bridge that is lighter than building a full app, but richer than static notes."*

Material because most prior wiki coverage of agent output formats focused on the agent-side (what the agent produces, how it streams, what the tokens cost). Thariq reframes around the **human-side cost**: how readable, navigable, comparable is the output?

### Use cases where HTML beats Markdown

From the examples gallery and Simon Willison's coverage:

- **Side-by-side direction comparisons** — render 3 alternative approaches as columns instead of sequential walls of text.
- **Annotated diffs / call-graphs / module diagrams** — spatial information presented as spatial output. Code review surfaces are particularly strong here.
- **PR descriptions with inline severity color-coding** — *"Help me review this PR by creating an HTML artifact that describes it... Render the actual diff with inline margin annotations, color-code findings by severity."*
- **Inline SVG figures, flowcharts, vector art** — generate once, paste into other documents.
- **Explainers with collapsible sections, tabbed code samples, glossaries** — make new topics navigable.
- **Threat-context analyses** with high-level summary + pattern analysis + specifics.

Simon Willison tested this on [copy.fail](https://copy.fail) (a Linux security-exploit explainer) — generating an HTML page from obfuscated Python code that successfully organized the explanation into navigable sections.

### Why this is a shift, not just a preference

The Markdown-first convention emerged in the GPT-4 era when the 8,192-token context limit made every token expensive. Markdown's efficiency was load-bearing then. With modern context windows (Claude Sonnet 4.6+ at 200K-1M tokens), the token-cost argument has weakened — and HTML's richer affordances become available without practical penalty.

Simon Willison: *"This represents a shift from his previous default approach."* From the wiki's perspective, this is a meaningful reversal of [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]]'s implicit assumption that markdown is the canonical agent-readable format.

### Cross-cite with the wiki's existing concepts

This thread strengthens, contextualizes, and partially complicates several wiki concepts:

- [[wiki/concepts/artifact-first-workflow]] — Open Design's `<artifact>` HTML emission is *exactly* this pattern. Thariq independently argues for it from inside Anthropic. Adds a strong *"Anthropic itself believes HTML is the right format"* signal to the artifact-first thesis.
- [[wiki/concepts/markdown-as-agent-contract]] — *partial reversal*. Markdown-as-contract still applies to *configuration / SOPs / instructions* (CLAUDE.md, AGENTS.md, SKILL.md, DESIGN.md). Thariq's argument is about *outputs* — what the agent produces *for the human to review*. The two layers (contract vs output) should now be split more carefully in the wiki.
- [[wiki/concepts/design-md]] — DESIGN.md is a configuration artifact (markdown), but it's consumed by an agent that *outputs* HTML. Thariq's piece reinforces this asymmetry.
- [[wiki/sources/nexu-io-open-design]] — Open Design's entire architecture (sandboxed `srcdoc` iframe, HTML→PDF/PPTX export pipeline) is the practical implementation of Thariq's thesis. Open Design predates this thread but shares the bet.

## Notable quotes

> *(via Simon Willison's blog)* "If an output is meant to be reviewed, clicked, compared, edited, or shared, HTML is often closer to the real workspace."

> *(via Simon Willison's blog)* "Help me review this PR by creating an HTML artifact that describes it... Render the actual diff with inline margin annotations, color-code findings by severity."

> *(Simon Willison's commentary)* "This represents a shift from his previous default approach."

## Notes

- **This source is reconstructed from a secondary source** (Simon Willison's blog post at simonwillison.net) rather than the original X thread (X.com returns HTTP 402 to bot fetches as of 2026-05). The substantive arguments and example use cases are well-covered by Willison; some specific tweet quotes may be paraphrased rather than verbatim. Treat as faithful summary, not exact transcription.
- **Examples gallery** at [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness) — 20 worked HTML artifacts. Worth visiting directly for the canonical reference.
- **Hacker News discussion** at https://news.ycombinator.com/item?id=48071940 — community engagement adds context, including pushback on whether HTML is universally better (some argue Markdown still wins for terminal-rendered or pipe-able output).
- **Cross-language coverage** — Chinese-language tech blogs (gyznsw.cn, abmedia.io) and Japanese (blog.lai.so) all picked it up. Indicates global Anthropic-engineer-said-this signal-amplification.
- **Important asymmetry to keep clear** as the wiki evolves: this thread is about **agent OUTPUT format** (what the agent gives the human). It does NOT contradict markdown-as-agent-contract for **agent INPUT format** (what the human gives the agent — CLAUDE.md, SKILL.md, DESIGN.md, AGENTS.md). The wiki should distinguish these two layers consistently.

## Mentioned entities

- [[wiki/entities/trq212]] — Thariq Shihipar.
- [[wiki/entities/anthropic]] — Thariq's employer; Claude Code is Anthropic's product.
- [[wiki/entities/claude-code]] — the platform the thread is about.

## Related concepts

- [[artifact-first-workflow]] — exactly the pattern Thariq advocates.
- [[markdown-as-agent-contract]] — partial reversal for output-side; still applies to input-side.
- [[design-md]] — input-side markdown that produces output-side HTML.
- [[claude-code-skills]] — adjacent (skill artifacts are markdown; output may be HTML).

## Related sources

- [[wiki/sources/nexu-io-open-design]] — practical implementation of Thariq's thesis (sandboxed-iframe HTML artifacts + PDF/PPTX export).
- [[wiki/sources/open-design-catalog]] — the 71 SKILL.md bundles in Open Design produce HTML artifacts, not Markdown.
