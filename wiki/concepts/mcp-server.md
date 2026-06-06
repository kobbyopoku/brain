---
type: concept
title: MCP Server
created: 2026-05-02
updated: 2026-06-06
aliases: [MCP, Model Context Protocol server]
tags: [claude-code, integration, infrastructure, tool-use]
---

# MCP Server

> A server speaking the Model Context Protocol that exposes external tools (search engines, file stores, email, communications, third-party APIs) to Claude as native callable capabilities — turning a chatbot into an automation platform.

## Definition

An **MCP server** is a process that implements the Model Context Protocol, advertising a set of tools (with name, description, and arguments) that an LLM agent like Claude can call directly. The agent connects to one or more MCP servers and treats their tools as native — no glue code in the prompt, no function-call shim. This is the integration layer between the LLM and the outside world: web search, files, email, chat, databases, vendor APIs.

## Why it matters

Without MCP, an agent is a closed system that can read what the user pastes and produce text. With MCP, the agent can act in the world: read a file, send an email, query an API, post to a channel. [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah]] frames the distinction crisply: *"connecting Claude to external tools is what separates a chatbot from an automation system."*

For [[ai-automation-services]] specifically, MCP is the layer where the *value* is delivered — a skill file describes a workflow, but only an MCP-enabled environment can actually do the work. For [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]]'s setup, MCP is implicit but central — every "agent runs while you sleep" workflow requires MCP-mediated access to the repo, GitHub, the deploy pipeline.

## Treatment across sources

- [[wiki/sources/khairallah-ai-automations-10k-month]] — the canonical source for the concept in this wiki. Names four concrete MCP servers a services builder must master: [[wiki/entities/tavily]] (web search), [[wiki/entities/google-drive]] (file access), [[wiki/entities/gmail]] (email), [[wiki/entities/slack]] (communications). Practice exercise: chain all four (search web → save summary to Drive → email it → post to Slack channel).
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — uses MCP implicitly throughout (GitHub interactions in `/fix-issue`, deploy pipelines in `/deploy staging`, security scanning in pre-push hooks) but does not theorize the layer.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — the **cost counterpoint**. MCP tool definitions are the 6th-largest [[claude-code-overhead-patterns|overhead pattern]] (~6% of tokens). Each connected MCP ships its tool schema to every request regardless of whether the task involves it. Author had 12 MCPs × ~600 avg tokens = 7,200 tokens of tool defs per request; cut to 3 always-on, saved 6,000 tokens per request. PostgreSQL MCP alone is ~1,200 tokens.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — **operational alternative**: prefer API endpoints saved as markdown over MCPs. *"MCPs load every endpoint and every function whether you need it or not. That eats tokens. Tell Claude: research the docs once, save them as a markdown reference, pull from that file when you need an endpoint. Markdown is cheap to read; API docs are expensive to crawl every time."* Same insight as Mnilax's cost analysis from a different starting point.
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. [[wiki/entities/open-design|Open Design]] **exposes** an MCP server (rather than just consuming them) — the daemon ships `search_files`, `get_file`, `get_artifact` as MCP tools so coding agents in *other* repositories can query Open Design projects directly without export/import loops. This is "design system as MCP-queryable knowledge" — a sibling pattern to Refero MCP but local-first. Notable architectural inversion: most wiki sources treat MCP as the *consumer* layer for an agent; Open Design treats it as the *provider* layer for cross-repo agent integration.
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — *2026-05-08*. **Strongest tool-layer reliability articulation in the wiki.** NainsiDwiv's 7-step roadmap — Protocol / Tool definitions as contracts / Error handling / Parallelization / Catalog size / Security / Evaluation — treats the tool surface (which MCP servers expose) as a discrete reliability discipline rather than a side-effect of agent design. Quote: *"Reliable agents treat the model as a reasoning engine — not an execution engine."* Worth absorbing into MCP design discipline: when a wiki source ingests a new MCP-exposing product, evaluate its tool surface against these 7 dimensions. Particularly relevant to step 5 (catalog size): aligns with [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax]]'s 12-MCPs-becomes-7,200-tokens overhead finding — too many MCPs is a tool-catalog problem, not a model problem.
- [[wiki/sources/Ai_here202-mcp-opportunity]] — *2026-05-09*. The **business-opportunity view** complementing NainsiDwiv's engineering-discipline view. Cleanest analogy in the wiki: *"MCP is USB for AI."* 3-capability framing: **Tools** (functions the AI can DO) / **Resources** (data the AI can REFERENCE) / **Prompts** (templates the AI should FOLLOW). Frames the ecosystem as *"the App Store in 2009"* with a ~2-year window before drag-and-drop builders + no-code + pre-built servers shrink the premium. **Pricing data**: freelance custom MCP builds $5K-$15K, productized $50-$200/mo or $500-$2K lifetime, enterprise $25K-$100K (consulting + customization + maintenance). Highest-margin verticals: industry-specific workflows (real estate / marketing / e-commerce).
- [[wiki/sources/zodchiii-x-claude-code-settings]] — *2026-05-09*. Adds a *third* token-cost data point: *"MCP servers load 18K+ tokens per turn per server. 5+ servers = 90K tokens of overhead before your first prompt."* Higher than [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's]] 600-token average; consistent with PostgreSQL-MCP-tier servers. Strengthens the trim-MCP-servers canon. Operational fix: `/mcp` command to inspect tool counts per connected server.
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — *2026-06-06*. The thread is effectively an MCP-server inventory — most of the named "plugins" (GitHub, Playwright, Filesystem, Database, Browser Tools) are MCP servers extending Claude Code's reach to repos, browsers, files, and databases.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — *2026-06-06*. Stage VI item 6 of the AI-engineer roadmap; advises learning to build, deploy, and connect MCP servers/clients to models as systems standardize tool/data/API connections.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — *2026-06-06*. Deployment principle "build APIs over existing data layer (SharePoint/databases) + model as orchestrator" and the named portfolio project "an MCP connecting an LLM to legacy software" instantiate the MCP-over-legacy pattern.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — *2026-06-06*. Layer 6. Treats connectors (Gmail/Calendar/Drive/Slack + "MCP connectors") as the tool-integration layer that grounds Claude's outputs in the user's real email/calendar/Slack data.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — *2026-06-06*. The Filesystem MCP is the read/write bridge between Claude Code and the Obsidian vault, enabling both the briefing (read) and property writeback (write).
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — *2026-06-06*. Named in the AI-engineer roadmap layer 3 (MCP for tool access).
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — *2026-06-06*. Pattern 3: the Shopify dev MCP server (7 tools) is presented as essential to stop Claude hallucinating API fields — grounding the agent in real docs/schemas/operations.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — *2026-06-06*. MCP and A2A framed as interop foundations (not marketplaces) underpinning the discovery layer; the MCP server registry pattern "indexes tools, not autonomous services."
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — *2026-06-06*. Phase 5; Anthropic MCP courses; framed as "the standard way AI systems connect to tools, APIs, and external environments."

## Sub-claims and details

### MCP as "USB for AI" (cleanest analogy)

Per [[wiki/sources/Ai_here202-mcp-opportunity|Ai_here202]]: *"Before USB every device needed its own cable and its own port. USB standardized the connection so any device could plug into any computer. MCP does the exact same thing for AI tools."* Build one MCP server → it works with Claude Code + Claude Desktop + Cursor + Windsurf + every MCP-compatible client. **The standardization is what creates the market** — companies want servers they plug in, not bespoke per-vendor integrations.

### Three things every MCP server can expose

| Capability | Symbol | What | When to use |
|---|---|---|---|
| **Tools** | 🔧 | Functions the AI can call (search DB, send email, create record) | Highest value; "DO" actions |
| **Resources** | 📄 | Data the AI can read (documents, DB records, API responses) | "REFERENCE" data |
| **Prompts** | 📋 | Pre-built templates the AI follows (SOPs, frameworks) | "FOLLOW" consistency |

Most MCP servers focus on Tools because that's where highest value is. The best servers combine all three.

### Original sub-claims

- **Protocol**: Model Context Protocol — open spec for advertising tools to LLM agents.
- **Server topology**: each MCP server exposes a set of tools. An agent can connect to multiple servers simultaneously and call any tool from any server.
- **Tool shape**: name, description, argument schema. The description is what the agent reads to decide whether to call.
- **Composition with [[claude-code-skills]]**: a skill that calls external tools is an MCP-dependent skill. Without the relevant MCP server connected, the skill silently degrades.
- **Composition with [[claude-code-hooks]]**: hooks can also invoke MCP tools (e.g. a pre-commit hook that posts a Slack notification).
- **MCP server distribution**: typically open-source; configured per-machine or per-Claude-Code-environment.
- **Common categories of MCP server**: search engines (Tavily, web-fetch), document stores (Google Drive, Notion, Obsidian), communications (Gmail, Slack), code platforms (GitHub, GitLab), observability (PostHog, Datadog), payments (Stripe), databases (Supabase, Postgres), and many more.

### Tool-layer reliability checklist (NainsiDwiv)

Per [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap|NainsiDwiv's 7-step roadmap]], a production MCP integration should satisfy seven discrete reliability properties:

1. **Protocol** — the wire format and lifecycle (MCP itself answers this).
2. **Tool definitions as contracts** — name + description + arg schema are *what the model reads to decide*. Treat them as durable interfaces, not afterthoughts.
3. **Error handling** — every tool can fail; failure modes must be enumerated and surfaced to the model so it can recover.
4. **Parallelization** — tools that don't conflict should be callable in parallel; serial-only constraints should be explicit.
5. **Catalog size** — too many tools degrade selection accuracy and cost tokens (see [[wiki/sources/Mnilax-430-hours-claude-code-waste]]). Trim aggressively.
6. **Security** — auth scope, credential isolation, capability minimization.
7. **Evaluation** — measure tool-call success rates, latency, and cost; iterate.

The first three are *design-time* properties; the last four are *operational* properties. A complete MCP integration touches all seven.

## Open questions and contradictions

- **Auth and credential management**: MCP servers require credentials (Google OAuth, Slack tokens, API keys). The lifecycle of these credentials — issuance, rotation, scoping — is a real operational surface that the current sources don't address.
- **Sandboxing**: if a Slack MCP server can post messages, can it post messages to channels the user didn't intend? Permission scoping matters and is unsourced here.
- **Reliability**: an MCP server going down causes the dependent skill to fail. Failure semantics (retry, degrade, alert) are an operational concern.
- **Cost**: MCP-mediated tool calls often hit metered third-party APIs (search, email send). Total cost of an automation is the sum of Claude tokens *plus* downstream service usage. Total-cost transparency is unsolved.
- **Discovery**: how does a user know which MCP servers are connected and what tools they expose? UI surface vs. inspection.

## Related concepts

- [[claude-code-skills]] — composes naturally; many skills are MCP-dependent.
- [[claude-code-hooks]] — can also invoke MCP tools.
- [[scheduled-automation]] — typically MCP-heavy (a daily briefing reads multiple MCP-mediated sources).
- [[ai-automation-services]] — MCP is one of the four core competencies of this business model.

## Related entities

- [[wiki/entities/claude-code]] — the platform that consumes MCP.
- [[wiki/entities/tavily]] — web search MCP.
- [[wiki/entities/google-drive]] — file-access MCP.
- [[wiki/entities/gmail]] — email MCP.
- [[wiki/entities/slack]] — communications MCP.

- [[wiki/entities/refero]] — ships an MCP server (Refero MCP) for AI coding tools.
- [[wiki/entities/open-design]] — exposes an MCP server with `search_files` / `get_file` / `get_artifact`.

## Mentioned in

- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/nexu-io-open-design]]
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — strongest tool-layer reliability articulation; 7-step checklist for MCP integration discipline.
- [[wiki/sources/Ai_here202-mcp-opportunity]] — *2026-05-09*. Business-opportunity view; USB-for-AI analogy; 3-capability framing; App-Store-2009 market timing.
- [[wiki/sources/zodchiii-x-claude-code-settings]] — *2026-05-09*. Third token-cost data point (18K+ per server / 90K with 5 servers).
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — *2026-06-06*. "Plugin" inventory that is mostly MCP servers (GitHub, Playwright, Filesystem, Database, Browser Tools).
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — *2026-06-06*. Roadmap Stage VI: build/deploy/connect MCP servers and clients.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — *2026-06-06*. MCP-over-legacy deployment pattern + portfolio project.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — *2026-06-06*. MCP connectors as the personal-AI tool-integration layer (layer 6).
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — *2026-06-06*. Filesystem MCP as read/write bridge to the Obsidian vault.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — *2026-06-06*. MCP for tool access (roadmap layer 3).
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — *2026-06-06*. Shopify dev MCP server (7 tools) grounds the agent against API hallucination.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — *2026-06-06*. MCP/A2A as interop foundations; registry indexes tools not services.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — *2026-06-06*. Phase 5; MCP as the standard tool/API connection layer.
