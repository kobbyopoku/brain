---
type: source
title: "Akintola Steve — How to Design a Backend That Handles 1 Million Users Without Breaking"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/Akintola_steve/status/2055620856802357587
source_type: x-thread
author: Akintola Steve (@Akintola_steve)
source_date: 2026-05-16
raw_path: raw/How to Design a Backend That Handles 1 Million Users Without Breaking.md
content_status: substantive-verbatim
tags: [backend, system-design, distributed-systems, scalability, architecture, caching, databases, observability, resilience, performance]
---

# Akintola Steve — How to Design a Backend That Handles 1 Million Users Without Breaking

> A 10-section "2026 architecture blueprint" for building a backend that stays fast, cheap, and resilient at 1 million concurrent users — the system-design counterpart to the AI/agent material that dominates this wiki, and direct background reading for the production stacks behind [[wiki/projects/vedge|Vedge]], [[wiki/projects/kivora|Kivora]], and [[wiki/projects/clarvyn|Clarvyn]].

## TL;DR

A concise, opinionated, end-to-end blueprint for a backend at 1M-concurrent-user scale. The load-bearing thesis: *the difference between systems that survive scale and systems that collapse is not talent — it is architectural decisions made early, before the traffic arrives.* It walks the request path from edge (CDN/WAF) → global load balancer → API gateway → stateless application services → sharded databases + caches + event bus → background workers → observability, and closes with consistency patterns (Outbox / Saga / Idempotency Keys), security (mTLS / zero-trust / chaos engineering), and pre-launch discipline (load-test at 2× peak, canary deploys, profile-before-optimize). Strongly prescriptive — names specific tools at every layer.

## Key takeaways

- **Define non-functional requirements first** — the most-skipped step and the reason teams rebuild six months later. Nail peak QPS (10k-50k), P99 latency (under 200ms, target under 100ms), uptime (99.99% ≈ 4 min downtime/month), consistency model (strong for financial data, eventual for feeds/timelines), and a strict cost ceiling per 1,000 users.
- **Use the Scale Cube as a mental model** — three orthogonal scaling axes: X-axis (horizontal duplication / more identical servers), Y-axis (functional decomposition / split into focused services), Z-axis (data partitioning / shard by user ID or region). Claimed to prevent "90% of scaling disasters."
- **Start as a modular monolith; extract microservices only when a specific service is a measured, proven bottleneck.** "Premature microservices are the single biggest killer of engineering velocity at scale."
- **Language/framework by goal** — Go or Rust for raw throughput and memory efficiency; TypeScript (NestJS) or Java/Kotlin (Spring Boot) when team velocity matters more than raw throughput. API strategy: REST + GraphQL public-facing, gRPC internal (typed, fast, streaming).
- **Push work to the edge.** Request path: User → Cloudflare/Fastly (CDN, DDoS, edge caching) → Global Load Balancer (AWS Global Accelerator / GCP equivalent) → API Gateway (rate limiting, WAF, bot detection) → application services. "The edge layer is your first line of defence."
- **Four non-negotiable application-layer rules**: (1) every service stateless — sessions in Redis/Dragonfly, never in app memory; (2) background jobs in a queue — Kafka or Pulsar at this scale, not RabbitMQ, not in-memory, not setTimeout; (3) resilience at the call level — circuit breakers, retries with jitter, hard timeouts on every outbound call; (4) auto-scale on the right signals — CPU is a lagging indicator, scale on queue depth and error rate instead.
- **Never use a single database** — it is both a performance ceiling and a single point of failure. Recommended polyglot stack: PostgreSQL + Citus (primary OLTP, horizontal sharding); Cassandra or ScyllaDB (high-write paths); Redis Cluster (caching / real-time); ClickHouse (analytics / aggregations).
- **Choose your shard key on day one.** Route all writes through a query router (Vitess or Citus); shard by `user_id` via modulo for even distribution; read replicas behind PgBouncer for connection pooling. Changing the shard key after production data exists is "one of the most painful migrations an engineering team can go through."
- **Multi-layer caching is the biggest cost lever** — target a cache hit ratio above 85%. Layer 1: edge CDN cache (static + publicly cacheable). Layer 2: application-level Redis (computed results, sessions, hot records). Layer 3: query-result cache (expensive DB reads). Only a full cache miss reaches the database.
- **Use event-driven cache invalidation via Kafka, not TTL alone** — e.g. a user-profile-update event immediately invalidates the relevant cache keys. "TTL alone is not reliable for critical data."
- **Full observability from day one.** Stack: Prometheus (metrics), Jaeger (distributed tracing), Loki (logs), all instrumented via OpenTelemetry, flowing into Grafana; Alertmanager routes critical alerts to PagerDuty. Instrument the four golden signals on every service — latency, traffic, errors, saturation. Define real SLOs, track error budget, "alert before users notice."
- **Three consistency/idempotency patterns**: Outbox (write events to a DB table in the same transaction as business logic; a background process publishes them — events survive a broker outage); Saga (compensating actions in sequence instead of two-phase commit for cross-service transactions); Idempotency Keys (every mutating op accepts a unique request ID; duplicate requests return the original result — "the only safe way to handle retries on unreliable networks").
- **Eventual consistency is the correct trade-off at scale, not a weakness.**
- **Security baseline**: mTLS between all internal services, zero-trust network (no service trusts another by default), encryption at rest and in transit everywhere, and regular chaos engineering (deliberately kill random pods in production to verify resilience before traffic does).
- **Pre-launch discipline**: start small and measure everything; load-test with k6 or Locust at 2× expected peak before launch; use feature flags + canary deployments (never ship directly to 100%); profile hot paths before optimizing ("the bottleneck is seldom where you think it is"); use spot/preemptible instances for non-critical workloads to cut cost.

## The complete architecture (§10)

```
1 Million Users
  → Edge + CDN + WAF
  → Global Load Balancer
  → API Gateway (Rate Limiting + Auth)
  → Stateless Application Services
  → Redis Cluster / Kafka Event Bus / Sharded PostgreSQL + Cassandra
  → Background Workers
  → Observability Layer (Prometheus, Grafana, Jaeger, Loki)
```

Claimed to handle 1M daily active users "with significant headroom to grow into tens of millions without a fundamental rewrite."

## Notable quotes

> "Building a system that works for 1,000 users is easy. Building one that stays fast, cheap, and rock-solid at 1 million concurrent users is where most engineers fail."

> "Premature microservices are the single biggest killer of engineering velocity at scale."

> "CPU is a lagging indicator. Scale on queue depth and error rate instead."

> "Choose your shard key on day one. Changing it after data is in production is one of the most painful migrations an engineering team can go through."

> "Eventual consistency is not a weakness at this scale. It is the correct architectural trade-off."

> "The difference between systems that survive scale and systems that collapse under it is not talent. It is architectural decisions made early, before the traffic arrives."

> **Further reading** named in the source: *Designing Data-Intensive Applications* by Martin Kleppmann | Uber Engineering Blog | Netflix Tech Blog | ByteByteGo.

## Notes

- **Off the dominant cluster, but high-relevance to the owner's portfolio.** The wiki skews heavily toward AI/agent tooling and AI-services business models; this is a pure backend system-design source. It earns shelf-space because Godwin ships multi-tenant SaaS backends ([[wiki/projects/vedge|Vedge]], [[wiki/projects/kivora|Kivora]], [[wiki/projects/clarvyn|Clarvyn]], [[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]]) — several already on the Spring Boot / PostgreSQL stack this blueprint recommends. It pairs naturally with [[wiki/sources/e_opore-system-design-roadmap]], the other system-design-career source in the wiki.
- **Prescriptive-by-name, not first-principles.** The piece is a tool-checklist (Citus, ScyllaDB, ClickHouse, Vitess, Kafka, Loki, k6) more than a derivation. Treat the specific tool choices as one defensible default set, not gospel — most are interchangeable with peers (e.g. Pulsar↔Kafka, ScyllaDB↔Cassandra, Tempo↔Jaeger). The *patterns* (stateless services, shard-key-on-day-one, event-driven invalidation, Outbox/Saga/Idempotency) are the durable, tool-agnostic content.
- **Connections to existing wiki concepts**: the Outbox pattern is the reliability primitive behind [[wiki/concepts/dual-write-rollout|dual-write rollout]] (Kivora's Finding-schema migration); idempotency keys + event-driven invalidation map onto [[wiki/concepts/scheduled-automation|scheduled-automation]] and broker-backed agent workflows. The "scale on queue depth, not CPU" rule echoes Hermes/Helm's queue-depth-as-pressure-signal ops thinking.
- **Scale-claim caveat**: the headline conflates "1 million concurrent users" (intro) with "1 million daily active users" (§10 close) — these differ by ~2 orders of magnitude in actual QPS. The architecture is sound for either, but the framing is loose; flagged so the numbers aren't over-trusted. No benchmarks or production references are given beyond "every pattern is running in production systems right now."
- **Author is new to the wiki.** @Akintola_steve, single X post (1 of presumably more); no prior context. Treated as an entity stub.

## Mentioned entities

- [[wiki/entities/akintola-steve]] — author of the blueprint.
- [[wiki/entities/postgres]] — primary OLTP store (with Citus for sharding).
- [[wiki/entities/citus]] — Postgres extension for horizontal sharding.
- [[wiki/entities/cassandra]] / [[wiki/entities/scylladb]] — high-write-path stores.
- [[wiki/entities/redis]] / [[wiki/entities/dragonfly]] — session store + application cache.
- [[wiki/entities/clickhouse]] — analytics / aggregation store.
- [[wiki/entities/kafka]] / [[wiki/entities/pulsar]] — event bus / job queue.
- [[wiki/entities/vitess]] — query router / sharding middleware.
- [[wiki/entities/pgbouncer]] — Postgres connection pooler.
- [[wiki/entities/cloudflare]] / [[wiki/entities/fastly]] — CDN + DDoS + edge cache.
- [[wiki/entities/prometheus]], [[wiki/entities/jaeger]], [[wiki/entities/loki]], [[wiki/entities/grafana]], [[wiki/entities/opentelemetry]], [[wiki/entities/alertmanager]], [[wiki/entities/pagerduty]] — observability stack.
- [[wiki/entities/k6]] / [[wiki/entities/locust]] — load-testing tools.
- [[wiki/entities/go-language]], [[wiki/entities/rust-language]], [[wiki/entities/nestjs]], [[wiki/entities/spring-boot]] — recommended languages/frameworks.
- [[wiki/entities/martin-kleppmann]] — author of *Designing Data-Intensive Applications* (further reading).
- [[wiki/entities/bytebytego]] — system-design learning resource (further reading).

## Related concepts

- [[wiki/concepts/backend-scalability-blueprint]] — *(new)* the 10-section blueprint this source defines.
- [[wiki/concepts/scale-cube]] — *(new)* X/Y/Z three-axis scaling mental model.
- [[wiki/concepts/multi-layer-caching]] — *(new)* edge → app → query three-tier cache strategy; >85% hit-ratio target.
- [[wiki/concepts/database-sharding]] — *(new)* shard-key-on-day-one, modulo-by-user_id, query-router routing.
- [[wiki/concepts/outbox-pattern]] — *(new)* transactional event publication for at-least-once delivery.
- [[wiki/concepts/saga-pattern]] — *(new)* compensating-action sequences for cross-service transactions.
- [[wiki/concepts/idempotency-keys]] — *(new)* unique request IDs for safe retries.
- [[wiki/concepts/four-golden-signals]] — *(new)* latency / traffic / errors / saturation per-service instrumentation.
- [[wiki/concepts/observability]] — *(new)* metrics + traces + logs from day one.
- [[wiki/concepts/stateless-services]] — *(new)* sessions externalized so any server can die.
- [[wiki/concepts/zero-trust-security]] — *(new)* mTLS + no-default-trust between internal services.
- [[wiki/concepts/chaos-engineering]] — *(new)* deliberately killing pods to verify resilience assumptions.
- [[wiki/concepts/dual-write-rollout]] — *(existing)* Outbox is the reliability primitive behind it.

## Related sources

- [[wiki/sources/e_opore-system-design-roadmap]] — the other system-design-career source in the wiki; this blueprint is the concrete architectural payload to e_opore's 12-phase learning roadmap.
