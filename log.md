# log.md — Operations log

Append-only chronological record. See [[CLAUDE]] for the format spec. Greppable: `grep "^## \[" log.md | tail -10`.

---

## [2026-05-02] schema-update | Initialize LLM Wiki vault
- pages created: [[CLAUDE]], [[index]], [[log]], `templates/source.md`, `templates/entity.md`, `templates/concept.md`, `templates/synthesis.md`, `raw/README.md`
- notes: Bootstrap of the vault following Karpathy's LLM Wiki pattern. Three-layer architecture (raw / wiki / schema) established. Four page templates created. Index and log initialized.

## [2026-05-02] ingest | LLM Wiki — Karpathy
- raw: `raw/llm-wiki-pattern-karpathy.md` (downloaded from gist)
- pages created: [[wiki/sources/llm-wiki-pattern-karpathy]], [[wiki/entities/andrej-karpathy]], [[wiki/entities/vannevar-bush]], [[wiki/entities/obsidian]], [[wiki/entities/qmd]], [[wiki/concepts/llm-wiki-pattern]], [[wiki/concepts/memex]], [[wiki/concepts/retrieval-augmented-generation]]
- pages updated: [[index]]
- notes: First ingest. This source is constitutive of the vault — it's the pattern the schema in [[CLAUDE]] instantiates. Future ingests will be more conventional (entities and concepts that don't appear in the schema itself).

## [2026-05-02] ingest | Design Systems for AI Agents — Refero
- raw: `raw/Design Systems for AI Agents.md` (Web Clipper from styles.refero.design)
- pages created: [[wiki/sources/refero-design-systems-for-ai-agents]], [[wiki/entities/refero]], [[wiki/concepts/design-md]], [[wiki/concepts/markdown-as-agent-contract]]
- pages updated: [[wiki/concepts/llm-wiki-pattern]] (added markdown-as-agent-contract to Related concepts; added agent-config tag), [[index]]
- notes: Thin landing-page clipping but yielded a high-value meta-pattern page ([[markdown-as-agent-contract]]) that retroactively reframes [[llm-wiki-pattern]] as one instance of a broader family. Did not create entity pages for the brands listed on the Refero landing page (Linear, Stripe, Apple, etc.) — they appear only as examples; defer until a brand becomes the subject of its own ingest.

## [2026-05-02] lint | First lint pass; 3 missing canonical concept pages found
- script run: `bin/wiki_lint.py` — initial naive version flagged 14 broken links across 6 unique targets
- false positives: `[[link]]`, `[[page-name]]`, `[[wikilinks]]` — all inside inline code or fenced code blocks; lint regex was naive
- real findings: `[[ingest]]`, `[[query]]`, `[[lint]]` — referenced in [[wiki/concepts/llm-wiki-pattern]] and [[wiki/entities/obsidian]] but no pages existed
- pages created: [[wiki/concepts/ingest]], [[wiki/concepts/query]], [[wiki/concepts/lint]] (operation pages, not stubs); [[wiki/concepts/agents-md]], [[wiki/concepts/skill-md]], [[wiki/concepts/readme-md]] (stub completions of the markdown-as-agent-contract family)
- pages updated: [[wiki/concepts/llm-wiki-pattern]] (Related concepts now lists all sibling agent-contract concepts), [[wiki/concepts/markdown-as-agent-contract]] (wikilinks each markdown-file mention; cleaned aliases)
- tooling: improved `bin/wiki_lint.py` to honor inline-code and fenced-code spans before parsing wikilinks; committed to repo for reuse by the weekly remote lint
- post-fix lint: clean (0 broken, 0 ambiguous, 0 orphans, 0 index drift, 0 frontmatter issues)
- notes: orphan-check, index-drift, and frontmatter-drift checks all clean on first run — surprising result given recent volume of writes; suggests the schema's discipline is paying off.

## [2026-05-02] ingest | How I Turned My Claude Code Into 24/7 Dev Team — regent0x_
- raw: `raw/How I Turned My Claude Code Into 247 Dev Team (Full Guide + Repos).md` (Web Clipper from x.com/regent0x_)
- pages created: [[wiki/sources/regent0x-claude-code-247-dev-team]], [[wiki/entities/regent0x]], [[wiki/entities/claude-code]], [[wiki/entities/trail-of-bits]], [[wiki/entities/superpowers]], [[wiki/entities/claude-mem]], [[wiki/entities/claude-subconscious]], [[wiki/entities/trail-of-bits-claude-code-skills]], [[wiki/entities/anthropic-skills]], [[wiki/entities/tdd-guard]], [[wiki/entities/wshobson-agents]], [[wiki/entities/davepoon-subagents-collection]], [[wiki/entities/wshobson-commands]], [[wiki/entities/claude-squad]], [[wiki/entities/claude-flow]], [[wiki/concepts/subagents]], [[wiki/concepts/claude-code-skills]], [[wiki/concepts/claude-code-hooks]], [[wiki/concepts/claude-code-slash-commands]], [[wiki/concepts/multi-agent-orchestration]]
- pages updated: [[wiki/entities/anthropic]] (promoted from stub to substantive entity — now central to the Claude Code ecosystem section, not just the Refero catalog), [[wiki/entities/obsidian]] (added "Use as a Claude Code memory layer (regent0x_)" section with the structured vault layout), [[wiki/concepts/llm-wiki-pattern]] (added to Treatment across sources — first wild secondary citation), [[wiki/concepts/markdown-as-agent-contract]] (added to Treatment with note on engineering-domain-specific scaling), [[wiki/concepts/skill-md]] (Related concepts now distinguishes file-format vs. mechanism), [[index]]
- notes: First source whose ingest *demonstrates compounding* — the source explicitly cites Karpathy's [[llm-wiki-pattern]] which is already in the wiki, so the cross-reference goes both ways immediately. Also flagged a URL discrepancy (the post links to `github.com/karpathy/llm-wiki` which doesn't appear to resolve; the actual gist URL is in [[wiki/sources/llm-wiki-pattern-karpathy]]). Rich source — the [[CLAUDE]] template the post recommends is reusable for any future engineering-vault work.

## [2026-05-02] ingest | How to Build & Sell AI Automations That Generate $10K Per Month — Khairallah
- raw: `raw/How to Build & Sell AI Automations That Generate $10K Per Month (Full Course).md` (Web Clipper from x.com/eng_khairallah1)
- pages created: [[wiki/sources/khairallah-ai-automations-10k-month]], [[wiki/entities/eng-khairallah]], [[wiki/entities/tavily]], [[wiki/entities/google-drive]], [[wiki/entities/gmail]], [[wiki/entities/slack]], [[wiki/concepts/ai-automation-services]], [[wiki/concepts/context-file]], [[wiki/concepts/mcp-server]], [[wiki/concepts/scheduled-automation]]
- pages updated: [[wiki/concepts/markdown-as-agent-contract]] (added context-file to the family; added Khairallah to Treatment), [[wiki/concepts/skill-md]] (Related concepts adds context-file as sibling), [[wiki/concepts/claude-code-skills]] (cross-cited from the regent0x_ ingest above; touched again to capture Khairallah's services-side framing), [[wiki/concepts/claude-code-slash-commands]] (Khairallah's `/schedule` cross-cite), [[index]]
- notes: This source pairs with the regent0x_ ingest above as **the same Claude Code primitives, opposite economic frame** — personal productivity vs. service-business. Several concepts (mcp-server, scheduled-automation, claude-code-skills) are cited by both sources; their pages capture both perspectives explicitly under "Treatment across sources." This is the kind of synthesis territory the wiki was built for. Pricing claims ($3-15k/build, $750/mo retainers, $165k/yr, 18-month window) are the author's prior, not market data.

## [2026-05-02] schema-update | Add Stubs convention; reference lint script
- pages updated: [[CLAUDE]] — added § Page conventions → Stubs (formalizes `tags: [stub]` shape and lifecycle); added tooling note in § Workflows → Lint pointing to `bin/wiki_lint.py`
- notes: Closes the schema gap flagged in the previous log entry. Stubs convention codifies Kobby's standing preference for completionist coverage. The Stubs subsection also tells future linters to flag long-stale stubs as candidates for expansion or deletion.

## [2026-05-02] refactor | Backfill stub entity pages for all Refero brands
- pages created: [[wiki/entities/acctual]], [[wiki/entities/anthropic]], [[wiki/entities/antimetal]], [[wiki/entities/apple]], [[wiki/entities/base44]], [[wiki/entities/column]], [[wiki/entities/cursor]], [[wiki/entities/dia-browser]], [[wiki/entities/elevenlabs]], [[wiki/entities/family]], [[wiki/entities/general-intelligence-company]], [[wiki/entities/hyperstudio]], [[wiki/entities/linear]], [[wiki/entities/mercury]], [[wiki/entities/minimalissimo]], [[wiki/entities/monopo-saigon]], [[wiki/entities/raycast]], [[wiki/entities/stripe]], [[wiki/entities/superhuman]], [[wiki/entities/titan]]
- pages updated: [[wiki/entities/refero]] (added "Featured brands in catalog" section linking all 20; added website frontmatter), [[wiki/sources/refero-design-systems-for-ai-agents]] (expanded "Mentioned entities" with all 20 backlinks), [[index]] (new "Brands in Refero catalog (stubs)" subsection; stats updated)
- notes: Per Kobby's standing preference — completionist entity coverage. All 20 pages tagged `stub` with consistent structure (one-line citable framing, no fabricated profile prose). When future ingests bring in a primary source about any of these brands, expand the corresponding stub. The schema-conventions section in [[CLAUDE]] should probably be updated to formalize the stub convention; flagging here for next schema-update pass.
