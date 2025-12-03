# F32: Skill Workflow Git Operations

**Status:** Deferred (removed from skill_workflow.py 2025-12-01)
**Effort:** Path B (30-45 min to re-implement if needed)
**Priority:** Low (out of scope for demo)

## Context

During pre-presentation simplification (Dec 2025), removed git-related functionality from `skill_workflow.py` to focus the script on its core pack/unpack responsibilities. These features were working but added complexity not needed for demo purposes.

## Removed Features

### 1. `commit` Command

**Functionality:**
- Automated git commit workflow for skill files
- Auto-generated commit messages (format: `"skill: Update {skill_name} skill"`)
- Interactive confirmation prompt
- Works with both `.skill` files and directories

**Usage:**
```bash
# Commit with auto-generated message
python scripts/skill_workflow.py commit skills/daily-summary-base/ -m "Description"

# Skip confirmation
python scripts/skill_workflow.py commit daily-summary-base.skill -y
```

**Implementation details:**
- Checked for uncommitted changes via `git diff --quiet`
- Staged file with `git add`
- Committed with standardized message prefix `"skill: "`
- Showed diff summary before committing

### 2. `_show_diff_summary()` Function

**Functionality:**
- Visual diff display for skill ZIP files
- Extracted old (HEAD) and new (working) versions
- Compared SKILL.md contents
- Showed first 20 lines of unified diff

**Implementation details:**
- Used `git show HEAD:{path}` to retrieve old version
- Extracted both ZIPs to temp directories
- Ran `diff -u` on SKILL.md files
- Truncated output for readability

### 3. `edit` Command

**Functionality:**
- Combined unpack + editor opening
- Configurable editor (default: `code`)

**Usage:**
```bash
python scripts/skill_workflow.py edit daily-summary-base.skill -e vim
```

**Implementation details:**
- Called `unpack_skill()` with force=False
- Opened SKILL.md in specified editor via `subprocess.run([editor, path])`

## Rationale for Removal

**For demo purposes:**
- Core workflow is pack/unpack, not git automation
- Users can use standard `git add` / `git commit` commands
- Reduces script complexity and dependencies
- Fewer things to break or explain

**Deferred, not deleted:**
- Functionality preserved in git history (pre-2025-12-01)
- Can be restored if needed for production use
- May be valuable for n=10+ users in future

## Manual Workflow (Replacement)

**Instead of `commit` command:**
```bash
# Pack skill
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Standard git workflow
git add skills/daily-summary-base.skill
git commit -m "Update daily-summary-base skill"
```

**Instead of `edit` command:**
```bash
# Option 1: Edit source directly (if already unpacked)
code skills/daily-summary-base/SKILL.md

# Option 2: Unpack then edit
python scripts/skill_workflow.py unpack daily-summary-base.skill
code skills/daily-summary-base/SKILL.md
```

**Instead of diff summary:**
```bash
# View git diff on .skill file (binary)
git diff skills/daily-summary-base.skill

# For meaningful diff, compare source directories
git diff skills/daily-summary-base/SKILL.md
```

## Related Features

- **F12: Python Tooling Improvements** - Testing framework would have needed to mock git operations
- **F21: Remove _fallback_pack()** - Another simplification opportunity
- **F23: Production/Development Workflow** - May need git tagging for deployments

## Future Considerations

**If re-implementing:**
- Consider integrating with F23 (dev/prod workflow) for deployment tagging
- Add `git diff` integration for source directories (not ZIPs)
- Support submodule-aware commits (personal/ vs main repo)
- Add pre-commit validation hooks

**Alternative approach:**
- Use git hooks or Makefile for commit automation
- Use IDE/editor integrations instead of CLI commands
- Keep Python script focused solely on skill packaging

## Code Location

**Removed from:** `scripts/skill_workflow.py` (lines 195-308)
**Git history:** Available pre-2025-12-01 commits
**Restore command:** `git show HEAD~1:scripts/skill_workflow.py`

## Decision Log

**2025-12-01:** Removed to simplify script for demo purposes. Core pack/unpack functionality sufficient. Git operations can use standard git CLI commands.
