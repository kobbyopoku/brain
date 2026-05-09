---
type: project
title: CPC RTBVD
created: 2026-05-09
updated: 2026-05-09
status: active
repo: local-only (no remote, no commits — working directory at /Users/kobbyopoku/Projects/CPC_RTBVD)
local_path: /Users/kobbyopoku/Projects/CPC_RTBVD
stack: [react-19, typescript-5.9, vite-rolldown, tailwind-v4, recharts-3, react-router-7, lucide-react, java-24, spring-boot-3, postgresql-15, redis, kafka, azure-aks, python-docx, pymupdf]
started: 2025-10-10
owner_org: roam-labs
prime_contractor: softtech-solutions
end_client: Cocoa Processing Company Plc (CPC)
affiliation: softtech-subcontract
aliases: [cpc-dashboard, cocoapro-ghana, cpc-real-time-dashboard, cpc-rtbvd-bid]
tags: [project, dashboard, bid, qcbs, ppa, ghana, cocoa, react-19, spring-boot, frontend-first, softtech-solutions]
---

> **Lineage**: government engagement. **[[wiki/entities/softtech-solutions|SoftTech Solutions]] is the prime contractor** holding the relationship with the end client (Cocoa Processing Company Plc / CPC); **[[wiki/entities/roam-labs|ROAM Labs]] is the subcontractor** delivering the technical build. [[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]] is named PM/CTO Key Expert in the QCBS bid response (CPC/PRO/CS/1/26).

# CPC RTBVD

> Bid-stage React 19 dashboard prototype + accompanying RFP submission package for the Cocoa Processing Company Plc (CPC) "Real-Time Business Visibility Operational Management Dashboard" tender — competing as SoftTech Solutions Limited under PPA QCBS rules for a GHS 2.98M, 12-week build.

## What and why

CPC RTBVD is the bid-and-build workspace for SoftTech Solutions' response to the Cocoa Processing Company tender RFP CPC/PRO/CS/1/26 (issued 10 March 2026, submission deadline 8 April 2026). The dashboard itself is a **100%-complete React 19 frontend prototype** rendering 11 mock-data pages across 5 operational domains: Sales & Revenue Monitoring, Production & Processing Monitoring, Stock & Inventory Management, Branch/Warehouse/Depot Operations, and Executive Dashboard & Reporting. The completed frontend is the strategic pivot that makes the 12-week timeline credible at proposal stage — backend microservices, Azure infrastructure, AI-assisted analytics, and integration with CPC operational systems are scoped to the contract delivery phase.

The repo also houses the QCBS bid package (Forms 3A through 3I + Forms 4A through 4E), a 15k-word Technical Specifications addendum, an 87KB Technical Team PRD with 50 user stories and a sprint plan, and a parallel CMC (Cocoa Marketing Company) business proposal for downstream integration work. It's structured as a parallel solo-bid + delivery readiness workspace: if the award lands, the team and tech direction are pre-locked.

## Stack and infrastructure

- **Frontend (`portal/`)**: React 19.1, TypeScript 5.9, Vite 7.1 (`npm:rolldown-vite@7.1.14` override — Rolldown bundler, not Rollup), Tailwind CSS 4 (`@tailwindcss/postcss` + `@import "tailwindcss"` syntax), Recharts 3.2, React Router 7.9, Lucide React. 11 pages: Overview, Production, QualityControl, Inventory, Orders, Branches, Warehouses, SupplyChain, Workforce, Reports, Settings. 4 shared components: KPICard, AlertPanel, StockGauge, Layout. Mock-data driven via `data/mockData.ts` simulating 30 days of sales (4 product types × 4 regions), per-plant production efficiency, auto-updating stock (5s refresh), 4 branches, 4 warehouses with GPS coordinates, priority-based alerts. Cocoa Brown (`#7f6356`) + Gold (`#f59e0b`) + Forest Green (`#22c55e`) palette.
- **Backend (`backend/`)**: empty placeholder. Proposed: Java 24 + Spring Boot 3.x microservices — 6 core (production / inventory / sales / branch / warehouse / analytics) + 4 supporting (notification / report / scheduler / audit) + Spring Cloud Gateway + auth-service. PostgreSQL 15 primary + Redis cache + Apache Kafka (or Azure Event Hubs with Kafka API) event bus.
- **Agent (`agent/`)**: empty placeholder. AI/ML analytics module (Prophet forecasting, anomaly detection, NL executive briefings via Claude Sonnet) envisioned for Phase 3 of the build, primarily for the parallel CMC proposal.
- **Cloud (proposed)**: Microsoft Azure — AKS cluster, Azure Database for PostgreSQL Flexible Server, Azure Cache for Redis, Azure Event Hubs, Azure Blob Storage, Azure CDN, Azure Key Vault, Azure Monitor + App Insights, Application Gateway with WAF. Estimated infra ≈ $1,312/month.
- **Docs (`docs/`)**: bid-artifact factory. Six Python build scripts (`build_*.py`) generate every DOCX deliverable from typed Python data structures with assertion-based consistency checks. Outputs land in `docs/proposals/`. Includes [`TECHNICAL-TEAM-PRD.md`](file:///Users/kobbyopoku/Projects/CPC_RTBVD/docs/TECHNICAL-TEAM-PRD.md) (87KB, 19 sections, 50 user stories with Gherkin acceptance criteria, 11×11 RACI matrix, 6-sprint plan) and [`TECHNICAL-SPECIFICATIONS.md`](file:///Users/kobbyopoku/Projects/CPC_RTBVD/docs/TECHNICAL-SPECIFICATIONS.md) (129KB, 17 sections, full PostgreSQL DDL for 22 tables across 7 schemas, OpenAPI specs for 7 services, Kubernetes YAML, Kafka topic catalog, Spring SecurityConfig).
- **Diagrams (`docs/diagrams/`)**: 14 custom HTML/CSS-rendered architecture diagrams (deliberately *not* Mermaid — see decisions below). Screenshotted via Playwright at 1400px viewport for print-quality clarity. Covers system architecture (8 layers), microservices topology (3 columns + API gateway), Kafka events (producer→topic→consumer), ER diagram (7 entity groups), real-time data flow (sequence), auth flow (sequence), Azure infrastructure (nested), CI/CD pipeline, 12-week dev roadmap (custom CSS Gantt). Plus 4 CMC-proposal diagrams (solution architecture, integration data flow, AI projections architecture, project timeline).
- **Auto-memory (`.remember/`)**: standard `now.md` + `today-YYYY-MM-DD.md` + `logs/` + `tmp/` pattern. Latest log (2026-05-09): *"Finalized CPC RFP docs: Tech Proposal (10 diagrams; 4 staff CVs: Godwin/Lilian/Richmond/Christian; CPC forms 3A-3I), Fin'l Proposal (GHS 2.98M firm no-VAT; Act 6 merged dev; no training/maintenance scope), response letter, Team PRD (87KB), Tech Specs (129KB); deadline 8 Apr 2026."*
- **Repo state**: git initialized but **no commits and no remote**. All work lives as untracked working files. Intentional — the bid contains commercially sensitive pricing and team data for an unawarded contract; not pushed pending award.

## Current focus

Bid submitted; awaiting CPC award notification. If awarded, kickoff is **15 May 2026** for a 12-week build to go-live ~**7 August 2026**.

- **Locked deliverables (financial)**: GHS 2,980,000 firm all-inclusive lump sum. No VAT chargeable. No training, no post-deployment maintenance — handover model only. CPC owns the system after acceptance. Payment 15% / 50% / 35% across 3 milestones.
- **Locked team (Key Staff, named on Form 3G CVs)**: Godwin Opoku Duah (CTO of SoftTech) → Project Manager / Business Systems Analyst (12 wks FT); Lilian Boyele → Data Engineer / Database Specialist (10 wks); Richmond Duah (ex-PwC Ghana → PwC USA, currently consulting for Datavant) → Data Analyst / BI Specialist (10 wks); Christian Osei-Bonsu (Head of Customer Ops, ex-MEST, Obama Foundation Leaders: Africa 2018) → Dashboard Developer / UI-UX Specialist (10 wks).
- **Locked team (Non-Key, named)**: Francis Adjei → Software Engineer (Frontend, 8 wks); Keynes Endjowoh → Software Engineer (Backend, 8 wks). Plus six unnamed TBD roles (Senior Backend Engineer, UI/UX Designer, QA Engineer ISTQB, DevOps Engineer Azure/AWS, Business Analyst, Technical Writer) totalling 32 staff-weeks.
- **Total contracted effort**: 90 staff-weeks across 12 weeks calendar (4 Key + 8 Non-Key).
- **Parallel track**: CMC (Cocoa Marketing Company) business proposal at `docs/proposals/CMC-BUSINESS-PROPOSAL.md` for downstream integration work (CPC ↔ CMC data bridge, AI projections layer). Active but contingent on CPC outcome.

## Architecture decisions

- **2025-10-10** — **Frontend-first strategic bet.** Built the React 19 prototype before the bid was issued, on spec. Rationale: a working dashboard demo beats a slide deck during sales conversations and pre-bid stakeholder workshops; if awarded, the prototype collapses 4+ weeks off the build; if not, it's reusable as a CocoaPro Ghana demo for other cocoa processors. Made the 12-week TOR timeline defensible at proposal stage.
- **2026-04-01** — **12-week timeline accepted as-is from CPC TOR**, compressed from initial 21-week design. Justified in Form 3D (Comments on TOR) by citing the completed frontend prototype as the time-saver. The five-phase compression: Inception (W1-2), Design (W3-4), Core Dev (W5-9), Testing & UAT (W10-11), Deployment & Handover (W12).
- **2026-04-01** — **All bid documents authored as Python build scripts** (`build_cmc_proposal.py`, `build_financial_proposal.py`, `build_rfp_response_letter.py`, `build_technical_proposal.py`, plus PDF builders). Every dollar figure, staff name, timeline date, and form line is in one editable Python source. Assertion-based consistency checks (`assert TOTAL_ALL == TOTAL_AMOUNT`, `assert _reimb_total == TOTAL_REIMBURSABLES`) fail loudly if any sum drifts — internal consistency verified at build time, not by an evaluator finding a typo. Output: standardized DOCX into `docs/proposals/`.
- **2026-04-10** — **Custom HTML/CSS for all architecture diagrams; Mermaid retired.** Mermaid sequence diagrams cropped, gantt charts squished, `\n` literals leaked into node labels. Replaced with hand-written HTML/CSS rendered at fixed 1400px viewport, screenshotted via Playwright. Each diagram is colour-coded, gold-bordered (`#C9A84C` accent), navy-headed (`#1C3557`), and reads cleanly in a printed PDF. Also produced an exportable 12-week Gantt with milestone diamonds. Same approach applied to the four CMC-proposal diagrams.
- **2026-04-14** — **GHS 2,980,000 firm all-inclusive — VAT removed entirely.** Reframed from "subtotal + 15% VAT = inclusive total" to a single firm price. Disclaimers added: *"No additional taxes, duties, or levies (including VAT) are chargeable."* Rationale: government parastatal procurement often has VAT exemption clauses; firm pricing protects against finance-team disputes at invoice time.
- **2026-05-09** — **Activity 6 (post-deployment maintenance) and training scope removed; costs merged into Activity 3 (Core Development).** Total stays at GHS 2.98M; the development phase becomes more premium. Rationale: handover model — CPC takes ownership post-acceptance, no ongoing dependency on SoftTech. Removed the entire "Optional Annual Maintenance (Year 2+)" section, removed Training Materials & Venue from reimbursables (39k merged into Activity 3 remuneration), renamed Activity 5 "Deployment, Training & Handover" → "Deployment & Handover". Staff-weeks now align exactly with Technical Proposal Form 3I (90 staff-weeks, no maintenance surplus).
- **2026-05-09** — **Address & cover-letter signatory standardised across both proposals.** Office address: *"Gamel Abdul Naser Ave, Accra, Ghana"* (was placeholder *"P.O. Box CT 1234, Cantonments"*). Form 4A cover signatory: *"Godwin Opoku Duah, Chief Technology Officer"*. Form 4A addressee: *"The Managing Director"* (replaced *"Prof. William Coffie, MD"* — generic role-based, decouples the bid from any one named person at CPC).

## Open questions

- **Repo remote** — push to a private GitHub remote, or stay local-only until award? Other Ghana-portfolio projects (StaceSprouts, Vedge, Kivora) all have GitHub remotes; CPC RTBVD is the outlier. Sensitivity argument cuts both ways: bid pricing/team is private but a single-machine working tree is also a single point of failure.
- **Backend & agent directories empty** — confirm these are placeholders for post-award work, not stubs to clear. The Technical Specifications doc has DDL + API contracts ready to scaffold from on day-1 of award.
- **CMC parallel proposal** — still active (per `docs/proposals/CMC-BUSINESS-PROPOSAL.md`), or shelved pending CPC outcome? CMC was a separate sales conversation; their Business Proposal is independent of the CPC RFP response.
- **CPC bid award status** — no update captured since 2026-05-09. Submission deadline was 8 April 2026; award decision timeline not in the brain.
- **Frontend-first reusability** — if CPC doesn't award, what's the second-best home for the 11-page React prototype? Direct-to-other-processor sales? Open-source it as a CocoaPro template?
- **Statutory attachments still pending** — Business Registration Cert, SSNIT Clearance, Tax Clearance (GRA), PPA Registration Cert. These are physical-doc deliverables to attach to the printed bid; status not tracked in this workspace.

## Lessons learned

Project-specific; promote to `wiki/concepts/` if a pattern recurs across other bids.

- **Frontend-as-bid-artifact compresses procurement timelines.** A working clickable demo collapses architecture-defence and credibility questions in stakeholder workshops; the time-saving carries forward into the build phase. Worth the upfront investment when the procurement is deterministic (named shortlist of consultants, clear evaluation criteria).
- **Python-as-bid-templating beats Word-and-find-replace.** Generating DOCX via `python-docx` from typed data structures means changing the lump sum from GHS 1.6M → 2.98M is one constant edit, not a 47-cell hunt across Forms 4A/4B/4C/4D/4E/payment-schedule/cover-letter/disclaimers. Assertions like `assert sum(activity_subtotals) == TOTAL_AMOUNT` catch the kind of mid-document arithmetic drift that disqualifies bids.
- **Mermaid is fine for code review, not for printed bids.** Sequence diagrams crop, gantts squish, `\n` literals leak. Custom HTML/CSS at fixed viewport + Playwright screenshot gives publication-grade output and full layout control. Same Playwright HTTP-server pattern (`python3 -m http.server`) applies for both CPC and CMC diagrams.
- **Bid forms are checklists, not narratives.** Ghana PPA evaluators score against item-by-item criteria — staff qualifications (30 pts), methodology (20 pts), local participation (15 pts). Optimising the bid means making each criterion immediately tickable: a dedicated annex per scoring dimension, named CVs in the prescribed format (Form 3G), local-participation table with nationality column.
- **Generic role addresses age better than named people.** Replacing *"Prof. William Coffie, MD"* with *"The Managing Director"* in Form 4A means the bid stays valid through MD turnover. Worth doing across any document with a 90-day validity window.
- **Removing scope can preserve the price.** Dropping maintenance and training from a fixed-scope bid while keeping the lump sum intact reframes the same dollars as *richer development* — defensible because the system must be more self-sufficient at handover. Cleaner narrative ("we build it, you own it") than ongoing-dependency models for parastatal clients who want to internalise IT operations.

## Related

- **Concepts**: *(none directly applicable yet — bid-mechanics patterns above could promote to `wiki/concepts/python-as-bid-templating.md` or `wiki/concepts/frontend-first-bid-strategy.md` if they recur on a second QCBS bid.)*
- **Entities**: *(CPC, CMC, SoftTech Solutions, Godwin Opoku Duah, and the rest of the named team are not in the brain yet. Worth stubbing if any of these recur in other projects or sources.)*
- **Sources**: *(none ingested for this project. The full RFP `docs/proposals/CPC Full RFP.pdf` is local-only; could be added to `raw/` if QCBS bid mechanics become a recurring brain topic.)*
- **Other projects**: [[wiki/projects/stacesprouts]] — sibling Ghana-portfolio project; same Spring Boot 3 + React 19 + Tailwind v4 ecosystem; if the CPC backend is built it'll be the third Spring Boot codebase in the portfolio. [[wiki/projects/vedge]] — multi-tenant healthcare OS; similar bounded-context microservices reasoning.

## External links

- **Repo**: *(no remote — local-only at `/Users/kobbyopoku/Projects/CPC_RTBVD`)*
- **Project's own `CLAUDE.md`**: *(none — only `.claude/settings.local.json`)*
- **Auto-memory**: `/Users/kobbyopoku/Projects/CPC_RTBVD/.remember/`
- **Bid package** (in repo): `docs/proposals/SoftTech-Technical-Proposal.docx`, `docs/proposals/SoftTech-Financial-Proposal.docx`, `docs/proposals/RFP-Response-Letter.docx`, `docs/proposals/CMC-Business-Proposal.docx`
- **Source RFP**: `docs/proposals/CPC Full RFP.pdf` (CPC/PRO/CS/1/26, issued 10 March 2026)
- **Build scripts**: `docs/build_*.py`
- **Architecture diagrams**: `docs/diagrams/` (PNGs + accompanying HTML/CSS source)
