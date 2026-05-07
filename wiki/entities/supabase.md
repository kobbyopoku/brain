---
type: entity
title: Supabase
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://supabase.com
aliases: []
tags: [backend, postgres, firebase-alternative, open-source, apache-2, mcp-integration, design-md-available, open-design-catalog]
---

# Supabase

> Open-source Postgres-native backend platform — Postgres + Auth + Realtime + Storage + Edge Functions + Vector + Cron + Queues + AI / ML embedding generation. Apache-2.0 licensed and self-hostable. Founded 2020 by Paul Copplestone + Ant Wilson + Inian Parameshwaran. Cataloged in [[wiki/entities/open-design|Open Design]] under Backend & Data with a *"dark emerald theme, code-first"* DESIGN.md. Ships an MCP server (`supabase:supabase`) that AI coding agents can use to read schemas, query data, and manage projects.

## Profile

Supabase is the most architecturally relevant open-source backend platform for [[wiki/projects/vedge|Vedge]]-class healthcare projects. It ships every layer Vedge needs (Postgres + auth + realtime + storage + edge functions + cron + vector) as a coherent integrated stack, all backed by Postgres semantics agents can reason about. The Apache-2.0 license + self-hostability address the PHI / data-residency concerns SaaS-only alternatives (Firebase, Supabase Cloud) leave open.

## Key facts

- **Founded**: 2020. Headquartered remote-first.
- **Founders**: Paul Copplestone (CEO), Ant Wilson (CTO), Inian Parameshwaran.
- **Website**: https://supabase.com
- **License**: Apache-2.0. Self-hostable.
- **Category** (per Open Design): Backend & Data.
- **Open Design DESIGN.md**: `raw/open-design/design-systems/supabase/DESIGN.md`
- **MCP server**: yes — `supabase:supabase` family of skills (covers Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues, Postgres best practices).

## Product surface

### Core Postgres-native stack

- **Database**: managed PostgreSQL with full SQL access. Critical: agents can write standard SQL, no proprietary query language. PostgREST exposes auto-generated REST + GraphQL APIs from the schema.
- **Auth**: GoTrue — JWT-based, supports email/password, magic links, OAuth (Google, GitHub, Apple, etc.), SAML/SSO, MFA, anonymous auth. Critical for healthcare: row-level-security policies enforce per-user / per-tenant data access at the database level.
- **Realtime**: WebSocket subscriptions to DB changes (INSERT/UPDATE/DELETE events on tables) + presence + broadcast channels.
- **Storage**: S3-compatible object storage with Postgres-backed metadata; integrates with row-level security so file access policies are SQL.
- **Edge Functions**: Deno runtime, deployed globally on edge POPs. Material for sending notifications, integrating third-party services, running per-request logic.
- **Vectors**: pgvector extension; embedding storage + similarity search inside Postgres. Material for AI-augmented patient-record search.
- **Cron**: SQL-defined scheduled jobs via pg_cron extension. Sibling of [[wiki/concepts/scheduled-automation|scheduled-automation]] at the database layer.
- **Queues**: pgmq-based job queues. Material for async workflows (e.g. NHIS claims submission retry queues in Vedge).

### Supabase MCP server + skills

The user's Claude Code has multiple Supabase skills targeting the MCP:

- `supabase:supabase` — main skill for any Supabase task (Database / Auth / Edge Functions / Realtime / Storage / Vectors / Cron / Queues).
- `supabase:supabase-postgres-best-practices` — Postgres performance optimization + best practices.

The MCP enables agents to read schemas, generate migrations, compose queries, deploy edge functions, configure auth providers — all without leaving the agent context.

### Self-hostable Supabase Stack

The full platform runs as a Docker Compose / Kubernetes deployment. Key implication for Vedge: **PHI never leaves your infrastructure**. The wiki's earlier [[wiki/syntheses/refero-open-design-claude-design-comparison|Vedge recommendation for Open Design]] hinges partly on local-first / BYOK posture; Supabase as backend matches that posture.

## Positions and claims

- **Postgres beats proprietary backends.** Supabase's bet vs Firebase: standard SQL + open-weight schema + portable migrations beats a proprietary key-value document store, even for the use cases (realtime, auth, storage) Firebase optimized for.
- **Open-source + cloud-hosted is the right go-to-market.** Self-host if you must (compliance, sovereignty); use the cloud if you want speed. Same codebase.
- **Row-level security is the right authorization primitive.** Push auth into the database, not into app code. Reduces leak surface.

## Vedge fit (specific)

- **PHI compliance**: self-host Supabase on Vedge's infrastructure → PHI never touches a SaaS vendor.
- **Multi-tenant healthcare**: row-level security via tenant_id + role policies enforces hospital / clinic / pharmacy data separation at the database layer.
- **Realtime**: clinician dashboards, patient queue updates, NHIS claim status changes — all natively pushed to UIs via Realtime.
- **Edge Functions**: SMS notifications (lab results, imaging-SMS outbox), payment webhooks (Paystack / Flutterwave callbacks), NHIS API integrations.
- **Vectors**: patient-record semantic search, similar-case retrieval for clinical decision support.
- **Cron + Queues**: scheduled NHIS claim submissions, retry queues, PHI purge schedulers (cf. existing imaging-SMS-outbox PHI purge in Vedge).
- **Caveat**: Vedge currently uses Spring Boot + Postgres + Flyway directly. Adding Supabase would mean a stack split (Spring Boot for some flows, Edge Functions for others). Worth weighing vs the simplicity of the current Spring Boot monolith.

## Mentioned in

- [[wiki/sources/open-design-catalog]] — Open Design catalog entry.

## Related entities

- [[wiki/entities/vercel]], [[wiki/entities/github]] — adjacent in the modern fullstack hosting layer; common Supabase pairings.
- [[wiki/entities/mongodb]], [[wiki/entities/sentry]] — sibling backend / data tools in the Open Design catalog.
- [[wiki/entities/openai]], [[wiki/entities/anthropic]] — Supabase pgvector commonly stores embeddings from these.

## Related concepts

- [[design-md]] — Supabase ships a DESIGN.md via Open Design's catalog.
- [[mcp-server]] — Supabase ships a high-value brand-side MCP.
- [[scheduled-automation]] — Supabase pg_cron is the Postgres-layer equivalent.
- [[byok-proxy]] — adjacent (Supabase Edge Functions can act as application-layer proxies).
- [[markdown-as-agent-contract]] — the supabase skill family encodes contracts for Postgres best practices.
