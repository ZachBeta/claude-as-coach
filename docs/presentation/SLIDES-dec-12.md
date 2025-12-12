---
title: Claude-as-Coach
subtitle: Context management without heavy infrastructure
author: Zach Morek
date: Dec 12, 2025
theme: white
transition: slide
slideNumber: true
header-includes: |
  <style>
    .reveal { font-size: 28px; }
    .reveal h1 { font-size: 1.8em; text-align: center; }
    .reveal h2 { font-size: 1.4em; text-align: center; }
    .reveal pre { font-size: 0.7em; }
    .reveal table { font-size: 0.8em; }
    .smaller { font-size: 0.8em; }
    .reveal .slides section { text-align: left; }
    .reveal .slides #title-slide { text-align: center; }
    .reveal .slides section ul,
    .reveal .slides section ol {
      display: block;
      margin-left: 1em;
    }
    .centered { text-align: center; }
  </style>
---

# The Goal

Bootstrapped garage startup life was wearing down my health.

I wanted to build better habits.

Exercise more. Sleep better. Ship more code.

Tried apps. Tried spreadsheets. Tried journaling.

What I really wanted: a conversational interface that could adapt

---

# Hammer in search of a nail 
## let's make an agent?

A flexible system that remembers yesterday.

And last week. And your goals.

So we have an agent to build?

...and we have RAG to configure.

...and ...and ...and ...

This is gonna take me a lot of building before I can easily use it...

---

# Evolution

## How the system developed

---

# Evolution v0: Giant Google Doc

- Daily logging: work, exercise, sleep, diet
- Gaining insights = manual effort or build systems
- Too much cognitive load sifting through it all

---

# Evolution v1: Journaling Agents

- Various attempts at building agents from scratch got stuck on all the little implementation details
- Using a basic conversation in claude.ai - ask it to summarize → copy/paste into new chat
- Repeat daily. Forever.

---

# Evolution v2: Projects (The Aha Moment)

- Projects + saving to documents
- Documents persist across conversations!
- But... wasting tokens on instructions

```
┌─────────────────────────────────────┐
│ Project Context (always loaded)     │
│ ┌─────────────────────────────────┐ │
│ │ instructions.md (5k tokens)     │ │ ← Always here
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

---

# Evolution v3: Skills

- On-demand instructions (only loaded when needed)
- Retro instructions only loaded during retro
- Not burning tokens every conversation

---

# Evolution v4: Skill Inheritance

- What's structural? (shareable)
- What's personal? (private)
- `claude-as-coach` + `claude-as-coach-personal`

No grand plan. Just iterated on friction.

---

# The Platform

## Claude.ai Projects + Skills

---

# Projects: The Mental Model

::: notes
SWITCH TO: Empty Claude.ai project, then one with documents
SHOW: Project sidebar with documents
:::

::: centered
![Project documents](screenshots/demo2-project-docs.png)
:::

Every conversation sees **all** project documents.

---

# Project Primitives

| Primitive | What it is | How I use it |
|-----------|------------|--------------|
| **Conversation** | Permanent chat, context not retained | Daily check-ins |
| **Artifact** | Generated content | Summaries, retros |
| **File** | Project document | Persistent context |
| **Skill** | On-demand instructions (.zip) | Structured workflows |
| **Memory** | 30 slots (200 chars each), agent/UI editable | (skipped - didn't fit flow) |
| **Instructions** | System prompt | (skipped to simplify) |

The workflow uses **conversations → artifacts → files**.

---

# The System: Daily → Weekly Loop

```
        ┌──────────────┐
   ┌───►│ Morning "gm" │  ← conversation only
   │    └──────┬───────┘
   │           ▼
   │    ┌──────────────┐
   │    │Daily Summary │──────┐
   │    └──────────────┘      │ x7
   │                          ▼         artifacts →
   │    ┌──────────────┐    ┌──────────────┐  project docs
   │    │ Weekly Plan  │◄───│ Weekly Retro │
   │    └──────┬───────┘    └──────────────┘
   │           │
   └───────────┘
```

---

# Conversations → Artifacts → Documents

```
┌─────────────────────────────────────────────────┐
│ Conversation (saved, but not revisited)         │
│ "How was your run today?"                       │
│ "Great! Did 2.5 miles, no walk breaks..."       │
│                    │                            │
│                    ▼                            │
│ ┌─────────────────────────────────────────────┐ │
│ │ Artifact (generated)                        │ │
│ │ Summary-2025-12-11-Wednesday.md             │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
                     │
                     ▼ "Add to project"
┌─────────────────────────────────────────────────┐
│ Project Document (persistent)                   │
│ Available in ALL future conversations           │
└─────────────────────────────────────────────────┘
```

---

# Fractal Compression

```
Sun Mon Tue Wed Thu Fri Sat
 │   │   │   │   │   │   │
 └───┴───┴───┼───┴───┴───┘
             ▼
      Weekly Retro (1 doc)
```

```
Week 1 ─┐
Week 2 ─┼──► Monthly Retro (1 doc)
Week 3 ─┤
Week 4 ─┘
```

**Manual workflow:** Download retro → add to project → remove rolled-up docs

---

# Skills

## On-demand instructions for Claude

---

# What's a Skill? (Basic)

::: notes
SWITCH TO: Show daily-summary-base/SKILL.md in repo
:::

A `.zip` containing markdown instructions.

```
daily-summary-base/
└── SKILL.md
```

```yaml
---
name: daily-summary-base
description: Use when user says "daily summary"
             or "end of day"
---

# Daily Summary Generator

## Process
1. Verify current date (bash command)
2. Ask which date to summarize
3. Generate structured markdown...
```

---

# What's a Skill? (With Tools)

Skills can bundle Python scripts.

```
skill-creator/
├── SKILL.md              # LLM instructions
└── scripts/
    ├── init_skill.py
    ├── package_skill.py
    └── quick_validate.py
```

**The blend:**

- Instructions tell Claude *what* to do and *when*
- Scripts give Claude *deterministic tools* to call
- LLM handles ambiguity, scripts handle precision

---

# Code is Data is Code

A skill is a function that runs on an LLM.

```
Input:  User says "daily summary"
        + Project documents (context)

Compute: LLM executes skill instructions
         Calls tools as needed

Output: Summary-2025-12-11-Wednesday.md
```

The instructions *are* the program.
The context *is* the state.
The LLM *is* the runtime.

---

# Skill Triggers

Triggers are function calls in human language.

| Skill | Triggers |
|-------|----------|
| Morning Routine | "gm", "good morning" |
| Daily Summary | "daily summary", "end of day" |
| Weekly Retro | "weekly retro" |
| Weekly Planning | "weekly planning" |

**How it works:**

- User says trigger phrase
- Claude pattern-matches against skill descriptions
- Skill instructions load into context
- Claude executes the process

---

# The .zip/.skill Confusion

::: notes
Links showing the inconsistency:
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/package_skill.py#L64
:::

Most Anthropic docs say `.zip`

But `skill-creator` tool outputs `.skill`

```bash
# skill-creator outputs:
python package_skill.py daily-summary-base/
# → daily-summary-base.skill  # Won't upload!

# Workaround:
mv daily-summary-base.skill daily-summary-base.zip
```

PR pending to fix their tooling.

---

# Projects vs Claude Code

| Claude.ai Projects | Claude Code |
|--------------------|-------------|
| Cross-device (phone + laptop) | Terminal-focused |
| Document-centric | Code-centric |
| "Log my run" from phone | "Fix this bug" from IDE |
| Context = your documents | Context = your codebase |
| Skills in Settings | Skills in repo |

::: centered
**Different tools, different jobs.**
:::

---

# Architecture

## How the pieces fit together

---

# Repo Structure

::: notes
SWITCH TO: Terminal or VS Code showing repo
:::

```
claude-as-coach-combined/          # Parent workspace
├── claude-as-coach/               # Public (shareable)
│   ├── skills/                    # Base skill frameworks
│   ├── examples/rob-the-runner/   # Demo persona
│   └── scripts/
└── claude-as-coach-personal/      # Private (your data)
    ├── skills/                    # Your extensions
    └── documents/                 # Your summaries
```

---

# Base + Personal Skill Pattern

```
┌────────────────────────────────────┐
│ daily-summary-base.zip             │
│ (Generic framework - shareable)    │
│ - Date verification                │
│ - Section structure                │
└────────────────────────────────────┘
              +
┌────────────────────────────────────┐
│ daily-summary-personal.zip         │
│ (Your customizations - private)    │
│ - Your metrics (pace, HR, sleep)   │
│ - Your thresholds                  │
└────────────────────────────────────┘
```

Import both. Claude loads both at runtime.

---

# Synthetic Data

## Why Rob isn't real

---

# The Demo Data Problem

Building demos for personal productivity tools is hard:

**Option A: Use real data**

- Privacy concerns (mine AND others')
- Can't share in public repo
- Awkward to present personal health info

**Option B: Make stuff up on the fly**

- Inconsistent across demos
- No version control
- "Let me just quickly fabricate a believable 8-week journey..."

---

# The Solution: Synthetic Personas

Three fictional personas, each demonstrating different use cases:

| Persona | Demonstrates |
|---------|--------------|
| **Rob the Runner** | Base skills only (simplicity) |
| **Alice the Athlete** | Custom personal skills (extensibility) |
| **Gina the Grad Student** | Non-fitness domain (versatility) |

All data is synthetic. All commits are tracked. All demos are reproducible.

---

# Synthetic Data: Work in Progress

**Reproducibility** (goal)

- Same demo, any day: `regenerate_demo_dates.py --demo-day 2025-12-12`
- Git tracks the "ground truth" - can diff persona evolution

**Testing without exposure**

- Iterate on skills without personal data leakage
- Share examples in public repo safely

**Template for adoption**

- Users can fork Rob's structure
- Customize for their domain without starting from scratch

*Still iterating on date alignment and gap handling.*

---

# Persona Design: Rob's Journey

```
Week 1-4: Monthly rollup (compressed)
     │
     └──► Single document captures early program

Week 5-7: Weekly retros (recent history)
     │
     └──► 3 documents show pattern extraction

Week 8: Daily summaries (current detail)
     │
     └──► 3 documents show daily capture

Week 9: Post-program (ongoing practice)
     │
     └──► Shows system continues past goal
```

**Demonstrates fractal compression with believable timeline.**

---

# Demo

## Two scenarios

---

# Demo Overview

**Demo 1: Bootstrap (0 → 1)**

Fresh project. Goal definition through first summary.

**Demo 2: Mature Project (Day Seam + Compression)**

Ongoing project. Morning routine → summary → retro/plan → cleanup.

---

# Demo 1: Project Bootstrap

::: notes
SWITCH TO: Fresh project "demo-bootstrap"
SHOW: project-coach-setup skill flow
:::

**Scenario:** New user, Week 1 Day 1

**Flow:**

1. Import skills → "let's set up this project"
2. Goal definition conversation
3. Generate first daily summary
4. Add to project → ready for tomorrow

**Key moments:**

- Skill guides goal articulation
- Summary structure appears
- "Add to project" creates persistent context

---

# Demo 1: Paste Quickstart

::: centered
![Paste quickstart](screenshots/demo1-bootstrap-01-pasted.png){height=500px}
:::

---

# Demo 1: Setup Running

::: centered
![Setup running](screenshots/demo1-bootstrap-02-running.png){height=500px}
:::

---

# Demo 1: Save Skills

::: centered
![Save skills](screenshots/demo1-bootstrap-03-save-skills.png){height=500px}
:::

---

# Demo 1: Goal Definition

::: centered
![Goal definition](screenshots/demo1-bootstrap-04-goals.png){height=500px}
:::

---

# Demo 1: Goals Result

::: centered
![Goals result](screenshots/demo1-bootstrap-05-goals-results.png){height=500px}
:::

---

# Demo 1: Add to Project

::: centered
![Add to project](screenshots/demo1-bootstrap-06-add-to-project.png){height=500px}
:::

---

# Demo 2: Mature Project

::: notes
SWITCH TO: Project "rob-week-9" with existing documents
SHOW: Morning → Summary → Retro → Manual cleanup
:::

**Scenario:** Rob at Week 9, Sunday morning

**What's in the project:**

- 3 daily summaries (recent week)
- Weekly retros (Weeks 5-8)
- Monthly rollup (October)

---

# Demo 2: Project Documents

::: centered
![Project documents](screenshots/demo2-project-docs.png){height=500px}
:::

---

# Demo 2a: Day Seam ("gm")

::: notes
SHOW: "gm" response finding yesterday's summary
:::

**Trigger:** "gm"

- Finds yesterday's summary
- Generates scannable morning brief
- Low cognitive load during wakeup

---

# Demo 2a: "gm" Trigger

::: centered
![gm trigger](screenshots/demo2a-gm-01-trigger.png){height=500px}
:::

---

# Demo 2a: Gap Handling

::: centered
![gap handling](screenshots/demo2a-gm-02-gap-handling.png){height=450px}

Yesterday not found → uses most recent (2 days ago)
:::

---

# Demo 2a: Morning Brief

::: centered
![morning brief](screenshots/demo2a-gm-03-morning-brief.png){height=500px}
:::

---

# Demo 2b: Daily Summary

**Trigger:** "daily summary"

→ Conversation throughout the day, then structured capture

---

# Demo 2b: Conversation + Trigger

::: centered
![conversation](screenshots/demo2b-summary-01-conversation.png){height=500px}
:::

---

# Demo 2b: Date Confirmation

::: centered
![confirmation](screenshots/demo2b-summary-02-confirmation.png){height=500px}
:::

---

# Demo 2b: Summary Preview

::: centered
![preview](screenshots/demo2b-summary-03-preview.png){height=500px}
:::

---

# Demo 2b: Add to Project

::: centered
![add to project](screenshots/demo2b-summary-04-add-to-project.png)
:::

→ Now persistent in ALL future conversations

---

# Demo 2c: Weekly Retro (Compression)

::: notes
SHOW: Retro pulling from daily summaries
:::

**Trigger:** "weekly retro"

```
Input: 7 daily summaries (~3500 words)
       ↓
Output: 1 weekly retro (~800 words)

What Worked:
- Morning runs before work
- 10-min warmup routine

Experiments for Next Week:
- Try 5-min post-run stretching
```

---

# Demo 2c: Retro Start

::: centered
![Retro start](screenshots/demo2c-retro-01-start.png){height=500px}
:::

---

# Demo 2c: Add Retro to Project

::: centered
![Add retro to project](screenshots/demo2c-retro-02-add-to-project.png){height=500px}
:::

---

# Demo 2d: Manual Pruning

::: notes
SHOW: Project files sidebar, removing old dailies
:::

**After saving retro:**

1. Weekly retro added to project
2. Daily summaries (now compressed) → remove from project
3. Keep locally for archive

**Platform limitation:** No API for project file management.

Manual but rare (weekly at most).

---

# Demo 2d: Select and Delete

::: centered
![Select and delete](screenshots/demo2d-pruning-01-select-and-delete.png){height=500px}
:::

---

# Lessons

## What actually matters

---

# What I Learned

1. **Skills are prompts** - just better organized
2. **Context management is the game** - not agent architecture
3. **Low-build wins** - I'm still using this daily
4. **Personal data stays personal** - base/personal split works

---

# LLMs Are Bad at Dates

Every skill that deals with dates starts with this:

```bash
TZ='America/New_York' date '+%A, %B %d, %Y'
```

LLMs make up dates. Tool calls give ground truth.

No assumptions. Verify first.

---

# Timestamps Help

Adding timestamps inside chat helps Claude understand:

- Flow of the day
- Roughly what happened when
- How long things took

```
Captain's log, stardate 2025-12-12 16:00 ET

Just finished the 3pm meeting. Went long.
Starting focused work block now.
```

The more temporal context, the better the summary.

---

# Skills Are Global (Pain Point)

Platform limitation: Skills not project-scoped

**The problem:**

- My account is both prod AND dev
- Manual toggle to test changes
- No "dev skill" vs "prod skill" per project

**Workaround:**

- Naming: `production-*` vs `development-*`
- Manual toggling in Settings > Capabilities

---

# Platform Limitations (Real Talk)

- Skills are **global** (not project-scoped)
- Skill upload/download is clunky, hard to version them
- Mobile summary->gm flow is clunky - missing "add to project"
- Context limits exist (Pro vs Max)
- **Pruning is manual:** generate artifact -> save artifact locally to back up → add to project → remove rolled-up docs after retro

Works despite these. Not because of them.

---

# Onboarding Experiments

Tested a few approaches to setting up the claude.ai project, one winner, and a runner up:

```
QUICKSTART.md           # Promoted (agent driven setup)
QUICKSTART-MANUAL.md    # Fallback (manually set up skills)
```

Skill-creator approach won: fetch SKILL.md + package.

---

# Safety Boundaries

This is a **reflection tool**, not a replacement for:

- Medical advice
- Mental health support
- Financial guidance
- Legal counsel

Claude has limitations. Critical decisions need professionals.

(Disclaimers added to README, skills, and setup docs)

---

# The Dev Process

"Zero build" doesn't mean zero iteration.

**Primitives explored:**

- Conversation (ephemeral)
- Artifact (generated)
- Project document (persistent)
- Memory (tried - adds complexity, not required)
- Instructions (tried - harder to git track, frankly not needed if there's a project file instead)

**Insight:** Project docs > base instructions for git tracking

---

# FEATURES.md: Dev with Claude Code

Tracking 50+ features in a markdown file. Sounds simple. Works well.

```
docs/FEATURES.md           # Summary backlog (this file)
docs/NEXT-SESSION.md       # "What do I do next?"
docs/features/FEATURE-*.md # Detailed planning (temporary)
```

**The pattern:**

1. New idea → quick entry in FEATURES.md
2. Getting complex? → spin out FEATURE-xyz.md
3. Done? → delete the detail file (git history preserves)

Claude Code reads the whole thing. Maintains context across sessions.

---

# Slides as Code

This presentation is markdown + pandoc + reveal.js.

```bash
# Edit content
vim SLIDES-dec-12.md

# Render
pandoc -t revealjs -s SLIDES-dec-12.md -o slides.html

# View
open slides.html
```

**Trade-off:**

- Less customizable than Keynote/Slides
- But: Claude Code can iterate on it directly
- "Add a slide about X" → done in seconds

Keep artifacts close to your tools.

---

# The Bitter Lesson

Why over-engineer when context windows keep growing?

| Approach | Friction |
|----------|----------|
| RAG pipeline | High (infra, embeddings, retrieval) |
| Custom agent | Medium (code, testing, deployment) |
| Summary-of-summaries | Low (just documents) |

Context stays in documents. Claude reads them all.

Like memory that decays naturally over time.

"Summary of Summaries is all you need"*

*for this use case at least

---

# What's Next

## Open source and beyond

---

# Where This Is Going

**Claude-as-coach tech demo prototype is MIT'd (now)**

- MIT license
- Base skills shareable
- Rob example included

**Microagent (future)**

- Smallest possible agent to replicate the functionality
- Same pattern, any model
- Tool-calling models (gpt-oss, kimi-k2, glm-4.6)
- Not locked to Claude (but also no token subsidies)

---

# Iterating on Skills

**The skills evolve with you:**

- Day over day: small tweaks to prompts
- Week over week: new sections, refined triggers
- Month over month: new skills, deprecated patterns

**Two layers:**

- **Base skills** - shareable frameworks (public repo)
- **Personal extensions** - your metrics, thresholds, protocols (private repo)

Edit → pack → upload → test → repeat.

---

# How to Contribute

**Adapt the skills to your domain:**

1. Fork the repo
2. Edit `skills/*/SKILL.md` for base frameworks
3. Create personal extensions in a private sibling repo
4. Pack with `python scripts/skill_workflow.py pack skills/my-skill/`
5. Test in Claude.ai → iterate

**Key files:**

| File | Purpose |
|------|---------|
| `skills/*/SKILL.md` | Skill source files (edit these) |
| `scripts/skill_workflow.py` | Pack/unpack utility |
| `QUICKSTART.md` | 5-minute setup |
| `PROJECT-SETUP.md` | Comprehensive guide |

**Share what works:** PRs welcome for base skill improvements.

---

# Under-engineering

We're AI engineers. We could build this with:

- LangChain
- Custom agents
- RAG pipelines
- Vector databases

Or we could just... use Claude Projects with some markdown files.

**Sometimes the best prototype is zero-build.**

---

# Try It Yourself

**Easiest:** Paste [`QUICKSTART.md`](https://github.com/ZachBeta/claude-as-coach/blob/main/QUICKSTART.md) into Claude

(Auto-fetches skills + runs project setup)

**Or manually:** See `QUICKSTART-MANUAL.md` for download links

```
skills/
├── project-coach-setup-base.zip  ← Start here
├── daily-summary-base.zip
├── daily-morning-routine-base.zip
├── planning-base.zip
└── retrospective-base.zip
```

See `docs/experiments/` for alternative onboarding approaches.

---

# Summary

| Concept | Key Point |
|---------|-----------|
| **Projects** | Documents always in context |
| **Skills** | On-demand instructions (.zip) |
| **Base + Personal** | Shareable framework + private data |
| **Fractal Compression** | Daily → Weekly → Monthly |
| **The Loop** | Morning → Summary → Retro → Plan |

**Repo:** [github.com/ZachBeta/claude-as-coach](https://github.com/ZachBeta/claude-as-coach)

**Triggers:** "gm" · "daily summary" · "weekly retro" · "weekly planning"
