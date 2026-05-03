---
type: concept
title: Reliability Decay Math
created: 2026-05-03
updated: 2026-05-03
aliases: [chained probability decay, reliability multiplication, multi-step reliability]
tags: [agentic-workflows, reliability, math, foundational]
---

# Reliability Decay Math

> The mathematical observation that chained probabilistic steps decay multiplicatively: five sequential 90%-success steps produce a 59% total success rate, not 90%. This is the core technical constraint that makes raw LLM chains unreliable for multi-step business processes — and the case for the [[do-framework]].

## Definition

Given *N* sequential steps each with independent success probability *p*, the total workflow success rate is *p^N*. For LLM-driven workflows where each call succeeds at 90% reliability:

| Steps | Total reliability |
|---:|---:|
| 1 | 90.0% |
| 2 | 81.0% |
| 3 | 72.9% |
| 5 | 59.0% |
| 7 | 47.8% |
| 10 | 34.9% |
| 15 | 20.6% |
| 20 | 12.2% |

By 5 steps, the workflow fails more often than not. By 10 steps, it succeeds only 1/3 of the time. Real business processes routinely involve 10-20 LLM calls in sequence.

## Why it matters

This single observation explains most of why production AI agents fail in ways that demos suggest they shouldn't. Demos are typically 1-3 steps, where 90% reliability looks good. Production workflows are 10-20 steps, where the same per-step reliability looks catastrophic.

It is also the mathematical case for why [[do-framework]] (and analogous separation-of-concerns architectures) actually work. By moving deterministic operations to code (100% reliability for the deterministic-able subset), the *N* in *p^N* gets smaller — only the genuinely-LLM steps count toward the chain.

For builders of [[ai-automation-services]], this is the difference between shipping something a client uses repeatedly and shipping something the client abandons after week 2.

## Treatment across sources

- [[wiki/sources/saraev-agentic-workflows-2026]] — canonical wiki source. *"If you have 90% success for step 1 times 90% for step 2 ... you don't end up with a 90% success rate across the entire process. You end up with a 59% success rate."* Used as the core motivation for the DO framework.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — adjacent: hooeem's "workflows vs. agents" distinction is a response to the same problem. Workflows have deterministic steps that don't decay; agents inherit the chained-probability problem.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — orthogonal but related: Mnilax measures *cost* decay (overhead %). Saraev describes *reliability* decay. Both are silent failures that compound across long-running sessions.

## Sub-claims and details

### The independence assumption (and where it breaks)
The math assumes independent step probabilities. In real LLM chains, errors are *correlated*:
- A misunderstanding in step 1 propagates to steps 2-N (worse than independent).
- Some errors are recoverable mid-chain (better than independent if the agent retries).

In practice, the multiplicative model is approximately right for naive LLM chains and approximately wrong for systems with retry/recovery loops. The DO framework's 4-step error-recovery loop (run → diagnose → fix → update) deliberately exploits this — it converts a multiplicative-decay chain into a retry-bounded chain where reliability becomes *p_retry^max_retries*, much higher than *p^N*.

### What raises *p* (the per-step success rate)
- Tighter prompts with explicit success criteria.
- Smaller, more-bounded tasks per step.
- Structured outputs (JSON schemas) instead of free text.
- Few-shot examples for ambiguous decisions.
- Better models (Sonnet > Haiku for reasoning-heavy steps).

### What lowers *N* (the chain length)
- The DO framework: deterministic operations are off-loaded to code, leaving only LLM-grade decisions in the chain.
- Composition: chain *workflows* (which already have internal reliability) instead of individual LLM calls.
- Caching: previously-correct outputs don't need to be re-derived.

### What the math implies for design
- **Build short LLM chains.** If your workflow is 20 LLM calls, can it be 5 LLM calls + 15 code calls? Almost always yes.
- **Insert checkpoints.** A "verify the previous step succeeded" node every 3-5 steps converts a long fragile chain into multiple shorter robust ones.
- **Plan for graceful recovery, not perfect prevention.** (Saraev's line.) Even with the math working in your favor, things will fail. Loops > linear chains.
- **Don't let the agent "just do the whole thing."** Single-prompt requests for complex workflows are 20-step chains in disguise — the model is doing them internally and decaying anyway.

### Why demos lie
Most public LLM-agent demos are 2-3 steps. At 90% × 90% × 90% = 73%, demos look broadly reliable. Real workflows hidden in client deliveries are 10-20 steps and quietly fail half the time. **The reliability ceiling for raw-LLM agents is lower than every demo suggests.**

## Open questions and contradictions

- **The 90% per-step number is itself approximate.** Modern frontier models are higher (95-98%) on simple tasks; 90% is a conservative working number for typical LLM steps. The math becomes less alarming with stronger models — at 95%, 10 steps = 60% (still bad but less catastrophic).
- **What's the *p* for a deterministic Python script?** ~99.9%+ (only fails on infrastructure errors). The asymmetry between LLM steps and code steps is what makes the DO framework work.
- **Is decay always multiplicative?** Not if steps recover errors. The frontier of agent reliability research is about converting multiplicative decay into something better — error-correcting codes for LLM chains.
- **Can the math be presented to non-technical clients?** The 90% × 90% = 81% framing is intuitive; the *p^N* generalization may not be. Worth packaging as a sales argument for [[ai-automation-services]] businesses explaining why their DO-framework-based workflows are worth more than competitors' raw-prompt versions.

## Related concepts

- [[do-framework]] — the architectural answer to this problem.
- [[reasoning-execution-split]] — the underlying principle.
- [[agent-workflow-patterns]] — five Anthropic patterns include several (evaluator-optimizer, prompt-chaining-with-gates) that explicitly address chain-decay.
- [[horizontal-leverage]] — the economic argument that depends on this math being solvable.
- [[ai-automation-services]] — the business model whose pricing depends on solving the reliability problem.

## Related entities

- [[wiki/entities/nick-saraev]] — articulator of this framing.

## Mentioned in

- [[wiki/sources/saraev-agentic-workflows-2026]]
