---
type: synthesis
title: Multi-Agent Ops Platform — Reusable Blueprint
created: 2026-05-09
updated: 2026-07-22
aliases: [multi-agent-blueprint, ops-platform-blueprint, agent-stack-blueprint]
tags: [synthesis, multi-agent, blueprint, reference-architecture, doe-framework, self-annealing]
---

# Multi-Agent Ops Platform — Reusable Blueprint

> **Reference architecture** for building a multi-agent operations platform that automates a small business's GTM + business operations. Synthesized from 7+ wild-cited multi-agent system descriptions in the brain ([[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT]] → [[wiki/sources/eng_khairallah1-x-2052684086414852546|Khairallah]] → [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]] → [[wiki/sources/nateherk-claude-code-os-3m-business|Nateherk]] → [[wiki/sources/Shruti_0810-self-improving-obsidian|Shruti]] → [[wiki/sources/shannholmberg-content-os|Shann Holmberg]]) plus the architectural foundations ([[wiki/concepts/do-framework|DOE]] / [[wiki/concepts/reasoning-execution-split|reasoning-execution-split]] / [[wiki/concepts/markdown-as-agent-contract|markdown-as-agent-contract]] / [[wiki/concepts/self-annealing|self-annealing]]). Worked example: [[wiki/projects/helm|Helm]] (ROAM Labs internal ops platform, 2026-05-09).

## When to use this blueprint

You should reach for this synthesis when designing **any agent system that meets all five criteria**:

1. **Multi-functional** — at least 3 distinct functional roles (sales / marketing / operations / etc.), each better-served by a specialized agent than a generalist.
2. **Knowledge-compounding** — agents share state across runs (not pure stateless API wrappers).
3. **Scheduled + on-demand** — at least one agent runs on a cron schedule (morning briefing, monthly review) and at least one runs on-demand.
4. **Production reliability matters** — failure modes can cost money or relationships (vs hobby experiments).
5. **Single small org** — one human or a small team, not a public-multi-tenant SaaS.

If only 2-3 of those apply, reach for a simpler pattern (single skill file, single Cowork session, single Hermes Agent instance with default skills).

## The five-layer architecture

```
┌────────────────────────────────────────────────────────────┐
│ LAYER 5: Specialized agents (3-6, role-bounded)            │
│   Lead Mgmt / Sales / Marketing / Ops / PM / Analytics     │
└─────────────────────┬──────────────────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────────────────┐
│ LAYER 4: Frontend supervision UI                           │
│   Single-tenant dashboard; agent state; review queues      │
└─────────────────────┬──────────────────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────────────────┐
│ LAYER 3: Orchestrator / API / scheduler                    │
│   Routes requests to agents; cron triggers; auth           │
└─────────────────────┬──────────────────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────────────────┐
│ LAYER 2: Shared knowledge layer                            │
│   PostgreSQL + pgvector; voice profiles; agent logs        │
└─────────────────────┬──────────────────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────────────────┐
│ LAYER 1: Agent runtime + model routing                     │
│   Hermes Agent / Anthropic SDK / LangGraph / etc.          │
└────────────────────────────────────────────────────────────┘
```

Each layer has its own design choices, with cross-layer dependencies explicit.

## Layer 1 — Agent runtime: three real options

| Choice | When to pick | Trade-offs |
|---|---|---|
| **Build on existing stack** (Spring Boot + FastAPI + Anthropic SDK) | You already have a similar agent service running (Clarvyn, Kivora). Reuse compounds. | High control; high build time; no built-in skills |
| **Hermes Agent** ([[wiki/entities/hermes-agent]]) | Internal tool, ship-speed > stack-elegance. Need built-in messaging surfaces (Telegram / Slack / Email / CLI). | MIT-licensed; 200+ provider routing via OpenRouter ([[wiki/entities/openrouter]]); built-in memory + skills; ~219K stars (2026-07-22); young but massively adopted |
| **Anthropic Claude Agent SDK** | Pure-Anthropic shop, want native MCP, willing to write more glue | Most native MCP support; younger; less battle-tested than Hermes |

(LangGraph / CrewAI / AutoGen are also options; the wiki has thinner coverage of those.)

**Default for Godwin's stack**: Hermes Agent for internal tools (Helm), build-on-existing for product-bearing agent services (Clarvyn, Kivora, future Vedge agent).

## Layer 2 — Shared knowledge layer (always pgvector)

Every agent reads and writes the same Postgres + pgvector database. Tables that recur in every multi-agent ops platform:

| Table | Purpose | Used by |
|---|---|---|
| `leads` | Prospect identification + signal scoring | Lead Mgmt → Sales |
| `deals` | Pipeline + stage + close-rate analytics | Sales |
| `customers` | Won deals + relationship state | Sales → Operations |
| `voice_profiles` | Per-product/per-brand voice (embedded) | Marketing |
| `content_drafts` | Run-folder-style content objects | Marketing |
| `invoices` / `expenses` | Financial state | Operations |
| `project_status` | Cross-project dashboards | PM |
| `agent_logs` | Per-call execution trace + cost | Analytics |
| `agent_optimizations` | Monthly system-prompt change recommendations | Analytics → all |

**Critical design choice**: shared knowledge layer or per-agent silos? **Always shared** for cross-functional ops. The Lead Mgmt agent qualifies prospects → Sales agent picks up the same record → Operations agent invoices the closed deal. If each agent has its own DB, you lose handoff context.

## Layer 3 — Orchestrator / API / scheduler

Three responsibilities:

1. **HTTP API surface** — frontend calls `/agents/lead/qualify`, `/agents/marketing/draft`, etc.
2. **Cron triggers** — 7AM morning briefing, 5PM end-of-day wrap-up, 1st-of-month Analytics review (the [[wiki/sources/eng_khairallah1-x-2052684086414852546|Khairallah three-session pattern]]).
3. **Auth** — single-user JWT or session if internal-only; full RBAC if eventually-extractable.

Stack choices:
- **FastAPI** if Layer 1 is Hermes Agent or Anthropic SDK (Python).
- **Spring Boot** if Layer 1 is your own Java/Kotlin agent runtime.
- **Node.js + Hono** if Layer 1 is TypeScript-first.

Scheduling primitives: APScheduler (in-process) for low-volume; Railway cron / SQS for higher reliability.

## Layer 4 — Frontend supervision UI

The required pages, in priority order:

1. **Dashboard** — agent status (running / idle / error), today's pipeline summary, decisions-needed inbox.
2. **Per-functional pages** — one page per agent's data domain (Leads / Deals / Marketing / Operations / Projects).
3. **Agents page** — system-prompt editor, system-prompt change history, monthly Analytics-agent recommendations.
4. **Logs** — agent execution traces for debugging.

**Always single-page-app for low-friction**: Next.js + Vercel is the path of least resistance. If you're already running React 19 + Vite (Clarvyn / Kivora style), use that.

**Don't build a public marketing surface for an internal tool.** No login screen polish, no onboarding, no docs site. Single-user JWT or session is fine.

## Layer 5 — The agent layer (3-6 agents, role-bounded)

The canonical 5-agent + 1-meta-orchestrator pattern from [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT]]:

| # | Agent | Job | When to include |
|---|---|---|---|
| 1 | **Research** | Structured briefs from multiple sources; counterintuitive angles | Always (cheapest week-1 build) |
| 2 | **Content / Marketing** | Voice-aware drafts; AI-SEO; cross-channel posting | If content is a meaningful part of the business |
| 3 | **Customer Communication** | Triage + draft + escalate (4-tier urgency) | If customer comms volume is meaningful |
| 4 | **Operations** | Reports, dashboards, alerts on threshold breaches | Always |
| 5 | **Analytics (meta-orchestrator)** | Monthly performance review; system-prompt rewrites for the other 4 | Always (Week N — last) |

**For ROAM-Labs-style multi-product orgs**, swap "Research" for **Lead Management** (revenue impact > generic research) and add **Project Management** as a 6th agent (cross-project visibility):

| # | Agent | Job |
|---|---|---|
| 1 | Lead Management | Prospect identification + qualification + outreach |
| 2 | Sales | Pipeline + deal-stage + proposal + close |
| 3 | Marketing | Voice-aware multi-product content + AI-SEO |
| 4 | Operations | Invoicing + collections + expenses + reports |
| 5 | Project Management | Cross-project visibility + risk flags |
| 6 | Analytics | Meta-orchestrator (always last) |

## The master CLAUDE.md template

Every multi-agent platform needs a **master system context** that governs all agents. Per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's]] verbatim template:

```markdown
# Master System Context

## Business Overview
[2-3 sentences: who the org is, what it does, who it serves]

## Agent Roster
- Agent 1: [one-line job description]
- Agent 2: [one-line job description]
- ...

## Shared Standards
- Reasoning vs execution: agents reason; tools execute.
- Cite or omit: every claim links to a verifiable source.
- Cost discipline: Sonnet 80%, Opus for complex reasoning, Haiku for simple.
- Output format: structured (no rambling prose).

## Current Focus
[Updated weekly: this week's priorities]

## Hard Rules That Apply to All Agents
- NEVER promise anything unauthorized.
- NEVER reference competitors by name in client-facing copy.
- ESCALATE when uncertain about scope, price, or authority.
- Scheduled communications run in review mode for 14 days before automation.
```

Per [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's]] cost discipline: target master CLAUDE.md ≤ 1,500 tokens. Every word ships on every turn of every session. **Be ruthless about cuts.**

## The 6-week sequential build order

Per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT]]:

> *"Do not build all five agents simultaneously."*

The order matters because each agent's outputs become inputs for the next.

**5-agent variant** (CyrilXBT shape — Research / Content / Communication / Operations / Analytics):

- **Week 1**: Agent 1 (the MVP / fastest revenue-impact).
- **Week 2**: Agent 2. Connect to Agent 1's output. Verify handoff.
- **Week 3**: Agent 3. Connect. Verify.
- **Week 4**: Agent 4. Run in *review mode* (no automated send) for 2 weeks before going automated. Customer-facing agents especially.
- **Week 5**: buffer / refinement.
- **Week 6**: Agent 5 (Analytics meta-orchestrator). By now the other 4 have generated enough data to actually analyze.

**6-agent variant** (Helm shape — Lead Mgmt / Sales / Marketing / Operations / PM / Analytics):

- **Weeks 1-4**: Agents 1-4 (same cadence as above).
- **Week 5**: Agent 5 (the 5th specialized agent — e.g. Project Management for Helm). No buffer; the meta-orchestrator slides to Week 6.
- **Week 6**: Agent 6 / Analytics meta-orchestrator.

Total build time: **6 weeks of evenings + weekends** in either variant. Daily operating time post-build: **30-60 minutes** reviewing outputs + approving communications + decisions only the human can make.

## The Analytics agent — most architecturally important

> *"The system learns. Every agent gets better every month. The compound effect over 12 months is dramatic."*

The 5th-or-6th agent (Analytics) reads `agent_logs` for the previous 30 days and generates **specific system-prompt changes** for the other agents. This is [[wiki/concepts/self-annealing|self-annealing]] codified into the architecture. Without it, your system runs the same way in week 52 as in week 6. With it, every agent gets monthly optimization.

**Critical safety constraint**: Analytics agent's prompt rewrites do **NOT** auto-apply. The human reviews and approves each one. Auto-applying agent prompts to other agents is unsafe.

## Cost discipline (from day 1)

Per [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax]] + [[wiki/sources/zodchiii-x-claude-code-settings|zodchii]]:

1. **Master CLAUDE.md**: ≤ 1,500 tokens combined.
2. **MCP catalog discipline**: only connect MCPs each agent actively uses. Per-agent MCP scope, not global.
3. **Model routing** (per [[wiki/sources/zodchiii-x-claude-code-settings|zodchii]]): Sonnet 80%, Opus for complex reasoning only, Haiku for simple categorization.
4. **Budget caps per agent run**: `--max-budget-usd` style caps to prevent runaway loops in scheduled jobs.
5. **Use [[wiki/entities/openrouter|OpenRouter]]** if Layer 1 supports it — lets you experiment with cheaper providers (Haiku 3.5, GPT-4o-mini, DeepSeek) for non-critical agent tasks.

**Target operating cost** for a small business: **$100-300/mo total LLM spend**. Comparison anchor (per [[wiki/sources/cyrilxbt-x-2052570518667378918]]): CyrilXBT's equivalent 5-agent system reports **~$89 hosting + $700-900 API spend = $800-1,000/mo total** at production volume, *or* ~$105/mo at minimum config (Claude Max + N8N self-hosted + free Supabase + free Obsidian). Lower-volume internal use should land closer to the minimum-config end.

## The 7-step tool-calling reliability rubric (per integration)

Per [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap|NainsiDwiv]]:

1. **Protocol** — MCP wire format.
2. **Tool definitions as contracts** — name + description + arg schema as durable interfaces.
3. **Error handling** — every tool failure surfaced to the agent for recovery.
4. **Parallelization** — explicit conflict-free vs serial-required annotations.
5. **Catalog size** — trim aggressively.
6. **Security** — auth scope minimization, credential isolation per agent.
7. **Evaluation** — track success rates, latency, cost per call.

Apply this checklist before any new MCP integration. The first three are *design-time* properties; the last four are *operational* properties.

## Open questions / known gaps in the blueprint

- **Multi-tenant version**: this blueprint is single-org. Multi-tenant changes Layers 2 and 3 substantially (row-level security, tenant-scoped agent context).
- **Engineering-ops agents**: this blueprint covers GTM + biz ops only. Engineering-ops (PR review, deploy, QA) is canonized separately by [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_'s]] 5-role pattern. Different shape.
- **Voice profile collection**: the *"feed Claude 20 best pieces"* pattern works for content-heavy products but is unproven for pure-B2B technical products with no published content. Document case-by-case.
- **Analytics agent prompt-rewrite quality**: bad rewrites could degrade the other agents. Mitigation: review-mode permanent + system-prompt change history with rollback.
- **Cross-product context bleed**: a Lead-Mgmt agent that knows about all 3 products might cross-sell incoherently. Mitigation: per-prospect *primary product* tag + lead-with-primary policy.

## Worked example

[[wiki/projects/helm]] — ROAM Labs internal ops platform, started 2026-05-09. Hermes Agent runtime + FastAPI on Railway + Next.js on Vercel + 6 agents. Direct application of every section of this blueprint.

## Composition with other wiki concepts

- [[multi-agent-orchestration]] — primary concept this blueprint instantiates.
- [[do-framework]] — every agent is a Directive + Orchestration + Execution cycle.
- [[reasoning-execution-split]] — the architectural foundation.
- [[self-annealing]] — Analytics agent codifies the pattern.
- [[hot-cache]] — daily morning briefing pattern.
- [[scheduled-automation]] — cron triggers.
- [[markdown-as-agent-contract]] — master CLAUDE.md + per-agent skill files.
- [[mcp-server]] — 7-step reliability rubric per integration.
- [[anti-ai-slop-machinery]] — Marketing agent loads master avoid-slop document.
- [[claude-code-overhead-patterns]] — cost discipline from day 1.
- [[reliability-decay-math]] — N agents × P% per-step compounds; aggressive error handling required.

## Source authority

This blueprint compresses claims from:

- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — verbatim 5-agent system + master CLAUDE.md + 6-week build order.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — three-session daily scheduling.
- [[wiki/sources/saraev-agentic-workflows-2026]] — DOE framework architectural foundation.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — subagent specialization at engineering scope.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — AI OS pattern at $3M/yr scale.
- [[wiki/sources/shannholmberg-content-os]] — Content OS framework + voice-profile-from-20-best-pieces.
- [[wiki/sources/exploraX_-google-maps-leadgen]] — Lead Management agent playbook.
- [[wiki/sources/ig_claims-x-meta-retargeting]] — Sales agent's Conviction Gap proposals.
- [[wiki/sources/bloggersarvesh-20-seo-prompts]] — Marketing agent SEO prompt-pack.
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — 7-step tool-layer reliability rubric.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] + [[wiki/sources/zodchiii-x-claude-code-settings]] — cost discipline.
- [[wiki/entities/hermes-agent]] — runtime option (a).

When the brain accumulates additional multi-agent system descriptions, this blueprint should refresh.
