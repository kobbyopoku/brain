---
type: source
title: nateherk — Claude Design Built My Brand End to End (without hitting limits)
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/nateherk/status/2049671370099826725
source_type: x-thread
author: nateherk (@nateherk)
source_date: 2026-04-30
raw_path: raw/Claude Design Built My Brand End to End (without hitting limits).md
content_status: substantive-verbatim
tags: [claude-design, opus-4-7, design-system, artifact-first-workflow, brand-pipeline, vercel, quota-management, verifier-agent]
---

# nateherk — Claude Design Built My Brand End to End (without hitting limits)

> nateherk builds a full fictional brand ("Tally") end-to-end with Anthropic's [[wiki/entities/claude-design|Claude Design]] — pitch deck, landing page, mobile prototype, brand guidelines, animated launch video, deployed live to [[wiki/entities/vercel|Vercel]] — then reverse-engineers a quota-stretching playbook after burning $500 in top-up usage on a [[wiki/entities/max-20x|Max 20x]] plan.

## TL;DR

A practical operator's walkthrough of Claude Design (Anthropic's vision-first design surface released April 17, 2026, running on [[wiki/entities/opus-4-7|Opus 4.7]]). nateherk demonstrates a repeatable **brand-to-build pipeline**: brainstorm the brand in regular Claude chat, lock a reusable **design system** (a generated `Design.md` spec), then execute six asset types (deck, wireframes, high-fidelity landing page, brand-guidelines doc, mobile prototype, launch video) that all pull from the same system, and ship the final build via [[wiki/entities/claude-code|Claude Code]] + Vercel. The second half is a token-economy playbook for not blowing the separate weekly Design quota: plan in chat, edit in-canvas instead of prompting, use Sonnet for tweaks, one change per prompt, export to Claude Code when the quota runs out.

## Key takeaways

- **Claude Design is a vision-first sibling to Claude Code.** Released April 17, 2026 (day after Opus 4.7), it runs on Opus 4.7 (strongest vision in the lineup) and builds visual artifacts — prototypes (wireframe or high-fidelity), slide decks, landing pages, animated promos, mobile mockups, short brand videos — from natural language.
- **The self-validating verifier loop is the killer feature.** After every render, Claude Design screenshots its own output, inspects the page, finds anything broken, and fixes it before the user sees the issue. nateherk reports it auto-caught and fixed issues on pitch-deck slides 6 and 10.
- **Mike Krieger pedigree is cited as the reason it "landed so polished."** Krieger left Figma's board right before the Claude Design announcement and joined Anthropic as CPO. *(Source's framing; see Notes on uncertainty.)*
- **Design is paid-only with a separate weekly quota.** Pro, Max 5x, and Max 20x get different weekly quotas, distinct from regular Claude and Claude Code usage. nateherk (Max 20x, $200/mo) burned 30% of his weekly quota on just a design system + pitch deck, and $500 in top-ups overall.
- **Start every project with a design system.** It holds colors, typography hierarchy, spacing, button styles, hover states, badges, tags, cards, input fields, and icon set, and generates a `Design.md` spec that becomes the source of truth for all later assets. On a team plan the system shares across the whole org.
- **Two ways to seed a design system:** (1) give it an existing website URL + GitHub repo (it scrapes both for brand DNA — but full GitHub repos eat far more tokens); or (2) for a brand with no site yet, give it a logo PNG + a markdown brand-concept doc + a short note on "button feel." Generation takes 5-10 minutes.
- **Brainstorm in chat, execute in Design — the single biggest lever for stretching a session.** The Design surface is for executing a known brief, not figuring out what the brief should be. For Tally, nateherk arrived with a 372-line markdown spec built entirely in regular Claude.
- **Wireframe-first is a myth for projects where you already know the layout.** nateherk burned 4% of his weekly quota on Tally landing-page wireframes, then scrapped them and went straight to high fidelity.
- **The editing surface (not the chat panel) is the quiet superpower.** Three in-canvas surfaces: the **edit tool** (click any element, change it directly — cheapest edit), the **draw tool** (circle a region + comment; Claude screenshots and acts on it), and the **tweaks panel** (pre-built variations for cover style, texture, accent colors, slide chrome). Rule: "if you can change it without prompting, change it without prompting."
- **The brand-to-build pipeline ran the same playbook six times:** investor pitch deck → landing-page wireframes (skippable in retrospect) → high-fidelity landing page → brand-guidelines doc → mobile app prototype → launch video. Every output landed in the same visual world because all pulled from one design system.
- **Cross-tool stack:** [[wiki/entities/gpt-image-2|GPT Image 2]] mocked logo variations + a one-page brand-guidelines visual (struggles with specific fonts — Roboto Mono and Montserrat got bent — fixed by dropping official fonts in via [[wiki/entities/canva|Canva]]); [[wiki/entities/kling|Kling]] generated a logo-loop video dropped into the landing-page hero; the [[wiki/entities/hyperframes|HyperFrames]] skill (built by a creator named [[wiki/entities/haegeon|Haegeon]]) injects animation primitives into Design to produce the launch video from a single prompt.
- **Shipping path: hand off to Claude Code, deploy to Vercel.** Two handoff options — Share → Download as zip, or "Hand off to Claude Code" (which generates a copy-paste command; had a 404 the day of recording). From Claude Code: push to a private GitHub repo, test on localhost, connect Vercel (~60s to a live domain).
- **Mobile is not auto-optimized.** Claude Design optimizes for desktop by default; neither Design nor Claude Code auto-optimize for mobile — but they'll do it on request. Test mobile (F12 in Chrome) before deploying.
- **Quota-stretching playbook:** plan/outline in regular Claude (separate limit); drop a tight markdown spec before generating; use Opus 4.7 for planning prompts, switch to [[wiki/entities/sonnet-4-6|Sonnet 4.6]] for tweaks (no quality drop with a tight spec); edit in-canvas; reference real designs by name ("Linear 2023 with higher density" beats "make it clean"); state negatives; one major change per prompt; watch the build live and stop it if it goes wrong.
- **Quirks:** file uploads cap ~30-40MB; long threads pollute context (export + reopen with a fresh session rather than trusting `/clear`); design systems with full GitHub repos cost far more tokens than logo + markdown.
- **Thesis: Claude Design isn't replacing Figma — it's replacing the gap between an idea and a shipped brand.** Three surfaces, one workflow: plan in chat, execute in Design, ship from Code, with one design system gluing them together.

## Notable quotes

> "It runs on Opus 4.7, which has the strongest vision in the lineup. After every render, Claude Design screenshots the output, looks at the page, finds anything broken, and fixes it before you even see the issue. That self-validating loop is the killer feature."

> "Don't brainstorm inside Claude Design. Ever. The Design surface is for executing a known brief, not for figuring out what the brief should be."

> "If you can change it without prompting, change it without prompting."

> "Claude Design isn't replacing Figma. It's replacing the gap between an idea and a shipped brand. Plan in chat. Execute in Design. Ship from Code."

> "The people getting real value out of this aren't the ones treating it like a chat box. They're the ones treating it like a specialist with its own context, its own quota, and its own role in a larger pipeline."

## Notes

- This is the **second nateherk source in the wiki**. The first ([[wiki/sources/nateherk-claude-code-os-3m-business|the AI OS / $3M business playbook]]) introduced [[wiki/concepts/hot-cache|hot-cache]] and was a wild citation of Karpathy's LLM Wiki. This piece is a different register — a hands-on Claude Design tutorial — but shares nateherk's signature operator framing of *"treat AI like a specialist; each chat gets one job."* That is the same separation-of-concerns instinct as [[wiki/concepts/reasoning-execution-split|reasoning-execution-split]] applied at the **session** level rather than the tool level.
- **The verifier loop is the load-bearing architectural claim** and is the strongest first-party-product evidence yet in the wiki for [[wiki/concepts/artifact-first-workflow|artifact-first-workflow]] coupled with an evaluator-optimizer pattern (screenshot → critique → fix). It is the proprietary Anthropic analogue to the self-critique mechanisms catalogued in [[wiki/concepts/anti-ai-slop-machinery|anti-ai-slop-machinery]] (from the open-source [[wiki/entities/open-design|Open Design]]).
- The **design-system-as-source-of-truth** move is the same pattern as [[wiki/concepts/design-md|DESIGN.md]] — Claude Design generates a `Design.md` spec, then reuses it across every asset. This is a first-party Anthropic instance of the DESIGN.md-for-AI-agents convention the wiki already tracks via Refero and Open Design.
- **Uncertainty flags (cite-or-omit):** several claims are nateherk's reportage, not verified facts — (1) the Mike Krieger "left Figma's board / joined Anthropic as CPO" claim; (2) the April 17, 2026 release date and "day after Opus 4.7" timing; (3) specific quota-burn percentages (30%, 4%, 8%) are his anecdotes. The $500 top-up figure and Max 20x $200/mo price are his stated experience. Recorded as the source's claims, not wiki-confirmed.
- **Relevance to Godwin:** directly actionable for the marketing surfaces in the portfolio ([[wiki/projects/roamlabs|_roamlabs]], [[wiki/projects/asanti-brokers|Asanti Brokers]], product landing pages for Vedge/Kivora/Clarvyn). The "lock one design system, generate every asset on-brand" pipeline is the exact shape a multi-brand operator wants. The brainstorm-in-chat / execute-in-Design / ship-from-Code discipline also maps onto [[wiki/projects/helm|Helm]]'s Marketing agent role.
- "Tally" is a **demo brand fabricated for the walkthrough** (a fictional weekly-digest product), not a real company — recorded here as a worked example, not an entity worth a profile.

## Mentioned entities

- [[wiki/entities/nateherk]] — author; operator who built the full brand and reverse-engineered the quota playbook.
- [[wiki/entities/claude-design]] — the product the entire source is about (Anthropic's vision-first design surface).
- [[wiki/entities/anthropic]] — maker of Claude Design, Opus 4.7, Claude Code.
- [[wiki/entities/opus-4-7]] — the model Claude Design runs on; "strongest vision in the lineup."
- [[wiki/entities/sonnet-4-6]] — cheaper model for in-canvas tweaks (no quality drop with a tight spec).
- [[wiki/entities/claude-code]] — the hand-off surface for shipping the final build.
- [[wiki/entities/vercel]] — deployment target (~60s to a live domain).
- [[wiki/entities/github]] — private repo the project is pushed to before Vercel.
- [[wiki/entities/mike-krieger]] — Figma board → Anthropic CPO; cited as the product-pedigree explanation.
- [[wiki/entities/figma]] — the incumbent Claude Design is positioned against ("not replacing Figma").
- [[wiki/entities/gpt-image-2]] — logo / brand-guidelines mock-up partner (struggles with specific fonts).
- [[wiki/entities/kling]] — generated the logo-loop hero video.
- [[wiki/entities/hyperframes]] — Design skill injecting animation primitives; produced the launch video.
- [[wiki/entities/haegeon]] — creator of the HyperFrames skill.
- [[wiki/entities/canva]] — used to drop official fonts back into GPT Image 2's bent-font layouts.
- [[wiki/entities/max-20x]] — the $200/mo plan nateherk runs; carries the weekly Design quota.

## Related concepts

- [[wiki/concepts/artifact-first-workflow]] — Claude Design is the canonical home of this pattern; the verifier loop (screenshot → critique → fix) is the evaluator-optimizer extension.
- [[wiki/concepts/design-md]] — Claude Design generates a `Design.md` spec as the reusable source of truth.
- [[wiki/concepts/reasoning-execution-split]] — "each chat gets one job" is the session-level version of reason-vs-execute separation.
- [[wiki/concepts/claude-code-overhead-patterns]] — the quota-stretching playbook is a token-economy discipline analogous to the measured overhead patterns.
- [[wiki/concepts/hot-cache]] — the "tight markdown spec before you generate" move is sibling to nateherk's own `_hot.md` discipline from his prior source.

## Related sources

- [[wiki/sources/nateherk-claude-code-os-3m-business]] — same author's AI OS / $3M business playbook (introduced hot-cache).
- [[wiki/sources/nexu-io-open-design]] — Apache-2.0 open-source alternative to Claude Design; its anti-slop machinery is the OSS counterpart to Design's verifier loop.
- [[wiki/sources/open-design-catalog]] — full DESIGN.md catalog; companion to Claude Design's generated `Design.md`.
- [[wiki/syntheses/refero-open-design-claude-design-comparison]] — three strategic bets in AI design tooling; this source is primary evidence for the Claude Design column.
- [[wiki/sources/trq212-x-html-effectiveness]] — Anthropic's HTML-as-output thesis underpinning the artifact-first surface.
