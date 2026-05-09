---
type: entity
title: Blockify
entity_type: product
created: 2026-05-09
updated: 2026-05-09
website: https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization
aliases: []
tags: [rag, retrieval, preprocessing, ideablocks, iternal-technologies, open-source, stub]
---

# Blockify

> Open-source RAG preprocessing layer by Iternal Technologies. **Replaces the chunk-as-unit assumption** with **IdeaBlocks** — typed atomic claims (one question + validated answer + governance fields). Surfaced via [[wiki/entities/akshay_pachaar|Akshay Pachaar's]] *"You're doing RAG wrong"* thread. Internal benchmark: 2.29× retrieval-distance reduction; 13.55% vector-accuracy improvement after semantic deduplication; 40× corpus-size reduction.

## Profile

This page is a **stub**. Blockify appears in the wiki via Akshay's surfacing thread. Repo: https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization.

## Key facts

- **License**: open-source.
- **Maintainer**: Iternal Technologies.
- **Atomic unit**: **IdeaBlock** = `{ question, validated_answer, typed_governance_fields }`. Each block is a single claim, not a window of prose.
- **Pipeline** (7 stages): Scoping → Ingestion → Chunking & extraction → Semantic deduplication → Auto-tagging → Human validation → Export.
- **Models used**: fine-tuned LLaMA 3 / QWEN 3.5 / Gemma 4 (and other custom foundation model variants).
- **Hardware**: GPU-optimized; CPU fallback via Intel Xeon optimized version.
- **Supported vector stores**: Azure AI Search, Pinecone, Milvus, Vertex Matching Engine.
- **Supported embeddings**: OpenAI, Bedrock, Mistral, Jina, open-source.
- **Internal benchmark** (17 documents, 298 pages):
  - 2,042 raw IdeaBlocks → 1,200 canonical (after iterative dedup at 80-85%, 3-5 rounds).
  - Word count: 88,877 → 44,537.
  - Cosine retrieval distance: 0.1585 (IdeaBlocks) vs 0.3624 (naive chunks) = **2.29× reduction**.
  - Distilled outperformed undistilled by **13.55% on vector accuracy**.

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — canonical surfacing source.

## Related concepts

- [[retrieval-augmented-generation]] — Blockify is the upstream-preprocessing fix.
- [[markdown-as-agent-contract]] — IdeaBlock's typed-fields shape is the meta-pattern applied to RAG.
- [[mcp-server]] — adjacent (Blockify could feed MCP-served knowledge bases).

## Related entities

- [[wiki/entities/akshay_pachaar]] — surfacing author.
- [[wiki/entities/iternal-technologies]] — maintainer (not yet stubbed; future ingest candidate).
