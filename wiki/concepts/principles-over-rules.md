---
type: concept
title: Principles over rules
created: 2026-06-06
updated: 2026-06-06
aliases: [rules overfit, principles transfer]
tags: [agents, agent-skills, design]
---

# Principles over rules

> The thesis that durable, general principles transfer to unseen situations whereas case-by-case rules overfit — applied to authoring agent skills so they stay robust rather than brittle and bloated.

## Definition

**Principles over rules** is the load-bearing thesis of [[wiki/sources/petradonka-agents-need-feedback-loops]]: enumerating case-by-case rules makes agent skills brittle and bloated, while durable principles transfer to situations the author never anticipated. The source's compression of the idea is *"rules overfit and principles transfer."* Example principles given are *"Be helpful, not defensive"* and *"lead with empathy, not a pitch."*

## Why it matters

For judgement-heavy agent work, an instruction set built from exhaustive rules cannot anticipate every situation and grows unwieldy as edge cases accumulate. Framing the agent's guidance as principles lets it generalize to novel situations and keeps the instruction set compact — directly tied to the source's broader argument that the engineering problem is the feedback loop, not the prompt.

## Treatment across sources

- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it as the source's load-bearing thesis: enumerating case-by-case rules makes agent skills brittle and bloated; durable principles (*"Be helpful, not defensive"*, *"lead with empathy, not a pitch"*) transfer to unseen situations. *"Rules overfit and principles transfer."*

## Sub-claims and details

- Case-by-case rules make agent skills brittle and bloated. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- Durable principles transfer to situations not seen at authoring time. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- Example principles: *"Be helpful, not defensive"*; *"lead with empathy, not a pitch."* (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- Compressed statement: *"Rules overfit and principles transfer."* (per [[wiki/sources/petradonka-agents-need-feedback-loops]])

## Open questions and contradictions

- (none surfaced by current sources)

## Related concepts

- [[agent-feedback-loop]] — the same source argues the loop, not the prompt, is the engineering problem.
- [[skills-as-code]] — where the principles live and how they are revised under governance.

## Related entities

- [[wiki/entities/petra-donka]]

## Mentioned in

- [[wiki/sources/petradonka-agents-need-feedback-loops]]
