---
name: daily-morning-routine-base
description: Framework for starting new daily chat with gentle context loading from previous day's summary. Use when user says "good morning", starts new chat with minimal prompt, or explicitly requests morning brief. Loads yesterday's summary and generates scannable brief. Optimized for low cognitive load during morning wakeup. Extend with personal metrics and protocols.
---

# Daily Morning Routine (Base Framework)

## Process

### 1. Verify Current Date

**CRITICAL FIRST STEP**

```bash
TZ='America/New_York' date '+%A, %B %d, %Y - %I:%M %p %Z'
```

State clearly: "Today is [Day], [Full Date]."

### 2. Find Yesterday's Summary (or Most Recent)

Calculate yesterday from verified date. Look for pattern: `Summary-YYYY-MM-DD-DayName-*.md` in project files.

**Primary:** Match yesterday's date exactly.
**Fallback:** If no exact match, find the most recent Summary file by date.

If using fallback, note the date difference for transparency.

### 3. Confirm with User

```
Found: Summary-2025-11-21-Thursday-[context].md

This should be yesterday's summary. Attend to it for morning brief?
```

Wait for confirmation.

### 4. Attend to Summary

**DO NOT re-read with `view`** - project documents already loaded in context.

Instead, **"heat up the KV cache"** by:
- Referencing specific filename from project_files
- Summarizing key content in detail
- Focusing attention through synthesis

Think: Document already in RAM, just heating cache lines for fast access.

### 5. Generate Morning Brief

**Format: detail-first, TL;DR at bottom**

```markdown
## Ground Truth
Today is [Day], [Full Date]
[Current cycle/phase state]

---

## Yesterday's Detail

### [Major Theme 1]
[Expanded context - 2-3 paragraphs]

### [Major Theme 2]
[Key patterns, decisions, insights]

---

## Yesterday's Snapshot (TL;DR)
- [Key number]
- [Major event]
- [What worked/didn't]
- [Evening state]

## Today's Focus (TL;DR)
- [Priority question]
- [Protocol to follow]
- [What to track]
```

**Structure:** Detail sections first (heats cache on loaded content) → TL;DR at bottom (scannable).

User reads detail OR jumps to TL;DR depending on morning state.

## Morning State Recognition

**Recognize and adapt to user's morning state:**

- **Irritable:** Extra gentle, short responses, minimal questions
- **Foggy:** Clear simple language, bullet points, no complex reasoning
- **Energized:** Can handle detail, ready for planning and discussion
- **Depleted:** Offer to defer complex topics, focus on essentials only

**Signs to watch for:**
- Short responses → may be irritable or foggy
- Typos or confusion → cognitive load too high
- Long thoughtful responses → good capacity, can engage
- Explicit statements → "brain not working yet", "feeling good today"

**Adaptation strategy:**
- Start with brief, scannable format
- User can ask for more detail if they have capacity
- Don't assume morning capacity equals previous day's evening capacity

## Edge Cases

**If Yesterday's Summary Not Found:**

Search for the most recent Summary file:
- Look for pattern `Summary-YYYY-MM-DD-*.md` in project files
- Sort by date (newest first)
- Use the most recent one available

Inform user:
```
Yesterday's summary ([expected_date]) not found.

Found most recent: Summary-[actual_date]-[day]-[context].md
(This is from [N] days ago)

Shall I use this for today's morning brief?
```

Wait for confirmation, then proceed.

**If NO Summaries Found At All:**
```
No summary files found in project.

Would you like me to:
1. Just start fresh today?
2. Help you create your first daily summary tonight?
```

**If Multiple Summaries:**
Show all matches, ask which to attend to.

**If User Starts Mid-Sentence:**
Acknowledge where they are, offer brief or dive straight into their topic.

Example:
```
User: "thinking about that experiment from yesterday"

You: "Good morning! I see yesterday's summary. Want me to pull up the experiment details, or would you like to think through it first?"
```

## Critical Rules

1. **Date verification FIRST** - no assumptions
2. **State today's date clearly**
3. **Confirm before attending to file**
4. **DO NOT re-read files** - attend to loaded content
5. **Two-tier brief** - scannable + comprehensive
6. **Low cognitive load** - morning brain waking up
7. **Adapt to user's morning state**
8. **No complex decisions** unless user initiates
