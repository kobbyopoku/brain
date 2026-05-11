---
type: project
title: Helm
created: 2026-05-09
updated: 2026-05-10
status: active
repo: multi-repo (local .git in each of helm-backend, helm-portal, helm-mcp as of 2026-05-09; outer wrapper at /Users/kobbyopoku/ROAM/CascadeProjects/helm has no .git; remotes pending github.com/ROAM-Labs/{helm-backend,helm-portal,helm-mcp} org creation per Q2)
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/helm
stack: [hermes-agent, python-3.11, fastapi, alembic, postgres, pgvector, openrouter, next.js, react-19, typescript, tailwind, railway, vercel, docker-compose]
started: 2026-05-09
owner_org: roam-labs
affiliation: roam-labs-internal
name_confirmed: 2026-05-09
repo_topology: multi-repo-wrapper
aliases: [roam-helm, roam-ops-platform]
tags: [project, multi-agent, internal-tool, hermes-agent, ops-automation, lead-management, marketing, sales, project-management, single-user, multi-repo]
---

> **Lineage**: internal multi-agent operations platform for [[wiki/entities/roam-labs|ROAM Labs]] ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder + sole user). **Internal-only for v1** (decision recorded 2026-05-09; see [[wiki/syntheses/helm-commercialization-paths]] for the 3 shapes considered + re-evaluation trigger). Architecturally informed by the wiki's strongest multi-agent blueprints (CyrilXBT 5-agent / Khairallah three-session / Saraev DOE / NainsiDwiv tool-calling reliability).

# Helm

> Multi-agent platform that automates ROAM Labs' GTM + business operations across all owned products (Vedge / Kivora / Clarvyn) and client engagements. Single user (Godwin), [[wiki/entities/hermes-agent|Hermes Agent]] runtime, FastAPI orchestrator on Railway, Next.js supervision UI on Vercel, PostgreSQL + pgvector for shared knowledge layer. **6-week sequential build order** modeled directly on [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's 5-agent system]], with Lead Management as the Week 1 MVP for immediate revenue impact.

## What and why

ROAM Labs has 3 owned products, 2 client engagements, 1 government subcontract, and 1 corporate marketing site — 9 active projects competing for one human's attention. Engineering work is already heavily automated via Claude Code. **The bottleneck is now GTM + business operations**: lead identification, sales follow-through, marketing across 3 distinct product voices, invoicing/collections, vendor management, and cross-project visibility. Helm is the agent stack that closes that bottleneck.

**Why a single shared agent stack** (vs per-product): leads for Vedge (healthcare facilities), Kivora (compliance teams), and Clarvyn (startup founders) are different markets, but the *qualification logic*, *outreach mechanics*, and *pipeline structure* are the same. One Lead Management agent that knows about all 3 products can cross-sell ("this prospect is a 50-person clinic — pitch Vedge primary, mention Clarvyn for their HR pain"). Same for Marketing (one agent, three voice profiles), Sales, Operations, and PM.

**Why internal-only**: Godwin is the only user. No multi-tenant data scoping, no RBAC, no productization polish. Single JWT or session auth. Cuts ~30% of the build surface; saves ~6 weeks vs an extractable-product version. If Helm becomes commercial later, the architecture absorbs that — the [[wiki/projects/clarvyn|Clarvyn]] portal pattern (single-tenant-scope-able) is the upgrade path.

**Why Hermes Agent runtime** (vs reusing Clarvyn's FastAPI + Spring Boot agent service stack): Hermes ships built-in skills, persistent memory, deepening user model, multi-platform messaging gateway (Telegram + Discord + Slack + WhatsApp + Signal + Email + CLI), and 200+ model routing via OpenRouter. The trade is *ship-speed > stack-reuse-elegance*. For an internal tool where the goal is "Godwin gets time back," Hermes's built-in machinery beats hand-rolling another agent service.

## Current focus

> _Updated as Godwin progresses through the build order._

**2026-05-09 — Multi-repo scaffold materialized.** All three sub-repos exist at `/Users/kobbyopoku/ROAM/CascadeProjects/helm/`. Each has `.git` initialized but **no commits yet** — everything sits as untracked working-tree state awaiting first commits + remote creation:

- **`helm-backend/`** — FastAPI shell with Lead Management agent's HTTP routes (`/lead/qualify`, `/lead/outreach`), system prompt, `master-claude.md`, and `leads` schema (includes `tenant_id` per Layer 3 spec + 5-value `primary_product` ENUM). Hermes Agent invocation body raises `NotImplementedError` and is the active build target.
- **`helm-portal/`** — Next.js 16 + React 19 + Tailwind 4 supervision UI; Dashboard + Leads pages (read-only); `vercel.ts` config.
- **`helm-mcp/`** — placeholder `README.md` per MCP subdir (`stripe-mcp/`, `postiz-mcp/`, `accounting-mcp/`, `crm-mcp/`, `brain-wiki-mcp/`); empty until Weeks 2-5.

Wrapper has no `.git`. Each sub-repo has its own `BRAIN.md` (gitignored) plus a wrapper-level un-ignored `BRAIN.md`. Master system context lives at `helm-backend/master-claude.md`. Voice-profile stubs sit at `helm-backend/voice-profiles/` awaiting migration of full pattern docs from [[wiki/syntheses/helm-voice-profiles]].

**2026-05-09 — Local dev infrastructure (added intra-day after initial scaffold).**

- **Wrapper-root `docker-compose.yml`** — `pgvector/pgvector:pg16` for local Postgres; bind-mounts `helm-backend/db/schema.sql` as `/docker-entrypoint-initdb.d/` init script so `docker compose up -d` reproducibly stands up the schema. Local-dev parity with Railway-managed Postgres in production.
- **Wrapper-root `README.md`** — developer quickstart (compose up + per-repo `pip install -e ".[dev]"` / `pnpm install`).
- **`helm-backend/db/schema.sql`** committed — `leads` table with `tenant_id` (default `'roam-labs'`), 5-value `primary_product` CHECK, and 7-stage workflow CHECK (`new` → `qualified` → `outreach_drafted` → `outreach_sent` → `replied` → `handed_off` → `rejected`). Future tables added per Layer 3 spec as agents come online.
- **`helm-backend/railway.json`** — NIXPACKS builder, `uvicorn app.main:app` start command, `/health` healthcheck, `ON_FAILURE` restart with 10 retries.
- **`helm-backend/tests/test_health.py`** — pytest scaffold (one passing health-endpoint test); `[tool.pytest.ini_options] asyncio_mode = "auto"` configured.
- **Backend deps**: `alembic` (migrations), `structlog`, `pydantic-settings`, `sqlalchemy[asyncio]`, `asyncpg`, `httpx` pinned in `pyproject.toml`. Hermes Agent dep still placeholder pending pypi name resolution.

**Immediate execution blockers**:
1. ~~Hermes Agent pypi package name not yet pinned in `helm-backend/pyproject.toml` (TODO comment placeholder).~~ **Resolved 2026-05-10**: Hermes is not on pypi (verified upstream); pinned via git tag — `"hermes-agent @ git+https://github.com/NousResearch/hermes-agent.git@v0.13.0"`. Programmatic-embedding path (`from agent import AIAgent`) preserves the in-process FastAPI integration assumption. See updated [[wiki/entities/hermes-agent]] for distribution details + heavy-dep footprint caveat.
2. `ROAM-Labs/` GitHub org not created; sub-repos have no remotes (and no first commits yet).

## Repo topology — multi-repo wrapper

Helm follows the **multi-repo wrapper pattern** consistent with the rest of Godwin's portfolio (see [[wiki/projects/clarvyn|Clarvyn]] 5-repo / [[wiki/projects/kivora|Kivora]] 4-repo / [[wiki/projects/coffee-break-with-big-sis|Coffee Break]] 2-repo / [[wiki/projects/stacesprouts|StaceSprouts]] 2-repo / [[wiki/projects/brolly|Brolly]] multi-repo / [[wiki/projects/vedge|Vedge]] 7-repo). Outer wrapper is a regular directory (no `.git`); each service repo has its own remote.

### Proposed split (3 repos + wrapper)

```
~/ROAM/CascadeProjects/helm/         (wrapper — no .git)
├── BRAIN.md                          (pointer to ~/brain/wiki/projects/helm.md)
├── helm-backend/                     (FastAPI + Hermes Agent — Python on Railway)
│   ├── BRAIN.md
│   ├── api/                           (FastAPI routes per agent + auth)
│   ├── agents/                        (per-agent skill configs + system prompts)
│   ├── runtime/                       (Hermes Agent integration)
│   ├── scheduler/                     (APScheduler — 7AM briefing / 5PM wrap-up / monthly Analytics)
│   ├── db/                            (PostgreSQL + pgvector schema + migrations)
│   ├── voice-profiles/                (4 voice profiles loaded from wiki sync; per-product agent config)
│   └── master-claude.md               (master system context for all 6 agents)
├── helm-portal/                      (Next.js — TypeScript on Vercel)
│   ├── BRAIN.md
│   ├── app/                           (Next.js 16 App Router)
│   ├── components/                    (shadcn-style supervision UI primitives)
│   └── lib/                           (custom fetch ApiClient — Clarvyn portal pattern)
└── helm-mcp/                         (custom MCP servers — Python or TypeScript)
    ├── BRAIN.md
    ├── brain-wiki-mcp/                (read-only ~/brain/wiki/ access; Week 5 dependency for PM agent)
    ├── stripe-mcp/                    (Week 2 — Sales agent invoicing)
    ├── postiz-mcp/                    (Week 3 — Marketing agent publish layer)
    ├── accounting-mcp/                (Week 4 — Operations agent QuickBooks/Xero)
    └── crm-mcp/                       (Week 4 — wraps the self-hosted Postgres CRM after migration off Notion)
```

> **Note**: Weeks 1-3 use Notion-as-CRM via REST through Hermes (per Q4 resolution — no custom MCP). The `crm-mcp/` folder above is added in Week 4 when the data migrates to self-hosted Postgres-backed and benefits from a typed MCP wrapper.

### Why 3 repos (not 2 or 5)

| Split option | Trade-off | Decision |
|---|---|---|
| **2 repos** (backend + portal) | Simpler. Fold MCPs into backend. Matches Coffee Break / StaceSprouts shape. | ❌ MCP servers want independent versioning + deployability + reusability across other ROAM products (Vedge / Kivora / Clarvyn could reuse Helm's brain-wiki-mcp). |
| **3 repos** (backend + portal + mcp) ✅ | MCPs are first-class artifacts; backend stays focused on orchestration; portal stays front-end-pure. | ✅ **Chosen**. Aligns with the [[mcp-server]] concept page's *MCPs as durable contracts* discipline. |
| **5 repos** (separate agents + runtime + landing + ...) | Maximum isolation. Matches Clarvyn shape. | ❌ Overkill for a single-user internal tool. Helm doesn't need a landing page (no marketing surface). Hermes Agent is a dependency, not a built-by-us repo. |

### BRAIN.md drops in each sub-repo

Per [[wiki/projects/clarvyn|Clarvyn's]] 2026-05-09 multi-repo BRAIN.md convention: drop `BRAIN.md` in **each sub-repo** (helm-backend, helm-portal, helm-mcp) plus the wrapper. Each `BRAIN.md` identifies which service it sits in and points at the same `~/brain/wiki/projects/helm.md` page. Add `BRAIN.md` to each sub-repo's `.gitignore`. The wrapper's BRAIN.md is unignored (wrapper has no `.git`).

This convention exists because *an agent might open just `helm-backend/`* in a Cursor / Claude Code session and not see the wrapper-level BRAIN.md. Per-repo drops ensure the brain pointer is always one path-level away.

### GitHub org

All 3 repos sit under the new **`ROAM-Labs/`** GitHub org (per Q2 resolution 2026-05-09). Org to be created when Week 1 build starts. Naming convention: `ROAM-Labs/helm-<service>` for clarity within the org alongside other future ROAM-Labs/ repos.

### What each repo deploys to

- **`helm-backend`** → Railway (Python service + PostgreSQL with pgvector add-on + APScheduler in-process)
- **`helm-portal`** → Vercel (Next.js 16 App Router; auto-deploy from `main` branch)
- **`helm-mcp`** → Railway (each custom MCP runs as a small Python or Node process; orchestrated alongside `helm-backend`)

## Stack and infrastructure

### Layer 1 — Agent runtime: Hermes Agent
- Open-source, MIT-licensed, by [[wiki/entities/nous-research|Nous Research]] / [[wiki/entities/hermes-agent|Hermes Agent]] entity in the wiki.
- Self-improving learning loop creates skills from experience.
- Persistent memory (FTS5-indexed conversation search).
- 200+ model providers via [[wiki/entities/openrouter|OpenRouter]].
- Multi-platform messaging out-of-box (Helm uses CLI + email + Slack initially; Telegram for proactive notifications later).
- Open question: fork or use upstream? Default *upstream* — pick up improvements without merge cost.

### Layer 2 — Orchestrator: FastAPI on Railway
- Wraps Hermes Agent in HTTP for the frontend to consume.
- Routes requests to specific agents (Lead / Sales / Marketing / Ops / PM / Analytics).
- Holds the *master CLAUDE.md* (the system context governing all agents — see `master-claude-md.md` template below).
- Schedules cron-style triggers for the daily 7AM briefing + 5PM wrap-up (Khairallah pattern).

### Layer 3 — Database: PostgreSQL + pgvector on Railway
- **Shared knowledge layer** — every agent can read/write here.
- Tables: `leads`, `deals`, `customers`, `invoices`, `expenses`, `content_drafts`, `voice_profiles`, `project_status`, `agent_logs`, `agent_optimizations`.
- **Cross-cutting columns on every business-data row**: `tenant_id` (per multi-tenant pivot insurance — see [[wiki/syntheses/helm-commercialization-paths]]) + `primary_product` ENUM (`vedge` / `kivora` / `clarvyn` / `roam-labs` / `client-work` — mitigates the cross-product context-bleed risk; agent leads with primary, mentions secondary only if signals support).
- pgvector for: voice-profile embeddings (per product), lead-similarity matching, content-archive semantic search, product-knowledge RAG.
- Same database choice as [[wiki/projects/kivora|Kivora]] and [[wiki/projects/clarvyn|Clarvyn]] — Godwin's signature for vector data.

### Layer 4 — Frontend: Next.js on Vercel
- Single-user supervision UI. No multi-tenant complexity.
- Pages:
  - **Dashboard** — agent status, today's pipeline, alerts, decisions-needed inbox.
  - **Leads** — pipeline by stage, signal-score sorted, per-row drill-into.
  - **Deals** — sales-stage Kanban, close-rate analytics.
  - **Marketing** — content-object run folders (Shann Holmberg pattern), voice-profile editor per product.
  - **Operations** — invoices/expenses/vendors/hiring-pipeline; weekly business reports.
  - **Projects** — 9-row table reading from BRAIN.md drops in each project repo.
  - **Agents** — per-agent system-prompt editor, system-prompt change history, monthly Analytics-agent recommendations.
  - **Logs** — agent execution logs, errors, costs.

### Layer 5 — Specialized agents (6 total: 5 inline-chained + 1 meta-orchestrator)

Six agents, scoped to GTM + business ops only (engineering is out of scope per Q1):

| # | Agent | Job | Wiki blueprint |
|---|---|---|---|
| 1 | **Lead Management** *(Week 1 MVP)* | Prospect identification (Google Maps + LinkedIn signals), qualification scoring, outreach drafting, follow-up sequencing | [[wiki/sources/exploraX_-google-maps-leadgen]] |
| 2 | **Sales** *(Week 2)* | Pipeline management, deal-stage tracking, proposal drafting, close-rate analytics, contract follow-through | [[wiki/sources/ig_claims-x-meta-retargeting]] (Conviction Gap Model for proposal copy) |
| 3 | **Marketing** *(Week 3)* | Content production across 3 product voices, social posting, AI-SEO optimization | [[wiki/sources/shannholmberg-content-os]] + [[wiki/sources/bloggersarvesh-20-seo-prompts]] |
| 4 | **Operations** *(Week 4)* | Invoicing, collections, expense tracking, hiring pipeline, vendor management, weekly reports | [[wiki/sources/cyrilxbt-x-2052570518667378918]] (Operations Agent prompt) |
| 5 | **Project Management** *(Week 5)* | Cross-project visibility (9 active), milestone tracking, status reports, risk flags | reads BRAIN.md drops; pulls from this wiki via brain-MCP |
| 6 | **Analytics** *(Week 6 — meta-orchestrator)* | Identifies performance patterns across the other 5, generates monthly system-prompt updates for each | [[wiki/concepts/self-annealing]] codified |

**The Analytics agent is the most architecturally important one** — it rewrites the system prompts of the other 5 agents based on monthly performance data. CyrilXBT's pattern. Without it, Helm runs the same way in week 52 as in week 6; with it, every agent gets monthly optimization for the compound effect.

## Reference architecture (pulled from the wiki)

### Master CLAUDE.md template (governs all 6 agents)

Per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's]] verbatim master template, adapted to ROAM Labs:

```
# Master System Context

## Business Overview
ROAM Labs is an AI products + services company founded by Godwin Opoku Duah.
Three commercial products (Vedge / Kivora / Clarvyn), two client engagements
(Coffee Break / StaceSprouts), one government subcontract (CPC RTBVD via SoftTech).
See ~/brain/wiki/entities/roam-labs.md for canonical reference.

## Agent Roster
- Lead Management: prospect identification + qualification + outreach drafting
- Sales: pipeline management + deal tracking + proposal drafting
- Marketing: content production + social posting + AI-SEO across 3 product voices
- Operations: invoicing + collections + expenses + reports + vendor mgmt
- Project Management: cross-project visibility + milestones + risk flags
- Analytics: monthly performance review + system-prompt rewrites for the other 5

## Shared Standards
- Reasoning vs execution: agents reason; tools execute. (See reasoning-execution-split.)
- Cite or omit: every claim links to a verifiable source.
- Cost discipline: Sonnet 80%, Opus for complex reasoning, Haiku for simple tasks.
- Output format: structured (no rambling prose; lists/tables/JSON where appropriate).

## Current Focus
[Updated weekly by Godwin: e.g. "Week of 2026-05-09: Q3 lead generation push;
CPC award decision pending; Clarvyn Wave 7 prep."]

## Hard Rules That Apply to All Agents
- NEVER promise anything Godwin hasn't authorized.
- NEVER reference competitors by name in client-facing copy.
- NEVER discuss Helm's existence externally — it is internal infrastructure.
- When uncertain about scope or pricing: ESCALATE to Godwin via the supervision UI.
- All scheduled communications go through "review mode" for 14 days before automated send.
```

### Daily scheduling (Khairallah three-session pattern)

| Time | Trigger | Agent | Output |
|---|---|---|---|
| 7AM | Cron | Lead Management + Operations | Morning briefing markdown file: pipeline stage summary, urgent decisions, top 3 priorities |
| Manual (1-3pm) | Godwin | Whichever | Production block — bulk drafts, pipeline updates, content production |
| 5PM | Cron | All 5 inline-chained (Lead Mgmt + Sales + Marketing + Ops + PM) | End-of-day wrap-up + carry-forward into tomorrow's briefing |
| 1st of month | Cron | Analytics | Monthly performance review + system-prompt change recommendations for the other 5 |

### Tool-calling reliability rubric (NainsiDwiv 7-step)

Every MCP integration must satisfy:

1. **Protocol** — MCP wire format. ⚠️ *Hermes Agent's native MCP support is unverified in the wiki; the [[wiki/entities/hermes-agent]] entity page lists OpenRouter routing + multi-platform messaging gateway but doesn't confirm MCP-protocol support specifically. **Verify against the upstream Hermes repo before Week 1**; if Hermes lacks native MCP, add an MCP-to-Hermes adapter layer (~3-5 days of additional work).*
2. **Tool definitions as contracts** — name + description + arg schema as durable interfaces
3. **Error handling** — every tool failure surfaced to the agent for recovery
4. **Parallelization** — explicit conflict-free vs serial-required tool annotations
5. **Catalog size** — trim aggressively; per [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax]] each MCP server costs 600-18,000 tokens per turn
6. **Security** — auth scope minimization, credential isolation per agent
7. **Evaluation** — tool-call success rates, latency, cost tracked per call in `agent_logs`

### MCP catalog (initial + planned)

**Built-in (Hermes ships these)**: web search, file ops, calendar, email.

**Custom MCPs to build** (in build-order priority):
- **Stripe MCP** — invoicing, subscriptions, payment status (Week 2 for Sales agent)
- **Google Workspace MCP** — Gmail + Calendar + Drive (Week 1; Hermes built-in may suffice)
- **GitHub MCP** — read PR status, issue counts, deploy status (Week 5 for PM agent)
- **Brain-wiki MCP** — read this brain (`~/brain/wiki/`); query syntheses + project pages (Week 5 for PM agent)
- **Postiz MCP** — social-media scheduling (Week 3 for Marketing; from [[wiki/entities/postiz|Postiz]])
- **Accounting MCP** — QuickBooks or Xero (Week 4 for Operations agent)
- **Slack MCP** — internal notifications (Week 4)
- **CRM MCP** — Week 4 only. Weeks 1-3 use Notion-as-CRM via REST through Hermes (per Q4 resolution; no MCP needed). Build the typed CRM MCP when the data migrates to self-hosted Postgres-backed in Week 4.

## Build order (6 weeks)

Per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT's]] sequential pattern:

### Week 1 — Lead Management Agent (MVP)
- Hermes Agent runtime stood up on Railway.
- FastAPI shell with one endpoint: `/lead/qualify` and `/lead/outreach`.
- Next.js Vercel shell: Dashboard page + Leads page (read-only initially).
- Postgres schema: `leads` table with signal scoring fields.
- **Direct application of [[wiki/sources/exploraX_-google-maps-leadgen|m0h's playbook]]**: 4 prospect signals + Instant Data Scraper output → Hermes filters and writes outreach.
- **Goal**: end of Week 1, Helm produces a daily list of 20 qualified prospects with personalized outreach drafts. Godwin manually approves before send.

### Week 2 — Sales Agent
- `deals` schema with stage Kanban.
- Stripe MCP integration (basic invoicing on close).
- Conviction Gap Model proposal copy (per [[wiki/sources/ig_claims-x-meta-retargeting]]).
- **Goal**: end of Week 2, Lead → Sales handoff is automated.

### Week 3 — Marketing Agent
- `voice_profiles` table (one per product: Vedge / Kivora / Clarvyn / ROAM Labs corp).
- Voice-profile extraction methodology: feed Hermes 20 best pieces per product, extract patterns, store as voice profile (per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT]] + [[wiki/sources/shannholmberg-content-os|Shann]] convergence).
- Postiz MCP integration for cross-channel posting.
- AI-SEO prompts adapted from [[wiki/sources/bloggersarvesh-20-seo-prompts]].
- Master avoid-slop document loaded per agent (per [[wiki/concepts/anti-ai-slop-machinery]]).
- **Goal**: end of Week 3, Helm produces a week's worth of content across 3 product voices, queued in Postiz, awaiting Godwin's review pass.

### Week 4 — Operations Agent
- Accounting MCP (QuickBooks or Xero).
- Stripe + accounting reconciliation.
- 7AM Morning Briefing + 5PM End-of-Day Wrap-up cron jobs (Khairallah pattern).
- 4-tier email urgency triage (per Khairallah).
- **Goal**: end of Week 4, Godwin's morning starts with a one-page briefing in his Inbox + Slack DM.

### Week 5 — Project Management Agent
- Brain-wiki MCP (read-only access to `~/brain/wiki/`).
- GitHub MCP (PR + commit + deploy status across 9 active projects).
- BRAIN.md drop integration — agent reads `~/Projects/*/BRAIN.md`, follows pointer to brain page.
- **Goal**: end of Week 5, the Projects page in Helm shows live status across Vedge / Kivora / Clarvyn / Brolly / CBwBS / StaceSprouts / Asanti / CPC RTBVD / _roamlabs.

### Week 6 — Analytics Agent (meta-orchestrator)
- Monthly cron job that reads `agent_logs` for the previous 30 days.
- Identifies patterns: which Lead-Mgmt prompts produced highest-converting outreach? Which Marketing voice-profile elements correlate with engagement?
- Generates `agent_optimizations` records: specific system-prompt diffs to apply to the other 5.
- **Critical safety constraint**: Analytics agent's prompt rewrites do NOT auto-apply. Godwin reviews and approves each one in the Helm UI. (Per [[wiki/sources/cyrilxbt-x-2052570518667378918|CyrilXBT]]'s constraint engineering — Communication agent ran in review mode for 2 weeks before auto-send; Analytics agent stays review-mode permanently for system-prompt changes.)
- **Goal**: end of Week 6, Helm has a closed-loop self-annealing mechanism with human-approval gates.

## Definition of done for v1

Helm is **shipped** when *all five* are true:

1. **All 6 agents are running in production** — Lead Mgmt + Sales + Marketing + Ops + PM + Analytics. Each has its own system prompt + per-agent MCP scope + budget cap.
2. **30 consecutive days** of the daily 7AM Morning Briefing + 5PM End-of-Day Wrap-up scheduled jobs running without manual intervention. Carry-forward state passes correctly between days.
3. **Lead Management agent has produced at least 100 qualified-prospect outputs** that Godwin manually approved and either called or emailed. Real outreach, not test data.
4. **Analytics agent has run at least 1 monthly review cycle** end-to-end and proposed system-prompt changes for at least 2 of the other 5 agents (Godwin reviews and approves; doesn't need to accept).
5. **Cost discipline holds**: 30-day rolling LLM spend ≤ $300/mo target.

When all 5 are true, file an `update-project` log entry marking `status: shipped-v1` (new frontmatter value) and date the milestone. Then run the [[wiki/syntheses/helm-commercialization-paths|commercialization re-evaluation]] check after another 60-90 days of production.

## Operations

### Secret management

API credentials (Anthropic, OpenRouter, Stripe, Postiz, Notion, GitHub, accounting MCP) live in **Railway environment variables** scoped per-service:

- `helm-backend` → `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `DATABASE_URL`, `REDIS_URL`
- `helm-mcp` → per-MCP credentials scoped to the specific MCP server that needs them (e.g. `STRIPE_SECRET_KEY` only on stripe-mcp)
- `helm-portal` → only public env vars (`NEXT_PUBLIC_API_URL`); no secrets in the Vercel build

**Local dev**: `.env.local` per repo (gitignored). Pull from a single Bitwarden / 1Password vault as the source of truth; never commit. Match Clarvyn's pattern (per [[wiki/projects/clarvyn]] practice).

### PostgreSQL backups

Railway runs daily automated backups for managed PostgreSQL (7-day retention on the basic plan). For Helm v1 single-user scope this is sufficient. Recovery procedure: Railway dashboard → database → restore-from-snapshot. Not yet exercised; Week 1 should include one rehearsal restore against a staging branch to verify the procedure works.

### Observability

- **`agent_logs` table** captures per-call: agent name, model, input-tokens, output-tokens, duration, success/error, cost in USD. Mnilax + zodchii overhead-pattern discipline.
- **Per-agent error rate** target: <5% per call (~95% per-call success matches the [[wiki/concepts/reliability-decay-math|reliability-decay-math]] inline assumption).
- **Cost dashboard** in `helm-portal` Logs page: 30-day rolling LLM spend per agent + spike alerts.
- **Cron job health**: APScheduler logs success/failure per scheduled run; missed-run alert fires after 2 consecutive misses.

Production-grade observability (Prometheus / Grafana / OpenTelemetry traces) is **out of scope for v1**; revisit when Helm crosses 3+ users or 1000+ agent calls/day.

## Cost discipline (from day 1)

Per [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax]] + [[wiki/sources/zodchiii-x-claude-code-settings|zodchii]]:

- **Master CLAUDE.md cap**: ~1,500 tokens combined. (Helm's master + per-agent specifics ≤ 1,500 each.)
- **MCP catalog discipline**: only connect MCPs an agent actively uses. Lead Management agent doesn't load Stripe MCP; Marketing agent doesn't load GitHub MCP.
- **Model routing**: Sonnet for 80%, Opus for Analytics agent's monthly review only, Haiku for simple categorizations and the morning-briefing email triage.
- **Budget caps per agent run**: `--max-budget-usd` style caps to prevent runaway loops in scheduled jobs.
- **Hermes Agent's OpenRouter integration** lets us experiment with cheaper providers (Claude Haiku 3.5, GPT-4o-mini, DeepSeek) for non-critical agent tasks.

**Target operating cost**: <$300/mo total Claude/OpenRouter spend. Comparison anchor (per [[wiki/sources/cyrilxbt-x-2052570518667378918]]): CyrilXBT's equivalent 5-agent system reports **~$89 hosting + $700-900 API spend = $800-1,000/mo total** at production volume, *or* ~$105/mo at minimum config (Claude Max + N8N self-hosted + free Supabase + free Obsidian). Helm targets the API-spend portion specifically and should land lower than CyrilXBT's because single-user volume is lower than a content business's daily output.

## Architecture decisions

| # | Decision | Rationale | Source |
|---|---|---|---|
| 1 | Hermes Agent as runtime | Built-in skills + memory + 200-provider routing > hand-rolling | Q4 (c) per [[wiki/entities/hermes-agent]] |
| 2 | FastAPI orchestrator (not Spring Boot) | Hermes is Python; same-language saves 1-2 weeks | Q4 (c) consequence |
| 3 | PostgreSQL + pgvector (single DB) | Reuse from Kivora/Clarvyn; vector layer for voice profiles + lead similarity | [[wiki/entities/godwin-opoku-duah]] signature stack |
| 4 | Next.js + Vercel frontend | User stated; matches _roamlabs and Asanti patterns | Q-prerequisite |
| 5 | Single shared agent stack across all products | Cross-sell context compounds; simpler than per-product stacks | Q2 (a) |
| 6 | Lead Management as Week 1 MVP | Immediate revenue impact; m0h playbook documents *"whole flow runs in ~2 hours"* (filter + cold-call top 20 + email-fallback the rest) per [[wiki/sources/exploraX_-google-maps-leadgen]]. Working agent achievable in Week 1 with that as the operating-time target. | Q3 (c) |
| 7 | 6-week sequential build (one agent per week) | CyrilXBT's documented order; debugging in isolation; learning failure modes one at a time | [[wiki/sources/cyrilxbt-x-2052570518667378918]] |
| 8 | Analytics agent system-prompt rewrites stay in review mode permanently | Auto-applying agent prompts to other agents is unsafe; manual approval gate is the safety boundary | Constraint engineering from CyrilXBT's Communication-agent precedent |
| 9 | Single-user JWT auth, no RBAC, no multi-tenant scoping | Q5 + Q6 → cut polish | Q5, Q6 (a) |
| 10 | **Tailwind 4 CSS-first config (helm-portal)** — no `tailwind.config.ts`; theme tokens declared in `app/globals.css` via `@theme` | Tailwind 4 default; theme lives next to the CSS that uses it; one fewer config file | Scaffold 2026-05-09 |
| 11 | **`vercel.ts` over `vercel.json` (helm-portal)** | Vercel 2026 platform default; full TypeScript with `@vercel/config`, IntelliSense, env access in config | Scaffold 2026-05-09 |
| 12 | **docker-compose at wrapper for local Postgres + pgvector** | Local-dev parity with Railway-managed Postgres; bind-mounting `helm-backend/db/schema.sql` as init script makes `docker compose up -d` reproducibly stand up the schema; faster iteration than tunneling to Railway during development | Scaffold 2026-05-09 (intra-day) |

## Resolved decisions (2026-05-09)

Six of the seven open questions resolved per Godwin's "proceed" with recommended defaults. Recorded here so future read-mode sessions don't re-ask:

| # | Question | Resolution |
|---|---|---|
| 1 | **Working name** | ✅ **Helm** (confirmed 2026-05-09). |
| 2 | **Repo location** | ✅ **New `ROAM-Labs/` GitHub org**. Cleaner separation from personal repos and from Brolly-Africa. Org to be created when Godwin starts Week 1 build. |
| 3 | **Hermes Agent fork vs upstream** | ✅ **Upstream**. Pick up improvements without merge cost. Fork only if a specific feature is missing. |
| 4 | **CRM choice for Week 1** | ✅ **Notion-as-CRM** for Weeks 1-3. Cheap, fast to set up, no MCP needed (Hermes can hit Notion via REST). Migrate to self-hosted Postgres-backed by Week 4 once schema stabilizes. |
| 6 | **Brain-wiki MCP build effort** | ✅ **1-day read-only file-system MCP** serving `~/brain/wiki/`. Build the simple version Week 5; upgrade to pgvector-indexed semantic search later if/when query latency becomes a felt cost. |
| 7 | **Notification channels** | ✅ **Email-first** for the 7AM Morning Briefing + 5PM End-of-Day Wrap-up. **Slack DM** for high-priority alerts (Week 4 enhancement). Telegram deferred. |
| 8 | **Scheduled-task runtime** | ✅ **APScheduler in-process** (matches [[wiki/projects/clarvyn|Clarvyn]]'s pattern). Upgrade to Railway cron if reliability concerns surface in production. |

## Resolved decisions (additional, 2026-05-09)

- **Q5 Voice profiles**: ✅ **Starter drafts complete** at [[wiki/syntheses/helm-voice-profiles]]. Four profiles extracted from existing landing-site copy via [[wiki/sources/shannholmberg-content-os|Shann's brand-foundation-extraction methodology]]: **Vedge** (high confidence — distinctive editorial voice), **Kivora / ROAM GRC** (high — consistent B2B SaaS voice), **Clarvyn** (medium — Startup landing extracted; Enterprise landing different voice not yet extracted), **ROAM Labs corp** (low — voice currently unsettled per [[wiki/projects/roamlabs]]; flagged as draft-only, do not auto-send corporate content until brand stabilizes). Refine when curated samples available; migrate from `wiki/syntheses/` to `helm-repo/voice-profiles/` when Helm repo exists.

- **Strategic shape (commercialization)**: ✅ **Internal-only for v1**. The "agent marketplace" shape (multi-tenant productized SaaS) was considered and **explicitly deferred**. Re-evaluate after 3-5 paying customers operating real volumes through Helm via the services-as-software path. Full decision record + 3 shapes considered + wiki evidence + re-evaluation trigger documented at [[wiki/syntheses/helm-commercialization-paths]]. **One architectural carry-over**: data model includes `tenant_id` columns from day 1 (UI doesn't surface them) — costs ~10% upfront, saves ~6 months later if multi-tenant pivot happens.

## Open questions

*(All resolved as of 2026-05-09. Project is in build-ready state.)*

## Lessons learned

*(none yet — project is at the brief-and-design stage)*

## Risks

- **Hermes Agent maturity**: 23k+ stars but a relatively new project. If a critical bug surfaces, Godwin may need to fork and patch — adding maintenance burden.
- **Analytics agent prompt-rewrite quality**: bad rewrites could degrade the other 5 agents. Mitigation: review-mode permanent + system-prompt change history with rollback.
- **Single-user assumption**: if Godwin hires a team, Helm's no-RBAC architecture becomes a refactor liability. Mitigation: data model carries `tenant_id` from day 1 (per the multi-tenant pivot insurance in [[wiki/syntheses/helm-commercialization-paths]]); a `user_id` column on per-tenant write rows is implied by the same scoping. UI surfaces neither in v1.
- **Cross-product context bleed**: a Lead Management agent that pitches Vedge to a clinic might also accidentally cross-sell Clarvyn (HR for clinic owners?) — could be feature, could be confusion. Mitigation: `primary_product` ENUM column on every business-data row (see Layer 3 schema); agent system prompts explicitly include *"lead with `primary_product`; mention secondary products only if signals strongly support"*.
- **Hermes Agent's self-improving loop**: it creates skills from experience. Without supervision, it might create skills that don't match Godwin's preferences. Mitigation: skill-creation review queue in Helm UI.

## Composition with the brain

Helm is the **most direct application of the wiki's 2026-05 ingest cluster** — every major source from the last week feeds into one of its 6 specialized agents (5 inline-chained + 1 meta-orchestrator):

- [[wiki/sources/exploraX_-google-maps-leadgen]] → Lead Management agent
- [[wiki/sources/ig_claims-x-meta-retargeting]] → Sales agent's Conviction Gap proposals
- [[wiki/sources/shannholmberg-content-os]] + [[wiki/sources/bloggersarvesh-20-seo-prompts]] → Marketing agent
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] → master CLAUDE.md template + Operations agent + Analytics agent
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] → daily scheduling pattern (7AM / midday / 5PM)
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] → MCP integration discipline
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] + [[wiki/sources/zodchiii-x-claude-code-settings]] → cost discipline
- [[wiki/sources/Shruti_0810-self-improving-obsidian]] + [[wiki/sources/llm-wiki-pattern-karpathy]] → Brain-wiki MCP for the PM agent

**The brain is finally being consumed by an agent stack that was designed against it.**

## Related projects

- [[wiki/projects/clarvyn]] — same Hermes-style agent design at startup-HR scope; the architectural sibling.
- [[wiki/projects/vedge]] — `vedge_agent` repo is currently scaffolding-only; Helm's Hermes-runtime pattern is a candidate for adoption there.
- [[wiki/projects/kivora]] — Spring Boot + FastAPI Claude variant of the same idea; Helm chose Hermes instead.

## Related concepts

- [[multi-agent-orchestration]] — primary concept this project instantiates.
- [[reasoning-execution-split]] — architectural foundation.
- [[doe-framework]] — every agent is a DOE cycle.
- [[self-annealing]] — Analytics agent codifies the pattern.
- [[hot-cache]] — daily morning briefing pattern.
- [[scheduled-automation]] — 7AM / 5PM cron triggers.
- [[markdown-as-agent-contract]] — master CLAUDE.md + per-agent SKILL.md.
- [[mcp-server]] — 7-step reliability rubric applied per integration.
- [[anti-ai-slop-machinery]] — Marketing agent loads master avoid-slop document.
- [[claude-code-overhead-patterns]] — cost discipline from day 1.
- [[reliability-decay-math]] — **5 inline-chained agents × 95% per-step = 77% end-to-end** (`0.95^5 ≈ 0.774`). Analytics is meta — runs monthly on logs, not in the inline pipeline, so it doesn't compound the chained-failure probability. Motivates aggressive error handling + reasoning-execution split for the inline 5.

## Related entities

- [[wiki/entities/godwin-opoku-duah]] — sole user; primary identity.
- [[wiki/entities/roam-labs]] — owner; Helm automates ROAM Labs operations.
- [[wiki/entities/hermes-agent]] — runtime.
- [[wiki/entities/nous-research]] — Hermes Agent maintainer.
- [[wiki/entities/openrouter]] — multi-provider LLM routing.
- [[wiki/entities/anthropic]] — Claude (primary model).
- [[wiki/entities/postiz]] — social publish layer (Marketing agent).
