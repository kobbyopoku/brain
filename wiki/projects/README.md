# wiki/projects/

One markdown page per active or historical project the human is (or was) working on. Each page captures the **durable summary** of a project — what it is, the stack, current focus, key decisions, lessons learned — so the brain knows about every project across all sessions and projects.

**Distinct from `wiki/entities/`**: an entity is something the wiki *references* (a person, an organization, a tool); a project is something the human is *building*. Projects have lifecycle (`status: active | paused | completed | exploring | archived`), changing state (current focus updates frequently), and a back-reference relationship with their own repo (typically a gitignored `BRAIN.md` at the project root pointing here).

**Distinct from project memory inside the project's own repo**: this directory holds *summary* state. Granular operational state (decisions log, error postmortems, session notes) belongs in the project's own repo, typically under `.memory/decisions/`, `.memory/errors/`, etc. — regent0x_ style. The brain only carries forward what's worth keeping if the project repo is ever archived.

## Conventions

- One page per project. Filename is kebab-case ASCII: `vedge.md`, `kivora.md`, `stace-sprouts.md`.
- Frontmatter `type: project` (a fourth wiki page type alongside source/entity/concept/synthesis).
- Use `templates/project.md` as the starting shape.
- Cross-reference into `wiki/entities/`, `wiki/concepts/`, `wiki/sources/` freely; that's how the brain accumulates project context.

## Workflows

- **Adding a project**: run `/brain-add-project` from inside the project's directory in any Claude Code session. The slash command surveys the project (README, stack manifest, recent git activity), discusses with you, then writes the page here. See `CLAUDE.md § Workflows → Adding a project`.
- **Updating a project**: `/brain-update-project` — re-survey + surgical edits to an existing page.
