# raw/

Immutable source documents. Articles, papers, gists, transcripts, notes — anything you want the wiki to draw from.

**Rules**:
- The LLM **reads from** this directory but **never writes to** it.
- Filenames mirror their wiki summary slug, e.g. `llm-wiki-pattern-karpathy.md` here ⟷ `wiki/sources/llm-wiki-pattern-karpathy.md`.
- Images and binary attachments go in `raw/assets/`.
- If a source needs annotation or correction, the note lives in the wiki page, not here.

To add a new source: drop the file in this folder and tell the LLM "ingest [filename]".
