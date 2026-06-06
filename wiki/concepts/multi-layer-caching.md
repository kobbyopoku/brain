---
type: concept
title: Multi-Layer Caching
created: 2026-06-06
updated: 2026-06-06
aliases: [Multi-Layer Caching, multi-tier cache, three-tier cache]
tags: [backend, caching, scalability, system-design]
---

# Multi-Layer Caching

> A caching strategy that stacks several cache tiers so that only a full miss reaches the database.

## Definition

Multi-Layer Caching arranges caches in tiers: **L1** edge CDN cache, **L2** application Redis cache (computed results, sessions, hot records), and **L3** query-result cache; only a full miss across all tiers hits the database. As framed in [[wiki/sources/akintola-steve-backend-1-million-users]], the target is a hit ratio above 85%, and it is called the biggest cost lever at scale.

## Why it matters

Each tier absorbs load the next tier would otherwise carry, and the database — the most expensive and hardest-to-scale resource — is reached only on a complete miss. The source positions it as the single biggest cost lever at scale.

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as a three-tier cache (L1 edge CDN, L2 application Redis for computed results/sessions/hot records, L3 query-result cache) where only a full miss hits the DB; targets a >85% hit ratio; called the biggest cost lever at scale, with event-driven (Kafka) invalidation preferred over TTL alone.

## Sub-claims and details

- **L1** — edge CDN cache. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- **L2** — application Redis cache for computed results, sessions, and hot records. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- **L3** — query-result cache; only a full miss reaches the database. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Target hit ratio above 85%. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Described as the biggest cost lever at scale. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Event-driven (Kafka) cache invalidation preferred over TTL alone. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- Sourced from a single page; no independent corroboration in the wiki yet.

## Related concepts

- [[backend-scalability-blueprint]] — the caching section of the blueprint.
- [[database-sharding]] — the database tier the cache layers protect from load.

## Related entities

- [[wiki/entities/akintola-steve]] — author of the source.

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
