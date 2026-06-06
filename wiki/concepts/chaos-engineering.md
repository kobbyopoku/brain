---
type: concept
title: Chaos Engineering
created: 2026-06-06
updated: 2026-06-06
aliases: [chaos testing, kill random pods, resilience testing]
tags: [backend, reliability, resilience, sre, testing]
---

# Chaos Engineering

> The practice of deliberately injecting failure into production — such as killing random pods — to verify resilience assumptions before real traffic exposes them.

## Definition

Chaos engineering tests a system's resilience by intentionally causing failures under controlled conditions and observing whether the system survives as designed. [[wiki/sources/akintola-steve-backend-1-million-users]] describes deliberately killing random pods in production to verify resilience assumptions before real traffic does.

## Why it matters

Resilience that is only assumed has never been tested; the first real proof usually arrives during an outage. The source's argument: "Discovering a failure mode in a controlled test is infinitely better than discovering it during a traffic spike at 2am" — chaos engineering moves the discovery of failure modes to a time and place the operators choose. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as deliberately killing random pods in production to verify resilience assumptions before real traffic does, arguing that discovering a failure mode in a controlled test is infinitely better than discovering it during a 2am traffic spike.

## Sub-claims and details

- Random pods are killed deliberately in production. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- The goal is to verify resilience assumptions before real traffic forces the issue. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Rationale: "Discovering a failure mode in a controlled test is infinitely better than discovering it during a traffic spike at 2am." ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/observability]] — prerequisite: you must be able to see the system to evaluate a chaos experiment.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
