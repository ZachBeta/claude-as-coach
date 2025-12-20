# Document Housekeeping

Regular maintenance tasks for keeping documentation in sync with code changes.

**State:** See [DOC_HOUSEKEEPING_STATE.md](../DOC_HOUSEKEEPING_STATE.md) for current progress.

**Convention:** This follows the instructions/state pattern. See [DOC-WORKFLOWS.md](../DOC-WORKFLOWS.md).

---

## Directory Structure

| Location | Purpose | Examples |
|----------|---------|----------|
| `docs/` | Reference materials | WORKFLOW-GUIDE.md, FEATURES.md |
| `docs/features/` | Detailed feature docs | FEATURE-*.md |
| `docs/instructions/` | Workflow instruction docs | SESSION-PLANNING.md |
| `skills/` | Skill source directories | daily-summary-base/, planning-base/ |
| `CHANGELOG.md` | Completed work history | What shipped, when |

---

## When to Run

Run housekeeping after:
- Completing a feature or significant code change
- Renaming files, skills, or directories
- Adding/removing skills
- Before committing documentation updates

---

## Checklist

### 1. CHANGELOG.md

Drain completed work from other docs:

- [ ] Check FEATURES.md "Completed" section - move entries to CHANGELOG
- [ ] Check NEXT_SESSION.md "Completed This Session" - move entries to CHANGELOG
- [ ] Add new section for today's date if needed
- [ ] Keep entries concise but informative

### 2. FEATURES.md

Update feature tracking:

- [ ] Update status for active features
- [ ] Move completed items to "Completed" section
- [ ] Check touch counters (per FEATURE_HOUSEKEEPING.md)
- [ ] Update priority guidance if needed

### 3. Cross-Reference Audit

Check for stale references when renaming files/skills:

```bash
# Example: after renaming daily-summary-base -> daily-summary
grep -r "daily-summary-base" docs/
grep -r "daily-summary-base" skills/
```

Files commonly affected:
- CLAUDE.md usage examples
- FEATURES.md skill references
- WORKFLOW-GUIDE.md examples
- Feature docs in `docs/features/`

### 4. Skill Docs

When modifying skills:

- [ ] Update SKILL.md frontmatter if triggers changed
- [ ] Update WORKFLOW-GUIDE.md if workflow changed
- [ ] Re-pack skill after source changes: `python scripts/skill_workflow.py pack skills/NAME/`

---

## Common Patterns

### File/Skill Rename

When renaming:

1. `git mv old-name/ new-name/`
2. Update CLAUDE.md usage examples
3. Update docs that reference the old name
4. Add rename note to CHANGELOG
5. Run cross-reference audit

### Feature Complete

When completing a feature:

1. Mark complete in FEATURES.md (move to Completed section)
2. Delete detailed FEATURE-*.md doc (git preserves history)
3. Add summary to CHANGELOG under current date
4. Update DOC_HOUSEKEEPING_STATE.md if relevant

### Skill Update

When updating a skill:

1. Edit skill source in `skills/NAME/SKILL.md`
2. Re-pack: `python scripts/skill_workflow.py pack skills/NAME/`
3. Update any docs referencing the skill
4. Note changes in CHANGELOG if significant

---

## Future: Skill Evolution

This document may evolve into a skill (`doc-housekeeping-base`) that can:
- Automatically detect stale cross-references
- Suggest documentation updates after code changes
- Generate CHANGELOG entries
- Track documentation debt
