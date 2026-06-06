---
type: entity
title: Vugola
entity_type: product
created: 2026-05-21
updated: 2026-05-21
website: https://vugolaai.com
aliases: [Vugola AI]
tags: [product, clip-extraction, captioning, ai-video, mcp-server, content-tooling]
---

# Vugola

> AI clip-extraction and captioning service. Takes long-form video → clips 30-60-second segments → adds captions → schedules for distribution. **Ships an MCP server** (`vugola-mcp@1.3.1`) exposing 8 tools: `clip_video / get_clip_status / caption_video / schedule_post / list_scheduled_posts / cancel_scheduled_post / download_clip / get_credits`. Pricing: $14/mo Starter / $21/mo Creator (unlimited posting + API access).

## Use case in wiki

The commercial-clipping playbook documented in [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] uses Vugola as the *clip-extraction* layer, with [[wiki/entities/hermes-agent|Hermes Agent]] orchestrating Vugola + [[wiki/entities/postiz|Postiz]] to run end-to-end clipping pages from one Telegram message. Stack: Hermes (brain) → Vugola (clips) → Postiz (publish).

## Mentioned in

- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — sole canonical source.

## Related concepts

- [[mcp-server]] — Vugola exposes 8 named tools as MCP.
- [[ai-automation-services]] — Vugola is a building block in clipping-page commercial stacks.

## Related entities

- [[wiki/entities/hermes-agent]] — primary orchestrator.
- [[wiki/entities/postiz]] — downstream publish layer.
