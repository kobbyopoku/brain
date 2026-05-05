---
type: entity
title: multica
entity_type: product
created: 2026-05-05
updated: 2026-05-05
website: https://github.com/multica-ai
aliases: []
tags: [open-source, ai-tooling, daemon, multi-agent, lineage, stub]
---

# multica

> Open-source project by **multica-ai**, credited by [[wiki/entities/open-design|Open Design]] as a lineage source for *"daemon architecture, PATH-scan detection, agent-as-teammate model."* The architectural foundation of Open Design's multi-agent CLI runtime.

## Profile

This page is a **stub**. multica appears in the wiki only via Open Design's lineage attribution. The description is the most architecturally significant of the four lineage credits: **PATH-scan multi-agent detection** is the primitive that lets Open Design auto-spawn whichever of 15 coding-agent CLIs the user has installed. The "agent-as-teammate" framing is also distinct from the more common "agent-as-tool" mental model — implying a peer-collaboration runtime.

## Key facts

- **Maintainer**: multica-ai (GitHub org).
- **Role per Open Design**: contributed *"daemon architecture, PATH-scan detection, agent-as-teammate model."*
- **Architectural impact**: the reason Open Design works with 15 different CLIs without needing per-CLI integrations — the daemon scans `$PATH`, detects which agents are present, and spawns the user's choice.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]] — names multica in the Lineage section as the architectural foundation.

## Related entities

- [[wiki/entities/open-design]] — downstream consumer.
- [[wiki/entities/huashu-design]], [[wiki/entities/guizang-ppt-skill]], [[wiki/entities/open-codesign]] — sibling lineage projects.

## Related concepts

- *(future)* multi-agent-cli-detection — the PATH-scan primitive originates here.
