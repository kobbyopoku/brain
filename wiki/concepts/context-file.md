---
type: concept
title: Context File
created: 2026-05-02
updated: 2026-06-06
aliases: [context engineering, business context file]
tags: [agent-config, ai-automation]
---

# Context File

> A markdown file that captures a specific business's voice, audience, projects, and quality standards — separate from the [[claude-code-skills|skill file]] that captures *workflow* — so an AI agent can produce industry-specific, voice-matched output without the human re-explaining the business every session.

## Definition

A **context file** is a per-business document that describes the *what* and *who*: business description, audience profile, voice and tone, current projects, quality standards. It pairs with the [[claude-code-skills|skill file]], which describes the *how*: process steps, output formats, edge case handling. Together they let one underlying skill (e.g. "weekly client report") produce results tuned to a specific client without rewriting the workflow.

In practice, a single skill file may be reused across many clients; the context file is what differentiates the output for each.

## Why it matters

Context files solve a real problem: out of the box, Claude's outputs are generic. For a services-business deliverable, generic isn't usable — the report needs the agency's voice, the proposal needs the firm's style. Forcing the agent to re-learn the brand every session is the same kind of repeated explanation [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]] argues against, just at the per-client granularity.

The context-file / skill-file split is a useful generalization beyond AI automation services. Anywhere an agent's behavior should depend on *who it's working for* (client, persona, brand) rather than *what task it's doing*, the same split applies.

## Treatment across sources

- [[wiki/sources/khairallah-ai-automations-10k-month]] — the canonical source. Defines context-file design as one of four core technical competencies for an AI automation services builder. Practice prescription: build 3 context files for 3 hypothetical businesses in 3 different industries (real estate agency, marketing consultancy, e-commerce brand), each containing business description, audience profile, voice and tone, current projects, quality standards.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] frames it as: steps 2-3 (identity template in the Project knowledge base + Custom Instructions) are the Claude.ai-chat equivalent of a persistent context file read at session start.
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]] frames it as: the "context document" shipped with every Package-1 deliverable — treated here as a packaged artifact rather than (as in the sibling source) a distinct engineered skill.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it as: Step 2, ~/CLAUDE.md as "the onboarding doc" read before every session and auto-loaded into every chat.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] frames it as: the design system functions as persistent brand context the tool reads before generating — analogous to a context file that front-loads decisions so the model guesses less.
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]] frames it as: Step 4's project-documentation folders (architecture notes, feature explanations, workflows, DB schemas, design systems, prior decisions) are context-files at repo granularity — "better documentation, not better prompting."
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] frames it as: Setup 2, a Claude Project with tone guide, past work, brand spine, and audience attached — the context-file pattern in consumer form: "Claude reads from your business, not from generic internet data."

## Sub-claims and details

- **Standard fields** (per Khairallah): business description, audience profile, voice and tone, current projects, quality standards.
- **Reusability boundary**: context file = per-client; skill file = per-task. A reporting skill + 5 client context files = 5 differently-voiced reports from one skill.
- **Composition with [[claude-code-skills]]**: a skill invocation passes through the active context file; the skill applies the workflow, the context applies the voice.
- **Authoring practice**: built via client interview (per Khairallah, a 2-hour discovery session). Quality of the context file is largely a function of how well the builder elicited the client's voice and standards.
- **Adjacent to [[CLAUDE]] in shape**: both are markdown files of conventions an agent reads. Context files are narrower (one client, often domain-specific) and more frequently revised (as projects shift) than [[CLAUDE]].

## Open questions and contradictions

- **Format conventions**: Khairallah names the fields but does not specify a canonical format (frontmatter? section headings? structured YAML?). A convention would aid portability across builders.
- **Context-skill collision**: when the skill file specifies a tone and the context file specifies another, who wins? Typically the context file should override (it's more specific), but this is unstated.
- **Versioning across client revisions**: when a client rebrands or shifts focus, the context file must update. A versioning convention would support audit and rollback.
- **Boundary with the broader [[markdown-as-agent-contract]] family**: is a context file an instance of that meta-pattern? Probably yes — it's a markdown file used as a contract about how the agent should behave for a specific principal.

## Related concepts

- [[claude-code-skills]] — pairs with context files; skill is workflow, context is voice.
- [[markdown-as-agent-contract]] — the broader meta-pattern this concept fits within.
- [[ai-automation-services]] — the business model this concept is a core competency for.
- [[CLAUDE]] — adjacent in shape; project-wide vs. per-client.

## Related entities

- [[wiki/entities/eng-khairallah]] — author of the canonical source.

## Mentioned in

- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]]
- [[wiki/sources/eng_khairallah1-real-money-ai-automations]]
- [[wiki/sources/charliejhills-full-agent-system-6-steps]]
- [[wiki/sources/prajwaltomar-claude-design-workflow]]
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]]
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]]
