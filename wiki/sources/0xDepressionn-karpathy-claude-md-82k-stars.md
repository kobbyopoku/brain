---
type: source
title: 0xDepressionn — Karpathy's CLAUDE.md hit #1 on GitHub with 82,000 stars
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/0xDepressionn/status/2055999112470839383
source_type: x-thread
author: 0xDepressionn (@0xDepressionn)
source_date: 2026-05-17
raw_path: raw/Karpathy's CLAUDE.md hit 1 on GitHub with 82,000 stars. Most devs still haven't read it..md
content_status: substantive-verbatim
tags: [claude-md, markdown-as-agent-contract, prompt-engineering, claude-code, paste-ready-prompts, cost-math]
---

# 0xDepressionn — Karpathy's CLAUDE.md hit #1 on GitHub with 82,000 stars

> A second, **economics-led** articulation of the viral CLAUDE.md ruleset: same 21 paste-ready instructions and same [[wiki/entities/andrej-karpathy|Karpathy]] 4-rules / 65→94% accuracy claim as the [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions|TheAIWorld22 sibling]], but organized into **3 cost-categories** (DEFAULTS / BEHAVIOR / MEMORY+STACK) each carrying an explicit dollar-waste figure. Headline: an unconfigured Claude Code costs **$975/week per developer** ($253,500/year for a team of 5); the fix is *"one plain text file, 21 rules, two hours of work."* Strongest [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] ROI-argument in the wiki.

## TL;DR

0xDepressionn frames CLAUDE.md as a fix for three categories of recurring, quantified waste: re-explaining context every session ($375/week), reverting unauthorized scope changes ($225/week), and recovering from forgotten decisions + wrong-stack suggestions ($375/week). The post supplies 21 paste-ready prompt fragments across these three sections, closes with Karpathy's distilled 4 rules, and prescribes a staged rollout: start with **only** Karpathy's 4 rules, then add one section per week. The substance overlaps almost entirely with the [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions|TheAIWorld22 thread]]; the *distinct contribution is the cost-math framing*.

## The 3-category framing (each with a price tag)

| Section | Failure it fixes | Stated waste / dev | Setup time |
|---|---|---|---|
| **1/3 DEFAULTS** | Re-explaining stack / standards / context every session (30 min/day @ $150/hr) | $375/week | 45 min |
| **2/3 BEHAVIOR** | Unauthorized refactors, deletes, scope-creep you must review + revert | $225/week | 30 min |
| **3/3 MEMORY + STACK** | Forgotten decisions + Claude re-suggesting already-ruled-out tools | $375/week | 20 min |
| **Total** | — | **$975/week per dev** | **~2 hours** |

> Team of 5: **$4,875/week**, **$253,500/year**.

The price tags are the load-bearing rhetorical device — the underlying rules are the same family of CLAUDE.md fragments already catalogued under [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]].

## The 21 rules (by section)

**1/3 DEFAULTS (7 rules)** — kill filler phrases; match response length to task complexity; show 2-3 approaches before acting; admit uncertainty before stating any fact/stat/date; an *about-me* block (name / role / background / strong-in / still-learning); a *current-project* block (project / goal / audience / stack constraints / what to avoid); a *voice-lock* block (style / sentence length / words I use / words I never use / format). Plus a meta-tip: don't write CLAUDE.md from scratch — have Claude draft it from what you've told it (under 500 words), then edit.

**2/3 BEHAVIOR (7 rules)** — stay in scope (touch only task-related code; note other fixes, never apply them); ask before significantly altering existing content; confirm before anything destructive (*"'You mentioned this earlier' is not confirmation"*); hard stops for production (deploys / migrations / external API calls / irreversible side effects require in-session yes); always end with a Files-changed / What-was-modified / Not-touched / Follow-up summary; never send/post/publish on the user's behalf without explicit confirmation; think step-by-step before writing code for architecture / debugging / non-trivial features.

**3/3 MEMORY + STACK (7 rules)** — maintain **MEMORY.md** (log every significant decision: what / why / what-was-rejected; read at session start; never contradict a logged decision without flagging); session-end summary written to MEMORY.md; maintain **ERRORS.md** (log any approach that took >2 attempts; check before suggesting similar approaches); a permanent-facts list applied every session; **lock the tech stack** (language / framework / package manager / database / testing / styling — never suggest alternatives unless asked); use **Extended Thinking** mode for architecture / performance / DB-design / long-term decisions; and **Karpathy's 4 rules**.

## Karpathy's 4 rules (the viral core)

> 1. **Ask, don't assume.** If something is unclear, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.
> 2. **Simplest solution first.** Always implement the simplest thing that could work. Do not add abstractions or flexibility that weren't explicitly requested.
> 3. **Don't touch unrelated code.** If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.
> 4. **Flag uncertainty explicitly.** If you are not confident about an approach or technical detail, say so before proceeding. Confidence without certainty causes more damage than admitting a gap.

The framing attributes the original 4 behaviors to [[wiki/entities/andrej-karpathy|Karpathy]] (*"Former Director of AI at Tesla. Founding member of OpenAI"*), with an unnamed developer expanding + publishing the file that reportedly hit #1 on GitHub Trending (82,000 stars / 7,800 forks) and took coding accuracy from **65% to 94%**.

## Notable quotes

> "It started with Andrej Karpathy. Former Director of AI at Tesla. Founding member of OpenAI. He identified 4 behaviors that make Claude Code fail and wrote them down in a single file."

> "Every time you open Claude Code, it starts with nothing. It doesn't know your stack. Your standards. Your project context. What you've already tried. What you explicitly decided not to do three sessions ago. So it guesses. And when it guesses, it refactors code you didn't ask it to touch."

> "Confirm before anything destructive ... 'You mentioned this earlier' is not confirmation. I must say yes in the current message."

> "The developers who set this up are working with a version of Claude that remembers decisions, stays in scope, confirms before destroying anything ... The ones who haven't are spending $975/week to repeat themselves."

> "start with Karpathy's 4 rules. just those 4. paste them into a new file called CLAUDE.md in your project root right now. it takes 2 minutes. add the rest one week at a time as you notice what's missing."

## Notes

- **This is effectively a near-duplicate of [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]].** Both posts ship the same ~21 CLAUDE.md fragments (kill-filler / show-options / admit-uncertainty / stay-in-scope / MEMORY.md / ERRORS.md / lock-stack), both close with Karpathy's 4 rules, both cite the 65→94% accuracy figure and the #1-on-GitHub-Trending claim. The two are almost certainly drawing on the same viral underlying file. They should be treated as a *cluster*, not independent corroboration.
- **The genuinely distinct contribution is the cost-math.** TheAIWorld22 framed the value qualitatively (*"costing people hours every single week"*); 0xDepressionn puts numbers on it: 30 min/day @ $150/hr → $375/week DEFAULTS, plus $225/week BEHAVIOR, plus $375/week MEMORY+STACK = $975/week/dev, $253,500/year for a team of 5. These figures are **illustrative, not measured** — they assume a flat $150/hr rate and self-reported time estimates, with no instrumentation. Contrast with [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 430-hours study]], which *instrumented* token waste rather than estimating dollar-hours.
- **Two items here that TheAIWorld22 did not foreground**: (1) an explicit **Extended Thinking** instruction (use extended-thinking mode for architecture / performance / DB-design / long-term decisions) and (2) the **staged-rollout prescription** (start with Karpathy's 4 rules only; add one section per week). The rollout advice is a small but useful adoption heuristic.
- **Provenance caveat — uncertain (flag).** The "Karpathy wrote 4 behaviors in a single file → a developer expanded it → 82k stars" origin story is asserted in both this post and TheAIWorld22 without a link to the actual repo. The wiki holds Karpathy's [[wiki/concepts/llm-wiki-pattern|LLM Wiki pattern]] as a primary source but has **no primary source for a Karpathy-authored coding-CLAUDE.md ruleset**. The 82,000-stars / 7,800-forks / 65→94% figures are likewise uncited. Treat all of these as claims-of-the-source, not wiki-verified facts.
- The MEMORY.md + ERRORS.md instructions (section 3) are the same external-markdown-persistent-state family as [[wiki/concepts/hot-cache|nateherk's `_hot.md`]] and the wiki's own `MEMORY.md` auto-memory convention — a passive markdown alternative to [[wiki/sources/nousresearch-hermes-agent|Hermes Agent]]'s agent-internal self-update loop.

## Mentioned entities

- [[wiki/entities/0xdepressionn]] — author of this thread (X creator).
- [[wiki/entities/andrej-karpathy]] — credited originator of the 4 rules; *"Former Director of AI at Tesla, founding member of OpenAI."*
- [[wiki/entities/claude-code]] — the platform the CLAUDE.md file configures.
- [[wiki/entities/anthropic]] — maker of Claude / Claude Code.

## Related concepts

- [[markdown-as-agent-contract]] — 21 paste-ready instances of the meta-pattern; this source adds the ROI/cost-math argument for it.
- [[hot-cache]] — MEMORY.md / ERRORS.md / permanent-facts are external-markdown persistent state, sibling to `_hot.md`.
- [[llm-wiki-pattern]] — Karpathy's other (separately-sourced) persistent-markdown contribution; conceptually adjacent.
- [[cognitive-debt]] — the admit-uncertainty rule (DEFAULTS) is the anti-hallucination protocol.
- [[claude-code-skills]] — adjacent CLAUDE.md / `.claude/` configuration surface.

## Related sources

- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — **near-duplicate sibling**; same 21 rules + Karpathy 4-rules + 65→94% claim, framed qualitatively rather than via cost-math.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's LLM Wiki pattern; the one Karpathy contribution the wiki holds as a primary source.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — the *instrumented* counterpart: measures token waste rather than estimating dollar-hours.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — `_hot.md` external-markdown-state ancestor of the MEMORY.md/ERRORS.md instructions.
