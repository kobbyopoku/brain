---
type: concept
title: Self-Annealing
created: 2026-05-05
updated: 2026-05-05
aliases: [self-annealing, self-annealing systems, self-improving workflows]
tags: [agentic-workflows, self-improvement, reliability, doe-framework]
---

# Self-Annealing

> A system-level property of [[doe-framework|DOE-framework]] agentic workflows: the system progressively encodes its own failure-modes into its directives over time, getting more reliable per-run without ongoing human intervention. Coined by [[wiki/entities/nick-saraev|Nick Saraev]] (borrowed from metallurgy: *annealing* hardens metal by working it through repeated heat-stress cycles).

## Definition

**Self-annealing** describes the way a [[doe-framework|DOE-framework]] system's reliability *increases* with use rather than degrading. The mechanism:

1. The orchestrator runs a directive.
2. An execution fails — bad input format, unexpected API response, edge case the directive didn't anticipate.
3. The orchestrator's error-recovery loop (run → diagnose → fix → **update**) doesn't just fix the immediate run — it *writes the fix back* into the directive or execution.
4. The next time this scenario occurs, the directive already accounts for it. No re-fix needed.

The system *anneals* — the workflow gets harder, more refined, more failure-resistant the more it's run. Distinct from generic "AI improvement" because the improvement happens at the **directive layer** (durable markdown files in version control) rather than in model weights (which are static unless retrained) or in conversation context (which evaporates between sessions).

## Why it matters

Three properties make self-annealing distinct from neighboring claims:

1. **It's structural, not learned.** Self-annealing doesn't require model training, fine-tuning, or RLHF. It works because the [[doe-framework]]'s directive layer is *editable markdown* — every fix the orchestrator makes is a first-class commit to the workflow's source-of-truth.
2. **It's local-first and version-controlled.** Improvements live in the user's directive files (in their git repo) rather than in a vendor's hosted service. Roll back a bad directive update via `git revert`. Audit what changed via `git log`.
3. **It compounds across model upgrades.** When the LLM behind the orchestrator improves (e.g. Claude 4.6 → 4.7 → 5.x), the directives don't have to be rewritten — they're already the *human-readable record* of what the workflow does. The new model just executes them better.

This is the architectural answer to *"why doesn't my agentic workflow get better over time?"* — because most agentic workflows have no place to *put* the improvement. Self-annealing requires DOE-style directive-as-source-of-truth.

## Treatment across sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — the canonical wiki source. Saraev demonstrates the 4-step error-recovery loop (run → diagnose → fix → update) but doesn't use the term *self-annealing* explicitly in the original course — it appears in his follow-up content.
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]] — *2025-2026*. First wiki source to explicitly cite the term. *"Systems that can self-improve over time (what Nick calls self-annealing)."*
- [[wiki/sources/prakash-bhandari-doe-framework]] — *2025-2026*. Doesn't use the *self-annealing* term but describes the underlying mechanism via the *"Act → Observe → Think → Act"* loop with explicit *"adapts the plan when results come back unexpected"*.

## Sub-claims and details

### The metallurgical metaphor

In metallurgy, **annealing** is heating a metal then cooling it slowly to relieve internal stresses and increase ductility. The metal *gets stronger and more workable* through repeated stress cycles. The metaphor for agentic workflows:

- **Heat** = a real production run with real edge cases hitting the workflow.
- **Stress** = an execution failure — the workflow didn't account for this case.
- **Cooling** = the orchestrator's error-recovery loop fixing the directive *after* the failure is understood.
- **Hardening** = the directive now accounts for this case forever; future runs don't fail this way.

The loop runs continuously in production, and the directive set converges toward a robust spec.

### How it differs from RLHF / fine-tuning

| Mechanism | Where the improvement lives | Speed of feedback | Auditability | Cross-model portability |
|---|---|---|---|---|
| **RLHF / fine-tuning** | Model weights | Slow (training cycles) | Low (weights are opaque) | Zero (weights are model-specific) |
| **Hot-cache** ([[hot-cache]]) | External markdown file | Per-session | High (markdown diff) | High (any model can read) |
| **Self-annealing** | Directive markdown files | Per-run | High (git history of directive changes) | High (any model can execute the directive) |
| **Hermes self-improving loop** ([[wiki/entities/hermes-agent]]) | Agent-internal state | Per-session | Lower (internal state) | Bound to Hermes |

Self-annealing sits in the same family as hot-cache and Hermes's self-improving loop — all three solve *"the agent gets better over time across sessions"*. They differ on *where* the improvement is encoded.

### Failure modes

- **Bad fixes encoded.** If the orchestrator misdiagnoses a one-off failure as a structural problem, it bakes a wrong fix into the directive. Future runs may misbehave per the bad fix. Mitigation: the directive update should be a separate *commit* the human can review.
- **Fix-thrashing.** Two contradictory fixes being added and reverted on alternating runs. Sign of a non-deterministic execution that the orchestrator is mistaking for a directive problem. Diagnose the execution layer, not the directive.
- **Unbounded growth.** A long-lived directive accumulates so many edge-case clauses it becomes unreadable. Mitigation: periodic refactoring — collapse 10 edge cases into one general clause when the pattern emerges.
- **Loss of the "annealing" property when humans edit directly.** If a human edits a directive *during* a run, the orchestrator's expected world-state diverges from reality. Mitigation: directive edits happen between runs, not during.

### Self-annealing vs continuous deployment

Both produce systems that improve over time but at different layers. CD is *engineering organization* improving the *codebase* via human-decided changes pushed to production. Self-annealing is *the system itself* improving its *directives* via orchestrator-decided changes accumulated through use. The two compose: CD-deployed orchestrator runs through self-annealing directive cycles; the engineering team can also commit human directives.

## Open questions

- **Convergence proof**: does a self-annealing directive set provably converge to a stable spec? Or can it oscillate forever? No formal analysis ingested. The empirical claim from Saraev is "it converges in practice."
- **Multi-tenant self-annealing**: when 10 clients run the same directive with slightly different inputs, fixes encoded for client A may not generalize to client B. How does self-annealing scale across tenants? Saraev's content doesn't address this.
- **Auditing the auditor**: who reviews the orchestrator's directive updates? In production, an LLM-driven directive-edit committed without human review is a real deployment surface. Worth a governance pattern.
- **Vedge implication**: self-annealing in clinical workflows ([[wiki/projects/vedge|Vedge]]'s billing audit / NHIS claims) carries the same risk as automated medication-dosing changes — the agent's "fix" might be wrong and the wrong fix becomes durable. Self-annealing is the wrong default for clinical-decision-support workflows; better as opt-in with human-review-gated commits.

## Related concepts

- [[doe-framework]] — the architecture self-annealing emerges from.
- [[reasoning-execution-split]] — the underlying separation that makes encoded fixes durable.
- [[reliability-decay-math]] — the math that explains why self-annealing matters: a 90%-per-step workflow needs continuous fix-encoding to stay above 90% as it grows.
- [[hot-cache]] — sibling pattern: external markdown the agent re-reads each session. Hot-cache is *manually* curated; self-annealing is *agent-curated*.
- [[llm-wiki-pattern]] — the wiki itself anneals via human + LLM cycles; same goal at the personal-knowledge layer.
- [[claude-code-skills]] — adjacent: skills can be self-annealed too if the agent updates them between runs.
- [[markdown-as-agent-contract]] — directives are the agent contract that gets annealed.

## Related entities

- [[wiki/entities/nick-saraev]] — coiner.
- [[wiki/entities/hermes-agent]] — agent-internal sibling mechanism.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]
- [[wiki/sources/bob-mwathu-doe-framework-linkedin]]
- [[wiki/sources/prakash-bhandari-doe-framework]]
