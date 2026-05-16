---
type: project
title: Glydr
created: 2026-05-11
updated: 2026-05-16
status: active
repo: multi-repo (5 separate repos under github.com/kobbyopoku/ — glydr_backend / glydr_landing / glydr_cc / glydr_mobile / glydr_docs). The local-cwd /Users/kobbyopoku/ROAM/CascadeProjects/glydr is an UNTRACKED workspace folder; PRD + docker-compose + infra/ removed from the workspace root post-Phase-7 (PRD now lives in docs/, local Postgres no longer needed since Railway is provisioned).
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/glydr
stack: [flutter, dart, java-21, spring-boot-3.5, maven, jjwt, aws-sdk-s3, h2-test, postgres, flyway, hibernate, hikari, nextjs-16, react-19, typescript, tailwindcss-v4, turbopack, railway, flutter-riverpod, go-router, dio, flutter-map, flutter-secure-storage, camera, image-picker, permission-handler, smile-id-unfit-on-ios, sentry-flutter, firebase-messaging, firebase-core, mnotify, resend, flutterwave-planned, brolly-insurance-planned, posthog-planned]
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

> **Repo topology** *(updated 2026-05-15)*: workspace folder + **5** sibling repos. The cwd-as-workspace at `/Users/kobbyopoku/ROAM/CascadeProjects/glydr` is **NOT** a git repo — by Phase 7 it had collapsed to just `BRAIN.md` + the five sibling clones (PRD + docker-compose + infra/ moved into `docs/`, which is itself now a separate repo). Each of `mobile/`, `backend/`, `landing/`, `control-center/`, `docs/` has its own `.git` pointing at its own GitHub repo under `kobbyopoku/`. Same shape as [[wiki/projects/helm|Helm]] and [[wiki/projects/brolly|Brolly]].

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
- **Brand identity** *(pivoted 2026-05-12)*: **Neon Carbon** — dark warm-black `#0A0807` background with neon-glow accents (lime `#D4FF3A` primary, orange glows), Hanken Grotesk for the wordmark + body. **Quiet Corridor was retired** when the visual system was unified across landing + mobile; previous Quiet-Corridor / Bone-background tokens are only kept on the control-center for now. See `[[brand_split]]` memory note. Mobile design lands on the same Neon Carbon system; the wordmark route mark (●━━●) stays.
- **Third-party integrations** *(updated 2026-05-15)*:
  - Payments: Flutterwave — *not yet wired*
  - KYC: Smile Identity (Ghana Card, DL, liveness) — **iOS bridge UNFIT (vendor bug, see Lessons)**; manual photo upload now first-class on both platforms with live in-app camera preview (`package:camera`). Smile Job Status Poller backstop on backend.
  - Insurance: [[wiki/projects/brolly|Brolly Africa]] per-trip top-up — *not yet wired*
  - Maps: **`flutter_map` (OpenStreetMap)** — picked over Google Maps for v1 because zero-credential / zero-Cloud-Console / no API key; tile source CartoDB Dark Matter (CC-BY). Swappable for Google Maps later.
  - Push: **Firebase Cloud Messaging** wired and live; covers BOOKING / TRIP / PAYOUT / PICKUP_CODE_ARMED / MESSAGE_RECEIVED / KYC_DECISION events. Mobile push handler invalidates the matching providers on receipt.
  - Errors / observability: **Sentry** scaffolded inert (Flutter + Spring), activates when `SENTRY_DSN` / `GLYDR_SENTRY_DSN` is set. Backend Railway has a real DSN; mobile is still inert until DSN is dart-defined.
  - Analytics: PostHog — *not yet wired*
  - Real-time chat: **SSE** (Server-Sent Events) — picked over WebSockets / Firestore for v1; mobile auto-reconnects + 30s catch-up poll for silent drops. See [[wiki/projects/glydr|architecture decisions § 2026-05-13]].
- **Hosting**: **Railway provisioned** (`glydr-staging` live, prod TBD). Backend deploys on push to main. Includes managed Postgres + R2 (Cloudflare) wired with proper env vars after a Phase 7r-6 footgun (R2_PUBLIC_URL is the SigV4 endpoint, not the public-read URL — see Lessons).
- **Local-dev story**: `docker compose up -d postgres` + `cd backend && set -a; . ./.env; set +a && ./mvnw spring-boot:run` + `cd control-center && npm run dev -- --port 3001` + `cd landing && npm run dev`. Operator login: `ops@glydr.app` / `ChangeMe123!` (bootstrapped from env on first backend start).

## What's wired today (end-to-end working)

*Phase 2 list (KYC, control-center, landing, operator alerts) all still working. Phases 4-7 dramatically expanded the surface — summary below.*

1. **Backend KYC manual approval flow** — driver submits multipart KYC → docs land in R2 → operator logs in via control-center → approves / rejects → driver flips PENDING → ACTIVE → Resend + mnotify + **FCM push** notifiers fire (Phase 7r-6 added the push wake-up via `KYC_DECISION` event).
2. **Control-center operator console** — login + KYC queue + KYC detail (10 docs via `/api/document-proxy`) + approve/reject form + **payout listing** (Phase 7b) + **token refresh** endpoint (Phase 7q backend support).
3. **Landing page** — full marketing site, waitlist form posting to `/v1/waitlist`, Neon Carbon visual.
4. **Mobile (Flutter, both Android + iOS)** — far past scaffold:
   - **Auth**: phone-OTP via mnotify with auto-fill from incoming SMS (Phase 6f), local PIN + biometric unlock (Phase 6g), AuthInterceptor 1-shot retry on 401/403 with multipart skip (Phase 7q).
   - **KYC**: manual photo upload end-to-end with live in-app camera preview inside the framing rectangle / face frame (Phase 7r-6); Smile Identity widget path attempted then abandoned on iOS (vendor bug). KYC submit lands directly on `/home`; standalone `/status` screen + "add vehicle" intermediate were removed.
   - **Trips lifecycle (Phase 7a → 7m)**: live trip lifecycle, driver payouts ledger + cash-out + ops batching (7b), trip-start workflows + safety SMS (7c), in-trip dark map + routed polyline + pickup roster + SOS (7d), in-app messaging via SSE (7e), passenger ↔ driver ratings (7f), shared GlydrMapView + trip-status unification (7h), driver trip history feed (7i), pickup-code 4-digit verification handshake (7j), Track-driver chip + routed mini-map (7k), pickup polling + overlay clearance (7l), trip-detail + chat polish (7m).
   - **Safety stack (Phase 7g)**: SOS fan-out + safe-arrival + ops alert.
   - **Reliability (Phase 7n → 7q)**: SSE auto-reconnect + 30s catch-up poll for silent drops, parentNavigatorKey discipline across top-level pushed routes, Sentry scaffold (inert until DSN), pull-to-refresh sweep on Activities + Messages + Driver Home, AuthInterceptor cold-start retry.
   - **UX**: ride/drive switcher rename, You-screen redesign, activities feed depth + smart bell, driver-side counterpart sheet, pickup global passenger OTP modal sheet (Phase 7r), splash flicker eliminated by preloading Hanken Grotesk (Phase 7r-6).
5. **Backend trip-side endpoints** — payouts (7b), ratings (7f), SOS (7g), trip-status unification (7h), driver trip history feed (7i), pickup-code handshake (7j), pricing AC surcharge runtime-tunable per country (Phase 7g+), country lifecycle status + trip-create gate, admin token refresh (Phase 7q backend), Smile Job Status Poller backstop (Phase 7r — polls Smile REST `job_status` to cover the case where the SDK consumes the verdict synchronously and never fires the partner callback).
6. **Cross-cutting integrations live**:
   - R2 (Cloudflare) — staging endpoint + bucket configured; SigV4 auth working after a Phase 7r-6 env-var detour.
   - FCM push — Android wired; iOS push gated on APNs + entitlement work (deferred).
   - Resend + mnotify — both live in staging.
   - `flutter_map` + `geolocator` + `geocoding` — live for the passenger map drop-pin flow + reverse-geocoding.

*Updates 2026-05-16 (Phase 7r-7 → 7w stack, pushed-on-branch awaiting merge to `main`):*

7. **Add-vehicle workflow (Phase 7r-7)** — driver picks a vehicle and must upload driver licence + 5 vehicle photos (front, back, left, right, interior); backend pre-checks NIC insurance synchronously on add-vehicle, then re-verifies again at trip-create. NIC verdict + `insurance_raw_response` retained for audit; `INSURANCE_NOT_ACTIVE` blocks the Save button. (Backend NPE on `fireOperatorSubmissionAlert` for vehicleless KYC submissions fixed in `bc32feb` / `f60634a` / `4dee4a9` / `cae389a`.)
8. **Passenger trust surface (Phase 7t)** — `DriverSummary` + `VehicleSummary` extended with `kycApproved` / `licenseOnFile` / 5 presigned photos / passenger-safe insurance status (ACTIVE → VERIFIED; NO_POLICY / UNKNOWN → PENDING). Mobile `TripTrustChipsRow` renders on search card, trip detail, waiting-for-driver, my-trip, and home pinned card. Trip detail gains a real vehicle thumbnail + tap-to-open 5-angle gallery. New `KycSubmissionRepository.findApprovedDriverIds(Collection<UUID>)` keeps the trip-list path O(1) on the KYC table.
9. **Operator fleet/insurance dashboard (Phase 7u)** — `GET /v1/admin/vehicles` returns paged fleet view filterable by insurance status / licence presence / KYC state; operators see **raw** enums (including `NO_POLICY`), not the passenger-softened view. Control-center `/vehicles` mirrors the `/kyc` queue layout — URL-as-state filter chip bar + desktop table + mobile card stack. New "Fleet" nav entry between Trips and Incidents. Read-only by design; mutations deferred to per-row detail page.
10. **Trip alerts subsystem (Phase 7v)** — V39 `trip_alerts` table + `POST/GET/DELETE /v1/trips/alerts`. 0-results passenger search → "Ping me when one opens"; `TripService.create()` fans out `TRIP_ALERT_MATCH` push to all matching alerts (region-pair exact match, one-shot, double-`try/catch` so a bad token never aborts trip creation). New mobile `/alerts` screen + You-screen "My alerts (N active)" entry. Mobile push handler invalidates relevant providers + deep-links to the matched trip.
11. **Welcome-screen "X glydrs in 2 km" pill (Phase 7v)** — replaced the static Accra–Kumasi placeholder with a live count of trips within 2 km of the user's GPS, auto-refreshing every 30 s via `Timer.periodic` disposed in `dispose()`. Reuses existing `/v1/trips/available` radius mode (no new endpoint).
12. **Messages thread route context (Phase 7v)** — backend `ThreadView.trip` block (nullable `ThreadTripSummary` = `{tripId, originLabel, destinationLabel}`); mobile messages list row renders `Origin → Destination` under the counterpart's name. Legacy threads without a trip association render fine (additive optional field).
13. **Selfie avatar (Phase 7v)** — `GET /v1/drivers/me` adds `selfieUrl` (24h presigned URL of the latest KYC SELFIE document); You-screen avatar renders selfie when on file, falls back to initial-on-gradient when null.
14. **Sentry mobile ACTIVATED (Phase 7s)** — real DSN minted at `roam-it-consultants/glydr` Flutter project. `mobile/.env` (gitignored) + `mobile/.env.example` (committed template) + `mobile/scripts/build-ios.sh` (~30-line bash wrapper forwarding every `key=value` from `.env` as `--dart-define` to `flutter build ios`). The Phase 7n scaffold (PII scrubber, expected-error filter, inert-by-default) is preserved; sentry-wizard was almost run on top of it and would have torched the scaffold (see Lessons).
15. **Admin token refresh fully wired** — backend `POST /v1/admin/auth/refresh` + JWT eligibility check + httpOnly expiry-metadata cookie; control-center `TokenRefreshMonitor` component integrated into the app shell; cookie-based silent refresh keeps operators logged in without re-typing the password every 12h.
16. **Admin create-country** — backend `POST /v1/admin/countries` clones settings from a source country + audits `COUNTRY_CREATED`; control-center settings page exposes the create form with server-side length validation. `CountryService` extracted from `AdminSettingsController` (refactor).
17. **Control-center UI uplift** — full-width console layout, full-height sidebar, modern single-line nav with icons, sidebar nav grouped under headings, wordmark went text-only (route mark dropped from CC), accent box after the wordmark, top-bar user profile menu with dropdown, notification bell surfacing incidents + payout requests. Minimal page headers (no eyebrow chip, terse subtitles).
18. **Landing legal-pages library (Phase 7w)** — 14 pages + `/legal` index, all behind a `<DraftBanner>`; central registry in `src/content/legal.ts` drives footer (4-column rewire) + sitemap + side-nav. Pages were sourced from a parallel agent audit (Legal Compliance Checker + Security Engineer) and grounded in the codebase's *actual* data flows (e.g., cookie policy says "zero cookies today"; privacy policy admits indefinite retention for `trip_locations` / `driver_otp_attempts` / KYC R2). Counsel review queued as Phase 7w-2.
19. **Smile Identity end-to-end on iOS unblocked (commits `2ef82d0` + `d776636` + `58b31bc` + `56aac0f`)** — cold-launch fix via static linkage + skip Firebase + null-safe push; Smile loop unstuck after the AuthInterceptor multipart-replay bug; Smile fullscreen + floating back button. Manual upload is still the primary path on both platforms post-7r-6, but the Smile widget path is no longer broken at cold-launch on iPhone.

Not wired yet: real Flutterwave (payments), real Brolly per-trip insurance, marketplace passenger-accident insurance (broker engagement pending), PostHog analytics, prod Railway environment, **backend Sentry** (audit-corrected memory, see Lessons), iOS APNs / FCM iOS, retention purge jobs (trip_locations / driver_otp_attempts / rejected-KYC R2), log scrubbing of phone numbers, Ghana counsel sign-off on legal pages, DPC registration.

## Current focus

*(updated 2026-05-16)* End of an enormous 24-hour stretch — Phases **7r-7 / 7s / 7t / 7u / 7v / 7w** all scoped + landed (or pushed-to-branch) the same day, sitting on top of the 7e → 7r-6 trips/safety/messaging foundation. Trust and triage went from "captured in the DB" to "visible to passengers + actionable for operators + defensible to regulators."

- **In flight (branches awaiting merge to `main`)**:
  - `backend feat/vehicle-photos-license-insurance` — phases 7r-7 (add-vehicle license + 5 photos + NIC pre-check), 7t (passenger trust surface), 7u (operator fleet endpoint), 7v (trip alerts + thread.trip + me.selfieUrl) **stacked**. Includes V37 Smile-user-id renumber + V39 trip_alerts. Currently on `fix/kyc-null-vehicle-handling` follow-up branch fixing the NPE noted in yesterday's open questions.
  - `mobile feat/smile-id-activation` — phases 7r-7 / 7s (Sentry .env+build-script) / 7t (trust chips) / 7v (nearby pill + alerts + selfie avatar). iPhone build rebuilt with `--dart-define=GLYDR_SENTRY_DSN=...`; awaiting first ingested Sentry event to confirm end-to-end ingestion.
  - `control-center feat/vehicles-fleet-dashboard` — `/vehicles` page with URL-as-state filter chips (insurance / license / KYC), depends on backend 7u merge.
  - `landing feat/landing-legal-pages` — 14 legal pages + `/legal` index + draft banner; waitlist removed from header/hero in a prior PR.
- **Phase 7s — Sentry mobile is ACTIVATED**. Real DSN at `roam-it-consultants/glydr` Flutter project; `.env` + `scripts/build-ios.sh` plumb dart-defines through the AOT build. The Phase 7n inert scaffold (PII scrubber, expected-error filter, `runZonedGuarded` wrapper) is what's live — sentry-wizard was almost run on top of it and would have torched the scaffold (see Lessons).
- **Phase 7w — legal coverage is the new load-bearing risk**. Pre-launch obligation under Ghana DPA 2012 (privacy policy) + need to contractualise the cost-share defence (BlaBlaCar-shaped: price cap formula, trip-frequency caps, "I'm making this trip anyway" representation, regulatory kill-switch). 14 pages live on `/legal/*` as **working drafts** behind an orange `<DraftBanner>`; Ghana-qualified counsel review queued as **Phase 7w-2**.
- **Backend Sentry is NOT wired** — Security Engineer audit caught the stale memory entry (the `pom.xml` has no `io.sentry`). Mobile Sentry is what's live; the legal pages don't overclaim. Backend wiring is now a tracked follow-up rather than an assumed state.
- **Next slice (cross-cutting)**: cross-device KYC retest on iPhone + Samsung + Tecno once the four feature branches land on `main`; confirm operator approval triggers the new push and trust chips render with real data; first Sentry event from the iPhone build.
- **Retention purge jobs queued**: `trip_locations` (target 30d), `driver_otp_attempts` (target 24h), KYC R2 objects of REJECTED submissions. All currently **indefinite** and disclosed as such on `/legal/privacy` Section 6.
- **Log scrubbing queued**: phone numbers leak into INFO-level logs at `DriverAuthService`, `WaitlistService`, `MnotifySmsNotifier`. Either downgrade to DEBUG in prod or route through a scrubber.
- **Vendor hardening still pending**: real Flutterwave wiring, real Brolly per-trip insurance, marketplace passenger-accident insurance (broker engagement — KEK / Goodwill / Hollard), PostHog activation, iOS APNs entitlement (FCM iOS still dormant), backend Sentry wiring, `R2_PUBLIC_URL` → `R2_ENDPOINT_URL` rename.

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

### Phase 7 (mobile + backend + reliability) — 2026-05-12 → 2026-05-15

- **2026-05-12** — **Brand pivot Quiet Corridor → Neon Carbon**. The dark + neon-glow system unifies landing + mobile (control-center stays Quiet Corridor for now). Driven by mobile design needs — the bone background didn't scale to Driver Home / map overlays. Wordmark route mark (●━━●) preserved; Hanken Grotesk replaces the Plus Jakarta + Inter pair. See memory `[[brand_split]]`.
- **2026-05-13** — **SSE for in-app chat** (Phase 7e). Picked over WebSockets and Firestore: SSE is one-direction (server→client), HTTP/1.1-friendly, plays with the existing Spring `WebMvc` stack, no extra connection layer to operate. Closes Q8 (real-time location transport) for the chat axis. Live-trip location uses the same SSE connection.
- **2026-05-13** — **`flutter_map` (OpenStreetMap) over Google Maps** for v1. Tile source CartoDB Dark Matter — already dark, matches Neon Carbon, free with CC-BY attribution. Zero-credential / zero-Cloud-Console / no API key. Swappable for Google Maps / Mapbox later when richer styling matters.
- **2026-05-14** — **`parentNavigatorKey` discipline** for every top-level pushed route. Without it, `system back` on Android pops the shell instead of the pushed route. Full sweep across `/kyc/*`, `/vehicle/add`, `/passenger/*`, etc. (Phase 7n).
- **2026-05-14** — **Sentry observability scaffold** — Flutter (`sentry_flutter`) + Spring boot wired but **inert until a DSN is provided**. Mirrors the "scaffold inert until configured" pattern set by Smile Identity. Backend Railway has a real DSN; mobile is dart-defined per build.
- **2026-05-14** — **SSE auto-reconnect + 30s catch-up poll**. Silent SSE drops were leaving chat threads stale; auto-reconnect re-establishes the stream and the catch-up poll closes any gap.
- **2026-05-15** — **AuthInterceptor 1-shot retry on 401/403** (Phase 7q). Cold-start race between hydrated session and provider `ref.watch` was stranding the user on a blank screen. One-shot retry + skip multipart bodies (FormData is a one-shot stream) handles the race without infinite loops.
- **2026-05-15** — **KYC in-app camera preview via `package:camera`** (Phase 7r-6). `image_picker` system-camera handoff left the framing rectangle / face-frame empty. New `EmbeddedCameraView` widget renders `CameraPreview()` inside the lime frame, `takePicture()` exposed via `GlobalKey<EmbeddedCameraViewState>`. Lifecycle handles iOS background pause-resume + Android `CameraDevice` auto-release.
- **2026-05-15** — **Smile Identity iOS bridge UNFIT** — pre-built native framework has two bugs (touch hijack via SwiftUI hosting controller, missing `didMove(toParent:)` blocking the terminal Continue button). Both bugs sit in vendor code; can't be patched from Dart. Manual photo upload promoted to first-class on both platforms. Smile Job Status Poller backstop on backend covers the case where the SDK consumes the verdict synchronously and never fires the partner-callback URL. Defer Smile widget rework until vendor ships an iOS SDK fix.
- **2026-05-15** — **`/status` screen + "Add your vehicle" intermediate REMOVED**. KYC submit lands the user directly on `/home`; an in-flight review is communicated by a soft "Listing opens once your KYC review completes" empty state on the dashboard widgets (which 403 until APPROVED). Killed two screens of forced navigation between submitting KYC and being a working driver.
- **2026-05-15** — **`KYC_DECISION` push wired backend → mobile**. `KycService` injects `PushNotifier`, fires the push immediately after the email + SMS notifiers in `decideAuthenticated`. Mobile push handler invalidates `statusControllerProvider` + driver-trips providers; the dashboard re-renders unlocked. Push is augment-only — the canonical state always comes back through `/me`.

### Phase 7r-7 → 7w (verification → trust → triage → legal) — 2026-05-16

- **2026-05-16** — **Driver licence + 5 vehicle photos + synchronous NIC insurance pre-check on add-vehicle** (Phase 7r-7). Trip-create re-verifies insurance. `INSURANCE_NOT_ACTIVE` is a hard gate, not a warning. The NIC raw response is persisted for audit (`insurance_raw_response`). Diagnostic story: NIC's `x-api-key` header convention + wrong endpoint path produced a misleading 401 — see Lessons.
- **2026-05-16** — **Single-source-of-truth records over a `trust:` sub-object** (Phase 7t). `DriverSummary` + `VehicleSummary` are already the passenger-projection boundary; extending them in place beats introducing `driver.trust = { ... }` (which would invite premature `risk:` / `compliance:` siblings).
- **2026-05-16** — **Asymmetric insurance softening: passengers see VERIFIED/PENDING, operators see ACTIVE/NO_POLICY/UNKNOWN** (Phases 7t + 7u). Passengers can't act on the granular state and `NO_POLICY` is alarming-without-being-useful for an already-booked trip; operators *need* the granular state for triage actions. Generalises: every status enum exposed in both directions should soften on the passenger side and stay raw on the operator side.
- **2026-05-16** — **`KycSubmissionRepository.findApprovedDriverIds(Collection<UUID>)` batched query** (Phase 7t) — keeps trip-list path O(1) on the KYC table regardless of page size. N+1 on a list path quietly kills trust features: every per-row trust lookup risks turning the search feel from "instant" to "thinking."
- **2026-05-16** — **Two `VehicleSummary.from(...)` factories (1-arg + 2-arg)** instead of threading `DocumentStore` through every caller (Phase 7t). The 1-arg factory encodes "this caller doesn't have trust signals to project" (create-trip return; cancelled-trip projection); 2-arg encodes "passenger-facing path."
- **2026-05-16** — **Operator fleet endpoint surfaces raw enums** (Phase 7u). `GET /v1/admin/vehicles` returns `KycStatus` (`SUBMITTED|IN_REVIEW|APPROVED|REJECTED`) and `InsuranceStatus` (`ACTIVE|NO_POLICY|UNKNOWN`) verbatim. KYC filter pre-resolves the eligible driver-id set via a batched `findLatestStatusByDriverIds(...)` query, then threads it into the vehicles Specification as `driver_id IN (?)` rather than embedding an `EXISTS (... MAX(submittedAt))` correlated subquery per row.
- **2026-05-16** — **Fleet list page is read-only by design** (Phase 7u). Zero action buttons; mutations live on a (deferred) per-row detail page after we watch operators use the list. Mutations on list views encourage scary "select all → bulk-suspend" patterns without the audit trail.
- **2026-05-16** — **URL-as-state for paginated filters** (Phase 7u control-center). Filter chips are `<Link>`s to the same page with updated query params; each chip click is a fresh server render. Client-side filter on a paginated dataset is misleading (filters only the current page); URL params survive refresh + are shareable.
- **2026-05-16** — **Plain `<img>` for R2 presigned thumbnails** (Phase 7u control-center) — avoids next.config hostname allowlisting that would diverge per-env between dev / staging / prod R2 buckets.
- **2026-05-16** — **One-shot trip alerts, region-pair exact match** (Phase 7v). `trip_alerts.satisfied_at` flips on the first match; the alert closes. Match is `(origin_region, dest_region)` equality — no corridor / radius / time-window matching yet (Ghana pilot regions are administrative units and most searches map to a single pair). `TripService.create()` fan-out is wrapped in **two layers of `try/catch`** (caller + per-push) so a bad token never aborts trip creation or the fan-out for other passengers.
- **2026-05-16** — **Additive nullable fields over v2 endpoints** (Phase 7v). `thread.trip` and `me.selfieUrl` ship as nullable additions to existing responses; every existing mobile client keeps parsing. Resist the temptation to introduce a v2 endpoint when an optional field gets the job done.
- **2026-05-16** — **`Timer.periodic(30s)` cancelled in `dispose()` over `WidgetsBindingObserver`** for the welcome-pill auto-refresh (Phase 7v). Lifecycle observers only fire on background→foreground transitions; they miss the steady-state foreground case the timer naturally handles.
- **2026-05-16** — **Sentry mobile activated via `.env` + 30-line bash wrapper, NOT via `sentry-wizard`** (Phase 7s). The wizard would have torched the Phase 7n scaffold (PII scrubber, expected-error filter, inert-by-default) and hardcoded the DSN in source. `mobile/.env` (gitignored) + `mobile/.env.example` + `mobile/scripts/build-ios.sh` forward every key as `--dart-define`. Same shape will work for Smile / Brolly / Flutterwave tokens later. Backend Sentry remains UN-wired (audit-corrected stale memory).
- **2026-05-16** — **Working-draft legal pages with explicit `<DraftBanner>`** (Phase 7w). Picked publish-with-banner over delay-until-counsel-signs-off because users today have no legal information about Glydr and pre-launch regulators evaluating us benefit from seeing exactly what we're building. 14 pages + `/legal` index, central registry in `src/content/legal.ts` drives nav + footer + sitemap. Counsel review queued as Phase 7w-2.
- **2026-05-16** — **Cost-share defence lives in the Driver Agreement, not in marketing copy** (Phase 7w). The "your car / your trip / no commercial licence required" claim has to be a binding representation by the driver with audit logs to back it — otherwise the marketing line is unsupported at regulator scale. Built into `/legal/driver-terms §4` with BlaBlaCar-shaped clauses (price-cap formula, trip-frequency caps, "journey anyway" representation, regulatory kill-switch).
- **2026-05-16** — **Honest-about-gaps over look-complete** for the privacy policy (Phase 7w). Retention windows for `trip_locations` / `driver_otp_attempts` / KYC R2 are currently *indefinite*; the policy says so plainly and names the windows we intend to ship. Better posture for a DPC inspection than overclaiming.

## Open questions

From PRD §16 (canonical) plus session-state flags. **Resolved items kept with strikethrough so the historical record stands.**

1. **Corporate structure** — separate company / Brolly subsidiary / unincorporated for POC (PRD §16 Q1). Currently `roam-labs-product` working assumption.
2. **Co-founder strategy** — solo through POC, or recruit before V1 (PRD §16 Q2). Risk table flags founder bandwidth as High/High.
3. **Commission rate at V1 launch** — 10% vs 15% (PRD §16 Q3).
4. **Brolly per-trip insurance specifics** — pricing, structure, timeline (PRD §16 Q4). Single point of failure for V1 booking flow.
5. **Legal counsel for cost-sharing review** before V1 launch (PRD §16 Q5).
6. ~~**Java vs Kotlin** for backend (PRD §11.2).~~ → **Resolved 2026-05-11: Java 21.**
7. ~~**Object storage vendor** for KYC + vehicle photos.~~ → **Resolved 2026-05-11: Cloudflare R2 + LocalFS dev fallback.**
8. ~~**Real-time location transport** for in-trip safety — Firestore sidecar vs WebSockets vs polling.~~ → **Resolved 2026-05-13: SSE for chat + live-trip location.**
9. ~~**Design system / visual direction**.~~ → **Resolved 2026-05-11: Quiet Corridor for landing + control-center.** *(updated 2026-05-12)* **Brand pivoted to Neon Carbon for landing + mobile**; control-center still Quiet Corridor for now.
10. **Brand name + domain** — "Glydr" is working only; PRD §16 Q7. (`name_confirmed: false`.)
11. **Investor capital after validation, or bootstrap from revenue** (PRD §16 Q10).
12. ~~**iOS-vs-Android-only for POC** (PRD §16 Q8).~~ → **Resolved 2026-05-15: both platforms targeted; Smile Identity widget path is iOS-blocked specifically (vendor bug). Manual KYC upload works on both.**
13. **Workspace shape** *(new 2026-05-11)* — keep root untracked (current state) or promote to a wrapper repo? Workspace got SLIMMER over Phase 7 (PRD + docker-compose + infra/ moved into the `docs/` repo, only `BRAIN.md` + 5 sibling clones remain at the root). Still untracked.
14. **PRD ↔ landing divergence** *(new 2026-05-11, still open)* — PRD v0.3 still pending; meanwhile the docs/ repo has 19 phase docs (7a → 7r-6) that effectively serve as the live source of truth for the current build.
15. ~~**Driver auth shape for next slice** *(new 2026-05-11)* — phone-OTP via mnotify.~~ → **Resolved + shipped 2026-05-12: phone-OTP via mnotify with auto-fill from incoming SMS (Phase 6f), local PIN + biometric unlock (6g).**
16. **Smile Identity iOS SDK fix timeline** *(new 2026-05-15)* — vendor needs to patch the SwiftUI hosting controller's touch hijack + add `didMove(toParent:)` for iOS 26 lifecycle. No ETA. Manual upload covers both platforms in the meantime; revisit Smile widget path when a patched `smile_id ^11.x` lands.
17. **R2 env var rename** *(new 2026-05-15)* — `R2_PUBLIC_URL` is misleadingly named (it's actually the SigV4 endpoint). Rename to `R2_ENDPOINT_URL` + add a separate `R2_PUBLIC_BASE_URL` for actual public download links. Coordinate with Railway env var migration.
18. ~~**Backend NPE in `fireOperatorSubmissionAlert`** *(new 2026-05-15)* — `vehicle.getPlateNumber()` without a null check NPEs when KYC is submitted without vehicle fields, gets swallowed into a generic 500.~~ → **Resolved 2026-05-16: null-guarded across queue projection (`bc32feb`), operator detail (`f60634a`), operator submission alert (`4dee4a9`), control-center detail + queue pages (`cae389a`); email also made optional in authenticated KYC submission (`ff171e8`).**
19. **Ghana counsel review** *(new 2026-05-16)* — 14 legal pages live on `/legal/*` as working drafts behind `<DraftBanner>`. Phase 7w-2 brief: Ghana-qualified commercial lawyer; 2–3 weeks; final language replaces drafts and `<DraftBanner>` drops everywhere via the central registry.
20. **Cost-share legal classification** *(new 2026-05-16)* — defensible by Ghana mirror of BlaBlaCar's EU defence (price cap formula, trip-frequency caps, "journey anyway" representation), now built into the Driver Agreement, but untested in Ghana courts. Single largest legal risk Glydr carries; defence sits in contracts + audit logs, not in marketing copy.
21. **Marketplace passenger-accident insurance** *(new 2026-05-16)* — broker engagement (KEK / Goodwill / Hollard) for platform-level passenger-accident cover. Both defensive (concrete answer to "what happens if a passenger gets hurt") and a marketing differentiator. `/legal/insurance §6` is shaped to absorb the policy schedule when in force.
22. **DPC registration** *(new 2026-05-16)* — file with Ghana's Data Protection Commission, publish the certificate number on `/legal/privacy`. Operational task; blocked on registered-company finalisation (also Q1).
23. **Retention purge jobs** *(new 2026-05-16)* — `trip_locations` (target 30d), `driver_otp_attempts` (target 24h), KYC R2 objects of REJECTED submissions. Currently indefinite and disclosed as such on `/legal/privacy §6`.
24. **Log scrubbing** *(new 2026-05-16)* — phone numbers leak into INFO-level logs at `DriverAuthService`, `WaitlistService`, `MnotifySmsNotifier`. Either downgrade to DEBUG in prod or route through a structured-field scrubber.
25. **Backend Sentry wiring** *(new 2026-05-16)* — Memory previously claimed backend Sentry was live; the `pom.xml` has no `io.sentry`. Memory has been corrected ([[project_sentry_setup]]); backend wiring is now a tracked follow-up rather than an assumed state.
26. **iOS push (APNs entitlement + `GoogleService-Info.plist` bundling)** *(re-stated 2026-05-16)* — FCM iOS path remains dormant. Trip alerts on iOS fall back to in-app refresh on next open until APNs lands. Cross-references Q12-resolution caveat.

## Lessons learned

Three patterns surfaced during the 2026-05-11 build session:

1. **Marketing-vs-product design system split** — for any project with both a marketing surface and a product surface, hand-rolled Tailwind for marketing wins (visual control, no third-party aesthetic baggage), but adopt shadcn-or-equivalent at the product surface where component density is high. Worked examples: this project + [[wiki/projects/coffee-break-with-big-sis|Coffee Break]]. Could be promoted to a concept page once a third worked example lands.
2. **Fail-soft env-gated notifier pattern** — single notifier impl serves dev (logs) and prod (calls vendor) based on env-var presence. Avoids `@Profile` bean overrides + `@ConditionalOnProperty` ceremony. Much easier reasoning at runtime: one log line at startup tells the operator whether the integration is hot. Worked examples: `ResendEmailNotifier` + `MnotifySmsNotifier` (now also `PushNotifier` / `FcmPushNotifier`).
3. **JPA `:param IS NULL` cursor-pagination Postgres footgun** — when a nullable JPQL parameter appears only in `:param IS NULL` context, Postgres can't infer its type and returns `ERROR: could not determine data type of parameter $N`. Hibernate doesn't help. Fix: split into two methods (cursor-present + cursor-absent) and route at the service layer. Cleaner than native query with explicit cast. Worth a concept page if it shows up on another project.

Five more from the Phase 7 stretch (2026-05-12 → 2026-05-15):

4. **Vendor SDKs that ship pre-built native frameworks can't be patched from Dart** — Smile Identity's iOS framework has two bugs (touch hijack + missing `didMove(toParent:)`) that block end-to-end KYC on iPhone. Both sit in vendor code; Dart can't reach them. Lesson: every vendor-SDK widget path needs a fallback path on day one (manual upload here). When the vendor SDK breaks on a platform, you don't want to be stuck shipping nothing for a week. Worth a concept page when a second example lands (Brolly insurance API will probably qualify).
5. **Env var names are load-bearing documentation** — `R2_PUBLIC_URL` set on Railway was actually the SigV4 endpoint variable; the user pasted the actual public-read `pub-...r2.dev` URL into it (because that's what "public" suggests). Result: silent 401 on every PutObject for a full afternoon. The variable is being renamed to `R2_ENDPOINT_URL` to match what it actually does. Rule: an env var named X should mean X. If "public URL" can be either an auth endpoint or a download base, split into two vars with names that disambiguate.
6. **iOS debug builds need `flutter run` attached forever** — debug-mode Flutter apps use a JIT-compiled VM that iOS only allows when the Dart debugger is actively attached (ptrace). Tap the app icon on the home screen → ptrace fails → black screen. For standalone home-screen launches during dev, build profile or release mode (AOT). Tripped me + the user across multiple sessions.
7. **`flutter run` install-and-launch is unreliable on iOS 26.5** — "Timed out waiting for CONFIGURATION_BUILD_DIR to update." Apple's tightened automation security around Xcode keeps breaking flutter's tooling. Workaround: `flutter build ios --profile`, then install with `xcrun devicectl device install app --device <UUID> build/ios/iphoneos/Runner.app`. The build is fine; only the install-and-launch via flutter automation is flaky.
8. **`go_router` parent route's `redirect` callback receives `state.matchedLocation` as the parent's own segment, NOT the full requested URL** — Phase 7r-5's "fix" of `state.matchedLocation == '/kyc' ? '/kyc/verify' : null` was true for every child path because `matchedLocation` at the `/kyc` redirect resolves to `/kyc`, not `/kyc/ghana-card-front`. `state.uri.path` is the full requested URL — use that for "only redirect on the parent itself" patterns. Cost: a half-day chasing why every KYC navigation bounced back.

Eleven more from the Phase 7r-7 → 7w stretch (2026-05-16):

9. **Don't run vendor wizards on top of existing scaffolds.** *(Now has two examples — Sentry + Smile — and is concept-page-worthy.)* Sentry's `sentry-wizard -i flutter` would have torched the Phase 7n bootstrap (PII scrubber, expected-error filter, inert-by-default) and replaced it with boilerplate `SentryFlutter.init` in `main.dart`, set `sendDefaultPii = true`, hardcoded the DSN, and added a sample `throw StateError(...)` on every cold launch. Caught and reverted in Phase 7t. Vendor wizards optimise for greenfield directories; if there's already integration, treat the wizard as a one-shot DSN-fetcher and revert its code changes. **Companion lesson**: Smile Identity's iOS framework was the same shape — pre-built vendor code Dart can't reach in. Both vendor-integration paths need (a) a non-vendor fallback on day one and (b) discipline against letting vendor tooling rewrite your scaffolding.
10. **Agent audits catch stale memory.** The Security Engineer agent flagged that backend Sentry was *not* live, contradicting the memory entry. Five minutes' read of `pom.xml` settled it. Two consequences: (a) memory was patched ([[project_sentry_setup]]), and (b) `/legal/privacy` doesn't overclaim about backend error monitoring. Generalises: when memory state and codebase state diverge, the codebase wins, and audit agents are good at finding the divergence.
11. **Honest "PENDING" beats misleading "NO POLICY" on already-booked surfaces.** Surfacing NIC's raw `NO_POLICY` to a passenger who already booked (or is about to book) doesn't help them — the trip exists, the booking is open, an alarming red banner just damages trust without giving them anything to act on. PENDING is the conservative read. Reserve alarming verdicts for paths where the user can *act* on them — driver-side and operator-side.
12. **Operator views should NOT inherit passenger softening.** Phase 7t mapped `NO_POLICY` / `UNKNOWN` → `PENDING` for passengers. Reusing that softening on `/v1/admin/vehicles` would destroy the triage workflow — operators *need* the granular state to know which action to take. Default rule: passenger surfaces honest-but-soothing; operator surfaces precise.
13. **Misleading entity field names cost time — inspect, don't assume.** `User.status` sounded like "the user's KYC status." It's actually `UserStatus(PENDING|ACTIVE|SUSPENDED)` — account suspension state, completely unrelated to KYC verdict. Real KYC verdict is on `KycSubmission.status` per submission, and a driver can have multiple submissions over time. The backend agent caught this by *reading the schema* before writing the read. Five extra minutes; saved a half-day downstream.
14. **N+1 on a list path quietly kills trust features.** Every trust signal added risks a per-row lookup that turns search from "instant" into "thinking." The `findApprovedDriverIds(Collection<UUID>)` + `findLatestStatusByDriverIds(Collection<UUID>)` pattern (batched ids → in-memory set or map) generalises: anywhere you're rendering a list of items each carrying a derived flag, the flag-computation query should be `WHERE id IN (?, ?, ?, ...)` *once*, not `WHERE id = ?` N times.
15. **Two-layer `try/catch` on fire-and-forget fan-out.** `TripService.create()` wraps `TripAlertService.matchAndFire(trip)`, AND `matchAndFire` wraps each per-passenger push in its own inner `try/catch`. Trip creation is a paid driver action that must never fail because of an alerts-side bug, AND a single bad device token shouldn't abort the fan-out for the remaining passengers on the same route. Pattern generalises to any side effect attached to a primary transaction.
16. **URL-as-state beats client-side filter for paginated lists.** A snappy in-memory filter on a paginated dataset is *misleading* — it only filters the current page, so matching rows on other pages disappear. URL params are one server render away, refreshable, and shareable in Slack. Reach for client-side filter only when the full dataset fits in one fetch.
17. **Additive nullable field beats v2 endpoint.** `thread.trip` and `me.selfieUrl` shipped as nullable additions; every existing mobile client kept parsing fine. Costs ~3 lines on each side; saves the entire migration / dual-deploy / deprecation conversation.
18. **AOT-baked dart-defines don't grep for as raw ASCII.** Confirming whether a dart-define value reached a profile/release build via `grep -ao "<value>" Runner.app/Runner` returns 0 even when the value IS in the binary — Dart's AOT snapshot interns string constants. The right verification path is runtime: trigger an event and watch Sentry. For build-time checks, `print(kSentryEnabled)` in the boot path and inspect device console output.
19. **`.env` + 30-line bash wrapper beats reaching for a build tool.** Resisted `make` / `just` / a Dart build runner for dart-define plumbing. One key=value file + one bash script reads top-to-bottom; anyone fluent in bash audits it in a minute. Reach for richer tooling when a second concern joins (release upload, source maps, multi-platform orchestration).
20. **Cost-share defence has to live in contracts, not in copy.** The marketing line "your car / your trip / no commercial licence required" is unsupported until those concepts appear as binding representations in the Driver Agreement, with audit logs backing them. Phase 7w put them in `/legal/driver-terms §4`. The general lesson: any defensible legal positioning needs (a) marketing-side framing AND (b) contractual expression AND (c) audit-able operational evidence. Two without the third is theatre.

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

*(updated 2026-05-16)*

- **Repos** (all under `github.com/kobbyopoku/`):
  - https://github.com/kobbyopoku/glydr_backend
  - https://github.com/kobbyopoku/glydr_landing
  - https://github.com/kobbyopoku/glydr_cc
  - https://github.com/kobbyopoku/glydr_mobile
  - https://github.com/kobbyopoku/glydr_docs
- **Live surfaces**:
  - `glydr.app/legal/*` — 14 working-draft legal pages + `/legal` index (Phase 7w; behind `<DraftBanner>` until counsel sign-off).
  - Railway `glydr-staging` — backend deploys on push to `main`.
- **Project's own CLAUDE.md**: _(none — `BRAIN.md` at workspace root is the only top-level marker)_
- **Project memory dir**: `~/.claude/projects/-Users-kobbyopoku-ROAM-CascadeProjects-glydr/memory/` — auto-memory accumulating cross-session facts (brand split, Smile iOS bugs, Sentry setup *(corrected 2026-05-16: backend NOT wired)*, agent worktree CWD pitfall, device_tokens race, etc.).
- **PRD**: ⚠️ **No longer at workspace root**. Moved into the `docs/` repo (or pruned — needs reconciliation). v0.3 absorption is still pending. Phase docs in `glydr_docs/phases/2026-05-1*-phase-7*.md` are the de-facto live source of truth.
- **Phase docs**: [`docs/phases/`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/docs/phases) — **25** dated docs covering Phase 7a → 7w (live-trip, payouts, ratings, safety, messaging, pickup-code, reliability sweep, KYC productionization, add-vehicle license+photos+insurance, Sentry mobile activation, passenger trust surface, operator fleet dashboard, passenger personalization + trip alerts, landing legal pages).
- **Landing DESIGN.md**: [`landing/DESIGN.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/landing/DESIGN.md) — modified locally (Neon Carbon update in flight; uncommitted at brain-update time).
- **Architecture docs scaffold**: [`docs/architecture/`](file:///Users/kobbyopoku/ROAM/CascadeProjects/glydr/docs/architecture) — partial; phase docs serve as the de-facto living architecture record.
