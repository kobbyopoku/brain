---
type: concept
title: DO Framework (Directives + Executions)
created: 2026-05-03
updated: 2026-05-03
aliases: [DO framework, directives and executions, directive execution architecture]
tags: [agentic-workflows, ai-automation, architecture, foundational]
---

# DO Framework (Directives + Executions)

> An architecture for agentic workflows that splits *what* (declarative markdown specifications) from *how* (deterministic Python scripts), with the LLM acting only as orchestrator between them. The pattern's promise: 2-3% error rates on real business workflows where raw LLM chains decay to 41-65% error rates per [[reliability-decay-math]].

## Definition

The **DO framework** has two layers:

- **D — Directives**: declarative markdown files in `directives/`. One file per workflow or capability (e.g. `scrape_leads.md`, `send_onboarding_email.md`, `enrich_company.md`). Each directive describes *what* the workflow does — its inputs, outputs, success criteria, edge cases — not how it does it. YAML frontmatter for metadata, markdown body for the spec.
- **O — Executions**: deterministic scripts in `executions/`. Typically Python; the language is incidental. Each script does one well-defined thing reliably (read a sheet, call an API, parse a CSV, send an email). Idempotent, modular, testable.

The LLM (the orchestrator) reads the directive when invoked, identifies which executions to call, runs them, handles outputs, retries on errors. It never *replaces* the executions — it composes them.

A directive without an execution is just a prompt. An execution without a directive is just code. The DO framework is the *separation* that makes the system reliable.

## Why it matters

Pure-LLM workflows fail in production because [[reliability-decay-math|chained probabilities decay multiplicatively]]: 5 sequential 90%-success steps = 59% total. The DO framework's contribution is to keep the LLM bounded to roles where 90% accuracy is fine (orchestration, decision-routing, error-interpretation) while moving deterministic operations (sorting, parsing, API calls, calculations) to code where reliability is 100%.

This is the architectural answer to the [[reasoning-execution-split]] principle: *LLMs reason, deterministic code executes*. The DO framework operationalizes the principle into a folder layout an agent can navigate.

For [[ai-automation-services]] specifically, the framework is what enables the economics. If your client's "monthly reporting workflow" is 10 steps and you're running raw-LLM, you're shipping ~35% reliability. With DO, you can claim 97-98% — which is the difference between a $5,000 build that works and a refund.

## Treatment across sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — canonical wiki source. Coined and demonstrated extensively across the 5h+ course. Saraev's framing: *"All DO does is reduce [the range of possible outcomes] so it's a lot more narrow. ... This lets me get to 2 to 3% error rates on a lot of business functions."*
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — adjacent: regent0x_'s 5-role subagent setup (architect/coder/reviewer/tester/ops) is a similar separation-of-concerns move at a different scope (per-task instead of per-workflow).
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — adjacent: nateherk's `.claude/skills/` + reference files structure is a similar but more general-purpose layout. DO is more opinionated; AI OS template is broader.

## Sub-claims and details

### Folder layout
```
workspace/
├── directives/
│   ├── scrape_leads.md
│   ├── enrich_company.md
│   ├── send_onboarding_email.md
│   └── new_client_workflow.md      # composes the above
├── executions/
│   ├── google_sheets.py
│   ├── http_client.py
│   ├── email_sender.py
│   └── csv_parser.py
└── CLAUDE.md                         # tells the agent how the layout works
```

### Directive shape (per Saraev's demo)
- YAML frontmatter: `name`, `description`, `inputs`, `outputs`, `tags`.
- Body: numbered steps in plain English, each step potentially calling a named execution script.
- Edge cases and error handling described inline.
- Length: keep one directive to one workflow. Don't make a "run business" directive that does everything.

### Execution shape
- One script per well-defined operation.
- Idempotent where possible.
- Returns structured output (JSON or named values) for the orchestrator to consume.
- Errors raised explicitly so the orchestrator can decide next steps.

### Composition
- A complex workflow (e.g. "new client onboarding") is itself a directive that references other directives. *"Just chain all of the existing capabilities together."*
- This avoids the "giant monolithic directive" anti-pattern, where a single directive tries to do everything and the orchestrator gets confused.

### Error recovery loop (4-step)
The framework specifies the agent's behavior on execution failure:
1. **Run** the execution.
2. **Diagnose** the error (read the message, the inputs, the context).
3. **Fix** the call (different inputs, different sequence, different execution).
4. **Update** the directive or execution if the fix should persist.

Loops until success or unfixable wall. *"This way your system continuously optimizes itself without any form of ongoing intervention."*

### Stochasticity bounding
Because the LLM is only orchestrating between deterministic units, the search space the model operates in is small ("which directive applies?", "did this execution succeed?"). Long autonomous runs that would otherwise drift get bounded by the framework's structure.

## Open questions and contradictions

- **Versioning**: a directive that worked last month may fail this month if the underlying APIs change. No versioning convention captured. Worth tracking when next ingest covers this.
- **Multi-tenant directives**: when the same workflow needs to run for many clients with different parameters, where does the per-client config live? Saraev shows examples but doesn't fully systematize.
- **Cross-language executions**: framework is shown with Python; Saraev says language is incidental. Composing JS + Python + shell executions in one workflow is mentioned but not demonstrated end-to-end.
- **DO vs AI OS** (nateherk): both are folder-shaped agent contracts. DO is more workflow-specific (one directive per repeatable task); AI OS is broader (contexts + skills + decisions + references). DO might be the *delivery surface* of an AI OS — workflows the OS exposes to the user.
- **DO framework in regulated domains** (healthcare, finance): the 2-3% error rate is impressive but still 1-in-50. For PHI workflows in [[wiki/projects/vedge|Vedge]], that may be too high. Worth thinking through when the framework is applied to clinical data.

## Related concepts

- [[reasoning-execution-split]] — the underlying principle the DO framework operationalizes.
- [[reliability-decay-math]] — the math that motivates the framework.
- [[horizontal-leverage]] — the economic thesis the framework enables at scale.
- [[ai-automation-services]] — the business model the framework underpins.
- [[services-as-software]] — Vacca's variant; DO is a candidate "delivery layer" inside this model.
- [[markdown-as-agent-contract]] — directives are an instance of this meta-pattern.
- [[claude-code-skills]] — adjacent but distinct: skills are platform-level invokable capabilities; directives are workflow-level orchestration specs.
- [[agent-workflow-patterns]] — the DO framework most resembles "orchestrator-workers" with deterministic workers.

## Related entities

- [[wiki/entities/nick-saraev]] — coiner.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]
