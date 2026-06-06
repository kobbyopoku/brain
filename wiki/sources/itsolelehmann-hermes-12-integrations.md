---
type: source
title: Ole Lehmann — Turn Hermes into a Superagent (12 integrations)
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/itsolelehmann/status/2056343273023688989
source_type: x-thread
author: Ole Lehmann (itsolelehmann)
source_date: 2026-05-18
raw_path: raw/Turn Hermes into a Superagent with these 12 integrations..md
content_status: substantive-verbatim
tags: [hermes-agent, integrations, mcp-server, superagent, agent-workflows, marketing-ops]
---

# Ole Lehmann — Turn Hermes into a Superagent (12 integrations)

> Ole Lehmann's prescription for **what integrations to plug into Hermes Agent**, organized into 4 job-buckets every useful agent setup covers: **Research / Action / Workspace / Memory**. Frames Hermes-without-integrations as *"a brain floating in a jar — smart, fast, happy to talk for hours, but completely cut off from your actual life."* Integrations are *"the senses and limbs you bolt onto that brain."* Plug 2 → context-aware chatbot. Plug 12 → *"the first thing you'll see when you unlock your phone in the morning is a list of complex workflows Hermes already ran for you overnight."*

## TL;DR — the 12 integrations

| Job | Integration | Why |
|---|---|---|
| **Research** | **Firecrawl** | Cleaner data, faster, fewer tokens than native Hermes search. Keep on by default. |
| **Research** | **Reddit** | Read on what people actually think about a product/niche/problem; scope new ideas. |
| **Research** | **YouTube transcripts** | Captions from any video → searchable notes. High-leverage; almost nobody plugs it in. |
| **Action** | **Browserbase** | Actual browser access — log in, click, navigate sites that block scrapers. If Firecrawl + Browserbase both plugged in, Hermes picks automatically. |
| **Action** | **Bland (or Twilio)** | Phone voice — Hermes places live calls (e.g. booking reservations). |
| **Action** | **Stripe** | Payments / customers / failed charges / refunds. Ask *"why did this customer churn"* with receipts. Agentic-payments rollout coming. |
| **Workspace** | **Google Workspace** | Gmail + Calendar + Drive + Docs + Sheets one connector. *"Plug this in before anything else."* |
| **Workspace** | **Discord** | Per-channel workflows (Ole hosts his business in Discord). |
| **Workspace** | **GitHub** | Code + issues + PRs. *"Non-negotiable if you ship code."* |
| **Memory** | **Readwise** | Highlights from books/articles/tweets/podcasts. Solves *"dead knowledge"* problem. |
| **Memory** | **Granola** | Searchable meeting transcripts. *"What did that client say about pricing last month."* |
| **Memory** | **Obsidian** | *"Karpathy-style LLM wiki second-brain maxxing."* Hermes reads across the whole vault. |

## The 4-job mental model

> *"Every Hermes setup that actually works ends up doing 4 things for you: research, action, workspace, and memory. Miss one and the agent goes blind in that direction. Cover all four and you've got something that feels like a coworker."*

Worth absorbing as a *general* multi-agent integration discipline — applies beyond Hermes (Helm, Claude Code, any agent runtime).

## Stacked workflows (the value compounding)

> *"Two tools are useful. Twelve tools are where the workflows above start working."*

Three of Ole's actual stacked workflows:

1. **The sponsor filter** — DM/email about sponsorship → Hermes auto-reads it → Firecrawl scrapes their site → Reddit + YouTube scan for chatter → drops a one-pager in Discord with a fit-rating for his audience.
2. **The customer support agent** — Hermes scans Gmail morning support emails → categorizes by issue type → logs in Discord with priority tagged. Weekly: drops a summary in Obsidian with the 5 recurring problems to fix at the root.
3. **The Monday business dashboard** — Mondays 8AM: pulls revenue/subs/refunds/churn from Stripe + follower growth/post views from X+LinkedIn via Browserbase → posts a week-vs-last-week breakdown in Discord. *"10 seconds to read instead of an hour of dashboard hopping."*

**Each stacked workflow uses 3-4 integrations. None possible with one plugged in.**

## Onboarding sequence (10 min)

1. *"Hey Hermes, I want to connect my Gmail. What do I need?"* — Hermes walks you through OAuth / API key / MCP / whatever in the same conversation.
2. Test before moving on (*"What's on my calendar today?"* / *"Pull the last 5 failed Stripe charges."*).
3. Stack them.

## Notable quotes

> *"Integrations are the senses and limbs you bolt onto that brain."*

> *"Plug Firecrawl and Browserbase in, Hermes picks between them automatically depending on the task."*

> *"Obsidian is for Karpathy-style LLM wiki second-brain maxxing."* *(direct nod to the [[wiki/concepts/llm-wiki-pattern|LLM Wiki pattern]] this brain is built on)*

## How this composes with the wiki

- [[wiki/entities/hermes-agent]] — adds **integration discipline** (the 4-job model) to the Hermes treatment beyond Shann's operator playbook.
- [[wiki/projects/helm]] — **Helm's MCP catalog should map to the 4-job model**: Lead-Mgmt MCP set covers Research (Firecrawl/Reddit) + Action (Notion-CRM); Sales MCP set covers Action (Stripe); Marketing MCP set covers Workspace (Google Workspace) + Action (Postiz/Browserbase); Operations + PM cover Memory (Brain-wiki MCP + Obsidian). Helm's current catalog is missing **Firecrawl, Browserbase, Bland, Readwise, Granola** — worth adding as Week 5+ enhancements.
- [[wiki/concepts/mcp-server]] — Ole's 12 integrations are 12 instances of the MCP-server concept (some are MCP, some are direct API per Hermes's gateway). Adds the **4-job categorization** as a useful taxonomy for MCP catalogs.
- [[wiki/concepts/markdown-as-agent-contract]] — sponsor-filter and Monday-dashboard workflows are agent-contract artifacts at the *integration-stack* scope.
- [[wiki/concepts/llm-wiki-pattern]] — Ole's explicit *"Karpathy-style LLM wiki second-brain maxxing"* via Obsidian + Hermes is the **5th wild secondary citation** (regent0x_ → nateherk → CyrilXBT → Shruti → Ole Lehmann).

## Mentioned entities

- [[wiki/entities/itsolelehmann]] — *(new)* Ole Lehmann; runs `aisolo.beehiiv.com` newsletter (37k subs); AI workflow content creator.
- [[wiki/entities/hermes-agent]] — primary subject.
- [[wiki/entities/firecrawl]] — *(stub candidate)* agent-optimized web search.
- [[wiki/entities/browserbase]] — already in wiki; confirmed as Hermes integration.
- [[wiki/entities/bland]] — *(stub candidate)* voice-call API for agents.
- [[wiki/entities/twilio]] — *(stub candidate)* voice/SMS alternative to Bland.
- [[wiki/entities/stripe]] — already in wiki; confirmed agent integration target.
- [[wiki/entities/google-workspace]] — adjacent to existing Gmail / Google Drive entities.
- [[wiki/entities/discord]] — *(stub candidate)* per-channel agent workflow surface.
- [[wiki/entities/github]] — *(stub candidate)* code/issues/PRs integration.
- [[wiki/entities/readwise]] — already in wiki; confirmed as Hermes memory integration.
- [[wiki/entities/granola]] — *(stub candidate)* meeting transcripts.
- [[wiki/entities/obsidian]] — already in wiki; confirmed as Hermes memory layer.

## Related concepts

- [[mcp-server]] — 12 integration instances.
- [[llm-wiki-pattern]] — 5th wild citation.
- [[markdown-as-agent-contract]] — stacked-workflow agent contracts.
- [[hot-cache]] — Memory-job integrations are operational hot-cache surfaces.

## Related sources

- [[wiki/sources/shannholmberg-hermes-agent-operator]] — operator playbook; integrations layer Ole describes plugs into Shann's fleet.
- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — `/goal` primitive; stacked workflows above are typical `/goal` use cases.
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — 5-agent architecture; Ole's stacked workflows are the cross-agent layer.
