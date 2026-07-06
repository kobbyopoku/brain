# LINT_REPORT.md — Weekly Wiki Health Check
**Date**: 2026-07-06  
**Script exit code**: 0 (clean — 0 broken links, 0 ambiguous links, 0 orphans, 0 index drift, 0 frontmatter issues across 1,053 files)  
**Auto-fixes applied**: 1 (see below)  
**Items needing human review**: 7 (below)

---

## Auto-fixes applied

| File | Change |
|---|---|
| `index.md` line 5 | Stats "last updated" corrected from `2026-06-17` to `2026-06-26` — the 2026-06-26 Helm update (`update-project | Helm`) was logged and applied to the index Helm entry but the header stats line was not bumped. |

---

## Items flagged — human review required

Items are organized by category, most-actionable first.

---

### 1. Stale / contradicted content in `wiki/projects/helm.md`

The 2026-06-26 Helm update added Decision #19 (repos at `godwin-roam`, not `ROAM-Labs`) and a revised current-focus block, but several earlier sections were **not cleaned up**. Three sub-items:

#### 1a. "GitHub org" subsection still names the wrong org
- **File**: `wiki/projects/helm.md:123–125`
- **Section**: `### GitHub org`
- **Current text**: *"All 3 repos sit under the new **`ROAM-Labs/`** GitHub org (per Q2 resolution 2026-05-09). Org to be created when Week 1 build starts. Naming convention: `ROAM-Labs/helm-<service>`…"*
- **Why it's wrong**: Decision #19 (2026-06-26) establishes that repos are at `github.com/godwin-roam/*`, not `ROAM-Labs`. An agent reading this section would act on stale information.
- **Recommended fix**: Replace or annotate the section with the decision-#19 resolution. Example: add `> ⚠ Superseded by decision #19 (2026-06-26): repos at github.com/godwin-roam/{helm-backend,helm-portal,helm-mcp,helm-docs}. ROAM-Labs org was inaccessible.`

#### 1b. Immediate execution blocker #2 was never marked resolved
- **File**: `wiki/projects/helm.md:73`
- **Current text**: `2. ROAM-Labs/ GitHub org not created; sub-repos have no remotes (and no first commits yet).`
- **Why it's wrong**: This blocker is resolved — repos were pushed to `godwin-roam` on 2026-06-26. Blocker #1 was struck through (`~~...~~`) when resolved (2026-05-10); blocker #2 was not.
- **Recommended fix**: Strike through item #2 and annotate with decision #19 resolution date, matching the style of item #1.

#### 1c. "Proposed split (3 repos)" — now 4 repos
- **File**: `wiki/projects/helm.md:79–105` (section header and "Why 3 repos" table)
- **Current text**: Section is titled `### Proposed split (3 repos + wrapper)` and the decision table shows `3 repos ✅ Chosen`.
- **Why it's wrong**: Frontmatter and current-focus (both updated 2026-06-26) show 4 repos: `helm-backend`, `helm-portal`, `helm-mcp`, `helm-docs`. `helm-docs` was added and does not appear in the original proposed split.
- **Recommended fix**: Update section title to "4 repos + wrapper" and note when/why `helm-docs` was added.

#### 1d. Open Questions Q2 table row — wrong resolution
- **File**: `wiki/projects/helm.md:385`
- **Current text**: `| 2 | **Repo location** | ✅ **New `ROAM-Labs/` GitHub org**.… |`
- **Why it's wrong**: Decision #19 overrides Q2 — the resolution was `godwin-roam`, not `ROAM-Labs`. The table still shows the superseded resolution.
- **Recommended fix**: Update Q2 resolution text to reference decision #19 and the actual outcome (`godwin-roam`).

---

### 2. Stale current-focus on active project pages

Two active projects have brain pages that haven't been updated in more than 6 weeks. Current-focus sections are likely out of date.

| File | `updated:` date | Current focus as written | Age |
|---|---|---|---|
| `wiki/projects/vedge.md` | 2026-05-09 | "Week of 2026-05-02" — billing audit, walk-in invoice, aging widget | ~8 weeks stale |
| `wiki/projects/glydr.md` | 2026-05-17 | Phase-2 wiring complete; KYC flow, control-center, landing waitlist | ~7 weeks stale |

**Note**: These are owner-update tasks — the brain cannot infer what's changed without surveying the project repositories. Recommend running `/brain-update-project` from inside each project directory.

---

### 3. Missing entity — Brolly Africa

- **Expected file**: `wiki/entities/brolly-africa.md`
- **Status**: Does not exist.
- **Where it's called out**: 
  - `CLAUDE.md` §Wiki owner: *"Brolly Africa *(entity to be added by Godwin separately)*"*
  - `wiki/projects/asanti-brokers.md:18`: *"Brolly Africa entity to be added separately by Godwin."*
  - `wiki/syntheses/godwin-portfolio.md:134`: *"Brolly Africa entity — pending creation by Godwin."*
- **Why not auto-fixed**: This requires owner-supplied facts (founding date, co-founders, registration, product scope). The brain should not fabricate entity content.
- **Recommended action**: Create `wiki/entities/brolly-africa.md` using `templates/entity.md`, with `entity_type: organization`. Core facts to populate: co-founders, founding date/country, mission, relationship to Brolly platform and Asanti Brokers. Link back from `wiki/projects/brolly.md` and `wiki/projects/asanti-brokers.md`.

---

### 4. Unverified claim — Hermes Agent GitHub stars

- **File**: `wiki/entities/hermes-agent.md:14` and `wiki/sources/nousresearch-hermes-agent.md:181`
- **Discrepancy**: The source page (ingested 2026-05-05) records **23k+ stars**; the entity page (updated post-Shann-Holmberg ingest) records **150,000+ stars** with an inline note *"verify before relying; this is a 6× jump from earlier 23k+ figure"*.
- **Status**: Already tracked and flagged within the entity page; no new action needed unless precision matters.
- **Recommended action**: If Hermes Agent figures appear in any deliverable or pitch, verify the current GitHub star count directly. The discrepancy in the wiki is correctly flagged and not a wiki defect.

---

### 5. Stale re-clip backlog (inherited — no new items)

8 sources remain with partial or URL-only content because X.com returns HTTP 402 to bot fetches. These are correctly tagged and tracked. Unchanged from the 2026-06-08 lint pass. Recovery requires desktop Obsidian Web Clipper re-clip. No action needed in this cycle.

| Source slug | Status |
|---|---|
| `_avichawla-x-2052326975034048754` | awaiting-content |
| `_avichawla-x-2053049489963811135` | awaiting-content |
| `cyrilxbt-x-2052923836090167526` | awaiting-content |
| `ashwingop-x-2052777467732283817` | url-only-stub |
| `neil_xbt-x-2052733885906051118` | url-only-stub |
| `kylejeong-x-2052103973377867913` | awaiting-content |
| `bloggersarvesh-x-2032130279494853118` | awaiting-content |
| `wizofecom-x-2045182674130837681` | image-only-stub |

---

## Summary

| Category | Count | Auto-fixed | Needs human review |
|---|---|---|---|
| Index stats drift | 1 | ✅ | — |
| Stale sections in Helm page | 4 sub-items | — | ✅ |
| Stale project current-focus | 2 pages | — | ✅ owner-update |
| Missing entity (Brolly Africa) | 1 | — | ✅ owner-gated |
| Unverified star count | 1 (tracked) | — | low priority |
| Re-clip backlog | 8 (inherited) | — | owner-side only |

The wiki's mechanical health is excellent: the lint script reports 0 broken links, 0 orphans, and 0 frontmatter issues across 1,053 pages. All issues in this report are semantic — stale prose, a missing entity, and residual historical sections not cleaned up after a project update.
