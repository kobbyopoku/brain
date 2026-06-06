---
type: concept
title: Reasoning + Execution Split
created: 2026-05-02
updated: 2026-06-06
aliases: [reasoning execution division, LLM reasons code executes]
tags: [agent-architecture, foundational]
---

# Reasoning + Execution Split

> The architectural principle that LLMs handle *reasoning* (judgment, interpretation, creative output) while deterministic code handles *execution* (sorting, parsing, structured extraction, exact computations). The agent decides *when* to invoke code; the code ensures *how* it gets done. This combination is what separates "demos" from "systems."

## Definition

The **reasoning + execution split** is a design principle for agent systems: don't ask the LLM to simulate operations that have a deterministic solution. Instead, package the deterministic operation as code (a function, a script, a tool) and let the LLM call it when appropriate.

The split applies most cleanly to operations where:
- The correct answer is unambiguously computable (sorting a list, parsing JSON, extracting fields from a known schema).
- Repetition matters (the operation runs many times and reliability matters more than creativity).
- Errors are expensive (financial calculations, security-sensitive parsing, regex over critical data).

LLMs are great at reasoning *about* these operations — deciding which to invoke, framing the inputs, interpreting the outputs. They are not the right tool for *performing* them.

## Why it matters

The principle reframes a recurring failure mode in agent design: **LLMs simulating operations they shouldn't be simulating.** Asking a model to "sort this list" or "parse this CSV" or "compute compound interest" is asking it to do work that any deterministic function does perfectly. The model's strength is reasoning; using it for deterministic execution wastes the strength and introduces variance where there should be none.

The split is what makes [[claude-code-skills|skills]] particularly powerful. A skill can include executable code (Python, JS, shell). The agent reasons about *whether* the skill applies; the skill's code handles *how* the work gets done. This combination is reliable in a way that pure-LLM workflows are not.

It is also why [[wiki/sources/nateherk-claude-code-os-3m-business|nateherk]]'s framing applies: *"Boring is beautiful: deterministic workflows beat AI agents 9 times out of 10. Most business processes don't need autonomy. They need a Python script that runs on a cron."* The cron-script is the execution layer; the AI sits on top deciding when and why.

## Treatment across sources

- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — canonical wiki source for the architectural framing. *"Language models are great at reasoning. But they're not always the best tool for doing. Sorting, parsing, structured extraction — these are deterministic problems. So instead of forcing the model to simulate them, you let code handle it. The agent decides when to use code. The code ensures how it gets done."*
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational corollary: *"Boring is beautiful — deterministic workflows beat AI agents 9 times out of 10."* Examples include hardcoding ClickUp list IDs into skill.md instead of querying via MCP every time, and delegating heavy data work to sub-agents that wrap deterministic queries.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — adjacent: tool design discipline in the same direction. *"One tool = one clear job"*; *"Tell the agent WHEN to use the tool"*. The tools are the execution side; the agent is the reasoning side.
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — *2026-06-06*. Closing thesis ("tooling > prompting; build high-context environments") is a popular-register statement of the model-reasons / tools-execute principle.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — *2026-06-06*. Implicit; the "system around the model is what makes it useful" thesis is this principle in informal prose.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — *2026-06-06*. Applied at the session level: "treat AI like a specialist, each chat gets one job" — brainstorm in regular Claude, execute a known brief in Design. Plan-vs-execute separation across surfaces rather than across model/tools.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — *2026-06-06*. Reinforced: "most automation tasks can be done with a series of tool calls and just one call to an LLM as an orchestrating layer"; over-using AI compounds token cost and lowers quality.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — *2026-06-06*. The thread's agentic-AI framing (AI reasons over intent, then executes actions across Maps/Gmail/Calendar) is the consumer-product instance of the reasoning-engine-not-execution-engine pattern.
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — *2026-06-06*. Restated for voice: "The LLM is not a parser. Python is a parser. Use Python." Validation (email regex, date parsing, name-length) lives in code, not the prompt; the LLM reasons and tools/code execute.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — *2026-06-06*. Applied at the file level: a project splits into a stable tool-agnostic knowledge/markdown substrate vs. thin swappable per-tool orchestration config — portable "knowledge" vs per-tool "wiring."
- [[wiki/sources/leopardracer-one-person-business-2026-ai]] — *2026-06-06*. Restated as business advice: "the person directing it is where the magic lies" — AI executes but the human supplies judgment/skill; agents do not absolve the operator from learning.
- [[wiki/sources/tricalt-memory-skills-same-harness]] — *2026-06-06*. Skills are "compressed procedures" the agent executes; memory is what it observes/reasons over — a memory-vs-skill cut that maps onto the reasoning/execution split.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — *2026-06-06*. Opus-Strategist analyses (reasoning), Sonnet-Builder executes (execution); the QA gate guards against agent drift — a clean consumer-facing articulation.
- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — *2026-06-06*. Loose echo: pgGraph separates topology-traversal (execution over an integer array) from data hydration (Postgres row fetch) — a separation-of-concerns instance worth a thin cross-link, not the source's framing.
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]] — *2026-06-06*. Agents framed as scoped reasoning units that read from and write to the spine; touched lightly, not the post's focus.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — *2026-06-06*. Reinforced by Anthropic's "dumb loop where all intelligence lives in the model" and by permission-enforcement separated from model reasoning (model decides what to attempt; tool system decides what's allowed).
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — *2026-06-06*. Pattern 5 restates the division at the org level: "The AI writes the code. The engineer decides what code should exist" — strategy (reasoning) flips from 30% to 70% of engineer time as execution is delegated.
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] — *2026-06-06*. Appears as "force structure before generation" — analyze, find edge cases, explain tradeoffs, define architecture, propose strategy, THEN generate. "The problem with AI code isn't syntax, it's poor thinking."
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — *2026-06-06*. Echoed in the contracting/settlement separation and in "machines will execute exactly what is encoded and nothing that is merely implied" — terms must be explicit enough for code to enforce.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — *2026-06-06*. The verifier is the execution-as-source-of-truth side: the agent reasons and claims, but an external execution step (re-running tests/build) is authoritative.
- [[wiki/sources/nurijanian-goal-for-product-managers]] — *2026-06-06*. /goal separates the working agent (does the work, surfaces evidence) from the evaluator (judges done-ness from observable proof) — a doing-vs-judging separation analogous to the reasoning/execution split.
- [[wiki/sources/everestchris6-100m-ai-opportunity]] — *2026-06-06*. The concrete-contractor voice agent embodies it: the agent reasons and quotes, but the owner presses 1/2/3 to send/modify/callback — judgment stays human, execution is delegated.

## Sub-claims and details

### When to apply the split

- **Definitely deterministic**: arithmetic, string processing with known schemas, sort/filter/aggregate, format conversions, exact lookups against structured data.
- **Definitely LLM-only**: open-ended writing, creative interpretation, judgment calls, ambiguous tasks where there's no "correct" answer.
- **Hybrid**: the LLM should reason about the task and *call* code for the deterministic part. Most real workflows are hybrid.

### Where the split sits in the agent architecture

In Claude Code's idiom:

- **The [[agentic-loop]]** is reasoning (LLM thinks → decides → tool call).
- **The tool call** is the boundary.
- **The tool's implementation** is the execution side (deterministic code handling the actual work).

This means tools are first-class execution carriers. Designing tools well — clear names, precise descriptions, structured error messages — is the same as designing the execution layer well.

### Composes with [[claude-code-skills]]

A skill that includes executable code is a packaged reasoning + execution unit:

- The skill's metadata + instructions = reasoning context (the LLM reads these to decide when to use the skill).
- The skill's bundled code = execution (the LLM invokes it when the task warrants).

This is why skills are more reliable than equivalent prose-only prompts: the deterministic parts of the workflow are off-loaded from the LLM to code.

### Failure modes

- **LLM as calculator** — asking the model to do arithmetic. Always flaky. Use a calculator tool.
- **LLM as parser** — asking the model to extract structured fields from unstructured input without a schema. Use code with a clear extraction function.
- **Code as judgment-maker** — the inverse failure: hard-coding decisions that should be left to the LLM (e.g. classifying ambiguous customer requests with a regex). Use the LLM with a structured output spec.
- **No clear boundary** — unclear which side is doing what. Diagnose by asking "if the LLM produces a wrong result here, was it a reasoning failure or an execution failure?" If you can't tell, the split is muddy.

## Open questions and contradictions

- **The boundary for "deterministic"** is not always clean. Is "extract the customer's intent from this email" deterministic? Probably not — it requires interpretation. Is "extract every email address from this email" deterministic? Yes — regex.
- **Cost-vs-reliability tradeoff**: invoking code adds a round-trip; for very simple tasks the LLM may produce the right answer faster than a tool call. The split is most valuable when reliability matters more than latency.
- **Cross-language code in skills**: skills in Python, JS, shell, etc. — what happens when the host environment doesn't have the right runtime? Sources don't address.

## Related concepts

- [[claude-code-skills]] — primary delivery mechanism for the split (skills with embedded code).
- [[augmented-llm]] — tools (one of three augmentations) are the execution boundary.
- [[agentic-loop]] — the runtime where reasoning happens; tool calls are where execution begins.
- [[progressive-disclosure]] — composes; deeper context layers can hold code, not just text.
- [[mcp-server]] — MCP-mediated tools are the most common execution carrier in production agents.
- [[ai-os-pattern]] — "boring is beautiful" is this principle stated as operational doctrine.

## Related entities

- [[wiki/entities/anthropic]] — Skills mechanism explicitly supports embedded code.

## Mentioned in

- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — *2026-06-06*. "Tooling > prompting" closing thesis.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — *2026-06-06*. "System around the model" framing.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — *2026-06-06*. Plan-vs-execute across surfaces; one job per chat.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — *2026-06-06*. One LLM call orchestrating many tool calls.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — *2026-06-06*. Consumer agentic-AI instance (reason over intent, act across apps).
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — *2026-06-06*. "The LLM is not a parser. Python is a parser."
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — *2026-06-06*. Knowledge substrate vs per-tool wiring.
- [[wiki/sources/leopardracer-one-person-business-2026-ai]] — *2026-06-06*. Human judgment directs; AI executes.
- [[wiki/sources/tricalt-memory-skills-same-harness]] — *2026-06-06*. Memory (observe) vs skills (execute).
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — *2026-06-06*. Opus-Strategist reasons, Sonnet-Builder executes, QA gate.
- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — *2026-06-06*. Topology-traversal vs data-hydration (loose echo).
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]] — *2026-06-06*. Agents as scoped reasoning units over a spine.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — *2026-06-06*. "Dumb loop where all intelligence lives in the model"; permission enforcement separate from reasoning.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — *2026-06-06*. "AI writes the code. The engineer decides what code should exist."
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] — *2026-06-06*. "Force structure before generation."
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — *2026-06-06*. Encoded-not-implied; contracting/settlement separation.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — *2026-06-06*. Verifier as execution-as-source-of-truth.
- [[wiki/sources/nurijanian-goal-for-product-managers]] — *2026-06-06*. Working agent vs evaluator separation.
- [[wiki/sources/everestchris6-100m-ai-opportunity]] — *2026-06-06*. Voice agent reasons; owner makes the call.
