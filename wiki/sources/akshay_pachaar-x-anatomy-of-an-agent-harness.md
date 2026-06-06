---
type: source
title: akshay_pachaar — The Anatomy of an Agent Harness
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/akshay_pachaar/status/2041146899319971922
source_type: x-thread
author: Akshay Pachaar (@akshay_pachaar)
source_date: 2026-04-06
raw_path: raw/The Anatomy of an Agent Harness.md
content_status: substantive-verbatim
tags: [agent-harness, harness-engineering, context-engineering, orchestration-loop, claude-agent-sdk, multi-agent, verification-loops, scaffolded-llm, foundational]
---

# akshay_pachaar — The Anatomy of an Agent Harness

> A long-form synthesis arguing that production agent performance is determined less by the model than by the **agent harness** — the complete non-model software infrastructure (orchestration loop, tools, memory, context management, state, error handling, guardrails, verification) wrapping an LLM — drawing on how Anthropic, OpenAI, Perplexity, and LangChain actually build.

## TL;DR

Pachaar formalizes the **agent harness**: the entire software stack around a model that turns a stateless LLM into a capable agent. The load-bearing thesis is *"if you're not the model, you're the harness"* (LangChain's Vivek Trivedy) — two products on identical model weights can differ by 20+ TerminalBench ranking positions based on harness design alone. The piece enumerates 12 harness components, traces a single orchestration cycle step-by-step, surveys how Claude Agent SDK / OpenAI Agents SDK / LangGraph / CrewAI / AutoGen implement the pattern, and closes with seven recurring architectural decisions and a "scaffolding-is-removed-when-the-building-is-complete" argument for thinning harnesses as models improve.

## Key takeaways

- **The harness is the product.** Changing only the infrastructure (same model, same weights) moved LangChain from outside the top 30 to rank 5 on TerminalBench 2.0; a separate research project hit a 76.4% pass rate by having an LLM optimize the infrastructure itself, beating hand-designed systems.
- **Canonical definition** (Vivek Trivedy, LangChain): *"If you're not the model, you're the harness."* The "agent" is the emergent goal-directed behavior; the harness is the machinery producing it. "I built an agent" really means "I built a harness and pointed it at a model."
- **Term provenance.** Formalized early 2026, concept older. Anthropic's docs call the SDK *"the agent harness that powers Claude Code"*; OpenAI's Codex team equates "agent" and "harness" as the **non-model infrastructure**.
- **Von Neumann analogy** (Beren Millidge, 2023 *"Scaffolded LLMs as Natural Language Computers"*): raw LLM = CPU; context window = RAM (fast, limited); external DBs = disk (large, slow); tools = device drivers; harness = operating system. *"We have reinvented the Von Neumann architecture."*
- **Three concentric engineering levels**: prompt engineering (instructions) ⊂ context engineering (what the model sees and when) ⊂ harness engineering (everything: orchestration, state, error recovery, verification, safety, lifecycle).
- **12 harness components**: (1) orchestration loop, (2) tools, (3) memory, (4) context management, (5) prompt construction, (6) output parsing, (7) state management, (8) error handling, (9) guardrails/safety, (10) verification loops, (11) subagent orchestration — plus the model itself as the 12th anchor. *(Note: the source labels "12 components" but enumerates 11; see Notes.)*
- **The loop is a "dumb loop."** Anthropic describes the runtime as a dumb while-loop where all intelligence lives in the model; the harness just manages turns. The complexity lives in what the loop manages, not the loop.
- **Context rot is the silent killer.** Model performance degrades 30%+ when key content sits mid-window (Chroma research; corroborated by Stanford's "Lost in the Middle"). Even million-token windows suffer instruction-following degradation. Mitigations: compaction, observation masking (JetBrains Junie), just-in-time retrieval (grep/glob/head/tail over full-file loads), sub-agent delegation (subagents return 1–2k-token condensed summaries).
- **Memory is multi-timescale and treated as a hint.** Short-term = session history; long-term persists across sessions (Anthropic CLAUDE.md + auto-generated MEMORY.md; LangGraph JSON Stores; OpenAI Sessions on SQLite/Redis). Claude Code uses a three-tier hierarchy (≈150-char index always loaded → topic files on demand → raw transcripts via search), and **verifies memory against actual state before acting**.
- **Errors compound.** A 10-step process at 99% per-step success has only ~90.4% end-to-end success. LangGraph distinguishes four error types (transient / LLM-recoverable / user-fixable / unexpected); Stripe's production harness caps retries at two.
- **Verification gives 2–3x quality.** Boris Cherny (creator of Claude Code) says giving the model a way to verify its work improves quality 2–3x. Three approaches: rules-based (tests/linters/type-checkers), visual (Playwright screenshots), LLM-as-judge.
- **The Ralph Loop** for tasks spanning multiple context windows: an Initializer Agent sets up environment + progress file + feature list + initial git commit, then a Coding Agent each session reads git logs + progress files, picks the highest-priority incomplete feature, works, commits, summarizes. Filesystem = continuity across context windows.
- **Seven harness decisions**: single- vs multi-agent (maximize single first; split only past ~10 overlapping tools); ReAct vs plan-and-execute (LLMCompiler: 3.6x speedup); context-window strategy (ACON: 26–54% token reduction at 95%+ accuracy); verification design (guides/feedforward vs sensors/feedback — Fowler/Thoughtworks); permission/safety (permissive vs restrictive); tool scoping (Vercel cut 80% of v0 tools and improved; Claude Code 95% context reduction via lazy loading); harness thickness (thin + model-improvement vs explicit control).
- **Co-evolution + scaffolding principle.** Models are now post-trained with specific harnesses in the loop, so changing tool implementations can degrade performance. As models improve, harness complexity should shrink (Manus rebuilt five times in six months, each removing complexity). Future-proofing test: if performance scales with stronger models *without* adding harness complexity, the design is sound.

## Notable quotes

> "If you're not the model, you're the harness."
> — Vivek Trivedy (LangChain), quoted as the canonical formula

> "We have reinvented the Von Neumann architecture."
> — Beren Millidge, *"Scaffolded LLMs as Natural Language Computers"* (2023)

> "The agent harness that powers Claude Code."
> — Anthropic Claude Code documentation, on the SDK

> "The next time your agent fails, don't blame the model. Look at the harness."
> — closing line

## Notes

- **This is a foundational systematization source.** It gives a single vocabulary (harness / harness engineering / 12 components / 7 decisions) that several existing wiki concepts already gesture at: [[wiki/concepts/agentic-loop]] (the orchestration loop), [[wiki/concepts/reasoning-execution-split]] (the "dumb loop, intelligence in the model" claim), [[wiki/concepts/augmented-llm]] (tools + memory + retrieval around the model), [[wiki/concepts/agent-workflow-patterns]]. The harness concept is the *superset* — likely the most useful new concept page from this ingest, with harness-engineering and context-engineering as siblings.
- **Counting discrepancy (flagged):** the heading says "The 12 Components of a Production Harness" but only 11 are enumerated (1–11). The 12th is most plausibly "the model" itself (the anchor the other 11 wrap), but the source does not state this explicitly. Marked uncertain — do not assert the 12th component as fact in derived pages.
- **Strong overlap with [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]** (same author, ~5 weeks later, status 2055629943891988719). That piece anatomizes the `~/.hermes` folder (a concrete harness); this piece is the abstract theory of harnesses generally. They are companion pieces — concrete instance vs general pattern.
- **Direct tie to [[wiki/projects/helm]] and [[wiki/syntheses/multi-agent-ops-platform-blueprint]].** Helm is a 6-agent ops platform on the [[wiki/entities/hermes-agent|Hermes]] runtime; the "seven harness decisions" (single vs multi-agent, tool scoping, harness thickness, verification design) are precisely the choices Helm's architecture makes. Worth cross-linking when the harness concept page lands.
- **The Ralph Loop** here maps to the wiki's existing `ralph-loop` plugin/skill references and is a candidate for its own concept page (long-running-agent / multi-context-window continuity via filesystem).
- Numerous benchmark claims (TerminalBench 20+ position swing, 76.4% pass rate, 3.6x LLMCompiler, 26–54% ACON, 95% Claude Code context reduction, 80% Vercel tool cut, 2–3x verification) are cited but unverified here — treat as the author's reported figures, not independently confirmed.
- New entities worth stubbing: LangChain (org), AutoGen / Microsoft Agent Framework, Deep Agents, Manus, JetBrains (Junie), Beren Millidge, Vivek Trivedy. New concepts: agent-harness, harness-engineering, context-engineering, prompt-engineering, context-rot, scaffolded-llm, von-neumann-architecture, verification-loops, context-management, state-management, guardrails, tool-scoping, ralph-loop.

## Mentioned entities

- [[wiki/entities/akshay_pachaar]] — author; this is his harness-anatomy thesis post.
- [[wiki/entities/anthropic]] — Claude Code / Claude Agent SDK as the canonical "dumb loop" harness.
- [[wiki/entities/claude-code]] — six tool categories, three-tier memory, Gather-Act-Verify, ~40 gated capabilities, three subagent models (Fork/Teammate/Worktree).
- [[wiki/entities/anthropic-agent-sdk]] — exposes the harness via `query()` returning an async iterator; "the agent harness that powers Claude Code."
- [[wiki/entities/openai]] — Codex/Agents SDK; equates "agent" and "harness"; strict priority stack; three-layer Codex architecture.
- [[wiki/entities/openai-agents-sdk]] — Runner class (async/sync/streamed), function/hosted/MCP tools, three-level guardrails, agents-as-tools + handoffs.
- [[wiki/entities/codex-cli]] — Codex harness; AGENTS.md 32 KiB cascade; surfaces share one harness.
- [[wiki/entities/perplexity-ai]] — named as one of the four labs "actually building" harnesses (framing/abstract only).
- [[wiki/entities/langchain]] — *(stub)* TerminalBench rank-5 jump on harness-only change; AgentExecutor deprecated in v0.2; Deep Agents.
- [[wiki/entities/langgraph]] — harness as explicit state graph (llm_call + tool_node + conditional edge), typed-dict state with reducers, checkpointing, four error types.
- [[wiki/entities/crewai]] — role-based multi-agent (Agent/Task/Crew) + Flows deterministic backbone.
- [[wiki/entities/autogen]] — *(stub)* conversation-driven orchestration; evolving into Microsoft Agent Framework; five orchestration patterns.
- [[wiki/entities/microsoft]] — *(stub)* Microsoft Agent Framework (AutoGen successor).
- [[wiki/entities/deep-agents]] — *(stub)* LangChain harness using the term "agent harness" explicitly (write_todos, file systems, subagents, persistent memory).
- [[wiki/entities/manus]] — *(stub)* rebuilt five times in six months, each removing harness complexity.
- [[wiki/entities/jetbrains]] — *(stub)* Junie uses observation masking (hides old tool outputs, keeps tool calls visible).
- [[wiki/entities/stripe]] — production harness caps retry attempts at two.
- [[wiki/entities/vercel]] — removed 80% of v0's tools and got better results.
- [[wiki/entities/boris-cherny]] — creator of Claude Code; "verify your work = 2–3x quality."
- [[wiki/entities/beren-millidge]] — *(stub)* author of "Scaffolded LLMs as Natural Language Computers"; Von Neumann analogy.
- [[wiki/entities/vivek-trivedy]] — *(stub)* LangChain; "if you're not the model, you're the harness."

## Related concepts

- [[wiki/concepts/agent-harness]] — *(new)* the core concept this source defines and systematizes.
- [[wiki/concepts/harness-engineering]] — *(new)* the outermost of the three concentric engineering levels.
- [[wiki/concepts/context-engineering]] — *(new)* managing what the model sees and when; the middle level.
- [[wiki/concepts/prompt-engineering]] — *(new)* the innermost level; crafting instructions.
- [[wiki/concepts/agentic-loop]] — the orchestration loop / TAO / ReAct cycle is the harness's heartbeat.
- [[wiki/concepts/reasoning-execution-split]] — "dumb loop, all intelligence in the model" is this split stated as a runtime principle.
- [[wiki/concepts/augmented-llm]] — tools + memory + retrieval are the augmentation the harness wires up.
- [[wiki/concepts/agent-workflow-patterns]] — single vs multi-agent, ReAct vs plan-and-execute are workflow-pattern choices.
- [[wiki/concepts/context-rot]] — *(new)* 30%+ mid-window degradation; the failure context management fights.
- [[wiki/concepts/context-management]] — *(new)* compaction, observation masking, JIT retrieval, sub-agent delegation.
- [[wiki/concepts/verification-loops]] — *(new)* rules-based / visual / LLM-as-judge; 2–3x quality.
- [[wiki/concepts/scaffolded-llm]] — *(new)* Millidge's scaffolding/Von-Neumann framing.
- [[wiki/concepts/ralph-loop]] — *(new)* two-phase Initializer + Coding agent continuity across context windows.
- [[wiki/concepts/multi-agent-orchestration]] — subagent orchestration (Fork/Teammate/Worktree; agents-as-tools/handoffs).
- [[wiki/concepts/subagents]] — subagents return condensed summaries to preserve parent context.
- [[wiki/concepts/tool-scoping]] — *(new)* minimum tool set; Vercel 80% cut, Claude Code 95% reduction.

## Related sources

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — same author; concrete `~/.hermes` harness instance to this abstract harness theory.
- [[wiki/sources/nousresearch-hermes-agent]] — Hermes as a worked example of nearly every harness component (memory, plugins, cron, subagents, prompt-cache discipline).
- [[wiki/sources/zodchiii-10-claude-code-agents]] — "agent = job description + trigger + output" is the harness pattern at the slash-command/hook/SDK deployment layer.
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — Anthropic Agent Skills; overlaps on progressive-disclosure / reasoning-execution-split.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — six-layer Claude Code stack; a concrete component breakdown adjacent to this taxonomy.
