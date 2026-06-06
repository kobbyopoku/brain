---
type: entity
title: Neo4j
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [Neo4j]
tags: [graph-database, database, stub]
---

# Neo4j

> Appears in this wiki via [[wiki/sources/daleverett-postgres-as-graph-pggraph]] as the dedicated graph database used as the memory-footprint comparison baseline for [[wiki/entities/pggraph|pgGraph]].

## Key facts

- **Role in source**: used as the baseline for [[wiki/entities/pggraph|pgGraph]]'s memory-footprint comparison (cited to [[wiki/sources/daleverett-postgres-as-graph-pggraph]])
- **Comparison result**: loading the LDBC dataset into Neo4j uses roughly 34x more memory than pgGraph because Neo4j stores row payloads, not just topology

## Mentioned in

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — dedicated graph database used as the memory-footprint comparison baseline.

## Related entities

- [[wiki/entities/pggraph]] — the Postgres extension compared against Neo4j on memory footprint.

## Related concepts

- (none yet)
