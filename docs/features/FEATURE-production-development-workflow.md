# F23: Production/Development Skill Workflow

**Effort:** Path C (1-2 hours implementation + testing)
**Priority:** Medium (post-Dec 12th)
**Status:** Manual workaround documented below. Automated tooling deferred until after presentation.

## Goal

Enable safe skill iteration without breaking production usage.

## User Problem (n=1 → n=100)

- Users want to test skill changes without breaking daily workflow
- Claude.ai skills are **global** (not project-scoped)—they affect all your projects
- Need versioning: production (stable) vs development (experimental)
- Can't experiment without breaking daily practice unless you have separate variants

**Why this matters for scaling:** Everyone who adopts this system will need this workflow. This is a core insight for making the system sustainable as it grows from n=1 → n=100.

## Manual Workaround (Current)

**Technical context (as of December 2025):** Claude.ai skills are **global** across all your projects, not project-scoped. We use naming conventions (`production-`, `development-`) to create pseudo-namespaces and enable toggling between variants. This is a workaround for the current platform limitation. If Claude.ai adds project-scoped skills in the future, this naming convention may become unnecessary.

### Working Directory

When packing skills with different variants, work from the parent workspace directory:

```bash
cd claude-as-coach-combined  # Start here
```

All example commands in this section use this working directory.

### Naming Convention

**Production skills** (your stable daily-use skills):
- `production-daily-summary-personal.skill`
- `production-daily-morning-routine-personal.skill`
- `production-weekly-retrospective-personal.skill`
- `production-weekly-planning-personal.skill`

**Development skills** (for testing changes):
- `development-daily-summary-personal.skill`
- `development-daily-morning-routine-personal.skill`
- `development-weekly-retrospective-personal.skill`
- `development-weekly-planning-personal.skill`

### Workflow for Testing Changes

1. **Copy** your production skill → create development variant
2. **Edit** the development variant to test your changes
3. **Toggle** in Claude.ai settings: Development ON, Production OFF
4. **Test** the changes in your project
5. **Validate** that changes work as expected
6. **Update** your production skill with the validated changes
7. **Toggle** back: Production ON, Development OFF

**Manual workflow is acceptable** for current scale (n=1). Future tooling will automate this, but for solo use, manual copying and toggling works fine.

## Future: Automated Tooling

### Proposed Workflow

```bash
# Pack for production use
python scripts/skill_workflow.py pack daily-summary-personal --env production
# Output: production-daily-summary-personal.skill

# Pack for development/testing
python scripts/skill_workflow.py pack daily-summary-personal --env development
# Output: development-daily-summary-personal.skill

# Promote dev to production after testing
python scripts/skill_workflow.py promote daily-summary-personal
# Copies dev → prod, repacks as production variant
```

### Features

- `--env production|development` flag for pack command
- `promote` command to move validated changes dev → prod
- Handles frontmatter name matching automatically
- Prevents conflicts from duplicate YAML names

## Implementation Notes

- Test frontmatter name matching behavior during F17 Task 1
- Design informed by friend feedback at n~10 scale
- May integrate with F9 (MCP) for direct Claude.ai deployment

## Why Post-Dec 12th?

- Rob/Sally demos can use manual workflow (acceptable for examples)
- Real user friction will emerge when friends adopt (n~10)
- Better to build based on actual pain points, not assumptions
