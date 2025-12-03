# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository implements a **Claude-as-Coach** methodology using custom Claude skills for daily reflections, weekly retrospectives, and planning. The key innovation is separating skills into **base frameworks** (shareable) and **personal extensions** (private sibling repo).

**Presentation target:** December 5th, 2025

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

**Separated (Base + Personal):**
- `daily-summary` - End-of-day structured summaries
- `daily-morning-routine` - Morning context loading

**Standalone (No Separation):**
- `weekly-planning` - Week-ahead planning
- `weekly-retrospective` - Weekly reflection
- `backfill-summary` - Generate past summaries
- `context-continuation` - Session context management

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

### Demo Example Skills

**Rob (Base Skills Only) - Primary demo:**
```bash
# Rob uses base skills only (no custom personal skills)
# His documents in examples/rob-the-runner/documents/ demonstrate:
# - Daily summaries (Week 8 + Week 9)
# - Weekly retros (Weeks 5-7)
# - Monthly rollup (October, Weeks 1-4)
# - Weekly plan (Week 9 - post-program exploration)
# Shows fractal compression pattern + ongoing practice without needing custom skills
```

**Alice (Custom Skills) - Advanced demo:**
```bash
# Edit Alice demo skill
vim examples/alice-the-athlete/skills/daily-summary-alice-personal/SKILL.md

# Pack Alice skill (provide directory path)
python scripts/skill_workflow.py pack examples/alice-the-athlete/skills/daily-summary-alice-personal/

# Results in: examples/alice-the-athlete/skills/daily-summary-alice-personal.zip
```

**Gina (Skeleton) - Future demo:**
```bash
# Skeleton only - content TBD post-Dec 12 presentation
# Location: examples/gina-the-grad-student/
```

### Standalone Skills

```bash
# Edit source directly (tracked in git)
vim skills/weekly-planning/SKILL.md

# Pack (provide directory path)
python scripts/skill_workflow.py pack skills/weekly-planning/

# Commit using standard git commands
git add skills/weekly-planning/ skills/weekly-planning.zip
git commit -m "Description"
```

## Directory Structure

```
claude-as-coach-combined/           # Parent workspace (Claude Code runs here)
├── claude-as-coach/                # Public repo
│   ├── /skills/                    # Base skills
│   │   ├── /daily-summary-base/    # Base skill source (tracked)
│   │   ├── /daily-morning-routine-base/ # Base skill source (tracked)
│   │   └── /*.zip                  # Packed skill ZIP files
│   ├── /examples/                  # Demo personas (all synthetic/fictional)
│   │   ├── README.md               # Persona overview
│   │   ├── /rob-the-runner/        # Base skills only demo
│   │   │   ├── README.md           # Rob's background
│   │   │   └── /documents/         # Daily/weekly/monthly samples
│   │   ├── /alice-the-athlete/     # Custom skills demo
│   │   │   ├── README.md           # Alice's background
│   │   │   ├── /documents/         # Sample documents
│   │   │   └── /skills/            # Custom personal skills
│   │   └── /gina-the-grad-student/ # Career domain demo (skeleton)
│   │       ├── README.md           # Gina's background
│   │       └── /documents/         # Empty (TBD)
│   ├── /vendor/skills/             # Submodule: anthropics/skills fork
│   │   └── /skill-creator/scripts/ # Official packaging tools
│   ├── /scripts/
│   │   └── skill_workflow.py       # Primary workflow tool
│   └── /docs/
│       ├── WORKFLOW-GUIDE.md       # Complete workflow documentation
│       ├── features/
│       │   ├── FEATURE-presentation-prep.md    # F17: Dec 5th presentation
│       │   └── FEATURE-mcp-skill-manager.md    # F9: MCP integration
│       └── FEATURES.md             # Feature backlog
└── claude-as-coach-personal/       # Private sibling repo - AUTHOR'S DATA
    ├── /documents/                 # All project documents (flat structure)
    │                               # Contains: Summary-*.md, Retro-*.md, protocols, etc.
    └── /skills/                    # Personal skill extension sources
        ├── /daily-summary-personal/        # Personal skill source
        ├── daily-summary-personal.zip      # Packed personal skill
        └── /daily-morning-routine-personal/ # Personal skill source
```

**Note:** `claude-as-coach-personal/` is a separate git repository (sibling, not submodule). `examples/` contains three demo personas: Rob (base skills only), Alice (custom skills), and Gina (skeleton for career domain). All demo personas are synthetic/fictional.

## Git Repository Management

### Vendor Skills Submodule (anthropics/skills fork)
```bash
# Initialize if missing
git -C claude-as-coach submodule update --init --recursive

# Update to latest
git -C claude-as-coach/vendor/skills pull origin main
git -C claude-as-coach add vendor/skills
git -C claude-as-coach commit -m "Update vendor/skills"
```

**Integration:** `skill_workflow.py` automatically uses vendor tools when available, falls back to manual ZIP if not.

### Personal Repo (Sibling Directory)
```bash
# Commit new project documents
git -C claude-as-coach-personal add documents/Summary-2025-11-26-Tuesday.md
git -C claude-as-coach-personal commit -m "Add Tuesday summary"
git -C claude-as-coach-personal push origin main

# No cross-repo reference update needed - sibling repos are independent
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

## Skill Naming Convention (Production/Development)

**Context:** Claude.ai skills are global (not project-scoped), requiring careful naming to separate production use from development/testing.

**Naming pattern (decided 2025-11-29):**
- `production-*-personal.zip` - User's stable production skills
- `development-*-base.zip` - Shareable base frameworks
- `development-*-alice-personal.zip` - Alice demo (custom skills example)
- `development-*-rob-personal.zip` - Rob demo (base skills only, not applicable - Rob has no custom skills)

**Rationale:**
- **Primary user need (n=1 → n=100):** Safe skill iteration without breaking production workflow
- **Demo examples:** Alice (custom skills), Rob (base skills only, no custom skills needed)
- **Manual workflow acceptable:** Tooling deferred to F23 (post-Dec 12th presentation)

**Workflow for skill developers:**
1. Edit skill source in tracked directory (e.g., `skills/daily-summary-base/`)
2. Pack with appropriate prefix: `python scripts/skill_workflow.py pack daily-summary-base`
3. Manually rename: `mv skills/daily-summary-base.zip skills/development-daily-summary-base.zip`
4. Upload to Claude.ai
5. Toggle between production/development variants in Claude.ai settings

**Open questions (to be resolved in F17 Task 1):**
- Does frontmatter `name:` need to match .zip filename?
- Do duplicate YAML names cause conflicts in Claude.ai?
- Should environment prefix be in frontmatter or just filename?

**Future automation (F23):**
```bash
# Proposed future workflow
python scripts/skill_workflow.py pack daily-summary-base --env development
# Output: development-daily-summary-base.zip with appropriate frontmatter

python scripts/skill_workflow.py pack daily-summary-personal --env production
# Output: production-daily-summary-personal.zip
```

**See:** `docs/features/FEATURE-presentation-prep.md` (Task 1) for testing procedures and results.

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

## Testing Skills in Claude.ai

See `docs/features/FEATURE-presentation-prep.md` Task 1 for comprehensive testing procedures.

**Quick validation:**
1. Import both base + personal .zip files to Claude.ai Project
2. Test skill trigger (e.g., "daily summary")
3. Verify base framework structure appears
4. Verify personal metrics/thresholds appear
5. Check if `extends:` directive affects behavior

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

**Note:** For git operations, use standard git commands (`git add`, `git commit`). See [FEATURE-skill-workflow-git-ops.md](docs/features/FEATURE-skill-workflow-git-ops.md) for details on removed git automation features.

## Common Development Tasks

### Creating New Separated Skill

1. Create base source: `claude-as-coach/skills/new-skill-base/SKILL.md`
2. Create personal source: `claude-as-coach-personal/skills/new-skill-personal/SKILL.md`
3. Pack both (from workspace root):
   ```bash
   python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/new-skill-base/
   python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/new-skill-personal/
   ```
4. Test import to Claude.ai with both files

### Editing Existing Separated Skill

1. Edit source directly (no unpack needed)
2. Repack: `python scripts/skill_workflow.py pack <name>-base` or `pack <name>-personal`
3. Test in Claude.ai

### Converting Standalone to Separated

1. Unpack existing: `python scripts/skill_workflow.py unpack skills/existing.zip`
2. Create `skills/existing-base/SKILL.md` with framework only
3. Create `personal/skills/existing-personal/SKILL.md` with personal content
4. Pack both versions
5. Test, then remove old monolithic .zip file

### Bringing Skills from Claude.ai

**Use case:** Developed/edited skill in Claude.ai Projects → want to add to repository

**Workflow:**
1. Download .zip file from Claude.ai
2. Unpack to tracked location: `python scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip`
3. Review: `code skills/my-skill/SKILL.md`
4. Pack: `python scripts/skill_workflow.py pack skills/my-skill/`
5. Track: `git add skills/my-skill/ skills/my-skill.zip && git commit -m "Add my-skill from Claude.ai"`

**Destination options (from workspace root):**
```bash
# Default: claude-as-coach/skills/NAME/
python claude-as-coach/scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip

# Base framework:
python claude-as-coach/scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip --output-dir claude-as-coach/skills/my-skill-base/

# Personal extension:
python claude-as-coach/scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip --output-dir claude-as-coach-personal/skills/my-skill-personal/
```

## Vendor Tools

**Available in vendor/skills/skill-creator/scripts/:**
- `init_skill.py` - Initialize new skill structure
- `package_skill.py` - Package skill into .zip file
- `quick_validate.py` - Validate skill structure

**Note:** Our `pack_skill.py` creates nested structure per official docs. Vendor tools may differ.

## Documentation Files

**Reference documentation:**
- **WORKFLOW-GUIDE.md** - Complete workflow, submodule management, troubleshooting
- **FEATURES.md** - Feature backlog and tracking (3-level hierarchy)

**Feature planning (in docs/features/):**
- **FEATURE-presentation-prep.md** - F17: Dec 5th presentation prep (HIGH PRIORITY - has deadline)
- **FEATURE-workflow-cleanup.md** - F15: Fix skill_workflow.py vendor integration
- **FEATURE-directory-refactoring.md** - F16: Flatten personal/ directory structure
- **FEATURE-vendor-submodule.md** - F11: Vendor submodule update strategy

**Session handoff:**
- **docs/NEXT-SESSION.md** - Current status and next steps

## Python Dependencies

```bash
pip install -r scripts/requirements.txt  # Optional, for vendor validation scripts
```

Python 3.x required. No other dependencies for basic workflow.

## Development Setup (Optional)

### VSCode/IDE Configuration

If using VSCode, a `.vscode/settings.json` file enables Python path resolution for vendor submodule imports:

```json
{
  "python.analysis.extraPaths": [
    "${workspaceFolder}/vendor/skills/skill-creator/scripts"
  ]
}
```

**Note:** `.vscode/` is gitignored to keep IDE settings personal and maintain IDE-agnostic project structure.
