# Claude-as-Coach: Project Setup Guide

## What This Is

**Claude-as-Coach** is an AI-assisted structured reflection system built on Claude Projects and custom skills. It provides a lightweight framework for daily summaries, weekly retrospectives, and weekly planning—helping you maintain context continuity across conversations, learn from experience systematically, and build sustainable goal-tracking habits.

**Problems it solves:**
- **Context fragmentation:** Each new Claude chat starts from scratch. This system maintains continuity through persistent documents.
- **Reflection friction:** Structured prompts reduce the activation energy for daily/weekly reflection.
- **Learning from experience:** The retrospective → planning loop helps you identify what works, run experiments, and adapt over time.

**Who it's for:** Anyone with goals requiring consistent reflection—learning new skills, health/fitness tracking, business projects, creative work, habit formation. If you've ever struggled to maintain a journal or reflection practice, this system provides the infrastructure to make it sustainable.

---

**🔧 Want to contribute or modify the system?** See [README.md](README.md) for repository structure, development workflow, and contribution guidelines.

**📚 Need quick setup instructions?** See [QUICKSTART.md](QUICKSTART.md) for fast-track installation.

---

## System Requirements

**Minimum Requirements:**
- **Claude Pro** subscription
- Access to Claude Projects
- Ability to import custom skills to Projects

**Limitations at minimum:**
- May hit context length limits with extensive project history
- Lower rate limits may require waiting between operations
- Basic thinking mode (fast but less thorough)

**Recommended Requirements:**
- **Claude Max x5** subscription
- Extended thinking mode enabled
- Well within capacity limits for intensive daily use

**Benefits of recommended:**
- Extended context window handles months of summaries/retros
- Higher rate limits support back-to-back skill invocations
- Extended thinking provides deeper analysis and better synthesis
- More reliable for power users with extensive project data

**Note:** This project is actively developed and tested with Max x5 + extended thinking enabled.

---

## Quick Start

**See [QUICKSTART.md](QUICKSTART.md) for complete installation and setup instructions.**

This guide focuses on understanding the system, customizing it for your goals, and developing your own workflows. For mechanical setup steps (cloning, importing skills, first run), refer to the Quick Start guide.

---

## The Core Loop

The system follows a daily → weekly reflection cycle:

### Daily Workflow

**Morning:** Say "good morning" or "gm"
- Loads yesterday's summary
- Generates a scannable morning brief (low cognitive load during wakeup)
- Sets context for the day ahead

**End of Day:** Say "daily summary"
- Guides you through structured reflection
- Generates `Summary-YYYY-MM-DD-DayName-tag.md`
- Captures key numbers, timeline, insights, decisions

### Weekly Workflow

**End of Week:** Say "weekly retro"
- Reflects on what worked and what didn't work
- Identifies experiments to run
- Tracks progress toward goals
- Generates `Weekly-Retro-YYYY-MM-DD-to-DD.md`

**Start of Week:** Say "weekly planning"
- Reviews constraints and capacity
- Sets 2-3 priorities maximum
- Defines success levels (L0-L3 framework)
- Generates `Weekly-Plan-YYYY-MM-DD-to-DD.md`

### Trigger Phrases Reference

| Skill | Trigger | Use Case |
|-------|---------|----------|
| Morning Routine | "good morning", "gm" | Start daily chat with context |
| Daily Summary | "daily summary" | End-of-day structured reflection |
| Weekly Retrospective | "weekly retro" | Reflect on the week |
| Weekly Planning | "weekly planning" | Plan the week ahead |

---

## Customization: Making It Yours

The base skills provide generic frameworks. You have two paths forward:

### Path 1: Start with Base Skills Only (Recommended)

**Use Rob as your template:** `examples/rob-the-runner/`

Rob demonstrates that **you don't need custom skills to get value**. He uses only the base skills and still gets:
- Structured daily summaries
- Weekly retrospectives
- Monthly rollups
- Fractal compression (recent detail → compressed history)
- Ongoing practice (Week 9 post-program exploration)

**This is the fastest path to getting started.** Import the base skills, start using them, see if they work for your goals. Only create custom skills if you need them later.

**Rob's profile:**
- 39-year-old accountant, couch-to-5K training + exploring yoga
- Uses base skills without modification
- See `examples/rob-the-runner/README.md` for details

### Path 2: Create Custom Skills (Advanced)

**Use Alice as your template:** `examples/alice-the-athlete/`

If base skills aren't enough, Alice shows how to extend them with custom personal skills:

- **Metrics:** Running distance, pace, heart rate zones, sleep quality
- **Context tags:** Week-Day format (W4-D2 = Week 4, Day 2 of training)
- **Protocols:** Recovery routines, pre-run warmups, fueling strategies
- **Success levels:** Calibrated to couch-to-5K milestones

You'll adapt this pattern to your domain.

### Step 2: What to Customize

**Timezone:**
- Base skills use `TZ='America/New_York'` for date verification
- Replace with your timezone (e.g., `TZ='Europe/London'`, `TZ='America/Los_Angeles'`)

**Key Numbers Table (Daily Summary):**
- Alice tracks: Distance, pace, heart rate, sleep hours, energy levels
- You might track:
  - **Learning:** Study hours, comprehension rating, topic mastery scores
  - **Business:** Revenue, customer calls, pipeline metrics, deep work hours
  - **Creative:** Word count, pieces completed, creative blocks encountered
  - **Productivity:** Deep work hours, tasks completed, focus quality ratings

**Context Tags:**
- Alice uses W4-D2 (training week + day)
- You might use:
  - Sprint numbers (S3-D2)
  - Phase labels (Bootstrap-D5, Build-D12)
  - Experiment IDs (ExpA-D3)
  - Or keep it simple: just dates

**Success Levels (Weekly Planning):**
- Alice's L0-L3 framework is calibrated to running milestones
- Calibrate yours to your goals:
  - **L0 (Minimum):** What absolutely must happen to call the week successful?
  - **L1 (Target):** What you're aiming for if things go well?
  - **L2 (Stretch):** What would exceed your expectations?
  - **L3 (Exceptional):** What would be a breakthrough week?

### Step 3: Create Your Personal Skills

**Directory structure (sister directories pattern):**
```
claude-as-coach-combined/             # Parent workspace
├── claude-as-coach/                  # Public repo
│   ├── /skills/                      # Base skills
│   │   ├── /daily-summary-base/      # Base skill source (tracked)
│   │   │   └── SKILL.md
│   │   ├── daily-summary-base.zip    # Packed base skill
│   │   └── [other base skills...]
│   ├── /examples/                    # Demo personas (all synthetic)
│   │   ├── README.md                 # Persona overview
│   │   ├── /rob-the-runner/          # Base skills only
│   │   │   ├── README.md
│   │   │   └── /documents/
│   │   ├── /alice-the-athlete/       # Custom skills
│   │   │   ├── README.md
│   │   │   ├── /documents/
│   │   │   └── /skills/
│   │   └── /gina-the-grad-student/   # Career domain (skeleton)
│   │       ├── README.md
│   │       └── /documents/           # Empty (TBD)
│   ├── /vendor/skills/               # Submodule (Anthropic tools)
│   ├── /scripts/                     # skill_workflow.py
│   └── /docs/                        # Documentation
└── claude-as-coach-personal/         # Your private repo
    ├── /documents/                   # Your daily summaries, retros
    └── /skills/                      # Your personal skill extensions
        ├── /daily-summary-personal/  # Source directory (tracked)
        │   └── SKILL.md              # Your metrics & context
        ├── daily-summary-personal.zip   # Packed skill
        ├── /daily-morning-routine-personal/
        ├── /weekly-retrospective-personal/
        └── /weekly-planning-personal/
```

### Why Sibling Directories?

This project uses **independent sibling repositories** (sibling directories) rather than git submodules for the personal repo:

**Benefits:**
- **No cross-repo reference updates needed** - Commit to each repo independently
- **Simpler mental model** - Two independent git repos, not parent/child relationship
- **Each repo has its own history** - Personal repo isn't tied to public repo commits
- **No submodule complexity** - No `git submodule update` commands needed

**Exception:** The `vendor/skills/` directory IS a submodule because it tracks upstream Anthropic tools that update independently.

**In practice:**
- Make changes in `claude-as-coach/` → commit and push there
- Make changes in `claude-as-coach-personal/` → commit and push there
- No synchronization needed between the two

**Frontmatter format:**
```yaml
---
name: daily-summary-personal
extends: daily-summary-base
description: Personal extensions with my specific metrics
---
```

**Pack your skills** (from parent workspace):
```bash
cd claude-as-coach-combined

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Result: claude-as-coach-personal/skills/daily-summary-personal.zip
```

**Import to Claude.ai:**
- Upload both base + personal .zip files to your project
- Claude will merge them automatically during execution

**See [WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md) for detailed skill editing workflows.**

### Customization Examples by Domain

**Learning a new skill (e.g., learning Spanish):**
- Metrics: Study minutes, vocabulary learned, conversation practice time
- Context: Topic focus (Grammar-W2, Conversation-W5)
- Success levels: L0 = Daily practice, L1 = Comprehension improving, L2 = Comfortable conversations

**Business/startup:**
- Metrics: Revenue, customer conversations, product iterations, deep work hours
- Context: Sprint cycles, product phases (Discovery, Build, Launch)
- Success levels: L0 = Core metrics tracked, L1 = Key milestones hit, L2 = User traction visible

**Creative work (e.g., writing a book):**
- Metrics: Word count, editing hours, scenes completed, creative flow state
- Context: Chapter milestones, draft phases (Draft1-Ch3, Revision-Ch1)
- Success levels: L0 = Daily writing habit maintained, L1 = Chapter completed, L2 = Breakthrough insights

**Health/fitness (beyond running):**
- Metrics: Strength gains, nutrition adherence, sleep quality, recovery markers
- Context: Training blocks, recovery weeks, testing weeks
- Success levels: L0 = Injury-free + consistency, L1 = Progressive overload, L2 = PR achieved

---

## Tips for Success

**Start simple:**
- Begin with just morning routine + daily summary for the first week
- Add weekly retro/planning once daily practice feels natural
- Don't force the full system on Day 1

**Skip when needed:**
- Miss a day? That's fine. The system adapts to you.
- Traveling or low capacity? Just do morning briefs, skip summaries.
- The goal is sustainable practice, not perfect adherence.

**Archive old content:**
- After a month, move older summaries to `claude-as-coach-personal/documents/archived/`
- Keeps your Claude Project context lean and fast
- Monthly rollups can compress weeks of summaries into one document
- See [WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md#document-lifecycle--archival) for complete archival strategy

**Use observation → reaction pattern:**
- Base skills lead with observations from your data
- You react, confirm, or refine rather than generating from scratch
- Less friction than staring at a blank page

**Extended thinking helps:**
- For deeper weekly retros and planning, extended thinking mode provides better synthesis
- Morning briefs and daily summaries work fine with standard thinking

**Don't over-engineer:**
- The system is a **process framework**, not a prescription
- Adapt the structure to what actually helps you learn and reflect
- Remove sections that don't serve you, add ones that do

---

## File Naming Conventions

The system uses consistent file naming patterns:

**Daily Summaries:**
- Format: `Summary-YYYY-MM-DD-DayName-tag.md`
- Example: `Summary-2025-11-20-Wednesday-W4-D2.md`
- Tag is optional but recommended for context

**Weekly Retrospectives:**
- Format: `Weekly-Retro-YYYY-MM-DD-to-DD.md`
- Example: `Weekly-Retro-2025-11-17-to-23.md`

**Weekly Plans:**
- Format: `Weekly-Plan-YYYY-MM-DD-to-DD.md`
- Example: `Weekly-Plan-2025-11-24-to-30.md`

**Date = date OF events, not FOR next day.**
Your daily summary on Tuesday night captures Tuesday's events, not Wednesday's plans.

---

## Where to Run Commands: Two Workflows

### Workflow A: Parent Workspace (Recommended)

**Best for:** Managing both repos simultaneously, using Claude Code

```bash
cd claude-as-coach-combined  # Stay here for all commands

# Pack base skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Git operations (change directory as needed)
cd claude-as-coach && git status && cd ..
cd claude-as-coach-personal && git status && cd ..
```

### Workflow B: Child Directory

**Best for:** Focused work on one repo at a time

```bash
cd claude-as-coach  # Work from public repo

# Pack base skill
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Pack personal skill (reach into sibling)
cd ../claude-as-coach-personal
python ../claude-as-coach/scripts/skill_workflow.py pack skills/daily-summary-personal/
```

**Choose the workflow that fits your style.** The examples in this guide use Workflow A (parent workspace) for clarity.

---

## Where This Is Going

**Microagent (coming soon):**
- Same skill pattern, but portable to any model with tool calling
- Run on open weights models (Llama, Qwen, Mistral, etc.)
- Not locked into Claude.ai Projects

**Open source:**
- MIT license—freely use, modify, and share
- Community skill templates for different domains
- Contributions welcome

**Portability:**
- Skills are markdown files in ZIP archives
- Easy to version control, diff, and share
- No vendor lock-in

**Future sessions:**
- Deeper technical dive into microagent architecture
- Live demo of running on local models
- Community-contributed skill libraries

---

## Getting Help

**If you encounter issues:**
- Check that both base + personal skills are imported
- Verify trigger phrases match exactly ("gm", "daily summary", etc.)
- Confirm timezone in skills matches your location
- Try toggling skills off/on in Claude.ai settings

**Repo:** [github.com/ZachBeta/claude-as-coach](https://github.com/ZachBeta/claude-as-coach)
**License:** MIT
**Questions:** Open an issue on GitHub

**Additional documentation:**
- [QUICKSTART.md](QUICKSTART.md) - Setup and installation
- [WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md) - Daily skill editing workflows
- [README.md](../README.md) - Repository overview
- [FEATURES.md](docs/FEATURES.md) - Feature roadmap

---

## Next Steps

1. **Import base skills** to your Claude Project (5 minutes)
2. **Test with "gm"** to validate morning routine works
3. **Generate your first daily summary** tonight ("daily summary")
4. **Choose your path:**
   - **Start simple (recommended):** Use base skills only like Rob - see if they meet your needs
   - **Go advanced:** Create personal skill extensions like Alice if base skills aren't enough
5. **Run your first weekly retro** next Sunday
6. **Refine and adapt** the system to your workflow

Welcome to sustainable, AI-assisted reflection. Let's build something meaningful together.
