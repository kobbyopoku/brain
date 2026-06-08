---
type: source
title: My Claude Code OS Runs My $3M/yr Business — Steal This — nateherk
created: 2026-05-02
updated: 2026-05-02
content_status: substantive
source_url: https://x.com/nateherk/status/2050116705322512766
source_type: x-thread
author: nateherk
source_date: 2026-05-01
raw_path: raw/My Claude Code OS Runs my $3Myr Business. Steal This..md
tags: [ai-os, claude-code, frameworks, llm-wiki-citation, services-business]
---

# My Claude Code OS Runs My $3M/yr Business — Steal This — nateherk

> A founder's full operational playbook for running a $3M/yr business on Claude Code as an "AI Operating System." Coins **Three Ms** (Default Shift / Function Breakdown / Curiosity Rule) and **Four Cs** (Context / Connections / Capabilities / Cadence) as durable frameworks that survive tool churn. **Second wild secondary citation of Karpathy's [[llm-wiki-pattern]]** in this wiki. Introduces the [[hot-cache]] pattern.

## TL;DR

nateherk argues that the way to extract maximum value from Claude Code is to treat it as an Operating System for your business, not as a chat tool. Three durable habits (the Three Ms) shape the mindset; four ordered capabilities (the Four Cs) shape the build. Author walks through his starter repo template ([[wiki/entities/ais-os|github.com/nateherkai/AIS-OS]]), the onboarding flow, the connections discipline (separate API accounts, prefer API-endpoints-saved-as-markdown over MCPs), the skill-authoring framework, and three cadence options (Cloud Routines / Local Scheduled Tasks / Loop) with explicit gotchas. The closing layer is a Karpathy-style LLM Wiki pattern integrated into the OS, with one new addition: a 500-token "hot cache" file that captures the active state of the week so Claude doesn't re-crawl the full wiki on repeat queries.

## Key takeaways

### The Three Ms (durable mindset)

1. **The Default Shift** — before any task, ask *"how could AI do this, or at least 30% of it?"* Author example: had to update 300+ YouTube descriptions; old self would have clicked through every video; new self brainstormed with Claude, found an API path, done in minutes.
2. **The Function Breakdown** — your role is a tree of tasks. A YouTube video isn't one job — it's ideation, scripting, packaging, descriptions, comment replies. You don't automate "a YouTube video." You automate one chunk at a time. Each chunk is reusable.
3. **The Curiosity Rule** — never accept AI output without asking why. Treat AI as a mentor, not a vending machine. Mentors push back, ask questions, sharpen you. Vending machines just take a coin.

**Productivity drops before it climbs**: real changes produce a ~20% dip for the first few days. The 50% gain is on the other side. Most people quit during the dip.

### The Four Cs (build order matters)

1. **Context** — what AI knows about you, your team, your tools, your voice, your money.
2. **Connections** — what data it can reach.
3. **Capabilities** — what it can produce.
4. **Cadence** — when it acts on its own while you sleep.

You can't have cadence without connections, can't have capability without context. Build in order.

**The litmus test**: open a new Claude session, ask a real business question. Does it answer like a teammate or like a stranger who met you 5 seconds ago? If the latter, you have zero context. Start there.

### Map your tools before you touch the repo

Seven tier-1 domains, each with where the data actually lives:

| Domain | Example tools |
|---|---|
| Revenue | Skool, Stripe, QuickBooks |
| Customer | Skool, YouTube |
| Calendar | Google Workspace |
| Comms | Google Workspace, ClickUp, Slack |
| Tasks | ClickUp, Notion |
| Meetings | Fireflies |
| Knowledge | YouTube transcripts, Google Workspace, local files |

This sketch becomes the connections roadmap. *"If you can't see all your business in one diagram, your AI OS won't either."*

### The starter repo

`github.com/nateherkai/AIS-OS` — clone, open in VS Code, set up in 5 minutes. Folders:

- `.claude/skills/` — reusable recipes; ships with three: Audit, Level Up, Onboard.
- `Archives/` — old documents, archived not deleted.
- `Contexts/` — About Business, About Me, Priorities. The Context C.
- `Decisions/` — append-only log; date + reasoning + context entry.
- `References/` — external knowledge. Three Ms doc, tool API references, SOPs.
- `claude.md` — master prompt; updated *2× a day* per the author.
- `.env` — secrets, gitignored.

### Connecting tools the right way

1. **Make a separate account for your AI OS.** Don't give Claude Code your personal API key with full permissions. Author has an "Up at AI" account inside ClickUp with a scoped key. Same for Stripe, QuickBooks. Separate keys also let you see which automation spends what.
2. **Prefer API endpoints over [[mcp-server|MCP servers]].** *"MCPs load every endpoint and every function whether you need it or not. That eats tokens."* Tell Claude: research the docs once, save them as a markdown reference, pull from that file when you need an endpoint. **Markdown is cheap to read; API docs are expensive to crawl every time.** Cross-cuts directly with [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's MCP overhead pattern]].
3. **Store keys in `.env`, never in chat.**
4. **Default to bypass permissions only after you trust it.** Plan mode for brainstorming, Auto for safe stuff, Bypass for everything. Author runs on bypass.
5. **First connection failure is a gift** — ask Claude to update the relevant API doc or skill so the same failure can never happen again. Failure → permanent learning.

### Skills authoring framework

Skill = folder. `.claude/skills/<skill-name>/skill.md`. YAML front matter (name + description) at top, step-by-step rules below.

**Anatomy:**
- Name + description (used by Claude to find the skill).
- Step-by-step rules (the SOP).
- Reference files (brand guidelines, tone, target avatars — heavy stuff).
- Optional scripts (Python or JS the skill can call).

**[[progressive-disclosure|Progressive context loading]] (three levels):**
- Level 1: scan all skill front matter (~100 tokens per skill). Cheap.
- Level 2: load the full skill.md if Claude picks one (couple thousand tokens).
- Level 3: only pull reference files when the task needs them.

→ skill.md should stay under 500 lines; reference docs separate.

**Six-step skill-building framework:**
1. Name and trigger (slash command, natural language, or both).
2. Goal in one sentence (what's the output).
3. Step-by-step process (what you'd do manually, in order).
4. Reference files (what context does it need).
5. Rules and guardrails (what could go wrong).
6. The improvement loop (after you run it, update it).

**Concrete example**: Pulse Check skill used to call ClickUp MCP and search every list ID — slow, wasteful. Author hardcoded list IDs into skill.md and delegated heavy ClickUp work to a `clickup-searcher` sub-agent so the heavy data never blows the main context.

**Skills live in two places:**
- **Project-level** — `.claude/skills/` inside a specific repo. Only that project sees them.
- **Global** — `~/.claude/skills/` in home directory. Every Claude Code session can reach them.

### Audit and Level Up — the built-in improvement loop

**Audit** (`/audit`) scores the AI OS out of 100 across the Four Cs; returns top 3 gaps ranked by leverage; saves every audit so the score climb is trackable. Author got 54.5/100 day one.

**Level Up** (`/level-up`) — pulls from priorities + connections + reachable capabilities, then asks five questions:
1. What did you do 3+ times this past week?
2. Drudgery — anything manual, boring, copy-paste?
3. Smart-intern test — anything a smart intern could absolutely handle that you did yourself?
4. Constraint — if 500 new community members showed up Monday, what would break first?
5. Growth lever — what would give you 500 more clients tomorrow if it ran on autopilot?

The pair is the engine. Audit finds where the foundation is thin. Level Up finds the next leverage point. Run weekly.

### Cadence — three options with gotchas

**1. Cloud Routines** (Anthropic infrastructure; laptop can be off):
- Triggered by schedule, API call, or GitHub event.
- Pro: 5/day. Max: 15/day. Team/Enterprise: 25/day.
- **Gotchas**: cloned-repo only (no local file access); `.env` not pushed (use cloud env vars); must explicitly tell prompt to use env vars not `.env`; default network access is "trusted" (Anthropic-vetted domains only — switch to "full" for ClickUp etc.); each run is stateless (cookies/local sessions don't persist); minimum interval 1 hour.
- *Don't push a 200MB repo just to run a small routine; spin up a smaller dedicated repo per routine if context is heavy.*

**2. Local Scheduled Tasks** — desktop app; can catch up on missed runs; needs the app open + computer awake.

**3. Loop** — one-off recurring runs inside a single session; 3-day expiry, then auto-deletes; great for "every 5 minutes check if my deploy is done"; wrong for weekly recurring jobs.

**Routines basically inject a prompt into a real Claude Code session.** Same as typing it yourself. So write specific, one-shot prompts; the routine won't ask clarifying questions.

### The LLM Wiki layer (Karpathy citation)

Author cites Andrej Karpathy's LLM Wiki concept directly. *"No fancy RAG. No embeddings. No vector DB. Just a folder with markdown files, an index file, and a log file."*

His structure:
- `/raw` — source documents.
- `/wiki` — organized output (concepts, entities, sources, analysis).
- `/wiki/_index.md` — master index.
- `/wiki/_log.md` — append-only operation history.
- `/wiki/_hot.md` — **a 500-token cache of what was most recently active**.

He runs two vaults: a YouTube transcripts vault (36+ ingested) for querying his own content, and a "Herk Brain" personal second-brain (meeting notes, business decisions, priorities).

Cites an X user who moved 383 scattered files + 100+ meeting transcripts into a wiki and **dropped token usage by 95% on queries**. Unverified but a useful upper-bound claim.

**The [[hot-cache]] is the move most people miss.** A small 500-token file at the top of the wiki capturing the active state of the week. Claude reads it first before crawling the bigger wiki. Saves tokens on repeat queries.

### Mindset shifts

- **Default Shift** — assume AI does it first.
- **Function Breakdown** — automate the leaves first, not the trunk.
- **Treat AI as a mentor.**
- **Never binary** — the question is never "can AI do this?" but "to what percentage."
- **Productivity drops before it climbs** — take the dip seriously.
- **Failure is data** — every broken run becomes a skill or doc update.
- **POC mindset** — Proof of Concept first; build the cheapest version; if it proves out, then dedicate real resources. Author built dashboards as Claude Artifacts before investing in custom dashboards.
- **Per-account permissions** — separate API keys per agent or service; restrict scope; read-only where possible.
- **Boring is beautiful** — deterministic workflows beat AI agents 9/10 times. Most business processes don't need autonomy. They need a Python script on a cron.

### Daily and weekly loops

- **Daily morning**: ask Claude to plan your day. If the plan is bad, write down what context was missing. Patch tomorrow.
- **Daily end-of-day**: which skills did you use, which prompts did you repeat, what did you have to correct.
- **Weekly Friday**: `/audit`, then `/level-up`. Pick one gap from each, build it next week.

### Success criteria (subjective signals)

1. Your team would rather message your AI OS than message you.
2. You stop opening browser tabs.
3. Knowledge leaves your head and lives in the wiki + contexts + skills.

If 2/3 are true within a month, the system has taken.

## Notable quotes

> "An AI OS sees all your files. It touches your tools. It remembers better than you do."

> "Tools change every six months. Models get deprecated. SDKs get retired. The Three Ms and the Four Cs don't."

> "Markdown is cheap to read. API docs are expensive to crawl every time."

> "Boring is beautiful: deterministic workflows beat AI agents 9 times out of 10."

> "Failure is data: every broken run becomes a skill update or a reference doc update. Nothing breaks twice."

> "If you can't see all your business in one diagram, your AI OS won't either."

> "Tools change. Models change. The Three Ms™ and the Four Cs™ don't."

## Notes

- **Second wild citation of Karpathy's [[llm-wiki-pattern]]** in this wiki — after [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]]. Two independent sources building on Karpathy's pattern in operational contexts. Worth noting on the [[llm-wiki-pattern]] page as an additional Treatment.
- **The [[hot-cache]] pattern is genuinely new** to this wiki and probably worth adopting. A 500-token "what's active this week" file at the top of the brain would prevent the agent from re-reading 123 wiki pages on every read-mode query. Worth a follow-up implementation pass.
- **Cross-cuts strongly with [[wiki/sources/Mnilax-430-hours-claude-code-waste]]**: Nate's "prefer API endpoints saved as markdown over MCPs" is exactly the same insight as Mnilax's #6 pattern (just-in-case tool definitions). The two sources arrive at the same conclusion from different starting points.
- **Cross-cuts with [[wiki/sources/itsalexvacca-services-as-software-7m-agency]]**: both source authors are running services-business-shaped operations on top of Claude Code. Vacca's $7M ARR services agency and Nate's $3M/yr business arrive at similar conclusions about what survives LLM compression (judgment, taste, accountability).
- **Productivity-dip claim** (20% dip before 50% gain) is unverified but consistent with how organizational change typically lands. Worth carrying forward as a planning prior.
- **Author's `/audit` and `/level-up` skills** are the closest thing in the wild to a self-improvement loop for a Claude Code OS. The brain has `bin/wiki_lint.py` for mechanical health; an audit-style skill that scores against Four Cs would be a sibling for *strategic* health.
- The **production-onboarding pattern** (clone repo → say "I want to set up my AI operating system" → 7-question Onboard skill writes About Me / About Business / Priorities to disk) is a model worth adopting for any future product that wants to scaffold context fast.
- The **Glaido voice-tool tip** ("don't type two-sentence answers; voice-dump three paragraphs into each onboarding answer; richer context → better future answers") is operationally useful.

## Mentioned entities

### People
- [[wiki/entities/nateherk]] — author.
- [[wiki/entities/andrej-karpathy]] — cited as conceptual inspiration for the wiki layer.

### Products and tools
- [[wiki/entities/ais-os]] — author's starter repo template.
- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/skool]] — community platform (referenced in business stack).
- [[wiki/entities/clickup]] — task management (referenced; primary connections example).
- [[wiki/entities/quickbooks]] — accounting (referenced).
- [[wiki/entities/fireflies]] — meeting transcripts (referenced).
- [[wiki/entities/glaido]] — voice tool (referenced for onboarding tip).
- [[wiki/entities/notion]] — knowledge platform (referenced).
- [[wiki/entities/stripe]] — referenced in revenue stack (already in wiki via Refero + clear_graphics).
- [[wiki/entities/obsidian]] — referenced as the visual graph view for the wiki layer.

## Related concepts

- [[ai-os-pattern]] — canonical wiki source for this concept.
- [[hot-cache]] — canonical wiki source for this concept.
- [[llm-wiki-pattern]] — second wild citation; nateherk's wiki structure adds `_hot.md` to the Karpathy template.
- [[claude-code-skills]] — skill anatomy + six-step framework.
- [[progressive-disclosure]] — three-level loading model.
- [[mcp-server]] — "prefer API endpoints saved as markdown over MCPs" framing.
- [[multi-agent-orchestration]] — cadence layer.
- [[scheduled-automation]] — Cloud Routines vs Local vs Loop tradeoff.
- [[subagents]] — clickup-searcher example.
- [[markdown-as-agent-contract]] — claude.md / skill / context as layered contracts.
- [[services-as-software]] — adjacent business model.

## Related sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — the foundational source nateherk's wiki layer is built on.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — sibling source: same pattern of layered Claude Code stack, different framing (24/7 dev team vs AI OS).
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — operational sibling: nateherk's "prefer API endpoints over MCPs" = Mnilax's MCP overhead pattern.
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — conceptual sibling: independently arrives at three-level progressive disclosure.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — adjacent: services-shape business running on Claude Code.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — early-stage version of the same business shape.
