---
type: project
title: Coffee Break With Big Sis
created: 2026-05-09
updated: 2026-05-09
status: active
repo: multi-repo (github.com/kobbyopoku/cbwbs-frontend, github.com/kobbyopoku/cbwbs-backend; outer wrapper has no remote)
local_path: /Users/kobbyopoku/Projects/CoffeeWithBigSis
stack: [java-17, spring-boot-3.4, postgres-15, redis-7, liquibase, jwt, react-19, typescript-5.9, vite-7, tailwind-v4, zustand-5, react-router-7, react-hook-form, zod, axios]
started: 2026-02-20
owner_org: roam-labs
affiliation: roam-labs-client-work
aliases: [cbwbs, coffee-with-big-sis]
tags: [project, multi-tenant, mentorship, networking, alumni, saas]
---

> **Lineage**: client work delivered through [[wiki/entities/roam-labs|ROAM Labs]] ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder). Services contract — IP is the client's, not ROAM-owned product.

# Coffee Break With Big Sis

> Multi-tenant networking and mentorship SaaS that gives institutions (universities, alumni chapters, professional bodies, community groups) a branded workspace to reconnect members, run mentor↔mentee matching, host events, and publish content.

## What and why

Coffee Break With Big Sis (CBWBS) is built around a single conviction: the institutions that shaped you are the most powerful network you have. Each tenant gets schema-isolated PostgreSQL via a custom `MultitenantDataSource` + ThreadLocal `TenantContext` + `TenantInterceptor` that issues `SET SCHEMA` on every connection, branded onboarding (logo, banner, color theme, slug), and the full feature surface: member directory + admin-gated registration, weighted-Jaccard mentor-mentee matching across 6 dimensions (areas, skills, interests, frequency, duration, communication style), event lifecycle (DRAFT → PUBLISHED → CANCELLED with capacity + paid/free), and a content CMS with DRAFT/PUBLISHED/ARCHIVED. Every backend endpoint wraps in `ApiResponse<T>` and routes errors through `GlobalExceptionHandler`. Self-serve onboarding, no sales motion. Production target is institutional small-to-mid scale (alumni chapters of 100–10k people).

## Stack and infrastructure

- **Backend (`backend/`)**: Spring Boot 3.4.6, Java 17, Maven. PostgreSQL 15 + Liquibase (18 changesets through `017-seed-data` + `018-performance-indexes`), Redis 7 cache (currently only `tenants` cache active; 6 others configured but unused), JWT (jjwt 0.12.3) + BCrypt + DB-stored refresh-token rotation (24h access / 7d refresh), HikariCP (max pool 20). 8 controllers / ~62 endpoints, 23 JPA entities, 9 services. SpringDoc OpenAPI / Swagger UI. Maven artifactId is `alumni-management` — vestigial naming from before the project was renamed.
- **Frontend (`frontend/`)**: React 19.2, TypeScript 5.9, Vite 7.3, Tailwind CSS v4 (`@theme` CSS-first config), Zustand 5 (persist middleware for auth + theme stores), React Router 7, React Hook Form + Zod, Axios with `X-Tenant-ID` interceptor, Lucide icons, shadcn-pattern UI primitives. Feature-based structure under `src/features/`. Caveat + Fraunces + Instrument Sans + Instrument Serif webfonts via Google Fonts. Dark mode via `.dark` class on `<html>` driven by Zustand store with system-preference fallback.
- **Repos**: `github.com/kobbyopoku/cbwbs-frontend`, `github.com/kobbyopoku/cbwbs-backend`. The outer wrapper at `/Users/kobbyopoku/Projects/CoffeeWithBigSis` has no `.git` and no remote — it's a working directory holding shared `README.md`, `PLAN.md`, and `docs/` (`ARCHITECTURE.md`, `API.md`, `SETUP.md`).
- **Deploy**: Frontend on Vercel (`tsc -b && vite build`); backend deploy target not yet finalized (Docker Compose only for local; managed PG/Redis intended for prod). Vercel build initially failed on the editorial-redesign push due to TS2783 in `login-page.tsx`; fix landed in `5a58f7a` on 2026-04-11.
- **Roles**: `SUPER_ADMIN` (platform), `TENANT_ADMIN` (institution admin), `MENTOR` ("Big Sister"), `MENTEE` ("Little Sister"), `MEMBER`. Approval workflow `PENDING → APPROVED / REJECTED / SUSPENDED` gates all member registration.
- **Routing**: every authenticated request needs both `Authorization: Bearer <jwt>` and `X-Tenant-ID: <id>` headers; `/auth/**`, `/swagger-ui/**`, `/v3/api-docs/**`, `/actuator/**` are excluded from tenant routing.

## Current focus

Last major work shipped **2026-04-11**:

- **Editorial redesign of landing + auth pages.** Replaced the generic purple-gradient SaaS look with an "Editorial Café Zine" aesthetic — parchment + espresso + terracotta + gold palette, Fraunces display serif, Instrument Sans body, Caveat brand wordmark. Scoped via a `.editorial` class on the page roots so the dashboard/admin (still on the old purple `--color-primary`) is untouched. Removed fake testimonials, fake decorative stats, and the rotating-word hero carousel. Preserved every functional behavior: tenant search with debounced 350ms availability check, featured articles + events loaded from `publicApi`, FAQ accordion, dark mode, 2-step register wizards, slug auto-fill from organization name, debounced slug uniqueness check, tenant-join prefill via `location.state`, TENANT_ADMIN onboarding redirect to `/setup`.
- **Logo + brand assets.** Optimized `logo.png` 4.0 MB → 299 KB transparent PNG via ImageMagick floodfill + trim. Generated `@2x` retina + WebP variants, full favicon set (`favicon.ico`, 16, 32, apple-touch 180, 192, 512), and a 59 KB OG card (1200×630, parchment background, Georgia Italic tagline). Added real SEO meta — `<title>`, description, Open Graph, Twitter Card. The wood-grain `logo.png` is the brand wordmark on the home page (replaced the hand-coded SVG cup + Caveat shorthand); auth pages use full "Coffee Break With Big Sis" in Caveat next to the logo image.
- **TypeScript fix.** Replaced `{...focusRing(...)}` + `{...register(...)}` spread collisions in 3 auth files with a single `fieldProps(name)` helper that spreads `register()` once and overrides `onFocus`/`onBlur` after the spread, manually chaining RHF's `onBlur` to preserve touched-mode validation. Also fixed two TS2783 errors in `login-page.tsx`. Vercel build green again as of `5a58f7a`.

**Still on the editorial backlog** (auth pages still in old purple aesthetic): `join-page.tsx` (member-via-invite), `forgot-password-page.tsx`, `reset-password-page.tsx`, `check-email-page.tsx` (post-tenant-registration landing), `verify-email-page.tsx`, `pending-approval-page.tsx` (post-member-registration landing). The latter two are the final impressions of the onboarding loop — highest-ROI next pass.

**Tech-debt list** (per [ARCHITECTURE.md](docs/ARCHITECTURE.md) Known Issues section): hardcoded JWT secret, `ddl-auto: update` still on alongside Liquibase, Docker port mismatch (`EXPOSE 8070` vs `8070:8080` mapping), Lombok `edge-SNAPSHOT`, zero test coverage, 6 of 7 Redis caches configured but unused, `Alumni` entity duplicates `User` + `Profile` fields without an FK between them.

## Architecture decisions

- **2026-02-20** — **Schema-per-tenant multitenancy** via custom `MultitenantDataSource` + ThreadLocal `TenantContext` + `TenantInterceptor`. Each tenant lives in its own PostgreSQL schema; `SET SCHEMA` runs before every JDBC operation. Strong isolation, but every request needs the `X-Tenant-ID` header (auth/swagger/actuator paths excluded). Trade-off: stronger than tenant-column-with-row-level-security, more operationally complex than separate databases.
- **2026-02-20** — **Standardized `ApiResponse<T>` envelope** + `GlobalExceptionHandler` mapping every exception to a structured `ApiError` with code, message, path, and field errors. The frontend Axios layer can rely on a single shape across all 62 endpoints; pagination uses a separate `PageResponse<T>` shape with content + page + size + totalElements + totalPages.
- **2026-02-20** — **Liquibase as the schema authority**. 18 changesets including seed data (super admin, default tenant, default skills/interests) and 20+ composite performance indexes. Intent is to drop Hibernate's `ddl-auto: update` (still on per known-issues list — schema conflict risk).
- **2026-04-11** — **Editorial design system scoped via `.editorial` class** on landing/auth root divs only, not as a global theme replacement. Tokens live alongside the existing `--color-primary` etc. in `index.css` `@theme`; the rest of the app keeps its purple SaaS theme. Lets the high-touch surfaces ship a distinctive aesthetic without forcing a full-app redesign.
- **2026-04-11** — **Replaced raw HTML-string injection with structured `EmTitle = { pre, em, post? }` objects** + a `<RenderTitle>` helper for emphasized-word headlines, after a security hook flagged the original implementation. Type-safe, lint-clean, and avoids the unsafe React HTML-injection escape hatch for content that's always known at build time.

## Open questions

- **Backend production deploy target** — local-only Docker Compose today; managed PG/Redis intended but provider not chosen (Railway? AWS RDS + ElastiCache? Render?).
- **Test coverage** — zero tests across backend and frontend. Highest-ROI targets per [docs/PLAN.md](docs/PLAN.md): `MatchingService.calculateMatchScore()` (the weighted-Jaccard algorithm is the product differentiator), `AuthenticationService` registration/login/refresh, `SecurityConfiguration` role enforcement, `EventService.registerForEvent()` capacity + deadline.
- **`Alumni` entity overlap** — duplicates `User` + `Profile` fields with no FK between them. Should it be removed in favor of `User` + `Profile` + `Education`, or kept as a public-facing directory linked to `User` via FK? (PLAN.md flags this as a Phase 1 decision.)
- **Email + notification delivery** — `Notification` entity exists with full schema but no SMTP wiring; `Spring Mail` not yet a dependency. Approval emails, match notifications, event reminders all currently silent.
- **File uploads** — `Profile.profileImageUrl`, `Event.imageUrl`, `Content.thumbnailUrl` all reference URLs but no upload pipeline exists. S3 / GCS / local fs decision pending.
- **Payment integration** — `Payment` entity exists with `provider` and `providerTransactionId` columns, but no gateway wiring. Stripe vs Paystack decision; product target is Africa-first so Paystack likely.
- **Editorial coverage** — six remaining auth pages still in the old purple aesthetic (see Current focus). Pull them into the editorial system or leave as low-traffic edge surfaces?
- **CI/CD** — no pipeline configuration in either repo. GitHub Actions intended.
- **Production secrets** — JWT secret hardcoded in `application.yml` (per Known Issues); needs externalization before any deploy beyond local.

## Lessons learned

Project-specific so far; promote to `wiki/concepts/` if any pattern recurs.

- **Scoped design tokens beat global redesigns.** A `.editorial` class on the landing/auth roots gave the brand surfaces a complete typographic + chromatic identity without touching the dashboard's existing tokens. Adding new `@theme` color/font variables alongside the existing semantic tokens is cheaper and lower-risk than overwriting them.
- **`{...focusRing(...)}` then `{...register(...)}` is a silent overwrite.** When two spreads each contain `onBlur`, the later one wins. TypeScript can't statically detect spread-vs-spread key collisions, so the build passes and the bug ships. Fix pattern: store `register(name)` in a local, spread it once, override `onFocus`/`onBlur` *after* the spread, and manually chain the stored `reg.onBlur(e)` inside the override to preserve RHF's touched-mode validation. TS2783 only fires when an explicit prop precedes a spread that includes the same key.
- **The wood-grain logo image is the most honest wordmark.** Hand-coding an SVG mark + script-font shorthand ("Coffee & Big Sis") was inventing brand at runtime; the existing `logo.png` already *contains* "Coffee Break with Big Sis" rendered in wood grain. Swapping the invented assets for `<img src="/logo.png">` deleted ~8 lines of SVG path data, displayed the full name, and used the brand's actual asset.
- **JPG beats PNG for photographic-texture OG cards.** PNG's lossless compression bloated a 1200×630 wood-grain OG card to 1.29 MB; the same render at JPG quality 86 dropped to 59 KB with no visible loss because the eye reads compression artifacts inside wood grain as more wood grain. Match codec to content type.
- **Local `npm run build` catches what `npm run dev` doesn't.** Vite's dev server uses on-demand esbuild transforms and skips full TypeScript project compilation. The TS2783 in `login-page.tsx` was invisible during dev but failed Vercel's `tsc -b && vite build` pipeline. Running `npx tsc -b` (or the full `npm run build`) before pushing is a 3-second habit that prevents CI surprises.
- **Vite `npm run dev` silently shifts ports without telling you the URL is stale.** A zombie Vite process on `5173` sent a fresh `npm run dev` to `5174` with a polite "Port 5173 is in use, trying another one..." message. Any URL referencing 5173 still hits stale code from the old process. Check `lsof -nP -iTCP:5173 -sTCP:LISTEN` before assuming the redirect is harmless.
- **Slug = kebab-case is also a UX detail, not just a routing detail.** The institution registration form auto-slugifies the org name on input; the frontend shows a live "Your door: /ashesi-university" preview and a debounced 400ms uniqueness check that branches into a "Join existing" CTA when the slug already resolves to a tenant. The slug is the door, the URL, and the brand handle in one — getting the input UX right matters as much as the validation regex.

## Related

- **Concepts**: [[wiki/concepts/landing-page-patterns]] — the editorial redesign is a worked example. [[wiki/concepts/visual-directions]] — the Editorial Café Zine commitment fits the named-aesthetic-direction frame.
- **Entities**: [[wiki/entities/editorial]] — closest design-system match for the new aesthetic. [[wiki/entities/warm-editorial]] — even closer; warm parchment + serif display + script accent. [[wiki/entities/vercel]] — frontend deploy target. [[wiki/entities/shadcn]] — frontend uses `@/components/ui/{Input, Button, Textarea}` for dashboard surfaces; the editorial redesign deliberately bypasses these for landing/auth with inline custom inputs to retain pill-shape + terracotta-focus-ring control.
- **Sources**: [[wiki/sources/clear_graphics-yc-unicorn-landing-pages]] — the redesign work is partly a reaction against the patterns this source catalogs (giant hero + social proof + 3-column features); the editorial direction deliberately breaks the YC-unicorn template.
- **Other projects**: [[wiki/projects/stacesprouts]] — closest sibling: multi-repo wrapper with no outer remote, Spring Boot + React 19 + Vite + Tailwind v4 + Zustand + Vercel deploy split for the web layer. Same auto-slug + debounced availability check pattern in tenant/product registration. [[wiki/projects/vedge]] — multi-tenant healthcare OS; precedent for multi-tenant Spring Boot architecture.

## External links

- **Repo (frontend)**: https://github.com/kobbyopoku/cbwbs-frontend
- **Repo (backend)**: https://github.com/kobbyopoku/cbwbs-backend
- **Project README**: `/Users/kobbyopoku/Projects/CoffeeWithBigSis/README.md`
- **Project plan**: `/Users/kobbyopoku/Projects/CoffeeWithBigSis/docs/PLAN.md`
- **Architecture doc**: `/Users/kobbyopoku/Projects/CoffeeWithBigSis/docs/ARCHITECTURE.md`
- **API reference**: `/Users/kobbyopoku/Projects/CoffeeWithBigSis/docs/API.md`
- **Auto-memory**: `~/.claude/projects/-Users-kobbyopoku-Projects-CoffeeWithBigSis/memory/MEMORY.md`
