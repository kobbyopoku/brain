---
type: project
title: StaceSprouts
created: 2026-05-09
updated: 2026-05-09
status: active
repo: multi-repo (github.com/kobbyopoku/stacesprouts-app, stacesprouts-service; pos tracked by outer wrapper with no remote)
local_path: /Users/kobbyopoku/Projects/stacesprouts
stack: [java-21, spring-boot, postgres, redis, flyway, react-19, typescript, vite, tailwind-v4, zustand, tanstack-query, flutter, riverpod, dio]
started: 2026-04-22
aliases: [stacesprouts-pos, stace-sprouts, stacesprout-pos]
tags: [project, ecommerce, retail, pos, ghana, baby-fashion, multi-channel]
---

# StaceSprouts

> Omni-channel commerce platform — eCommerce storefront, admin dashboard, and Flutter POS — for a Ghana-based baby and children's fashion retailer (ages 0–14).

## What and why

StaceSprouts is the operating system for a small Ghanaian baby/kids fashion business: a customer-facing storefront, an admin dashboard for catalog/inventory/finance, and a roaming Flutter POS that takes cash, mobile money, and card-via-Flutterwave at pop-up shops and home deliveries. The platform replaces a paper + spreadsheet workflow with a single source of truth for products, stock, orders, customers, and shifts. Stock enforcement is end-to-end (sold-out badges on the storefront, quantity clamps in the cart, shift-aware register reconciliation in POS) so the business can run multi-channel without overselling. It's a portfolio of three sub-repos in one outer wrapper: `app/` (web), `service/` (backend), `pos/` (mobile). The outer wrapper is a working directory, not a meta-repo — it has no remote and is not the unit of deploy.

## Stack and infrastructure

- **Backend (`service/`)**: Spring Boot 3.3.7, Java 21, Maven. PostgreSQL 16 + Flyway (V1 → V32 as of 2026-05-09), Redis 7, JWT + DB-stored refresh-token rotation (15min access / 7d refresh). SpringDoc OpenAPI. Feature-based packaging (`com.stacesprouts.{feature}.{layer}`). Standardized response wrapper + global exception handling.
- **Storefront + admin (`app/`)**: React 19, TypeScript 5.9, Vite 7.3, TailwindCSS v4 (`@theme`), Zustand 5, TanStack Query 5, React Router 7, react-hook-form + zod, Framer Motion, Radix UI primitives, Lucide icons. ProtectedRoute + RoleGate guards. Axios with auto-refresh interceptors.
- **POS (`pos/`)**: Flutter 3.32+, Dart 3.8+. Riverpod 2 (state), go_router 14 (routing), dio 5 (HTTP), flutter_secure_storage (PIN/JWT), local_auth (biometric unlock), mobile_scanner (barcode), pdf + printing (receipts + barcode labels), gal (save-to-gallery), webview_flutter (Flutterwave hosted MoMo checkout). Mirrors the [[wiki/projects/vedge|Vedge]] `vedge_staff` architecture.
- **Repos**: `github.com/kobbyopoku/stacesprouts-app`, `github.com/kobbyopoku/stacesprouts-service`. The `pos/` directory has no separate remote — it's tracked by the outer wrapper at `/Users/kobbyopoku/Projects/stacesprouts/.git`, which itself has no remote. Outer commits stay local.
- **Deploy**: storefront on Vercel; backend on Railway at `https://stacesprouts.up.railway.app` (default API base for device builds — not localhost); POS sideloaded via `adb install` to a Samsung Android device. No Play Store submission yet.
- **Integrations**: Flutterwave (hosted MoMo + card checkout via WebView; `tx_ref` + `transaction_id` intercepted on redirect; reconciliation goes through `verify`, never webhooks); mnotify (SMS — Card-via-SMS, receipt delivery, future SMS).

## Current focus

Week of 2026-05-09:

- **Branding pass shipped** (2026-05-09) — single source-of-truth logo (`app/public/logo.png`, `pos/assets/logo.png`) wired across favicon (multi-size), Android launcher icon (via `flutter_launcher_icons`), receipt PDF header, barcode-label PDF top-left. App label set to "Stacesprout POS".
- **SKU-as-canonical-identifier** (2026-05-09) — V32 migration drops `barcode` column from `products` + `product_variants` after backfilling SKU from barcode where empty. Scanner endpoint `/api/products/barcode/{value}` retained but switched to `findBySku()` — transparent to all clients.
- **Storefront inventory enforcement** (2026-05-08/09) — `ProductResponse.availableStock` populated via batched `sumQuantityByProductIds()` to avoid N+1; sold-out badges (grayscale + pill) on cards; quantity clamps on PDP and cart; CartItem snapshots `availableStock` at add-time.
- **ScrollToTop** (2026-05-09) — React Router doesn't reset scroll on navigation; new `<ScrollToTop />` uses `useNavigationType()` to scroll on PUSH/REPLACE only and preserve POP scroll for Back/Forward.
- **Recently shipped**: ProductAttributes shows specific age labels and falls back to `primaryColor`/`secondaryColor` when variants are empty; POS save-barcode-to-gallery as white-background PNG (Samsung Gallery dark-mode rendered transparent PDFs as black blobs); MoMo via Flutterwave with synthetic phone-derived email; Overview metrics field-name fix (`{orderCount, totalSales}` vs `{count, total}`).

## Architecture decisions

- **2026-04-22** — **Three-sub-repo wrapper, not a meta-repo.** Outer `stacesprouts/` is a git working directory with no remote; deploys come from `app/` (Vercel) and `service/` (Railway) sub-repos with their own GitHub remotes. The `pos/` directory is tracked by the outer wrapper only. Rationale: independent deploy cadence per surface; outer wrapper is for cross-cutting commits and workflow scripts, not the unit of release.
- **2026-04-22** — **Pivoted POS from React Native + Expo to Flutter same-day** after surveying the [[wiki/projects/vedge|Vedge]] `vedge_staff` codebase. Rationale: a working Riverpod + go_router + dio reference architecture beats a cleaner-on-paper RN stack with no in-portfolio precedent. Mobile work in this portfolio is now Flutter by default.
- **2026-05-08** — **Flutterwave reconciliation goes through `verify`, not webhooks.** Webhooks have been observed to silently fail in this account; never design fulfillment logic that depends on them firing. POS polls `verify` after the WebView redirect captures `tx_ref` + `transaction_id`.
- **2026-05-08** — **Synthetic email for MoMo**. Flutterwave hosted checkout requires `customer.email` even for MoMo; synthesized as `<phone-digits>@pos.stacesprouts.local` in PosService MoMo branch. Solves the 400 "Customer email is required" without prompting cashiers.
- **2026-05-09** — **Drop `barcode` column; SKU is the canonical scannable identifier.** V32 migration backfills SKU from barcode where empty for legacy products, then drops the column from `products` + `product_variants`. The scanner URL path stays the same; lookup switched to `findBySku()`. Rationale: two identifier columns drift; one source of truth eliminates a class of mismatch bugs.
- **2026-05-09** — **Add JPA record overload factories rather than break call sites.** When adding a field to a record DTO (e.g., `availableStock` to `ProductResponse`), add `from(Product)` + `from(Product, long)` overloads instead of forcing positional-argument changes everywhere. Cheaper than a migration of every call site.
- **2026-05-09** — **Inventory queries batch via `sumQuantityByProductIds(Collection<UUID>)`.** Storefront product list pages compute available stock with one round-trip per page through `ProductService.summarisePage()`, not N+1 per card.

## Open questions

- **Outer wrapper remote** — should `stacesprouts/` itself have a GitHub remote (private) for cross-cutting commits, or stay local-only?
- **Analytics provider** — recommended PostHog over a build-your-own dashboard (page visits / heat map / country); planning doc only, no code shipped. Decision pending.
- **POS distribution** — currently `adb install` to a single Samsung device. Play Store internal testing track? Or stay sideloaded for the foreseeable?
- **Cross-channel inventory** — the storefront and POS share the same `inventory_items` table. What's the locking story when a cashier and an online customer race for the last unit?
- **Receipt SMS / email delivery** — mnotify is wired for SMS but receipt-via-SMS is not yet integrated end-to-end.
- **Customer record dedup** — POS captures phone + name; no deduplication against existing online customers.

## Lessons learned

Project-specific; promote to `wiki/concepts/` when patterns generalize.

- **PDF rasterization preserves transparency.** `Printing.raster()` → `toPng()` keeps the page background transparent unless explicitly filled. Samsung Gallery's dark-mode preview renders that as a black blob. Fix: `pw.Container(color: PdfColors.white)` + `marginAll: 0` on `PdfPageFormat`.
- **`flutter_launcher_icons` adaptive-icon background must be solid for line-art logos.** A transparent `adaptive_icon_foreground` over a wallpaper-aware adaptive mask shows the wallpaper through. Set `adaptive_icon_background: "#FFFFFF"`.
- **Edit + multi-line `replace_all` only matches the first occurrence when later occurrences differ in formatting.** Have to do separate Edit calls per call site for record-factory overloads.
- **Spring Boot record DTOs are positional** — adding a field anywhere mid-record breaks every caller; the `from(Entity)` factory pattern with overloads insulates against this.
- **`gal` save-to-gallery on Android** uses MediaStore on API 29+ (no runtime permission) and falls back to `WRITE_EXTERNAL_STORAGE` with `maxSdkVersion="28"` for older devices — keeps the manifest tidy and avoids the scary "all files" prompt on modern installs.
- **Flutterwave WebView intercepts** — read both `tx_ref` and `transaction_id` from the redirect URL; some MoMo redirects only include `tx_ref`. Always re-verify server-side; never trust the WebView alone.

## Related

- **Concepts**: *(none directly — this is a product project, not a pattern study. Inventory N+1 batching and the SKU-as-canonical-identifier consolidation could promote to concepts later if they recur.)*
- **Entities**: [[wiki/entities/posthog]] — recommended analytics provider for the storefront (page visits / heat map / country); decision pending. [[wiki/entities/vercel]] — storefront deploy target.
- **Sources**: *(none yet — no curated source has been ingested for this project's patterns.)*
- **Other projects**: [[wiki/projects/vedge]] — sibling project; `vedge_staff` is the Flutter architecture reference for `pos/` (Riverpod + go_router + dio + flutter_secure_storage), and the same Flutterwave verify-not-webhook reconciliation lesson applies.

## External links

- **Repo (storefront + admin)**: https://github.com/kobbyopoku/stacesprouts-app
- **Repo (backend service)**: https://github.com/kobbyopoku/stacesprouts-service
- **Backend deploy**: https://stacesprouts.up.railway.app
- **Project's own `CLAUDE.md`**: `/Users/kobbyopoku/Projects/stacesprouts/CLAUDE.md` (behavioral guidelines — Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution)
- **Implementation plan**: `/Users/kobbyopoku/Projects/stacesprouts/PLAN.md`
- **Auto-memory**: `~/.claude/projects/-Users-kobbyopoku-Projects-stacesprouts/memory/MEMORY.md`
