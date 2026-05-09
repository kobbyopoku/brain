---
type: synthesis
title: Godwin Opoku Duah — Portfolio Landscape
created: 2026-05-09
updated: 2026-05-09
aliases: [roam-portfolio, kobby-portfolio, godwin-projects]
tags: [synthesis, portfolio, roam-labs, brolly-africa, project-landscape, wiki-owner]
---

# Godwin Opoku Duah — Portfolio Landscape

> **One-page map** of every project [[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]] owns or delivers, organized by *who owns the IP* and *who holds the client relationship*. Filed 2026-05-09 after the user explicitly briefed the brain on his organizational landscape. Updates when Brolly Africa is entified separately.

## The four buckets

```
┌─────────────────────────────────────────────────────────────────┐
│                    GODWIN OPOKU DUAH                            │
│                    (founder + co-founder + PM/CTO)              │
└────────────────────────────┬────────────────────────────────────┘
                             │
       ┌─────────────────────┼─────────────────────────────┐
       │                     │                             │
       ▼                     ▼                             ▼
┌──────────────┐    ┌────────────────┐         ┌────────────────────┐
│  ROAM LABS   │    │ BROLLY AFRICA  │         │ SOFTTECH SOLUTIONS │
│  (founder)   │    │ (co-founder)   │         │ (subcontractor on  │
│              │    │                │         │  CPC RTBVD only)   │
└──────┬───────┘    └────────┬───────┘         └─────────┬──────────┘
       │                     │                           │
       │                     │                           │
   ┌───┴────┐                │                           │
   ▼        ▼                ▼                           ▼
┌──────┐ ┌──────────┐  ┌─────────────┐         ┌──────────────────┐
│ Own  │ │  Client  │  │  Client     │         │  Government      │
│ IP   │ │  work    │  │  work       │         │  subcontract     │
└──┬───┘ └────┬─────┘  └──────┬──────┘         └────────┬─────────┘
   │          │               │                         │
   ▼          ▼               ▼                         ▼
 Vedge      CBwBS         Asanti                    CPC RTBVD
 Kivora     Stace-                                  (end client:
 Clarvyn    Sprouts                                  CPC)
 _roamlabs
 (self)
```

## Bucket 1 — ROAM Labs owned products (commercial / IP-bearing)

These carry [[wiki/entities/roam-labs|ROAM Labs]] IP and recurring-revenue logic. Godwin owns them outright as the founder.

| Project | Brand | Domain | Stack signature | Status |
|---|---|---|---|---|
| [[wiki/projects/vedge]] | Vedge | African healthcare OS | Spring Boot 3.4 + Next.js 16 + Flutter ×2 + React Email | Active build; modular monolith with 11+ modules |
| [[wiki/projects/kivora]] | **ROAM GRC** | Multi-tenant SaaS GRC | Spring Boot 3 + Vite/React 19 + FastAPI Claude + pgvector RAG | Active; Tier 1 Finding-schema migration shipped 2026-05-08 |
| [[wiki/projects/clarvyn]] | Clarvyn | AI-first HR for startup founders | Spring Boot 3.3.5 + FastAPI Claude (Sonnet 4 + Haiku 4) + pgvector + Vite/React 19 + RN/Expo 54 | Active; Wave 6 shipped — proactive conversations + MCP layer |
| [[wiki/projects/roamlabs]] | _roamlabs | Agency corporate marketing | Next.js 14 + custom NeuralNetwork canvas hero | Active; visual direction in flux |

**Pattern**: Spring Boot backend + FastAPI Claude agent + pgvector RAG + React/Vite (or Next.js) web + React Native mobile. Same architecture across Kivora and Clarvyn; Vedge keeps Spring Boot + Next.js + Flutter (no FastAPI agent service yet but planned). High reuse.

## Bucket 2 — ROAM Labs client work (services delivered, client owns IP)

These are services contracts. ROAM Labs builds and delivers; the client owns the resulting code and product.

| Project | Client | Domain | Status |
|---|---|---|---|
| [[wiki/projects/coffee-break-with-big-sis]] | Big Sis (institutional networking + mentorship) | Multi-tenant SaaS — schema-per-tenant Spring Boot + Vite/React 19 + Tailwind v4 | Active; last major work was Editorial Café Zine redesign 2026-04-11 |
| [[wiki/projects/stacesprouts]] | StaceSprouts (Ghana baby/kids fashion retailer) | Omni-channel commerce: storefront + admin + Flutter POS | Active; V32 SKU-as-canonical-identifier migration shipped 2026-05-08/09 |

## Bucket 3 — Brolly Africa client work

Brolly Africa is Godwin's **co-founded** venture (he is co-founder, not sole founder). The wiki has not yet entified Brolly — Godwin will add it separately. Current Brolly project on file:

| Project | Client | Domain | Status |
|---|---|---|---|
| [[wiki/projects/asanti-brokers]] | Asanti Brokers Limited (Ghana NIC-licensed insurance brokerage) | Marketing site — Next.js 16 + React 19 + Tailwind v4 + TypeScript 5 | Active; deployed at `asanti.insure`; ~2 months quiet may warrant `paused` |

The `/Users/kobbyopoku/Brolly/asanti-brokers` filesystem path reflects the Brolly umbrella.

## Bucket 4 — Government subcontract

| Project | Prime contractor | End client | Status |
|---|---|---|---|
| [[wiki/projects/cpc-rtbvd]] | [[wiki/entities/softtech-solutions]] | Cocoa Processing Company Plc (CPC) | Bid submitted 2026-05-09; GHS 2,980,000 firm all-inclusive lump sum; 12-week build proposed; awaiting award decision |

[[wiki/entities/softtech-solutions|SoftTech Solutions]] holds the prime contract with CPC; ROAM Labs is the subcontracted technical-delivery partner. Godwin is named **PM/CTO Key Expert** in the QCBS bid response (CPC/PRO/CS/1/26).

## Cross-cutting observations

### Architectural reuse across owned products

Kivora + Clarvyn share a near-identical stack: Spring Boot 3 + FastAPI Claude + pgvector RAG. This isn't accidental — it's **deliberate compounding** so each new product launch costs less than the last. Vedge predates the FastAPI agent service pattern but is positioned to absorb it (the [[wiki/projects/vedge|vedge_agent]] repo exists as scaffolding).

### MCP-everywhere as a near-term convergence

- [[wiki/projects/clarvyn]] Wave 6E added MCP server + client.
- [[wiki/projects/kivora]] has it from inception.
- [[wiki/projects/vedge]] is planned.

The wiki's [[mcp-server]] concept page accumulates against this practice — every new MCP-related source ingested compounds against actual production deployment in three different ROAM products.

### Multi-repo wrapper convention

[[wiki/projects/stacesprouts]], [[wiki/projects/coffee-break-with-big-sis]], and [[wiki/projects/clarvyn]] all use the same pattern: outer wrapper directory (no `.git`) + N service-level repos with their own remotes. The Clarvyn 2026-05-09 update established the convention: **drop `BRAIN.md` in every sub-repo for multi-repo projects**, because an agent might open just one service.

### Scale of wiki compounding

The brain has accumulated 90+ sources, 297+ entities, 48 concepts, 2 syntheses, 8 active projects, and 221+ stubs as of 2026-05-09. The portfolio above is the *real-world target* this knowledge-compounding effort exists to serve — most ingested patterns ([[ai-automation-services]], [[reasoning-execution-split]], [[hot-cache]], [[markdown-as-agent-contract]], [[doe-framework]], [[mcp-server]], [[anti-ai-slop-machinery]]) translate directly into operational decisions in one or more of the 8 active projects.

## Open questions for future filing

- **Brolly Africa entity** — pending creation by Godwin.
- **Godwin's primary product priority** — when split-attention pressure rises across Vedge / Kivora / Clarvyn / client work / CPC, which project gets the next hour? *(Not currently documented; might warrant a "current focus" file.)*
- **Whether to file CMC** (the parallel proposal flagged in the CPC RTBVD page) — currently surfaced as a question, not an answer.
- **Client-work pricing rubric** — the wiki has [[ai-automation-services]] (Khairallah's $3-15K/build) and [[services-as-software]] (Vacca's scaled version) as external references; not yet documented how ROAM Labs' actual pricing compares.

## Mentioned entities

- [[wiki/entities/godwin-opoku-duah]] — wiki owner.
- [[wiki/entities/roam-labs]] — primary org.
- [[wiki/entities/softtech-solutions]] — prime contractor on CPC RTBVD.
- *(Brolly Africa — entity to be added by Godwin)*

## Mentioned projects

- [[wiki/projects/vedge]], [[wiki/projects/kivora]], [[wiki/projects/clarvyn]], [[wiki/projects/roamlabs]] — ROAM owned.
- [[wiki/projects/coffee-break-with-big-sis]], [[wiki/projects/stacesprouts]] — ROAM client work.
- [[wiki/projects/asanti-brokers]] — Brolly client work.
- [[wiki/projects/cpc-rtbvd]] — SoftTech subcontract.

## Related concepts

- [[ai-automation-services]] — services-side business model.
- [[services-as-software]] — products-side business model.
- [[markdown-as-agent-contract]] — applied across all ROAM products.
- [[mcp-server]] — production-deployed in multiple products.
- [[reasoning-execution-split]] — architectural pattern.
- [[doe-framework]] — agent-workflow framing.
