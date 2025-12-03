# Personal Skills - Example Template

This directory contains **example personal skill extensions** using a couch-to-5K running training scenario.

## Quick Start

To create your own personal skills:

```bash
# Copy this example to personal/ (gitignored)
cp -r personal.example personal

# Customize the skills for YOUR use case
vim personal/skills/daily-summary-personal/SKILL.md
vim personal/skills/daily-morning-routine-personal/SKILL.md

# Pack your personal skills
python scripts/skill_workflow.py pack daily-summary-personal
python scripts/skill_workflow.py pack daily-morning-routine-personal

# Import to Claude.ai along with base skills
# - skills/daily-summary-base.skill
# - personal/daily-summary-personal.skill
```

## What to Customize

### Daily Summary Personal Skill

**Replace couch-to-5K metrics with your own:**
- Running → Your domain (productivity, learning, business, health, etc.)
- Metrics table → Your tracked values
- Context tags → Your experimental structure
- Domain terminology → Your specific concepts

**Keep from base:**
- Date verification process
- Filename patterns
- Section structure
- Formatting rules

### Morning Routine Personal Skill

**Replace training protocols with yours:**
- Sleep targets → Your sleep needs
- Training plan → Your goals/projects
- Recovery metrics → Your indicators
- Readiness checks → Your criteria

**Keep from base:**
- Morning brief structure
- Summary loading process
- State recognition patterns
- Two-tier format

## Example Use Cases

Adapt this pattern for:
- **Learning:** Daily study sessions, skill practice, course progress
- **Business:** Sales calls, revenue tracking, customer conversations
- **Creative:** Writing word count, art pieces completed, creative blocks
- **Productivity:** Deep work hours, tasks completed, focus metrics
- **Health:** Any health tracking (sleep, nutrition, symptoms, treatments)
- **Habit Building:** Streaks, consistency, behavior patterns

## Directory Structure

```
personal.example/
├── README.md                              # This file
├── documents/                             # All project documents (flat structure)
│   ├── couch-to-5k-plan.md               # Reference: training plan
│   └── Summary-2025-11-20-Wednesday-W4-D2.md  # Example daily summary
└── skills/                                # Your personal skill extensions
    ├── daily-summary-personal/
    │   └── SKILL.md
    ├── daily-summary-personal.skill       # Packed skill (import to Claude.ai)
    ├── daily-morning-routine-personal/
    │   └── SKILL.md
    └── daily-morning-routine-personal.skill  # Packed skill (import to Claude.ai)
```

## Privacy Note

The `personal/` directory is **gitignored** in the main repository. You can:
- Keep it local only (not tracked)
- Create your own private git repo for personal/
- Back it up however you prefer

Your personal data never gets committed to the public repo.

## Need Help?

See the main [README.md](../README.md) and [docs/WORKFLOW-GUIDE.md](../docs/WORKFLOW-GUIDE.md) for complete instructions.
