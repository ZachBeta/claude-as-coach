---
name: backfill-summary-generator
description: Generate daily summary for past dates using conversation_search. For backfilling timeline when original chat maxed out or summary was never created. Confirms date, searches past chats, generates comprehensive summary document.
---

# Backfill Summary Generator

**Purpose:** Create daily summary for specific past date from archived conversations.

**Use Cases:**
- Original chat maxed out before generating summary
- Backfilling past dates to build timeline
- Generating summary days/weeks after the fact

---

## When I Trigger This

**User requests:**
- "generate summary for [past date]"
- "backfill [date]"
- "create summary from [date]"
- "I need the summary for [date]"

**Context:** Used in FRESH chat (not original daily chat), working from archived conversation data.

---

## Workflow

### 1. Establish Date Ground Truth

**Always first step:**
```bash
# Show current date
TZ='America/New_York' date '+%A, %B %d, %Y - %I:%M %p %Z'

# Show relevant week containing target date
for day in 10 11 12 13 14 15 16; do 
  TZ='America/New_York' date -d "2025-11-$day" '+%A, November %d, 2025'
done
```

Adjust day range to show week containing target date.

### 2. Confirm Target Date

**Prompt user:**
```
I see we're generating a summary. Let me confirm:

Target date: [Day], [Full Date] (based on your request)
Current date: [Today's Day], [Today's Full Date]

Is this correct?
```

**Wait for user confirmation before proceeding.**

### 3. Ask for Context Tag

**Prompt:**
```
What context tag should I use for the filename?

Examples:
- FC1-PhaseA-D2 (Feed Cycle 1, Phase A, Day 2)
- FastC1-D2 (Fast Cycle 1, Day 2)
- Crash-D5 (Crash recovery, Day 5)
- Day24-CrashD10

Your tag: _____
```

Wait for user to provide the tag.

### 4. Search for Target Date's Chat

Use `conversation_search` with date + context keywords:
```
conversation_search("[Month] [Day]" OR "YYYY-MM-DD")
```

Add relevant keywords if user provides:
- Chat title fragments
- Key topics from that day
- Experimental context

**Show results:**
```
Found these conversations:

1. "[Chat title]" (updated [date])
2. "[Chat title]" (updated [date])

Which chat contains [target date]'s events?
```

**Wait for user selection.**

### 5. Generate Summary Document

**Filename format:**
```
Summary-YYYY-MM-DD-DayName-[context-tag].md
```

**Example:**
```
Summary-2025-11-12-Wednesday-FastC1-D2.md
```

**Critical:** Date in filename = date of events inside (NOT today's date).

**Document structure:**
```markdown
# [Day], [Date] - Daily Summary

**GROUND TRUTH:**
- Date: [Full day and date being summarized]
- [Context state - cycle/phase/day info]
- [Dopamine detox or other long-running counters]

---

## TL;DR - Day Summary

[2-3 sentence summary of this day's trajectory]
[Key decision or insight from today]
[How capacity showed up today]

---

## Key Numbers

| Metric | Morning | Evening | Notes |
|--------|---------|---------|-------|
| [Key data] | | | |

---

## Timeline

### Detailed Events

[Chronological events with timestamps from this day]

---

## Insights & Learnings

### What This Day Revealed

[Major insights, patterns recognized, experimental results]

---

## Decisions Made

### What Was Decided

[Decisions for future days, protocol adjustments, experimental changes]

---

## What Mattered This Day

[Clear summary of the day's significance]
[No ambiguity]
```

### 6. Save to Outputs

```
/mnt/user-data/outputs/Summary-YYYY-MM-DD-DayName-context-tag.md
```

### 7. Remind User

```
Summary created: Summary-2025-11-12-Wednesday-FastC1-D2.md

This captures Wednesday's events. Click 'add to project' to save it to your timeline.
```

---

## Critical Rules

1. **Date grounding FIRST** - Bash commands establish ground truth
2. **Summary date = events date** - Filename matches content, NOT next day
3. **User confirms everything** - Date, context tag, which chat to use
4. **Filename follows format** - ISO date + day name + exact tag user provided
5. **Ground truth at top** - Absolute date being summarized in document
6. **Save to outputs** - User manually adds to project

---

## Edge Cases

**Multiple chats for one date:**
- Show all options
- User picks primary daily log (vs side chats)

**No chat found:**
- Tell user: "No conversations found for [date]. Try different keywords or skip it?"
- User decides

**Multi-day chat (crash periods):**
- Ask user: "This chat spans Nov 10-14. Which specific day's summary? (e.g., Nov 12)"
- Generate for that specific day within the larger chat

**Chat content unclear:**
- Ask user to provide key events manually if search results ambiguous

---

## Example Flow

```
User: "Generate summary for Wednesday November 12, 2025 - it was a fasting day"

Claude: 
[runs date commands]

Today is Sunday, November 16, 2025.

Week dates:
Monday, November 10, 2025
Tuesday, November 11, 2025
Wednesday, November 12, 2025
Thursday, November 13, 2025
Friday, November 14, 2025
Saturday, November 15, 2025
Sunday, November 16, 2025

Generating summary for: Wednesday, November 12, 2025
Correct?

User: "yes"

Claude:
What context tag should I use?

User: "FastC1-D2"

Claude:
[searches conversations]

Found:
1. "2025-11-12 Wed. 60-hour fast progress tracking" (updated Nov 13)

Is this the right chat?

User: "yes"

Claude:
[reads chat, generates summary]

Summary created: Summary-2025-11-12-Wednesday-FastC1-D2.md

Click 'add to project' to save it to your timeline.
```

---

## Recovery Context Reference

When generating summaries, include relevant recovery context:
- Month 3.5 of 12-24 month recovery timeline
- Feed/Fast cycling experiments
- Testing food variables systematically
- Baseline capacity tracking
- Target: Feb/March 2026 job search NYC
- Dopamine detox ongoing (started Oct 16/17)

Adjust as user's protocols evolve.
