---
type: source
title: 20 Claude Prompts that Turn a $20 Subscription into a Personal Assistant, Editor, Coach, and Analyst — Anatoli Kopadze
created: 2026-05-02
updated: 2026-05-02
source_url: https://x.com/AnatoliKopadze/status/2049492553133629950
source_type: x-thread
author: Anatoli Kopadze
source_date: 2026-04-29
raw_path: raw/20 Claude Prompts that turn a $20 Subscription into a personal Assistant, Editor, Coach, and Analyst.md
tags: [prompts, personal-productivity, claude, prompt-engineering]
---

# 20 Claude Prompts that Turn a $20 Subscription into a Personal Assistant, Editor, Coach, and Analyst — Anatoli Kopadze

> A curated catalog of 20 detailed prompt templates spanning research, writing, career, daily life, and learning. Each prompt is a structured directive — role + task + rules + output spec — usable verbatim or as a base for personalization. The wiki's canonical source for [[personal-claude-prompts]].

## TL;DR

Anatoli Kopadze argues that most $20/mo Claude subscriptions are 10% utilized — people ask, rewrite, summarize, and stop there. The post demonstrates 20 prompt templates that turn Claude into a research analyst, brutal editor, salary-negotiation roleplayer, interview simulator, meal planner, financial analyzer, Feynman tutor, Socratic teacher, and more. Each template is a fully-structured directive (role + task + structured output rules + constraints). The contribution to this wiki is both the **catalog itself** (saved as raw source) and the **meta-pattern** of curating personal prompts — see [[personal-claude-prompts]].

## Key takeaways

The 20 prompts are organized into 5 categories. Each is captured here by name + one-sentence essence; full text lives in the raw source.

### Deep research
1. **Multi-Source Synthesis** — paste many articles; produce a single conflict-resolved brief with consensus / conflicts / gaps / strongest claim / actionable takeaway.
2. **Devil's Advocate Mode** — Claude as ruthless critic; attack across flawed assumptions, execution risks, market reality, fatal flaw.
3. **Steelman Any Position** — build the strongest, most charitable version of a position you disagree with.
4. **Mental Model Builder** — teach a topic as 3-5 connected mental models, not facts.

### Writing
5. **Style Mimic** — analyze 3 samples of your writing, then produce new writing in your voice.
6. **The Brutal Editor** — destroy a draft across cuts, weak ideas, missing pieces, structure, single biggest problem.
7. **One Text, Five Audiences** — beginner, expert, skeptic, journalist, executive — fully committed translations of one idea.
8. **Bullets to Article** — turn rough notes into a finished piece without dropping or inventing ideas.

### Career
9. **Salary Negotiation Roleplay** — Claude plays a hiring manager with realistic budget objections; pushes back on weak arguments.
10. **Interview Simulator** — full interview with structured per-answer feedback (strong/weak/should-have-said).
11. **Resume Multiplier** — three tailored versions of one resume for three different jobs without lying or omitting.
12. **Difficult Conversation Prep** — opening line, 3 likely responses, your responses, the trap, the exit.
13. **LinkedIn Bio Rewrite** — five voice-distinct headline + summary versions, banned-word list enforced.

### Daily life
14. **Weekly Meal Plan with Shopping List** — 7-day plan + grocery list by section + meal-prep guide + estimated cost.
15. **Legal Document Translator** — plain-English summary + 3 riskiest clauses + missing standard protections + 5 questions to ask a lawyer. Explicitly *not* legal advice.
16. **Personal Finance Analyzer** — categorize last month's spend, find specific leaks (not "spend less on dining" — quantified), feasibility of stated goal, the one behavior to change.
17. **Travel Planner** — day-by-day itinerary, book-in-advance list, hidden gems, money breakdown, overhyped places to skip.

### Learning
18. **Feynman Tutor** — one concept at a time, comprehension question after each, never repeats the same explanation.
19. **30-Day Curriculum Builder** — day-by-day doing-not-reading plan, 80% doing 20% learning, checkpoints at 7/14/21/30.
20. **Socratic Mode** — only questions, never answers; one question at a time; refuse to break character even if asked.

## Notable quotes

> "You pay $20/month for Claude. Most people use 10% of it."

> "Claude can be your fitness coach, your language tutor, your negotiation trainer, your financial analyst, your editor, your strategist. Not approximately. Literally. The only variable is the quality of your prompt."

> "Passive reading creates familiarity. Socratic dialogue creates knowledge. There is a difference, and you feel it immediately."
> — § Socratic Mode

## Notes

- **Each prompt is a kind of de facto skill file.** They have a role, a task, a structured output spec, and explicit rules for what NOT to do. This is the same shape as [[skill-md]]. The difference is distribution — these are personal prompts pasted on demand, not loaded as registered skills.
- **The catalog approach is itself a contribution.** Curating prompts in categories matters — it lets you recall not just *what* prompt to use but *which class* of prompt the situation calls for. See [[personal-claude-prompts]].
- **Three prompts cross-cut directly with this wiki's operations**:
  - **Multi-Source Synthesis (#1)** is essentially a manual [[ingest]] for one query.
  - **Devil's Advocate Mode (#2)** is the kind of [[lint]] sub-operation worth running on the wiki itself periodically.
  - **Mental Model Builder (#4)** is what concept pages aim to be.
- **Worth considering**: registering several of these as actual Claude Code skills in this vault. The Brutal Editor, Devil's Advocate, and Multi-Source Synthesis would each benefit from being one slash-command away.
- **Prompt-engineering evolution**: relative to godofprompt's `<role>...<task>` Paul Graham prompts, this source's prompts are denser, more rules-explicit, and use plain markdown structure rather than XML-like tags. Both work; this style is more readable.

## Mentioned entities

### People
- [[wiki/entities/anatoli-kopadze]] — author.

## Related concepts

- [[personal-claude-prompts]] — meta-pattern this source is the canonical wiki source for.
- [[claude-code-skills]] — adjacent: structured prompts as the seed of skill files.
- [[skill-md]] — related: many of these prompts could be re-shaped as SKILL.md files.
- [[markdown-as-agent-contract]] — broader pattern.
- [[ingest]] — Multi-Source Synthesis prompt is a manual instance.
- [[lint]] — Devil's Advocate Mode is a wiki-applicable critique pattern.

## Related sources

- [[wiki/sources/godofprompt-paul-graham-startup-prompts]] — narrower domain (startup eval), same practice.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — describes the *systems* layer that makes prompts compound; this source is the *content* layer.
