---
type: source
title: "CyrilXBT — How to Build an Obsidian Dashboard That Shows You Everything That Matters Today"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/cyrilXBT/status/2056555832805089310
source_type: x-thread
author: CyrilXBT (@cyrilXBT)
source_date: 2026-05-19
raw_path: raw/How to Build an Obsidian Dashboard That Shows You Everything That Matters Today.md
content_status: substantive-verbatim
tags: [obsidian, dataview, dashboard, personal-knowledge, daily-briefing, claude-code, mcp, n8n, second-brain, ai-os]
---

# CyrilXBT — How to Build an Obsidian Dashboard That Shows You Everything That Matters Today

> CyrilXBT's complete zero-to-operational build of a single Obsidian note that **reads** (never stores) live data from across the vault via Dataview and surfaces six business-critical views, then connects to Claude Code via Filesystem MCP for an automated 6 AM natural-language morning briefing.

## TL;DR

The dashboard is *one note that reads, it does not store*: every section is a Dataview query that pulls live data from project / task / client / daily notes based on their YAML properties, so it never needs manual maintenance — you update source notes the way you always have and the dashboard reflects the change on open. Six sections (Today's Priorities / Active Projects / Next 7 Days / Client Health / Open Loops / Revenue Pulse) replace a 45-minute morning orientation across five tools with a single note you read in under two minutes. Connected to Claude Code via the Filesystem MCP, it gains two capabilities: an intelligent morning briefing (Claude synthesizes meaning, not raw tables, in under 300 words) auto-delivered to the daily note via N8N at 6 AM, and automatic property updates (Claude reads `DONE:` / `UPDATE:` lines from the daily note and writes the corresponding project/task properties). The build takes one afternoon; the compounding (data-currency discipline) shows at month two.

## Key takeaways

- **Read not store is the core principle.** A dashboard is not another place to put information — it is a single note that *reads* from everywhere else in the vault and displays what is relevant right now. It has no content of its own, only queries. Because it reads rather than stores, it never needs manual maintenance.
- **The integration-layer problem.** Most people start the workday as the integration layer connecting email / Slack / project folders / calendar / task list — a 45-minute manual assembly. The dashboard removes the human from that role by surfacing everything before any project file is opened.
- **Six sections, one note.** Today's Priorities (tasks due/overdue, priority-sorted, `LIMIT 10`), Active Projects (completion % + deadline + `next_action`), Next 7 Days (everything vault-wide with a deadline in the window, any note type), Client Health (health + last_contact + next_touchpoint, at-risk auto-sorted to top), Open Loops (yesterday's `OPEN:` items), Revenue Pulse (active clients by MRR + live total).
- **Two Obsidian features make it possible:** Dataview (community plugin; a query engine that renders live results inside any note) + Properties (YAML frontmatter metadata Dataview reads). Dataview is the *only* plugin the core dashboard requires.
- **Consistent properties per note type are mandatory.** Property names must match *exactly* between notes and queries — one typo makes a note invisible to its query. Start with minimum-viable properties (`type`, `status`, `priority`, `due`/`deadline`, `client`, `next_action`, `completion`, `mrr`, `health`, `last_contact`, `next_touchpoint`) and add as needed.
- **Folder convention encodes note type:** `01 - PROJECTS` / `02 - TASKS` / `03 - CLIENTS` / `04 - DAILY`. Queries scope to a folder (`FROM "01 - PROJECTS"`) for speed.
- **`LIMIT 10` is a forcing function, not a display cap.** A dashboard showing 40 overdue tasks creates anxiety not clarity; capping forces honest prioritization at the properties level — items that do not make the cut need their due date or priority re-evaluated.
- **`next_action` is the most valuable column** — it surfaces what each project needs right now without opening any project file; combined with deadline + completion you assess every active project in under two minutes.
- **Client health sort makes the action obvious without thought.** `SORT health ASC, last_contact ASC` puts at-risk clients (and least-recently-contacted within each tier) at the top. Three canonical health values: `healthy` / `attention` / `atrisk`. Turns a 20-minute manual CRM review into an auto-sorted table.
- **The `OPEN:` convention captures the in-between items.** Anything important enough to note but not formal enough to be a task gets prefixed `OPEN:` in the daily note; a `FLATTEN file.lists` query surfaces yesterday's `OPEN:` items on today's dashboard — closing the gap that formal-task-only systems leave open.
- **Revenue Pulse uses an inline DataviewJS reduce** to live-sum active-client `mrr` (`...map(p => p.mrr).array().reduce((a,b) => a + b, 0)`) — current revenue picture in 15 seconds, no spreadsheet. MRR property must be a *number* (`mrr: 3000`), not a string (`mrr: "$3,000"`).
- **An inline date header** (`dv.date("today").toFormat("EEEE, MMMM d, yyyy")`) renders today's date so you always know which day the dashboard shows.
- **Claude Code via Filesystem MCP adds two capabilities:** (1) intelligent morning briefing — Claude reads the dashboard + every file it references and synthesizes *what the data means* (most-important thing, what needs attention before noon, what's at risk, which client needs attention, one open decision) in <300 words, not a description of tables; (2) automatic property updates — Claude reads `DONE:` / `UPDATE:` lines from the daily note, finds the files, writes the properties, and logs the changes.
- **The briefing runs automatically via N8N at 6 AM**, depositing the briefing in the daily note before the laptop is opened; a Telegram notification signals it is ready. Daily workflow: 6:00 notification → 6:02 read briefing → 6:05 confirm against dashboard + add tasks → 6:10 start working. No email-first, no Slack-first.
- **Data-currency discipline is the real product.** Three habits keep the dashboard accurate: update properties the moment something changes, use `OPEN:` consistently, and do a 3-minute end-of-day review (five 5 PM property updates produce a more accurate 6 AM briefing than five updates made while reading it). Immediate value day one; compounding visible month two; by month three you do not start your day without it.

## Notable quotes

> "A dashboard is not another place to put information. It is a single note that reads information from everywhere else in your vault and displays what is relevant right now."

> "The problem is not that the information does not exist... The problem is that accessing it requires you to be the integration layer between all of it. You are the system that connects the information. The Obsidian dashboard removes you from that role."

> "Do not describe the tables. Tell me what they mean." — the morning-briefing prompt's load-bearing instruction.

> "The build takes one afternoon. The compounding starts the first morning. Build it today."

## Notes

- **This is a CyrilXBT post that finally arrives with a verbatim, technically complete body.** Prior CyrilXBT ingests split between substantive ([[wiki/sources/cyrilxbt-x-2052570518667378918|5-agents-replace-5-employees]], [[wiki/sources/cyrilxbt-claude-agent-manages-business|agent-vs-automation mental model]]) and URL-only stubs ([[wiki/sources/cyrilxbt-x-2052923836090167526]], [[wiki/sources/cyrilxbt-x-2052235121416188114]]). This is a distinct status-id (`2056555832805089310`) and a new ingest, not a stub upgrade.
- **The "read not store" principle is the data-layer complement to the [[wiki/concepts/llm-wiki-pattern|LLM Wiki pattern]].** Karpathy's wiki is curated prose the LLM maintains; CyrilXBT's dashboard is a *derived read-only view* over structured note metadata. Both reject duplication — the wiki keeps one canonical source page; the dashboard keeps one canonical property value. This is the same single-source-of-truth discipline applied at the metadata layer rather than the prose layer.
- **This is the third Obsidian-as-second-brain morning-briefing source in the wiki**, joining Shruti's [[wiki/sources/Shruti_0810-self-improving-obsidian|6 AM Daily AI Briefing]] and Khairallah's [[wiki/sources/eng_khairallah1-x-2052684086414852546|7 AM Morning Briefing session]]. CyrilXBT's contribution over those is the *exact Dataview query layer* — the others describe the briefing outcome; this one ships the queries that produce the underlying data.
- **The Filesystem-MCP + N8N + Telegram stack mirrors the runtime in CyrilXBT's own [[wiki/sources/cyrilxbt-x-2052570518667378918|5-agents post]]** (Claude Max + N8N + Obsidian). The dashboard is best read as the *personal-productivity surface* of that same multi-agent business stack — the human-facing read view sitting on top of the agent-maintained data.
- **Directly relevant to [[wiki/projects/helm|Helm]].** Helm's Analytics meta-orchestrator agent needs exactly this kind of cross-entity read view (lead / sales / marketing / operations status in one place). The Dataview "read not store" pattern and the `LIMIT`-as-forcing-function discipline are transferable to Helm's reporting surface even though Helm's store is PostgreSQL not markdown frontmatter.
- **The automatic-property-update capability is a writeback agent**, structurally the inverse of the dashboard's read. It is a narrow, safe instance of the [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] pattern: the daily note's `DONE:` / `UPDATE:` lines are an informal command surface the agent parses and acts on. Uncertain how conflict/ambiguity is handled (e.g. two projects with similar names) — the source does not say.
- **Troubleshooting section is a useful properties-hygiene checklist:** empty results = property-name mismatch; properties not displaying = frontmatter not at very top; date queries failing = non-`YYYY-MM-DD` format (`2026-5-18` breaks, `2026-05-18` works); slow loads = query the whole vault (`FROM ""`) instead of a folder; inline-calc errors = MRR stored as string not number.
- The post closes with a CTA to follow [[wiki/entities/cyrilxbt|@cyrilXBT]] for the exact queries / prompts / templates — mild promotional tail, but the body already contains the full working build.

## Mentioned entities

- [[wiki/entities/cyrilxbt]] — author; agentic-AI + personal-knowledge-vault content. This is his first verbatim Obsidian-dashboard build ingested.
- [[wiki/entities/obsidian]] — the host environment; the vault the dashboard reads from.
- [[wiki/entities/dataview]] — *(new)* the Obsidian community plugin that powers every dashboard section.
- [[wiki/entities/claude-code]] — connected via Filesystem MCP to produce the morning briefing and writeback property updates.
- [[wiki/entities/model-context-protocol]] — the Filesystem MCP is the integration surface between Claude Code and the vault.
- [[wiki/entities/n8n]] — runs the 6 AM briefing job automatically.
- [[wiki/entities/telegram]] — *(new)* delivers the "briefing ready" notification.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]] — the dashboard's "read not store" principle is the structured-metadata complement to Karpathy's curated-prose wiki.
- [[wiki/concepts/read-not-store-dashboard]] — *(new)* the core pattern this source defines: a single note of live queries over vault metadata, never manually maintained.
- [[wiki/concepts/properties-as-metadata]] — *(new)* consistent YAML frontmatter per note type as the queryable substrate; exact-match property names are mandatory.
- [[wiki/concepts/daily-ai-briefing]] — *(new)* the automated morning natural-language synthesis pattern (6 AM N8N + Claude + daily note), shared with Shruti and Khairallah.
- [[wiki/concepts/markdown-as-agent-contract]] — the `DONE:` / `UPDATE:` / `OPEN:` daily-note conventions are informal command surfaces an agent parses.
- [[wiki/concepts/mcp-server]] — the Filesystem MCP is the read/write bridge between Claude Code and the vault.
- [[wiki/concepts/scheduled-automation]] — the N8N 6 AM cron is the orchestration trigger for the briefing.
- [[wiki/concepts/ai-os-pattern]] — the dashboard is the human-facing read surface of a Claude-as-OS personal-business stack.

## Related sources

- [[wiki/sources/Shruti_0810-self-improving-obsidian]] — Shruti's 4-layer Obsidian vault + 6 AM Daily AI Briefing; describes the briefing outcome where this source ships the Dataview query layer beneath it.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — Khairallah's three-session daily architecture (7 AM Morning Briefing); the workflow analogue at the Cowork layer.
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — same author's 5-agents-replace-5-employees post; same Claude Max + N8N + Obsidian runtime, the agent layer beneath this read surface.
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — same author's agent-vs-automation mental-model post.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — AI-OS playbook; the dashboard is a concrete instance of the read surface in that OS pattern.
