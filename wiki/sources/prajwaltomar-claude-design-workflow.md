---
type: source
title: Prajwal Tomar — The Claude Design Workflow That Actually Works
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/PrajwalTomar_/status/2056347864822083809
source_type: x-thread
author: Prajwal Tomar (@PrajwalTomar_)
source_date: 2026-05-18
raw_path: raw/The Claude Design Workflow That Actually Works..md
content_status: substantive-verbatim
tags: [claude-design, design-system, templates, claude-code-skills, ai-design, workflow, prajwal-tomar, ignytlabs, anti-vibe-designing, token-discipline]
---

# Prajwal Tomar — The Claude Design Workflow That Actually Works

> Prajwal Tomar (@PrajwalTomar_) documents a **4-step pre-establishment workflow** for [[wiki/entities/claude-design|Claude Design]] — design system, then templates, then a Claude Code/Desktop copy skill, *then* open Claude Design — arguing that the tool's quality problem is not the model but the user front-loading too few decisions into the first prompt.

## TL;DR

Most people "vibe design" in [[wiki/entities/claude-design|Claude Design]] — one cold prompt asking Claude to decide colors, fonts, layout, copy, and structure all at once — and burn through tokens iterating toward a mediocre result. Tomar's fix, used at his agency [[wiki/entities/ignytlabs|IgnytLabs]], is to **pre-establish everything before opening Claude Design**: (1) build a reusable design system, (2) build templates per repeatable deliverable, (3) pre-write copy with a Claude Code/Desktop skill, then (4) build in Claude Design from template + design system + pasted copy prompt. The result is a first-pass output that is "70-90% done" before a single pixel renders. He credits the 4-step structure to a YouTube video by [[wiki/entities/ben-ai|Ben AI]].

## Key takeaways

- **The core principle is "pre-establish as much as possible before you ever open Claude Design."** More defined upfront = less Claude has to guess = better first output = fewer iterations.
- **The failure mode it counters ("vibe designing")**: a single cold prompt forces Claude to make every decision (colors, fonts, layout, copy, structure) at once, producing generic, shifting output and an endless iteration loop that drains tokens.
- **Step 1 — Design system first, always.** A design system is "your brand's blueprint" (colors, fonts, button style, spacing) connected before building anything, so every output is automatically on-brand and consistent across deliverables. Built in Claude Design's **Design Systems tab** via a structured prompt (brand name, one-line description, 3-word personality, primary/accent color, font feel, button style, dark/light mode), then refined with a "needs work" feedback loop, then connected to every new project before prompting.
- **Step 2 — Templates per repeatable use case.** A template pre-defines layout/format/structure ("the skeleton the design system dresses up"). Built by screenshotting layouts from Claude Design's **Examples tab** (or [[wiki/entities/dribbble|Dribbble]] / [[wiki/entities/framer|Framer]] / [[wiki/entities/behance|Behance]]), recreating them in-brand as a slide deck with placeholder copy, then **Share → Duplicate as Template**. Reused via **From Template**. Iterating on layout is called "one of the biggest token wasters in Claude Design."
- **Step 3 — Pre-define copy with a skill (the "unlock").** Claude Design is a design tool, not a copywriter; iterating copy inside it "burns design tokens on a writing task." Instead, build a [[wiki/concepts/claude-code-skills|skill]] in [[wiki/entities/claude-code|Claude Code]] or Claude Desktop that knows brand voice, which template layouts to use for which content, and reference copy. Run it before each design; it maps sections to template layouts, writes copy with variations to choose from, and emits a ready-to-paste full design prompt.
- **Step 4 — Build in Claude Design.** Sequence: go to claude.ai/design → From Template → select template → connect design system → paste skill prompt → answer clarifying questions (or "decide for me") → review. First pass is "significantly better than any cold one-shot prompt" because structure, brand, and copy are all already fixed.
- **Four in-canvas refinement tools**: Direct edit (click text to change), Comments (click element + describe change), Draw (sketch on canvas, Claude interprets), Tweaks (color schemes / dark-light / layout variations without prompting).
- **Handoff to Claude Code**: Share → "handoff to Claude Code" → copy command → paste into [[wiki/entities/claude-code|Claude Code]], which builds the design into a real app (database, accounts, payments, working forms). Framed as "Claude Design makes it. Claude Code builds it."
- **What Claude Design is**: lives inside an existing Claude subscription at claude.ai/design; requires at least a **Pro plan**. Produces animated websites/landing pages, slide decks, LinkedIn carousels/infographics, sales proposals/one-pagers, onboarding guides/PDFs, and product UI/app designs. Four entry modes: Prototype (Wireframe or High Fidelity), Slide deck, From template, Other.
- **Token warning**: Claude Design has its own **separate weekly usage limit** (not the same pool as regular Claude usage); a single high-fidelity design can consume a significant chunk of the weekly allowance. Pre-establishing system/templates/copy is framed as budget protection, not just hygiene.
- **It is still a research preview** — expect bugs, text overlap, and weird rendering on some layouts.
- **The 20% caveat**: Claude gets ~80% of the way fast; the final 20% (taste, judgment, brand understanding) is "what separates a good design from a great one" — "your taste is the product."
- **Agency claim**: at IgnytLabs, concepts that "used to take two weeks" are "now ready in a day"; the team has templates for every deliverable (landing pages, case studies, client proposals, onboarding guides) and builds a design system for every client before touching a page.
- **Attribution**: the 4-step structure is credited to a Claude Design YouTube video by **Ben AI**.

## Notable quotes

> "Pre-establish as much as possible before you ever open Claude Design. The more you define upfront, the less Claude has to guess."

> "You are not starting from scratch. You are finishing something that is already 70% done before Claude Design generates a single pixel."

> "Claude Design makes it. Claude Code builds it."

> "Claude Design is not the workflow. The workflow is what makes Claude Design work. Set it up once. Use it forever."

> "The bottleneck in design has never been creativity. It has always been production."

## Notes

- This is the **first primary source in the wiki about using Claude Design directly** (as opposed to inferring it through [[wiki/sources/nexu-io-open-design|Open Design]], its open-source clone). It documents concrete UI surfaces — Design Systems tab, Examples tab, From Template, Share → Duplicate as Template, the Direct edit / Comments / Draw / Tweaks toolset, and the Claude Code handoff — that the existing [[wiki/entities/claude-design|Claude Design]] entity page lacks because no primary source had been ingested. Strong candidate to expand that stub-ish entity.
- The thesis is structurally identical to the wiki's **"front-load the decisions" pattern** seen across the agent-CLI sources: reduce what the model must infer at runtime by pre-committing structure (templates ≈ scaffolding), brand (design system ≈ a [[wiki/concepts/context-file|context file]]), and content (skill-written copy ≈ Directive). The "design system + template + copy skill" trio maps cleanly onto the Directive/Orchestration/Execution decomposition the wiki uses elsewhere — the design system and template are persistent directives; the copy skill is a reusable orchestration step; Claude Design is execution.
- The **token-budget framing is notable**: Claude Design's separate weekly pool makes iteration-avoidance an explicit economic discipline, echoing the cost-discipline aesthetic the wiki tracks in Claude Code usage (small prompts, pre-scoped context). The mechanism differs but the lesson — every avoidable round-trip is paid for — is the same.
- The **copy-skill step is the cross-tool bridge**: it uses Claude Code / Claude Desktop *skills* to feed Claude Design, treating the design tool as pure execution and the skill as the writing brain. This is a concrete instance of skills composing across Anthropic surfaces.
- Marketing voice throughout ("CRACKED", "LFG", "2026 is going to be UNFAIR for builders") — the workflow substance is sound but the framing is promotional, written by an agency operator demonstrating a method he sells the output of. Treat the time-savings claims ("two weeks → one day") as agency self-report, not measured.
- Uncertainty: the exact mechanics of Claude Design's Design Systems / template features may evolve (the author flags it as a research preview), so specific UI labels here are point-in-time as of May 2026.

## Mentioned entities

- [[wiki/entities/claude-design]] — the subject tool; this source documents its UI surfaces and modes in primary detail.
- [[wiki/entities/claude-code]] — destination of the design handoff (builds the design into a real app) and host (with Claude Desktop) of the copy skill.
- [[wiki/entities/prajwal-tomar]] — author; agency operator at IgnytLabs.
- [[wiki/entities/ignytlabs]] — author's AI-products agency where the workflow is used in client work.
- [[wiki/entities/ben-ai]] — YouTube creator credited with the original 4-step Claude Design video.
- [[wiki/entities/anthropic]] — maker of Claude Design / Claude Code / the Claude subscription the tool lives in.
- [[wiki/entities/dribbble]] — named source of layout inspiration for building templates.
- [[wiki/entities/framer]] — named source of layout inspiration for building templates.
- [[wiki/entities/behance]] — named source of layout inspiration for building templates.

## Related concepts

- [[wiki/concepts/claude-code-skills]] — the copy-pre-definition step (Step 3) is a Claude Code / Desktop skill feeding Claude Design.
- [[wiki/concepts/artifact-first-workflow]] — Claude Design's underlying emission model that this workflow drives.
- [[wiki/concepts/context-file]] — the design system functions as a persistent brand context the tool reads before generating.
- [[wiki/concepts/design-system]] — the reusable brand blueprint at the center of Step 1 (concept page to be created).
- [[wiki/concepts/vibe-designing]] — the named anti-pattern this workflow exists to defeat (concept page to be created).

## Related sources

- [[wiki/sources/nexu-io-open-design]] — Open Design is the open-source clone of Claude Design; this is the complementary "how to actually use the proprietary original" source.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — companion Claude Design walkthrough (brand-driven build) in the wiki.
- [[wiki/sources/refero-open-design-claude-design-comparison]] — strategic comparison that includes Claude Design as the proprietary Anthropic surface.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — same "trigger + prompt + output" / front-loaded-Directive philosophy applied to Claude Code agents instead of design.
