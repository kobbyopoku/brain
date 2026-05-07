---
type: concept
title: Claude Code Skills
created: 2026-05-02
updated: 2026-05-05
aliases: [skills, claude skills, skill plugins]
tags: [claude-code, mechanism, agent-config]
---

# Claude Code Skills

> The mechanism by which Claude Code is taught domain-specific workflows — markdown files (and frontmatter) that define a single capability, when it activates, and the steps the agent follows when invoking it.

## Definition

A **skill** in Claude Code is a unit of domain-specific instruction packaged so the agent can selectively invoke it. The unit file format is a [[skill-md|SKILL.md]] (or equivalent) with frontmatter that includes at minimum a name and a description; the description determines when the agent decides the skill applies. Skills can be plugin-namespaced (e.g. `superpowers:writing-plans`, `pr-review-toolkit:code-reviewer`). Where [[CLAUDE]] is the project-wide contract, a skill is a **single capability** the agent picks up and uses on demand.

## Why it matters

Out of the box, Claude is a generalist. Skills turn it into a specialist for the workflows you care about — without losing the generality, because skills activate selectively based on description-matching against the current task. This lets a user stack many skills (security review, TDD enforcement, design taste, document generation, etc.) and still keep the agent's effective context tight: only the relevant skills actually load.

This concept is **distinct from the file format** captured in [[skill-md]]. SKILL.md is the *file*; this page is about the *mechanism* — invocation, activation, namespacing, composition with [[subagents]].

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — characterizes skills as transforming Claude Code "from 'write code when asked' into a complete development methodology." Names specific skill collections: [[wiki/entities/superpowers]] (workflow discipline), [[wiki/entities/trail-of-bits-claude-code-skills]] (security), [[wiki/entities/anthropic-skills]] (official PDF/DOCX/XLSX), [[wiki/entities/tdd-guard]] (TDD enforcement). Asserts skills don't conflict with each other and stack additively.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — frames skill-file authoring as one of four core competencies for an AI automation services business: "the skill file is the engine of every automation." The author's framing is implementation-side: a skill file is a process-spec the agent executes (process steps, output formats, edge case handling, quality checks, error recovery).
- [[wiki/sources/HeyZaraKhan-anthropic-skills-announcement]] — announcement-style coverage characterizing skills as *modular, versioned, dynamically loaded* — the shift from "prompt engineering" to "programmable, reusable AI systems."
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — architectural framing: a skill is a packaged capability combining *guidance + context + execution*. Names [[progressive-disclosure]] as the conceptual unlock (metadata first, content on demand) and [[reasoning-execution-split]] as why skills with embedded code are reliable in a way pure-prompt skills aren't. Also flags the security risk surface: skills add power, which means they add risk.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational skill-authoring playbook: six-step framework (name+trigger / one-sentence goal / step-by-step process / reference files / rules+guardrails / improvement loop), three-level loading model (front matter → skill.md → reference files), keep skill.md under 500 lines, project-level vs `~/.claude/skills/` global distinction, hardcode stable values into skill.md instead of querying via MCP every time.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — the cost counterpoint: skill loading on irrelevant tasks is the 5th-largest [[claude-code-overhead-patterns|overhead pattern]] (~7% of total tokens). Author had 11 active skills loading "just in case"; cut to 4 and saved 9,000+ tokens per task on average. Auto-invocation is conservative (when in doubt, load), so unused skills cost on every task.
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. The **largest substantive skill-pack** in the wiki — [[wiki/entities/open-design|Open Design]]'s `skills/` directory contains **71 SKILL.md bundles (live count, 2026-05-05)** spanning prototypes (web/mobile/dashboard/landing), HTML decks (21+ deck flavors), documents (PRDs, runbooks, OKRs, finance reports), media generation, integrations (orbit family), and meta-skills (critique, tweaks, fidelity audit). Bundles [[wiki/entities/guizang-ppt-skill|guizang-ppt-skill]] verbatim with attribution.
- [[wiki/sources/open-design-catalog]] — *2026-05-05*. Catalog enumeration of all 71 skills with descriptions; raw bundles fetched at `raw/open-design/skills/<name>.md`. Adds a notable observation: the **orbit family** (`orbit-general`, `orbit-github`, `orbit-gmail`, `orbit-linear`, `orbit-notion`) implies a **platform-integration substrate** in the Open Design daemon — functionally analogous to MCP servers but skill-shaped (the agent calls an `orbit-github` skill rather than calling a github MCP). Worth investigating whether orbits are a meaningful alternative to MCPs or just thin wrappers around them. The wiki now has three substantive non-Anthropic skill-packs in size order: Open Design (71) > Refero design-md (33) > marketingskills (139 tactics packed across fewer files).
- [[wiki/sources/noisyb0y1-marketingskills-repo]] — the **most substantive non-design skill-pack example yet ingested**. Surfaces [[wiki/entities/marketingskills-repo|coreyhaines31/marketingskills]] — a free, open-source skill-pack containing 139 growth tactics, 12 programmatic-SEO playbooks, frameworks for copywriting / CRO / A/B testing / pricing / [[ai-seo|AI SEO]], and a tool registry (GA4, GSC, Mixpanel, [[wiki/entities/posthog|PostHog]], [[wiki/entities/stripe|Stripe]], etc.) with API/MCP/CLI availability noted per tool. Architectural pattern: **every skill begins by reading `product-marketing-context.md`** ([[context-file]] applied to product-marketing) before any other action — no [[context-file]], no useful output. Claims to replace a $10K/mo marketing agency. Sibling to [[wiki/entities/refero|Refero]] (design-tokens-as-skills): same shape, different domain.

## Sub-claims and details

- **File format**: see [[skill-md]] — markdown plus frontmatter (name, description, when to invoke).
- **Activation**: based on description matching against the current task. The agent reads available skill descriptions as part of its context and invokes the matching one(s).
- **Three-level loading** (per [[wiki/sources/nateherk-claude-code-os-3m-business|nateherk]] and [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world|NainsiDwiv50980]]):
  - **L1**: scan all skill front matter (~100 tokens per skill). Always loaded.
  - **L2**: full skill.md (~couple thousand tokens). Loaded when L1 metadata matches.
  - **L3**: reference files. Loaded only when L2 instructions point at them.
  See [[progressive-disclosure]].
- **Six-step authoring framework** (per [[wiki/sources/nateherk-claude-code-os-3m-business|nateherk]]): name+trigger / one-sentence goal / step-by-step process / reference files / rules+guardrails / improvement loop. After each run, update the skill.
- **Namespacing**: plugin-prefixed (e.g. `posthog:querying-posthog-data`, `vercel:nextjs`) when distributed via plugin marketplaces.
- **Composition**: skills stack — multiple skills can apply to the same task. Reported (regent0x_) as non-conflicting; in practice ordering and interaction may matter for complex stacks.
- **Composition with [[subagents]]**: each subagent can have its own skill stack; e.g. the reviewer subagent + the trail-of-bits security skill collection.
- **Distribution**: open-source repos on GitHub; some via the Anthropic plugin marketplace (`/plugin install <name>@<source>`).
- **Two perspectives on the same artifact** (worth keeping straight):
  - From a **personal-productivity** angle (regent0x_), skills are pre-built collections you install to gain capabilities you didn't have to write yourself.
  - From a **services-business** angle (Khairallah), skill-file authoring is a billable craft — the value the AI automation provider delivers to a client is fundamentally a portfolio of well-designed skill files.

## Open questions and contradictions

- **Activation collision**: when two skills' descriptions both seem to match the task, who wins? Sources don't address this.
- **Skill versioning**: as skill files evolve, agents loading older or newer versions may behave differently. No skill-versioning convention captured yet.
- **Skill quality variance**: open-source skill repos vary widely in quality; "stack as many as you want" assumes the skills are well-authored, which is unsourced.
- **The "stack additively" claim is contradicted by [[claude-code-overhead-patterns|measured overhead]]**: regent0x_ asserts skills don't conflict and stack additively; Mnilax measures that 9 active skills × ~1,500 tokens = 13,500 tokens of overhead per task even when none of them apply. Both claims are correct in different senses (no behavioral conflict vs. real cost compounding); reconciling them: stack additively but audit aggressively.
- **Description quality is load-bearing**: a skill with a vague description either over-fires (cost) or under-fires (manual instructions). No tooling for "your description has drifted from your skill's actual behavior."

## Related concepts

- [[skill-md]] — the file format this concept builds on.
- [[markdown-as-agent-contract]] — skills are an instance of the meta-pattern.
- [[subagents]] — composes naturally with skills.
- [[context-file]] — adjacent concept (Khairallah's "context file" is to the *business* what a skill is to the *workflow*).
- [[claude-code-hooks]] — different mechanism, same Claude Code platform.
- [[claude-code-slash-commands]] — different mechanism, same platform.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/superpowers]] — workflow-discipline skill plugin.
- [[wiki/entities/anthropic-skills]] — official skill collection.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — security skill collection.
- [[wiki/entities/tdd-guard]] — TDD-enforcement skill.
- [[wiki/entities/anthropic]] — maintainer of Claude Code and the official skill collection.
- [[wiki/entities/marketingskills-repo]] — substantive marketing-domain skill-pack (139 tactics + 12 SEO playbooks + tool registry).
- [[wiki/entities/refero]] — substantive design-domain skill-pack (20-brand DESIGN.md collection).
- [[wiki/entities/open-design]] — **largest substantive skill-pack** (64 SKILL.md bundles + 138 design systems).

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/khairallah-ai-automations-10k-month]]
- [[wiki/sources/HeyZaraKhan-anthropic-skills-announcement]]
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]]
- [[wiki/sources/noisyb0y1-marketingskills-repo]]
- [[wiki/sources/nexu-io-open-design]]
- [[wiki/sources/open-design-catalog]]
