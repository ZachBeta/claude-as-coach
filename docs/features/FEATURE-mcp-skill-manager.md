# MCP Skill Manager - Design Document

## Overview

An MCP (Model Context Protocol) server that enables Claude.ai to save `.skill` archives directly to this repository, with automatic unpacking, validation, and version control integration.

**Status:** Design phase
**Created:** 2025-11-25
**Goal:** Eliminate manual file transfer when editing skills in Claude.ai

---

## Problem Statement

Currently, editing skills requires manual steps:
1. Download `.skill` file from Claude.ai
2. Manually save to `skills/` directory
3. Run `skill_workflow.py unpack/pack/commit` commands
4. Handle git operations manually

**Desired state:** Claude.ai directly saves skills to the repo via MCP, with automatic commit handling.

---

## Architecture

### Components

```
skills-mcp/                      # MCP server package
├── pyproject.toml               # Python package config
├── README.md                    # MCP server documentation
└── src/
    └── skills_mcp/
        ├── __init__.py
        ├── server.py            # Main MCP server
        ├── config.py            # Configuration management
        └── handlers/
            ├── save.py          # save_skill_archive handler
            ├── list.py          # list_skills handler
            ├── get.py           # get_skill_content handler
            └── diff.py          # diff_skill handler
```

### Integration Points

- **Existing workflow:** Reuses `scripts/skill_workflow.py` functions
- **Git operations:** Via `subprocess` (matches current approach)
- **Validation:** Leverages `vendor/skills/` validation scripts

---

## MCP Tools Specification

### 1. save_skill_archive

Save a `.skill` file from Claude.ai to the repository with automatic commit.

**Parameters:**
```typescript
{
  skill_name: string;        // Base name (e.g., "planning")
  archive_data: string;      // Base64-encoded .skill ZIP file
  commit_message?: string;   // Optional custom message
  auto_commit?: boolean;     // Default: true
  dry_run?: boolean;         // Default: false, preview without saving
}
```

**Workflow:**
1. Decode base64 data
2. Validate ZIP structure (must contain `SKILL.md`)
3. Save to `skills/{skill_name}.skill`
4. Check git status (must be clean working directory)
5. Git add + commit with standardized message
6. Return status with commit hash

**Returns:**
```json
{
  "success": true,
  "skill_file": "skills/planning.skill",
  "commit_hash": "abc123def",
  "commit_message": "skill: Add constraint identification section",
  "files_changed": ["skills/planning.skill"],
  "validation": {
    "valid": true,
    "warnings": []
  }
}
```

**Error handling:**
- Invalid ZIP: Return error, don't save
- Missing SKILL.md: Return error
- Dirty working directory: Return error with status
- Git conflicts: Return error, suggest resolution

### 2. list_skills

Show all current skills in the repository with git status.

**Parameters:** None

**Returns:**
```json
{
  "skills": [
    {
      "name": "planning",
      "path": "skills/planning.skill",
      "size_bytes": 2644,
      "last_modified": "2025-11-25T11:08:00Z",
      "git_status": "clean",
      "last_commit": {
        "hash": "abc123",
        "message": "skill: Add constraint identification",
        "date": "2025-11-25T11:08:00Z"
      }
    }
  ],
  "total": 6,
  "working_directory_clean": true
}
```

### 3. get_skill_content

Retrieve and unpack a skill for Claude.ai to read/edit.

**Parameters:**
```typescript
{
  skill_name: string;        // Name of skill to retrieve
  include_metadata?: boolean; // Default: true
}
```

**Workflow:**
1. Find `skills/{skill_name}.skill`
2. Unpack ZIP to temporary location
3. Read `SKILL.md` content
4. Extract metadata from ZIP
5. Return structured data

**Returns:**
```json
{
  "skill_name": "planning",
  "content": "# Weekly Planning Skill\n\n## Instructions\n...",
  "metadata": {
    "files": ["SKILL.md"],
    "size_bytes": 2644,
    "created_date": "2025-11-23T14:01:00Z"
  },
  "git_info": {
    "last_modified": "2025-11-25T11:08:00Z",
    "commits_count": 3
  }
}
```

### 4. diff_skill

Show changes between working directory and committed version.

**Parameters:**
```typescript
{
  skill_name: string;
  context_lines?: number;    // Default: 3 (unified diff context)
}
```

**Workflow:**
1. Check if `skills/{skill_name}.skill` has uncommitted changes
2. Extract both HEAD and working versions
3. Generate unified diff of `SKILL.md` content
4. Return diff with stats

**Returns:**
```json
{
  "has_changes": true,
  "diff": "--- a/SKILL.md\n+++ b/SKILL.md\n@@ -10,3 +10,5 @@\n...",
  "stats": {
    "additions": 5,
    "deletions": 2,
    "files_changed": 1
  }
}
```

---

## Workflow Examples

### Example 1: Save edited skill from Claude.ai

**User:** Downloads edited `planning.skill` from Claude.ai, uploads to conversation

**Claude.ai calls MCP:**
```json
{
  "tool": "save_skill_archive",
  "arguments": {
    "skill_name": "planning",
    "archive_data": "UEsDBBQAAgAIAAAAIQD...",
    "commit_message": "Add constraint identification section"
  }
}
```

**MCP server:**
1. Decodes base64 → saves to `skills/planning.skill`
2. Validates ZIP structure ✓
3. Checks git status (clean) ✓
4. Runs: `git add skills/planning.skill`
5. Commits: `skill: Add constraint identification section`
6. Returns commit hash

**Claude.ai response:**
"✅ Saved and committed planning.skill (commit: abc123def)"

### Example 2: Preview changes before saving

**Claude.ai calls:**
```json
{
  "tool": "save_skill_archive",
  "arguments": {
    "skill_name": "planning",
    "archive_data": "UEsDBBQAAgAIAAAAIQD...",
    "dry_run": true
  }
}
```

**MCP returns:**
```json
{
  "success": true,
  "dry_run": true,
  "would_save_to": "skills/planning.skill",
  "validation": {"valid": true},
  "diff_preview": "--- a/SKILL.md\n+++ b/SKILL.md\n..."
}
```

**Claude.ai:** Shows user the diff, asks for confirmation, then calls again with `dry_run: false`

---

## Implementation Plan

### Phase 1: Basic MCP Server (Path B: 30-45 min)

**Tasks:**
1. Create `skills-mcp/` package structure
2. Implement `save_skill_archive` tool (core functionality)
3. Implement `list_skills` tool (simple git queries)
4. Basic error handling and validation
5. Test with local MCP client

**Deliverable:** Working MCP server that can save skills

### Phase 2: Git Integration (Path A: 20-30 min)

**Tasks:**
1. Standardized commit message format
2. Git safety checks (clean working directory, no conflicts)
3. Integration with existing `skill_workflow.py` functions
4. Commit hash tracking and reporting

**Deliverable:** Full git automation with safety checks

### Phase 3: Advanced Tools (Path A: 20-30 min)

**Tasks:**
1. Implement `get_skill_content` (read/unpack)
2. Implement `diff_skill` (change preview)
3. Add `dry_run` mode for all operations
4. Enhanced validation using vendor scripts

**Deliverable:** Complete MCP toolset

### Phase 4: Testing & Documentation (Path A: 15-20 min)

**Tasks:**
1. Integration tests with Claude.ai
2. Error scenario testing
3. Update README with MCP setup instructions
4. Add examples to documentation

**Deliverable:** Production-ready MCP server

---

## Configuration

### MCP Server Config

**File:** `~/.config/claude/mcp.json` (or equivalent for Claude.ai)

```json
{
  "mcpServers": {
    "skills": {
      "command": "python",
      "args": ["-m", "skills_mcp"],
      "env": {
        "SKILLS_REPO_PATH": "/path/to/claude-as-coach"
      }
    }
  }
}
```

### Environment Variables

- `SKILLS_REPO_PATH`: Absolute path to this repository
- `GIT_AUTHOR_NAME`: (optional) Override git author
- `GIT_AUTHOR_EMAIL`: (optional) Override git email
- `SKILLS_AUTO_COMMIT`: (optional) Default for auto_commit flag
- `SKILLS_REQUIRE_CLEAN`: (optional) Require clean working directory (default: true)

---

## Security Considerations

### Path Validation
- **Constraint:** Only allow saves to `skills/` directory
- **Implementation:** Validate skill_name has no path separators (`/`, `\`)
- **Reject:** Absolute paths, parent directory references (`..`)

### ZIP Bomb Protection
- **Max archive size:** 10 MB (configurable)
- **Max extraction size:** 50 MB
- **Max file count:** 100 files
- **Implementation:** Check ZIP central directory before extraction

### Git Safety
- **Never force-push:** Read-only git operations except add/commit
- **Clean working directory check:** Refuse to commit if dirty
- **No credential storage:** Use system git credentials
- **Atomic operations:** Roll back on failure

### Input Validation
- **Base64 decoding:** Validate before processing
- **ZIP structure:** Verify central directory integrity
- **SKILL.md presence:** Required file validation
- **File size limits:** Prevent resource exhaustion

---

## Error Handling

### Common Errors

**E1: Invalid Archive**
```json
{
  "success": false,
  "error": "INVALID_ARCHIVE",
  "message": "File is not a valid ZIP archive",
  "suggestion": "Ensure you're uploading a .skill file downloaded from Claude.ai"
}
```

**E2: Dirty Working Directory**
```json
{
  "success": false,
  "error": "DIRTY_WORKING_DIRECTORY",
  "message": "Repository has uncommitted changes",
  "suggestion": "Commit or stash changes before saving new skill",
  "git_status": "M skills/another-skill.skill"
}
```

**E3: Git Conflict**
```json
{
  "success": false,
  "error": "GIT_CONFLICT",
  "message": "Skill has been modified both locally and remotely",
  "suggestion": "Pull latest changes and resolve conflicts manually"
}
```

**E4: Missing SKILL.md**
```json
{
  "success": false,
  "error": "MISSING_SKILL_MD",
  "message": "Archive does not contain SKILL.md",
  "suggestion": "Ensure the archive was created properly with skill metadata"
}
```

---

## Testing Strategy

### Unit Tests
```python
# Test save_skill_archive
def test_save_valid_skill():
    result = save_skill_archive("test-skill", valid_base64_data)
    assert result["success"] == True
    assert Path("skills/test-skill.skill").exists()

def test_reject_invalid_zip():
    result = save_skill_archive("bad-skill", invalid_data)
    assert result["success"] == False
    assert result["error"] == "INVALID_ARCHIVE"
```

### Integration Tests
```bash
# Test full workflow
python -m skills_mcp.test save_skill_archive \
  --skill-name test-skill \
  --archive-file test.skill \
  --commit-message "Test commit"

# Verify git log
git log -1 --oneline  # Should show: "skill: Test commit"
```

### Manual Testing with Claude.ai
1. Configure MCP in Claude.ai settings
2. Upload a `.skill` file to conversation
3. Ask Claude to save it via MCP
4. Verify commit appears in git log
5. Test error scenarios (dirty repo, invalid file, etc.)

---

## Dependencies

### Required
- **Python:** 3.10+
- **MCP SDK:** `@modelcontextprotocol/sdk` (Python bindings)
- **Git:** System git installation
- **zipfile:** Python standard library

### Optional
- **GitPython:** Alternative to subprocess for git operations
- **PyYAML:** For skill validation (already used by vendor scripts)

### Installation
```bash
cd skills-mcp
pip install -e .
```

---

## Future Enhancements

### Automatic Skill Diffing (Phase 5)
Before saving, automatically show Claude.ai what changed:
- Extract both old and new versions
- Generate side-by-side diff
- Claude reviews and approves before commit

### Skill Versioning (Phase 6)
Track semantic versions of skills:
- Tag skills with v1.0, v1.1, etc.
- Show version history
- Rollback to previous versions

### Multi-Skill Operations (Phase 7)
Batch operations:
- Save multiple skills in one operation
- Compare skills across versions
- Bulk validation

### Rollback Support (Phase 8)
Git operations:
- `rollback_skill(skill_name, commit_hash)` - Revert to previous version
- `cherry_pick_changes(skill_name, commit_hash)` - Apply specific changes

### MCP Tool: deploy_skills (Phase 9)
Package all skills for upload to Claude Projects:
```json
{
  "tool": "deploy_skills",
  "arguments": {
    "skills": ["planning", "daily-summary"],
    "output_dir": "/tmp/deploy"
  }
}
```

---

## Open Questions

1. **Commit granularity:** Should each skill save be a separate commit, or batch multiple changes?
   - Current plan: Separate commits for traceability
   - Alternative: Staging area, manual batch commit

2. **Branch strategy:** Should MCP create feature branches for skill edits?
   - Current plan: Direct commits to current branch
   - Alternative: Auto-create branch, require PR

3. **Conflict resolution:** How to handle concurrent edits from multiple sources?
   - Current plan: Fail fast, require manual resolution
   - Alternative: Automatic merge strategies

4. **Validation strictness:** Should validation failures block saves?
   - Current plan: Allow saves with warnings, block on errors
   - Alternative: Strict mode (configurable)

---

## Success Metrics

**Primary goals:**
- ✅ Eliminate manual file transfers for skill edits
- ✅ Maintain full git history of skill evolution
- ✅ Preserve safety (no data loss, no corrupt commits)

**Measurable outcomes:**
- Time to save edited skill: < 5 seconds (vs. ~60 seconds manual)
- Error rate: < 1% (with clear error messages)
- Adoption: 100% of skill edits use MCP after implementation

---

## Related Documents

- [WORKFLOW-GUIDE.md](../WORKFLOW-GUIDE.md) - Current manual workflow
- [FEATURES.md](../FEATURES.md) - Feature backlog and priorities
- [scripts/skill_workflow.py](../../scripts/skill_workflow.py) - Existing Python workflow
- [README.md](../../README.md) - Repository overview

---

## Changelog

**2025-11-29:** Moved from `docs/MCP-SKILL-MANAGER.md` to `docs/features/FEATURE-mcp-skill-manager.md` to follow feature documentation convention
**2025-11-25:** Initial design document created
