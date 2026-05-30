---
type: project
title: AfriMart
created: 2026-05-30
updated: 2026-05-30
status: active
repo: not-yet — local-only workspace; git not initialized as of 2026-05-30. Monorepo planned at `github.com/kobbyopoku/afrimart` (single-repo, pnpm + Turborepo).
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/africart
stack: [typescript, nestjs, fastify, postgres-16, postgis, redis, bullmq, drizzle-orm, drizzle-kit, zod, nextjs-15, react-19, tailwindcss-v4, expo-sdk-53, react-native, tamagui, stripe-connect-standard, stripe-tax, twilio-whatsapp, twilio-sms, uber-direct, resend, cloudflare-r2, lucia-or-better-auth, sentry, axiom, posthog, railway, vercel, eas, github-actions, turborepo, pnpm-workspaces]
started: 2026-05-29
ended:
owner_org: roam-labs
affiliation: roam-labs-product
name_confirmed: true
brand_name_status: confirmed
repo_topology: monorepo-planned
aliases: [afrimart, africart]
tags: [project, marketplace, two-sided, grocery, african-diaspora, houston, instacart-for-x, multi-store-fulfillment, stripe-connect, marketplace-facilitator, pre-implementation]
---

# AfriMart

> **Lineage**: ROAM Labs owned product ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder + builder). Pre-implementation as of 2026-05-30 — design spec + pitch PDF exist; no code yet, no git repo yet.

> **Repo topology**: monorepo planned (pnpm workspaces + Turborepo). Local workspace at `/Users/kobbyopoku/ROAM/CascadeProjects/africart` contains a pitch PDF (`AfriMart_StoreOwner_Pitch.pdf`) + a design spec at `docs/superpowers/specs/2026-05-29-afrimart-marketplace-design.md`. Git not yet initialized.

> **One-sentence framing**: An Instacart-style marketplace that aggregates existing Houston African-owned grocery stores under a unified product catalog, with split-fulfillment multi-store carts, AfriMart-as-merchant-of-record payments via Stripe Connect, and Uber Direct delivery — targeting the Houston African diaspora as v1 market and an Africa-to-US import line as Phase 2.

## What and why

AfriMart is a two-sided marketplace connecting African diaspora customers in Houston, TX with the city's existing African-owned grocery stores. Customers shop a unified canonical-product catalog, can mix items from multiple stores in one basket, and pay AfriMart, which collects Texas sales tax (as marketplace facilitator under the post-2019 law), takes a small per-order service fee from the customer, and pays stores via weekly Stripe Connect payouts. v1 is intentionally a software-first aggregator over 3–5 pilot stores; stores keep 100% of product revenue, fulfill orders themselves, and hand off to Uber Direct drivers at pickup. Catalog is built by a field team that photographs each store's SKUs and uses AI-assisted normalization to map them to canonical products.

The strategic positioning is "Instacart for African diasporas" — Houston has 90,000+ Nigerian-Americans alone plus tens of thousands of Ghanaians, Ethiopians, Cameroonians, Senegalese, and others who currently drive 30–45 minutes to reach an African store, or default to Walmart / Weee! for convenience. The competition that actually matters is **Weee!** (which is expanding into African groceries), not Walmart. v1 success unlocks a deliberately separate Phase 2 — source produce directly from Africa, operate as a vertically integrated importer with FDA/USDA/CBP/FSMA compliance, and use AfriMart as the distribution channel. Phase 2 is recorded in the design spec as a separate business; v1's modular monolith is architected so the import line can layer on without an architectural rewrite.

The full v1 design lives at `docs/superpowers/specs/2026-05-29-afrimart-marketplace-design.md` in the project workspace (10 sections, ~5,000 words; 12 locked architecture decisions; 9 open questions). The pitch PDF at the project root (`AfriMart_StoreOwner_Pitch.pdf`) is the store-facing positioning artifact — consistent with the design except for three claims that need updating before it ships: (1) "Day 1 your store is live", (2) "we coordinate our driver network" (actually Uber Direct in v1), and (3) the service-fee model needs disclosure to defuse the "what's the catch" reaction the current `$0 commission` framing triggers.

## Stack and infrastructure

**Pre-implementation**: nothing is wired today. The stack list below is the *intended* v1 stack from the design spec. All items are commitments-on-paper, not running systems.

- **Repo topology**: monorepo planned (`afrimart/` with `apps/`, `packages/`, `db/`, `ops/`, `docs/`). pnpm workspaces + Turborepo. Single GitHub repo `github.com/kobbyopoku/afrimart` (not yet created).
- **Languages / frameworks**:
  - Backend: TypeScript / NestJS (Fastify adapter) — single modular monolith with 9 bounded-context modules (`catalog`, `identity`, `cart`, `orders`, `payments`, `delivery`, `store-ops`, `notifications`, `search`). HTTP surface grouped by audience under `api/customer/*`, `api/store/*`, `api/admin/*`, `api/webhooks/*`.
  - Web: Next.js 15 (App Router, RSC), React 19, Tailwind v4 — three separate apps (`web-customer`, `web-store`, `web-admin`) deployed under subdomains of `afrimart.com`.
  - Mobile: Expo SDK 53 + Expo Router (React Native iOS + Android). Same routing semantics as the Next.js App Router; UI primitives shared via Tamagui in `packages/ui/`.
  - WhatsApp: Node worker consuming Twilio WhatsApp Business API webhooks → backend API.
- **Database**: Postgres 16 (Neon-managed) with PostGIS extension for store + delivery geo. Drizzle ORM, `drizzle-kit` migrations. Single Postgres for v1; no sharding; no read replicas yet.
- **Cache + queues**: Redis (BullMQ for delayed jobs — 15-min suborder ack timers, payout schedules, daily store availability reminders, notification retries).
- **Search**: Postgres FTS for v1 (≤500 SKUs); promote to Typesense at v1.5 when canonical catalog crosses ~2,000 SKUs.
- **Object storage**: Cloudflare R2 (S3-compatible, no egress fees) for product images + receipt images.
- **Payments**: Stripe Connect Standard with AfriMart as platform + merchant of record. Stripe Tax for Texas marketplace facilitator sales-tax calculation + remittance. Per-suborder transfers + weekly ACH payouts to stores.
- **Delivery**: Uber Direct API. One delivery per suborder; 3-store order = 3 deliveries; customer pays a bundled displayed fee; AfriMart absorbs the variance. Webhook-driven status mirror. Owned driver network deferred to Phase 2.
- **Notifications**: Twilio (SMS + WhatsApp), Expo Push (iOS/Android), Resend (email). All dispatched via the `notifications` module.
- **Auth**: Lucia or Better-Auth — phone OTP for customers + stores, email magic link as fallback, strong-password + 2FA for admin. Decision between Lucia and Better-Auth pending.
- **Observability**: Sentry (errors + release tagging), Axiom (structured logs), Posthog (product analytics + feature flags + session replay on web). PagerDuty or Better Stack for on-call.
- **CI/CD**: GitHub Actions. Railway for backend (api + whatsapp-bot + worker + redis as services under one project) + Neon Postgres attached. Vercel for the three Next.js apps. EAS for Expo builds → TestFlight + Play Internal Track from week 14.
- **Domain-event runtime**: NestJS `EventEmitter2` in-process for v1. Promote to Redis Streams or an external broker only when a module gets extracted into its own service.
- **IaC**: none in v1. Railway + Vercel managed.
- **Local dev**: planned one-command bootstrap (`pnpm install && pnpm db:migrate && pnpm db:seed && pnpm dev`) brings up backend + 3 web apps + worker against docker-compose Postgres + Redis. Stripe CLI + Uber Direct sandbox + Twilio test creds.

## Current focus

**Phase 0 (Weeks 1–2 of the design's 20-week timeline) — foundations + regulatory threads.**

The design spec calls out several critical-path items that must start in week 1, *not* week 12, because their approval timelines are longer than the engineering work that depends on them:

- **Stripe Connect platform application** — 2–4 weeks approval.
- **A2P 10DLC SMS registration** (Twilio Texas SMS) — 2–8 weeks.
- **WhatsApp Business display-name verification** — 1–3 weeks.
- **Apple Developer + Google Play developer accounts** — short but non-zero delays.
- **CPA engagement** for Texas marketplace facilitator sales-tax filings.
- **Marketplace lawyer engagement** for ToS, privacy policy, marketplace facilitator terms, store agreement, driver pass-through terms.
- **Legal entity + EIN** — required before Stripe Connect application.
- **Insurance** (marketplace liability + cyber + general liability) — quote required by week 4.

Engineering-side, Phase 0 is monorepo + CI + auth scaffolding + schema migrations + seed + catalog data model + admin CRUD shell. As of 2026-05-30 none of this is started; project is at scaffolding-files-only stage.

**Project-meta tasks queued (2026-05-30)**: brain page created; project-root CLAUDE.md + AGENTS.md + scaffolded monorepo skeleton being produced this session (per user request following brain-add). Pre-implementation work; no production code.

## Architecture decisions

Twelve foundational decisions locked during the 2026-05-29 brainstorming session. All carry the same date because they were debated in sequence as a single design conversation; rationales are in §1.1 of the design spec.

- **2026-05-29** — **Marketplace aggregator over direct import** as the v1 business model. The pitch initially blurred two business shapes (aggregate Houston African stores vs. source produce in Africa and import). Phase 2's import line is a separate, capital-intensive, regulated business (FDA / USDA / CBP / FSMA, cold chain, customs); validating diaspora demand on a software-first marketplace must come first. The design spec records Phase 2 as informational only.
- **2026-05-29** — **3–5 pilot stores in Houston** as v1 scope, not city-wide and not multi-city. Limits cohort to validate marketplace dynamics (not just one store) while keeping catalog ops + onboarding tractable. Catalog data entry for the cohort is the launch's critical path, not engineering.
- **2026-05-29** — **Store staff picks orders (not independent shoppers)**. v1 stays one-sided on the supply side; no shopper recruitment, no in-store training, no virtual cards. Trade-off explicitly accepted: depends on store reliability + accuracy.
- **2026-05-29** — **Unified canonical product catalog with per-store mapping**, not browse-by-store. Better discovery + customer UX. Trade-off: SKU normalization is the hardest catalog problem in the African-grocery vertical (stockfish alone has 4+ origins × 3+ sizes × 5+ brands under inconsistent names). Catalog ops becomes an ongoing function, not a one-time engineering task.
- **2026-05-29** — **Multi-store cart with split-fulfillment** (one cart → N suborders → N stores → N Uber Direct deliveries → bundled displayed delivery fee + AfriMart-absorbed variance). The most complex single mechanic in the system; concentrates risk in one module (`orders`).
- **2026-05-29** — **AfriMart is merchant of record** (Stripe Connect Standard). Customer pays AfriMart; AfriMart remits Texas sales tax under the post-2019 marketplace facilitator law (the PDF pitch does not disclose this and must be updated). Per-suborder transfers + weekly ACH payouts to stores. AfriMart owns the customer relationship + data.
- **2026-05-29** — **Uber Direct API for delivery in v1**, owned driver network later. Building a 1099 gig fleet is its own startup; Uber Direct's API ($7–$12 per delivery in Houston) lets v1 ship in days on a fully solved logistics layer. Owned fleet unlocked at Phase 2 if economics + volume justify (rule-of-thumb threshold ~100 deliveries/day in a single market).
- **2026-05-29** — **Three customer surfaces**: React Native (Expo) iOS + Android app, responsive Next.js web (PWA-capable), Twilio WhatsApp Business bot. Headless backend, all three consume the same OpenAPI-generated client. Trade-off: triples the frontend surface area at v1; coherent only because of the headless architecture.
- **2026-05-29** — **Catalog built by field team + AI-assisted normalization**, not store self-serve (small African grocery stores won't reliably maintain catalogs themselves). Field team photographs SKUs, AI drafts entries (Claude vision), human reviews + maps to canonical. ~1–2 days per store.
- **2026-05-29** — **Daily availability snapshot + per-order confirm-or-substitute** for inventory, not POS integration (rarely feasible at small African groceries) and not blind catalog-equals-available (worst customer experience). Customer sets substitution preference per cart item (`allow_any` / `confirm_each` / `refuse`); store ack window is 15 minutes; payment is manual-capture with +10% authorization headroom for substitution price deltas.
- **2026-05-29** — **Modular monolith over microservices**. 9 bounded-context modules inside a single NestJS deployable, single Postgres, single Redis. Microservices rejected as premature for a 2–4 person team on a 4–6 month timeline; commerce-platform fork (Medusa.js / Shopify Multi-Vendor) rejected because split-fulfillment + canonical-SKU-with-per-store-mapping fight the framework. Modules extractable later when load justifies — bounded contexts are strict.
- **2026-05-29** — **Stripe Connect Standard, not Express or Custom**. Stores onboard via Stripe-hosted KYC flow; AfriMart doesn't take on the KYC operations burden. Trade-off: stores see Stripe-branded payout statements; weighed acceptable.

## Open questions

Carried forward from §9 of the design spec. None block design approval; all should be resolved by end of Phase 0 (Week 2).

- **2026-05-29 — Sales tax CPA.** Named CPA + signed engagement letter required before the Stripe Connect platform application goes in. Find someone who has filed Texas marketplace facilitator returns before.
- **2026-05-29 — Service fee structure.** PDF pitch says "$1–$3 paid by customer". Need to choose between flat-per-order, percentage of subtotal, or banded by basket size. Affects checkout UI + payments module.
- **2026-05-29 — Delivery fee model.** Bundled (single displayed fee, AfriMart absorbs the variance between multi-store Uber Direct charges) vs. per-store (transparent but multi-line). Spec recommendation: bundled.
- **2026-05-29 — Pilot store identities.** Who are the 5? Verbal commits, signed LOIs, or cold prospects? Direct impact on launch timeline.
- **2026-05-29 — Founder identity in app + marketing.** Strong trust signal for the diaspora audience. About-page profile photo + bio + Houston/African heritage framing.
- **2026-05-29 — Languages for v1.1.** Pick top 2–3 to translate (likely Yoruba + Twi + Amharic) so the `packages/i18n/` infra has real targets from day one. v1 ships English-only.
- **2026-05-29 — Legal entity + EIN.** Required before Stripe Connect application. Decide LLC vs. C-corp; jurisdiction (Delaware vs. Texas).
- **2026-05-29 — Insurance.** Marketplace liability + cyber + general liability. Quote required by week 4.
- **2026-05-29 — Marketplace lawyer engagement.** Engagement letter by week 2 for ToS, privacy policy, marketplace facilitator terms, store agreement, driver pass-through terms.

## Lessons learned

*Pre-implementation; no production lessons yet. The brainstorming session itself produced a few patterns worth keeping in mind for future implementation:*

- **Pitch artifacts can diverge from product reality in dangerous ways.** AfriMart's PDF pitch describes a marketplace aggregator while a casual founder statement described a vertically integrated importer — wildly different businesses. Pattern: every pitch artifact should be diff'd against the locked design before it ships. Recorded in design spec §1 ("The pitch artifact... is consistent with this design except where noted").
- **"$0 commission" framing on a sustainable marketplace triggers the 'what's the catch' reaction.** Store owners pattern-match small-business operators to spot hidden costs. The economics must visibly pencil out (here: $1–$3 customer service fee × order volume + future SaaS tier). The PDF needs to either disclose the bridge funding model or restructure to a believable economic story. Pattern is project-specific but generalizes to any "free for X" go-to-market that isn't credibly funded.
- **Texas marketplace facilitator law makes the marketplace, not the store, responsible for sales tax** when the marketplace processes payments. Hidden cost the PDF doesn't address; surfaced in §6 of the design spec as the single biggest unaddressed economic burden in the v1 model.

## Related

- **Concepts**: *(no concept pages link yet; candidates for future ingest: "marketplace facilitator law", "split-fulfillment", "merchant-of-record-models", "canonical-sku-normalization")*
- **Entities**:
  - [[wiki/entities/godwin-opoku-duah]] — owner of this wiki; AfriMart founder.
  - [[wiki/entities/roam-labs]] — owner org.
  - [[wiki/entities/stripe]] — payments + Stripe Connect platform + Stripe Tax.
  - [[wiki/entities/uber]] — Uber Direct API (delivery).
  - [[wiki/entities/instacart]] — closest functional analogue (multi-store grocery marketplace); referenced as the structural blueprint.
  - [[wiki/entities/doordash]] — secondary analogue (store-picks model historical precedent).
  - [[wiki/entities/anthropic]] — Claude vision for the AI-assisted catalog normalization workflow.
  - [[wiki/entities/sentry]] — error tracking.
  - [[wiki/entities/posthog]] — product analytics + feature flags.
  - [[wiki/entities/vercel]] — Next.js hosting.
  - [[wiki/entities/expo]] — React Native mobile platform.
  - [[wiki/entities/resend]] — transactional email.
  - [[wiki/entities/supabase]] — *not used* — Neon Postgres chosen for v1.
  - [[wiki/entities/superpowers]] — workflow plugin used during the 2026-05-29 brainstorming session that produced the design spec.
- **Sources**: *(none — no external sources were directly cited in the design)*
- **Other projects**:
  - [[wiki/projects/stacesprouts]] — sibling ROAM Labs client-work commerce platform (storefront + admin + Flutter POS); shares Stripe + Flutterwave-adjacent patterns and African-market context.
  - [[wiki/projects/glydr]] — sibling ROAM Labs owned product; also a two-sided marketplace (peer-to-peer carpooling); shares operator dashboard + KYC + payment-rails patterns; different vertical.
  - [[wiki/projects/brolly]] — Brolly Africa owned platform; possible future integration partner if AfriMart adds driver/cart insurance at Phase 2.

## External links

- **Pitch PDF**: `/Users/kobbyopoku/ROAM/CascadeProjects/africart/AfriMart_StoreOwner_Pitch.pdf` — v1 store-owner positioning artifact (4 pages; needs 3 updates before shipping — see "Lessons learned").
- **Design spec**: `/Users/kobbyopoku/ROAM/CascadeProjects/africart/docs/superpowers/specs/2026-05-29-afrimart-marketplace-design.md` — 10-section v1 marketplace design produced by `superpowers:brainstorming` on 2026-05-29; the durable source of truth for the project's architecture, scope, sequences, stack, scope cuts, timeline, and resilience/observability/testing approach.
- **Repo**: not yet created. Planned at `github.com/kobbyopoku/afrimart` (single monorepo).
- **Project's own CLAUDE.md**: `/Users/kobbyopoku/ROAM/CascadeProjects/africart/CLAUDE.md` *(being created in the same session as this brain page; agent contract for the project)*.
- **Project's own AGENTS.md**: `/Users/kobbyopoku/ROAM/CascadeProjects/africart/AGENTS.md` *(same)*.
