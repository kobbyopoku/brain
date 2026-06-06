---
type: concept
title: Markdown as Agent Contract
created: 2026-05-02
updated: 2026-06-06
aliases: [markdown as agent config, agent-readable markdown]
tags: [meta-pattern, ai-agents, markdown, agent-config, foundational]
---

# Markdown as Agent Contract

> An emerging meta-pattern in which markdown files (`CLAUDE.md`, `AGENTS.md`, `DESIGN.md`, `SKILL.md`, `README.md`) serve as the durable, human-readable configuration and instruction layer between humans and AI agents.

## Definition

"Markdown as agent contract" is the observation that markdown files are becoming the default place where humans encode the rules, conventions, taste, and context that AI agents should respect when operating in a domain. The files are durable artifacts (versioned, diffable, reviewable), human-readable (so the human stays in the loop), and natively consumable by LLMs (no parser, no schema, no special tooling). Examples in the wild:

- **`CLAUDE.md`** — schema for a Claude Code session; defines workflows, conventions, allowed actions. (See [[CLAUDE]] in this vault.)
- **`AGENTS.md`** — analogous file for OpenAI Codex / generic-agent setups. See [[agents-md]].
- **`DESIGN.md`** — design system reference for AI coding agents. See [[design-md]].
- **`SKILL.md`** — instructions for a Claude skill, defining when and how it should activate. See [[skill-md]].
- **`README.md`** — older convention, but increasingly read by agents as part of their context. See [[readme-md]].
- **Context files** — per-client/per-principal voice, audience, quality standards. Same shape, narrower audience scope. See [[context-file]].

What unifies these files is not a shared schema (each has its own structure) but a shared *role*: they are the **contract** between human intent and agent execution.

## Why it matters

This pattern reframes the question "how do I configure my AI agent?" away from per-tool UI surfaces or proprietary config formats and toward a portable, human-first artifact in the codebase. Several second-order consequences:

1. **Co-evolution**. Because the contract is a markdown file the human edits, both parties can update it as understanding deepens. The schema is alive.
2. **Knowledge compounds**. A `CLAUDE.md` written for one project carries forward; tweaks survive across sessions. Same for `DESIGN.md`.
3. **Tool-agnostic**. The same `AGENTS.md` works in Codex today and (in theory) in any future agent that respects the convention.
4. **Reviewable**. Pull-request review applies — a team can argue about the contract the same way they argue about code.
5. **Observable failure mode**: the agent does the wrong thing because the contract underspecifies or misspecifies, not because the agent is broken. Diagnose by reading the markdown.

This vault is itself an instance: [[CLAUDE]] is the contract, [[llm-wiki-pattern]] is the pattern, the wiki is the artifact the contract governs.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — frames `CLAUDE.md` (or `AGENTS.md`) as "the key configuration file" that "makes the LLM a disciplined wiki maintainer rather than a generic chatbot." This is the strongest articulation of the pattern in the wiki so far; Karpathy's framing of "co-evolved schema" is the canonical statement.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — instantiates the pattern in the design-systems domain via [[design-md]]. The framing is implicit (the source doesn't theorize the meta-pattern) but the artifact is the same shape.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — provides a **highly structured, engineering-domain-specific** CLAUDE.md template (sections for project, conventions, architecture decisions, current focus, rules) and partially answers an open question of this concept ("does the pattern scale beyond moderate complexity?"). The answer demonstrated: yes, by being highly structured per-domain rather than generic. Each subagent ([[subagents]]) gets its own CLAUDE.md, composing the contract into role-specific layers.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — adds [[context-file]] (per-client business voice/standards) and the [[claude-code-skills|skill file]] (per-task workflow) as instances of the pattern, distinct from the project-wide [[CLAUDE]] contract. Suggests the pattern naturally splits along *audience scope*: project (CLAUDE), client (context file), workflow (skill file), single capability (skill-md).
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational layered version: the AI OS uses claude.md (master prompt, updated 2× a day) + skills (`.claude/skills/<name>/skill.md`) + reference files (in `References/`) + contexts (in `Contexts/`) all as agent contracts at different scopes. Adds a strong cost discipline: *"Markdown is cheap to read; API docs are expensive to crawl every time"* — the *cost* of a contract file matters too, not just its content. Cross-cuts with [[claude-code-overhead-patterns]].
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — **the cost discipline made literal**: CLAUDE.md bloat is the largest single overhead pattern (~14% of all tokens). Every word in an agent-contract file is paid for on every turn of every session. The pattern's value depends on its size discipline; the source's target is combined user + project CLAUDE.md under 1,500 tokens.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — the pattern applied to **operations** rather than agents: ColdIQ documents repeatable client tasks as workflow files in markdown ("Written for someone who started Monday with zero context"). Same shape; different consumer (humans + agents both).
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. Instantiates the meta-pattern at **seven layers simultaneously**: SKILL.md (64 bundles), DESIGN.md (138 systems with the richer 9-section schema), CLAUDE.md (project instructions per agent), per-CLI agent contracts, question-form structured intake outputs, `<artifact>` HTML emissions, and MCP `get_file` responses. The most multi-layered single instance of the pattern in the wiki. Each layer is markdown a human wrote that an agent acts on. *Particularly worth noting*: Open Design extends the meta-pattern with explicit **anti-AI-slop machinery** ([[anti-ai-slop-machinery]]) — pre-emit gates, P0/P1/P2 checklists, blacklists — which is the most explicit "agent output discipline" articulation yet ingested.
- [[wiki/sources/noisyb0y1-marketingskills-repo]] — the pattern applied to **public-web buying-agent surfaces**: machine-readable endpoints like `/llms.txt`, `/pricing.md`, `/changelog.md` that expose product information directly to AI buying agents in a format they can consume. *"If pricing is hidden behind JavaScript or 'contact sales' an AI agent may simply exclude your product from a comparison."* The marketingskills repo itself is also an instance — a [[claude-code-skills|skill-pack]] in markdown — and its mandatory `product-marketing-context.md` is yet another instance ([[context-file]] applied to product-marketing). Three layers of the same meta-pattern visible in one source: the skill-pack (agent contract), the context file (agent contract), and the public web endpoints (buying-agent contract).
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — *2026-05-08*. **The pattern extended to non-developer audiences.** TheAIWorld22 enumerates 21 specific CLAUDE.md instructions across 5 parts (how Claude talks / behaves / context / memory / for developers), positioning CLAUDE.md as a configuration-for-anyone, not a developer-only artifact. Closes with Karpathy's viral 4 rules and a third-party "65→94% coding accuracy" claim. Cumulatively the strongest checklist-style articulation of the pattern in the wiki — a complement to the *theory* of the pattern (Karpathy) with *concrete prescription* for what to actually put in the file.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — *2026-05-08*. The pattern applied to a **workspace-folder-level contract** for [[cowork|Claude Cowork]]. Guri prescribes paste-ready Global Instructions (a per-user master agent contract) and three folder-level conventions (`ABOUT ME/`, `PROJECTS/`, `TEMPLATES/`, `CLAUDE OUTPUTS/`) — folders themselves become a contract, with the agent expected to read context from `ABOUT ME/` and write output to `CLAUDE OUTPUTS/`. **Folder-as-contract** is a sub-pattern worth tracking — the directory structure encodes input/output expectations the same way markdown encodes them.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — *2026-05-08*. The pattern applied to **task templates** in Khairallah's three-session Cowork architecture. Each template specifies input source, processing steps, output format, and save location — a contract between the human's intent ("produce a weekly report") and the agent's execution. The pattern crosses scope again: from project (CLAUDE) → folder (Cowork) → individual task (Khairallah's templates).
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — *2026-05-08*. **An attack on chunks as the unit of agent input** that strengthens the meta-pattern. Akshay argues against unstructured chunks of text in a RAG pipeline, in favor of typed Q-A packets ("IdeaBlocks") with governance fields. CLAUDE.md is *narrative-prose* contract; IdeaBlock is *atomic-typed* contract — both are markdown-shaped artifacts a human writes that an agent acts on, distinguished by structural granularity. Worth tracking: as the meta-pattern matures, the unit gets smaller and more typed.
- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it as Buzz's principle-based skill files being agent contracts; the source refines the meta-pattern with two claims — write principles not rules, and govern the contract like code (PR review, rollback).
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] frames it via Blueprint 01 (Session Agent) loading voice + topic positioning + algorithm scoring priorities from a CLAUDE.md/MEMORY.md project file every session — the contract-markdown pattern applied to a personal posting agent.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] frames it as Project Instructions / Custom Instructions functioning as a chat-product agent contract — the consumer-app counterpart to CLAUDE.md.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] frames it as Layers 1-2 (Personal Preferences + Project instructions) being the consumer-UI-field expression of the agent-contract pattern, rather than markdown files; gives a concrete Personal Preferences template (WHO I AM / HOW I WORK / WHAT I DO NOT WANT / GOALS, <500 words).
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] frames it as the daily-note conventions OPEN: / DONE: / UPDATE: being informal command surfaces an agent parses — DONE:/UPDATE: drive Claude's automatic property writeback; OPEN: drives the open-loops query. A narrow read/write instance of the agent-contract pattern.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] frames it as the deliverable unit being a documented Claude workflow built around a system prompt plus a context document; system-prompt-as-deliverable, with a concrete luxury-real-estate copywriter system prompt example.
- [[wiki/sources/cyrilxbt-personal-operating-system]] frames it as CLAUDE.md being the single source of truth governing every workflow; updating it updates all generated output. Note same-name collision with the Claude Code project-instruction convention — here it is a personal life-context file.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] frames it generalized across tools: CLAUDE.md and AGENTS.md are the same content under two filenames, and the shared markdown knowledge layer is read unchanged by any agent. Strongest wiki articulation that the agent-contract pattern is vendor-neutral by construction.
- [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]] frames it as 21 paste-ready CLAUDE.md instructions — concrete instances of the meta-pattern; distinct contribution is an explicit ROI/cost argument ($975/week per dev) for adopting the markdown contract, which prior wiki sources framed only qualitatively.
- [[wiki/sources/tricalt-memory-skills-same-harness]] frames it by arguing a memory API, skills, and an agent-md file are "the same play" — even compaction strategies — collapsing the contract-format distinction into one world model.
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] frames it as SOUL.md, MEMORY.md, and USER.md being markdown files injected into the system prompt as the agent's identity/knowledge contract — a Hermes-internal instance of the pattern, scoped to persona + memory.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it as both the CLAUDE.md context and the per-correction memory .md files being markdown contracts the agent reads.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] frames it via Pattern 4: CLAUDE.md as git-committed team infrastructure (Stack/Commands/Architecture/Rules), shared across 23,000 engineers, kept deliberately small (<60 lines); "stuffing it with every standard makes performance worse."
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] frames it as the "context + constraints + persistent project memory" lever mapping directly onto CLAUDE.md as the environment Claude reasons in.
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]] frames it as CLAUDE.md treated as "onboarding documentation for your AI coworker" — define instructions once vs repeating every session; the most slogan-level articulation of the meta-pattern (candidate sections: overview, stack, conventions, folder structure, design rules, API patterns, deployment, testing, forbidden actions).
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] frames it as SPEC.md being the written done-criteria contract the builder runs /goal against; Hermes authors it as the first card.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] frames it via Setup 1 (project-root CLAUDE.md declaring voice/audience/constraints/output rules) as a consumer-grade instance of this meta-pattern; "every chat starts as a specialist in your work."

## Sub-claims and details

- **Each file is contractual, not configurational.** The human commits to instructions; the agent is expected to follow them. Configuration is a value; a contract is a relationship.
- **Naming convention is converging on `<DOMAIN>.md` in CAPS.** CLAUDE, AGENTS, DESIGN, SKILL — all CAPS, suggesting "this is the canonical contract for this domain in this repo."
- **MCP servers are the runtime complement.** Where markdown contracts express *what the agent should do*, MCP servers expose *what the agent can call*. Refero (in [[wiki/entities/refero]]) ships both: a DESIGN.md catalog and a Refero MCP server.
- **The pattern crosses domains.** Personal knowledge (CLAUDE.md), design (DESIGN.md), generic agents (AGENTS.md), individual capabilities (SKILL.md). The shared property is "human writes prose; agent acts on it."
- **The pattern extends to public-web surfaces.** `/llms.txt` (site summary), `/pricing.md` (structured pricing), `/changelog.md` (public update log) expose product information for AI buying agents to read. Same shape, different consumer: not a coding agent in the user's IDE but a *third-party* agent acting on behalf of a prospect. See [[ai-seo]].

## Open questions and contradictions

- **Does the pattern scale beyond moderate complexity?** A 50-line CLAUDE.md is easy; a 5,000-line one starts to fail in obvious ways (the agent stops respecting later sections, contradictions accumulate). When does prose-as-contract break, and what replaces it? Possibly: split into multiple smaller contract files; possibly: structured frontmatter + prose hybrid.
- **Versioning**. Should agents be told *which version* of the contract they are operating against? In practice no one does this, but cross-session drift is a real failure mode.
- **Contract conflicts**. When `CLAUDE.md` says X and `DESIGN.md` says Y and they conflict, who wins? No convention exists. Likely solved per-project for now.
- **Discovery**. How does an agent know which contract files exist in a repo? `CLAUDE.md` is auto-loaded by Claude Code; arbitrary `<DOMAIN>.md` files are not. This may push toward a manifest/index file that lists all contracts.

## Related concepts

- [[llm-wiki-pattern]] — instance of the meta-pattern in the personal-knowledge domain.
- [[design-md]] — instance of the meta-pattern in the design-systems domain.
- [[agents-md]] — instance of the meta-pattern for OpenAI Codex / generic agents.
- [[skill-md]] — instance of the meta-pattern at the single-capability scope.
- [[readme-md]] — older sibling convention being absorbed into the family.
- [[context-file]] — instance at the per-client / per-principal scope.
- [[claude-code-skills]] — the *mechanism* through which one of these contracts (skill files) becomes runnable.
- [[ai-seo]] — public-web instance of the meta-pattern; `/llms.txt` and `/pricing.md` are buying-agent contracts.

## Related entities

- [[wiki/entities/refero]] — ships DESIGN.md, an instance of the pattern.
- [[wiki/entities/andrej-karpathy]] — strongest articulator of the pattern in the wiki so far (via the LLM Wiki gist).

- [[wiki/entities/marketingskills-repo]] — instantiates the pattern at three layers (skill-pack + context file + public endpoints).
- [[wiki/entities/open-design]] — instantiates the pattern at **seven layers** (SKILL.md / DESIGN.md / CLAUDE.md / per-CLI contracts / question-form / `<artifact>` HTML / MCP `get_file`).

## Important asymmetry: input-format vs output-format

This concept addresses **markdown as the agent INPUT format** (the contract / SOPs / instructions the human gives the agent — CLAUDE.md, AGENTS.md, SKILL.md, DESIGN.md, README.md, context files). It does **not** assert markdown is the right format for agent OUTPUT. [[wiki/sources/trq212-x-html-effectiveness|Thariq Shihipar's 2026-05-08 argument]] is that **HTML beats Markdown for agent output** when the output is meant for human review. The two layers compose cleanly: humans write markdown contracts → agents act → agents emit HTML artifacts. See [[artifact-first-workflow]] for the output-side concept.

This wiki page should not be cited to claim markdown is always the right agent format — only that markdown is the right *contract* format.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[wiki/sources/refero-design-systems-for-ai-agents]]
- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]]
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]]
- [[wiki/sources/noisyb0y1-marketingskills-repo]]
- [[wiki/sources/nexu-io-open-design]]
- [[wiki/sources/trq212-x-html-effectiveness]] — input-vs-output asymmetry caveat.
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — concrete checklist of 21 CLAUDE.md instructions extending the pattern to non-developer audiences.
- [[wiki/sources/heygurisingh-x-cowork-setup]] — folder-as-contract sub-pattern + paste-ready Global Instructions.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — task-template-as-contract at the production-block scope.
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — chunks vs typed Q-A packets as the unit of agent input.
- [[wiki/sources/petradonka-agents-need-feedback-loops]] — principle-based skill files as agent contracts; govern the contract like code.
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] — Session Agent loading voice/positioning/scoring from a project CLAUDE.md/MEMORY.md.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] — Project/Custom Instructions as the consumer-app counterpart to CLAUDE.md.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — Personal Preferences + Project instructions as UI-field expression of the pattern.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — OPEN:/DONE:/UPDATE: daily-note conventions as informal command surfaces.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] — system-prompt-plus-context-document as the deliverable unit.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — CLAUDE.md as single source of truth (personal life-context variant).
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — CLAUDE.md = AGENTS.md; vendor-neutral by construction.
- [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]] — 21 paste-ready CLAUDE.md instructions + explicit ROI ($975/week per dev).
- [[wiki/sources/tricalt-memory-skills-same-harness]] — memory API + skills + agent-md as "the same play."
- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] — SOUL.md/MEMORY.md/USER.md as Hermes identity/knowledge contract.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — CLAUDE.md + per-correction memory .md files as agent contracts.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — CLAUDE.md as git-committed team infra (<60 lines) across 23,000 engineers.
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] — context + constraints + persistent project memory lever.
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]] — CLAUDE.md as onboarding documentation for your AI coworker.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — SPEC.md as the written done-criteria contract for /goal.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] — Setup 1 project-root CLAUDE.md as consumer-grade instance.
