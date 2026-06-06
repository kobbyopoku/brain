---
type: source
title: heynavtoor — How to Build a Personal AI System With Claude That Knows Everything About You
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/heynavtoor/status/2055249160782389690
source_type: x-thread
author: Nav (@heynavtoor)
source_date: 2026-05-15
raw_path: raw/How to Build a Personal AI System With Claude That Knows Everything About You.md
content_status: substantive-verbatim
tags: [claude, personal-ai, memory, projects, voice-matching, connectors, scheduled-automation, no-code, heynavtoor]
---

# heynavtoor — How to Build a Personal AI System With Claude That Knows Everything About You

> Nav (@heynavtoor)'s 7-layer, ~60-minute, no-code recipe for turning Claude from a stateless chatbot into a persistent personal AI that knows your name, business, voice, clients, and goals — *"Every conversation after that starts at mile 10, not mile zero."* This is the **consumer-Claude-product** counterpart to the wiki's Claude-Code / Hermes engineering stacks: same persistent-memory thesis, but built entirely through Settings/Projects/Memory/Connectors UI rather than markdown files or code.

## TL;DR

A non-technical walkthrough for building a "personal AI system" on the consumer Claude product (no Claude Code, no coding) across 7 layers: (1) Personal Preferences, (2) Projects as separate brains, (3) Memory, (4) voice-matching from writing samples, (5) Project Knowledge file uploads, (6) tool connectors (Gmail/Calendar/Drive/Slack/MCP), (7) scheduled automations via Cowork scheduled tasks or Claude Code Routines. The load-bearing claim is the **compound effect**: each layer makes every other layer more powerful, and after three months Claude *"anticipates what you need before you finish typing."* Total setup is ~60 minutes spread over one week; claimed payoff is 5-10 hours saved per week.

## Key takeaways

- The whole system is framed against a single pain: users re-explain who they are *every* conversation because Claude forgets overnight — the fix is making context persistent so each session *"starts at mile 10, not mile zero."*
- **Layer 1 — Personal Preferences** (Settings → Personal Preferences) loads into every conversation automatically. Recommended structure: WHO I AM / HOW I WORK / WHAT I DO NOT WANT / MY CURRENT GOALS. Keep under 500 words.
- The *"What I Do Not Want"* section is called the most powerful and most-skipped part: *"telling Claude what NOT to do is what makes the output feel human instead of robotic."* Example negatives: no "Great question!"/"Absolutely!", no em dashes, no "dive deep into"/"in today's world"/"it's worth noting", don't ask "would you like me to continue?".
- **Layer 2 — Projects as separate brains**: one messy thread causes context bleed across domains; a Project is a separate workspace with its own instructions, files, memory, and conversations. Nav's five: Content Creation / Client Work / Business Operations / Research & Learning / Personal.
- Project custom instructions are distinct from global preferences: *"Global preferences tell Claude who you are. Project instructions tell Claude what this specific workspace is for."*
- **Layer 3 — Memory** (Settings → Memory) is described as off by default for many users; turning it on lets Claude build a profile automatically from conversations, corrections, and repeated mentions. You can also seed it manually ("Remember that my client Sarah prefers formal emails with no exclamation marks") and view/edit/delete entries.
- Memory compounds on a stated timeline: basics after one week, patterns after one month, anticipation after three months.
- **Layer 4 — Voice matching**: upload 5-10 of your best writing samples as Project Knowledge, add a VOICE PROFILE instruction (short sentences, simple words, action-first openings, no filler), and create a reusable Style ("My Voice") under Settings → Styles selectable in any conversation.
- Claimed voice-matching payoff: content you edit for 30 seconds instead of 30 minutes.
- **Layer 5 — Upload your world**: each Project holds files Claude reads and references; start with the 3 most important files per Project rather than dumping everything. Specific upload lists given per Project (content calendar, client list + pricing tiers, SOPs, reading list, etc.).
- **Layer 6 — Connectors** (Settings → Connectors): Gmail, Google Calendar, Google Drive, Slack, and more via MCP connectors. Each connection multiplies the value of the others and turns hypothetical outputs (e.g. a Morning Briefing) into ones grounded in real email/calendar/Slack.
- **Layer 7 — Scheduled automation**: Cowork has Scheduled Tasks; Claude Code has Routines (`/schedule`). Nav runs three daily/weekly: 6:30 AM Morning Briefing (Gmail+Calendar+Slack → one-page brief posted to personal Slack), 4 PM Friday Weekly Report (→ Google Drive), 8 PM Sunday Content Plan (reads analytics → next week's plan).
- **The compound effect is the thesis**: *"Memory makes Projects more useful. Projects make voice matching more accurate. Voice matching makes content creation faster. Connectors make scheduled tasks smarter. Everything reinforces everything else."*
- Explicit rollout order to avoid overwhelm: Layers 1-3 on day one (~22 min), Layer 4 next day, Layers 5-6 across the week, Layer 7 next week. *"60 minutes now for thousands of hours later."*
- Cadence note: Nav posts *"one of these every Tuesday and Friday"* on skills, sub-agents, overnight agents.

## Notable quotes

> "It is not a chatbot anymore. It is a personal AI that knows me better than most of my coworkers do."

> "The 'What I Do Not Want' section is the most powerful part. Most people skip it. But telling Claude what NOT to do is what makes the output feel human instead of robotic."

> "Global preferences tell Claude who you are. Project instructions tell Claude what this specific workspace is for."

> "Opening a blank AI chat feels like going back to a flip phone."

> "Your AI does not know you yet. Go fix that."

## Notes

- **This is the consumer-product version of a thesis the wiki has mostly seen in engineering form.** The persistent-personal-memory goal is identical to [[wiki/sources/nousresearch-hermes-agent|Hermes Agent's]] built-in learning loop and to Karpathy's [[llm-wiki-pattern]], but the *mechanism* here is entirely Claude.ai UI surfaces (Personal Preferences, Projects, Memory, Styles, Connectors, Cowork Scheduled Tasks) — no markdown contract files, no code. Worth filing as the "no-code on-ramp" pole opposite Hermes (agent-internal state) and the LLM-wiki (external markdown).
- **The seven layers map cleanly onto wiki concepts**: Layer 1/2 (preferences + project instructions) are an instance of [[markdown-as-agent-contract]] expressed through UI fields rather than files; Layer 3 (Memory) parallels Hermes's user model and [[hot-cache]]; Layer 6 (Connectors) is [[mcp-server]] integration; Layer 7 (Scheduled Tasks / Routines) is [[scheduled-automation]].
- **The Morning Briefing pattern recurs across the wiki.** Nav's 6:30 AM Gmail+Calendar+Slack briefing is the same shape as Khairallah's 7 AM Cowork Morning Briefing ([[wiki/sources/eng_khairallah1-x-2052684086414852546]]) and Shruti's 6 AM Daily AI Briefing ([[wiki/sources/Shruti_0810-self-improving-obsidian]]). This is now at least the third independent description of a scheduled morning-briefing agent — a candidate pattern worth a concept page if a fourth lands.
- **Unverified / promotional caveats**: the "5-10 hours/week saved", "65→94%"-style improvement implied by the week-1→month-3 timeline, and "Memory is off by default for many users" are author assertions without measurement. The Memory-default claim in particular may be product-version-dependent and is not corroborated by any first-party Anthropic source in the wiki. Treat the timeline figures as motivational, not benchmarked.
- **Voice-matching method overlaps with Shann Holmberg's Content OS** ([[wiki/sources/shannholmberg-content-os]]) and the [[wiki/syntheses/helm-voice-profiles|Helm voice-profiles synthesis]] — both extract a voice profile from a corpus of best work. Nav's version is the lightest-weight articulation (5-10 samples + a 6-line VOICE PROFILE + a saved Style).
- **Relevance to Godwin**: directly applicable to [[wiki/projects/helm|Helm's]] Marketing agent (per-brand voice profiles, scheduled content plans) and to a personal-ops setup; the Projects-as-separate-brains pattern mirrors Helm's per-product agent isolation. The no-code framing is the opposite end from Godwin's typical code-first builds but useful as a fast personal-productivity layer.
- This is heynavtoor's 3rd substantive source in the wiki (after the 10-repos thesis and the $10K/mo 90-day automation business playbook) — update the [[wiki/entities/heynavtoor|heynavtoor]] entity accordingly.

## Mentioned entities

- [[wiki/entities/heynavtoor]] — author; consumer-Claude personal-AI-system tutorial (3rd substantive post).
- [[wiki/entities/claude-code]] — named as the host for Routines (`/schedule`) in Layer 7.
- [[wiki/entities/cowork]] — Claude Cowork named as the host for Scheduled Tasks in Layer 7.
- [[wiki/entities/gmail]] — connector for reading email / drafting replies / Morning Briefing.
- [[wiki/entities/google-calendar]] — connector for schedule + meeting prep + time blocks.
- [[wiki/entities/google-drive]] — connector for reading/referencing docs and saving outputs.
- [[wiki/entities/slack]] — connector for scanning channels + posting the Morning Briefing.
- [[wiki/entities/model-context-protocol]] — "MCP connectors" named as the extension surface beyond the four first-party connectors.
- [[wiki/entities/anthropic]] — maker of Claude, the product the entire system is built on.

## Related concepts

- [[claude-memory]] — Layer 3; Claude's per-account learning system (preferences, patterns, corrections), manually seedable and editable.
- [[wiki/concepts/claude-projects]] — Layer 2; per-domain workspaces with their own instructions/files/memory ("separate brains").
- [[personal-ai-system]] — the overarching framing: stacked persistent-context layers that compound into an AI that knows the user.
- [[voice-matching]] — Layer 4; teaching Claude a user's writing voice via samples + VOICE PROFILE + a saved Style.
- [[scheduled-automation]] — Layer 7; Cowork Scheduled Tasks / Claude Code Routines running briefings and reports unattended.
- [[mcp-server]] — Layer 6; connectors (incl. MCP) wiring Claude to Gmail/Calendar/Drive/Slack.
- [[markdown-as-agent-contract]] — Layers 1-2 are the UI-field expression of the agent-contract pattern (preferences + project instructions).
- [[hot-cache]] — Memory + Personal Preferences play the persistent-active-context role the `_hot.md` file plays in the engineering stacks.
- [[personal-claude-prompts]] — adjacent personal-productivity-via-Claude theme.

## Related sources

- [[wiki/sources/nousresearch-hermes-agent]] — same persistent-personal-memory goal achieved via agent-internal state + code rather than consumer-product UI.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — the external-markdown approach to persistent personal context; Nav's is the no-code UI approach.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — Khairallah's three-session Cowork daily architecture; the 7 AM Morning Briefing is the same pattern as Nav's 6:30 AM brief.
- [[wiki/sources/Shruti_0810-self-improving-obsidian]] — Shruti's 6 AM Daily AI Briefing + self-improving vault; sibling personal-knowledge-architecture source.
- [[wiki/sources/shannholmberg-content-os]] — voice-profile-from-corpus methodology overlapping Nav's Layer 4.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — Cowork onboarding (folder structure + global instructions); the Cowork-specific companion to Nav's Layer 7.
- [[wiki/sources/heynavtoor-10k-claude-automation-business-90-days]] — same author's prior AI-automation-business playbook.
