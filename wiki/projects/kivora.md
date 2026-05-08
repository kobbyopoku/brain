---
type: project
title: Kivora
created: 2026-05-08
updated: 2026-05-08
status: active
repo: not git-initialized (local only)
local_path: /Users/kobbyopoku/ROAM/CascadeProjects/Kivora
stack: [java-21, spring-boot, postgres, pgvector, flyway, react, typescript, vite, tailwind, fastapi, python, anthropic-claude, minio, cloudflare-r2, railway, vercel, docker]
started: 2026-02-11
aliases: [roam-grc, kivora-grc]
tags: [project, grc, multi-tenant, saas, ai-agent]
---

# Kivora

> An AI-powered multi-tenant SaaS GRC platform — risk register, compliance frameworks, governance lifecycle, and vendor-trust visibility, with a Claude-driven agent that queries workspace data via tools and answers via SSE streaming.

## What and why

Kivora (product name **ROAM GRC**) addresses the lack of a single, AI-aware platform for governance, risk, and compliance teams who currently juggle spreadsheets, isolated GRC tools, and ad-hoc vendor questionnaires. The platform unifies six core domains — risk management, compliance (frameworks + controls + evidence), governance (policies/attestations/exceptions), vendor trust, task management, and AI services — under a multi-tenant architecture with per-workspace scoping. Subscription tiers (`STARTUP`, `GROWTH`, `ENTERPRISE`, `SYSTEM`) gate feature access. The Python FastAPI agent reasons over real workspace data using **20 tool definitions** (14 base + 6 Composio-gated for remediation and PII discovery), persists conversations with Haiku-driven compaction at 50+ messages, and enforces RBAC via a per-tool capability matrix that filters tools at registration time so Claude only sees what the caller's role permits. The hybrid Java + Python AI architecture reserves complex reasoning/chat for the Python agent and routes simple AI tasks through a Spring AI proxy.

## Stack and infrastructure

- **Backend (`backend/`)**: Spring Boot 3.3.6, Java 21, Maven modular monolith. **13 modules**: `kivora-common`, `kivora-security`, `kivora-platform`, `kivora-tenant`, `kivora-risk`, `kivora-compliance`, `kivora-governance`, `kivora-vendor`, `kivora-ai`, `kivora-reporting`, `kivora-notification`, `kivora-trust`, `kivora-app`. PostgreSQL 16 with pgvector. Flyway 10.21 (39+ SQL migrations). MapStruct + Lombok. JJWT for auth. Apache POI + OpenPDF + JFreeChart for reports. Testcontainers + ArchUnit for tests. Spring AI 1.0.0-M4 (BOM).
- **Frontend (`frontend/`)**: React 18, TypeScript 5 (strict), Vite 6. TanStack Query v5 + Table v8, Zustand v5, Radix UI primitives, Tiptap 3 editor, Tailwind 3, Recharts 2.14, react-hook-form + Zod, Vitest, Playwright e2e.
- **Landing (`landing/`)**: React 19, Vite, Tailwind — separate marketing surface.
- **Agent (`agent/`)**: Python 3.11+, FastAPI, Anthropic SDK, SQLAlchemy + pgvector, sentence-transformers (MiniLM-L6-v2, 384-dim), SSE streaming via `sse-starlette`. Port 8090.
- **Storage**: MinIO (dev) / Cloudflare R2 (prod), S3-compatible.
- **Email**: Unosend transactional API.
- **Deploy**: Docker + Railway (backend, agent), Vercel (frontend, landing).
- **AI models**: `claude-sonnet-4-5-20250929` (reasoning + tool use), `claude-haiku-4-5-20251001` (titles + compaction), `all-MiniLM-L6-v2` (embeddings).
- **Repo**: not git-initialized at the workspace root. *(Flag — see Open questions.)*

## Current focus

Week of 2026-05-08:

- **Widget Dashboard System** (`tasks/todo.md`) — converting cards across 4 dashboards (Main, Compliance, Governance, Vendor) into toggleable widgets with localStorage preferences, slide-over Customize panel, drag-to-reorder. 9-step plan, all currently TODO.
- **Feature-gating cleanup** (per auto-memory `project_feature_gating_audit.md`, dated 2026-04-07): 11 of 26 features lack backend `requireFeature()` gates. Frontend shows all nav items/routes to all tiers. This is unfinished and load-bearing.
- **GRC PRD review cadence** — Systems Inventory PRD reviewed 2026-05-08. Phase 3 Systems Inventory module is on the roadmap.

**Recently shipped (2026-05-08):** Agent-review wave landed 10 of 12 findings — see [`tasks/agent-review-2026-05-08.md`](file:///Users/kobbyopoku/ROAM/CascadeProjects/Kivora/tasks/agent-review-2026-05-08.md). Highlights: HITL safety promoted from prompt to code with state-machine-enforced remediation lifecycle; agent-layer RBAC with capability matrix; tool consolidation (21 → 20); parallel tool execution; sanitized error events; tool-result transparency. 93 tests passing across new + existing suites. Framework: [[wiki/syntheses/agent-review-framework]].

## Architecture decisions

- **2026-02** — **Modular monolith over microservices** for backend. 13 Maven modules, single Spring Boot deploy. Same pattern as [[wiki/projects/vedge|Vedge]]. Rationale: small team, transactional consistency, deploy simplicity.
- **2026-02** — **Two-layer tenant isolation**. Layer 1: Hibernate `@Filter` on `TenantScopedEntity` base class. Layer 2: PostgreSQL Row-Level Security policies. `TenantContext` is a `ThreadLocal` set from JWT claims by `TenantSecurityFilter`. Workspace selected per-session via `X-Workspace-ID` header. Defense in depth — RLS catches anything that bypasses Hibernate.
- **2026-02** — **Hybrid Python + Java AI architecture**. Python FastAPI agent (`agent/`) handles complex reasoning, tool use, and RAG with Claude Sonnet. Java `kivora-ai` module handles simple AI tasks (risk-mitigation suggestions, policy drafts) via OpenAI and acts as an authenticated proxy. Mirrors [[wiki/concepts/reasoning-execution-split]].
- **2026-02** — **In-process SQL agent tools, no HTTP round-trips**. The Python agent's 12 tools execute SQL directly against GRC tables (tenant-scoped) rather than calling the Java backend's REST API. Tradeoff: tighter coupling between Python and DB schema, but lower latency and no auth replay between services.
- **2026-02** — **PostgreSQL + pgvector instead of a dedicated vector DB**. RAG uses 384-dim MiniLM-L6-v2 embeddings stored in `ai_document_chunks` with HNSW index. Chunking is sentence-boundary, 500 chars, 50-char overlap. Top-5 cosine search.
- **2026-02** — **SSE streaming over WebSockets** for chat. `sse-starlette` async generators yield `text` / `tool_use` / `tool_result` / `done` events.
- **2026-02** — **Conversation compaction at 50+ messages** by Haiku, replacing older messages with a summary. Bounds context cost.
- **2026-02** — **Subscription-tier feature gating** via `requireFeature()` in services/controllers + `user.features` filter on the frontend. Currently incomplete (see Open questions).
- **2026-05** — **State-machine-enforced remediation lifecycle.** Composio remediation actions (`PROPOSED → APPROVED|REJECTED → EXECUTING → COMPLETED|FAILED → VERIFIED`) are gated by an atomic conditional-UPDATE state machine in `agent/app/services/remediation_state_machine.py`. Pre-2026-05, the lifecycle constraint was enforced only by the system prompt — a single jailbreak or hallucination could trigger an unauthorized Composio action against Okta/AWS/Azure AD. Now: hard SQL gates in `_execute_remediation` and `_verify_remediation` reject any non-`APPROVED` execution attempt before the Composio client is reached. Per [[wiki/concepts/reasoning-execution-split]] — safety belongs in execution, not in reasoning.
- **2026-05** — **Agent-layer RBAC via capability matrix.** Per-tool minimum-role declarations live in `agent/app/agent/capabilities.py`. Tools are filtered out of the schema at registration time based on the caller's `user_roles` (so Claude can't even attempt a forbidden call), with a defense-in-depth hard gate at the executor level. Six roles supported: `PLATFORM_ADMIN`, `WORKSPACE_ADMIN`, `RISK_MANAGER`, `COMPLIANCE_MANAGER`, `VIEWER`, `AUDITOR`. `execute_remediation` is admin-only by blast radius; `propose_remediation` and `verify_remediation` available to risk/compliance managers; `scan_for_pii` to compliance managers and admins.
- **2026-05** — **Parallel tool execution + sanitized error events.** When Claude emits multiple `tool_use` blocks in a single turn, the agent loop fans them out via `asyncio.gather` over an extracted `_execute_one_tool`, then yields SSE events in deterministic block order. Errors map to a small set of user-facing codes (`AI_SERVICE_ERROR`, `DATABASE_ERROR`, `INTERNAL_ERROR`) plus a UUID `error_id` — raw exception strings never reach the client.
- **2026-05** — **Tool-result transparency.** SSE `tool_result` events now carry `preview` (500-char clip), `result` (full parsed payload), `result_size`, and `truncated_in_preview` so clients can render inline summaries with click-to-expand "AI consulted this" widgets. Conversation history API returns `tool_use` and `tool_result` rows for audit transparency.

## Open questions

- **Workspace not under version control.** No `.git` at `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora`. Production-deployed software with no source-of-truth repo is a real risk. Plan: git-init + push to GitHub, or split into polyrepo like Vedge?
- **Feature-gating gaps** — 11 features (autopilot, risk_bank, risk_import, questionnaire_bank, trust_center, integrations, scim_provisioning, multi_workspace, csv_export, webhook_notifications, audit/api/analytics) have no `requireFeature()` enforcement. Most pages are visible to all tiers regardless of plan. Active risk for tier-bypass abuse.
- **Composio migration** — `tasks/composio-migration-plan.md` exists; status unclear from this survey.
- **Systems Inventory PRD (Phase 3)** — open questions per the PRD reviewed 2026-05-08 (configurable enums? soft-delete? scoping uniqueness? bulk import in v1?). Decisions pending.
- **Repo URL for `repo:` field** is unknown until git-init happens.

## Lessons learned

Distilled from `tasks/lessons.md` and Kivora's auto-memory. Promote to `wiki/concepts/` if any generalize beyond GRC.

**Frontend / UX (L001-L008):**

- Navigation item count > completeness — 7 items beats 15; use section landing pages + tabs.
- Dual entry points for the same feature break user mental models — pick one primary surface and commit.
- Dead buttons destroy trust faster than missing features — remove unwired UI immediately.
- "Dashboard" proliferation signals unclear ownership — domain dashboards belong as section landing pages, not peer nav items.

**Engineering (E001-E005):**

- `import.meta.env.VITE_*` is baked at build time — adding env vars in Vercel post-deploy doesn't fix a deployed bundle without a rebuild.
- Vercel doesn't auto-rebuild on env var changes — explicit redeploy required.
- Stale Maven jars cause Spring 404s — when adding a controller in a sub-module, run `mvn install -pl <module> -am -DskipTests` before booting from `kivora-app`.
- Hardcoded fallback URLs (`|| 'http://localhost:8080'`) are a production footgun — use `|| ''` so failures surface visibly.

**Workflow (from auto-memory):**

- **Always run review/QA agents before pushing.** The pattern of push → user finds crash → fix → push has been wasteful. A code-reviewer scan catches snake_case/camelCase mismatches, null-guard gaps, API path mismatches, missing array defaults, wrong HTTP methods, JdbcTemplate column errors, and LazyInitializationException patterns before they ship.

## Related

- **Concepts**:
  - [[wiki/concepts/reasoning-execution-split]] — directly applies to the Python-Sonnet (reasoning) vs Java-OpenAI (simple tasks) + Sonnet-vs-Haiku (reasoning vs compaction) splits, AND to the 2026-05 promotion of HITL remediation safety from prompt to code.
  - [[wiki/concepts/retrieval-augmented-generation]] — Kivora's pgvector RAG implementation is a concrete instance of the pattern.
  - [[wiki/concepts/agentic-loop]] — the agent's max-10-rounds Claude → Tool → Feedback loop.
  - [[wiki/concepts/agent-workflow-patterns]] — informs the 2026-05 state-machine remediation refactor (autonomous loop → workflow pattern).
  - [[wiki/concepts/augmented-llm]] — informs the 2026-05 tool consolidation (21 → 20) and "WHEN to use" description tightening.
  - [[wiki/concepts/markdown-as-agent-contract]] — Kivora's `CLAUDE.md` is exactly this pattern.
  - *(Candidates to seed later: `multi-tenant-saas-isolation`, `modular-monolith`, `feature-gating-strategy`, `subscription-tier-gating`, `pgvector-rag`.)*
- **Entities**:
  - [[wiki/entities/anthropic]] — Claude Sonnet 4 + Haiku 4 power the agent.
  - [[wiki/entities/claude-code]] — Kivora's `CLAUDE.md`, `tasks/` directory, and `.remember/` show heavy Claude Code usage.
  - [[wiki/entities/vercel]] — frontend + landing deploy targets.
  - *(Candidates to seed later: Spring Boot, Spring AI, FastAPI, PostgreSQL, pgvector, Flyway, MinIO, Cloudflare R2, Railway, MapStruct, Lombok, TanStack Query, Radix UI, Tiptap, Unosend.)*
- **Sources**: *(none yet — `ARCHITECTURE.md` and `Requirements Doc.md` at project root are closest equivalents; referenced under External links.)*
- **Syntheses**:
  - [[wiki/syntheses/agent-review-framework]] — five-lens framework for auditing LLM agent codebases. Kivora's 2026-05-08 agent review is the worked example; the project-side findings list with 12 items lives at `tasks/agent-review-2026-05-08.md`.
- **Other projects**:
  - [[wiki/projects/vedge]] — Vedge's brain page already declares **"Kivora as GRC of record"** as a 2026-04 architecture decision. The link is bidirectional.

## External links

- **Repo**: not yet git-initialized
- **Project's CLAUDE.md**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/CLAUDE.md`
- **Architecture doc**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/ARCHITECTURE.md` (50KB, last updated Feb 2026)
- **Requirements doc**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/Requirements Doc.md` (56KB)
- **Risk template implementation notes**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/RISK_TEMPLATE_IMPLEMENTATION.md`
- **Tasks**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/tasks/` (todo.md, lessons.md, qa-report.md, gtm-strategy.md, composio-migration-plan.md, finding-schema-tier1-plan.md, **agent-review-2026-05-08.md**)
- **Agent review backup**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/agent.backup-2026-05-08/` — pre-fix snapshot of the agent directory (730MB, includes venv). Roll-back path while the project remains git-uninitialized.
- **Auto-memory**: `~/.claude/projects/-Users-kobbyopoku-ROAM-CascadeProjects-Kivora/memory/MEMORY.md`
- **Project memory dir**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/.remember/`
- **Agent README**: `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/agent/README.md`
