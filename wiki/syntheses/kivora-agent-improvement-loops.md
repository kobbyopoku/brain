---
type: synthesis
title: Kivora agent improvement loops
created: 2026-07-24
updated: 2026-07-24
question: Where do Kivora's agents already match the wiki's agent patterns, and what would make them smarter and self-improving — framed as loops and graphs?
tags: [synthesis, agents, self-improvement, kivora]
---

# Kivora agent improvement loops

> [[wiki/projects/kivora|Kivora]]'s Compass agent family reviewed against the wiki's accumulated agent patterns: the architecture is strong where the wiki predicts strength, and every remaining gap is the same shape — a loop that is instrumented on one side but never closed on the other.

## TL;DR

Kivora already implements several of the wiki's strongest agent patterns — verifier-gated delegation (it is the worked example on [[wiki/concepts/multi-agent-delegation-with-verifier]]), [[wiki/concepts/hybrid-rag-retrieval|hybrid RAG]], [[wiki/concepts/dual-write-rollout|dual-write rollout]], typed tool contracts with per-persona palettes, and per-call audit logging. What it lacks is not capability but *closure*: five feedback loops (self-annealing, failure-learning, evals, triggers, theater-detection) are each half-built — data collected, nothing consumes it. The second structural upgrade is topological: the verified action path is a linear chain, and [[wiki/concepts/reliability-decay-math]] argues for restructuring it into a graph with parallel branches, deterministic edges, and verification concentrated at side-effect points.

## Context

Filed back from a read-mode query on 2026-07-24 that reviewed Kivora's agent codebase against the wiki's agent-architecture pages. Kivora's Python agent has grown from a single `soul.py` into the Compass persona family (Compass / Scribe / Pulse / Autopilot / Verifier) with 292 tools, sub-agent autonomy, and full audit instrumentation ([[wiki/projects/kivora]]). The question is what separates this from the *self-improving* agents the wiki documents — and the answer decomposes cleanly into loops that need closing and a chain that wants to become a graph. The cross-cutting reference architecture for this class of system is [[wiki/syntheses/multi-agent-ops-platform-blueprint]].

## Argument / analysis

### Where Kivora already matches the wiki

- **Verifier-gated delegation.** Kivora is the wiki's original worked example on [[wiki/concepts/multi-agent-delegation-with-verifier]]: a read-only Verifier persona with refusal-shaped defaults gates every destructive Composio action, invoked on a narrow context independent of the executing persona ([[wiki/projects/kivora]]).
- **Hybrid RAG.** The retrieval path runs BM25 + dense vector + cross-encoder reranking fused via RRF — the exact shape [[wiki/concepts/hybrid-rag-retrieval]] describes ([[wiki/projects/kivora]]).
- **Dual-write rollout.** The Findings pipeline shipped as an idempotent additive dual-write behind a toggle, failures swallowed with `log.warn` so the new path cannot break the old — a textbook instance of [[wiki/concepts/dual-write-rollout]].
- **Typed tool contracts and per-persona palettes.** The 292-tool Compass palette is RBAC-filtered at registration time, and each sub-agent runs a filtered palette inside its own token budget — matching the tool-definition, catalog-size, and security steps of the reliability roadmap in [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]].
- **Per-call instrumentation.** `AiUsageLogger` writes every Compass activity — main chat, all four sub-agent loops, memory operations, injection checks — to `ai_audit_log` rows ([[wiki/projects/kivora]]).
- **Cold-open briefings.** Client-triggered briefings on chat open (observed in the 2026-07-24 review) implement the *synthesis, not restatement* principle of [[wiki/concepts/daily-ai-briefing]]: the agent reports what workspace data means, not what it says.

### Five unclosed loops — the improvement roadmap

Each loop below is already instrumented on the input side; none has a consumer. Closing them is the roadmap.

**1. Self-annealing loop.** No Kivora process reads `ai_audit_log` and proposes prompt or soul-file diffs — the audit trail accumulates but never anneals the system that produced it. The blueprint exists in-house: [[wiki/projects/helm|Helm]]'s Analytics meta-orchestrator runs review-mode-permanent over agent transcripts ([[wiki/concepts/self-annealing]]). The Kivora-native shape is a **"Coach" persona** that periodically reads the audit log and files prompt-change proposals *through the existing Ed25519 two-person promotion pipeline* — self-improvement gated by the same two-human approval machinery that already gates content promotion ([[wiki/projects/kivora]]).

**2. Failure-learning loop.** Failed trajectories currently die in logs. [[wiki/concepts/learning-from-failure]] argues failures are the highest-signal training data an agent produces; the loop is: retain and label failed trajectories, have an LLM name the failure mode and draft a patch (a prompt amendment or tool-contract fix per [[wiki/concepts/inference-time-patching]]), and gate application behind a human. Kivora retains nothing structured about *why* a run failed.

**3. Eval loop — the gate on the other four.** Neither of the above loops is safe without measurement: [[wiki/concepts/automated-prompt-optimization]] warns that prompt optimization without evals is "automated tweaking." The Kivora-sized starting point per [[wiki/concepts/agent-evals]] is a golden dataset of ~20 queries per persona, plus **tool-layer metrics tracked separately from end-to-end quality** — tool-selection accuracy, argument validity, retry rate. Notably, Verifier verdicts are free labels: every approve/refuse decision already recorded in the audit ledger is a graded example waiting to be harvested.

**4. Trigger loop.** Helm's build log states the operating constraint plainly: agents are not autonomous without a trigger ([[wiki/projects/helm]]). Kivora's personas act only when a client opens a chat. Two additions close this: cron-scheduled briefings posted to a persistent thread ([[wiki/concepts/scheduled-automation]]), and Helm-Phase-C-style guarded self-management tools — `create_task` / `create_schedule`, JWT-scoped and rate-capped — so the agent can arrange its own future work within hard bounds.

**5. Theater-detection loop.** [[wiki/concepts/helpful-assistant-theater]] documents the failure mode where a persona *claims* progress it never executed. Kivora records both sides of the comparison — persona claims in chat transcripts, ground truth in the tool-invocation log — and compares them nowhere. A theater detector is a diff job over data that already exists.

### From chains to graphs

The wiki is currently thin on graph orchestration — no LangGraph or knowledge-graph source has been ingested — flagged here as an **ingestion gap**. The claims below are limited to what existing pages support.

Kivora's verified action path is a linear chain: intent → plan → delegate → verify → execute → log. [[wiki/concepts/reliability-decay-math]] quantifies why chains are fragile — five sequential steps at 95% each compound to roughly 77% end-to-end — and this argues for restructuring the chain into a graph: run independent branches (e.g., posture queries via Pulse and evidence retrieval) in parallel so the effective sequential N shrinks; move deterministic edges (routing, schema validation, RBAC filtering) into code where reliability is 100%; and place verification nodes only at side-effect concentration points rather than uniformly, per [[wiki/concepts/verification-loops]] and the system-over-model thesis of [[wiki/sources/stanford-anthropic-system-more-powerful-than-model]]. Kivora's Verifier-before-destructive-Composio placement already honors the concentration principle; the parallelization and deterministic-edge moves do not exist yet.

Memory is the second graph candidate. The nearest existing coverage is [[wiki/concepts/agentic-memory]] plus [[wiki/concepts/retain-reflect-memory-split]] — a memory-as-graph treatment (entities and decisions as nodes, provenance as edges) would need a dedicated source ingest before it can be argued from the wiki.

### Priority order

Effort-ascending, each item independently shippable:

1. **Theater-detector** — a diff over two datasets Kivora already records.
2. **Golden datasets + tool-layer eval** — ~20 queries/persona; harvest Verifier verdicts as labels.
3. **Cron briefings** — scheduled trigger into a persistent thread.
4. **Guarded self-management tools** — `create_task` / `create_schedule`, JWT-scoped, capped.
5. **Coach persona** — audit-log-reading prompt-diff proposer, gated by two-person promotion.

The ordering embeds a dependency: the eval loop (item 2) should land before the Coach persona (item 5), because unevaluated self-modification is the "automated tweaking" anti-pattern ([[wiki/concepts/automated-prompt-optimization]]).

## Evidence summary

| Claim | Supporting |
|---|---|
| Kivora is the worked example of verifier-gated delegation | [[wiki/concepts/multi-agent-delegation-with-verifier]], [[wiki/projects/kivora]] |
| Hybrid retrieval and dual-write rollout are implemented as documented | [[wiki/concepts/hybrid-rag-retrieval]], [[wiki/concepts/dual-write-rollout]], [[wiki/projects/kivora]] |
| Tool layer matches the reliability roadmap | [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] |
| Audit trail exists but nothing anneals from it | [[wiki/projects/kivora]], [[wiki/concepts/self-annealing]], [[wiki/projects/helm]] |
| Failures are high-signal data, currently discarded | [[wiki/concepts/learning-from-failure]], [[wiki/concepts/inference-time-patching]] |
| Optimization without evals is automated tweaking | [[wiki/concepts/automated-prompt-optimization]], [[wiki/concepts/agent-evals]] |
| No trigger means no autonomy | [[wiki/projects/helm]], [[wiki/concepts/scheduled-automation]] |
| Claim-vs-action divergence is a documented failure mode | [[wiki/concepts/helpful-assistant-theater]] |
| Sequential chains decay multiplicatively; graphs mitigate | [[wiki/concepts/reliability-decay-math]], [[wiki/concepts/verification-loops]], [[wiki/sources/stanford-anthropic-system-more-powerful-than-model]] |
| Memory-as-graph nearest coverage | [[wiki/concepts/agentic-memory]], [[wiki/concepts/retain-reflect-memory-split]] |

## Open questions

- **Ingestion gap**: no LangGraph / graph-orchestration / knowledge-graph source in the wiki yet; the graph-restructuring argument currently rests on reliability math rather than a dedicated orchestration source.
- What golden-dataset refresh cadence keeps evals honest as the tool palette grows past 292?
- Should Coach proposals target soul files only, or extend to tool contracts and palette membership (higher blast radius, same promotion gate)?
- Does the theater-detector run online (per-response) or as a batch audit — and what false-positive rate is tolerable before admins stop reading it?

## Related

- [[wiki/syntheses/multi-agent-ops-platform-blueprint]] — the cross-cutting 5-layer architecture this roadmap slots into.
- [[wiki/projects/kivora]] — the project under review.
- [[wiki/projects/helm]] — in-house blueprint for the meta-orchestrator and trigger patterns.
- [[wiki/syntheses/agent-review-framework]] — the earlier (2026-05-08) five-lens audit of the same agent; this synthesis is its loop-and-graph sequel.
