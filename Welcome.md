# Welcome

This is **Kay's LLM Wiki** — a personal knowledge base that an LLM agent maintains for me, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Start here

- **[[CLAUDE]]** — the schema. Tells the LLM how this vault is organized and what to do.
- **[[index]]** — catalog of every wiki page, grouped by type.
- **[[log]]** — chronological record of operations (ingests, queries, lints).

## How it works

- I drop sources into `raw/` and ask the LLM to ingest them.
- The LLM owns everything in `wiki/`: source summaries, entity pages, concept pages, and syntheses. It maintains cross-references and flags contradictions.
- I read, browse, and ask questions. The LLM does the bookkeeping.
- Templates for new pages live in `templates/`.

## Common requests

- *"Ingest `raw/<file>`"* — process a new source; create/update wiki pages and append a log entry.
- *"What does the wiki say about X?"* — query against existing pages, with citations.
- *"Lint the wiki"* — health-check for contradictions, stale claims, orphans, missing pages.
- *"File this back as a synthesis"* — turn a substantive answer into a permanent `wiki/syntheses/` page.
