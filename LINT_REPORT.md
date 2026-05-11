# LINT_REPORT.md — Weekly Wiki Health Check
**Lint date**: 2026-05-11
**Tool pass**: `python3 bin/wiki_lint.py` — exit 0, 0 mechanical issues across 454 wiki pages.
**LLM semantic pass**: conducted manually against all project pages, key concept pages, source pages, syntheses, and the index.

---

## Auto-fixes applied (no human action needed)

| File | Fix |
|---|---|
| `wiki/projects/helm.md` | `updated:` corrected `2026-05-09 → 2026-05-10` to match git mtime (commit `c0967dd` on 2026-05-10). **Note**: the 2026-05-10 log entry explicitly says *"Helm `updated:` not bumped — the project page change is a status flip, not a structural addition."* The fix applies the schema rule literally (`Always update updated: when you modify a page`). Revert to `2026-05-09` if you prefer the lighter-weight policy documented in the log. |
| `index.md` | Stats line `last updated 2026-05-09 → 2026-05-10` to reflect the most recent operation date. |

---

## Items requiring human judgment

### 1. Stale version claim — source page vs entity page (Contradiction)

**File**: `wiki/sources/nousresearch-hermes-agent.md` (line 16)
**Claim**: *"currently at v0.11.0 (May 2026)"*
**Contradicts**: `wiki/entities/hermes-agent.md` (updated 2026-05-10) which records v0.13.0 as the verified current version.

The source page is a snapshot-at-ingest (2026-05-05) and the "currently" language is now stale. The entity page is the live authority on the version. Consider annotating the source-page TL;DR with a note like: *"Version at ingest: v0.11.0; current verified version v0.13.0 as of 2026-05-10 — see [[wiki/entities/hermes-agent]]."*

---

### 2. Stale "proposed" language in index.md — Helm entry (Index drift / stale claim)

**File**: `index.md` (line 681)
**Claim**: `multi-repo wrapper (proposed ROAM-Labs/{helm-backend, helm-portal, helm-mcp} — Clarvyn-style topology)`
**Reality**: Per `wiki/projects/helm.md` (§ Current Focus, updated 2026-05-09), all three sub-repos were materialized that same day: *"All three sub-repos exist at `/Users/kobbyopoku/ROAM/CascadeProjects/helm/`."* The word "proposed" is no longer accurate.

Suggested replacement: remove "proposed" and write `multi-repo wrapper (ROAM-Labs/{helm-backend, helm-portal, helm-mcp} — Clarvyn-style topology; scaffold materialized 2026-05-09)`.

---

### 3. URL-only stub section outdated — 7 of 12 sources now substantive (Index drift)

**File**: `index.md` — section `### X-thread batch ingest (2026-05-08)` → `**URL-only stubs (12)**`
**Issue**: The section header and entry grouping label 12 sources as URL-only stubs. Seven have since been upgraded to `content_status: substantive` by the Web-Clipper batch ingests:

| Source file | content_status (now) |
|---|---|
| `wiki/sources/jaynitx-x-2052734499319091384.md` | `substantive` |
| `wiki/sources/rohit4verse-x-2050968031493550202.md` | `substantive` |
| `wiki/sources/zodchiii-x-2052368125480354000.md` | `substantive` |
| `wiki/sources/cyrilxbt-x-2052235121416188114.md` | `substantive` |
| `wiki/sources/creatorpascal-x-2053034511726756159.md` | `substantive` |
| `wiki/sources/itsalexvacca-x-2052740083820958072.md` | `substantive` |
| `wiki/sources/noisyb0y1-x-2044692412061425748.md` | `substantive` |

**Still URL-only**: `cyrilxbt-x-2052923836090167526`, `ashwingop-x-2052777467732283817`, `neil_xbt-x-2052733885906051118` (3 of 12 remain stubs).

The index batch-section narrative is historical and describes what the batch was at creation time. You may want to either:
- Leave the section as historical record and add a parenthetical `(7 of 12 now upgraded via Web-Clipper; see batch #1 and #2 sections)`.
- Or restructure the batch section to move the 7 upgraded entries into the Web-Clipper batch #2 section alongside the other upgrades.

The source pages themselves are correct; only the index narrative is misleading.

---

### 4. Missing entity: `wiki/entities/brolly-africa.md` (Missing page)

**Referenced by**: CLAUDE.md (wiki owner section), `wiki/projects/brolly.md`, `wiki/projects/asanti-brokers.md`, `wiki/entities/godwin-opoku-duah.md`, `wiki/syntheses/godwin-portfolio.md`, and 14+ other pages — all as plain text (no wikilink, so the tool pass doesn't flag broken links).

**Context**: CLAUDE.md explicitly notes *"Brolly Africa (entity to be added by Godwin separately)"*, so this is intentionally deferred. However, 19 text references currently have no resolvable entity. When Godwin adds this entry, backlinks across all those pages would benefit from being converted to wikilinks.

**Suggested stub**:
- `wiki/entities/brolly-africa.md` with `entity_type: organization`, `tags: [stub, organization, africa, insurtech]`
- One-line framing: *"Co-founded by Godwin Opoku Duah; parent organization of the Brolly Africa insurtech platform ([[wiki/projects/brolly]]) and Brolly Africa client work ([[wiki/projects/asanti-brokers]])."*

---

### 5. `wiki/projects/README.md` example filename inconsistency (Minor)

**File**: `wiki/projects/README.md` (line 11)
**Text**: `"vedge.md", "kivora.md", "stace-sprouts.md"`
**Reality**: The actual project file is `wiki/projects/stacesprouts.md` (no hyphen).

This is a low-impact inconsistency in a directory-level README (not a wiki page). Fix if you want the README to serve as accurate documentation; skip if the README is informal.

---

### 6. Unverified claim — Claude Code thinking-effort reduction (Potentially stale)

**File**: `wiki/sources/zodchiii-x-claude-code-settings.md`
**Claim**: *"Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026"* — attributed to Boris Cherny on HN; already flagged `unverified` in the source page.

8 weeks have passed since the alleged event (March 2026). If this was a real, documented change, a primary source (Anthropic release notes, Boris Cherny's HN comment) should be findable and ingested. If not confirmable, consider annotating the claim as *"unverified as of 2026-05-11; ingest Boris Cherny's HN comment or Anthropic release notes to confirm or retract."*

---

### 7. Helm open question — Hermes Agent MCP protocol support unverified (Project risk)

**File**: `wiki/projects/helm.md` — Tool-calling reliability rubric, Step 1 (line 222)
**Text**: *"Hermes Agent's native MCP support is unverified in the wiki … Verify against the upstream Hermes repo before Week 1."*
**Status**: This open question persists after the 2026-05-10 update (which only resolved the pypi/version blocker). The `wiki/entities/hermes-agent.md` entity page does not confirm MCP-protocol support.

This is not a lint error — it's a documented project risk and has a clear action: verify the Hermes Agent repo's `AGENTS.md` / `tools/` directory for MCP adapter presence before starting Week 1 build. If Hermes lacks native MCP, the build plan needs an adapter layer added. Flag for pre-build checklist.

---

## Stubs aging report

The wiki currently has **222 stub pages** (out of 454 total). All stubs were created between 2026-05-02 and 2026-05-09 — a window of 9 days. Per schema convention, stubs are candidates for expansion or deletion only after *a long period*. No action warranted at this time; revisit at the next lint pass if the wiki has not grown since.

---

## Clean areas (no issues found)

- Broken wikilinks: **0** (tool-verified across all 454 pages)
- Ambiguous wikilinks: **0**
- Orphan pages: **0**
- Frontmatter required-field coverage: **100%**
- Source / entity / concept / project / synthesis page counts match `index.md` stats exactly (90 / 300 / 48 / 10 / 6)
- DO ↔ DOE framework naming: consistent across all concept and source pages (canonical name is DOE; alias resolves `[[do-framework]]` correctly)
- Wild-citation count for `llm-wiki-pattern`: 4 citations consistently documented across `index.md`, `wiki/concepts/llm-wiki-pattern.md`, and all four source pages
- Project affiliation frontmatter: all 10 project pages carry valid `affiliation:` values per schema
