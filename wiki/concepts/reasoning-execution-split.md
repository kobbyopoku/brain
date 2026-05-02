---
type: concept
title: Reasoning + Execution Split
created: 2026-05-02
updated: 2026-05-02
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
