---
type: project
title: Asanti Brokers
created: 2026-05-09
updated: 2026-05-09
status: active
repo: git@github.com:kobbyopoku/asanti-brokers.git
local_path: /Users/kobbyopoku/Brolly/asanti-brokers
stack: [nextjs, react, tailwind, typescript, vercel]
started: 2026-03-11
ended:
aliases: [asanti, asanti-brokers-limited]
tags: [project, marketing-site, insurance, ghana, nextjs]
---

# Asanti Brokers

> Marketing website for *Asanti Brokers Limited* — a Ghana-licensed (NIC-registered) insurance brokerage — pitching motor, property, business, travel, fire, marine, personal-accident, and group-employee-benefits cover with an "insurance made simple" digital-first stance.

## What and why

Asanti Brokers is the public marketing site for *Asanti Brokers Limited*, a Ghana-licensed insurance broker registered with the National Insurance Commission (NIC). The site sells the brokerage's "insurance made simple" pitch — fast, digital, hassle-free placement of motor, property, business-liability, fire & special-perils, marine cargo, travel, personal-accident, and group-employee-benefits cover — and acts as the lead-capture funnel for the brokerage. It is a static-shaped Next.js 16 App Router site with one route per product line for SEO surface area, a WhatsApp CTA for direct lead capture, and Vercel Analytics for traffic measurement. The site sits in the `Brolly/` parent directory alongside other insurance work, suggesting Asanti is one face of a broader insurance brand cluster (relationship to be confirmed; see Open questions).

## Stack and infrastructure

- **Languages / frameworks**: TypeScript 5, Next.js **16.1.6** (App Router), React **19.2.3**, Tailwind CSS **v4** (PostCSS pipeline), ESLint 9
- **Key dependencies / services**: `@vercel/analytics` 2.x, `next/font` (Inter — variable still named `--font-geist-sans` from the create-next-app template)
- **Repo / locations**: GitHub `kobbyopoku/asanti-brokers`; local `/Users/kobbyopoku/Brolly/asanti-brokers`
- **Deployed at**: [asanti.insure](https://www.asanti.insure) (Vercel)
- **Routes**: `/` (home), `/about`, `/blog`, `/claims`, `/contact`, `/how-it-works`, `/services` + 8 service sub-pages — `motor-insurance`, `property-insurance`, `business-liability-insurance`, `fire-special-perils`, `marine-cargo-insurance`, `travel-insurance`, `personal-accident-insurance`, `group-employee-benefits`
- **Shared components**: Navbar, Footer, WhatsAppButton, CookieConsent, AnimatedCounter, Testimonials, PageHeader, InsurerLogos grid, PolicyIllustrations
- **Tooling artifacts in tree**: `.playwright-mcp/` (visual review captures), `firebase-debug.log` (Firebase tooling explored at some point — purpose unconfirmed)

## Current focus

_To be filled in._ No signal in the repo — README is the create-next-app default. Last commit 2026-03-12; no active changes between then and the brain page creation on 2026-05-09. Working assumption: **live and stable**, no in-flight redesign or feature work.

## Architecture decisions

Observed from the codebase and manifests on 2026-05-09. Rationale to be filled in by the human where the *"why"* is not yet captured.

- **2026-03-11** — Built on Next.js **16 App Router** with **one route per service product** (`/services/<product>`) rather than a single dynamic `/services/[slug]` route. *Why (likely): SEO surface area — each product line gets its own indexable page, metadata, and copy.*
- **2026-03-11** — **Tailwind v4** with custom `asanti-green` brand-color tokens; **Inter** font via `next/font/google` (variable misnamed `--font-geist-sans` from the create-next-app template — cosmetic, not load-bearing).
- **2026-03-11** — **Vercel Analytics** + **Vercel hosting**; `asanti.insure` as the production domain. No CMS, no API routes, no DB — fully static-shaped marketing site.
- **2026-03-11** — Compliance/UX baseline: **WhatsApp CTA** for direct lead capture (Ghana-market default channel), **cookie consent** banner, and an **NIC registration badge** in the hero as a trust signal.

## Open questions

- **Brolly relationship.** The repo lives under `~/Brolly/`. Is *Brolly* the umbrella brand, a sister project, a working folder name, or something else? Should the brain track Brolly as a separate page, or is Asanti the only public-facing surface?
- **Active vs paused.** No commits between 2026-03-12 and the brain page creation on 2026-05-09 (~2 months). Currently filed as `active` on the assumption that "deployed and operating" counts as active. Move to `paused` if no roadmap.
- **Lead-capture pathway.** WhatsApp button is the visible CTA. Is there a forms backend (Firebase? something else? — the `firebase-debug.log` artifact hints at exploration), and does it need to be captured here?
- **Blog program.** `/blog` route exists. Is content actually being shipped, or is it a placeholder?
- **Group employee benefits route.** Present in routes but absent from the homepage `policies` array — intentional, or oversight?

## Lessons learned

_To be filled in by the human._ Do not fabricate.

## Related

- **Concepts**: [[wiki/concepts/landing-page-patterns]] (this is a marketing site; the YC-unicorn patterns apply), [[wiki/concepts/switching-forces]] (push/pull/habit/anxiety as a useful lens for an insurance brokerage funnel)
- **Entities**: [[wiki/entities/vercel]] (host + analytics)
- **Other projects**: [[wiki/projects/roamlabs]] (closest in *shape* — also a Next.js marketing site)

## External links

- **Repo**: https://github.com/kobbyopoku/asanti-brokers
- **Production site**: https://www.asanti.insure
- **Project's own CLAUDE.md** (if exists): _none_
- **Project memory dir** (if exists): _none_ — only `.claude/settings.local.json`
