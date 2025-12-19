# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository implements a **Claude-as-Coach** methodology using custom Claude skills for daily reflections, weekly retrospectives, and planning. The key innovation is separating skills into **base frameworks** (shareable) and **personal extensions** (private sibling repo).

## Claude Code Operational Guidance

### Working Directory Options

This repository supports two working directory patterns:

#### Option A: Standalone (Recommended for most users)

Work directly from the `claude-as-coach/` directory:

```bash
cd claude-as-coach

# Pack base skills
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Git operations
git status
git add skills/
git commit -m "Update skills"
```

**Use when:**
- Working only with base skills
- Don't need simultaneous access to personal repo
- Want simpler, more direct paths

#### Option B: Parent Workspace (Advanced)

Work from parent workspace with both repos accessible:

```bash
cd claude-as-coach-combined  # Parent directory containing both repos

# Pack base skills
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Pack personal skills (if personal repo is sibling)
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Git operations for each repo
git -C claude-as-coach status
git -C claude-as-coach-personal status
```

**Use when:**
- Working with both base and personal repos simultaneously
- Using sibling directories pattern (see docs/examples/parent-workspace-CLAUDE.md)
- Need to coordinate changes across both repos

**Note:** Parent workspace setup is optional. See `docs/examples/parent-workspace-CLAUDE.md` for setup instructions.

## Architecture: Base + Personal Skill Pattern

### Two-Layer Design

**Base Skills** (`skills/NAME-base/`):
- Generic process frameworks, shareable publicly
- Date verification, file patterns, section structure, formatting rules
- NO personal metrics, thresholds, or domain-specific content

**Personal Extensions** (`claude-as-coach-personal/skills/NAME-personal/`):
- User-specific metrics, thresholds, protocols
- Domain terminology and context
- Private data in sibling git repo
- Uses `extends: base-skill-name` in frontmatter

**Import to Claude.ai:** Both base + personal .zip files are imported together for stacked behavior.

### Current Skill Status

**Daily Skills (Base + Personal):**
- `daily-summary` - End-of-day structured summaries (pure capture)
- `daily-morning-routine` - Morning context loading

**Unified Skills (Any Time Scale):**
- `planning` - Forward planning with constraints (daily/weekly/monthly/quarterly/yearly)
- `retrospective` - Reflection and pattern extraction (daily/weekly/monthly/quarterly/yearly)

**Setup:**
- `project-coach-setup` - Initial project setup and goal definition

## Skill Workflow Commands

### Base Skills (Main Repo)

```bash
# Edit base skill source directly
vim skills/daily-summary-base/SKILL.md

# Pack base skill (provide directory path)
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Results in: skills/daily-summary-base.zip (in parent directory)
```

### Personal Skills (Sibling Repo)

```bash
# Edit personal extension (in sibling repo)
vim ../claude-as-coach-personal/skills/daily-summary-personal/SKILL.md

# Pack personal skill (provide directory path, run from workspace root)
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Results in: claude-as-coach-personal/skills/daily-summary-personal.zip
```

### Demo Examples

Demo personas in `examples/`:
- **rob-the-runner/** - Base skills only (primary demo)
- **alice-the-athlete/** - Custom skills demo
- **gina-the-grad-student/** - Career domain (skeleton)

## Directory Structure

```
claude-as-coach/                # This repo (public)
├── skills/                     # Base skill sources + .zip files
├── examples/                   # Demo personas (rob, alice, gina)
├── vendor/skills/              # Submodule: anthropics/skills fork
├── scripts/skill_workflow.py   # Pack/unpack tool
└── docs/                       # WORKFLOW-GUIDE.md, FEATURES.md

claude-as-coach-personal/       # Sibling repo (private)
├── documents/                  # Summary-*.md, Retro-*.md, etc.
└── skills/                     # Personal skill extensions
```

**Note:** `claude-as-coach-personal/` is a separate git repo (sibling, not submodule).

## Git Management

```bash
# Initialize vendor submodule
git submodule update --init --recursive

# Sibling repos are independent - no cross-repo reference updates needed
```

## Skill File Format

Skills are ZIP archives with `.zip` extension containing:
- Directory named after skill (e.g., `daily-summary-base/`)
- `SKILL.md` inside that directory with frontmatter and markdown instructions

**Structure:**
```
my-skill.zip
└── my-skill/
    ├── SKILL.md
    └── resources/  (optional)
```

**Frontmatter example (base):**
```yaml
---
name: daily-summary-base
description: Framework for creating end-of-day summary documents
---
```

**Frontmatter example (personal):**
```yaml
---
name: daily-summary-personal
extends: daily-summary-base
description: Personal extensions with specific metrics
---
```

## Critical Principles

### Skill Separation Guidelines

**When separating skills, put in BASE:**
- Process frameworks (date verification, confirmation flows)
- File naming patterns and structure
- Section templates and formatting rules
- Edge case handling
- Markdown/ASCII formatting guidelines

**When separating skills, put in PERSONAL:**
- Specific metrics and thresholds
- Domain-specific terminology
- Personal protocols and interventions
- Example data with actual values
- Context tags and experimental state

### File Naming Conventions

**Summary files:** `Summary-YYYY-MM-DD-DayName-context-tag.md`
- Date = date OF events (not FOR next day)
- Example: `Summary-2025-11-26-Tuesday-W5-D2.md`

**Skill directories match .zip filenames:**
- `claude-as-coach/skills/daily-summary-base/` → `claude-as-coach/skills/daily-summary-base.zip`
- `claude-as-coach-personal/skills/daily-summary-personal/` → `claude-as-coach-personal/skills/daily-summary-personal.zip`

### README Privacy

Main README.md must NOT contain personal health information. Uses couch-to-5k running training as example use case instead. Personal context stays in private sibling repo.

## Skill Workflow Script API

```bash
# Pack skill (provide directory path)
python scripts/skill_workflow.py pack <path/to/skill-directory/>
# Output: <path/to/skill-directory.zip> (in parent directory)

# Unpack .zip file (extracts next to .zip file by default)
python scripts/skill_workflow.py unpack <path/to/skill.zip> [--output-dir DIR] [--force]
# Output: <path/to/skill-directory/>
```

**Convention:**
- **Directory name = .zip filename** (always)
- Pack outputs to parent directory of skill directory
- Unpack extracts to sibling directory of .zip file
- No name parsing or searching - explicit paths only
- ZIP contains nested structure: `skill-name/SKILL.md`

**Note:** For git operations, use standard git commands. See `docs/WORKFLOW-GUIDE.md` for detailed workflows (creating skills, importing from Claude.ai, etc.).

## Reference

- **docs/WORKFLOW-GUIDE.md** - Complete workflows, troubleshooting, vendor tools
- **docs/FEATURES.md** - Feature backlog
- **vendor/skills/** - Anthropic skill-creator tools (submodule)

Python 3.x required. Optional: `pip install -r scripts/requirements.txt` for vendor validation.
