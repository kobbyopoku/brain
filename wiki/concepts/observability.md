---
type: concept
title: Observability
created: 2026-06-06
updated: 2026-06-06
aliases: [observability stack, metrics tracing logging, telemetry]
tags: [backend, observability, monitoring, sre, opentelemetry]
---

# Observability

> The practice of instrumenting a system with metrics, traces, and logs from day one so its internal state can be inferred from its outputs — on the premise that you cannot debug what you cannot see.

## Definition

Observability is the ability to understand a running system's internal state from the telemetry it emits. [[wiki/sources/akintola-steve-backend-1-million-users]] prescribes full observability from day one, composed of metrics, distributed tracing, and logs collected via a common instrumentation standard and routed into dashboards and alerting.

## Why it matters

The source's governing claim is "you cannot debug what you cannot see": at scale, failures are diffuse and intermittent, and without metrics, traces, and logs in place before incidents occur, operators are blind. Treating observability as a day-one requirement rather than a retrofit is what makes a large system operable. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as full observability from day one — Prometheus (metrics) + Jaeger (tracing) + Loki (logs) collected via OpenTelemetry into Grafana, with Alertmanager paging PagerDuty — on the principle "you cannot debug what you cannot see."

## Sub-claims and details

- Observability should be in place from day one, not retrofitted. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- The named stack: Prometheus for metrics, Jaeger for tracing, Loki for logs. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Telemetry is collected via OpenTelemetry and surfaced in Grafana. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Alertmanager routes alerts to PagerDuty. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Governing principle: "You cannot debug what you cannot see." ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/four-golden-signals]] — the per-service metric set that this observability practice instruments.
- [[wiki/concepts/chaos-engineering]] — depends on observability to verify resilience under deliberate failure.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
