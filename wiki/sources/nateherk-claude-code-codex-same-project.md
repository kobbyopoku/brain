---
type: source
title: nateherk — How to Use Your Claude Code Projects in Codex in 5 Mins
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/nateherk/status/2056456654015639567
source_type: x-thread
author: nateherk (@nateherk)
source_date: 2026-05-18
raw_path: raw/How to Use Your Claude Code Projects in Codex in 5 Mins.md
content_status: substantive-verbatim
tags: [claude-code, codex, agents-md, claude-md, skills, subagents, agent-portability, session-handoff, multi-agent, vendor-lock-in]
---

# nateherk — How to Use Your Claude Code Projects in Codex in 5 Mins

> nateherk's portability playbook: a Claude Code project converts to a Codex project in one prompt because **the bulk of a project (its shared markdown knowledge layer) is tool-agnostic** — only the thin config and sub-agent format differ. The thesis is *don't get locked into one ecosystem*; run [[wiki/entities/claude-code|Claude Code]] and [[wiki/entities/codex-cli|Codex CLI]] in the same folder, in two terminals, and hand off when one gets stuck. nateherk's 3rd substantive wiki source.

## TL;DR

A coding-agent project decomposes into three layers, and only two of them are tool-specific. The big layer — shared markdown knowledge (wiki, references, scripts, decisions) — is read by any agent unchanged. [[wiki/entities/claude-code|Claude Code]] looks for `CLAUDE.md` + a `.claude/` folder; [[wiki/entities/codex-cli|Codex]] looks for `AGENTS.md` + a `.codex/` folder + a `.agents/` folder. Skills are identical (markdown + YAML frontmatter, just a different folder); sub-agents differ only in file format (markdown for Claude, TOML for Codex). You convert a whole project by telling Codex to mirror your `CLAUDE.md`, then run both agents in parallel and use a session-handoff move when one spirals on an error.

## Key takeaways

- **The "either/or" framing is wrong** — running Claude Code and Codex in the same project is a both/and setup. nateherk reports being "bailed out by Codex pretty frequently" when Claude Code loops on the same error burning tokens, while still doing most work in Claude Code.
- **Three layers of a coding-agent project**: (1) **Shared knowledge** — wiki, references, scripts, decisions, archives, brand assets, project files; anything markdown; *never changes per tool*; (2) **Workflows and skills** — prompts and reusable agents; same format, different folder per tool; (3) **Tool-specific config** — `settings.json` for Claude Code, config files for Codex; small and easy to mirror.
- **The load-bearing insight**: layer 1 is huge and doesn't move. "Most of what makes your project actually work sits there." Only layers 2-3 get mirrored — so cross-tool portability is cheap.
- **Claude Code wants two things at project root**: `CLAUDE.md` (instructions file, "like a system prompt") + `.claude/` folder (config, settings, skills, agents).
- **Codex wants three things**: `AGENTS.md` (same content as `CLAUDE.md`, different filename) + `.codex/` folder (config and agents) + `.agents/` folder (skills).
- **Both tools respect the global-vs-project split** — a user-level `~/.claude/CLAUDE.md` applies to every project; a project-level one lives in the repo. Codex works the same way.
- **Skills are plug-and-play across both tools** — markdown files with YAML frontmatter in both. Same format, same structure. Only the folder differs: Claude Code reads `.claude/skills`, Codex reads `.agents`. Drop the same file in both places; no rewrite, no translation.
- **Sub-agents differ in format only** — Claude Code uses markdown, Codex uses TOML. Same job (describe what the agent does, what model it runs on, what tools it can call), different wrapper syntax.
- **One real divergence: Codex sub-agents don't auto-invoke.** Claude Code routes to a sub-agent based on its description; Codex requires you to call the sub-agent explicitly by name.
- **The convert prompt is the whole setup** — tell Codex: create an `AGENTS.md` from `CLAUDE.md`, set up a `.codex` config, put skills in `.agents`, put agents in `.codex`, and research both tools' docs to make sure everything important converts. Codex reads your `CLAUDE.md`, mirrors the structure, does its own doc research, and writes the parallel files.
- **Maintenance after conversion is small** — mirror major `CLAUDE.md` changes into `AGENTS.md`; new skills work in both places as the same file.
- **Run both at once**: same folder, two terminals — type `claude` in one, `codex` in the other. nateherk built the video's HTML cheat sheet with both agents collaborating on the same file (Claude styled the page; Codex "restored the value that got lost in the styling pass").
- **File-collision warning**: if both agents edit the same file simultaneously they overwrite each other — coordinate which agent owns which file.
- **Terminal over IDE extension** — nateherk moved most work to the terminal (`claude` / `codex` in-project) over the VS Code extensions; faster and keeps the workflow clean.
- **The session-handoff move** — when Claude Code spirals, nateherk runs a `session-handoff` skill he built that summarizes the conversation, active files, decisions made, and next steps; he pastes that summary into Codex and continues. "Sometimes Codex fixes in 10 seconds what Claude Code was looping on for ten minutes."
- **The point is anti-lock-in, not tool superiority** — "don't get locked into one ecosystem." When Claude Code goes down for a day, Codex is already wired into the same project so you keep building at the same speed. Cost is two subscriptions.
- **Transferable mental model**: "If you've mastered Claude Code, you've basically mastered Codex. The mental model is the same. The file names are different."

## Notable quotes

> "Both agents read from the same shared knowledge base. The setup difference is small."

> "The trick is recognizing that the first layer is huge and doesn't move. Most of what makes your project actually work sits there. The other two layers are the part you mirror."

> "Drop the same file in both places. Both tools can run it. No rewrite, no translation."

> "When Claude Code spirals on the same error, I run a skill I built called session-handoff. It summarizes what we've talked about, which files are active, what decisions we made, and what the next steps are. I copy that summary, paste it into Codex, and keep going."

> "If you've mastered Claude Code, you've basically mastered Codex. The mental model is the same. The file names are different."

## Notes

- **This is the cross-tool generalization of [[markdown-as-agent-contract]].** Prior wiki sources treat `CLAUDE.md` as the contract for *one* agent; nateherk's three-layer model shows the contract is portable — the same markdown knowledge layer drives any agent, and `CLAUDE.md` ↔ `AGENTS.md` are the same content under two filenames. This is the strongest articulation in the wiki so far that the agent-contract pattern is *vendor-neutral by construction*, not Claude-specific.
- **Directly upgrades two stubs.** [[wiki/entities/codex-cli|Codex CLI]] was a stub known only via Open Design's PATH-scan; this source supplies its first behavioral facts (looks for `AGENTS.md` + `.codex/` + `.agents/`; TOML sub-agents; no sub-agent auto-routing). The [[wiki/concepts/agents-md|AGENTS.md]] concept stub gets its first primary-source treatment: AGENTS.md is the Codex-side mirror of CLAUDE.md, same content.
- **The three-layer model is a sibling of [[wiki/concepts/reasoning-execution-split|reasoning-execution-split]] applied to *files* rather than runtime** — it splits a project into a stable knowledge substrate vs. thin swappable orchestration config. The portable layer is the "knowledge"; the per-tool layer is the "wiring."
- **Skill-format convergence corroboration.** nateherk's claim that skills are identical markdown+YAML across Claude Code and Codex (different folder only) is a real-world counterpart to the [[wiki/sources/nousresearch-hermes-agent|Hermes Agent]] source's note on agentskills.io as a cross-vendor skill standard. Two independent sources now point at skills converging on a portable format while sub-agents and config stay vendor-specific. *(Uncertain whether nateherk's "drop the same file in both" holds for all skill features or just the common subset — he asserts full interchangeability but the source is a tutorial thread, not a spec.)*
- **The session-handoff skill is a [[wiki/concepts/hot-cache|hot-cache]]-adjacent move** — it externalizes live session state (conversation summary + active files + decisions + next steps) into a portable artifact that survives the jump from one agent to another. nateherk's own earlier source introduced `_hot.md`; session-handoff is the same externalize-context primitive used for *cross-tool* handoff rather than session-restart.
- **Caveat on the convert prompt**: it relies on Codex doing accurate self-research of both tools' docs. nateherk presents this as reliable; in practice the fidelity of an auto-generated `AGENTS.md` depends on the model and the project's complexity. Treat the one-prompt conversion as a strong starting point, not a guaranteed-complete migration.
- **Relevance to [[wiki/projects/helm|Helm]] and the wiki owner's stack**: the three-layer decomposition is a useful portability discipline for any multi-agent build — keep the knowledge/markdown layer tool-agnostic, isolate the per-tool config thin. The anti-lock-in argument (keep a second agent wired into the same project as availability insurance) is a concrete resilience pattern for production agent work.

## Mentioned entities

- [[wiki/entities/nateherk]] — author; reports daily parallel use of Claude Code + Codex (3rd substantive source).
- [[wiki/entities/claude-code]] — primary agent; reads `CLAUDE.md` + `.claude/`.
- [[wiki/entities/codex-cli]] — the parallel agent; reads `AGENTS.md` + `.codex/` + `.agents/`; TOML sub-agents; no sub-agent auto-routing. **First behavioral source — upgrades the stub.**
- [[wiki/entities/openai]] — vendor of Codex.
- [[wiki/entities/anthropic]] — vendor of Claude Code.
- [[wiki/entities/clickup]] — nateherk's "ClickUp searcher" sub-agent is the worked example of markdown-vs-TOML format divergence.

## Related concepts

- [[markdown-as-agent-contract]] — nateherk generalizes the contract across tools: `CLAUDE.md` ↔ `AGENTS.md`, same content, two filenames.
- [[agents-md]] — first primary-source treatment of `AGENTS.md` as Codex's mirror of `CLAUDE.md`.
- [[claude-code-skills]] — skills are markdown+YAML in both tools; portable file, different folder.
- [[subagents]] — sub-agents differ only in format (markdown vs TOML); Codex's don't auto-invoke.
- [[reasoning-execution-split]] — file-level analogue: stable knowledge layer vs swappable per-tool config.
- [[hot-cache]] — the session-handoff skill externalizes live session state into a portable handoff artifact.
- [[multi-agent-orchestration]] — two agents in two terminals on one folder; coordinate file ownership.

## Related sources

- [[wiki/sources/nateherk-claude-code-os-3m-business]] — same author's AI OS playbook; introduces `_hot.md`/hot-cache, the externalize-context ancestor of the session-handoff move.
- [[wiki/sources/nousresearch-hermes-agent]] — corroborates cross-vendor skill-format convergence (agentskills.io) and is itself model/tool-agnostic by design.
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — single-tool articulation of the CLAUDE.md contract that nateherk generalizes across tools.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — sub-agents framed as job-description + trigger + output; complements the markdown-vs-TOML sub-agent format note.
