---
type: source
title: TheAIWorld22 — CLAUDE.md fixes everything (21 instructions across 5 parts)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/TheAIWorld22/status/2053023798170198453
source_type: x-thread
author: TheAIWorld22
source_date: 2026-05-09
raw_path: raw/You've been using Claude wrong this whole time. CLAUDE.md fixes everything. Here's how..md
content_status: substantive
tags: [claude-md, markdown-as-agent-contract, prompt-engineering, claude-code, paste-ready-prompts]
---

# TheAIWorld22 — CLAUDE.md fixes everything (21 instructions across 5 parts)

> The most comprehensive **paste-ready CLAUDE.md prompt-fragment library** ingested into the wiki. 21 numbered instructions organized into 5 parts (how Claude talks / how Claude behaves / your context / memory and continuity / for developers). Closes with **Andrej Karpathy's CLAUDE.md viral 4 rules** — reportedly took coding accuracy from **65% to 94%**. Direct extension of [[markdown-as-agent-contract]] applied to non-developer audiences (writers / marketers / researchers / business owners). Reframes CLAUDE.md from *"developer config"* to *"permanent instruction file anyone using Claude seriously should set up first."*

## TL;DR

CLAUDE.md is what makes a stateless conversation feel stateful — every session starts with zero memory unless you've configured a persistent instruction file. TheAIWorld22's contribution: a complete paste-ready library of 21 specific instructions covering communication style, behavior boundaries, context (about-you + about-project + voice/style), memory continuity (MEMORY.md + ERRORS.md + permanent-facts), and developer-specific safeguards.

## The 21 instructions (with paste-ready prompts)

### Part 1 — How Claude talks to you

1. **Kill the filler forever** — *"Never open responses with filler phrases like 'Great question!', 'Of course!', 'Certainly!', or similar warmups. Start every response with the actual answer. No preamble. Just the information."*
2. **Always show options before acting** — *"Before any significant task, always show me 2-3 possible approaches first. Wait for my choice before proceeding."*
3. **Be honest when you don't know** — *"If you are uncertain about any fact, statistic, date, or quote — say so explicitly before including it. 'I'm not certain about this' is always better than presenting a guess as a fact. Never fill gaps with plausible-sounding information."*
4. **Match length to what's actually needed** — *"Match response length to task complexity. Simple questions get short direct answers. Complex tasks get full detailed responses. Never pad responses with restatements or closing sentences that repeat what you just said."*

### Part 2 — How Claude behaves

5. **Ask before making big changes** — stop completely; describe what you're about to change and why; wait for confirmation.
6. **Stay focused on what was asked** — only change what was asked. Mention other improvements at the end; don't touch them.
7. **Always tell me what you changed** — end with a brief summary: changed / untouched / needs attention.
8. **Never take actions on my behalf without asking** — never send/post/publish/share/schedule without explicit current-message confirmation.

### Part 3 — Your context

9. **Tell Claude who you are and what you know** — Name. Role. Background. Strong in [topics]. Still learning [areas].
10. **Give Claude the context of what you're working on** — Project. Goal. Audience. Tone. What to avoid.
11. **Lock in your voice and style** — Voice. Sentence length. Words I use. Words I never use. Format preference.

### Part 4 — Memory and continuity

12. **Make Claude keep a memory file** — *"Maintain a file called MEMORY.md. After any significant decision — add an entry with what was decided, why, and what was rejected. Read MEMORY.md at the start of every session before doing anything."*
13. **End-of-session summary** — *"When I say 'session end' or 'let's stop here' — write a session summary to MEMORY.md."*
14. **Log what didn't work** — *"Maintain a file called ERRORS.md. When an approach takes more than 2 attempts to work — log what didn't work, what worked, and what to remember next time."*
15. **Give Claude a list of facts that never change** — *"These facts are always true. Apply them to every session without exception: [permanent facts]."*

### Part 5 — For developers

16. **Stay in scope — touch nothing you weren't asked about** — *"Only modify files, functions, and lines of code directly related to the current task. Do not refactor, rename, or 'improve' anything I did not explicitly ask you to change."*
17. **Confirm before anything destructive** — list exactly what will be affected; ask for explicit confirmation.
18. **Hard stops** — actions requiring explicit in-session confirmation: deploys / migrations / external API calls / irreversible side effects.
19. **Lock your tech stack** — Language. Framework. Package manager. Database. Testing. Linting. *"If something seems like the wrong tool — flag it. But use it anyway unless I say otherwise."*
20. **Always show exactly what changed** — Files changed. What was modified — one line per file. Files intentionally not touched. Follow-up needed.
21. **Andrej Karpathy's 4 rules** — ask-don't-assume / simplest-solution-first / don't-touch-unrelated-code / flag-uncertainty-explicitly. *"A developer distilled them into 4 instructions. That file hit #1 on GitHub Trending and improved coding accuracy from 65% to 94%."*

## Cross-cite with the wiki

- **[[markdown-as-agent-contract]]**: directly extends the meta-pattern; 21 paste-ready instances of CLAUDE.md applied to non-developer use cases. The wiki's existing concept page focused on the meta-shape (markdown-as-contract) but didn't include a paste-ready instruction library. This source fills that gap.
- **[[CLAUDE]]** (the wiki's own schema file): TheAIWorld22's framing aligns with the wiki's *cite-or-omit* rule (Instruction 3) and *only-modify-what-was-asked* discipline (Instruction 6, 16). Worth reviewing whether any of TheAIWorld22's 21 instructions should be promoted into the brain's own CLAUDE.md.
- **[[hot-cache]]**: Instructions 12-14 (MEMORY.md + ERRORS.md + permanent-facts) are *external-markdown persistent state* — sibling pattern to [[wiki/sources/nateherk-claude-code-os-3m-business|nateherk's `_hot.md`]]. Worth a sub-pattern note.
- **[[cognitive-debt]]**: Instruction 3 (*"be honest when you don't know"*) is the anti-debt protocol applied to Claude's hallucination tendency. Aligns with [[wiki/entities/rohit4verse|Rohit's]] protocol 4 (*"verify load-bearing claims"*).
- **[[wiki/entities/andrej-karpathy]]**: cited in Instruction 21 as the author of the viral CLAUDE.md ruleset. **Notable**: the wiki has Karpathy's [[llm-wiki-pattern]] but not yet his coding-CLAUDE.md ruleset. Worth a future ingest if a primary source surfaces.

## Notable quotes

> "Most people using Claude have never heard of [CLAUDE.md]. The ones who have don't know what to actually put in it. And that gap is costing people hours every single week."

> "Without CLAUDE.md — you start from zero every single session. You repeat yourself. You correct the same mistakes. You explain your preferences for the hundredth time."

> "CLAUDE.md is not just a developer tool. It is a permanent instruction file that anyone who uses Claude seriously should set up before their very first real session."

> *(on Karpathy's 4 rules)* "That file hit #1 on GitHub Trending and improved coding accuracy from 65% to 94%."

## Mentioned entities

- [[wiki/entities/theaiworld22]] — author.
- [[wiki/entities/anthropic]] — Claude provider.
- [[wiki/entities/andrej-karpathy]] — cited in Instruction 21.

## Related concepts

- [[markdown-as-agent-contract]] — direct extension to non-developer audiences.
- [[CLAUDE]] — wiki's own schema; this source's discipline aligns with several wiki conventions.
- [[claude-code-skills]] — adjacent.
- [[hot-cache]] — Instructions 12-14 (MEMORY.md / ERRORS.md / permanent-facts) are external-markdown persistent state.
- [[cognitive-debt]] — Instruction 3 (anti-hallucination) aligns with Rohit's protocol 4.

## Related sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's pattern; TheAIWorld22 cites Karpathy's CLAUDE.md as closing reference.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — adjacent: layered claude.md / skills / contexts / references architecture.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — sibling Cowork-setup guide; Guri's Global Instructions are the operational equivalent of TheAIWorld22's Instructions 1-15.
