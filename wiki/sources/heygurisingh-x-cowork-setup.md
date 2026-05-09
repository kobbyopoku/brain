---
type: source
title: Guri Singh — How to Set Up Claude Cowork (And Quit ChatGPT for Good)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/heygurisingh/status/2052791496269812020
source_type: x-thread
author: Guri Singh
source_date: 2026-05-08
raw_path: raw/How to Set Up Claude Cowork (And Quit ChatGPT for Good).md
content_status: substantive
tags: [claude-cowork, knowledge-worker-tooling, anthropic-plugins, askuserquestion, folder-protocol]
---

# Guri Singh — How to Set Up Claude Cowork (And Quit ChatGPT for Good)

> The most comprehensive **Claude Cowork onboarding guide** ingested into the wiki. Provides specific folder structure (`ABOUT ME/` + `PROJECTS/` + `TEMPLATES/` + `CLAUDE OUTPUTS/`), file templates (about-me.md, anti-ai-writing-style.md), paste-ready Global Instructions, day-to-day workflow patterns, and coverage of Anthropic's 11 official Cowork plugins. Targets **knowledge workers** rather than developers — *"if you don't write code, mastering Claude Cowork should be your number one priority right now."*

## TL;DR

Claude Cowork ≈ Claude Code for non-developers. Sets up a dedicated folder where Claude has read+write access; you populate `ABOUT ME/` with identity files; configure Global Instructions once; then run 10-word prompts that produce *"this sounds like a real employee"* output instead of *"generic AI."* AskUserQuestion (Cowork-specific feature) generates an interactive form Claude uses to gather context before executing — the most-transformative feature most guides explain incorrectly.

## Key takeaways

### Claude's modes (the disambiguation)

Most users conflate Claude's product surfaces. Guri's clarification:

| Mode | What it is |
|---|---|
| **Claude Chat** | Like ChatGPT. The only one most users know. |
| **Claude Projects** | Chat organized by separate projects. |
| **Claude Code** | Revolution for developers. Programming much faster. |
| **Claude Cowork** | Like Code, but for knowledge workers. **The one that matters for non-developers.** |
| **Claude Skills** | Teaches repeatable workflows. Like Projects, but more powerful. |
| **Claude Connectors** | Connects Claude with Slack, Gmail, Calendar — reads, writes, acts inside your tools. |
| **Claude Plugins** | Like Connectors, but you configure them manually. |

### Recommended folder structure

```
📁 CLAUDE COWORK/
├── 📁 ABOUT ME/
│   ├── about-me.md                    # who you are; what you do
│   └── anti-ai-writing-style.md       # voice rules; what AI patterns to avoid
├── 📁 PROJECTS/
│   └── [one subfolder per active project]
├── 📁 TEMPLATES/
│   └── [structures of work you want to reuse]
└── 📁 CLAUDE OUTPUTS/
    └── [the only place Claude delivers finished work]
```

The asymmetry: 3 read-only folders + 1 write folder. *"Cowork has real read and write access to the folder you share. If something goes wrong, you want the damage to be contained."*

### Paste-ready Global Instructions

```markdown
# GLOBAL INSTRUCTIONS

## BEFORE EVERY TASK

1. Read ABOUT ME/. No task starts without reading both files.
2. If the task relates to a project, read everything in the corresponding PROJECTS/ subfolder before proceeding.
3. If the task involves a type of content that has a pattern in TEMPLATES/, study that structure first.

## FOLDER PROTOCOL

You have three read-only folders and one write folder.

### Read-only — never create, edit, or delete anything here:
- ABOUT ME/    → Identity and writing rules.
- TEMPLATES/   → Proven structures to reuse as patterns.
- PROJECTS/    → Briefings, references, and finished work organized by project.

### Write folder — the only place where you deliver work:
- CLAUDE OUTPUTS/ → Everything you create goes here. Organize with one
  subfolder per project, mirroring the structure of PROJECTS/.

## NAMING CONVENTION

project_content-type_v1.ext

Content types: Newsletter, Post, Brief, Deck, Report.

## OPERATING RULES

- If the briefing is unclear or incomplete, use AskUserQuestion. Don't fill gaps with generic content.
- Don't over-explain. Deliver the work.
- Never delete files anywhere.
```

### AskUserQuestion as the most-transformative feature

> *"This is the feature that most transforms the way you work. And it's the one most guides explain incorrectly."*

Always include in prompts: *"Start by using the AskUserQuestion tool before responding to gather enough context."* Cowork generates an interactive form (real buttons, selectable options, multi-select, drag-rankable). The AI asks you the questions so it can give the right answer.

This is the **operational instantiation** of the wiki's [[question-form-first]] concept. The wiki concept describes the pattern abstractly; Guri's guide gives the paste-ready prompt fragment that triggers it in Cowork.

### The 80% prompt that works for almost everything

```text
I want [TASK] for [SUCCESS CRITERIA].

First, explore my CLAUDE COWORK folder. Then, ask me questions using
the AskUserQuestion tool. I want to refine the approach with you
before you execute.
```

Five steps that follow:
1. Claude reads context files.
2. Generates a clickable form asking about audience, goals, preferences.
3. You click answers in <1 minute.
4. Claude shows a plan; you approve.
5. Executes; creates real files in your folder.

### The 11 official Anthropic plugins

Sales, Marketing, Legal, Finance, Data Analysis, Product Management, Customer Support — each ships with specific skills, workflows, slash commands. Customizable per-context (Claude asks about your company / project and remembers).

Cited examples:
- **Marketing**: `/marketing:draft-content` → reads about-me.md, drafts a post sounding like you, suggests hook variations.
- **Data**: `/data:explore` → drop a CSV; Claude summarizes, flags anomalies, suggests analyses, can build dashboard, writes SQL in natural language.
- **Legal**: *"Review the NDA in this folder. Flag any unusual or one-sided clauses."* → highlights risk clauses, plain-language explanations, alternative wording. *"This is what made the legal sector lose $285 billion on the stock market"* (claim cited but not verified).

## Notable quotes

> "When Anthropic launched [Cowork], software stocks lost $830 billion in 6 days because of its potential impact." *(claim cited; not verified)*

> "Forget about prompts. The game is text files. The more context you give it as files, the fewer prompts you need."

> "Cowork has real read and write access to the folder you share. If something goes wrong, you want the damage to be contained."

> "The whole process feels like directing someone competent, not fighting with a text box."

## Cross-cite with the wiki

- **[[wiki/entities/cowork]]**: this source substantially upgrades the existing Cowork stub. The 11-plugins list, mode disambiguation, and folder protocol are now wiki-canonized.
- **[[markdown-as-agent-contract]]**: the `ABOUT ME/about-me.md` + Global Instructions shape are direct instances. *"A good .md file is worth more than 50 random uploads"* — Guri's restatement of the meta-pattern.
- **[[question-form-first]]**: Guri's *"Always add 'Start by using AskUserQuestion'"* is the wiki concept applied operationally with a specific Cowork command.
- **[[doe-framework]]**: Cowork's folder protocol (read-only directives + write-only execution-output) is structurally a DOE-shaped layout — `ABOUT ME/` + `PROJECTS/` + `TEMPLATES/` are the directive layer; `CLAUDE OUTPUTS/` is the execution layer.
- **[[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]]**: sibling source on CLAUDE.md instructions. TheAIWorld22's 21 instructions are *what to put in CLAUDE.md*; Guri's guide is *what folder structure to put around CLAUDE.md*. Read together.

## Notes

- **Cited claim about Anthropic launching Cowork costing software stocks $830B**: not independently verified. Likely inflated marketing-style framing. Worth flagging when citing.
- **Same about the *"$285B legal sector loss"* claim**. Both are content-marketing-style hooks; the substantive folder-protocol + Global Instructions content is unaffected by these specific dollar claims.
- **Vedge implication**: Cowork's folder protocol is directly applicable to internal Vedge documentation work. The `CLAUDE OUTPUTS/` write-only convention matches Vedge's *expert-led implementation protocol* — agent writes are constrained to specific paths, not arbitrary edits.

## Mentioned entities

- [[wiki/entities/heygurisingh]] — author.
- [[wiki/entities/cowork]] — primary tool.
- [[wiki/entities/anthropic]] — publisher.

## Related concepts

- [[markdown-as-agent-contract]] — folder-protocol + Global Instructions are the meta-pattern instantiated.
- [[question-form-first]] — AskUserQuestion is the operational instantiation.
- [[doe-framework]] — folder protocol is DOE-shaped.
- [[claude-code-skills]] — adjacent (the 11 plugins are skill-pack-equivalent).

## Related sources

- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — sibling CLAUDE.md guide.
- [[wiki/sources/eng_khairallah1-x-2052684086414852546]] — sibling Cowork-as-automation guide (three-session daily architecture: Morning Briefing 7AM / Midday Production / End-of-Day Wrap-up 5PM).
