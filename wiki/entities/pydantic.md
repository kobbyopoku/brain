---
type: entity
title: Pydantic
entity_type: product
created: 2026-06-06
updated: 2026-06-06
website: https://docs.pydantic.dev
aliases: [pydantic]
tags: [python, data-validation, structured-output, library]
---

# Pydantic

> Python data-validation library. In this wiki it appears as the tool used to define the **teacher's structured-output JSON schema** in [[wiki/sources/athletickoder-building-agents-first-principles|On Building Agents From First Principles]].

## Profile

Pydantic provides `BaseModel` / `Field` primitives for declaring typed data models in Python. In the first-principles agent-building tutorial it defines the schema the teacher model must emit, and its generated JSON schema is handed to the LLM's structured-output mode so the teacher's responses are machine-parseable.

## Key facts

- **Used in `teacher_generate.py`** via `BaseModel` / `Field` to define the `CreateShape`, `Connect`, and `AgentResponse` models (cited to [[wiki/sources/athletickoder-building-agents-first-principles]]).
- **`AgentResponse.model_json_schema()`** supplies the `response_json_schema` passed to [[wiki/entities/gemini|Gemini]] structured output (cited to [[wiki/sources/athletickoder-building-agents-first-principles]]).

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]] — defines the teacher's structured-output JSON schema (CreateShape / Connect / AgentResponse models).

## Related concepts

- [[markdown-as-agent-contract]]
