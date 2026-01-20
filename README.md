# Claude as Coach

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Experiment in using Claude as a personal coach for behavior change, using Claude Projects with custom skills for daily summaries, weekly retrospectives, and planning.

---

**🔥 Wanna try out a new project?** See [QUICKSTART.md](QUICKSTART.md) - paste into Claude.ai to auto-fetch and package skills.

**🔄 Already using this?** See [UPGRADE_SKILLS.md](UPGRADE_SKILLS.md) to update your skills to the latest versions.

**📋 Prefer manual setup?** See [QUICKSTART-MANUAL.md](QUICKSTART-MANUAL.md) to download skill files directly.

**📖 New to this system?** See [PROJECT-SETUP.md](PROJECT-SETUP.md) for a comprehensive guide on using Claude-as-Coach for your own goals.

**🔧 Contributing or developing?** You're in the right place - this README covers repository structure, development workflow, and contribution guidelines.

---

## Structure

```
claude-as-coach-combined/        # Parent workspace
├── claude-as-coach/             # This repo (public)
│   ├── /docs/                   # Documentation
│   ├── /skills/                 # Custom Claude skills
│   │   ├── daily-summary-base/  # Base skill source (tracked)
│   │   ├── daily-summary-base.zip # Packed base skill
│   │   ├── [other-skill-base]/  # Other base skill sources
│   │   └── [standalone].zip     # Standalone skills
│   ├── /examples/               # Demo personas (all synthetic/fictional)
│   │   ├── rob-the-runner/      # Base skills only demo
│   │   ├── alice-the-athlete/   # Custom skills demo
│   │   └── gina-the-grad-student/ # Career domain demo (skeleton)
│   ├── /vendor/skills/          # Submodule - anthropics/skills fork
│   └── /scripts/                # Workflow automation
└── claude-as-coach-personal/    # Sibling repo (private) - YOUR data
    ├── documents/               # Your daily summaries, retros, etc.
    └── skills/                  # Your personal skill extensions
        ├── daily-summary-personal/   # Source directory
        ├── daily-summary-personal.zip # Packed skill
        └── daily-morning-routine-personal/ # Source directory
```

## Quick Start

### Clone

```bash
# Create parent workspace directory
mkdir claude-as-coach-combined
cd claude-as-coach-combined

# Clone public repo with vendor submodule
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach

# Create your own private repo for personal data (optional)
git clone https://github.com/YOUR-USERNAME/claude-as-coach-personal
# OR: cp -r claude-as-coach/examples/rob-the-runner claude-as-coach-personal && cd claude-as-coach-personal && git init
```

If already cloned (vendor submodule only):

```bash
cd claude-as-coach
git submodule init
git submodule update
```

### Using Claude Code

If using [Claude Code](https://code.claude.com/docs/en/overview), you have two options:

**Option A: Standalone (simpler)**
```bash
cd claude-as-coach
claude
```

**Option B: Parent workspace (advanced)**
```bash
cd claude-as-coach-combined
claude
```

Parent workspace allows simultaneous access to both repos. See `docs/examples/parent-workspace-CLAUDE.md` for setup.

### Using the Example Data

Three demo personas are available in `examples/`:

**examples/rob-the-runner/** - **Rob the Runner (Base Skills Only)**
- 39-year-old accountant, couch-to-5K + exploring yoga
- Demonstrates the system works WITHOUT custom personal skills
- Shows fractal compression: daily → weekly → monthly rollup
- Shows ongoing practice (Week 9 post-program exploration)
- **Start here** - lower barrier to entry

**examples/alice-the-athlete/** - **Alice (Custom Skills)**
- Couch-to-5K runner with custom personal skill extensions
- Demonstrates base + personal skill pattern (extensibility)
- Use to learn how to create custom skills

**examples/gina-the-grad-student/** - **Gina (Skeleton - TBD)**
- Grad student (job search/interview prep domain)
- Demonstrates non-fitness use case
- Skeleton only (content TBD post-Dec 12 presentation)

**Which to use?**
- **New users:** Start with Rob (base skills only, simpler)
- **Advanced users:** Reference Alice (custom skills, more powerful)
- **Career/non-fitness:** Check Gina (when content complete)

The author's actual personal data lives in a sibling `claude-as-coach-personal/` private repository (not included in this public repo).

**See [examples/README.md](examples/README.md) for complete persona details.**

### Editing Skills

**Working Directory:** The following examples assume you're in the parent workspace directory (`claude-as-coach-combined/`), which allows working with both repos simultaneously.

**New Structure (Base + Personal):**

Skills are separated into base frameworks (shareable) and personal extensions (private):

```bash
# Edit base skill source directly (in public repo)
code claude-as-coach/skills/daily-summary-base/SKILL.md

# Pack base skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Edit personal extension (in sibling repo)
code claude-as-coach-personal/skills/daily-summary-personal/SKILL.md

# Pack personal skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/

# Import both to Claude.ai for stacked behavior
```

**Unified Skills (Any Time Scale):**

Planning and retrospective skills work at any time scale (daily/weekly/monthly/quarterly/yearly):

```bash
# Edit unified planning skill
code claude-as-coach/skills/planning-base/SKILL.md

# Pack
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/planning-base/
```

## Documentation

### Workflow & Reference
- **[docs/WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md)** - Complete skill editing workflow
- **[docs/features/FEATURE-mcp-skill-manager.md](docs/features/FEATURE-mcp-skill-manager.md)** - MCP server design for Claude.ai integration
- **[docs/FEATURES.md](docs/FEATURES.md)** - Feature backlog and implementation tracking
- **[docs/NEXT-SESSION.md](docs/NEXT-SESSION.md)** - Current status and next steps

### Skills

**Daily Skills (Base + Personal):**
- **daily-summary** - End-of-day capture
  - `skills/daily-summary-base.zip` - Framework for structured daily summaries
  - `personal/daily-summary-personal.zip` - Personal metrics & domain-specific context
- **daily-morning-routine** - Morning kickoff routine
  - `skills/daily-morning-routine-base.zip` - Framework for morning context loading
  - `personal/daily-morning-routine-personal.zip` - Personal protocols & thresholds

**Unified Skills (Any Time Scale):**
- `planning-base.zip` - Forward planning with constraints (daily/weekly/monthly/quarterly/yearly)
- `retrospective-base.zip` - Reflection and pattern extraction (daily/weekly/monthly/quarterly/yearly)

**Setup:**
- `project-coach-setup-base.zip` - Initial project setup and goal definition

**Experimental:**
- `context-curation-base.zip` - Project file context management (WIP)

## Skill Architecture: Base + Personal Pattern

Skills are separated into two layers:

**Base Skills** (shareable, main repo):
- Generic process frameworks
- File patterns and structure
- Formatting guidelines
- Edge cases and error handling
- No personal context or thresholds

**Personal Extensions** (private, sibling repo):
- Specific metrics and thresholds
- Domain terminology
- Personal protocols and interventions
- Context-specific examples
- `extends: base-skill-name` in frontmatter

**Import to Claude.ai:**
Both skills are imported together. Claude reads the base framework first, then applies personal extensions. Test whether `extends:` directive enables proper inheritance, or if simple sequential loading is sufficient.

**Benefits:**
- Base skills can be shared publicly
- Personal context stays private in sibling repo
- Framework improvements benefit all users
- Easy to swap personal extensions
- Clear separation of concerns

---

## Example Use Case: Couch-to-5K Training

To illustrate the base + personal pattern, imagine using these skills for running training:

### Base Skills (Shareable Framework)

**daily-summary-base:**
- Date verification process
- Filename pattern: `Summary-YYYY-MM-DD-DayName-tag.md`
- Section structure (TL;DR, Key Numbers, Timeline, Insights, Decisions)
- Formatting rules (markdown, ASCII-safe, emoji guidance)
- Context usage monitoring

**daily-morning-routine-base:**
- Date verification
- Find yesterday's summary
- Generate morning brief structure
- Morning state recognition patterns
- Two-tier format (detail + TL;DR)

### Personal Extensions (Your Training Plan)

**daily-summary-personal:**
```markdown
## Key Numbers

| Metric | Morning | Evening | Notes |
|--------|---------|---------|-------|
| **Running Distance** | - | 3.2 mi | Week 4, Day 2 complete |
| **Average Pace** | - | 10:15/mi | Target: <10:00/mi |
| **Heart Rate Zones** | - | Z2: 80% | Good aerobic base |
| **Morning Weight** | 165 lbs | - | Down 2 lbs this week |
| **Sleep Quality** | 7.5 hrs | - | Garmin score: 85 |
| **Nutrition** | 2100 cal | 2300 cal | On target for training |
```

**daily-morning-routine-personal:**
- Sleep data integration (Garmin)
- Recovery metrics (HR variability, soreness level)
- Training plan status (Week 4, Day 2 next)
- Nutrition goals for today
- Rest vs. run day protocols

### Benefits of Separation

1. **Shareable framework:** You can share the base skills with the running community
2. **Private data:** Your actual training metrics stay in your private sibling repo
3. **Easy adaptation:** Switch from running to cycling by swapping personal extensions
4. **Framework improvements:** Bug fixes and enhancements to date handling, file patterns, etc. benefit all users
5. **Multiple users:** Different people can use the same base with their own training metrics

---

## Development

### Setup

No special setup required. Clone the repo and initialize the vendor submodule:

```bash
cd claude-as-coach
git submodule update --init --recursive
```

**Optional:** Set up parent workspace for working with both repos. See `docs/examples/parent-workspace-CLAUDE.md`.

### Skills Workflow

**Standalone usage (from claude-as-coach/ directory):**

```bash
# Pack a skill after editing
python scripts/skill_workflow.py pack skills/daily-summary-base/

# For detailed workflow, see docs/WORKFLOW-GUIDE.md
```

**Parent workspace usage (from claude-as-coach-combined/ directory):**

```bash
# Pack base skill
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/

# Pack personal skill (if sibling repo exists)
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach-personal/skills/daily-summary-personal/
```

### Personal Files (Sibling Repo)

```bash
# Commit new personal files (from parent workspace)
cd claude-as-coach-personal
git add documents/Summary-2025-11-24-Sunday.md
git commit -m "Add Sunday summary"
git push origin main
cd ../claude-as-coach
```

No submodule reference update needed - sibling repos are independent.

## Dependencies

- Python 3.x
- Git
- Optional: PyYAML (for skill validation via vendor scripts)

```bash
pip install -r scripts/requirements.txt
```

## About

This repository demonstrates using Claude Projects as a personal coach with custom skills for:
- Daily reflections and structured summaries
- Weekly retrospectives (what worked / didn't work)
- Weekly planning with goal setting
- Iterative skill refinement

**Key innovation:** Separating skills into base frameworks (shareable) and personal extensions (private) enables:
- Community sharing of coaching methodologies
- Privacy for personal data and metrics
- Rapid adaptation to different use cases (fitness, productivity, learning, etc.)

Skills evolve based on what works in practice, with changes tracked via git for analysis and iteration.

## License

Project methodology and custom skills: [Your choice]

Vendor submodule (anthropics/skills): See [vendor/skills/LICENSE](vendor/skills/LICENSE)
