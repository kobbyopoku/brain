---
type: concept
title: Evaluator-optimizer
created: 2026-06-06
updated: 2026-06-06
aliases: [evaluator-optimizer, evaluator-optimizer loop, self-critique loop]
tags: [agent-workflow-patterns, self-critique, agents, stub]
---

# Evaluator-optimizer

> An agent workflow pattern in which one pass generates output and another critiques it, looping until the critique is satisfied — "forcing the agent to argue with itself." Appears in this wiki via [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]].

## Definition

This is a **stub**. The evaluator-optimizer is one of the named [[agent-workflow-patterns]]: a self-critique loop where a generator produces output and an evaluator judges and pushes for revision. In [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] it appears as "extended critique loops" expressed as a prompt template rather than an orchestration topology — *"force the agent to argue with itself"* — framed as the same self-annealing-at-inference-time idea.

## Treatment across sources

- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] expresses the evaluator-optimizer / self-critique pattern as a prompt template (Pattern 2, extended critique loops), distinct from an orchestration topology.

## Related concepts

- [[agent-workflow-patterns]] — the broader catalog this pattern belongs to.
- [[verification-loops]] — adjacent agent self-checking mechanism.

## Related entities

## Mentioned in

- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]
