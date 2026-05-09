---
type: entity
title: ROAM Labs
entity_type: organization
created: 2026-05-09
updated: 2026-05-09
website: ""
aliases: [ROAM, _roamlabs]
tags: [organization, ai-products, services-agency, founded-by-wiki-owner, ghana, primary-org]
---

# ROAM Labs

> **AI products + services company** founded by [[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]]. Houses three commercial AI products ([[wiki/projects/vedge|Vedge]], [[wiki/projects/kivora|Kivora]] / *ROAM GRC*, [[wiki/projects/clarvyn|Clarvyn]]), takes on AI-services client work ([[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]], [[wiki/projects/stacesprouts|StaceSprouts]]), and acts as subcontractor on the CPC RTBVD government engagement under [[wiki/entities/softtech-solutions|SoftTech Solutions]]. The corporate marketing site is at [[wiki/projects/roamlabs|_roamlabs]].

## Profile

ROAM Labs sits in the *AI services + AI products* hybrid model that the wiki tracks heavily — see [[wiki/concepts/services-as-software]] (Vacca's $7M ARR pattern) and [[wiki/concepts/ai-automation-services]] (Khairallah's $10K/mo playbook). The portfolio split is deliberate: **products carry recurring-revenue + IP**, **client work funds the runway**, **government contracts deliver high-value single engagements**. The architectural signature across all three product builds is *Spring Boot backend + FastAPI Claude agent + pgvector RAG + React/Vite (or Next.js) web + React Native mobile* — high reuse, low cognitive switching cost.

The "ROAM" umbrella covers product sub-brands:

- **ROAM GRC** = product name for [[wiki/projects/kivora|Kivora]] (the platform's commercial brand).
- **_roamlabs** = the agency / corporate brand.
- *Vedge* and *Clarvyn* keep their own product names rather than ROAM-prefixed branding.

## Key facts

- **Founder**: [[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]] (also "Kobby" / "Kobby Opoku").
- **Headquarters / locale**: Ghana.
- **Marketing surface**: [[wiki/projects/roamlabs|_roamlabs]] corporate site (Next.js 14 + custom NeuralNetwork canvas hero).
- **Architectural signature**: Spring Boot 3 + FastAPI + Claude (Sonnet 4 / Haiku 4) + pgvector RAG + React 19 / Next.js + React Native + Expo + PostgreSQL + Redis.
- **MCP integration**: production in Clarvyn (Wave 6E); native to Kivora; planned for Vedge.

## Portfolio

### Owned products (commercial / IP-bearing)

| Project | Product brand | Domain | Status |
|---|---|---|---|
| [[wiki/projects/vedge]] | Vedge | African healthcare OS | Active |
| [[wiki/projects/kivora]] | **ROAM GRC** | Multi-tenant SaaS GRC | Active — Tier 1 Finding-schema migration shipped 2026-05-08 |
| [[wiki/projects/clarvyn]] | Clarvyn | AI-first HR for startup founders | Active — Wave 6 shipped (proactive conversations, MCP layer, Slack/Jira/GCal integrations) |

### Internal tools (built for ROAM Labs's own use)

| Project | Domain | Status |
|---|---|---|
| [[wiki/projects/helm]] | Multi-agent ops platform automating GTM + business operations across all ROAM products + client work | Just-started 2026-05-09 — design phase complete, week 1 build (Lead Management agent MVP) about to begin. Hermes Agent + FastAPI on Railway + Next.js on Vercel + PostgreSQL + pgvector. |

### Services / client work

| Project | Client | Domain | Status |
|---|---|---|---|
| [[wiki/projects/coffee-break-with-big-sis]] | Big Sis (institution networking + mentorship) | Multi-tenant SaaS | Active |
| [[wiki/projects/stacesprouts]] | StaceSprouts (Ghana baby/kids fashion retailer) | Omni-channel commerce | Active — V32 migration shipped 2026-05-08/09 |

### Government subcontract

| Project | Prime contractor | End client | Status |
|---|---|---|---|
| [[wiki/projects/cpc-rtbvd]] | [[wiki/entities/softtech-solutions]] | Cocoa Processing Company Plc (CPC) | Bid submitted 2026-05-09; awaiting award decision |

## Mentioned in

- [[wiki/projects/roamlabs]] — corporate marketing site.
- [[wiki/projects/vedge]], [[wiki/projects/kivora]], [[wiki/projects/clarvyn]] — owned products.
- [[wiki/projects/coffee-break-with-big-sis]], [[wiki/projects/stacesprouts]] — client work.
- [[wiki/projects/cpc-rtbvd]] — subcontract under SoftTech.

## Related entities

- [[wiki/entities/godwin-opoku-duah]] — founder / wiki owner.
- [[wiki/entities/softtech-solutions]] — prime contractor on CPC RTBVD.
- [[wiki/entities/anthropic]] — Claude provider (model layer of every ROAM AI product).

## Related concepts

- [[ai-automation-services]] — the services-side of the business model.
- [[services-as-software]] — the products-side (Vacca's framework).
- [[markdown-as-agent-contract]] — applied across all ROAM products (CLAUDE.md per repo).
- [[mcp-server]] — production-deployed in multiple ROAM products.
- [[reasoning-execution-split]] — architectural pattern across all three AI products.
- [[doe-framework]] — agent-workflow architectural framing.
