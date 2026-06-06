---
type: concept
title: Outbox Pattern
created: 2026-06-06
updated: 2026-06-06
aliases: [Outbox Pattern, transactional outbox]
tags: [backend, messaging, reliability, system-design]
---

# Outbox Pattern

> A reliability pattern that writes outgoing events to a database table inside the same transaction as the business logic, so events are never lost if the message broker is unavailable.

## Definition

The Outbox Pattern writes events to a database table within the same transaction as the business logic; a background process then reads and publishes them. Because the event and the business write commit atomically, events survive even if the broker goes down. As framed in [[wiki/sources/akintola-steve-backend-1-million-users]], it is the source's reliability primitive for at-least-once event delivery.

## Why it matters

It closes the gap between committing a business change and publishing the event that announces it — a gap where naive implementations lose events when the broker is unavailable. It is the consistency-section reliability primitive of the [[backend-scalability-blueprint]].

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as: write events to a DB table inside the same transaction as business logic; a background process reads and publishes them, so events are never lost even if the broker goes down — the source's reliability primitive for at-least-once event delivery.

## Sub-claims and details

- Events are written to a DB table inside the same transaction as the business logic. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- A background process reads the table and publishes the events. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Events are never lost even if the broker goes down. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- It is the source's reliability primitive for at-least-once event delivery. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- Sourced from a single page; no independent corroboration in the wiki yet.

## Related concepts

- [[backend-scalability-blueprint]] — reliability primitive within the consistency section.
- [[saga-pattern]] — paired cross-service consistency approach in the same section.

## Related entities

- [[wiki/entities/akintola-steve]] — author of the source.

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
