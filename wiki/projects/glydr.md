---
type: project
title: Glydr
created: 2026-05-11
updated: 2026-05-11
status: exploring
repo: (no remote yet — local git initialized 2026-05-11; no commits yet)
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/glydr
stack: [flutter, dart, java-21, spring-boot-3.5, maven, postgres, flyway, hibernate, hikari, nextjs-15, react, typescript, tailwindcss, turbopack, docker-compose, railway-planned, flutterwave-planned, smile-identity-planned, brolly-insurance-planned, hubtel-planned, google-maps-planned, firebase-cloud-messaging-planned, posthog-planned, sentry-planned]
started: 2026-05-11
ended:
owner_org: roam-labs
affiliation: roam-labs-product
name_confirmed: false
brand_name_status: working
aliases: [glydr]
tags: [project, mobility, carpooling, ghana, marketplace, two-sided, mobile-first, monorepo, intercity-transport, cost-sharing]
---

# Glydr

> **Lineage**: ROAM Labs owned product ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder + sole builder). Insurance underwriting via [[wiki/projects/brolly|Brolly Africa]] (Godwin co-founded). Brand name "Glydr" is a **working name**, not yet confirmed (PRD §16 Q7). Corporate structure (PRD §16 Q1) is still open — the `roam-labs-product` affiliation reflects current intent; subject to revision if Glydr is later spun out as a separate company or absorbed into Brolly.

> **One-sentence framing**: Peer-to-peer intercity carpooling for Ghana, launching narrowly on Accra ↔ Kumasi weekend trips, structurally positioned as cost-sharing rather than commercial transport.

## What and why

Glydr is a peer-to-peer intercity carpooling marketplace connecting drivers with empty seats to passengers travelling the same route, launching on the Accra ↔ Kumasi corridor with weekend Friday-out / Sunday-back trips. The product is positioned legally as **cost-sharing** (the driver counts as one occupant who pays their own per-seat share of fuel + wear), which keeps it out of the commercial-transport regulatory bucket and unlocks a supply pool that ride-hailing platforms cannot reach: car owners who would never drive for a living but make predictable, recurring intercity trips. Two structural moats are baked into the design — payments via Flutterwave (existing relationship) and per-trip insurance top-ups underwritten by [[wiki/projects/brolly|Brolly Africa]] — and the insurance moat doubles as the strongest anti-leakage mechanism, because off-platform trips physically lose coverage. POC scope is intentionally small (2-4 weeks of solo evening/weekend build, manual KYC, single corridor, no commission); successful POC criteria gate the V1 build (Smile Identity KYC, Flutterwave escrow, Brolly automation, in-trip safety stack, iOS).

The local-cwd PRD ([`PRD_Glydr_v0.2.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/PRD_Glydr_v0.2.md)) is the canonical source of product truth as of v0.2 (11 May 2026, "Draft for internal review").

## Stack and infrastructure

Single git repo at the workspace root; **polyglot monorepo** with four sibling projects, each with its own toolchain.

- **Repo topology**:
  - `mobile/` — Flutter (Android-first per POC §6.1, iOS at V1)
  - `backend/` — Spring Boot 3.5.14 / Java 21 / Maven
  - `landing/` — Next.js 15 (App Router, TS, Tailwind v4, Turbopack)
  - `control-center/` — Next.js 15 (App Router, TS, Tailwind v4, Turbopack) — operator console (driver approval queue, payment reconciliation, incident triage; PRD §8.8)
  - `docs/` — `architecture/` + `decisions/` (ADRs)
  - `infra/` — `railway/` + `scripts/`
- **Languages / frameworks**:
  - Mobile: Flutter / Dart; planned packages `riverpod`, `go_router`, `dio`, `google_maps_flutter`, `geolocator`, `image_picker`, `firebase_messaging`, `flutter_secure_storage`
  - Backend: Java 21 (Kotlin still on the table per Q6 below), Spring Boot 3.5.14 (Web, Security, Data JPA, Validation, Actuator, Flyway, Postgres driver, Configuration Processor, DevTools), Maven
  - Web: Next.js 15 App Router, React 19, TypeScript, Tailwind, Turbopack
- **Database**: Postgres 16 (local via `docker-compose.yml` at root; Railway managed Postgres planned for `dev` / `staging` / `prod`)
- **Migrations**: Flyway, on by default; `V1__init.sql` placeholder present
- **Configuration**: `application.yml` base + `application-dev.yml` / `application-prod.yml` profile overrides; env-var defaults make `./mvnw spring-boot:run` work immediately after clone
- **Planned third-party integrations** (PRD §11.4):
  - Payments: Flutterwave (Standard checkout for POC; inline SDK + escrow for V1)
  - KYC: Smile Identity (Ghana Card, DL, liveness, OCR — V1)
  - Insurance: [[wiki/projects/brolly|Brolly Africa]] internal API for per-trip top-up issuance (V1)
  - Maps: Google Maps Platform ([[wiki/entities/google-maps|Maps SDK / Places / Directions / Geocoding]])
  - SMS / OTP: Hubtel (local Ghana provider)
  - Push: Firebase Cloud Messaging
  - Analytics: PostHog (generous free tier, self-hostable later, session replay)
  - Errors: Sentry
- **Hosting target** (PRD §11.5): Railway Pro plan, three projects (`glydr-dev` / `glydr-staging` / `glydr-prod`) provisioned from day one
- **Local-dev story**: `docker compose up -d postgres` + `./mvnw spring-boot:run` + `flutter run` + `npm run dev` per Next.js app; per-project READMEs document the commands

## Current focus

Week of 2026-05-11 — **Building MVP as POC** (PRD §6.1 scope). Project just scaffolded (mobile / backend / landing / control-center / docs / infra), no functional features yet, no commits beyond the scaffold. Immediate sub-tracks:

- Pick the first end-to-end slice (likely **driver phone-OTP signup** — exercises mobile + backend + Hubtel without needing payments or insurance)
- **Pick a design system / visual direction** for the four product surfaces (mobile, landing, control-center, in-app trip flows) — see Q9 below
- Resolve the Java-vs-Kotlin ADR before serious feature work (Q6)
- Resolve corporate structure (PRD §16 Q1) so payments + insurance + liability can be wired correctly
- Provision the three Railway environments per PRD §11.5

## Architecture decisions

### Technical (made by scaffolding 2026-05-11)

- **2026-05-11** — **Polyglot monorepo, single root `.git`**, four sibling apps over four separate repos. Reason: solo founder, no shared library surface yet, simpler ops; matches Helm/CPC pattern of cwd-as-workspace.
- **2026-05-11** — **Spring Boot 3.5.14 / Java 21 / Maven** for backend. Matches PRD §11.2 intent (Java 21 LTS, Spring Boot 3.x). Maven over Gradle for solo-dev simplicity. (`3.5.14.RELEASE` from `start.spring.io` rejected — Spring Boot dropped the `.RELEASE` suffix in 2.4+; pinned to `3.5.14`.)
- **2026-05-11** — **Flutter Android-first**, iOS deferred to V1 per PRD §6.1. POC distribution via APK side-load.
- **2026-05-11** — **Next.js 15 (App Router, TS, Tailwind, Turbopack)** for both `landing/` and `control-center/`. Single web tooling for both surfaces; differentiated by route + auth.
- **2026-05-11** — **Three Railway environments** (`dev` / `staging` / `prod`) provisioned from day one — non-negotiable per PRD §11.5; migrating later is unnecessarily painful.
- **2026-05-11** — **Flyway from day one** with the migration directory pre-created (`backend/src/main/resources/db/migration/V1__init.sql` placeholder). No `ddl-auto: update` ever.

### Product (load-bearing, set in PRD v0.2)

- **2026-05-11** — **Cost-sharing legal positioning** (PRD §9.5): the driver counts as an occupant who pays their own fuel share, so the trip is structurally not commercial transport. Load-bearing for the entire business model — if this is challenged, almost everything downstream (insurance category, regulatory positioning, commission shape) has to be rethought.
- **2026-05-11** — **Asymmetric KYC**: driver-deep (Ghana Card, DL, vehicle docs, photos, liveness), passenger-light (phone OTP at signup, Ghana Card + selfie only at first booking) — PRD §8.2 / §10.1. Balances safety burden against demand-side liquidity.
- **2026-05-11** — **Anti-leakage as architecture, not policy** (PRD §10.2): Brolly per-trip insurance only activates on app-booked trips, so drivers physically lose protection by going off-platform. Strongest single defensible mechanic.
- **2026-05-11** — **POC = no commission, manual KYC, single corridor, weekend trips only** (PRD §6.1) — concierge MVP designed to validate demand pull and supply economics before V1 build investment.

## Open questions

From PRD §16 (canonical) plus scaffold-stage flags:

1. **Corporate structure** — separate company / Brolly subsidiary / unincorporated for POC (PRD §16 Q1). Affects payments routing, insurance arrangement, liability. Currently tagged `roam-labs-product` as working assumption.
2. **Co-founder strategy** — solo through POC, or recruit before V1 (PRD §16 Q2). Risk table flags founder bandwidth as High/High; V1 timeline is conditional on resolving this.
3. **Commission rate at V1 launch** — 10% vs 15% (PRD §16 Q3). Trade-off between driver retention and platform unit economics.
4. **Brolly per-trip insurance specifics** — pricing, structure, timeline (PRD §16 Q4). Single point of failure for V1 booking flow if not ready.
5. **Legal counsel for cost-sharing review** before V1 launch (PRD §16 Q5).
6. **Java vs Kotlin** for backend (PRD §11.2 leaves it to founder choice). Decision deferred at scaffold; defaulted to Java 21 because tooling defaults are simpler for solo. Pick before serious feature work.
7. **Object storage vendor** for KYC + vehicle photos — S3 / Cloudflare R2 / Backblaze B2. Railway has no first-class object store; decision affects mobile upload code and the data model.
8. **Real-time location transport** for in-trip safety — Firestore sidecar vs WebSockets vs polling. Affects backend complexity, mobile battery story, and iOS background-location entitlement.
9. **Design system / visual direction** — not chosen. Needed for mobile (passenger + driver flows), landing site, control-center, in-app messaging. No aesthetic-style picked yet (cf. brain entries: editorial / minimal / brutalism / claymorphism / etc.).
10. **Brand name + domain** — "Glydr" is working only; PRD §16 Q7. (Frontmatter carries `name_confirmed: false`.)
11. **Investor capital after validation, or bootstrap from revenue** (PRD §16 Q10).
12. **iOS-vs-Android-only for POC** (PRD §16 Q8) — PRD §6.1 leans Android-only; not yet formally confirmed.

## Lessons learned

_(Empty — populated as patterns surface. If a lesson generalizes beyond Glydr, file it as a concept in `wiki/concepts/` and link from here. Candidate compounds-back-to-the-wiki areas: cost-sharing-as-regulatory-positioning, anti-leakage-as-architecture, Ghana-mobile-money-payment-flows, Brolly per-trip insurance integration pattern.)_

## Related

- **Other projects**:
  - [[wiki/projects/brolly]] — insurance underwriting partner (per-trip top-up); both founded / co-founded by Godwin; Glydr is the first external consumer of Brolly's per-trip insurance product
  - [[wiki/projects/asanti-brokers]] — adjacent Ghana insurance product (different category — brokerage vs underwriting); same founder umbrella
  - [[wiki/projects/stacesprouts]] — closest stack precedent in the wiki: Flutter + Spring Boot + Flutterwave on Vercel + Railway
  - [[wiki/projects/vedge]] — sibling architectural pattern (multi-tenant Spring Boot + Flutter mobile)
- **Concepts**:
  - [[wiki/concepts/visual-directions]] — relevant when picking design system / visual identity
  - [[wiki/concepts/landing-page-patterns]] — relevant for `landing/` build-out
  - [[wiki/concepts/switching-forces]] — relevant to the leakage thesis (what makes off-platform trips structurally worse)
- **Entities**:
  - [[wiki/entities/godwin-opoku-duah]] — founder + sole builder
  - [[wiki/entities/roam-labs]] — owning org (working assumption, see Q1)
  - [[wiki/entities/google-maps]] — Maps / Places / Directions / Geocoding for trip listing + pricing
- **Sources**: _(none directly cited yet — future ingests on cost-sharing legal frameworks, BlaBlaCar precedent, Ghana DPA / NIA / DVLA regulatory environment would land here)_

## External links

- **Repo**: no remote yet — local git initialized 2026-05-11
- **Project's own CLAUDE.md**: _(none yet — `BRAIN.md` reference at root)_
- **Project memory dir**: _(none)_
- **PRD**: [`PRD_Glydr_v0.2.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/PRD_Glydr_v0.2.md) (v0.2, 11 May 2026, "Draft for internal review")
- **Architecture docs scaffold**: `docs/architecture/README.md` + `docs/decisions/README.md` (ADR template + open decisions list)
- **Infra scaffold**: `infra/railway/README.md` (provisioning checklist)
