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

## [2026-05-02] schema-update | Add Stubs convention; reference lint script
- pages updated: [[CLAUDE]] — added § Page conventions → Stubs (formalizes `tags: [stub]` shape and lifecycle); added tooling note in § Workflows → Lint pointing to `bin/wiki_lint.py`
- notes: Closes the schema gap flagged in the previous log entry. Stubs convention codifies Kobby's standing preference for completionist coverage. The Stubs subsection also tells future linters to flag long-stale stubs as candidates for expansion or deletion.

## [2026-05-02] refactor | Backfill stub entity pages for all Refero brands
- pages created: [[wiki/entities/acctual]], [[wiki/entities/anthropic]], [[wiki/entities/antimetal]], [[wiki/entities/apple]], [[wiki/entities/base44]], [[wiki/entities/column]], [[wiki/entities/cursor]], [[wiki/entities/dia-browser]], [[wiki/entities/elevenlabs]], [[wiki/entities/family]], [[wiki/entities/general-intelligence-company]], [[wiki/entities/hyperstudio]], [[wiki/entities/linear]], [[wiki/entities/mercury]], [[wiki/entities/minimalissimo]], [[wiki/entities/monopo-saigon]], [[wiki/entities/raycast]], [[wiki/entities/stripe]], [[wiki/entities/superhuman]], [[wiki/entities/titan]]
- pages updated: [[wiki/entities/refero]] (added "Featured brands in catalog" section linking all 20; added website frontmatter), [[wiki/sources/refero-design-systems-for-ai-agents]] (expanded "Mentioned entities" with all 20 backlinks), [[index]] (new "Brands in Refero catalog (stubs)" subsection; stats updated)
- notes: Per Kobby's standing preference — completionist entity coverage. All 20 pages tagged `stub` with consistent structure (one-line citable framing, no fabricated profile prose). When future ingests bring in a primary source about any of these brands, expand the corresponding stub. The schema-conventions section in [[CLAUDE]] should probably be updated to formalize the stub convention; flagging here for next schema-update pass.
