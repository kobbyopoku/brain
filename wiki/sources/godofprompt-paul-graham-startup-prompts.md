---
type: source
title: 6 Paul Graham-Style Startup Evaluation Prompts — godofprompt
created: 2026-05-02
updated: 2026-05-02
source_url: https://x.com/godofprompt/status/2040377584551358575
source_type: x-thread
author: godofprompt
source_date: 2026-04-04
raw_path: raw/Post by @godofprompt on X.md
tags: [prompts, startup, agent-config, claude-code]
---

# 6 Paul Graham-Style Startup Evaluation Prompts — godofprompt

> A short post packaging six structured prompts that pressure-test a startup idea using frameworks attributed to [[wiki/entities/paul-graham]]. Notable in the wiki because the prompts are written in a `<role>...<task>...` format that mirrors agent-contract conventions.

## TL;DR

godofprompt presents six Claude prompt frameworks — pressure test the idea, validate the real problem, map real competition, find first 10 customers, build MVP in 2 weeks, build growth engine — each cast as a `<role>` invocation of a Paul Graham-flavored persona. The post positions these prompts as a way to "pressure-test your idea before you waste months." The prompts themselves are partially truncated in the source; full text is not captured.

## Key takeaways

- **Six named prompt frameworks** (each opens with a `<role>` Paul Graham-flavored persona):
  1. **Pressure test your idea** — the "evaluator who has reviewed thousands of ideas and knows exactly which ones die in week one and which become billion dollar companies."
  2. **Validate the real problem** — customer-discovery specialist applying PG's "talk to users" framework.
  3. **Map your real competition** — competitive intelligence analyst applying PG's "what are people doing now" framework.
  4. **Find your first 10 customers** — early-traction specialist applying PG's "do things that don't scale" framework.
  5. **Build your MVP in 2 weeks** — MVP architect applying PG's "build something people want" framework.
  6. **Build your growth engine** — startup growth strategist applying PG's "make something people want and tell their friends" framework.
- **Format observation**: the prompts use XML-like tags (`<role>...</role>`, `<task>...</task>`). This is a recognizable pattern in Anthropic prompt engineering and overlaps with the [[skill-md|SKILL.md]] format philosophy — a structured directive an agent can reliably consume.
- **Free-resource pitch**: the post advertises Gemini Mastery Guide, Prompt Engineering Guide, Claude Mastery Guide, OpenAI Mastery Guide as ancillary free guides.

## Notable quotes

> "Most ideas sound good. Few survive real scrutiny."
> — opening

> "Act as a Paul Graham-style startup evaluator who has reviewed thousands of ideas and knows exactly which ones die in week one and which ones become billion dollar companies."
> — prompt 1, role line

## Notes

- **Prompts are truncated** in the captured source — each `<task>` block cuts off mid-sentence. The full text would need to be retrieved from the original post or a follow-up source.
- **The framing leans on Paul Graham's authority** without him having authored or endorsed these prompts. Treat as "Paul Graham-style," not "Paul Graham-authored."
- **Cross-source resonance**: [[wiki/sources/AnatoliKopadze-20-claude-prompts]] takes the same approach (curated personal prompts) at much higher volume and detail. godofprompt's contribution is a startup-specific niche of the same practice. See [[personal-claude-prompts]].
- **One sharp comment from the post**: *"prompts are cool but the real pressure test is 10 conversations with people who'd actually pay."* Worth carrying forward as a counterpoint when this wiki later treats the limits of LLM-only validation.

## Mentioned entities

### People
- [[wiki/entities/godofprompt]] — author.
- [[wiki/entities/paul-graham]] — referenced as the source of the frameworks the prompts are built on.

## Related concepts

- [[personal-claude-prompts]] — broader pattern this source instantiates.
- [[claude-code-skills]] — adjacent: structured prompts as the seed of skill files.
- [[markdown-as-agent-contract]] — `<role>/<task>` format is one approach to encoding agent contracts in markdown.

## Related sources

- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — much larger, more detailed catalog of personal prompts.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — the LLM Wiki pattern is itself a kind of prompt-engineering meta-pattern; this source is a narrow domain instance.
