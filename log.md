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
