---
type: project
title: Clarvyn
created: 2026-05-09
updated: 2026-05-09
status: active
repo: multi-repo (github.com/clarvyn/backend, clarvyn/workspace [portal], clarvyn/landing, clarvyn/app; agent at git@clarvyn:clarvyn/agent.git; outer wrapper has no remote)
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/clarvyn
stack: [java-21, spring-boot-3.3.5, python-3.11, fastapi, anthropic-claude, pgvector, postgres, react-19, vite-rolldown, typescript, tailwind, react-native, expo-54, zustand, tanstack-query, liquibase, docker-compose, prometheus, grafana]
started: 2026-01-15
owner_org: roam-labs
affiliation: roam-labs-product
aliases: [clarvyn-platform, clarvyn-hr]
tags: [project, hr, hris, ai-agent, agentic, multi-tenant, saas, startups, claude]
---

> **Lineage**: owned product of [[wiki/entities/roam-labs|ROAM Labs]] ([[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]], founder). Commercial / IP-bearing — sister architecture to [[wiki/projects/kivora|Kivora]] (same Spring Boot + FastAPI Claude + pgvector RAG stack, different domain).

# Clarvyn

> AI-first HR platform for startup founders — the agent *is* the HR department, autonomously running payroll, reviews, hiring, onboarding, and 1:1 employee check-ins across a Spring Boot HRIS, a FastAPI Claude agent, a React portal, and a React Native mobile app.

## What and why

Clarvyn replaces "HR software for HR people" with "an HR department that happens to be software." Founders of 5–50-person startups sign up, connect their tools (Slack, Jira, calendar, payroll), and the Claude-powered agent runs HR — proactively, not reactively. The HRIS (Spring Boot + Postgres) is the data backbone; the agent (FastAPI + Claude Sonnet + pgvector RAG) is the primary interface. Founders use the portal for oversight; employees use the mobile app to talk to "HR" (the agent). The agent serves both audiences with role-aware system prompts: founder mode (full access, write actions) and employee mode (own data, policies, requests, anonymous complaints). Success is "the founder gets updates, not tasks."

## Stack and infrastructure

- **Backend API (`backend/`)**: Spring Boot 3.3.5 / Java 21 / Maven. PostgreSQL + pgvector. Liquibase (40+ changesets). JWT (HS512, 24h) + BCrypt + 5-role RBAC (PLATFORM_OWNER → WORKSPACE_OWNER → MANAGER → HR_STAFF → EMPLOYEE) with 38 permissions. Multi-tenant via `companyId` scoping on every query. Standardized `BaseResponse<T>` envelope and `BaseEntity` audit base. Port 8089, package `com.clarvyn.platform`. Repo: `github.com/clarvyn/backend`.
- **AI Microservice (`agent/`)**: FastAPI / Python 3.11. Anthropic Claude API: Sonnet (`claude-sonnet-4`) for agent reasoning, Haiku (`claude-haiku-4`) for titles + memory compaction. Agentic loop pattern: `core.py` + `soul.py` + `memory.py` + `tools.py` + `tool_executor.py` (15 tools — 10 HR data, 4 AI/ML, 1 RAG). SSE streaming → Java WebClient Flux → React `ReadableStream`. Memory: conversation persistence + Haiku compaction at 50+ messages. RAG: chunk (500 tokens, 50 overlap) → `sentence-transformers/all-MiniLM-L6-v2` (384-dim) → pgvector. APScheduler `CronTrigger` for proactive briefings. MCP server + client added in Wave 6E for per-company external tool integrations. Port 8090. Repo: `git@clarvyn:clarvyn/agent.git`.
- **HR Portal (`portal/`)**: React 19 + TypeScript + Vite (Rolldown). Custom `ApiClient` (native `fetch`). React Context for state (Auth, Theme, FontSize). Vitest + MSW (39 tests). Port 5175. Repo: `github.com/clarvyn/workspace`.
- **Landing Page (`landing/`)**: React 19 + TypeScript + Vite. Port 5174. Repo: `github.com/clarvyn/landing`.
- **Mobile App (`app/`)**: React Native 0.73 + Expo 54. Zustand + TanStack Query v5. Axios with auto-refresh interceptor. Expo Push Notifications wired in Wave 6B. Repo: `github.com/clarvyn/app`.
- **Database**: `ankane/pgvector:latest` on host port 5433. Four agent-specific tables (`conversations`, `conversation_messages`, `document_chunks`, `scheduled_tasks`) on top of the HRIS schema.
- **Infra**: Docker Compose (`docker-compose.yml` + `docker-compose.monitoring.yml`), `clarvyn-network` (172.25.0.0/16), `start.sh` / `stop.sh`. GitHub Actions CI/CD. Prometheus + Grafana monitoring stack.
- **Outer wrapper**: `/Users/kobbyopoku/ROAM/CascadeProjects/clarvyn` is *not* a git repo — it's a working directory holding the five service repos. Same topology as [[wiki/projects/stacesprouts|StaceSprouts]] and [[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]].
- **Brain pointer drops**: this multi-repo project carries `BRAIN.md` in **six** locations — the wrapper plus each of the five service repos (`backend/`, `agent/`, `portal/`, `landing/`, `app/`) — so any agent session opened in any service finds the brain page immediately. `BRAIN.md` is in each service's `.gitignore` (lines 6 / 80 / 27 / 27 / 28 respectively as of 2026-05-09); the wrapper's `.gitignore` ignores it as well (no-op for git since the wrapper isn't a repo, but respected by ripgrep/find). All six pointer files reference the same brain page.

## Current focus

Week of 2026-05-09:

- **Wave 6 just landed** — proactive agent conversations + Expo Push Notifications, Slack bot (Events API + HMAC verification, DM ↔ agent flow), Integrations UI (Slack/Jira/GCal/Teams/Discord cards), MCP integration layer (per-company external tool servers via `agent/app/mcp/`), Jira + Google Calendar webhook receivers, `McpConnection` per-tenant registry, `PushToken` entity + `/api/push-tokens` endpoint.
- **Wave 5 shipped just before** — mobile agent chat (SSE streaming + FAB + conversation CRUD), role-aware agent (founder vs employee personas, tool filtering at executor layer), agent write tools (13 write tools via `hr_action_service` + privileged `InternalAgentController`), anonymous feedback (sentiment + classification + threshold-based founder alerts).
- **Open vision gaps surfaced in MEMORY.md**: real 2-way payroll integrations (Gusto / Deel), portal Activities + Insights tabs partly mocked still, deeper role-aware soul tuning, Google Calendar two-way sync, anonymous feedback configurability.

## Architecture decisions

- **Pre-2026-01-15 (initial scaffold)** — **Five services, one product**. Backend (HRIS) + Agent (FastAPI) + Portal (founder oversight) + Landing + Mobile (employee-facing). Each is a separate git repo; the wrapper has no remote. Rationale: independent deploy cadence per surface; portal and mobile are different audiences and need different release rhythms.
- **Pre-2026-01-15** — **Single backend package `com.clarvyn.platform`** with `BaseResponse<T>` envelope and `BaseEntity` audit base. Liquibase as schema authority. **Multi-tenant by `companyId` column scoping** (not schema-per-tenant — diverges from sibling [[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]] which uses schema-per-tenant). Rationale: simpler operational model, single connection pool, easier cross-company analytics for the platform owner.
- **Pre-2026-03 (initial agent build)** — **Agent loop is SOUL + Tools + Memory** (`core.py` + `soul.py` + `memory.py` + `tools.py`). Worked example of [[wiki/concepts/agentic-loop]]. [[wiki/concepts/reasoning-execution-split]] applied: Sonnet drives the loop, Haiku handles titles + memory compaction at the 50-message threshold.
- **Pre-2026-03** — **RAG is in-process pgvector**, not a separate vector DB. Embed with `sentence-transformers/all-MiniLM-L6-v2` (384-dim). Rationale: one less moving piece in Compose; pgvector is "good enough" until the corpus grows past Postgres single-node comfort.
- **2026-03 (Wave 5C — Agent Evolution)** — **Agent gets write access**. Until Wave 5C, every agent tool was read-only; Wave 5C added 13 write tools through `hr_action_service` + a privileged `InternalAgentController`. Rationale: the product thesis (agent-as-HR-department) requires actions, not just answers — approve leave, process payroll, create reviews, file complaints.
- **2026-03 (Wave 5B)** — **Role-aware agent personas**. Three system prompts (founder / manager / employee) + per-role tool filtering at the `tool_executor` layer. Rationale: same agent must safely serve a CEO and an employee from the same codebase without cross-tenant or cross-role data leakage.
- **2026-03 (Wave 5D)** — **Anonymous feedback mode**. Complaints stored without `user_id`, only category + sentiment kept; pattern-detection alerts fired to founder when threshold tripped. Rationale: psychological safety as a first-class product feature, not an afterthought.
- **2026-04/05 (Wave 6E)** — **MCP server + client layer for per-company external integrations**. `agent/app/mcp/server.py` exposes Clarvyn's HR tools as an MCP server; `agent/app/mcp/client.py` consumes external MCP tool servers; `McpConnection` model registers per-tenant connections; `tool_executor` routes external MCP calls. Rationale: avoid bespoke per-integration glue code as the integration surface grows (Slack/Jira/GCal/Gusto/Deel/job boards). Direct integrations stay where vendors don't speak MCP yet.
- **March 2026** — **`agentJ` retired**. Earlier Java-based agent prototype removed; the Python `agent/` is the single agent codebase.

## Open questions

- **Real 2-way payroll integrations** — Gusto / Deel are named in the vision but not built. Build order vs which integration is the wedge?
- **Google Calendar two-way sync** — webhook receiver landed in 6C; full bidirectional sync (creating events from agent decisions) still open.
- **Portal Activities + Insights tabs** — partially backed by real scheduled-task data after 6A, but Insights still has mock segments. Worth finishing or pivoting?
- **Outer wrapper remote** — should `clarvyn/` itself have a private GitHub remote for cross-cutting commits, or stay local-only? Same question as [[wiki/projects/stacesprouts|StaceSprouts]].
- **MCP credential rotation per tenant** — per-company MCP credentials stored where, rotated how, with what audit trail?
- **Mobile push delivery reliability** — Expo Push works for dev; need a fallback for users who disable Expo notifications or are on dev clients without `projectId` set.
- **Anonymous feedback pattern-alert thresholds** — currently fixed; should they be per-company configurable, and how is the founder educated about what triggers an alert?
- **Performance review conducted-via-chat UX** — mobile chat is the surface, but the "conducting a review through conversation" pattern hasn't been studied for completion rate vs a structured form fallback.

## Lessons learned

Project-specific; promote to `wiki/concepts/` when patterns generalize.

- **Read-only agents disappoint.** Wave 5C was a step-change in product perception once the agent could *do* (approve leave, file a review) instead of only *answer*. Agentic products plateau at low value until they get write access; a read-only agent is a chatbot wearing an agent costume. *Candidate for promotion to a concept page if it recurs in [[wiki/projects/kivora|Kivora]] or future agent projects.*
- **Role-aware system prompts are not just a prompt change.** They require parallel changes in the tool-executor's allow-list and the tool-call response shape (an employee asking "show me everyone's salary" should get a polite refusal *from a tool*, not a model-level evasion that can be jailbroken). Defense-in-depth: prompt + tool gate + data-layer scope.
- **Reasoning-execution-split (Sonnet/Haiku) pays off at the memory-compaction boundary.** Compaction is the highest-volume LLM call in a long conversation; using Haiku there cuts cost without a quality hit because the task is summarization, not reasoning. Direct application of [[wiki/concepts/reasoning-execution-split]].
- **MCP is the right abstraction once external integrations exceed ~3.** Below that, direct tools are simpler. Wave 6E was triggered exactly when Slack + Jira + GCal + Teams + Discord all needed connectors and the per-integration glue was about to duplicate. *Candidate for promotion to a concept page — "MCP threshold" — if it holds across other agent projects.*
- **In-process pgvector beats a separate vector DB until the corpus forces it.** One Postgres, one Compose service, one connection pool — and the embeddings sit next to the rows they describe. Same conclusion reached independently in [[wiki/projects/kivora|Kivora]].

## Related

- **Concepts**: [[wiki/concepts/agentic-loop]] (SOUL+Tools+Memory pattern), [[wiki/concepts/augmented-llm]], [[wiki/concepts/reasoning-execution-split]] (Sonnet for loop, Haiku for compaction), [[wiki/concepts/retrieval-augmented-generation]] (in-process pgvector), [[wiki/concepts/mcp-server]] (Wave 6E layer), [[wiki/concepts/scheduled-automation]] (APScheduler proactive briefings), [[wiki/concepts/services-as-software]] (HR-as-agent thesis), [[wiki/concepts/agent-workflow-patterns]], [[wiki/concepts/multi-agent-orchestration]] (loose fit — single-agent today, multi-agent eventually).
- **Entities**: [[wiki/entities/anthropic]] (Claude Sonnet/Haiku), [[wiki/entities/huggingface]] (sentence-transformers, RoBERTa, BART), [[wiki/entities/expo]] (mobile + Expo Push), [[wiki/entities/slack]] (Wave 6C bot), [[wiki/entities/gusto]] (named future integration target).
- **Other projects**: [[wiki/projects/kivora]] — sibling architecture (Spring Boot + FastAPI Claude agent + pgvector RAG); the closest pattern-match in the brain — different domain (GRC vs HR), same agent stack. [[wiki/projects/vedge]] — multi-tenant SaaS reference. [[wiki/projects/stacesprouts]] and [[wiki/projects/coffee-break-with-big-sis]] — same "outer wrapper, no remote, multiple service repos" topology.

## External links

- **Repo (backend)**: https://github.com/clarvyn/backend
- **Repo (portal)**: https://github.com/clarvyn/workspace
- **Repo (landing)**: https://github.com/clarvyn/landing
- **Repo (mobile app)**: https://github.com/clarvyn/app
- **Repo (agent)**: `git@clarvyn:clarvyn/agent.git`
- **Project's own `CLAUDE.md`**: `/Users/kobbyopoku/ROAM/CascadeProjects/clarvyn/CLAUDE.md` (Plan-Mode-Default + Subagent Strategy + Self-Improvement Loop + Verification + Demand Elegance + Autonomous Bug Fixing operating instructions).
- **Auto-memory**: `~/.claude/projects/-Users-kobbyopoku-ROAM-CascadeProjects-clarvyn/memory/MEMORY.md` (and `architecture.md` companion).
- **Project docs**: `/Users/kobbyopoku/ROAM/CascadeProjects/clarvyn/docs/` (14+ markdown files — `PROJECT_OVERVIEW.md`, `PROJECT_ASSESSMENT.md`, `DOCKER_GUIDE.md`, etc.).
- **Default platform-owner credential** (dev only): `godwin@clarvyn.ai` / `Admin@123` (seeded by `DataInitializer`).
