---
type: project
title: Glydr
created: 2026-05-11
updated: 2026-05-11
status: active
repo: multi-repo (4 separate repos under github.com/kobbyopoku/ — glydr_backend / glydr_landing / glydr_cc / glydr_mobile). The local-cwd /Users/kobbyopoku/ROAM/CascadeProjects/glydr is an UNTRACKED workspace folder holding PRD + docs + infra + docker-compose, mirroring Helm and Brolly's wrapper pattern.
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/glydr
stack: [flutter, dart, java-21, spring-boot-3.5, maven, jjwt, aws-sdk-s3, h2-test, postgres, flyway, hibernate, hikari, nextjs-15, react, typescript, tailwindcss, turbopack, docker-compose, railway-planned, flutterwave-planned, smile-identity-planned, brolly-insurance-planned, mnotify-planned, resend-planned, google-maps-planned, firebase-cloud-messaging-planned, posthog-planned, sentry-planned]
started: 2026-05-11
ended:
owner_org: roam-labs
affiliation: roam-labs-product
name_confirmed: false
brand_name_status: working
repo_topology: multi-repo-wrapper
aliases: [glydr]
tags: [project, mobility, carpooling, ghana, marketplace, two-sided, mobile-first, multi-repo, intercity-transport, cost-sharing]
---

# Glydr

> **Lineage**: ROAM Labs owned product ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder + sole builder). Insurance underwriting via [[wiki/projects/brolly|Brolly Africa]] (Godwin co-founded). Brand name "Glydr" is a **working name**, not yet confirmed (PRD §16 Q7). Corporate structure (PRD §16 Q1) is still open — the `roam-labs-product` affiliation reflects current intent; subject to revision if Glydr is later spun out as a separate company or absorbed into Brolly.

> **Repo topology**: workspace folder + 4 sibling repos. The cwd-as-workspace at `/Users/kobbyopoku/ROAM/CascadeProjects/glydr` is **NOT** a git repo — it holds PRD + `docs/` + `infra/` + `docker-compose.yml` only on disk. Each of `mobile/`, `backend/`, `landing/`, `control-center/` has its own `.git` pointing at its own GitHub repo under `kobbyopoku/`. Same shape as [[wiki/projects/helm|Helm]] (proposed `ROAM-Labs/{helm-backend, helm-portal, helm-mcp}`) and [[wiki/projects/brolly|Brolly]] (`/Users/kobbyopoku/Brolly` workspace + `Brolly-Africa/{admin-portal, backend-service, ...}`).

> **One-sentence framing**: Peer-to-peer Point-A-to-Point-B carpooling for Ghana, piloting two corridors at once (Accra ↔ Kumasi weekend trips + in-Accra commute), structurally positioned as cost-sharing rather than commercial transport.

## What and why

Glydr is a peer-to-peer carpooling marketplace connecting drivers with empty seats to passengers travelling the same route. Originally PRD-scoped to Accra ↔ Kumasi weekend trips only; **broadened on 2026-05-11** to *Point A to Point B* with a dual pilot — the same intercity weekend trips **plus** in-Accra commute (e.g. Madina ↔ Osu). The product is positioned legally as **cost-sharing** (the driver counts as one occupant who pays their own per-seat share of fuel + wear), which keeps it out of the commercial-transport regulatory bucket and unlocks a supply pool that ride-hailing platforms cannot reach: car owners who would never drive for a living but make predictable, recurring trips. Two structural moats are baked into the design — payments via Flutterwave (existing relationship) and per-trip insurance top-ups underwritten by [[wiki/projects/brolly|Brolly Africa]] — and the insurance moat doubles as the strongest anti-leakage mechanism, because off-platform trips physically lose coverage. POC scope is intentionally small (2-4 weeks of solo evening/weekend build, manual KYC, no commission); successful POC criteria gate the V1 build (Smile Identity KYC, Flutterwave escrow, Brolly automation, in-trip safety stack, iOS).

The local-cwd PRD ([`PRD_Glydr_v0.2.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/PRD_Glydr_v0.2.md)) is the *original* source of product truth. Note that the landing now diverges from PRD §3.3 / §6.3 (which list in-Accra commute as a Year-1 *non-goal*) — a v0.3 PRD update is pending.

## Stack and infrastructure

Workspace folder + four sibling repos, each with its own toolchain.

- **Repo topology**:
  - GitHub `kobbyopoku/` (canonical):
    - `glydr_backend` — Spring Boot 3.5.14 / Java 21 / Maven
    - `glydr_landing` — Next.js 16 (App Router, TS, Tailwind v4, Turbopack)
    - `glydr_cc` — Next.js 16 control-center (operator console; PRD §8.8)
    - `glydr_mobile` — Flutter (Android-first per POC §6.1, iOS at V1)
  - Workspace-level (not in any repo):
    - `PRD_Glydr_v0.2.{md,docx}` — product source of truth
    - `docker-compose.yml` — local Postgres on host port `:5433` (shifted from `:5432` to avoid native Postgres collision)
    - `docs/` — `architecture/`, `decisions/` (ADRs), `brand/` (brief, `references/perk-com.md`, screenshots)
    - `infra/` — `railway/` provisioning checklist + `scripts/`
- **Languages / frameworks**:
  - Mobile: Flutter / Dart; planned packages `riverpod`, `go_router`, `dio`, `google_maps_flutter`, `geolocator`, `image_picker`, `firebase_messaging`, `flutter_secure_storage`. **No feature code yet — scaffold only.**
  - Backend: Java 21 + Spring Boot 3.5.14 (Web, Security, Data JPA, Validation, Actuator, Flyway, Postgres driver, Configuration Processor, DevTools), Maven. Plus `jjwt 0.12.6` for JWT + `aws-sdk v2 s3` for R2 + JDK `HttpClient` for Resend/mnotify. H2 runtime-scoped for tests + the optional `localdev` profile.
  - Web: Next.js 16 App Router, React 19, TypeScript, Tailwind v4, Turbopack
- **Database**: Postgres 16 (local Docker on `:5433`; Railway managed Postgres planned for `dev` / `staging` / `prod`)
- **Migrations**: Flyway, on by default. `V1__init.sql` ships the real KYC schema (users / vehicles / kyc_submissions / kyc_documents); `V2__waitlist.sql` adds the landing waitlist.
- **Configuration**: `application.yml` base + `application-{dev,prod,localdev}.yml` profiles; env-var defaults, `.env.example` documents every var. `OperatorBootstrap` provisions the operator account from `OPERATOR_EMAIL`/`OPERATOR_PASSWORD` at startup (idempotent).
- **Document storage**: Cloudflare R2 (S3-compatible, AWS SDK v2) with **LocalFS auto-fallback** when R2 env vars absent — same `DocumentStore` interface, log warning at startup so operators know which is active.
- **Notifications** (replaces PRD §11.4 SMS choice):
  - Email: **Resend** transactional API. Wired via `ResendEmailNotifier`. Logs only when `RESEND_API_KEY` absent.
  - SMS: **mnotify** (Ghana SMS provider — replaces Hubtel from PRD). Wired via `MnotifySmsNotifier`. Same env-gated fail-soft pattern.
  - Both fire on KYC decision (driver) AND landing waitlist signup (operator alert).
- **Brand identity**: **Quiet Corridor** — Corridor Green `#0e5c3a` primary, Sunrise Amber `#f2a71b` accent (decorative only), Bone `#f7f5ef` background, Plus Jakarta Sans + Inter + JetBrains Mono trio. Formalised as Open Design 9-section DESIGN.md at `landing/DESIGN.md` + `control-center/DESIGN.md` (inherits). Includes wordmark route mark (●━━●), eyebrow chips, no-shadows discipline. Mobile design direction still pending. See [[wiki/concepts/design-md]] + [[wiki/concepts/visual-directions]].
- **Planned third-party integrations** (PRD §11.4):
  - Payments: Flutterwave (Standard checkout for POC; inline SDK + escrow for V1) — *not yet wired*
  - KYC: Smile Identity (Ghana Card, DL, liveness, OCR — V1) — *manual review at POC, working*
  - Insurance: [[wiki/projects/brolly|Brolly Africa]] internal API for per-trip top-up issuance (V1) — *not yet wired*
  - Maps: [[wiki/entities/google-maps|Google Maps Platform]] (Maps SDK / Places / Directions / Geocoding) — *not yet wired*
  - Push: Firebase Cloud Messaging — *not yet wired*
  - Analytics: PostHog — *not yet wired*
  - Errors: Sentry — *not yet wired*
- **Hosting target** (PRD §11.5): Railway Pro plan, three projects (`glydr-dev` / `glydr-staging` / `glydr-prod`) — *not yet provisioned*
- **Local-dev story**: `docker compose up -d postgres` + `cd backend && set -a; . ./.env; set +a && ./mvnw spring-boot:run` + `cd control-center && npm run dev -- --port 3001` + `cd landing && npm run dev`. Operator login: `ops@glydr.app` / `ChangeMe123!` (bootstrapped from env on first backend start).

## What's wired today (end-to-end working)

1. **Backend KYC manual approval flow** — driver submits multipart KYC (POST `/v1/drivers/kyc`) → 10 documents land in R2/LocalFS → operator logs in (POST `/v1/admin/auth/login`) → fetches queue (GET `/v1/admin/kyc/queue`) → opens detail (GET `/v1/admin/kyc/{id}`) → approves/rejects with reason (POST `/v1/admin/kyc/{id}/decision`) → driver flips PENDING → ACTIVE → Resend + mnotify notifiers fire (or log if unconfigured). 14/14 backend tests passing.
2. **Control-center operator console** — login + KYC queue + KYC detail (with all 10 docs proxied through `/api/document-proxy` for LocalFS or direct for R2 presigned URLs) + approve/reject form. Quiet Corridor design tokens. Verified end-to-end through the browser (Playwright).
3. **Landing page** — full marketing site with hero, persona toggle (`?for=driver|passenger`), how-it-works, cost-share explainer (5/5/5 grid: in-Accra | "what that buys you" | intercity), trust strip, safety, comparisons, FAQ (`<details>`), waitlist form. Wired to backend POST `/v1/waitlist` (idempotent on phone+source). 3 hero/CTA copy options live in `docs/brand/landing-copy.md`.
4. **Operator email alerts on every waitlist signup** — Resend wiring fires for both KYC decisions and waitlist signups via the same `EmailNotifier` interface.

Not wired yet: real R2 bucket, real Resend API key, real mnotify API key, Railway provisioning, mobile app (Flutter scaffold only).

## Current focus

Week of 2026-05-11 — **Phase 2 wiring complete**. Moving to driver auth + mobile.

- **Next slice (recommended)**: **driver phone-OTP auth via mnotify**. Backend POST `/v1/drivers/auth/{request-otp,verify-otp}` + JWT for drivers + retire the tracking-token kludge. ~Half-day. Exercises the mnotify integration for real.
- **After that**: mobile app onboarding flow (Flutter — phone OTP screen → KYC document capture → "submitted, awaiting approval" screen → status flips to ACTIVE when operator approves).
- **Tactical / vendor hardening pending**: provision the three Railway environments per PRD §11.5; create real Cloudflare R2 bucket; verify a sender domain on Resend; set `MNOTIFY_API_KEY`. Half-day of clicking + config.
- **PRD update pending**: landing diverges from PRD §3.3 / §6.3 on in-Accra scope; PRD v0.3 should absorb the broadened pilot.

## Architecture decisions

### Technical (made by scaffolding 2026-05-11)

- **2026-05-11** — **Polyglot codebase, four separate sibling repos** under `github.com/kobbyopoku/`. Workspace folder at `/Users/kobbyopoku/ROAM/CascadeProjects/glydr` is untracked (holds PRD + docs + infra + docker-compose). Mirrors Helm/Brolly pattern.
- **2026-05-11** — **Spring Boot 3.5.14 / Java 21 / Maven** for backend. Maven over Gradle for solo-dev simplicity. (`3.5.14.RELEASE` from `start.spring.io` rejected — Spring Boot dropped the `.RELEASE` suffix in 2.4+; pinned to `3.5.14`.)
- **2026-05-11** — **Flutter Android-first**, iOS deferred to V1 per PRD §6.1. POC distribution via APK side-load.
- **2026-05-11** — **Next.js 16 (App Router, TS, Tailwind v4, Turbopack)** for both `landing/` and `control-center/`. Single web tooling for both surfaces.
- **2026-05-11** — **Three Railway environments** (`dev` / `staging` / `prod`) — non-negotiable per PRD §11.5; not yet provisioned.
- **2026-05-11** — **Flyway from day one**, `ddl-auto: validate` everywhere. Schema changes go through Flyway only.
- **2026-05-11** — **Docker Postgres on host port `:5433`** (not `:5432`) so it doesn't collide with a native Postgres on the same port. Documented in `docker-compose.yml` and `backend/.env`.

### Vendor + integration choices (resolved this session)

- **2026-05-11** — **Object storage: Cloudflare R2** with **LocalFS auto-fallback** when R2 env vars absent. Closes PRD §16 Q7. The `DocumentStore` interface keeps the swap mechanical; `R2DocumentStore` uses AWS SDK v2 with R2's S3-compatible endpoint.
- **2026-05-11** — **Email: Resend** transactional API (HTTP). Used for operator alerts on waitlist signups + KYC decisions.
- **2026-05-11** — **SMS: mnotify** (Ghana). **Replaces Hubtel from PRD §11.4** — Godwin's existing integration knowledge from Stacesprouts wins over PRD-time choice.
- **2026-05-11** — **Email + SMS notifiers are env-gated and fail-soft**. Same impl, vendor-call-or-log based on `RESEND_API_KEY` / `MNOTIFY_API_KEY` presence. Avoids `@Profile` bean games. Failures never propagate (KYC decision is already committed).
- **2026-05-11** — **Java over Kotlin** for backend. Closes PRD §16 Q6. Defaulted to Java because the scaffold was Java; revisit if a Kotlin-shaped problem appears.

### Auth + security

- **2026-05-11** — **JWT operator auth (HS256, jjwt 0.12)** + env-provisioned operator account via `OperatorBootstrap`. JWT TTL 12h. Single operator at POC; multi-operator in a later phase.
- **2026-05-11** — **Driver "auth" via opaque tracking token** at POC (returned at KYC submission, used for status checks). **Retired in next slice** when phone-OTP driver auth ships.
- **2026-05-11** — **Same-origin document proxy** in control-center (`/api/document-proxy`) so the operator JWT (httpOnly cookie) reaches backend-served LocalFS docs. Whitelisted to the backend's exact path pattern → cannot become an SSRF vector.

### Brand + design system

- **2026-05-11** — **Brand identity: "Quiet Corridor"** — Corridor Green primary, Sunrise Amber accent (decorative only — never CTAs), Bone background, Plus Jakarta + Inter + JetBrains Mono trio. Established by the Brand Guardian agent; formalised as Open Design 9-section DESIGN.md at `landing/DESIGN.md` + `control-center/DESIGN.md` (inherits). Closes PRD §16 Q9 for landing + control-center; mobile direction still pending.
- **2026-05-11** — **No shadows + no glassmorphism** discipline. Glydr commits to **zero shadow tokens** in `globals.css`; surfaces differ by background value + 1px border only. `backdrop-blur` explicitly forbidden. Aligns with brain's documented "no box-shadows is a recurring rule" cross-brand pattern (Apple / Anthropic / Mercury / Minimalissimo). See [[wiki/concepts/design-md]].
- **2026-05-11** — **Wordmark route mark** (●━━●, two filled circles + dashed hairline) — typographic flourish that describes the *product* (Point A → Point B), not the *name*. Rename-safe. Documented in DESIGN.md.
- **2026-05-11** — **Eyebrow chips** (`bg-primary/10` pill chips) replace plain uppercase eyebrow text. Used on every section header + persona panel + pricing scenario label.
- **2026-05-11** — **Marketing-vs-product design system split**: hand-rolled Tailwind v4 for landing, same for control-center for now (will adopt shadcn/ui at the control-center level when it needs many shadcn-shaped components — modals, command palettes, dropdowns). Mirrors [[wiki/projects/coffee-break-with-big-sis|Coffee Break]]'s established pattern.

### Product (load-bearing, set in PRD v0.2 + landing extensions)

- **2026-05-11** — **Cost-sharing legal positioning** (PRD §9.5): driver counts as an occupant who pays their own fuel share. Load-bearing for the entire business model.
- **2026-05-11** — **Asymmetric KYC**: driver-deep, passenger-light (PRD §8.2 / §10.1).
- **2026-05-11** — **Anti-leakage as architecture**: Brolly per-trip insurance only on app-booked trips (PRD §10.2).
- **2026-05-11** — **POC scope** = no commission, manual KYC, weekend trips only (PRD §6.1).
- **2026-05-11** — **Landing positioning broadened to "Point A to Point B"** with **dual pilot** (Accra↔Kumasi + in-Accra commute). Diverges from PRD §3.3 / §6.3 which list in-Accra commute as Year-1 non-goal. Decision noted; PRD v0.3 should absorb. Trade-offs (matching density, leakage on repeat pairs, Bolt as direct competitor for in-Accra) acknowledged.
- **2026-05-11** — **Pricing example in landing**: Toyota Camry replaces PRD Appendix A's BMW X5 (more representative Ghanaian intercity vehicle). Two scenarios shown side-by-side: intercity (~GHS 62/seat) + intra-Accra commute (~GHS 5/seat).

## Open questions

From PRD §16 (canonical) plus session-state flags. **Resolved items kept with strikethrough so the historical record stands.**

1. **Corporate structure** — separate company / Brolly subsidiary / unincorporated for POC (PRD §16 Q1). Currently `roam-labs-product` working assumption.
2. **Co-founder strategy** — solo through POC, or recruit before V1 (PRD §16 Q2). Risk table flags founder bandwidth as High/High.
3. **Commission rate at V1 launch** — 10% vs 15% (PRD §16 Q3).
4. **Brolly per-trip insurance specifics** — pricing, structure, timeline (PRD §16 Q4). Single point of failure for V1 booking flow.
5. **Legal counsel for cost-sharing review** before V1 launch (PRD §16 Q5).
6. ~~**Java vs Kotlin** for backend (PRD §11.2).~~ → **Resolved 2026-05-11: Java 21.**
7. ~~**Object storage vendor** for KYC + vehicle photos.~~ → **Resolved 2026-05-11: Cloudflare R2 + LocalFS dev fallback.**
8. **Real-time location transport** for in-trip safety — Firestore sidecar vs WebSockets vs polling.
9. ~~**Design system / visual direction**.~~ → **Resolved 2026-05-11: "Quiet Corridor" Open Design DESIGN.md for landing + control-center. Mobile direction still pending.**
10. **Brand name + domain** — "Glydr" is working only; PRD §16 Q7. (`name_confirmed: false`.)
11. **Investor capital after validation, or bootstrap from revenue** (PRD §16 Q10).
12. **iOS-vs-Android-only for POC** (PRD §16 Q8) — leans Android-only; not yet formally confirmed.
13. **Workspace shape** *(new 2026-05-11)* — keep root `/Users/kobbyopoku/ROAM/CascadeProjects/glydr` untracked (current state, mirrors Brolly), or promote to a wrapper repo (`glydr_workspace`) holding PRD + docs + infra + docker-compose? Untracked is fine while solo; wrapper helps when collaborators land.
14. **PRD ↔ landing divergence** *(new 2026-05-11)* — landing now positions broader than PRD (Point A to Point B + in-Accra commute). PRD v0.3 should absorb the broadened scope, OR landing should be treated as the more recent source of truth and PRD frozen at v0.2 with a "see decision-log" pointer.
15. **Driver auth shape for next slice** *(new 2026-05-11)* — phone-OTP via mnotify (decided in principle); confirm OTP TTL, replay protection, throttle policy before code.

## Lessons learned

Three patterns surfaced during the 2026-05-11 build session:

1. **Marketing-vs-product design system split** — for any project with both a marketing surface and a product surface, hand-rolled Tailwind for marketing wins (visual control, no third-party aesthetic baggage), but adopt shadcn-or-equivalent at the product surface where component density is high. Worked examples: this project + [[wiki/projects/coffee-break-with-big-sis|Coffee Break]]. Could be promoted to a concept page once a third worked example lands.
2. **Fail-soft env-gated notifier pattern** — single notifier impl serves dev (logs) and prod (calls vendor) based on env-var presence. Avoids `@Profile` bean overrides + `@ConditionalOnProperty` ceremony. Much easier reasoning at runtime: one log line at startup tells the operator whether the integration is hot. Worked examples: `ResendEmailNotifier` + `MnotifySmsNotifier`.
3. **JPA `:param IS NULL` cursor-pagination Postgres footgun** — when a nullable JPQL parameter appears only in `:param IS NULL` context, Postgres can't infer its type and returns `ERROR: could not determine data type of parameter $N`. Hibernate doesn't help. Fix: split into two methods (cursor-present + cursor-absent) and route at the service layer. Cleaner than native query with explicit cast. Worth a concept page if it shows up on another project.

## Related

- **Other projects**:
  - [[wiki/projects/brolly]] — insurance underwriting partner (per-trip top-up); both founded / co-founded by Godwin; Glydr is the first external consumer of Brolly's per-trip insurance product. Same multi-repo wrapper pattern.
  - [[wiki/projects/asanti-brokers]] — adjacent Ghana insurance product (different category — brokerage vs underwriting); same founder umbrella.
  - [[wiki/projects/stacesprouts]] — closest stack precedent in the wiki: Flutter + Spring Boot + Vercel + Railway + Flutterwave + mnotify. The mnotify decision here directly inherits from Stacesprouts' established integration.
  - [[wiki/projects/vedge]] — sibling architectural pattern (multi-tenant Spring Boot + Flutter mobile).
  - [[wiki/projects/coffee-break-with-big-sis]] — established the marketing-vs-product design system split that Glydr now reinforces.
  - [[wiki/projects/helm]] — same multi-repo wrapper topology.
- **Concepts**:
  - [[wiki/concepts/design-md]] — `landing/DESIGN.md` is a worked example of the Open Design 9-section schema.
  - [[wiki/concepts/markdown-as-agent-contract]] — DESIGN.md is an instance of this meta-pattern.
  - [[wiki/concepts/visual-directions]] — relevant when picking design direction; Glydr's Quiet Corridor sits in the AI-product-restraint cluster.
  - [[wiki/concepts/landing-page-patterns]] — the Glydr landing implements patterns 1, 2, 3, 7, 8, 10 from the YC-unicorn catalog.
  - [[wiki/concepts/switching-forces]] — the leakage thesis (Brolly insurance only on app-booked trips) is a structural switching-force play.
- **Entities**:
  - [[wiki/entities/godwin-opoku-duah]] — founder + sole builder.
  - [[wiki/entities/roam-labs]] — owning org (working assumption, see Q1).
  - [[wiki/entities/google-maps]] — Maps / Places / Directions / Geocoding for trip listing + pricing.
- **Sources**: _(none directly cited yet — future ingests on cost-sharing legal frameworks, BlaBlaCar precedent, Ghana DPA / NIA / DVLA regulatory environment would land here)_

## External links

- **Repos** (all under `github.com/kobbyopoku/`):
  - https://github.com/kobbyopoku/glydr_backend
  - https://github.com/kobbyopoku/glydr_landing
  - https://github.com/kobbyopoku/glydr_cc
  - https://github.com/kobbyopoku/glydr_mobile
- **Project's own CLAUDE.md**: _(none yet — `BRAIN.md` reference at workspace root)_
- **Project memory dir**: _(none)_
- **PRD**: [`PRD_Glydr_v0.2.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/PRD_Glydr_v0.2.md) (v0.2, 11 May 2026, "Draft for internal review"). v0.3 pending to absorb the Point-A-to-Point-B broadening.
- **Brand brief**: [`docs/brand/brand-brief.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/docs/brand/brand-brief.md) — Quiet Corridor lineage.
- **Landing DESIGN.md**: [`landing/DESIGN.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/landing/DESIGN.md) — Open Design 9-section schema, source of truth for visual system.
- **Design system decision ADR**: [`docs/decisions/0001-design-system.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/docs/decisions/0001-design-system.md) — captures Quiet Corridor + perk.com structural borrows + Travelperk-file rejection lineage.
- **Architecture docs scaffold**: [`docs/architecture/`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/docs/architecture) (system-context, data-model, trip-state-machine, payments, kyc, safety-stack, data-residency planned).
- **Infra scaffold**: [`infra/railway/`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/infra/railway) (provisioning checklist).
