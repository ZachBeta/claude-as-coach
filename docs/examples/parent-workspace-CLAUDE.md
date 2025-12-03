# Parent Workspace CLAUDE.md (Example/Template)

**Status:** Experimental - Part of F33 sister directories pattern validation
**Use case:** Running Claude Code from parent workspace with both public and personal repos accessible
**Location:** Place this file at `claude-as-coach-combined/CLAUDE.md` (parent workspace root)

---

# Claude Code Workspace: claude-as-coach-combined

This workspace contains two independent git repositories:

```
claude-as-coach-combined/        # ← You are here (Claude Code working directory)
├── claude-as-coach/             # Public repo - base skills & documentation
│   ├── CLAUDE.md                # Detailed operational guidance
│   ├── skills/                  # Base skill frameworks (shareable)
│   ├── docs/                    # All documentation
│   └── scripts/                 # skill_workflow.py
└── claude-as-coach-personal/    # Private repo - personal data & extensions
    ├── documents/               # Daily summaries, retros, protocols
    ├── skills/                  # Personal skill extensions
    └── reference/               # Personal reference materials
```

## Primary Guidance

**See @claude-as-coach/CLAUDE.md for complete operational instructions**, including:
- Repository architecture (base + personal skill pattern)
- Skill workflow commands
- Git repository management
- Common development tasks
- Directory structure details

## Working from Parent Workspace

Running Claude Code from this parent directory allows access to both repositories simultaneously:

**Typical operations:**
```bash
# Pack base skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Git operations
cd claude-as-coach && git status
cd claude-as-coach-personal && git status
```

## Quick Reference

**Public repo (claude-as-coach/):**
- Base skill frameworks
- Documentation
- Example data (personal.example/)
- Vendor submodule (anthropics/skills)

**Private repo (claude-as-coach-personal/):**
- Your daily summaries and retrospectives
- Your personal skill extensions with metrics
- Your protocols and reference materials
- **Never committed to public repo**

## For Detailed Instructions

All operational guidance, workflows, and architecture details are in:
- **@claude-as-coach/CLAUDE.md** - Complete guide
- **@claude-as-coach/README.md** - Repository overview
- **@claude-as-coach/docs/WORKFLOW-GUIDE.md** - Skills and file management
- **@claude-as-coach/PROJECT-SETUP.md** - Setup instructions for adopters

---

**Note:** This parent-level CLAUDE.md is intentionally minimal. The detailed guidance lives in the public repo so it can be version-controlled and shared with contributors/adopters.
