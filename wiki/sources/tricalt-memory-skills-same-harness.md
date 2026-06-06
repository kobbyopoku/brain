---
type: source
title: tricalt — Memory isn't a plugin. Skills aren't a plugin. They're the same harness.
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/tricalt/status/2055876832797581406
source_type: x-thread
author: tricalt (@tricalt)
source_date: 2026-05-17
raw_path: raw/Memory isn't a plugin. Skills aren't a plugin. They're the same harness..md
content_status: substantive-verbatim
tags: [memory, skills, agent-harness, world-model, self-improvement, cognee, agent-architecture]
---

# tricalt — Memory isn't a plugin. Skills aren't a plugin. They're the same harness.

> The author (a Cognee/topoteretes maintainer) argues that **memory and skills are not separable product categories** — both are facets of a single "world model" that an agent's harness loads to decide its next action; Cognee stores skills and memory in the same graph so each can improve the other.

## TL;DR

The post collapses two then-current debates into one claim: "memory APIs are not a viable product category" and "skill systems are just markdown" are two sides of the same coin. Both memory and skills are part of a single **world model** — the entire aggregate of context the harness loads to decide the next step. Skills are the *narrow, procedure-recording* slice ("to do task T, run X, Y, Z"); memory is the *broad, world-observing* slice. Cognee unifies them in one graph store so self-improvement runtime and agentic retriever share the same nodes, and a `SkillChangeEvent` makes a skill a traceable, evolving memory node.

## Key takeaways

- The post stitches together two arguments: @sarahwooders + @hwchase17's "memory isn't a plugin, it's the harness," and the author's own earlier (1.7M-view) post that "skills aren't static files" — both reduce to *the same harness*.
- **Skills degrade silently in dynamic environments**; they need a loop — **Observe → Inspect → Amend → Evaluate** — to stay correct.
- A **world model** is "whatever the agent is aware of and what it uses to predict the next action": codebase layout, tool schemas, file system, last ~20 conversation turns, user preferences — the entire aggregate of context the harness loads.
- Framing: **memory is a broad harness, skill is a specific one.** Skills are "the part that records what to do"; a `SKILL.md` is a procedure-level claim.
- A skill is "a compressed procedure" — "the world has responded to X, Y, Z by producing T in the past, and probably will again." **Memory observes the world while skills codify it into a rule.**
- **No clean line between memory and skills**: "Skills improve by reading their memory. Memory improves by amending the skills attached to it... because there should not be one."
- Cognee stores skills and memory in the **same graph store**; self-improvement runtime and agentic retriever share the same graph nodes.
- `cognee.remember("skills/")` ingests skills "with one line"; a `SkillChangeEvent` emits memory events on skill change, making each skill a memory node that "evolves, is traceable, and controllable."
- The self-improvement API is exposed via a `SkillRunEntry` passed to `cognee.remember(...)` with a `success_score`, `feedback`, and a `skill_improvement` block (`apply`, `score_threshold`).
- Anecdote: a hackathon produced **21 "LLM Knowledge Wikis" in 3 hours** using Cognee plus Redis as a session store.
- Thesis on misspecification: "Every world model outside board games is permanently misspecified. The harness's job isn't to fix the schema. It's to run a controller on top of one that's wrong by construction." Cognee positions itself as that controller.
- It doesn't matter whether you use a memory API, skills, or an AGENTS.md/agent-md file — "even compaction strategies are part of the same play... It is the same world model."
- Closing test: "if your memory system can't route a skill, it's not memory, let alone a world model."
- Cognee is open-source (github.com/topoteretes/cognee).

## Notable quotes

> "Both arguments are in essence about the same harness. A world model."

> "Memory observes the world while skills codifies it into a rule."

> "Skills improve by reading their memory. Memory improves by amending the skills attached to it. There's no clean line between them because there should not be one."

> "Every world model outside board games is permanently misspecified. The harness's job isn't to fix the schema. It's to run a controller on top of one that's wrong by construction."

> "if your memory system can't route a skill, it's not memory, let alone a world model."

## Notes

- This is a **vendor-positioning post** for Cognee (topoteretes): the philosophical argument is real, but the conclusion ("Cognee is that controller") is a product pitch. Treat the architecture claims as advocacy, not benchmarked results.
- The "world model" framing is the load-bearing idea and a useful counterweight to the wiki's existing tendency to treat skills (`SKILL.md`) and memory as separate. It argues they are two queries against one graph.
- Strong resonance with [[wiki/sources/nousresearch-hermes-agent|Hermes Agent]]'s built-in learning loop: Hermes "creates skills from experience" and "improves them during use" — the agent-internal realization of exactly the Observe → Inspect → Amend → Evaluate loop this post prescribes. Cognee externalizes that loop into a graph store rather than baking it into the agent runtime.
- The Observe → Inspect → Amend → Evaluate loop is structurally Saraev's [[self-annealing]] — self-improvement via a feedback loop — but encoded in a graph store with scored skill events rather than directive markdown files. Same goal, different where-does-improvement-live trade-off.
- Directly relevant to this vault: the post's "21 LLM Knowledge Wikis in 3 hours" hackathon and its memory-as-graph framing are an alternative substrate for the [[llm-wiki-pattern]] — the wiki here uses markdown files an LLM maintains; Cognee uses a graph the agent self-amends.
- The code snippet in the raw contains typos (`"Review the current skiill,` with an unterminated string) — it is illustrative pseudo-code from a social post, not a verified API contract. Do not treat the exact `SkillRunEntry` signature as authoritative.
- Uncertainty: the post references "@sarahwooders and @hwchase17 made the case last month" without a link to that specific claim; the author's own "1.7M views" skills post is linked (status 2032179887277060476) but not ingested here.

## Mentioned entities

- [[wiki/entities/tricalt]] — author; Cognee/topoteretes maintainer arguing memory and skills are one harness.
- [[wiki/entities/cognee]] — the product; graph store unifying skills + memory with a self-improvement runtime.
- [[wiki/entities/topoteretes]] — the org/GitHub owner behind Cognee.
- [[wiki/entities/sarah-wooders]] — credited with the "memory isn't a plugin, it's the harness" argument.
- [[wiki/entities/harrison-chase]] — (@hwchase17) credited with the same memory-as-harness argument.
- [[wiki/entities/redis]] — used as session store in the 21-wikis hackathon.

## Related concepts

- [[world-model]] — the central concept the post introduces: the aggregate of context the harness loads to predict the next action.
- [[agent-harness]] — memory and skills are framed as facets of a single harness.
- [[skill-md]] — a `SKILL.md` is framed as a "procedure-level claim"; the narrow slice of the world model.
- [[self-annealing]] — the Observe → Inspect → Amend → Evaluate loop is a self-improvement / self-annealing mechanism.
- [[llm-wiki-pattern]] — Cognee's graph-store self-amendment is an alternative substrate to the markdown LLM-wiki; the hackathon built 21 "LLM Knowledge Wikis."
- [[markdown-as-agent-contract]] — the post argues memory API vs skills vs agent-md files are all "the same play."
- [[reasoning-execution-split]] — skills as "compressed procedures" the agent executes vs memory it reasons over.

## Related sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — companion treatment of agentic memory as the storage/retrieval/management layer that makes an agent stateful; this post argues that same layer is inseparable from skills.
- [[wiki/sources/nousresearch-hermes-agent]] — Hermes's built-in learning loop is the agent-internal realization of this post's Observe → Inspect → Amend → Evaluate loop.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — Cognee's self-amending graph is an alternative to Karpathy's markdown-wiki substrate.
