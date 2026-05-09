---
type: concept
title: Hot Cache
created: 2026-05-02
updated: 2026-05-05
aliases: [_hot.md, active-state cache]
tags: [llm-wiki, optimization, claude-code]
---

# Hot Cache

> A small (~500-token) markdown file at the top of an LLM Wiki capturing what's most recently active — the week's focus, recent decisions, in-flight projects. Loaded first on every read-mode query so the agent doesn't have to crawl the full wiki to answer questions about *now*.

## Definition

A **hot cache** is a deliberately short summary file (typically `_hot.md`, `wiki/_hot.md`, or similar) that lives at a known path in an [[llm-wiki-pattern|LLM Wiki]]. Its content is the **active state of the wiki at this moment** — what the user is currently working on, the questions live this week, the decisions made in the last 7 days, anything time-sensitive. The file is small by design (~500 tokens) so the agent can load it as the cheapest possible first read on any query.

The pattern is an extension to Karpathy's original LLM Wiki design (which has `index.md` + `log.md`). It adds a third special file optimized for *recency*, where index optimizes for *catalog* and log optimizes for *chronology*.

## Why it matters

Most queries against a personal wiki are about **what's current**, not what's historical. Without a hot cache, the agent has to either (a) read the full index and follow links to find recent material — expensive on a 100+ page wiki, or (b) crawl `log.md` for recent entries — narrow and operational. Neither is optimized for "what's relevant to me right now."

The hot cache solves this with a single file that holds the *currently-load-bearing context*. One source ([[wiki/sources/nateherk-claude-code-os-3m-business]]) cites an X user who reduced query token usage by **95%** by introducing a hot cache against scattered files and 100+ meeting transcripts. Unverified upper-bound, but directionally consistent with [[claude-code-overhead-patterns|overhead-pattern]] math: most queries don't need most of the wiki.

The pattern composes naturally with [[progressive-disclosure]]: hot cache is L0 (always loaded), index is L1 (catalog navigation), individual pages are L2 (full content), referenced sub-pages or sources are L3.

## Treatment across sources

- [[wiki/sources/nateherk-claude-code-os-3m-business]] — canonical wiki source for the pattern. Author describes a `_hot.md` file at the top of his Karpathy-style wiki: *"a 500-token cache of what was most recently active"*. Calls it *"the move I'd missed"* until adoption. Cites a 95% token-usage reduction from a third party (unverified).
- [[wiki/sources/nousresearch-hermes-agent]] — *2026-05-05*. The **agent-internal alternative** to the external-`_hot.md` pattern: [[wiki/entities/hermes-agent|Hermes Agent]] builds active state into the agent itself rather than as an external markdown file. Self-improving learning loop creates and refines skills from experience, persists knowledge across sessions, searches its own past conversations, builds a deepening user model. Both approaches solve the same problem (persistent agent state across sessions) via different mechanisms (passive markdown read by agent vs active state managed by agent). Worth comparing when designing a new agent setup: external markdown is simpler to inspect and version; agent-internal is more autonomous but less observable.
- [[wiki/sources/cyrilxbt-x-2052235121416188114]] — *2026-05-08*. **Daily Brief variant** of the hot-cache pattern. Where nateherk's `_hot.md` is *manually updated recent state*, CyrilXBT's Daily Brief is an *automated 6am prompt* that surfaces *"3 most interesting connections"* between recent captures and older notes — adds **connection-finding** to the recent-state-summary semantics. A natural extension worth tracking as a sub-pattern within the hot-cache family.

## Sub-claims and details

### What goes in a hot cache

- **Active focus** — what the user is working on this week.
- **Recent decisions** — last 7-14 days.
- **In-flight projects** — names + status (links to project pages).
- **Open questions** — anything live and unresolved.
- **Currently-relevant entities** — people / orgs / tools that matter this week.

What does NOT go in: historical context, archived projects, exhaustive lists. The cache is for *now*; the rest of the wiki holds *all*.

### Maintenance

The hot cache is the **most aggressively maintained** file in the wiki. nateherk's master prompt updates "two times a day." The cadence is:

- **Daily** — bump active focus and recent decisions; archive stale entries to the relevant project page or log.
- **Weekly** — full refresh; verify in-flight projects status; update open questions.

The maintenance discipline is what makes it work. A hot cache that doesn't get updated becomes a stale cache, which is worse than no cache.

### Where it sits in load order

In a read-mode session against the wiki, the suggested load order is:

1. **`CLAUDE.md`** — schema (one-time per session).
2. **`_hot.md`** — active state (cheap; informs whether the question is about *now* or *history*).
3. **`index.md`** — catalog (read if hot cache doesn't have what's needed).
4. **Drill into specific pages** as the question demands.

This order exploits the locality of most queries (most are about now) without sacrificing the ability to answer historical questions.

### Composition with the rest of the wiki

- **Hot cache is generated, not composed.** It should be re-derivable from the rest of the wiki (recent log entries + project current-focus sections + active-status pages). If you lose the hot cache, you can rebuild it.
- **Hot cache references, doesn't duplicate.** It should link to the canonical pages (project pages, concept pages) rather than restating their content. Stale duplication is the failure mode.
- **Hot cache changes belong in the log too.** When the hot cache moves on (a project completes, a decision lands), the log gets the entry; the hot cache just reflects current truth.

## Open questions and contradictions

- **Optimal token budget**: 500 tokens is one author's experience. The right size is probably a function of the wiki's total size and the query mix; an empty wiki doesn't need a hot cache, a 1,000-page wiki might want 1,500 tokens.
- **Auto-generation vs hand-curation**: nateherk hand-curates ("updates two times a day"). An auto-generated version (script that pulls last-7-days log entries + active-status project pages) is plausible but unmeasured.
- **Cache invalidation**: the classic problem. How does the agent know if the hot cache is stale? A `last_updated` timestamp + a freshness check at the top of the file is one answer.
- **Multi-context users**: a person with separate work / personal / hobby contexts may want multiple hot caches with selectors. Not addressed in the source.
- **The 95% token-reduction claim** is third-hand and unverified. Treat as an upper-bound directional signal, not a benchmark.

## Brain-applicability

This wiki (the brain) currently has **no hot cache**. With 123 wiki pages and growing, every read-mode query forces the agent to read CLAUDE.md + index.md + drill into specific pages. A hot cache at `~/brain/_hot.md` would:

- Reduce average read-mode query cost by some meaningful fraction.
- Surface "what's active right now" without requiring a maintainer-mode query against the log.
- Compose well with the existing slash commands (`/brain` could read `_hot.md` first).

Worth implementing as a follow-up. The maintenance discipline is the question — daily hand-curation is unlikely; an auto-generation pass during the weekly remote lint is more sustainable.

## Related concepts

- [[llm-wiki-pattern]] — the parent pattern; hot cache is an extension.
- [[progressive-disclosure]] — composes naturally; hot cache is L0.
- [[claude-code-overhead-patterns]] — addresses several patterns by reducing per-query crawl cost.
- [[lint]] — the wiki operation that should keep the hot cache fresh.
- [[ai-os-pattern]] — the broader operating model the hot cache participates in.

## Related entities

- [[wiki/entities/nateherk]] — author of the canonical source.
- [[wiki/entities/andrej-karpathy]] — author of the LLM Wiki pattern this concept extends.
- [[wiki/entities/obsidian]] — typical viewer for this kind of file.
- [[wiki/entities/hermes-agent]] — agent-internal alternative implementation; same goal, different mechanism.

## Mentioned in

- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/nousresearch-hermes-agent]]
