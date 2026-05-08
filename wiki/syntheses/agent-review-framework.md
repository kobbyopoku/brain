---
type: synthesis
title: Agent review framework — auditing an LLM agent against architectural first principles
created: 2026-05-08
updated: 2026-05-08
question: When given an existing LLM agent codebase, how do you produce a substantive architectural review beyond "the code looks fine"?
tags: [synthesis, agents, agent-architecture, review, framework]
---

# Agent review framework — auditing an LLM agent against architectural first principles

> A reusable lens for reviewing AI-agent codebases by cross-referencing five wiki concepts — [[agentic-loop]], [[augmented-llm]], [[reasoning-execution-split]], [[agent-workflow-patterns]], [[retrieval-augmented-generation]] — against the actual implementation. The framework was developed reviewing [[wiki/projects/kivora|Kivora]]'s Python FastAPI agent on 2026-05-08 and produced 8 actionable findings, the top two of which were not visible without the conceptual lens.

## TL;DR

- **Code review on its own can't see architectural drift.** Static analysis catches bugs; concept-anchored review catches *category errors* (e.g. "this safety rule lives in the wrong layer"). The brain's concept pages provide the anchors.
- **Five concept pages cover the agent attack surface**: [[agentic-loop]] (loop hygiene), [[augmented-llm]] (tool/retrieval/memory profile), [[reasoning-execution-split]] (LLM-vs-code boundary), [[agent-workflow-patterns]] (autonomous-vs-deterministic shape), [[retrieval-augmented-generation]] (knowledge-layer choice). Apply each as a lens; record divergences.
- **The highest-value findings are usually placement errors, not coding errors.** "Safety rule lives in prompt instead of code", "tool count drifted past the discipline threshold", "sub-flow that should be a workflow is being run as an agent loop" — these are conceptual mismatches that don't appear on a `grep` or in a linter run.
- **Documentation drift** is a near-universal finding: README claims N tools, code has M, M > N. Catalog this every time.

## Context

Reviewing a non-trivial agent codebase ("how does Kivora's agent look?") presents a typical scope problem: the code is too large for a uniform line-by-line read, and a line-by-line read misses the architectural questions that actually matter. The brain accumulated foundational agent concepts during 2026-05-02's [[wiki/sources/hooeem-build-an-ai-agent-today]] and adjacent ingests; this synthesis is the first time those concepts were applied as an audit framework against a real codebase.

The framework's purpose is to make agent reviews **repeatable and load-bearing** — usable on the next agent ([[wiki/projects/vedge|Vedge]]'s eventual agent, third-party agents being evaluated, future iterations of Kivora) without re-deriving the lens each time.

## Argument / analysis

### Strand 1: The five lenses

Each brain concept maps to a category of finding. Apply them in order; severity tends to descend down the list.

#### Lens 1 — [[agentic-loop]]: loop hygiene

What to check:

- **Termination conditions.** Is there a hard cap on tool-use rounds? ([[agentic-loop]] flags "loop can spin forever" as a primary failure mode.) Look for `MAX_TOOL_ROUNDS` or equivalent.
- **Stop-reason handling.** Does the loop check `stop_reason` correctly? Does it differentiate `tool_use` / `end_turn` / `max_tokens`?
- **Tool result re-injection.** Are tool results fed back as a `user` role message containing `tool_result` blocks?
- **Stream-vs-discrete semantics.** If streaming, is the streaming-mid-loop pattern handled cleanly? (Open question in [[agentic-loop]] — implementations diverge.)
- **Failure handling at the boundary.** Are tool exceptions wrapped or propagated? (A naked exception escaping a tool poisons the next round.)

Worked example (Kivora): `core.py:29` sets `MAX_TOOL_ROUNDS = 10`, `core.py:186` checks `final_message.stop_reason == "tool_use"`, `core.py:257-260` re-injects results as `{"role": "user", "content": tool_results}`. **Loop is canonical.** ✅

#### Lens 2 — [[augmented-llm]]: tool / retrieval / memory profile

What to check:

- **Tool count discipline.** Per [[augmented-llm]]: *"Better tools = smarter agent. Fewer tools = more reliable agent."* Count actual tool definitions. If > ~10-15, look for consolidation candidates (overlapping verbs, parameterized variants).
- **Tool description clarity.** Each tool description should answer "WHEN to use this." If two tools could plausibly handle the same input, ambiguity will produce wrong-tool calls.
- **Conditional registration.** Tools the agent can't actually use in the current environment should not appear in the schema. ([[agentic-loop]] flags "tool description ambiguous so LLM picks wrong tool" as a failure mode.)
- **Memory layer.** Is conversation history bounded? Is there a compaction strategy? Is long-term knowledge a separate primitive (RAG, files, MCP)?
- **Augmentation portability.** If the agent claims to support multiple LLM providers, are tool schemas translated correctly across `input_schema` (Anthropic) vs function format (OpenAI)?

Worked example (Kivora): 15 base + 6 Composio = **21 tools** when fully loaded. README claims 12. Tool overlap exists (`get_risk_dashboard` / `get_risk_trends` / `detect_anomalies`). Conditional registration is good (`pgvector_available`, `composio_enabled`). Compaction exists (Haiku at 50+ messages).

#### Lens 3 — [[reasoning-execution-split]]: LLM-vs-code boundary

This lens produces the highest-severity findings most often.

What to check:

- **Are deterministic operations being simulated by the LLM?** ("LLM as calculator", "LLM as parser" — both anti-patterns from [[reasoning-execution-split]].)
- **Are judgment calls being hard-coded into rules?** (The inverse failure — regex-classifying customer intent.)
- **Where do safety rules live?** *Critical question.* If a safety constraint is enforced only by the system prompt — "never call X without Y" — and the underlying tool/handler doesn't enforce it in code, the constraint fails open under any prompt-injection, jailbreak, or hallucination. **Safety belongs in execution, not in reasoning.**
- **Where do permission/RBAC checks live?** Same logic — if "only an admin can do X" is a prompt instruction, it's not a permission, it's a request.
- **Tool implementations as the execution carrier.** Each tool's body is the execution side; design quality there is design quality of the execution layer.

Worked example (Kivora): **HIGH-severity finding.** `soul.py:54` instructs *"NEVER call `execute_remediation` on a PROPOSED action."* But `tool_executor._execute_remediation` has no `if action.status != 'APPROVED': return error` gate. The safety rule is purely prompt-side. A jailbreak or hallucination produces an unauthorized Composio action against Okta/AWS/Azure AD.

This was the single most important finding of the review — and it's invisible without the [[reasoning-execution-split]] lens.

#### Lens 4 — [[agent-workflow-patterns]]: autonomous-vs-deterministic shape

What to check:

- **Is the agent a single fully-autonomous loop, or composed of patterns?** Per [[agent-workflow-patterns]]: most problems can be solved with one of five patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) without going fully autonomous.
- **Are there sub-flows that should be patterns?** State machines (lifecycles), report generation (fixed steps), classification + dispatch — all are pattern candidates currently being run as free-form agent loops.
- **[[reliability-decay-math]] argument.** Chained probabilistic steps decay multiplicatively. Each round that *could* be deterministic but isn't compounds error rate.
- **Tool-call parallelism.** If multiple tools fire in one Claude response and the runtime executes them sequentially, that's free latency. `asyncio.gather` for independent tools.

Worked example (Kivora): Remediation lifecycle (`propose → approve → execute → verify`) is an explicit state machine currently driven by Claude's judgment per turn. Should be enforced as a workflow pattern. Compliance-report generation has fixed structure (framework → controls → evidence → summary) and is a [[agent-workflow-patterns|prompt-chaining]] candidate. Tools run sequentially in the loop despite `asyncio` being available.

#### Lens 5 — [[retrieval-augmented-generation]]: knowledge-layer choice

What to check:

- **Is RAG the right shape for the domain?** Per [[retrieval-augmented-generation]] (Karpathy via [[wiki/sources/llm-wiki-pattern-karpathy]]): RAG rediscovers connections from raw fragments every query. Good for very large corpora, weaker for repeated synthesis.
- **Is there a precomputed-synthesis layer?** For domains where the same questions recur (compliance posture, framework readiness), an [[llm-wiki-pattern|LLM-Wiki-style]] curated layer can outperform pure RAG.
- **Embedding choices.** Model, dimensionality, chunk size, overlap, index type. Defaults are usually fine; outliers are worth flagging.
- **Hybrid potential.** Wiki for stable knowledge (frameworks, controls, vendor profiles) + RAG for free-text long tail (uploaded policy documents) is the cleanest hybrid.

Worked example (Kivora): Plain RAG over pgvector with MiniLM-L6-v2 (384-dim, 500-char chunks, HNSW). Standard implementation. The framework-readiness questions GRC users ask repeatedly are an [[llm-wiki-pattern|LLM-Wiki]] candidate; pure RAG forces re-synthesis every query.

### Strand 2: The framework as a checklist

For a one-pass review, the lenses cash out as a sequenced checklist:

1. **Read the agent's own README.** Note tool count, endpoints, workflows it claims.
2. **Read `core.py` (or equivalent loop).** Apply Lens 1.
3. **Read `tools.py`.** Count tools; check overlap; apply Lens 2.
4. **Read `tool_executor.py` (or equivalent).** Apply Lens 3 — *especially* check whether prompt-stated safety rules are enforced in code.
5. **Read `system_prompt`/`soul.py`.** Catalogue every "ALWAYS / NEVER / CRITICAL" instruction; cross-reference with Lens 3.
6. **Read state-machine code (lifecycles, workflows).** Apply Lens 4.
7. **Read RAG/retrieval code.** Apply Lens 5.
8. **Diff README claims vs code reality.** Document drift.

Output: a severity-ranked findings list. Severity rubric:

- **CRITICAL** — Safety, RBAC, or tenant-isolation enforced only in prompt, not in code.
- **HIGH** — Architectural pattern mismatch (sub-flow that should be deterministic is autonomous; vice versa).
- **MEDIUM** — Tool/retrieval-layer hygiene (count drift, ambiguous descriptions, sequential where parallel is free).
- **LOW** — Documentation drift, transparency gaps, defensive-coding nits.

### Strand 3: Why this lens-based approach works

Three reasons concept-anchored review beats line-by-line review for agents:

1. **The architecture is the bug surface.** Agents fail at category-level — "wrong layer for this rule", "missing pattern for this lifecycle" — not at line-level. Line-by-line review reads code; concept review reads *placement*.
2. **Concepts compress prior reading.** Each lens here is the distillate of one or more sources already in the wiki ([[wiki/sources/hooeem-build-an-ai-agent-today]], [[wiki/sources/saraev-agentic-workflows-2026]], [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]], [[wiki/sources/llm-wiki-pattern-karpathy]]). The reviewer is borrowing taste, not deriving it.
3. **The framework outlives the codebase.** Kivora's specific findings will be fixed; the lens stays applicable to the next agent. The concepts compound; the audits are the application.

## Open questions and contradictions

- **Per-domain extensions.** GRC agents have specific failure modes (audit transparency, data lineage, role separation) not covered by the five lenses. Worth a follow-up synthesis once two or three GRC agents have been reviewed.
- **Severity rubric calibration.** "CRITICAL prompt-side safety" is unambiguous; "HIGH pattern mismatch" is a judgment call. A small set of named anti-patterns ("the lifecycle-as-loop anti-pattern") would tighten the rubric.
- **Lens 6 — observability.** Not currently included but probably should be. Open question in [[agentic-loop]]: "standard tooling for tracing loops across frameworks is still emerging." Worth promoting from open-question to first-class lens once the brain has a concept page on it.
- **What about evaluation?** Evals are conspicuously absent from the framework. Most reviewed codebases lack agent evals entirely; the framework currently catches that as a gap rather than a lens. Probably correct, but worth re-examining.

## How to use

When asked "review this agent" — at any granularity, in any project:

1. Open this page.
2. Walk the eight-step checklist in Strand 2.
3. Tag each finding with its lens (Lens 3, Lens 4, etc.) so the reasoning is traceable.
4. Produce a severity-ranked output and link back to the project's brain page.
5. Update this synthesis if the review surfaced a new lens or a new anti-pattern that other reviews would benefit from.

The synthesis is a working document — refine it.

## Worked example: Kivora 2026-05-08 review

The review of [[wiki/projects/kivora|Kivora]]'s Python agent on 2026-05-08 produced 8 findings using this framework:

- 1 CRITICAL (Lens 3): HITL safety rules in prompt instead of code
- 2 HIGH (Lens 4): remediation lifecycle and compliance-report generation should be workflow patterns, not autonomous loops
- 4 MEDIUM (Lens 2 + Lens 4): tool count drift (12 → 21), sequential tool execution, missing role-based gating, RAG-only knowledge layer
- 1 LOW (cross-cut): README documentation drift

The full project-side findings list with file:line references and recommended fixes lives at `/Users/kobbyopoku/ROAM/CascadeProjects/Kivora/tasks/agent-review-2026-05-08.md`. This synthesis page intentionally avoids restating those — the project artifact is the action list; the synthesis is the framework.

## Related concepts

- [[agentic-loop]] — Lens 1.
- [[augmented-llm]] — Lens 2.
- [[reasoning-execution-split]] — Lens 3 (highest-leverage lens).
- [[agent-workflow-patterns]] — Lens 4.
- [[retrieval-augmented-generation]] — Lens 5.
- [[reliability-decay-math]] — supporting argument for Lens 4.
- [[llm-wiki-pattern]] — alternative to RAG referenced in Lens 5.
- [[multi-agent-orchestration]] — adjacent; matters when reviewing systems composed of agents rather than single agents.
- [[subagents]] — adjacent; matters when reviewing role-specialized architectures.

## Related entities

- [[wiki/entities/anthropic]] — `input_schema` tool format and the SDKs most reviewed agents use.
- [[wiki/entities/anthropic-agent-sdk]] — wraps the loop with Anthropic's conventions.
- [[wiki/entities/openai-agents-sdk]] — wraps the loop with OpenAI's conventions.

## Related projects

- [[wiki/projects/kivora]] — the worked example for this framework's first application.
- [[wiki/projects/vedge]] — `vedge_agent` is currently an empty scaffold; this framework will apply when it's built out.

## Mentioned in

- [[wiki/projects/kivora]] — agent review on 2026-05-08 produced the findings list referenced above.
