---
name: project-coach-setup-base
description: Initial project setup for goal coaching system. Use when user says "set up my project", "configure my coaching project", "initialize my goals", or when starting a fresh coaching project with no existing Project-Goals.md. Guides user through conversational setup (one question at a time), generates Project-Goals.md artifact, and introduces daily/weekly workflow trigger phrases.
---

# Project Coach Setup

## Workflow

1. Check for existing Project-Goals.md
2. Ask setup questions (one at a time, stop when user signals enough detail)
3. Generate Project-Goals.md artifact
4. Provide handoff instructions

---

## Step 1: Check for Existing Setup

Search for `Project-Goals.md`:

```bash
find /mnt/user-data/uploads -name "Project-Goals.md" 2>/dev/null
```

**If found:** Offer to revise (generate new version, user replaces old file)
**If not found:** Proceed with setup

---

## Step 2: Setup Questions

Ask one question at a time. Stop when user signals enough detail or you have minimum viable info (primary focus + timezone).

**Essential questions:**
1. Main goal or focus for this coaching project
2. Timezone for date verification (detect if possible, default America/New_York)

**Optional questions** (ask if user wants more detail):
3. Timeframe or milestone (8-week program, quarterly, ongoing)
4. Key metrics to track (distance/pace, study hours, revenue, word count)
5. Context tag preference (W4-D2 format, dates only, custom)

---

## Step 3: Generate Project-Goals.md Artifact

Create artifact using this template (adapt to their responses):

```markdown
# Project Goals

## Primary Focus
[User's goal in their words]

## Target Outcome
[Specific outcome or "To be defined"]

## Timeframe
[Specified timeframe or "Ongoing"]

## Key Metrics
[Metrics mentioned or "Will define through use"]

## Context Tags
[W#-D# format, dates only, or custom]

## Timezone
[Confirmed timezone]

---

## Daily/Weekly Workflow

**Morning:** "good morning" or "gm" → loads yesterday's summary, generates brief

**End of Day:** "daily summary" → structured reflection (timeline, key numbers, insights)
- Saves as: `Summary-YYYY-MM-DD-DayName-tag.md`

**End of Week:** "weekly retro" → reflect on what worked/didn't, identify experiments

**Start of Week:** "weekly planning" → set 2-3 priorities, define success levels

**Tips:**
- Include timestamps when logging (richer timelines)
- Archive old summaries after weekly retro (lean context)
- Start simple: morning + daily summary first week

---

_Edit this document anytime or run "set up my project" again for fresh version._
```

Instruct user to save artifact to project. Confirm artifacts enabled in Settings > Capabilities.

---

## Step 4: Handoff Instructions

Provide minimal instructions:

```
Project-Goals.md is ready. Save it to your project, then:

1. Start logging activities today (include timestamps)
2. End of day: "daily summary"
3. Tomorrow morning: "good morning" or "gm"
```

Offer to answer questions if user needs more guidance.

---

## Edge Cases

**Artifacts disabled:** Provide markdown in code block to copy/paste. Remind to enable in Settings > Capabilities.

**User already shared goals in conversation:** Reference earlier context, ask confirmation before using in Project-Goals.md.

**Minimal vs comprehensive setup:** Adapt question depth to user preference ("just get me started" vs detailed questions).
