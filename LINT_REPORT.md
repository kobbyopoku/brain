# LINT_REPORT.md — Weekly Wiki Health Check
**Date**: 2026-07-22
**Run**: automated weekly lint pass
**Mechanical check**: `python3 bin/wiki_lint.py` — exit 0; 1054 files audited, 0 broken wikilinks, 0 orphan pages, 0 index drift, 0 frontmatter issues
**Auto-fixes applied**: 0 (all outstanding items require owner input)

---

## Resolved since last report (2026-07-13)

| ID | What | When fixed |
|---|---|---|
| 3 | **Helm GitHub org contradiction** — `wiki/projects/helm.md` "Repo Topology" section claimed `ROAM-Labs/` org; decision #19 said `godwin-roam`. Fixed in commit 79b4a98 (2026-07-22): `helpful-assistant-theater` concept filed + broken wikilink repaired + Repo Topology updated. | 2026-07-22 interactive lint |

---

## Items requiring human review

### 1 — Stale claim: Hermes Agent star count (5 pages)

**Severity**: medium — factual staleness across multiple pages

`wiki/entities/hermes-agent.md` records the corrected figure as:
> "23,000+ (early May 2026) → **150,000+ (mid-May 2026 per Shann Holmberg)**. 6× growth in ~2 weeks; verify against actual GitHub before relying."

Five pages still carry the old `23k+` figure without the update or caveat:

| File | Approximate location | Stale text |
|---|---|---|
| `wiki/syntheses/multi-agent-ops-platform-blueprint.md` | line ~62 | "23k+ stars" |
| `wiki/syntheses/helm-commercialization-paths.md` | line ~42 | "23k+ stars" |
| `wiki/entities/nous-research.md` | line ~24 | "23k+ stars" |
| `wiki/sources/nousresearch-hermes-agent.md` | lines ~118, 181 | "23,000+" |
| `wiki/projects/helm.md` | line ~413 | "23k+ stars" |

**Recommended action**: Update each occurrence to match the hermes-agent.md phrasing (150k+ figure + "per Shann Holmberg; verify before relying" caveat), or replace with a cross-reference to `[[wiki/entities/hermes-agent]]` rather than repeating the number.

---

### 2 — Stale project status: CPC RTBVD bid outcome unknown ⚠ TIME-SENSITIVE

**Severity**: high — planned go-live is **7 August 2026 (16 days away)**

`wiki/projects/cpc-rtbvd.md` was last updated **2026-05-09**. Its "Current focus" section reads:
> "Bid submitted; awaiting CPC award notification. If awarded, kickoff is **15 May 2026** for a 12-week build to go-live ~**7 August 2026**."

Today is 2026-07-22:
- Planned kickoff date (15 May 2026) has passed by **68 days**.
- Planned go-live date (7 August 2026) is **16 days away**.
- No award/rejection/delay update has been captured in the wiki.

**Recommended action**: Update `wiki/projects/cpc-rtbvd.md` with the actual outcome. If awarded and in active delivery, the page needs a near-complete rewrite to reflect the build phase. If rejected, change `status: archived`. This is now urgent — the planned delivery date is within the month.

---

### 3 — Re-clip backlog: 8 content-incomplete sources

**Severity**: low — tracked stubs; not defects

These 8 sources failed initial web retrieval (X.com 402 "Thread Not Found" or image-only capture):

| Source | Issue |
|---|---|
| `wiki/sources/*avichawla*` (×2) | X.com retrieval failed; url-only-stub |
| `wiki/sources/*cyrilxbt*` (1 of 3) | X.com retrieval failed; url-only-stub |
| `wiki/sources/*ashwingop*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*neil_xbt*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*kylejeong*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*bloggersarvesh*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/wizofecom*` | Image-only capture; text body not retrieved |

**Recommended action**: Desktop re-clip via Obsidian Web Clipper. No automated recovery — X.com requires authenticated session.

---

### 4 — Diagram staleness: godwin-portfolio.md ASCII org chart

**Severity**: low — tables in the file are correct; diagram is visual summary only

`wiki/syntheses/godwin-portfolio.md` ASCII org chart (the `┌──────────────┐` diagram) still shows only 4 ROAM Labs products (Vedge / Kivora / Clarvyn / _roamlabs). Missing: **Glydr**, **Africart**, **Helm**. The Bucket tables below the diagram were updated 2026-06-08 and are correct.

**Recommended action**: Redraw the ASCII diagram when the portfolio framing is next reviewed, or request explicitly.

---

### 5 — 94 raw sources queued but not yet ingested

**Severity**: medium — the backlog has grown substantially since the last ingest wave

As of the 2026-07-22 interactive lint pass, the log notes **94 raw sources** are queued in `raw/` with no corresponding `wiki/sources/` page. These were added in multiple `raw: queue …` commits between 2026-06-26 and 2026-07-22. Topics span graph/loop engineering, GTM, LLM-wiki patterns, company-OS, harness theory, second-brain, memory, software-craft, AI careers, markets/trading.

**Recommended action**: Schedule an ingest session. The backlog is large enough that a multi-cluster ingest (following the 2026-05-21 wave pattern) is the right approach — 8–12 sources per cluster, thematically grouped.

---

### 6 — 550 stubs aging; 207 created before 2026-05-10 (75+ days)

**Severity**: low — stubs are by-design; flagged for human judgment on which to expand or prune

207 stub pages were created before 2026-05-10 and have not been expanded. Most are Open Design aesthetic-style stubs (clean design archetypes like `brutalism`, `glassmorphism`) which are fine as stubs indefinitely. The candidates worth human review for expansion or deletion are those with **no inbound links from any non-index page** (i.e., orphan-ish stubs that only exist because of completionist coverage).

**Recommended action**: No immediate action required. At a future lint pass, consider running `bin/wiki_lint.py` with a filter for stubs older than 90 days with low cross-reference count, and make a batch keep/delete decision.

---

### 7 — Informational: Kivora AI model versions on Sonnet 4.5 / Haiku 4.5

**Severity**: informational — project-state fact; not a wiki error

`wiki/projects/kivora.md` records `claude-sonnet-4-5-20250929` and `claude-haiku-4-5-20251001`. Newer models (Sonnet 5, Opus 4.8) are available as of 2026-07. If Kivora has been upgraded, update the project page.

---

## Summary

| # | Category | Severity | Status | Action needed |
|---|---|---|---|---|
| 1 | Stale claim — Hermes stars (5 pages) | Medium | Open | Maintainer propagate hedged wording |
| 2 | Stale status — CPC RTBVD ⚠ | **High** | Open | **Owner** — go-live in 16 days |
| 3 | Helm GitHub org contradiction | Medium | **Resolved** 2026-07-22 | — |
| 4 | Re-clip backlog (8 sources) | Low | Open | Owner — desktop re-clip |
| 5 | godwin-portfolio ASCII diagram | Low | Open | Owner — redraw when reviewing |
| 6 | 94 raw sources un-ingested | Medium | Open | Schedule ingest session |
| 7 | 550 aging stubs | Low | Open | Future lint judgment call |
| 8 | Kivora model versions | Info | Open | Owner — check if upgraded |

---

*Lint ran: 2026-07-22. Mechanical tool: `bin/wiki_lint.py` (Exit 0, 1,054 files). Semantic pass: LLM maintainer (weekly routine).*
*Previous report: 2026-07-13 (6 items). Item #3 resolved in 2026-07-22 interactive pass (commit 79b4a98).*
