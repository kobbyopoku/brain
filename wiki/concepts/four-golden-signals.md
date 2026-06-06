---
type: concept
title: Four Golden Signals
created: 2026-06-06
updated: 2026-06-06
aliases: [golden signals, latency traffic errors saturation]
tags: [backend, observability, monitoring, sre, slo]
---

# Four Golden Signals

> The four core service-health metrics — latency, traffic, errors, and saturation — instrumented on every service as the baseline for defining SLOs and tracking an error budget.

## Definition

The four golden signals are latency (how long requests take), traffic (how much demand a service is under), errors (rate of failing requests), and saturation (how full the service's resources are). [[wiki/sources/akintola-steve-backend-1-million-users]] treats them as the per-service observability baseline — instrumented on every service — and ties them directly to defining real SLOs and tracking an error budget.

## Why it matters

Without a fixed, uniform set of health metrics per service, teams cannot define meaningful service-level objectives or know when they have spent their error budget. The four golden signals give every service the same minimal instrumentation surface, making SLOs and error-budget accounting possible across a fleet. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames them as the per-service observability baseline — latency, traffic, errors, saturation instrumented on every service — tied to defining real SLOs and tracking an error budget.

## Sub-claims and details

- The four signals are latency, traffic, errors, and saturation. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- They are instrumented on every service. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- They are the basis for defining real SLOs and tracking an error budget. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/observability]] — broader practice this metric set sits inside.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
