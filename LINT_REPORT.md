# LINT_REPORT.md — Weekly Wiki Health Check
**Date**: 2026-07-13
**Run**: automated weekly lint pass
**Mechanical check**: `python3 bin/wiki_lint.py` — exit 0; 1053 files audited, 0 broken wikilinks, 0 orphan pages, 0 index drift, 0 frontmatter issues
**Auto-fixes applied**: 1 (see § Auto-fixes below)

---

## Auto-fixes applied

| File | Change |
|---|---|
| `index.md` line 5 | Stats "last updated" date corrected: `2026-06-17` → `2026-07-13`; description updated to reflect this lint pass. The 2026-06-26 Helm update touched index.md (de-staling the Helm line) but did not advance the stats date — this was the true correction point. |

---

## Items requiring human review

### 1 — Stale claim: Hermes Agent star count (5 pages)

**Severity**: medium — factual staleness across multiple pages

`wiki/entities/hermes-agent.md` (updated 2026-06-06) records the corrected figure as:
> "23,000+ (early May 2026) → **150,000+ (mid-May 2026 per Shann Holmberg)**. 6× growth in ~2 weeks; verify against actual GitHub before relying."

Five pages still carry the old `23k+` figure without the update or caveat:

| File | Approximate location | Stale text |
|---|---|---|
| `wiki/syntheses/multi-agent-ops-platform-blueprint.md` | line ~62 | "23k+ stars" |
| `wiki/syntheses/helm-commercialization-paths.md` | line ~42 | "23k+ stars" |
| `wiki/entities/nous-research.md` | line ~24 | "23k+ stars" |
| `wiki/sources/nousresearch-hermes-agent.md` | lines ~118, 181 | "23,000+" |
| `wiki/projects/helm.md` | line ~413 | "23k+ stars" |

**Recommended action**: Update each occurrence to match the hermes-agent.md phrasing (150k+ figure + "per Shann Holmberg; verify before relying" caveat), or at minimum add a cross-reference note. The hermes-agent.md page already carries the authoritative hedged wording — the other pages just need to reference it rather than repeat the stale number. Not auto-fixed because the 150k+ figure itself carries a "verify before relying" caveat in the entity page; propagating it without that caveat could make the wiki less accurate, not more.

---

### 2 — Stale project status: CPC RTBVD bid outcome unknown

**Severity**: high — 60+ days past planned kickoff with no outcome captured

`wiki/projects/cpc-rtbvd.md` was last updated **2026-05-09**. Its "Current focus" section reads:
> "Bid submitted; awaiting CPC award notification. If awarded, kickoff is **15 May 2026** for a 12-week build to go-live ~**7 August 2026**."

Today is 2026-07-13:
- Planned kickoff date (15 May 2026) has passed by **59 days**.
- Planned go-live date (7 August 2026) is **25 days away**.
- No award/rejection/delay update has been captured in the wiki.

This is also listed under "Open questions" in the project page itself:
> "CPC bid award status — no update captured since 2026-05-09. Submission deadline was 8 April 2026; award decision timeline not in the brain."

**Recommended action**: Update `wiki/projects/cpc-rtbvd.md` with the actual outcome — awarded (and current delivery phase), rejected, or deferred. If the project was awarded and is in active delivery, the page needs a near-complete rewrite to reflect the build phase. Not auto-fixed — requires Godwin's input on actual outcome.

---

### 3 — Contradiction: Helm GitHub org (two claims in the same file)

**Severity**: medium — internal contradiction within `wiki/projects/helm.md`

`wiki/projects/helm.md` contains two conflicting statements about where the repos were pushed:

**Claim A** — "Repo Topology" section (written before 2026-06-26):
> "All 3 repos sit under the new `ROAM-Labs/` GitHub org"

**Claim B** — Architecture decision #19 (added 2026-06-26):
> Repos were pushed to `github.com/godwin-roam/*` (personal account, NOT the planned `ROAM-Labs/` org). Decision #19 explicitly revises the org plan.

Decision #19 is the most recent and authoritative statement; Claim A has not been updated to reflect it. The "Repo Topology" section still asserts the ROAM-Labs org when the repos actually live under `godwin-roam`.

**Recommended action**: Update the "Repo Topology → GitHub org" section to match decision #19 — replace `ROAM-Labs/` org reference with `godwin-roam/` personal account, noting the pivot reason (per decision #19: GitHub org creation deferred, pushed to personal account to unblock). Not auto-fixed — requires reading the full Helm page to identify the exact section/wording.

---

### 4 — Re-clip backlog: 8 content-incomplete sources (continuing from 2026-06-08 lint)

**Severity**: low — tracked, tagged stubs; not defects, but a known recovery queue

These 8 sources failed initial web retrieval (X.com 402 "Thread Not Found" or image-only ingest) and are correctly tagged `awaiting-content` or `partial-content` in their frontmatter. They represent the owner-side re-clip queue from the 2026-06-08 lint — no change in status since then.

| Source | Issue |
|---|---|
| `wiki/sources/*avichawla*` (×2) | X.com retrieval failed; url-only-stub |
| `wiki/sources/*cyrilxbt*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*ashwingop*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*neil_xbt*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*kylejeong*` | X.com retrieval failed; url-only-stub |
| `wiki/sources/*bloggersarvesh*` | X.com retrieval failed; url-only-stub |
| (1 image-only stub) | Image-only capture; text body not retrieved |

**Recommended action**: Desktop re-clip via Obsidian Web Clipper when convenient. No automated recovery path — X.com requires authenticated session. Surfaced again to keep this visible; no action needed immediately.

---

### 5 — Diagram staleness: godwin-portfolio.md ASCII org chart incomplete

**Severity**: low — visual summary only, not a content defect; tables below the diagram are correct

`wiki/syntheses/godwin-portfolio.md` was updated 2026-06-08 to add Glydr and Africart to the Bucket 1 product table (12 projects total, correctly mapped). However, the **ASCII org chart** at the top of the file (the `┌──────────────┐` diagram) still shows only 4 ROAM Labs owned products:
> `Vedge / Kivora / Clarvyn / _roamlabs (self)`

Missing from the diagram: **Glydr**, **Africart** (both added to Bucket 1 table in 2026-06-08 refresh), and **Helm** (Bucket 5, listed in table below but absent from top-level ownership tree).

The 2026-06-08 refresh-log entry explicitly notes: "Full Bucket-1 table rows for Glydr/Africart left for owner refresh (or on request)" — so this was a known deferred item, not an oversight.

**Recommended action**: Owner to refresh the ASCII diagram when the portfolio framing is next updated. Alternatively, request the diagram update explicitly and a maintainer will redraw it. Not auto-fixed — the diagram is considered owner's framing territory.

---

### 6 — Informational: Kivora AI model versions on Sonnet 4.5 / Haiku 4.5

**Severity**: informational — factual project-state record; not necessarily a defect

`wiki/projects/kivora.md` records:
> `"AI models": claude-sonnet-4-5-20250929, claude-haiku-4-5-20251001`

As of 2026-07-13, newer models are available (Sonnet 5, Opus 4.8, Haiku 4.5 final). This is a **project-state fact**, not a wiki error — if the Kivora codebase currently runs on Sonnet 4.5 / Haiku 4.5, the wiki is accurate. Surfaced here only because a future update session might want to capture any model upgrades.

**Recommended action**: If Kivora has been upgraded to newer models, update the project page. If the models haven't changed, no action needed.

---

## Summary

| # | Category | Severity | Action needed |
|---|---|---|---|
| 1 | Stale claim — Hermes stars (5 pages) | Medium | Owner/maintainer update |
| 2 | Stale status — CPC RTBVD bid outcome | High | Owner input on actual outcome |
| 3 | Contradiction — Helm GitHub org | Medium | Maintainer edit (decision #19 is authoritative) |
| 4 | Re-clip backlog — 8 url-only stubs | Low | Owner desktop re-clip |
| 5 | Diagram staleness — portfolio ASCII chart | Low | Owner refresh on request |
| 6 | Informational — Kivora model versions | Info | Update if models upgraded |
