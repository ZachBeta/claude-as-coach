# FEATURE: Workflow Cleanup

**Status:** In Progress (Partial completion)
**Effort:** Path B (30-45 min implementation + 15-20 min testing)
**Priority:** Medium

## Recent Changes (2025-11-29)

✅ **Completed: Import cleanup and validation**
- Removed unused `validate_skill` import from `skill_workflow.py` (only used internally by `package_skill`)
- Removed dead `validate` parameter from `pack_skill_wrapper()` function
- Removed non-functional `--no-validate` CLI flag
- Validation now always runs automatically when vendor `package_skill` is available
- Updated all documentation (CLAUDE.md, WORKFLOW-GUIDE.md) to remove `--no-validate` references

✅ **Completed: VSCode/IDE integration**
- Added `.vscode/settings.json` pattern with `python.analysis.extraPaths` for vendor submodule
- Added `.vscode/` to `.gitignore` to maintain IDE-agnostic project structure
- Documented VSCode setup in CLAUDE.md under "Development Setup (Optional)"

🔄 **Remaining: Legacy code paths**
- Still need to remove `skills-working/` code path (legacy unpack/repack cycle)
- Still need to remove `WORKING_DIR` from `skill_workflow.py`
- `unpack` command may be vestigial for base/personal skills (sources already tracked in git)

## Goal

Fix `skill_workflow.py` vendor script integration and improve git workflow for base+personal skill pairs.

## Current Issues

1. **Vendor integration broken/confusing**
   - Script tries to import vendor scripts, falls back to manual ZIP
   - Fallback might hide integration issues
   - User wants vendor scripts ALWAYS used when available

2. **Unpack/repack cycle painful**
   - Base/personal skills have source already unpacked in `skills/NAME-base/` and `personal/skills/NAME-personal/`
   - Why would you ever "unpack" them?
   - Unpack may be vestigial from standalone skill era

3. **Git workflow doesn't handle pairs**
   - `commit` command only handles single skills
   - Need to handle paired base+personal commits together
   - Should prompt which one(s) to commit? Auto-commit both?

## Investigation Needed

### Phase 1: Understand Vendor Scripts
- [ ] Read `vendor/skills/skill-creator/scripts/package_skill.py` - API and usage
- [ ] Read `vendor/skills/skill-creator/scripts/quick_validate.py` - validation logic
- [ ] Read `vendor/skills/skill-creator/scripts/init_skill.py` - initialization logic
- [ ] Test current vendor integration - what actually breaks?

### Phase 2: Analyze Current Workflow
- [ ] Map current `skill_workflow.py` behavior for base/personal/legacy
- [ ] Identify actual pain points in current implementation
- [ ] Determine what `unpack` should do (or if it should exist for base/personal)

## Design Questions

**Vendor integration:**
- What's the function signature for `package_skill()`?
- Does vendor `package_skill()` handle output naming for our base/personal pattern?
- What's the actual error/confusion with current integration?

**Workflow:**
- For base/personal skills, when would you ever "unpack"?
- Should `unpack` command be removed for base/personal, kept only for legacy standalone skills?
- What's the ideal "edit → pack → commit" flow?

**Git workflow:**
- How should `commit` command work with paired base+personal skills?
- Should it auto-commit both if both changed?
- Should it prompt which one(s) to commit?
- Different commit messages for base vs personal?

## Implementation Plan

### Phase 3: Design Improved Workflow
- [ ] Design clean vendor script integration
- [ ] Design git workflow for paired skills
- [ ] Simplify pack/edit commands for base/personal (no unpack needed)
- [ ] Update CLI help/documentation

### Phase 4: Implementation
- [ ] Refactor `skill_workflow.py` with cleaner vendor integration
- [ ] Add paired base+personal commit support
- [ ] Update documentation (CLAUDE.md, WORKFLOW-GUIDE.md)
- [ ] Test workflow with real skills

## Related Files

- `scripts/skill_workflow.py` - Workflow script to be refactored
- `vendor/skills/skill-creator/scripts/` - Official anthropics skill tools
- `docs/WORKFLOW-GUIDE.md` - Current workflow documentation
- `CLAUDE.md` - Project instructions (will need updates)

## Notes

- User confirmed vendor scripts should ALWAYS be used when available (not optional fallback)
- Base/personal skills have source already unpacked - unpack operation may be vestigial
- Current script tries to import vendor, falls back to manual ZIP

## Next Steps

1. Run investigation Phase 1 (vendor script analysis)
2. Test current workflow to identify actual breakage
3. Document findings in this file
4. Proceed with design and implementation
