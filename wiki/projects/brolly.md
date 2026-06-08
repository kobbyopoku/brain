---
type: project
title: Brolly
created: 2026-05-09
updated: 2026-06-08
status: active
owner_org: brolly-africa
affiliation: brolly-africa-product
repo: multi-repo workspace (Brolly-Africa GitHub org + brolly1 GitLab mirrors)
local_path: /Users/kobbyopoku/Brolly
stack: [java, kotlin, spring-boot, jhipster, gradle, react, typescript, nextjs, vite, tailwindcss, redux-toolkit, react-query, postgres, paystack, aws-s3]
started: 2021-11-14
ended:
aliases: [Brolly Africa, brolly-africa]
tags: [project, insurtech, insurance, africa, ghana, multi-repo]
---

# Brolly

> African digital-insurance / insurtech platform with vehicle-insurance roots in the Bolt-driver market, now spanning a customer self-service portal, an agency / broker admin dashboard, and a multi-service backend mid-migration from JHipster Java to Kotlin / Spring Boot 3.

## What and why

Brolly is an African digital-insurance platform that began as a vehicle-insurance product targeting Bolt drivers in Ghana. It has grown into a multi-channel insurtech platform with customer self-service (Next.js portal), agency / broker administration (React admin), insurer relationship management, and end-to-end policy lifecycle handling — quotes, PayStack payments, claims, and S3-backed document management. The backend is mid-migration from a JHipster Spring Boot monolith toward a new Kotlin + Spring Boot 3 core (`core-backend`). The workspace also holds a freshly-scaffolded Vite / React 19 landing page and a shared "insurtech-platform" UI template, suggesting a planned design-system unification across the customer + admin surfaces.

## Stack and infrastructure

Brolly is **not a single git repo** — `/Users/kobbyopoku/Brolly` is a workspace folder holding multiple separately-versioned repos plus a few cross-cutting shell scripts and database dumps.

- **Languages / frameworks**:
  - Backend (current): Java 11 + Spring Boot via JHipster 7.5, Gradle
  - Backend (rewrite, in progress): Kotlin + Spring Boot 3.5 + Java 21
  - Admin dashboard: React 18 + TypeScript + Redux Toolkit + TailwindCSS + React Query + Chart.js / Nivo
  - Customer portal: Next.js 13 + TypeScript + TailwindCSS + Formik / Yup
  - Landing page: React 19 + Vite (very fresh, single commit)
  - UI template: React 18 "insurtech-platform" component library
- **Key dependencies / services**:
  - **Database**: Azure Postgres (per SQL dumps `azure_dev_brolly-*.sql` and `azure_test_brolly-*.sql` at workspace root)
  - **Payments**: PayStack
  - **Storage**: AWS S3 (document management)
  - **Notifications**: Slack webhooks
  - **Auth**: Google OAuth (customer portal)
  - **Analytics**: Google Analytics, Microsoft Clarity
  - **Anti-abuse**: reCAPTCHA
- **Repos**:
  - GitHub `Brolly-Africa/` (canonical):
    - `admin-portal` — React admin (Brolly Admin)
    - `backend-service` — JHipster Spring Boot backend
    - `customer-portal` — Next.js customer-facing site (`dark-slab` package)
    - `landing-page` — Vite / React 19 landing
    - `ui-template` — `insurtech-platform` shared UI components
  - GitLab `brolly1/` (older mirrors of the backend / admin):
    - `brolly_backend`
    - `brolly_admin`
  - Local-only (not yet versioned):
    - `core-backend` — Kotlin + Spring Boot 3 rewrite of the backend
- **Workspace-level artifacts**:
  - DTO-refactor shell scripts: `complete_dto_fixes.sh`, `convert_remaining_dtos.sh`, `fix_dto_packages.sh`, `fix_dto_types.sh` (dated 2025-07-24)
  - Postgres dumps from Azure dev + test environments
  - `certificates/` directory
- **Sibling directory in workspace** (separate project, NOT part of Brolly): `asanti-brokers` — see [[wiki/projects/asanti-brokers]].
- **Deployed at**: Azure (Postgres confirmed; deployment topology for the apps is not captured here yet).

## Current focus

_To be filled in by the human._ Recent commit signals (for context, not as a substitute for direction):

- `admin-portal`: broker-activations organization filtering, sort order, button-visibility fixes (`Filter broker activations by organization type`, `Fix invisible Activate button on broker activations page`, `Sort broker activations newest-first`).
- `backend-service`: activity-stream mutability bug, policy-document creation bug, PayStack + enterprise extra-seat charging, Smart Drive → third-party-amplified migration for Enterprise.
- `core-backend`: Kotlin rewrite in progress, not yet under version control.

## Architecture decisions

- **2025-07-24** — Cross-service DTO refactor. Four shell scripts at the workspace root (`complete_dto_fixes.sh`, `convert_remaining_dtos.sh`, `fix_dto_packages.sh`, `fix_dto_types.sh`) imply a coordinated DTO package / type alignment effort across the backend services that day.
- **~2025-09-10** — `core-backend` introduced as a Kotlin + Spring Boot 3.5 + Java 21 rewrite of the JHipster 7.5 / Java 11 backend. Direction implied: graduate off the JHipster generator, modernize the JVM, adopt Kotlin idioms.
- **GitHub `Brolly-Africa` org as canonical**, GitLab `brolly1/` repos retained as legacy mirrors. (Inferred from activity recency — GitHub repos have current PR-merge history, GitLab repos do not.)

_(Other durable decisions to be added by the human as they surface — e.g. payment-provider choice rationale, design-system unification plan, customer-portal Next.js version pin.)_

## Open questions

_To be filled in by the human._ Candidate prompts:

- Should the GitLab mirrors (`brolly_backend`, `brolly_admin`) be archived or formally retired?
- What's the cutover plan from JHipster `backend-service` to the Kotlin `core-backend`?
- Is `landing-page` (React 19 / Vite, single commit) the planned replacement for the existing customer-portal landing surface, or a separate marketing site?
- Is `ui-template` (`insurtech-platform`) intended as a shared design system for both `admin-portal` and `customer-portal`?

## Lessons learned

_(Empty — populated as patterns surface. If a lesson generalizes beyond Brolly, file it as a concept in `wiki/concepts/` and link from here.)_

## Related

- **Other projects**:
  - [[wiki/projects/asanti-brokers]] — your separate insurance-brokerage marketing site that lives as a sibling directory in this workspace; conceptually adjacent (insurance, Ghana) but a distinct project on a personal repo.
  - [[wiki/projects/vedge]] — both are African multi-tenant Spring Boot platforms; same author, similar architectural lineage.
- **Concepts**: _(none linked yet)_
- **Entities**: _(none linked yet)_
- **Sources**: _(none linked yet)_

## External links

- **Repos**:
  - https://github.com/Brolly-Africa/admin-portal
  - https://github.com/Brolly-Africa/backend-service
  - https://github.com/Brolly-Africa/customer-portal
  - https://github.com/Brolly-Africa/landing-page
  - https://github.com/Brolly-Africa/ui-template
  - https://gitlab.com/brolly1/brolly_backend (legacy mirror)
  - https://gitlab.com/brolly1/brolly_admin (legacy mirror)
- **Project's own CLAUDE.md**: _(none at workspace root)_
- **Project memory dir**: _(none)_
