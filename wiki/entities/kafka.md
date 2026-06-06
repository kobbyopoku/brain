---
type: entity
title: Apache Kafka
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [Kafka]
tags: [backend-data, event-streaming, message-queue, stub]
---

# Apache Kafka

> Distributed event-streaming platform / message bus. Appears in this wiki via [[wiki/sources/akintola-steve-backend-1-million-users]].

## Profile

This page is a **stub**. Apache Kafka appears in the wiki only via the [[wiki/sources/akintola-steve-backend-1-million-users]] ingest. No primary source about Kafka has been ingested.

## Key facts

- **Recommended use** (per [[wiki/sources/akintola-steve-backend-1-million-users]]): background jobs at 1M-user scale (with Pulsar), explicitly preferred over RabbitMQ.
- Used as the event bus for event-driven cache invalidation: a profile-update event invalidates cache keys.
- Appears in §10 as the "Kafka Event Bus."

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]] — recommended background-job queue / event bus; also drives event-driven cache invalidation.

## Related entities

- [[wiki/entities/pulsar]] — named alongside Kafka as a queue option for background jobs.
