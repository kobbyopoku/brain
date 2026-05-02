---
type: source
title: I Want to Build an AI Agent Today (Full Course) — hooeem
created: 2026-05-02
updated: 2026-05-02
source_url: https://x.com/hooeem/status/2037250422403113188
source_type: x-thread
author: hooeem
source_date: 2026-03-26
raw_path: raw/I want to build an AI agent today (full course).md
tags: [agents, agent-frameworks, anthropic, openai, foundational, agent-workflow-patterns]
---

# I Want to Build an AI Agent Today (Full Course) — hooeem

> A from-zero course on building an AI agent today. Synthesizes Anthropic and OpenAI guidance into a layman-friendly path: how agents work, the five workflow patterns, building your first agent, tool design, memory, real-world testing, multi-agent setups, and the discipline of starting simple. The wiki's foundational source on [[agentic-loop]], [[augmented-llm]], [[agent-workflow-patterns]], and [[beginner-agent-types]].

## TL;DR

hooeem positions this as "the course no one made for the layman." Eight sections walk through: (1) how agents work — the LLM + tools + memory loop; (2) five workflow patterns from Anthropic — prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer; (3) building your agent (Anthropic-first or OpenAI-first); (4) tool design (fewer + clearer beats more); (5) memory (most agents don't need it); (6) real-world testing; (7) multi-agent setups (start with one); (8) the wrap. The recurring discipline: agents are conceptually simple but operationally demanding; start with the simplest pattern that works; tool design and evaluation matter more than framework choice.

## Key takeaways

### How agents work — the foundations
- **The agentic loop** ([[agentic-loop]]): user input → LLM thinks → LLM decides (respond or call a tool) → if tool, execute and feed result back → repeat.
- **Brain / hands / notepad**: LLM is the brain, tools are the hands, memory is the notepad. Frameworks (LangGraph, CrewAI, Anthropic SDK, OpenAI Agents SDK) wrap this loop with abstractions but don't change its essence.
- **Augmented LLM** ([[augmented-llm]]): plain LLM + tools + retrieval + memory. Anthropic exposes tools via JSON schema with `input_schema`; OpenAI wraps functions in a function object with parameters.
- **Workflows vs. agents**: workflows are deterministic (your code controls execution); agents are dynamic (the LLM decides next step, may call tools repeatedly). Workflows are cheaper. Start with a workflow; graduate to agent only if needed.

### The 5 workflow patterns ([[agent-workflow-patterns]])
1. **Prompt chaining** — sequential steps, each LLM call processes prior output, programmatic gates between steps. Use when task decomposes cleanly.
2. **Routing** — classify input, route to specialized handlers each with its own optimized prompt. Use for fundamentally different input categories (customer service triage).
3. **Parallelization** — run multiple LLM calls simultaneously (sectioning for independent subtasks; voting for consensus on a critical decision).
4. **Orchestrator-workers** — central LLM dynamically breaks down a task and delegates to worker LLMs at runtime; subtasks are not predefined. Use for code generation across files, research, report writing. **This is essentially the pattern that [[subagents]] formalize at the team scale.**
5. **Evaluator-optimizer** — one LLM generates, another evaluates and feeds back; loop until criteria met. Use for translation, code generation, writing.

### Building your agent
- **Five-question mental model**: Write down the job → Decide what tools it needs → Tell the model how to behave → Test on 5 real examples → Add complexity only on failure.
- **The four design questions**: What is the outcome? What information does it need? What actions should it be allowed to take? What rules must it follow?
- **The formula**: `Agent = Role + Goal + Tools + Rules + Output format`.
- **Anthropic-first** if the agent should read/write/edit files, run shell, search web, use MCP, write code.
- **OpenAI-first** if you want clean SDK with hosted tools, handoffs, guardrails, simple path to production.
- **Use AI to design the agent before building it** — paste a structured request to Claude/ChatGPT asking for spec, system prompt, tool list, roadmap, test cases.

### Five beginner agent types ([[beginner-agent-types]])
1. **Research agent** — gather and summarize.
2. **Content agent** — write, rewrite, summarize, transform.
3. **Workflow agent** — repeatable business processes (classification, routing, response drafting).
4. **Personal knowledge agent** — answer from your documents (file search / RAG).
5. **Operator agent** — take actions in an environment (read/edit files, run shell, save reports).

### Tool design
- *"Better tools = smarter agent. Fewer tools = more reliable agent."*
- Ask "does this need a tool?" before adding one. No tool needed for "rewrite this email"; tool needed for "what's the weather right now?"
- One tool = one clear job. `read_file(path)` beats `manage_files(action, file, dest, overwrite, format, permissions)`.
- Tell the agent **when** to use the tool — *"Use this tool whenever maths is required. Never guess calculations."*
- Let the agent fail and fix iteratively (description / inputs / rules).

### Memory
- Two types: short-term (conversation) and long-term (external knowledge).
- Most agents don't need complex memory. Start without it. Add only when something breaks.
- File-based memory (RAG with file search) is often enough; vector DB / embeddings come last.

### Multi-agent setups
- Start with ONE agent. Always.
- Three valid reasons to add more: different skills, clear pipeline, different permissions.
- **Supervisor model** is the safest starting pattern (User → Main agent → calls others if needed). Avoid swarm / fully-autonomous multi-agent setups early.

### Three actionable takeaways (closing)
- Build the from-scratch agent first to understand the raw loop.
- Start with the simplest pattern that works (often prompt chaining or routing, not autonomous agents).
- Invest in tool design and evaluation early — well-designed tools beat better models or bigger frameworks.

### Stable-vs-volatile claim
- Volatile: frameworks (LangGraph, CrewAI, Anthropic SDK, OpenAI SDK), MCP standardization, version numbers (Claude Code SDK renamed to Claude Agent SDK Sept 2025; current v0.1.50 March 2026; OpenAI Agents SDK launched March 11, 2025; openai-agents v0.13.1).
- Stable: the agentic loop, the five workflow patterns, principles of tool design, the discipline of starting simple.

## Notable quotes

> "The LLM is the 'brain' that reasons. Tools are the 'hands' that perform actions. Memory is the 'notepad' that records what has happened so far."

> "Workflows are deterministic; your code controls execution. Agents are dynamic; the LLM decides the next step."

> "Better tools = smarter agent. Fewer tools = more reliable agent."

> "Agents are conceptually simple but operationally demanding."

> "Start with one of these workflow patterns. Graduate to autonomous agents only when you need the LLM to decide the execution path dynamically."

## Notes

- **This is the most foundational source on agent-building** ingested so far. It is the source the wiki should cite when explaining the *why* underneath any specific Claude Code feature.
- **The 5 workflow patterns are Anthropic's framing** (originally from Anthropic's "Building effective agents" guidance, per the post's attribution). Capturing them as a single concept page ([[agent-workflow-patterns]]) keeps them findable.
- **Cross-source resonance**:
  - **regent0x_'s 5-role subagent setup** (architect/coder/reviewer/tester/ops) is essentially an instance of orchestrator-workers + evaluator-optimizer composed.
  - **heynavtoor's 10 repos** include CrewAI and LangGraph as canonical multi-agent frameworks — the same frameworks hooeem treats as workflow-pattern implementations.
- **Date inconsistency to flag**: post header lists `published: 2023-03-26` but content references "Claude Code launched in February 2025" and "March 2026 release v0.1.50." The 2023 date in frontmatter is likely a metadata error — content unambiguously dates to 2026 Q1. Treat content as 2026.
- **The "use AI to design the agent before building it" prompt** is itself a high-quality reusable prompt (see [[personal-claude-prompts]]).
- **The author's Substack** (`sevenc.substack.com`) is named at the end as a CTA. Worth tracking if a follow-up on this thread arrives.

## Mentioned entities

### People
- [[wiki/entities/hooeem]] — author.

### Frameworks / SDKs / tools
- [[wiki/entities/anthropic-agent-sdk]] — Claude Code SDK renamed to Claude Agent SDK in September 2025; v0.1.50 in March 2026.
- [[wiki/entities/openai-agents-sdk]] — Python `openai-agents`; launched March 11, 2025; v0.13.1 in March 2026.
- [[wiki/entities/langgraph]] — already in wiki via heynavtoor; named here as a canonical framework.
- [[wiki/entities/crewai]] — already in wiki via heynavtoor; named here as a canonical multi-agent framework.

### Organizations
- [[wiki/entities/anthropic]] — origin of the 5 workflow patterns documentation.

## Related concepts

- [[agentic-loop]] — canonical wiki source.
- [[augmented-llm]] — canonical wiki source.
- [[agent-workflow-patterns]] — canonical wiki source.
- [[beginner-agent-types]] — canonical wiki source.
- [[subagents]] — orchestrator-workers pattern at the team scale.
- [[multi-agent-orchestration]] — adjacent runtime layer.
- [[mcp-server]] — referenced as standardization milestone ("MCP became a universal standard in under a year").
- [[claude-code-skills]] — Anthropic-first agents naturally compose with skills.

## Related sources

- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — names the same canonical frameworks (CrewAI, LangGraph) as off-the-shelf replacements.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — applied configuration of orchestrator-workers via subagents.
- [[wiki/sources/AnatoliKopadze-20-claude-prompts]] — adjacent (prompt engineering as the content layer).
