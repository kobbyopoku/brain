---
type: entity
title: AnyMailFinder
entity_type: product
created: 2026-05-03
updated: 2026-05-03
website: https://anymailfinder.com
aliases: []
tags: [enrichment, lead-generation, mcp-candidate, stub]
---

# AnyMailFinder

> Email-enrichment tool referenced in [[wiki/sources/saraev-agentic-workflows-2026]] as part of a worked lead-scraping workflow. *"I also already have a pre-existing subscription to AnyMailFinder, which is an enrichment tool."*

## Profile

This page is a **stub**. AnyMailFinder appears in this wiki only via Saraev's worked example of a [[do-framework|DO-framework]] lead-scraping workflow. The tool's role: take a list of company-name + first-name + last-name tuples and return verified email addresses. No primary source about AnyMailFinder's product surface, pricing, or accuracy claims is yet ingested.

## Key facts

- **Website**: https://anymailfinder.com
- **Role per source**: email enrichment in a lead-scraping workflow's DO chain. Saraev calls it from a directive after scraping company names from search results.
- **MCP-relevance**: a candidate for an MCP server wrapper if Saraev's "research the docs once, save to markdown" pattern from [[wiki/sources/nateherk-claude-code-os-3m-business|nateherk]] is applied — i.e. you'd save the AnyMailFinder API spec as a reference doc that workflows pull from.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]

## Related concepts

- [[do-framework]] — used as an execution component in Saraev's example.
- [[mcp-server]] — adjacent: AnyMailFinder is the kind of API service that benefits from MCP wrapping (or the API-saved-as-markdown alternative).
- [[ai-automation-services]] — enrichment tools like this are common building blocks.
