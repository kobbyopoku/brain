---
type: project
title: Vedge
created: 2026-05-02
updated: 2026-05-05
status: active
repo: multi-repo (github.com/kobbyopoku/vedge_backend, vedge_frontend, vedge_patient, vedge_staff, vedge_landing, vedge_emails, vedge_agent)
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/vedge
stack: [java-21, spring-boot, postgres, flyway, redis, next.js, react, typescript, tailwind, flutter, riverpod, dio]
started: 2026-04-05
aliases: [vedge-platform, vedge-health]
tags: [project, healthcare, ehr, africa, multi-tenant]
---

# Vedge

> A multi-tenant healthcare operating system for African hospitals, clinics, labs, and pharmacies — a modular-monolith Spring Boot backend with web, marketing, and Flutter companion apps for patients and staff.

## What and why

Vedge addresses the absence of an integrated, locally-aware EHR + billing + claims + lab/imaging/pharmacy platform for African healthcare facilities. The product spans a clinician/admin web app, a patient mobile companion, a staff mobile companion, transactional emails, and a marketing site, all sharing a single Spring Boot backend organized as a modular monolith. Core domains include multi-tenant identity, scheduling, walk-in intake, billing/claims (with NHIS/Paystack/Flutterwave integration), lab orders/results, imaging with SMS notifications, pharmacy stock and dispensing, and finance/expenses. Patients reach their records via phone-OTP auth and cross-tenant claim flows; clinicians and ops staff use JWT-based web and mobile clients. The system is in active build with weekly shipped features and a hard-edged review protocol for anything touching auth, PHI, billing, or migrations.

## Stack and infrastructure

- **Backend (`vedge_backend`)**: Spring Boot 3.4.2, Java 21, Maven modular monolith. Modules: `vedge-auth`, `vedge-tenant`, `vedge-patient`, `vedge-billing`, `vedge-finance`, `vedge-expenses`, `vedge-lab`, `vedge-pharmacy`, `vedge-scheduling`, `vedge-interop`, `vedge-common`, `vedge-app`. Postgres 18 + Flyway migrations, Redis, Docker, Kafka (provisioned but dormant).
- **Web frontend (`vedge_frontend`)**: Next.js 16, React 19, TypeScript — clinician/admin app.
- **Landing site (`vedge_landing`)**: Next.js 16, React 19, Tailwind v3 — Afro-modernist editorial marketing site.
- **Patient mobile (`vedge_patient`)**: Flutter 3.32, Riverpod, Dio, go_router — phone-OTP auth + cross-tenant claim.
- **Staff mobile (`vedge_staff`)**: Flutter 3.32, Riverpod, Dio — staff companion (W5.7 walking skeleton).
- **Emails (`vedge_emails`)**: React Email templates.
- **Agent (`vedge_agent`)**: scaffold only, currently empty.
- **GRC**: Kivora (external SaaS).
- **Repos**: `kobbyopoku/{vedge_backend, vedge_frontend, vedge_patient, vedge_staff, vedge_landing, vedge_emails, vedge_agent}` on GitHub. The workspace root `/Users/kobbyopoku/ROAM/CascadeProjects/vedge/` is not itself a git repo — it's a polyrepo container.
- **Deploy**: staging on Railway; staging-first with fast-forward to main.

## Current focus

Week of 2026-05-02:

- Billing audit sweep — hardening `chk_audit_action` across V168-V171 (invoices, claims, preauth, payments).
- Unified walk-in invoice across labs + imaging.
- Aging widget + claims dashboard filter parity.
- Finance P&L JPQL enum binding fixes (`Expense`, `PaymentType`).
- Imaging-SMS outbox security/compliance fixes (cross-tenant filter, transaction fence, schema resolution, PHI purge scheduler).
- Recently shipped: staging Flyway out-of-order crash fix via `spring.flyway.out-of-order=true`.

## Architecture decisions

- **2026-04** — **Modular monolith over microservices** for backend. One Spring Boot app, modules per domain. Rationale: small team, deploy simplicity, transactional consistency across PHI.
- **2026-04** — **Expert-led implementation protocol** is mandatory for any change touching auth, billing, PHI, Flyway migrations, security, architecture, or 3+ files. Subagents spawn before code is written; security + performance reviews gate commits. See project `CLAUDE.md`.
- **2026-04** — **Migrations are immutable once pushed**. Never edit a Flyway file; add a follow-up. Per-tenant migrations must check column existence per-schema (iterate `information_schema`, not `public`).
- **2026-04** — **Native Google SDK for patient mobile login**. The Spring OAuth2 `google-patient` wiring (Wave 5b) is dormant.
- **2026-04** — **Kivora as GRC of record**. Legal/compliance lives there; don't duplicate in-app.
- **2026-04** — **Built-in role permissions exclude admin roles**. `chk_built_in_role` rejects ORG_ADMIN/SUPER_ADMIN — use `role_permissions` instead.
- **2026-04** — **Staging-first deploys**. Never commit directly to main; fast-forward main from staging.

## Open questions

- **Kafka cleanup** (Phase 10): drop from `docker-compose` and `application-*.yml`, or actually wire a producer.
- **`vedge_agent` scope**: what's it for? Currently an empty scaffold.
- **Therapy module**: 0L stubs — when does this get fleshed out?
- Patient Companion redesign, CC Settings frontend, Resend delivery, diagnostic-center widget gap (deferred backlog).
- Cross-tenant referral chain primitives — when, and what shape?

## Lessons learned

Seeded from `tasks/lessons.md` and auto-memory. Will be promoted to `wiki/concepts/` when patterns generalize beyond Vedge.

- Always run `mvn test-compile` before pushing service-signature changes — Railway catches arity mismatches `compile -DskipTests` doesn't.
- On Postgres 18, never `::text` cast `jsonb_build_object` output (SQL state 42804) — it already returns `jsonb`.
- When a migration touches `chk_audit_action`, diff against the **latest** migration that modified it, not V92.
- Spring beans with multiple constructors must mark one `@Autowired` or prod boot fails (`NoSuchMethodException`).
- Fetch `origin` and re-check the highest `V*` right before writing a new Flyway migration — collisions have happened twice.

## Related

- **Concepts**:
  - [[switching-forces]] — directly applicable to `vedge_landing` copy. The four forces for African healthcare facility switching from paper/fragmented systems to Vedge are mapped in the [[switching-forces#Mapping the four forces (a worked example for [[wiki/projects/vedge|Vedge]])|switching-forces page]] (Push: scattered notes, slow NHIS reimbursement; Pull: integrated platform with NHIS-aware billing; Habit: 30 years of paper; Anxiety: PHI security, training cost, migration risk). Pull-only landing copy will under-convert.
  - [[ai-seo]] — `vedge_landing` should expose `/llms.txt`, `/pricing.md`, and structured FAQ blocks if Vedge wants to be cited when AI agents compare African EHR options. Especially relevant given the buyer profile (clinic owners doing late-night research via ChatGPT or Perplexity).
  - [[landing-page-patterns]] — the 11 unicorn patterns are aspirational for `vedge_landing`; pattern 5 (social proof through scale) and pattern 8 (free CTA) are the lowest-hanging.
  - *(Other candidates to seed later: `multi-tenant-ehr`, `modular-monolith`, `flyway-migration-safety`, `expert-led-implementation-protocol`.)*
- **Entities**:
  - [[wiki/entities/marketingskills-repo]] — directly usable for `vedge_landing`: drop the repo into `~/.claude/skills`, fill out a Vedge-specific `product-marketing-context.md` (ICP = small/medium African healthcare facility owner; pain = NHIS reimbursement delays; quotes pulled from real clinic-owner interviews; proof = first 3 case studies), then invoke skills like CRO 7-question audit, switching-forces mapping, programmatic SEO playbooks (esp. Locations / Comparisons / Glossary).
  - [[wiki/entities/open-design]] — *added 2026-05-05*. Apache-2.0 design-tooling platform with 64 SKILL.md bundles + 138 DESIGN.md systems + BYOK proxy + sandboxed preview. **Direct fit for `vedge_landing`**: pick the `saas-landing` skill + an appropriate DESIGN.md (Linear or Stripe for clean SaaS feel; Notion for warm-clinical) + a Vedge-specific brand context. Local-first + BYOK = no Refero subscription dependency. The `pm-spec` and `eng-runbook` skills also apply to internal Vedge documentation. The `pricing-page` skill addresses the [[wiki/concepts/ai-seo|AI SEO]] recommendation directly. Daemon dependency is the tradeoff — Open Design adds a Node 24 + pnpm runtime to the dev environment vs just dropping markdown into `~/.claude/skills`.
  - *(Other candidates: Spring Boot, Flyway, Flutter, Riverpod, Paystack, Flutterwave, Kivora, Railway.)*
- **Sources**: *(none yet — the project's `CLAUDE.md` is the closest equivalent and is referenced under External links.)*
- **Other projects**: *(this is the first project page in the wiki.)*

## External links

- **Repo (backend)**: https://github.com/kobbyopoku/vedge_backend
- **Repo (web)**: https://github.com/kobbyopoku/vedge_frontend
- **Repo (patient mobile)**: https://github.com/kobbyopoku/vedge_patient
- **Repo (staff mobile)**: https://github.com/kobbyopoku/vedge_staff
- **Repo (landing)**: https://github.com/kobbyopoku/vedge_landing
- **Repo (emails)**: https://github.com/kobbyopoku/vedge_emails
- **Repo (agent)**: https://github.com/kobbyopoku/vedge_agent
- **Project's CLAUDE.md**: `/Users/kobbyopoku/ROAM/CascadeProjects/vedge/CLAUDE.md`
- **Backend platform review (2026-04-19)**: `/Users/kobbyopoku/ROAM/CascadeProjects/vedge/vedge_backend/docs/reviews/2026-04-19/README.md`
- **Auto-memory**: `~/.claude/projects/-Users-kobbyopoku-ROAM-CascadeProjects-vedge/memory/MEMORY.md`
