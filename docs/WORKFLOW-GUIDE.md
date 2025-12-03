# Workflow Guide: Managing Skills & Personal Files

## Overview

This repository uses:
- **Python workflow** (`skill_workflow.py`) for editing `.zip` ZIP files
- **Sibling directories** for isolation (public repo + private sibling repo)
- **Git submodule** only for vendor code (anthropics/skills fork)
- **Flat structure** for skills (no subdirectories)

## Directory Structure

```
claude-as-coach-combined/             # Parent workspace
├── claude-as-coach/                  # Public repo
│   ├── /docs/                        # All documentation
│   ├── /skills/                      # Skills (.zip ZIPs and sources)
│   │   ├── /daily-summary-base/      # Base skill source
│   │   ├── /daily-morning-routine-base/ # Base skill source
│   │   └── /*.zip                  # Packed skill files
│   ├── /vendor/skills/               # Submodule → anthropics/skills fork
│   └── /scripts/                     # skill_workflow.py
└── claude-as-coach-personal/         # Private sibling repo
    ├── /documents/                   # Generated outputs (flat structure)
    │                                 # Daily summaries, weekly retros, etc.
    └── /skills/                      # Personal skill extensions
        ├── /daily-summary-personal/  # Personal metrics & context
        ├── daily-summary-personal.zip # Packed personal skill
        └── /daily-morning-routine-personal/ # Personal protocols
```

## Primary Workflow: Editing Skills

Skills are stored as `.zip` ZIP files. Use `skill_workflow.py` for all operations.

## Two Skill Patterns

### Pattern 1: Base + Personal (Separated Skills)

**For skills that benefit from separation:**
- **Base skills**: Generic frameworks (shareable) - edit sources directly in `claude-as-coach/skills/NAME-base/`
- **Personal skills**: User-specific extensions (private) - edit sources in `claude-as-coach-personal/skills/NAME-personal/`

**Workflow (from workspace root):**
```bash
# Edit base skill
vim claude-as-coach/skills/daily-summary-base/SKILL.md

# Pack base skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Edit personal extension
vim claude-as-coach-personal/skills/daily-summary-personal/SKILL.md

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Import BOTH to Claude.ai for stacked behavior
```

**Current separated skills:**
- `daily-summary` (base framework + personal metrics)
- `daily-morning-routine` (base process + personal protocols)

### Pattern 2: Standalone Skills

**For skills that don't need separation:**

Use the traditional unpack/edit/pack workflow (see below).

**Current standalone skills:**
- `weekly-planning`
- `weekly-retrospective`
- `backfill-summary`
- `context-continuation`

### The Direct Edit-Pack-Commit Flow (Standalone Skills)

All skill sources are tracked in git. No unpacking needed!

#### Step 1: Edit Source Directly
```bash
# Open source directory in your editor
code skills/weekly-planning/SKILL.md

# Make your changes...
```

#### Step 2: Pack
```bash
python scripts/skill_workflow.py pack weekly-planning
```
Creates updated: `skills/weekly-planning.zip`

#### Step 3: Review & Commit
```bash
# Option A: Using the commit command
python scripts/skill_workflow.py commit weekly-planning -m "Add constraint identification"

# Option B: Manual git workflow
git add skills/weekly-planning/ skills/weekly-planning.zip
git commit -m "skill: Add constraint identification to weekly-planning"
```

### Bringing Skills from Claude.ai

**Use case:** You create/edit a skill within a Claude.ai Project conversation and want to add it to your tracked repository.

**Complete workflow:**

```bash
# 1. Download .zip file from Claude.ai (typically downloads to ~/Downloads/)

# 2. Unpack to tracked location
python scripts/skill_workflow.py unpack ~/Downloads/my-new-skill.zip

# Default: unpacks to skills/my-new-skill/
# Or specify destination:
python scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip --output-dir skills/my-skill-base/
python scripts/skill_workflow.py unpack ~/Downloads/my-skill.zip --output-dir personal/skills/my-skill-personal/

# 3. Review/edit extracted SKILL.md
code skills/my-new-skill/SKILL.md

# 4. Track in git
git add skills/my-new-skill/
git commit -m "Add my-new-skill from Claude.ai"

# 5. Repack for Claude.ai import
python scripts/skill_workflow.py pack my-new-skill
```

**Output directory patterns:**
- `skills/NAME/` - Standalone skill (default)
- `skills/NAME-base/` - Base framework skill
- `personal/skills/NAME-personal/` - Personal extension skill

**Force overwrite:**
If destination already exists, use `--force` to overwrite:
```bash
python scripts/skill_workflow.py unpack my-skill.zip --output-dir skills/my-skill/ --force
```

## Advanced Workflow Commands

### Force Overwrite
If skill is already unpacked:
```bash
python scripts/skill_workflow.py unpack skills/weekly-planning.zip --force
```

### Auto-Commit
Skip confirmation prompt:
```bash
python scripts/skill_workflow.py commit weekly-planning -m "Quick fix" -y
```

### Custom Editor
Use different editor:
```bash
python scripts/skill_workflow.py edit skills/weekly-planning.zip -e vim
```

## Managing Personal Files (Sibling Repo)

Personal files (project documents, skill extensions) live in a **private sibling repository**.

### Adding New Project Documents

```bash
# Files auto-save to claude-as-coach-personal/ if using the skills
cd claude-as-coach-personal/documents
ls  # Your new summary appears here

# Commit in personal repo
git add Summary-2025-11-24-Sunday.md
git commit -m "Add Sunday summary"
git push origin main

# No cross-repo reference update needed - sibling repos are independent
```

### Editing Personal Skill Extensions

```bash
# Edit personal extension (from workspace root)
vim claude-as-coach-personal/skills/daily-summary-personal/SKILL.md

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Commit in personal repo
cd claude-as-coach-personal
git add skills/daily-summary-personal/SKILL.md skills/daily-summary-personal.zip
git commit -m "Update daily summary personal extensions"
git push origin main

# No cross-repo reference update needed
```

### Pulling Latest Personal Files

```bash
cd claude-as-coach-personal
git pull origin main
# No cross-repo reference update needed
```

## Document Lifecycle & Archival

The claude-as-coach system uses a **fractal compression pattern** where documents at each timescale compress the level below. This keeps the Claude.ai Project context lean while preserving full history locally.

### Document Lifecycle Table

| Document Type | Created | Lives In Project | Archived After |
|---------------|---------|------------------|----------------|
| Daily Summary | End of day | Until weekly retro | Weekly retro exists |
| Weekly Plan | Sunday planning | During that week | Weekly retro exists |
| Weekly Retro | Sunday | Until monthly retro | Monthly retro exists |
| Monthly Retro | Month end | Until quarterly | Quarterly retro exists |

**Key principle:** Trust the compression. Each rollup IS the compressed reference for the documents below it. If something was important, it made it into the rollup.

### Compression Hierarchy

```
Daily Summaries (7 docs)
    ↓ compress into
Weekly Retro (1 doc)
    ↓ archive dailies locally

Weekly Retros (4-5 docs)
    ↓ compress into
Monthly Retro (1 doc)
    ↓ archive weeklies from project

Monthly Retros (3 docs)
    ↓ compress into
Quarterly Retro (1 doc)
    ↓ archive monthlies from project
```

**Result:** Project context stays lean, full history preserved locally, summary-of-summaries maintains continuity.

### Archival Workflow

#### After Weekly Retro Created
1. Weekly retro saved to `personal/documents/`
2. Daily summaries (7 docs) backed up locally (outside project)
3. Daily summaries removed from Claude.ai Project
4. Weekly retro becomes compressed reference for that week

#### After Monthly Retro Created
1. Monthly retro saved to `personal/documents/`
2. Weekly retros (4-5 docs) backed up locally
3. Weekly retros removed from Claude.ai Project
4. Weekly plans from that month also archived
5. Monthly retro becomes compressed reference for that month

#### After Quarterly Retro Created
1. Quarterly retro saved to `personal/documents/`
2. Monthly retros (3 docs) backed up locally
3. Monthly retros removed from Claude.ai Project
4. Quarterly retro becomes compressed reference for that quarter

### What to Keep in Project

**Current period only:**
- This week's daily summaries (until weekly retro)
- This week's plan (until weekly retro)
- This month's weekly retros (until monthly retro)
- This quarter's monthly retros (until quarterly retro)

**Current rollup:**
- Most recent weekly retro
- Most recent monthly retro (optional: keep current month's weeklies too)
- Most recent quarterly retro (optional: keep current quarter's monthlies too)

**Reference docs:** Living documents that don't follow rollup pattern (protocols, symptom tracking, etc.) stay in project indefinitely.

### Local Archival Strategy

Archived documents are preserved in the personal sibling repo, just removed from the active Claude.ai Project to reduce context size.

**Directory structure (local):**
```
claude-as-coach-personal/documents/
  Summary-2025-11-01-Friday.md         # Current week's dailies
  Summary-2025-11-02-Saturday.md
  ...
  Retro-2025-W5-Nov-17-23.md          # Current month's weeklies
  Retro-2025-W6-Nov-24-30.md
  Retro-2025-11-November.md           # Current quarter's monthlies
  archived/
    2025-11/                           # Archived monthlies for November
      dailies/                         # Archived dailies
      weeklies/                        # Archived weeklies
```

**Note:** Specific archival directory structure is still being validated. See `docs/design/MONTHLY-ROLLUP-DESIGN.md` for evolving best practices.

### Design Rationale

See `docs/design/MONTHLY-ROLLUP-DESIGN.md` for complete design rationale, including:
- Fractal compression principle
- Monthly rollup output structure
- Open questions being validated
- Plan vs actual integration options

## Vendor Skills Submodule

**Location:** `vendor/skills`
**Status:** ✓ Initialized and working
**Source:** https://github.com/ZachBeta/anthropics-skills (fork of anthropics/skills)
**Branch:** main (tracking)

### Available Vendor Tools

The vendor submodule provides official Anthropic skill utilities:

```bash
# Initialize a new skill structure
python vendor/skills/skill-creator/scripts/init_skill.py

# Package skill directory into .zip ZIP
python vendor/skills/skill-creator/scripts/package_skill.py

# Validate skill structure
python vendor/skills/skill-creator/scripts/quick_validate.py
```

### Integration with skill_workflow.py

Our `scripts/skill_workflow.py` automatically uses vendor tools when available:

```python
# Imported from vendor/skills
from package_skill import package_skill
# Note: validate_skill is called internally by package_skill
```

**Fallback behavior:** If vendor tools are unavailable, the script falls back to manual ZIP packaging. This ensures the workflow always works, even if submodules aren't initialized.

### Reference Skills in Vendor

The vendor submodule includes example skills you can reference:
- `template-skill` - Starter template for new skills
- `document-skills` - docx, pdf, xlsx, pptx handlers
- `mcp-builder` - MCP server development skill
- And more...

Browse `vendor/skills/` for additional reference implementations.

### Updating Vendor Skills

```bash
cd vendor/skills
git pull origin main
cd ../..
git add vendor/skills
git commit -m "Update vendor/skills to latest"
```

### Troubleshooting Vendor Tools

**Warning: "Could not import vendor scripts"**

This is informational - the workflow falls back to manual packaging. To use vendor tools:

```bash
# Initialize submodules
git submodule update --init --recursive

# Verify vendor scripts exist
ls vendor/skills/skill-creator/scripts/

# Install Python dependencies (if needed)
pip install -r scripts/requirements.txt
```

## Setup (One-Time)

### Cloning This Repo

```bash
# Create parent workspace
mkdir claude-as-coach-combined
cd claude-as-coach-combined

# Clone public repo with vendor submodule
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach

# Create your own private repo for personal data (optional)
git clone https://github.com/YOUR-USERNAME/claude-as-coach-personal
# OR: cp -r claude-as-coach/examples/rob-the-runner claude-as-coach-personal && cd claude-as-coach-personal && git init

# Or if already cloned (vendor submodule only):
cd claude-as-coach
git submodule init
git submodule update
```

### Installing Dependencies

```bash
# Optional: For vendor validation
pip install -r scripts/requirements.txt
```

## Tips & Best Practices

### Skill Development
- **Small commits**: Each meaningful change gets its own commit
- **Descriptive messages**: Use the `-m` flag with clear descriptions
- **Test in Claude**: Before committing, test the skill works as expected
- **Clean working directory**: Commit or stash changes before editing new skill

### Workflow Efficiency
- **Use `edit` command**: Combines unpack + open in one step
- **Review diffs**: The `commit` command shows automatic diff before committing
- **Force flag**: Use `--force` to overwrite existing unpacked skills

### Repository Management
- **Personal repo**: Commit + push daily summaries/retros as you create them (independent from public repo)
- **Public repo**: Track base skills and documentation
- **Vendor submodule**: Pull updates periodically to stay current

### File Organization
- **Skills**: Flat structure in `claude-as-coach/skills/` (base frameworks)
- **Personal**: Flat structure in `claude-as-coach-personal/documents/` (summaries, retros, protocols)
- **Docs**: All documentation in `claude-as-coach/docs/`
- **Scripts**: Minimal - just `skill_workflow.py` in `claude-as-coach/scripts/`

## Current Skills

### Separated Skills (Base + Personal)

| Skill | Base (Framework) | Personal (Extensions) |
|-------|-----------------|----------------------|
| **daily-summary** | `claude-as-coach/skills/daily-summary-base.zip` | `claude-as-coach-personal/skills/daily-summary-personal.zip` |
| **daily-morning-routine** | `claude-as-coach/skills/daily-morning-routine-base.zip` | `claude-as-coach-personal/skills/daily-morning-routine-personal.zip` |

**Import both base + personal to Claude.ai for full functionality.**

### Standalone Skills

| Skill | Purpose |
|-------|---------|
| `weekly-planning.zip` | Week-ahead planning with experiments |
| `weekly-retrospective.zip` | Weekly reflection and analysis |
| `backfill-summary.zip` | Generate summaries for past days |
| `context-continuation.zip` | Session context management |

## Troubleshooting

### "Vendor submodule not initialized"
```bash
cd claude-as-coach
git submodule init
git submodule update
```

### "Directory already exists"
Use `--force` flag:
```bash
python scripts/skill_workflow.py unpack skills/foo.zip --force
```

### "No changes detected"
The skill file is identical to committed version. No commit needed.

### "Vendor scripts not found"
Initialize submodules:
```bash
git submodule update --init --recursive
```

### "ZIP validation warnings"
These are informational messages from the vendor validation scripts. They are usually harmless and indicate style/formatting issues rather than errors. Validation runs automatically when vendor tools are available.

## Python Workflow Reference

### skill_workflow.py Commands

```bash
# Unpack skill for editing
python scripts/skill_workflow.py unpack <skill-file> [--force]

# Pack edited skill
python scripts/skill_workflow.py pack <skill-name>

# Commit skill changes
python scripts/skill_workflow.py commit <skill-name> [-m MESSAGE] [-y]

# Edit (unpack + open in editor)
python scripts/skill_workflow.py edit <skill-file> [-e EDITOR]
```

### Example Workflow

```bash
# Complete workflow for editing weekly-planning skill
code skills/weekly-planning/SKILL.md
# ... make edits ...
python scripts/skill_workflow.py pack weekly-planning
python scripts/skill_workflow.py commit weekly-planning -m "Add constraint identification section"
```

## Future: MCP Integration

See [features/FEATURE-mcp-skill-manager.md](features/FEATURE-mcp-skill-manager.md) for planned MCP server that will enable Claude.ai to save skills directly via Model Context Protocol.

**Benefits:**
- Eliminate manual file transfers
- Reduce save time from ~60s to <5s
- Automatic validation and git commits

## Related Documents

- [README.md](../README.md) - Repository overview
- [FEATURES.md](FEATURES.md) - Feature backlog
- [NEXT-SESSION.md](NEXT-SESSION.md) - Current status and next steps
- [design/MONTHLY-ROLLUP-DESIGN.md](design/MONTHLY-ROLLUP-DESIGN.md) - Monthly rollup design (fractal compression, output structure)
- [features/FEATURE-presentation-prep.md](features/FEATURE-presentation-prep.md) - F17 presentation prep (Task 1 has testing procedures)
- [features/FEATURE-monthly-rollup.md](features/FEATURE-monthly-rollup.md) - F26 monthly rollup (validation phase)
- [features/FEATURE-mcp-skill-manager.md](features/FEATURE-mcp-skill-manager.md) - MCP server design
