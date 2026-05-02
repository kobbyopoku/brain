---
type: concept
title: Progressive Disclosure
created: 2026-05-02
updated: 2026-05-02
aliases: [progressive context loading, three-level skill loading]
tags: [claude-code, agent-architecture, optimization]
---

# Progressive Disclosure

> An architectural pattern for agent context: don't load everything upfront — load metadata first, then drill into content only when relevant. Reframes the LLM context window from a *limitation* into a *navigation problem*.

## Definition

**Progressive disclosure** is the principle that an agent should consume context in layers of increasing detail, starting with cheap metadata and expanding into expensive content only when the metadata indicates relevance. The pattern is most clearly instantiated in Anthropic's [[claude-code-skills|Agent Skills]] — the agent scans all skill front matter (~100 tokens per skill), picks the relevant one, loads its full SKILL.md, and pulls in reference files only when the task warrants depth.

The pattern generalizes beyond skills. Anywhere an agent has to choose between many possible context sources, the same three-level shape applies: metadata-then-summary-then-full.

## Why it matters

The naive answer to "agent isn't using the right knowledge" is **more context**: more prompts, more examples, more instructions stuffed into the window. That approach hits hard limits — token budgets, attention dilution, recency bias, cost. Progressive disclosure flips the framing: the agent doesn't need to *hold* everything; it needs to *find* the right thing.

The reframe matters because it makes context architecture a *navigation* problem, which is solvable. Humans don't memorize manuals — we navigate them. Designing skills, references, and contexts so the agent can navigate them the same way is what makes agent setups scale beyond toy size without blowing the context window.

It is also the **architectural answer** to several patterns in [[claude-code-overhead-patterns]]:

- Pattern #5 (skill loading on irrelevant tasks) — solved by metadata-first activation.
- Pattern #6 ("just in case" tool definitions) — solved by per-task tool inclusion.
- Pattern #1 (CLAUDE.md bloat) — partially solved by extracting infrequently-used rules into reference docs.

## Treatment across sources

- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — canonical wiki source for the architectural framing. Names progressive disclosure as the conceptual unlock and contrasts it with the "more context = better outputs" approach. Frames the context window as a navigation problem, not a capacity limit.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — independently arrives at the same three-level model in operational language:
  - Level 1: scan all skill front matter (~100 tokens per skill). Cheap.
  - Level 2: load the full skill.md if Claude picks one (~couple thousand tokens).
  - Level 3: only pull reference files when the task actually needs them.
  Author's design rule: skill.md stays under 500 lines; reference docs are separate.

## Sub-claims and details

- **Metadata is the activation contract.** A skill's `name` and `description` (top of SKILL.md) are how the agent decides whether to use the skill. Bad descriptions = bad activation = either over-loading (wastes tokens) or under-loading (skill never fires).
- **The three levels by token cost** (per nateherk):
  - L1: ~100 tokens per skill (front matter only). Always loaded.
  - L2: ~couple thousand tokens. Loaded when L1 metadata matches the task.
  - L3: heavy reference files (often 5-20k+ tokens). Loaded when L2 instructions point at them.
- **Skill-md size discipline** (nateherk): SKILL.md should stay under 500 lines. Heavy content goes in `references/` files. This keeps L2 cheap.
- **The pattern composes with [[reasoning-execution-split]]**: L3 might include executable code, not just reference text. The agent decides *when* to invoke the deeper layer; the layer's contents (code or text) determine *how* the work gets done.
- **Failure modes**:
  - **Over-eager activation** — descriptions too broad → skill loads when not relevant → pattern #5 in [[claude-code-overhead-patterns]].
  - **Under-eager activation** — descriptions too narrow → skill never fires → user types instructions manually → net negative.
  - **Layer coupling** — L2 references too many L3 files → agent fans out into excessive reference reads → undermines the cost gain.

## Open questions and contradictions

- **How many levels are right?** Three is the empirical default, but more or fewer might be better for specific domains. Documentation systems sometimes use 4-5 layers (TOC → chapter → section → paragraph → footnote).
- **What about cross-skill discovery?** L1 metadata sees only its own skill. If two skills together would solve a task, but neither's L1 strongly matches, the activation gates may both stay closed. Composition discovery is unsolved.
- **Update friction**: the metadata description is critical and probably needs updating as skill behavior evolves. No good tooling for "your description has drifted from your skill content" as of current sources.

## Related concepts

- [[claude-code-skills]] — primary instance of the pattern.
- [[claude-code-overhead-patterns]] — overhead patterns this concept is the architectural answer to.
- [[reasoning-execution-split]] — composes with progressive disclosure (deeper layers can hold code).
- [[hot-cache]] — adjacent: a pre-computed top-level summary that reduces L1 navigation cost.
- [[skill-md]] — the file format the pattern operates on.
- [[markdown-as-agent-contract]] — broader meta-pattern progressive disclosure refines.
- [[augmented-llm]] — adjacent: tools-retrieval-memory all benefit from progressive loading.

## Related entities

- [[wiki/entities/anthropic]] — origin of the Skills mechanism that instantiates the pattern.
- [[wiki/entities/claude-code]] — the platform.

## Mentioned in

- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
