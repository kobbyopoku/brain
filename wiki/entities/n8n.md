---
type: entity
title: n8n
entity_type: product
created: 2026-05-02
updated: 2026-06-06
website: https://github.com/n8n-io/n8n
aliases: [n8n-io/n8n, N8N]
tags: [workflow-automation, integration, open-source]
---

# n8n

> Self-hosted workflow automation platform with 400+ integrations and native AI nodes. Positioned in [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] as the "ops hire replacement" — every internal tool and workflow a team used to build from scratch.

## Profile

n8n is a self-hosted workflow automation platform with 400+ integrations and native AI nodes, positioned in [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] as the "ops hire replacement." Across the agentic-AI sources in this wiki it recurs as the **orchestration / automation layer** of larger stacks: in CyrilXBT's personal operating system it is "Layer 3," running on a "$5 server" to schedule workflows, fire triggers, call the Claude API, and pass information between systems ([[wiki/sources/cyrilxbt-personal-operating-system]]); in CyrilXBT's Obsidian-dashboard build it runs the morning briefing as a 6 AM cron job ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]); and ColdIQ's Reply Manager agent runs on n8n ([[wiki/sources/itsalexvacca-3-phases-ai-layer]]). One source frames it less favorably — as a drag-and-drop no-code tool being "outclassed" by agentic workflows ([[wiki/sources/exploraX_-5-solo-ai-business-models]]).

## Key facts

- **Repo**: https://github.com/n8n-io/n8n
- **Integrations**: 400+ (per [[wiki/sources/heynavtoor-10-repos-replace-eng-team]]).
- **AI capability**: native AI nodes.
- **Deployment**: self-hosted; can run on a "$5 server" ([[wiki/sources/cyrilxbt-personal-operating-system]]).
- **Role per heynavtoor**: ops hire replacement.
- **Role in CyrilXBT's stack**: Layer 3 (automation) — schedules workflows, fires triggers, calls the Claude API, passes data between systems; used to build five workflows as cron jobs incl. a 6 AM morning briefing ([[wiki/sources/cyrilxbt-personal-operating-system]], [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Role in ColdIQ's stack**: runtime for the Reply Manager agent ([[wiki/sources/itsalexvacca-3-phases-ai-layer]]).

## Positions and claims

- Framed as a **no-code automation tool being outclassed by agentic workflows** in [[wiki/sources/exploraX_-5-solo-ai-business-models]] — a contrarian framing against the orchestration-layer role it plays in the other sources.

## Mentioned in

- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — ops hire replacement; 400+ integrations, native AI nodes, self-hosted.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — Layer 3 (automation) on a "$5 server"; schedules workflows, calls the Claude API, builds five cron-job workflows.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — runs the morning briefing as a 6 AM cron job, depositing it in the daily note before the user opens their laptop.
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]] — runtime for ColdIQ's Reply Manager agent.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — named as a no-code automation tool being outclassed by agentic workflows.

## Related entities

- [[wiki/entities/coolify]] — sibling self-hosted tool (DevOps-flavored).
- [[wiki/entities/posthog]] — sibling self-hosted tool (analytics).
- [[wiki/entities/chatwoot]] — sibling self-hosted tool (support).

## Related concepts

- [[scheduled-automation]] — adjacent: n8n is often the runtime for scheduled workflows.
- [[ai-automation-services]] — n8n is a common building block in this domain.
