# LINT_REPORT.md — Weekly Wiki Health Check

**Date**: 2026-05-18  
**Tool run**: `python3 bin/wiki_lint.py` — exit 0 (0 broken wikilinks · 0 ambiguous · 0 orphans · 0 index drift · 0 frontmatter issues)  
**Automated result**: Clean.  
**Semantic pass**: 5 categories of issues requiring human judgment, documented below.  
**Auto-fixes applied**: 1 (index.md stats date corrected from 2026-05-11 → 2026-05-17, matching last git mtime of that file).

---

## 1. Potential Contradictions

### 1.1 DOE Framework — temporal ambiguity in evolution narrative
**File**: `wiki/concepts/do-framework.md` (lines 37–50, framing-evolution table)  
**Issue**: The concept page describes the DO framework as originating in "early-2026 course" (Saraev's 5h+ course) and having "evolved to DOE in late-2025 / 2026 follow-up content" (Bhandari blog + Mwathu LinkedIn). If "late-2025" precedes "early-2026", this inverts the described evolution — the DOE evolution would *predate* the original DO course.  
**Most likely interpretation**: "late-2025 / 2026" means "late 2025 or [early] 2026" — Bhandari's blog may have been published around the same time as or slightly after the course. The ambiguity is in the phrasing, not necessarily a real contradiction.  
**Proposed fix**: Clarify the table header for the DOE column — e.g., "DOE (Bhandari blog, circa 2026)" — or confirm the actual publication dates of Bhandari's post and Saraev's course to resolve the "late-2025" question. Until confirmed, the evolution description could be misleading.

---

## 2. Stale / Unverified Claims

### 2.1 "Anthropic silently lowered Claude Code's thinking effort" — unverified since 2026-05-09
**Files**: `wiki/sources/zodchiii-x-claude-code-settings.md`, `wiki/entities/boris-cherny.md`  
**Issue**: The zodchiii source opens with a load-bearing claim: *"Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026 — Boris Cherny confirmed this on Hacker News."* Both the source page and the boris-cherny stub explicitly flag this as unverified. The wiki has captured the claim with appropriate hedging, but the claim has been unverified for 9 days. If true, it's a significant operational recommendation for all Claude Code users in the wiki.  
**Proposed action**: Search for the Boris Cherny HN comment and verify (or disprove) the claim. If verified, upgrade boris-cherny from stub and remove the "unverified" qualifier. If disproved, add a `verification_result: false` note to the source page and update the entity stub.

### 2.2 Hermes Agent star count — stale external metric
**File**: `wiki/sources/nousresearch-hermes-agent.md`  
**Issue**: The source page claims "23k+ stars at v0.11.0" as of the 2026-05-05 ingest. The version has since advanced to v0.13.0 (verified 2026-05-10 per log). Star counts on actively-maintained projects move quickly.  
**Proposed action**: Low priority — external metric, not a claim the wiki relies on for reasoning. Mark as "as-of 2026-05-05" rather than a present-tense fact if it hasn't been so labeled already. Worth updating at the next Hermes ingest.

### 2.3 Helm "Week 1 build active" — status unclear
**File**: `index.md` (Projects → Active, Helm entry)  
**Issue**: The index.md says "scaffold 2026-05-09; Week 1 build active" for Helm. The last log entry for Helm is 2026-05-10 (Hermes pin cleared, blocker #2 — `ROAM-Labs/` GitHub org creation + first commits — still open). No log entry since 2026-05-10. It is unclear whether Week 1 has actually started or is still blocked.  
**Proposed action**: Run `/brain-update-project` on Helm. If Week 1 has not started, update index.md entry to "scaffold 2026-05-09; Week 1 pending — blocker: ROAM-Labs/ GitHub org" to avoid misleading future read-mode sessions. If it has started, update with progress.

### 2.4 Hermes Agent MCP support — flagged unverified, no resolution
**File**: `wiki/projects/helm.md` (Architecture decisions, Layer 3)  
**Issue**: The 2026-05-09 second-pass review (B.4) caveated the Hermes MCP support claim: *"⚠️ unverified — [[wiki/entities/hermes-agent]] entity page contains zero MCP mentions; verify before Week 1."* The entity page was updated on 2026-05-10 with distribution facts but the MCP support question was not resolved in that update.  
**Proposed action**: Check the Hermes v0.13.0 upstream for MCP support before Helm's Week 1 build. If unsupported, the helm.md Architecture decisions section for the helm-mcp service needs an adapter-layer note.

---

## 3. Stale Stubs Without Recovery Path

### 3.1 Three permanently deleted X-thread stubs
**Files**:  
- `wiki/sources/cyrilxbt-x-2052923836090167526.md`  
- `wiki/sources/ashwingop-x-2052777467732283817.md`  
- `wiki/sources/neil_xbt-x-2052733885906051118.md`  
**Issue**: All three were marked "Thread Not Found" on twitter-thread.com as of 2026-05-08. No alternative aggregator has surfaced the content. These are URL-only stubs with no recoverable body.  
**Proposed action**: Delete all three stub source pages and their corresponding stubs in entity pages:
- `cyrilxbt-x-2052923836090167526` → remove from `wiki/entities/cyrilxbt.md` "Mentioned in" section
- `ashwingop-x-2052777467732283817` → remove from `wiki/entities/ashwingop.md` "Mentioned in" section
- `neil_xbt-x-2052733885906051118` → remove from `wiki/entities/neil_xbt.md` "Mentioned in" section (and consider whether the neil_xbt entity stub itself has any value if this is its only mention)

Then remove from `index.md` "URL-only stubs (12)" subsection (those 3 entries) and update stats.  
**Note**: Keep as stubs if there's value in the backlink trail (e.g., the author has other content worth tracking). If the stubs are solely for the deleted thread, delete them.

### 3.2 Image-only stub — recovery pending
**File**: `wiki/sources/wizofecom-x-2045182674130837681.md`  
**Issue**: The body is in 3 Twitter media images that weren't OCR'd at time of capture (2026-05-09). Recovery path is "re-clip via Obsidian Web Clipper desktop with image OCR." This has been pending for 9 days.  
**Proposed action**: Either re-clip (if the images are still available) or, if recovery is not feasible, delete the stub source page. The wizofecom entity stub (`wiki/entities/wizofecom.md`) can remain if there's value in tracking the author.

---

## 4. Missing Pages — Multi-Mentioned Without Own Page

### 4.1 Brolly Africa — organization entity not created
**Mentioned in**: `CLAUDE.md` (Wiki owner section: *"Brolly Africa (entity to be added by Godwin separately)"*), `wiki/entities/godwin-opoku-duah.md`, `wiki/syntheses/godwin-portfolio.md`, `wiki/projects/brolly.md`, `wiki/projects/helm.md`, `wiki/projects/glydr.md`, `wiki/projects/asanti-brokers.md` (7+ pages)  
**Issue**: Brolly Africa is one of the two organizations Godwin runs, co-anchors two active projects (Brolly, Asanti Brokers), and is cross-referenced across the wiki. Despite the completionist-coverage policy, no entity page exists. The CLAUDE.md explicitly defers to Godwin to add it, but per policy a stub should be created from existing citable facts even before a primary source is ingested.  
**Proposed action**: Create `wiki/entities/brolly-africa.md` as a stub using only citable facts from existing wiki pages: co-founded by Godwin, Brolly (vehicle insurance platform) is its owned product, Asanti Brokers is its client work, operates in the African insurtech market (Ghana). Add to index.md under "Organizations — wiki owner's." Remove the deferred-note from CLAUDE.md (or keep it as a reminder for when a primary source is ingested).

### 4.2 Concept: `intra-class @Transactional silent no-op`
**Mentioned across**: `wiki/projects/glydr.md` (Phase 7x poller, Phase 7x-1 orchestrator, and a third instance noted in 2026-05-17 log — 3 examples total)  
**Evidence from log** (2026-05-16): *"intra-class @Transactional silent no-op (was glimpsed in 7x poller, now explicit in 7x-1 orchestrator)"*; (2026-05-17): *"intra-class @Transactional silent no-op (already noted yesterday — third example?)"*  
**Issue**: Three cross-phase examples of the same Java/Spring JPA footgun (intra-class method calls bypass Spring's AOP proxy, so `@Transactional` annotations have no effect). This is a well-known architectural invariant for Spring developers that the wiki currently buries in project-page lessons.  
**Proposed action**: Create `wiki/concepts/intra-class-transactional-noop.md` as a concept page under a new "Engineering patterns — JVM" subsection in the index. Cite Glydr as the worked example. Keep project-level lesson text as-is.

### 4.3 Concept: `vendor-sdk-artifact-pull`
**Mentioned across**: `wiki/projects/glydr.md` (Smile Identity in Phase 7x), future Brolly per-trip insurance API (predicted in 2026-05-16 log)  
**Evidence from log** (2026-05-16): *"worth promoting to a concept page (`vendor-sdk-artifact-pull`) when a second example lands (Brolly per-trip insurance API may qualify)"*  
**Issue**: The pattern — vendor SDK returns a verdict or event reference, and the consumer must separately pull the associated artifact (images, PDF, metadata) via a different API endpoint — is distinct and not obvious. Two examples documented.  
**Proposed action**: Create `wiki/concepts/vendor-sdk-artifact-pull.md`. Cite Smile Identity (Glydr Phase 7x) as the primary worked example. File under a new "Engineering patterns — integrations" subsection. Flag the Brolly insurance API as a candidate second example once integrated.

### 4.4 Concept: `parallel-agent enum/union drift`
**Mentioned across**: `wiki/projects/glydr.md` (Phase 7x SmileVerificationView nullability, Phase 7x-1 AuditAction union — both in 2026-05-16 log)  
**Evidence from log** (2026-05-16): *"parallel-agent type-contract drift (was Phase 7x's SmileVerificationView nullability, now Phase 7x-1's AuditAction union)"* — identified as "second-example" status.  
**Issue**: When multiple agents work in parallel on a shared type boundary (enum, union, or nullable field), they can produce conflicting type contracts that only manifest at integration time. Two examples in one day.  
**Proposed action**: Create `wiki/concepts/parallel-agent-type-drift.md`. Cite Glydr Phase 7x + 7x-1 as worked examples. File under "Agent architecture" or "Claude Code mechanisms" in the index. Could cross-cite the existing `[[wiki/concepts/multi-agent-orchestration]]` page.

### 4.5 Concept: `Flyway version collision`
**Mentioned across**: `wiki/projects/glydr.md` (V48 and V51 collisions both on 2026-05-17 log)  
**Evidence from log** (2026-05-17): *"Two Flyway version collisions today (V48 + V51) reinforce the existing `feedback_update_before_branching` rule — both happened when a branch went stale before merging."*  
**Issue**: The specific failure mode (stale branches accumulating schema migrations that conflict with the merged-main version sequence) is distinct and recurrent. Two confirmed examples.  
**Proposed action**: Create `wiki/concepts/flyway-version-collision.md`. Distinguish from the more general "Flyway migration discipline" — this is specifically about the branching-induced collision pattern. Cite Glydr as the worked example. The existing `feedback_update_before_branching` rule in Glydr's project auto-memory is the manual fix; this concept page generalizes the principle. File under "Engineering patterns — database" in the index.

---

## 5. Frontmatter / Staleness Flags

### 5.1 Vedge project — updated: 2026-05-09
**File**: `wiki/projects/vedge.md`  
**Issue**: The Vedge project page has `updated: 2026-05-09` — 9 days ago. No log entries indicate Vedge activity since then. If Vedge development has been in a pause, the page is current. If there has been active development, the brain page may not reflect it.  
**Proposed action**: Run `/brain-update-project` on Vedge to verify currency. If no significant changes, update the `updated:` date to today as part of the lint pass to signal the page was reviewed-and-confirmed-current.

---

## Auto-fixes Applied (this PR)

1. **`index.md` stats date corrected**: `last updated 2026-05-11` → `last updated 2026-05-17`  
   *Rationale*: Git confirms `index.md` was last modified in commit `1041482` (2026-05-17, Kivora Systems Inventory update). The stats line was 6 days stale.

---

## No Action Required

- **Automated lint**: 0 broken wikilinks, 0 ambiguous links, 0 orphan pages, 0 index drift entries, 0 frontmatter type/field issues. Exit 0.
- **222 stubs**: Stub count is high (222 of 300 entities) but consistent with the completionist-coverage policy. The design-catalog stubs (aesthetic-style entities) account for ~54 of these and are by design thin. Not flagged as a problem.
- **Ethical-flag stubs**: `wiki/sources/creatorpascal-x-2053034511726756159` carries `ethical_flag: true` — this is intentional per the established flagging convention (ingested as a negative example).
- **Glydr brand name working**: `name_confirmed: false` in Glydr frontmatter is an open question tracked as Q7 in the project page — not a lint failure.
- **Glydr/PRD divergence (in-Accra commute)**: Tracked as open question Q14 in `wiki/projects/glydr.md`. Known and documented.
