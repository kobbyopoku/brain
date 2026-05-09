---
type: source
title: Shann Holmberg — Content OS for AI-augmented content production (5M impressions in 2 weeks)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/shannholmberg/status/2052780393326092407
source_type: x-thread
author: Shann Holmberg
source_date: 2026-03-24
raw_path: raw/How to build your content system with AI (and get to 5M impressions).md
content_status: substantive-verbatim
tags: [content-os, ai-content, voice-profile, anti-ai-slop-machinery, run-folder-pattern, hermes-agent, postiz]
---

# Shann Holmberg — Content OS for AI-augmented content production (5M impressions in 2 weeks)

> Shann Holmberg's *Content OS* — the most architecturally detailed content-production framework yet ingested. **5M impressions in 2 weeks; 11M impressions and 100K bookmarks in 2 months** from a near-silent X account. Co-founder of [[wiki/entities/lunar-strategy|Lunar Strategy]] (deploys the OS for clients). Distinguishes from the previous wave (4-agent generic systems) by leaning **fewer agents + more workflows + sharper voice profile**. Optimizes for *bookmarkable content*, scored on a 12-point rubric. Ships **4 verbatim production-grade prompts**. Recommends [[wiki/entities/hermes-agent|Hermes Agent]] or self-hosted Claude Code on VPS for execution; [[wiki/entities/postiz|Postiz]] for publish layer.

## TL;DR

Six-folder Content OS:

```
/content-os
  /strategy        # positioning, audience, pillars, source-watchlist
  /voice           # voice-profile.md + master-avoid-slop.md
  /stores          # inbox, workboard, ideas, hooks, proof, feedback
  /runs            # active/ + archive/ (one folder per content object)
  /modules         # /writer (SKILL.md + references + templates)
  /workflows       # idea-to-published, verifier checklist, scheduler-handoff, feedback-loop
```

Four routes for any content object (decided at *idea gate*):

1. **ORIGINAL** — drawn from second brain (personal OS, notes, voice memos). High taste investment.
2. **REPURPOSE** — extend owned content (thread spinoff, self-QRT). Spine yours, format changes.
3. **REWRITE** — translate external source through your POV.
4. **RESEARCH + IDEATE** — pre-drafting exploration; output is sharpened idea, not post.

Lifecycle of one content object:

```
captured → idea_review (route) → brief_ready → drafting → verification
       → shann_draft_review → approved → scheduler_ready → scheduled
       → published → feedback_24h → feedback_72h → learned
```

## Key takeaways

### "Bookmarkable" as the unit of content quality

> *"The unit of work is not 'another post.' It is something a reader wants to keep. A bookmark is a small promise the reader makes to their future self. It says 'I will need this again.' That is a much higher bar than a like."*

This reframes content-quality measurement from *engagement* to *future utility*. Pairs with the [[hot-cache]] / [[llm-wiki-pattern]] cluster — both treat *future retrievability* as the load-bearing property.

The 12-point rubric (8 = personal bar):

1. Saves the reader a future task
2. Includes proof (numbers, screenshot, named example)
3. Gives a reusable takeaway (template, checklist, frame)
4. Has a specific audience and job-to-be-done
5. Can be applied without me being in the room
6. Has a strong screenshot or visual

(0/1/2 each = 12 max.) **Below 8 → back to the packet.** *"Most 'bad' drafts are good drafts that skipped a row."*

### Voice profile from 20 best pieces (Saraev / CyrilXBT echo)

> *"Before you write the system prompt, collect your 20 best performing pieces of content. Feed all of them to Claude and ask it to extract the patterns: average sentence length, capitalization habits, vocabulary level, structural tendencies, what you never say. Use that extracted profile as the voice section of your system prompt."*

**Identical methodology to [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's]] Content Agent voice profile.** Two independent practitioners now describe *"feed the model your 20 best pieces, extract patterns, install as system prompt"* as the canonical voice-extraction method. Worth promoting to a sub-pattern in [[markdown-as-agent-contract]] / [[anti-ai-slop-machinery]]. Call it **voice-profile-extraction**.

### The master avoid-slop document (54 patterns, 3 severity tiers)

Shann ships an 8-pattern starter version (the full 54-pattern doc is "still working on it"):

```
- promotional language ("groundbreaking", "game-changing")
- significance inflation ("pivotal moment", "testament to")
- vague attribution ("experts believe", "studies show")
- false agency ("the system compounds", "the data tells us")
- rhetorical setups ("the question is whether you X")
- staccato fragmentation ("no X. no Y. no Z.")
- em dash overuse (zero is the target)
- filler adverbs ("actually", "literally", "quietly")
```

**Direct sibling of [[anti-ai-slop-machinery]]** (Open Design's pre-emit blacklist). Both are *negative-pattern* discipline catalogs. Worth cross-cite in the concept page; Shann adds the *severity tier* dimension (3 tiers) which Open Design's blacklist doesn't have explicitly.

### The writer context packet (as an instance of [[markdown-as-agent-contract]])

Per content object, before drafting:

```
writer context packet
─────────────────────
thesis:        one sentence the post must prove
reader:        the specific person who should save it
proof:         numbers, screenshots, stories I am allowed to use
angle:         the unexpected framing
constraints:   format, length, tone, banned phrases
voice anchors: 2-3 lines that sound like me
risks:         what would make this read as slop or as cringe
open loops:    what I do not yet know, that the writer should flag
```

400-900 tokens. *"A tight packet beats a giant context window almost every time."* Direct application of [[wiki/concepts/claude-code-overhead-patterns|context discipline]] from Mnilax: smaller-context-better-output.

### The viral postmortem prompt (highest-leverage prompt in the system)

> *"You are reading a post that already crossed 1M views and 10K bookmarks one week from now. You are not writing it. You are explaining, after the fact, why it landed."*

Forces the model to **point at exact lines** for: hook move / credibility / screenshottable / save-worthy / share-trigger / weakest part. *"The whole point is the model cannot hide behind generic praise. Force it to point at mechanics."* This is the strongest articulation in the wiki of *evaluator-mode prompting* — the model adopts a critical reader perspective rather than generative-author perspective.

Pairs cleanly with [[wiki/concepts/anti-ai-slop-machinery]]'s *5-dimensional self-critique* — both force the model into a critic role with concrete lines to point at, instead of vague approval.

### Two models, two roles (architectural pattern)

> *"The job of writing and the job of running the system are different jobs, and they reward different models."*

| Model | Role | What it handles |
|---|---|---|
| **opus 4.7** | writer | taste, rhythm, compression, voice, the actual draft |
| **gpt-5.5** | orchestrator | routing, context packaging, verifier, publish handoff |

Aligns with [[wiki/concepts/reasoning-execution-split]] but extends it: not just *reasoning vs execution*, but *taste vs orchestration*. The taste layer rewards a stronger generation model; the orchestration layer rewards reliability + tool-use. Worth promoting to a sub-pattern in [[reasoning-execution-split]] (or [[multi-agent-orchestration]]).

### The 4-agent → 3-step + feedback simplification

> *"Before the current Content OS, I built a 4-agent system that ran a version of this same loop: researcher, idea maker, writer, and an orchestrator routing between them… It worked. But it was overbuilt. Four agents for what is, structurally, three production steps and a feedback loop. The agent count was not the lever. The knowledge layer feeding the writer was."*

Important counter to the *"specialize more agents"* canon (CyrilXBT, regent0x_). **Specialization works at coarse granularity (5 distinct roles) but breaks at fine granularity (4 micro-agents for one workflow).** Worth flagging in [[multi-agent-orchestration]] / [[subagents]]: there's a Goldilocks zone for agent count, and adding agents past it produces overhead without quality gains.

### Hermes Agent endorsement (and Postiz publish layer)

> *"Hermes agent, which is what I run. Its built for this shape of work: agents, skills, tool access, file and git operations, browser and search, scheduled jobs, and context that persists across the whole workflow."*

Strong external validation of [[wiki/entities/hermes-agent]] for non-trivial content workflow. Pairs with the existing wiki coverage. Postiz (open-source social scheduler at `gitroomhq/postiz-app`) is named as the publish layer — *"X, LinkedIn, Instagram, Threads, TikTok, YouTube, Bluesky, Reddit, and more."*

## Notable quotes

> "Never publish unedited, hand-finish every draft. The system is an accelerator, not autopilot. Used as automation, it decays."

> "Most people stop at publish. That is where the system starts earning."

> "If you cannot fill the packet, you do not have a post yet. You have a vibe."

> "The brain is the system."

> "Bookmark rate is the one I watch most. It tells me which posts earned the save, not just the scroll."

> "Generic AI content sounds like AI. A properly configured voice profile produces content that sounds like you."

## How this composes with the wiki

- [[markdown-as-agent-contract]] — the writer-context-packet, the voice-profile, the master-avoid-slop, the SKILL.md for `/writer` are all instances of the meta-pattern at *workspace + task* scope. Most-explicit-folder-as-contract treatment so far.
- [[anti-ai-slop-machinery]] — Shann's master-avoid-slop document is the strongest non-Open-Design sibling. Worth cross-cite. Adds the 3-severity-tier dimension.
- [[hot-cache]] — Shann's `/stores/winners`, `/stores/feedback`, weekly review loop is conceptually the hot-cache for content production: most-recently-active state surfaces first.
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — same voice-profile-from-20-best-pieces methodology. Two-source corroboration.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — same templates-as-agent-contract pattern at the production-block scope.
- [[reasoning-execution-split]] — Shann's writer-vs-orchestrator extension is a sub-pattern (taste-vs-orchestration).
- [[multi-agent-orchestration]] — *"agent count was not the lever. The knowledge layer feeding the writer was."* Counter to the specialize-more-agents canon.
- [[wiki/entities/hermes-agent]] — strong external validation for non-trivial content workflow.

## Mentioned entities

- [[wiki/entities/shannholmberg]] — *(new)* author.
- [[wiki/entities/lunar-strategy]] — *(stub candidate)* Shann's agency.
- [[wiki/entities/postiz]] — *(stub candidate)* open-source social scheduler.
- [[wiki/entities/bookmarkable-io]] — *(stub candidate)* Shann's upcoming blueprint product.
- [[wiki/entities/hermes-agent]] — endorsed runtime.
- [[wiki/entities/claude-code]] — alternate runtime (VPS deployment).
- [[wiki/entities/anthropic]] — Claude / Opus 4.7.
- [[wiki/entities/openai]] — *(stub candidate)* GPT-5.5 as orchestrator.

## Related concepts

- [[markdown-as-agent-contract]] — most-detailed folder-as-contract instance.
- [[anti-ai-slop-machinery]] — sibling avoid-slop catalog with severity tiers.
- [[claude-code-skills]] — `/modules/writer/SKILL.md` is the canonical skill structure.
- [[reasoning-execution-split]] — extended to *taste vs orchestration*.
- [[multi-agent-orchestration]] — Goldilocks agent count.
- [[hot-cache]] — `/stores/` as recent-active-state hot cache.
- [[scheduled-automation]] — weekly feedback loop.
- [[self-annealing]] — winners → inputs feed; losers → updated banned-patterns.
