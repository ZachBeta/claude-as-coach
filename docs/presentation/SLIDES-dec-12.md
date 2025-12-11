---
title: Claude-as-Coach
author: Zach Morek
date: Dec 12, 2025
theme: white
transition: slide
slideNumber: true
---

# Claude-as-Coach

**Zero-build context management**

Zach Morek | Dec 12, 2025

---

# The Problem

- Context dies between Claude conversations
- Building agents is overkill for personal tracking
- You want **continuity**, not infrastructure

---

# What if you could just... talk to it?

And it remembered yesterday.

And last week.

And your goals.

Without writing code.

---

# Claude.ai Projects

::: notes
SWITCH TO: Empty Claude.ai project, then one with documents
SHOW: Project sidebar with documents
:::

- **All documents in context**, every conversation
- Persistent across sessions
- Cross-device (phone + laptop)
- No code required

---

# Projects: The Mental Model

```
┌─────────────────────────────────────┐
│  Claude.ai Project                  │
│                                     │
│  ┌─────────────┐ ┌─────────────┐   │
│  │ Summary-Mon │ │ Summary-Tue │   │
│  └─────────────┘ └─────────────┘   │
│  ┌─────────────┐ ┌─────────────┐   │
│  │ Weekly-Retro│ │ Project-Goal│   │
│  └─────────────┘ └─────────────┘   │
│                                     │
│  Every conversation sees ALL docs   │
└─────────────────────────────────────┘
```

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

# The .zip/.skill Confusion

Anthropic's docs say `.skill` extension

Anthropic's uploader only accepts `.zip`

```bash
# Their tooling outputs:
daily-summary-base.skill  # Won't upload

# What actually works:
daily-summary-base.zip    # Uploads fine
```

PR pending to fix their docs/tooling.

---

# Projects vs Claude Code

| Claude.ai Projects | Claude Code |
|--------------------|-------------|
| Cross-device (phone + laptop) | Terminal-focused |
| Document-centric | Code-centric |
| "Log my run" from phone | "Fix this bug" from IDE |
| Context = your documents | Context = your codebase |
| Skills in Settings | Skills in repo |

**Different tools, different jobs.**

---

# The System: Daily → Weekly Loop

```
        ┌──────────────┐
   ┌───►│ Morning "gm" │
   │    └──────┬───────┘
   │           ▼
   │    ┌──────────────┐
   │    │Daily Summary │──────┐
   │    └──────────────┘      │ x7
   │                          ▼
   │    ┌──────────────┐    ┌──────────────┐
   │    │ Weekly Plan  │◄───│ Weekly Retro │
   │    └──────┬───────┘    └──────────────┘
   │           │
   └───────────┘
```

---

# Fractal Compression

```
Week 1: 7 daily summaries  ─┐
Week 2: 7 daily summaries  ─┼──► Monthly Retro (1 doc)
Week 3: 7 daily summaries  ─┤
Week 4: 7 daily summaries  ─┘

Recent = granular detail
Historical = compressed summaries
```

Context stays manageable. Nothing lost.

---

# Demo Time: Rob the Runner

**Persona:** 39-year-old accountant

**Goal:** Couch-to-5K program

**Week:** 8 of training

4 pre-run scenarios showing the system in action

---

# Demo 1: Morning Routine

::: notes
SWITCH TO: Project "rob-morning"
SHOW: The "gm" command and response
POINT OUT: How it found yesterday's summary
:::

**Trigger:** "gm" or "good morning"

- Verifies today's date
- Finds yesterday's summary
- Generates scannable morning brief

---

# Demo 2: Daily Summary

::: notes
SWITCH TO: Project "rob-daily-summary"
SHOW: Completed summary artifact
POINT OUT: Key Numbers table, TL;DR section
:::

**Trigger:** "daily summary"

- Guided conversation about the day
- Structured output with sections
- Saves to project for tomorrow

---

# Daily Summary: The Output

```markdown
# Wednesday, Dec 11, 2025 - Daily Summary

**GROUND TRUTH:**
- Date: Wednesday, December 11, 2025
- W8-D3 (Week 8, Day 3 of C25K)

## TL;DR
Solid 2.5mi run, felt strong. First time
finishing without walk breaks.

## Key Numbers
| Metric | Value | Notes |
|--------|-------|-------|
| Distance | 2.5 mi | No walk breaks! |
| Pace | 11:30/mi | PR for continuous |
```

---

# Demo 3: Weekly Retrospective

::: notes
SWITCH TO: Project "rob-weekly-retro"
SHOW: Retro pulling from daily summaries
POINT OUT: "What Worked / What Didn't Work" structure
:::

**Trigger:** "weekly retro"

- Reviews 7 daily summaries
- Extracts patterns
- Identifies experiments to run

---

# Weekly Retro: Compression in Action

```
Input: 7 daily summaries (~3500 words)
       ↓
Output: 1 weekly retro (~800 words)

What Worked:
- Morning runs before work
- 10-min warmup routine

What Didn't Work:
- Evening runs (too tired)
- Skipping rest days

Experiments for Next Week:
- Try 5-min post-run stretching
```

---

# Demo 4: Weekly Planning

::: notes
SWITCH TO: Project "rob-weekly-plan"
SHOW: Plan with success levels
POINT OUT: L0-L3 framework
:::

**Trigger:** "weekly planning"

- Reviews previous retro
- Sets priorities with constraints
- Defines success levels

---

# The L0-L3 Success Framework

```
L0 (Minimum): Complete 3 scheduled runs
              "The week isn't a failure"

L1 (Target):  3 runs + all rest day stretching
              "A good week"

L2 (Stretch): L1 + one extra distance run
              "Exceeded expectations"

L3 (Exceptional): Hit 5K distance milestone
                  "Breakthrough week"
```

Calibrated to YOUR goals, not generic metrics.

---

# Repo Structure

::: notes
SWITCH TO: Terminal or VS Code showing repo
:::

```
claude-as-coach/
├── skills/
│   ├── daily-summary-base/
│   │   └── SKILL.md
│   ├── daily-summary-base.zip
│   ├── planning-base/
│   └── retrospective-base/
├── examples/
│   └── rob-the-runner/
│       └── documents/
├── scripts/
│   └── skill_workflow.py
└── docs/
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

Import both. Claude merges them.

---

# Evolution v1-v2: The Search

**v1: Giant Google Doc**
- Daily logging: work, exercise, sleep, diet
- Gaining insights = manual effort or build systems
- Too much cognitive load sifting through it all

**v2: Journaling Agents**
- Various attempts at building agents
- Create summary → copy/paste into new chat
- Repeat daily. Forever.

---

# Evolution v3: The Aha Moment

**Projects + saving to documents**

But I was wasting tokens:

```
┌─────────────────────────────────────┐
│ Project Context (always loaded)     │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐│
│ │Summary-1│ │Summary-2│ │Summary-3││
│ └─────────┘ └─────────┘ └─────────┘│
│ ┌─────────────────────────────────┐│
│ │ instructions.md (5k tokens)     ││ ← Always here
│ └─────────────────────────────────┘│
└─────────────────────────────────────┘
         +
   "Please read Summary-1"  ← Wasted! Already in context
```

---

# Evolution v4-v5: The Pattern

**v4: Skills = on-demand instructions**
- Retro instructions only loaded during retro
- Not burning tokens every conversation

**v5: Skill inheritance**
- What's structural? (shareable)
- What's personal? (private)
- `claude-as-coach` + `claude-as-coach-personal`

No grand plan. Just iterated on friction.

---

# What I Learned

1. **Skills are prompts** - just better organized
2. **Context management is the game** - not agent architecture
3. **Low-build wins** - I'm still using this daily
4. **Personal data stays personal** - base/personal split works

---

# Platform Limitations (Real Talk)

- Skills are **global** (not project-scoped)
- Can't programmatically manage skills
- Mobile upload is clunky
- Context limits exist (Pro vs Max)

Works despite these. Not because of them.

---

# Where This Is Going

**Open Source (now)**

- MIT license
- Base skills shareable
- Rob example included

**Microagent (future)**

- Same pattern, any model
- Tool-calling models (Llama, Qwen, etc.)
- Not locked to Claude

---

# Try It Yourself

```bash
git clone https://github.com/ZachBeta/claude-as-coach
```

Import to Claude.ai project:

- daily-summary-base.zip
- daily-morning-routine-base.zip
- planning-base.zip
- retrospective-base.zip

Say "gm" in a new conversation.

---

# The Pitch

You're AI engineers. You could build this with:

- LangChain
- Custom agents
- RAG pipelines
- Vector databases

Or you could just... use Claude Projects with some markdown files.

**Sometimes the best agent is no agent.**

---

# Questions?

**Repo:** github.com/ZachBeta/claude-as-coach

---

# Appendix: Skill Triggers

| Skill | Triggers |
|-------|----------|
| Morning Routine | "gm", "good morning" |
| Daily Summary | "daily summary", "end of day" |
| Weekly Retro | "weekly retro" |
| Weekly Planning | "weekly planning" |

---

# Appendix: Key Files

| File | Purpose |
|------|---------|
| `QUICKSTART.md` | 5-minute setup |
| `PROJECT-SETUP.md` | Comprehensive guide |
| `skills/*/SKILL.md` | Skill source files |
| `scripts/skill_workflow.py` | Pack/unpack utility |
