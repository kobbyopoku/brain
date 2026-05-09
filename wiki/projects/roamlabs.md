---
type: project
title: _roamlabs
created: 2026-05-09
updated: 2026-05-09
status: active
repo: https://github.com/kobbyopoku/roamlabs
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/roam
stack: [next.js, react-18, tailwind, framer-motion, lucide-react, javascript]
started: 2026-01-14
owner_org: roam-labs
affiliation: roam-labs-self
aliases: [roam-labs, roamlabs-website]
tags: [project, marketing-site, agency-site, ai-agency, next-js]
---

> **Lineage**: corporate marketing site for [[wiki/entities/roam-labs|ROAM Labs]] itself ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder). The agency's own surface — distinct from owned products (Vedge / Kivora / Clarvyn) and from client work.

# _roamlabs

> The corporate marketing website for **_roamlabs**, an enterprise AI agency selling autonomous AI agents, workflow automation, custom AI development, and AI consulting — built as a single Next.js 14 App Router site with a Tailwind design system.

## What and why

_roamlabs is the public-facing surface for an AI services company that designs and deploys autonomous agents and intelligent automation for enterprises. The site is a six-page marketing surface (Home, Solutions, How It Works, Use Cases, About, Contact) intended to drive demo bookings and consultation requests; it is not a product, just the front door. The core proposition mirrors the broader [[wiki/concepts/ai-automation-services]] / [[wiki/concepts/services-as-software]] models — sell AI builds at the high end, leverage AI tooling for delivery margin. Success looks like: distinctive visual identity, fast load, conversion-focused copy, and a clear pipeline to `/contact`. Sister to the other ROAM-umbrella projects ([[wiki/projects/vedge]], [[wiki/projects/kivora|Kivora / ROAM GRC]]).

## Stack and infrastructure

- **Framework**: Next.js 14.0.4 (App Router), React 18, JavaScript (no TypeScript).
- **Styling**: Tailwind 3.4 with a custom `primary` (indigo) + `dark` (slate) palette; design tokens centralized in `app/globals.css` via `@layer components`.
- **Animation**: Framer Motion 10 (every page is `'use client'` + `whileInView` reveals).
- **Icons**: lucide-react (imported as a barrel — known bundle-size cost; flagged but not yet remediated).
- **Hero animation**: a custom `<NeuralNetwork />` HTML5 canvas (~780 lines) with particles, signal pulses, activation bursts, data packets, and 4 *"robot agents"* that wander/work/communicate.
- **Repo**: `github.com/kobbyopoku/roamlabs` · single repo, single deployable.
- **Deployed at**: not yet captured. Likely candidate is Vercel given the stack, but unconfirmed.

## Current focus

Visual design direction is being actively explored. As of the last working session (2026-05-09) two alternate aesthetics were prototyped end-to-end and then reverted:

1. **Editorial-quarterly** — cream paper canvas, Instrument Serif + Newsreader display, oxblood accent, §-style section markers, footnotes/marginalia/drop-caps. Reverted: *"the editorial thingy doesn't work with this concept"* — too literary for an AI-agents company.
2. **Mission control / engineering atelier** — warm-black surface, Bricolage Grotesque + JetBrains Mono, electric lime accent, telemetry-style readouts, panel corner ticks, scanlines. Also reverted.

The current `main` is the original aesthetic: indigo-on-dark hero with the NeuralNetwork canvas, JetBrains-Mono-headlines / Inter-body type pairing, and the typewriter-cycling tagline. Visual direction is unsettled; perf/architectural fixes (server components + client islands, dynamic-imported canvas, DPR-safe scaling, passive scroll listeners, prefers-reduced-motion, lucide barrel imports) were also prototyped and reverted alongside the redesigns.

## Architecture decisions

*(Drawn only from what is visible in code and commits — no fabrication. Most are implicit; promote to a real decision log when one is started.)*

- **2026-01-14** — Next.js 14 App Router over Pages Router; visible from `app/` layout with `page.js` files.
- **2026-01-14** — JavaScript, not TypeScript; deliberate for a small marketing site.
- **2026-01-14** — All page routes are `'use client'` whole-page; framer-motion reveals applied per-element rather than via server components + client islands.
- **2026-01-14** — Custom canvas hero (`NeuralNetwork.js`) over a Lottie / WebGL / video.
- **2026-01-14** — Two Google Fonts loaded together (Inter + JetBrains Mono); no `modularizeImports` for lucide-react.

## Open questions

- **Production URL / hosting** — not yet captured. Confirm whether deployed and where.
- **Visual direction** — third aesthetic exploration pending; the editorial and mission-control directions were both rejected. Worth recording the next attempt's brief before building, to avoid another full revert.
- **Architectural cleanup** — should the perf fixes (server-component pages, dynamic Schematic, passive scroll, reduced-motion, lucide modularize) be reapplied independently of a visual redesign? They survive any aesthetic.
- **Inner pages** — about / solutions / contact / how-it-works / use-cases all still live as whole-page client components. Same redesign-vs-perf question applies.
- **Team / authorship** — the about page lists Godwin / Richmond / Frank / Justice / Gabriel / Amma. Confirm whether this is the user's own company site or a contractor build, and whether team copy is final.

## Lessons learned

*(none filed yet — populate after the next visual-direction decision lands. If a lesson generalizes — e.g. "editorial aesthetics fight high-velocity AI brands" — promote to `wiki/concepts/`.)*

## Related

- **Concepts**: [[wiki/concepts/ai-automation-services]], [[wiki/concepts/services-as-software]], [[wiki/concepts/landing-page-patterns]]
- **Other projects**: [[wiki/projects/vedge]], [[wiki/projects/kivora]] *(sibling ROAM-umbrella projects)*
- **Entities**: [[wiki/entities/coldiq]] *(analogous services-as-software agency at $7M ARR)*

## External links

- **Repo**: https://github.com/kobbyopoku/roamlabs
- **Local path**: `/Users/kobbyopoku/ROAM/CascadeProjects/roam`
- **Project's own CLAUDE.md**: not present
- **Project memory dir**: not present
