---
type: concept
title: Personal Claude Prompts
created: 2026-05-02
updated: 2026-06-06
aliases: [curated prompts, prompt library, personal prompt catalog]
tags: [prompts, personal-productivity, claude, prompt-engineering]
---

# Personal Claude Prompts

> The practice of curating a personal library of high-quality, structured prompt templates — research synthesizers, brutal editors, salary-negotiation roleplayers, Feynman tutors, Socratic teachers — and pasting them on demand to turn a generic Claude session into a domain-specific tool.

## Definition

A **personal Claude prompt** is a reusable, fully-structured directive that turns a Claude session into a specific role for a specific task. Each prompt typically includes:

- A **role** assignment (e.g. "you are a senior research analyst").
- A **task** with a clear outcome shape.
- **Output rules** (sections, length limits, required elements).
- **Constraints** (what NOT to do, banned moves, behavioral commitments).
- Often a **template variable** to fill in (the topic, the draft, the resume).

The practice is to **maintain a personal catalog** of these prompts — organized by category — and recall the right one when the situation calls for it. The recall step matters: knowing *which class of prompt* the situation needs is part of the skill.

## Why it matters

A Claude subscription's ceiling isn't the model — it's the prompt. Most users underutilize Claude because they default to "ask, rewrite, summarize" and stop. A curated personal prompt library raises the ceiling by an order of magnitude: the same $20/month subscription becomes a research analyst, brutal editor, negotiation coach, financial analyzer, Feynman tutor, and Socratic teacher — depending on which prompt you reach for.

The practice is **adjacent to but distinct from [[claude-code-skills]]**. A Claude Code skill is *registered with the runtime* and activates by description-matching; a personal prompt is *pasted on demand* by the user. Skills work for repeatable workflows tied to the Claude Code environment; personal prompts work for one-shot uses in a vanilla Claude session. Many of the best personal prompts could be re-shaped as skills if the user crosses into Claude Code; until then, the catalog itself is the productivity multiplier.

## Treatment across sources

- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — canonical wiki source. Twenty detailed prompts across five categories (deep research, writing, career, daily life, learning). Each is fully written out, with role / task / structured output spec / explicit rules.
- [[wiki/sources/godofprompt-paul-graham-startup-prompts]] — narrower domain (startup evaluation). Six prompts framed as `<role>...<task>...` patterns invoking Paul-Graham-style personas.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] belongs to the genre; ships 5 verbatim ready-to-use prompts (Feynman explanation, travel, expense analysis, reflection partner, business-idea stress-test) plus setup meta-prompts.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] is the systems-level (settings/projects/memory) counterpart to prompt-library approaches — adjacent theme of Claude-as-personal-productivity-multiplier.

## Sub-claims and details

### Common shapes of high-quality personal prompts

Looking across both sources, the recurring shapes are:

1. **Role-then-task**: opens with a strong role assignment, then specifies the task.
2. **Critique-as-service**: Claude as ruthless critic / brutal editor / steelman builder. Explicit "do not soften" rules.
3. **Roleplay**: Claude plays an adversary (hiring manager, interviewer, customer) for practice scenarios.
4. **Multi-version output**: produce N variations (5 audience versions, 5 LinkedIn bios, 3 resume tailorings).
5. **Structured output spec**: numbered sections that the model must emit, with rules for each section.
6. **Banned-move list**: explicit "do not soften", "do not use these words", "do not summarize each separately."
7. **Pedagogical constraint**: Socratic mode (only questions), Feynman tutor (one concept at a time, comprehension check before next).

### What separates a good prompt from a bad one

- **Specificity of role** beats generic ("you are a research analyst" beats "be helpful").
- **Output structure as constraint** beats "give me an answer" (numbered sections, length limits, banned content).
- **Explicit "do not" rules** beat implicit assumptions (don't soften, don't add ideas, don't use these words).
- **Worked examples** when the model needs to match a tone or format.

### Bridge to Claude Code skills

Several of [[wiki/sources/AnatoliKopadze-20-claude-prompts|Anatoli's 20 prompts]] could be registered as Claude Code skills:

- **Multi-Source Synthesis** → an `ingest-research` skill.
- **The Brutal Editor** → a `brutal-edit` skill.
- **Devil's Advocate Mode** → a `devil-advocate` skill (and is a useful sub-mode of the [[lint]] operation).
- **Mental Model Builder** → a `mental-models` skill.

The benefit of registering: invocation by description-matching, no copy-paste, composable with [[claude-code-hooks]] and [[subagents]].

## Open questions and contradictions

- **Catalog organization**: Anatoli uses 5 categories (research, writing, career, daily life, learning); other catalogs may use task-type, audience, or domain. No standard exists.
- **Versioning**: a prompt that works today may degrade as the underlying model updates. The catalog needs maintenance — same problem as [[CLAUDE]] needing updates as conventions evolve.
- **Sharing vs. personal**: a personal catalog is by definition tuned to one person's voice and workflow. Shared catalogs are a different artifact. Both have value.
- **The XML-tagged style** ([[wiki/sources/godofprompt-paul-graham-startup-prompts]]'s `<role>...<task>...` pattern) vs. the markdown-structured style ([[wiki/sources/AnatoliKopadze-20-claude-prompts]]) — both work, but no convention has won.

## Related concepts

- [[claude-code-skills]] — registered version of the same shape.
- [[skill-md]] — file format that personal prompts can graduate into.
- [[markdown-as-agent-contract]] — broader meta-pattern.
- [[ingest]] — Anatoli's "Multi-Source Synthesis" prompt is a manual instance.
- [[lint]] — Anatoli's "Devil's Advocate Mode" is a wiki-applicable critique pattern.

## Related entities

- [[wiki/entities/anatoli-kopadze]] — author of the canonical catalog source.
- [[wiki/entities/godofprompt]] — author of the narrower startup-eval catalog.

## Mentioned in

- [[wiki/sources/AnatoliKopadze-20-claude-prompts]]
- [[wiki/sources/godofprompt-paul-graham-startup-prompts]]
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]]
- [[wiki/sources/heynavtoor-personal-ai-system-claude]]
