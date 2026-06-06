---
type: concept
title: DOE Framework (Directive + Orchestration + Execution)
created: 2026-05-03
updated: 2026-06-06
aliases: [DOE framework, doe-framework, DO framework, directives and executions, directive execution architecture, directive orchestration execution]
tags: [agentic-workflows, ai-automation, architecture, foundational]
---

# DOE Framework (Directive + Orchestration + Execution)

> An architecture for agentic workflows that splits *what* (declarative markdown specifications), *how* (orchestration: planning + routing + failure-handling), and *doing* (deterministic Python scripts / specialized agents). Originally framed as 2-layer **DO** (Directives + Executions) in Saraev's early-2026 course; publicly evolved to **DOE** (3-layer) in late-2025 / 2026 content. The pattern's promise: 2-3% error rates on real business workflows where raw LLM chains decay to 41-65% error rates per [[reliability-decay-math]].

## Filename note

This concept page is filed at `wiki/concepts/do-framework.md` for backward compatibility with prior wikilinks (`[[do-framework]]`). The canonical name is now **DOE Framework**; both `[[do-framework]]` and `[[doe-framework]]` resolve to this page via the aliases.

## Definition

The **DOE framework** has three layers:

- **D — Directive**: declarative markdown files in `directives/`. Captures *intent* — *what* needs to be accomplished and *why*. One file per workflow or capability (e.g. `scrape_leads.md`, `send_onboarding_email.md`, `enrich_company.md`). YAML frontmatter for metadata, markdown body for the spec — inputs, outputs, success criteria, edge cases, definition-of-done. Plain language, no code. *"A good directive captures intent. It doesn't need to say 'go to this URL, click this button, copy this text' — it simply states what needs to be accomplished."* ([[wiki/sources/prakash-bhandari-doe-framework]]).
- **O — Orchestration**: the planning / routing / coordination layer. Reads the directive, decomposes the goal into sub-tasks, decides which executions / agents handle each part and in what order, runs them, observes results, retries on failure, adapts the plan when results come back unexpected. The "brain" — planner + project manager + coordinator rolled into one. Conventionally an LLM, but the framework doesn't mandate which one (Claude / GPT / Gemini / open-weight all work). Runtime contract: **Act → Observe → Think → Act** loop.
- **E — Execution**: deterministic scripts / specialized agents in `executions/`. Each does one well-defined thing reliably (read a sheet, call an API, parse a CSV, send an email). Typically Python; the language is incidental. Idempotent, modular, testable. Returns structured output for the orchestrator to consume.

A directive without an orchestrator is just a prompt. An orchestrator without executions is just a chatbot. An execution without a directive is just code. The DOE framework is the **separation** that makes the system reliable — and makes each layer **independently improvable**.

## Why it matters

Pure-LLM workflows fail in production because [[reliability-decay-math|chained probabilities decay multiplicatively]]: 5 sequential 90%-success steps = 59% total. The DOE framework's contribution is to keep the LLM bounded to roles where 90% accuracy is fine (orchestration, decision-routing, error-interpretation) while moving deterministic operations (sorting, parsing, API calls, calculations) to code where reliability is 100%.

This is the architectural answer to the [[reasoning-execution-split]] principle: *LLMs reason, deterministic code executes*. The DOE framework operationalizes the principle into a folder layout an agent can navigate.

For [[ai-automation-services]] specifically, the framework is what enables the economics. If your client's "monthly reporting workflow" is 10 steps and you're running raw-LLM, you're shipping ~35% reliability. With DOE, you can claim 97-98% — the difference between a $5,000 build that works and a refund.

## Framing evolution: DO → DOE

The framework's public name and layer-count shifted between Saraev's early-2026 course (the canonical wiki source) and his late-2025 / 2026 follow-up content:

| | DO (early 2026, [[wiki/sources/saraev-agentic-workflows-2026|original course]]) | DOE (late 2025 / 2026, follow-up content) |
|---|---|---|
| **Layer count** | 2 | 3 |
| **D** | Directive | Directive (unchanged in spirit) |
| **O** | "Executions" — Saraev's *artifact-named* layer | **Orchestration** — *role-named*, first-class |
| **E** | (collapsed into D + implicit LLM-orchestrator) | Execution — *role-named*, first-class |
| **Orchestrator's status** | implicit (the LLM that runs) | first-class layer with its own concerns: planning, routing, failure-handling, retry, adaptation |
| **Self-annealing** | implicit (4-step error recovery loop) | named explicitly as a system property — see [[self-annealing]] |

The architecture didn't change — the *naming* did. Both framings describe the same separation-of-concerns pattern. DOE is more pedagogically clear: by promoting orchestration to a first-class named layer, beginners can locate "the brain" in the architecture instead of having it disappear into the LLM. DOE is also more accurate as systems scale — orchestration genuinely deserves its own named concerns once you're handling failure-modes, retry-policies, and plan-adaptation programmatically.

For wiki citations: prefer **DOE Framework** as the canonical name when writing new content. Existing references to `[[do-framework]]` continue to resolve here via aliases.

## Treatment across sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — canonical wiki source for the 2-layer DO framing. Coined and demonstrated extensively across the 5h+ course. Saraev's framing: *"All DO does is reduce [the range of possible outcomes] so it's a lot more narrow. ... This lets me get to 2 to 3% error rates on a lot of business functions."*
- [[wiki/sources/prakash-bhandari-doe-framework]] — *2025-2026*. Cleanest expository treatment of the 3-layer DOE framing. Adds the *"Act → Observe → Think → Act"* runtime loop as orchestration's contract. Uses a travel-booking worked example: directives ("find flights under $2,000") flow through orchestration (search / filter / check-calendar / book) into execution (API calls with observation-based adjustments).
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]] — *2025-2026*. LinkedIn post that surfaced the DOE framing for this wiki (via Kobby's question). Derivative — paraphrases Saraev's late-2025/2026 content. Notable additions: explicit comparison with [[wiki/entities/n8n|n8n]] / Make ("you're no longer the orchestrator — the agent handles routing autonomously") and naming **self-annealing** as a system-level outcome.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — adjacent: regent0x_'s 5-role subagent setup (architect/coder/reviewer/tester/ops) is a similar separation-of-concerns move at a different scope (per-task instead of per-workflow).
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — adjacent: nateherk's `.claude/skills/` + reference files structure is a similar but more general-purpose layout. DOE is more opinionated; AI OS template is broader.
- [[wiki/sources/nousresearch-hermes-agent]] — adjacent: Hermes Agent's "self-improving learning loop" is the *agent-internal* version of DOE's [[self-annealing|self-annealing]] property — same goal (systems get better over time without ongoing intervention) via different mechanism (agent-managed state vs file-managed directives).
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] frames it as the AI-automation learning path: Saraev's directive → orchestration → execution. Points to Saraev's free 6-hour course as the canonical resource.
- [[wiki/sources/cyrilxbt-personal-operating-system]] frames it as the spine of the Queue Processor: the `VERB-topic.md` filename convention encodes trigger + prompt + output via file naming, and the five workflows are DOE Directive (prompt) + Orchestration (N8N cron) + Execution (Claude).
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] frames it motivationally: *"the valuable skill is shifting from execution → orchestration"* — DOE's Directive/Orchestration/Execution split stated as prose rather than architecture.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] arrives at the same decomposition independently: Saboo's role triad maps onto DOE — Orchestrator ≈ Orchestration, Builder+Reviewer ≈ Execution, the `/goal` text ≈ Directive.
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]] frames it implicitly: each Adaptive agent is a trigger + prompt + output unit, and the plan is DOE composition across four agents though the source never uses the term.

## Sub-claims and details

### Folder layout

```
workspace/
├── directives/                       # D — declarative markdown specs
│   ├── scrape_leads.md
│   ├── enrich_company.md
│   ├── send_onboarding_email.md
│   └── new_client_workflow.md       # composes the above
├── executions/                       # E — deterministic Python / specialized agents
│   ├── google_sheets.py
│   ├── http_client.py
│   ├── email_sender.py
│   └── csv_parser.py
└── CLAUDE.md                         # the orchestrator's contract — "how the layout works"
```

The orchestration layer (O) doesn't have a folder of its own — it lives in the LLM and the orchestrator-contract file (CLAUDE.md / AGENTS.md / SKILL.md). This is a useful detail: in a DOE filesystem, two folders contain artifacts; the third layer is *runtime behavior* the orchestrator-contract describes.

### Directive shape (per Saraev's demo)

- YAML frontmatter: `name`, `description`, `inputs`, `outputs`, `tags`, `definition_of_done`.
- Body: numbered steps in plain English, each step potentially calling a named execution script.
- Edge cases and error handling described inline.
- Length: one directive to one workflow. Don't make a "run business" directive that does everything.

### Orchestration runtime contract (Act → Observe → Think → Act loop)

The DOE framing makes orchestration's runtime explicit:

1. **Act** — execute the next planned step (call an execution).
2. **Observe** — read the execution's structured output (success / failure / unexpected result).
3. **Think** — interpret: did this match expectations? Is the plan still on-track? Do we need to retry / re-route / abort / re-prompt?
4. **Act** — execute the next step based on the updated understanding.

Loops until directive-success or unfixable wall. Distinct from a hardcoded waterfall (n8n, Make) where the route is decided up-front and any deviation breaks the workflow.

### Execution shape

- One script per well-defined operation.
- Idempotent where possible.
- Returns structured output (JSON or named values) for the orchestrator to consume.
- Errors raised explicitly so the orchestrator can decide next steps.

### Composition

- A complex workflow (e.g. "new client onboarding") is itself a directive that references other directives. *"Just chain all of the existing capabilities together."*
- This avoids the "giant monolithic directive" anti-pattern, where a single directive tries to do everything and the orchestrator gets confused.

### Self-annealing — the system-level property

DOE systems improve themselves over time without ongoing intervention. The orchestrator's 4-step error-recovery loop (run → diagnose → fix → update directive/execution) accumulates fixes into the directives themselves. After enough runs, the system has *encoded* its own failure modes into the directives. See [[self-annealing]] for the canonical wiki concept page.

### Stochasticity bounding

Because the LLM (in the orchestration layer) is composing deterministic units, the search space the model operates in is small ("which directive applies?", "did this execution succeed?"). Long autonomous runs that would otherwise drift get bounded by the framework's structure.

### Filename-as-directive encoding

The Queue Processor's `VERB-topic.md` filename convention encodes a directive's trigger, prompt, and output through the filename itself ([[wiki/sources/cyrilxbt-personal-operating-system]]) — a compact instance of the directive layer where the file's *name* carries the DOE metadata rather than YAML frontmatter.

### Independent rediscoveries of the decomposition

Several sources arrive at the same three-way split without using the DOE vocabulary: Saboo's Orchestrator / Builder+Reviewer / `/goal`-text triad ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]) and 8xgrowth's four-agent trigger+prompt+output composition ([[wiki/sources/8xgrowth-100-days-to-10k-clipping]]) both map cleanly onto Directive / Orchestration / Execution. The convergence is evidence the decomposition is a natural attractor for agentic-workflow design rather than a single author's idiosyncrasy.

## Open questions and contradictions

- **Versioning**: a directive that worked last month may fail this month if the underlying APIs change. No versioning convention captured. Worth tracking when next ingest covers this.
- **Multi-tenant directives**: when the same workflow needs to run for many clients with different parameters, where does the per-client config live? Saraev shows examples but doesn't fully systematize.
- **Cross-language executions**: framework is shown with Python; language is incidental. Composing JS + Python + shell executions in one workflow is mentioned but not demonstrated end-to-end.
- **DOE vs AI OS** (nateherk): both are folder-shaped agent contracts. DOE is more workflow-specific (one directive per repeatable task); AI OS is broader (contexts + skills + decisions + references). DOE might be the *delivery surface* of an AI OS — workflows the OS exposes to the user.
- **DOE in regulated domains** (healthcare, finance): the 2-3% error rate is impressive but still 1-in-50. For PHI workflows in [[wiki/projects/vedge|Vedge]], that may be too high. Worth thinking through when the framework is applied to clinical data.
- **Orchestration-as-first-class implication**: if orchestration genuinely deserves its own layer, it should also have its own *artifacts* (orchestration policies, retry-rules, plan-templates) — but Saraev's repos don't show explicit `orchestration/` folders. The layer-as-runtime-only is a soft inconsistency in the 3-layer framing worth tracking.

## Related concepts

- [[reasoning-execution-split]] — the underlying principle the DOE framework operationalizes.
- [[reliability-decay-math]] — the math that motivates the framework.
- [[horizontal-leverage]] — the economic thesis the framework enables at scale.
- [[self-annealing]] — the system-level property DOE produces over time.
- [[ai-automation-services]] — the business model the framework underpins.
- [[services-as-software]] — Vacca's variant; DOE is a candidate "delivery layer" inside this model.
- [[markdown-as-agent-contract]] — directives are an instance of this meta-pattern.
- [[claude-code-skills]] — adjacent but distinct: skills are platform-level invokable capabilities; directives are workflow-level orchestration specs.
- [[agent-workflow-patterns]] — the DOE framework most resembles "orchestrator-workers" with deterministic workers.
- [[hot-cache]] — adjacent: an external mechanism for the same self-improvement goal that DOE achieves via directive-update loops.

## Related entities

- [[wiki/entities/nick-saraev]] — coiner of both DO and DOE framings.
- [[wiki/entities/prakash-bhandari]] — author of the cleanest 3-layer DOE expository.
- [[wiki/entities/bob-mwathu]] — derivative content creator who surfaced DOE for this wiki.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]
- [[wiki/sources/prakash-bhandari-doe-framework]]
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]]
- [[wiki/sources/exploraX_-5-solo-ai-business-models]]
- [[wiki/sources/cyrilxbt-personal-operating-system]]
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]]
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]]
