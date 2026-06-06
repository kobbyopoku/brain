---
type: source
title: "AnatoliKopadze — How to Actually Use Claude: 18 steps that unlock 100% of its potential"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/AnatoliKopadze/status/2054568935274549597
source_type: x-thread
author: Anatoli Kopadze (@AnatoliKopadze)
source_date: 2026-05-13
raw_path: "raw/How to Actually Use Claude. 18 steps that unlock 100% of its potential.md"
content_status: substantive-verbatim
tags: [claude, prompt-engineering, claude-projects, custom-instructions, extended-thinking, personal-productivity, token-economy, anatoli-kopadze]
---

# AnatoliKopadze — How to Actually Use Claude: 18 steps that unlock 100% of its potential

> Anatoli Kopadze's second wiki source — an 18-step consumer playbook for the **Claude.ai chat product** (not Claude Code), built on the thesis that *"most people who use it every day are still using 10% of what it can do"* and that the fix is setup (Projects + Custom Instructions) plus a shift from treating Claude as a search engine to treating it as a thinking partner.

## TL;DR

A non-developer-facing guide to the consumer Claude.ai app, organized as 18 steps across five phases: **setup** (Projects, identity context, Custom Instructions), **reframing** (Claude is a thinking partner, not a search engine), **power techniques** (style cloning, sparring partner, Extended Thinking, meta-prompting), **token economy** (output-length limits, preamble removal, one-context-per-chat hygiene), and **ready-to-use prompts** (Feynman explanation, travel, expense analysis, reflection, business-idea stress-test). The load-bearing claim is the same "10% of potential" framing the author used in his earlier [[wiki/sources/AnatoliKopadze-20-claude-prompts|20 Claude Prompts]] catalog, here applied to *setup and interaction discipline* rather than a prompt library. Closing thesis: *"Set it up once. Change how you work permanently."*

## Key takeaways

- **Use a Project, not a bare chat.** Every new chat starts with zero memory; a Project is a persistent workspace where context (identity, instructions, knowledge base) carries across every conversation inside it (step 1).
- **Front-load an identity template into the Project knowledge base** — name, role, day-to-day responsibilities, current goals, main use cases, knowledge level, preferred information format, anti-preferences ("things I don't want"), and topics of interest. Claude reads it at the start of every conversation in the Project (step 2).
- **Convert that identity context into Custom Instructions** via a meta-prompt that asks Claude to write second-person operating rules under 400 words; paste the output into Project Instructions to make it Claude's permanent operating mode (step 3).
- **"Claude is not a search engine."** Treating it as a retrieval tool *"cuts its usefulness by 80 percent."* Replace *"What is X?"* with a problem framed in your context — give it a problem to solve with you, not a definition to recite (step 4).
- **Ask Claude to ask you questions first.** Before any complex task, instruct it to surface the 5 most important questions it needs answered, then begin — output is *"dramatically better because it's built on the right foundation"* (step 5).
- **Style cloning requires samples, not description.** Paste 3-5 writing samples and ask Claude to *analyze patterns* (sentence length, rhythm, vocabulary, openings/closings, formality) and match them exactly, overriding its default voice (step 6).
- **Sparring partner: tell Claude to "attack," not "critique."** Have it destroy a plan — find every wrong assumption and failure mode, argue the opposite, no politeness — then steelman the original position, then give its honest verdict (step 7).
- **Extended Thinking** is a mode (brain icon, or a "think step by step" prompt) where Claude reasons before answering; unnecessary for simple tasks, significant quality gain on hard decisions and analysis (step 8).
- **Claude writes prompts for Claude.** When unsure how to prompt a task, ask Claude to write the best prompt (role + context + format + constraints) and use it immediately — meta-prompting as the *"most underused"* technique (step 9).
- **Specify output length** ("3 sentences max", "5 bullets, no explanation", "under 150 words") — the author claims this *"cuts token usage on most tasks by 40 to 60 percent"* (step 10).
- **Remove preamble** via Custom Instructions: no affirmations ("Great question"), no restatements, no end-summaries unless asked, no gratuitous disclaimers — go directly to the answer (step 11).
- **Don't re-explain yourself each conversation** — pasting the same background every chat wastes tokens; that is precisely what Projects + Custom Instructions exist to absorb (step 12).
- **Start a new chat for a new topic.** Long chats carry all prior context, costing tokens and causing *"context bleed"*; a fresh chat inside the Project keeps Project memory but drops irrelevant baggage (step 13).
- **Five ready-to-use prompts** ship verbatim: Feynman/analogy explanation with comprehension checks (14), travel planning around personal travel style (15), monthly expense analysis with actionable conclusions (16), non-advice-first reflection partner (17), and ruthless business-idea stress-test (18).
- **Closing thesis**: Claude isn't smarter than you — it has *"infinite patience, broad knowledge, and the ability to think through problems from angles you haven't considered."* The people who get the most have *set it up to understand them* and *use it as a partner rather than a dispenser*.

## Notable quotes

> "Claude has been out for two years. Most people who use it every day are still using 10% of what it can do. Not because it's complicated. Because nobody showed them what the other 90% looks like."
> — opening

> "Claude is not a retrieval tool. It is a thinking partner... The moment you treat it like a search engine, you cut its usefulness by 80 percent."
> — step 4

> "Your job is to destroy it. Find every assumption I'm making that could be wrong... Do not be polite. Do not add qualifications. Just attack."
> — step 7 (sparring-partner prompt)

> "Claude is not smarter than you. It does not have better ideas than you. What it has is infinite patience, broad knowledge, and the ability to think through problems from angles you haven't considered."
> — closing

> "Set it up once. Change how you work permanently."
> — closing line

## Notes

- **This is a consumer-product guide, not a Claude Code / agent guide.** Every mechanic referenced — Projects, Project knowledge base, Custom Instructions, the brain-icon Extended Thinking toggle — lives in the Claude.ai chat UI. This distinguishes it from most Claude-Code-centric sources in the wiki (Mnilax, zodchiii, regent0x) and aligns it with the consumer-prompts lineage ([[wiki/sources/AnatoliKopadze-20-claude-prompts|20 Claude Prompts]], godofprompt, bloggersarvesh). Useful as the "front of the funnel" for non-developer Claude adoption — relevant framing for ROAM Labs client onboarding where end-users are not engineers.
- **Cross-author resonance on the "10%" framing.** The same *"you're using 10% of Claude"* hook appears in [[wiki/sources/zodchiii-10-claude-code-agents|zodchiii's 10 agents]] (*"Your Claude Code is 10% of what it could be"*) and in the author's own [[wiki/sources/AnatoliKopadze-20-claude-prompts|20-prompts]] catalog. It is a recurring genre convention in this content cluster, not an independently-derived measurement — the "80%", "40-60%", "10%" figures are rhetorical, not benchmarked. Mark all percentage claims as unverified author assertions.
- **Three of the 18 steps are token-economy claims** (10, 12, 13) that overlap conceptually with [[wiki/concepts/claude-code-overhead-patterns|claude-code-overhead-patterns]] and [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's instrumented study]] — but applied at the *consumer chat* layer (Projects absorb repeated context; new-chat-per-topic avoids context bleed) rather than the agent-runtime/prompt-cache layer. The intuition is the same (don't pay tokens for redundant context); the mechanism is coarser and unmeasured.
- **Step 5 ("ask me questions first") is a direct instance of [[wiki/concepts/question-form-first|Question Form First]]** — though Kopadze frames it as a free-text "ask 5 questions" intake rather than the structured-form variant Open Design codifies. Worth linking as the lightweight consumer-prompt form of the same discipline.
- **Steps 7 and 18 are the same technique applied twice** (adversarial stress-test: "attack then steelman" for a plan; "find everything wrong, then tell me what it would need" for a business idea). Both encode a red-team-then-steelman pattern absent as a standalone concept in the wiki — candidate for a future `adversarial-prompting` concept page if more sources corroborate.
- **Step 3 (Custom Instructions) and step 2 (identity template)** are the consumer-app equivalent of the [[wiki/concepts/context-file|context-file]] / [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] pattern — persistent operating context the model reads at session start. The Claude.ai "Project Instructions" field is functionally CLAUDE.md for the chat product.
- **Step 9 (Claude writes prompts for Claude)** is meta-prompting — adjacent to but distinct from the [[wiki/concepts/personal-claude-prompts|personal-claude-prompts]] library approach; here the prompt is generated on-demand rather than curated.

## Mentioned entities

- [[wiki/entities/anatoli-kopadze]] — author (this is his 2nd substantive wiki source; entity is currently a stub — candidate for de-stubbing).
- [[wiki/entities/anthropic]] — maker of Claude (implicit; the product under discussion).
- [[wiki/entities/claude-projects]] — the persistent-workspace feature the guide is built around (steps 1, 12, 13).

## Related concepts

- [[wiki/concepts/personal-claude-prompts]] — the genre this source belongs to; ships 5 ready-to-use prompts (steps 14-18).
- [[wiki/concepts/question-form-first]] — step 5 ("ask me 5 questions first") is the consumer-prompt form of this intake discipline.
- [[wiki/concepts/context-file]] — steps 2-3 (identity template + Custom Instructions) are the Claude.ai-chat equivalent of a persistent context file.
- [[wiki/concepts/markdown-as-agent-contract]] — Project Instructions function as a chat-product agent contract.
- [[wiki/concepts/extended-thinking]] — step 8 is a direct treatment of the Extended Thinking mode.
- [[wiki/concepts/claude-code-overhead-patterns]] — steps 10/12/13 are the consumer-chat analogue of token-overhead discipline.

## Related sources

- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — same author; the prompt-library companion to this setup-and-discipline guide (shared "10% of potential" thesis).
- [[wiki/sources/godofprompt-paul-graham-startup-prompts]] — sibling consumer-prompt source; step 18 (business-idea stress-test) overlaps with its Paul-Graham startup-eval prompts.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — shares the "you're using 10% of Claude" framing, applied to Claude Code agents instead of the consumer chat product.
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — checklist-format Claude-instruction source; the Custom-Instructions steps here are the consumer-app counterpart to its CLAUDE.md instructions.
