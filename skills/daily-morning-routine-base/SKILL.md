---
name: daily-morning-routine-base
description: Framework for starting new daily chat with gentle context loading from previous session's summary. Use when user says "good morning", starts new chat with minimal prompt, or explicitly requests morning brief. Loads most recent summary and generates scannable brief. Optimized for low cognitive load during morning wakeup. Includes contemplation thread reopening from summary. Extend with personal metrics and protocols.
---

# Daily Morning Routine (Base Framework)

## Process

### 1. Verify Current Date

**CRITICAL FIRST STEP**

```bash
TZ='America/New_York' date '+%A, %B %d, %Y - %I:%M %p %Z'
```

State clearly: "Today is [Day], [Full Date]."

### 2. Find Most Recent Summary

Look for pattern: `Summary-YYYY-MM-DD-*.md` or `Summary-YYYY-MM-DD-Day-to-DD-Day-*.md` in project files.

**Note:** Summaries may use range-based naming if they span calendar boundaries (e.g., `Summary-2026-01-15-Thu-to-16-Fri-week-5-long-run.md`).

Sort by date (newest first), use the most recent one.

If the most recent summary is from more than 1 day ago, note the gap.

### 3. Confirm with User

```
Found: Summary-2026-01-15-Thu-to-16-Fri-week-5-long-run.md

This is the most recent summary. Attend to it for morning brief?
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

**Format: detail-first, TL;DR at bottom, threads at end**

```markdown
## Ground Truth
Today is [Day], [Full Date]
[Current training phase/week]

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
- [What to track]
- [Training focus]
```

**Structure:** Detail sections first (heats cache on loaded content) → TL;DR at bottom (scannable).

User reads detail OR jumps to TL;DR depending on morning state.

### 6. Reopen Contemplation Threads

**After generating the brief, do NOT close the conversation.**

Pull from summary's "Tomorrow's Seeds" section:

```markdown
---

## Threads Still Warm

[From summary's "Threads still warm" - contemplation topics, questions raised, decisions pending]

**From yesterday:** "[One thing from today" - the single insight or question that was sitting with the user]

---

What's present this morning?
```

**Key principles:**
- Surface what's still alive, not just what needs doing
- Offer the contemplation threads, don't push them
- End with texture check, not task prompt
- Hold space open - the brief is the start of conversation, not its conclusion

### 7. Conversation Holding Pattern

**After the brief and threads, maintain open stance:**

- Don't close with "let me know when ready" or "I'm here if you need me"
- Keep threads named and available
- Offer texture checks: "What's present?" / "What's the morning like?"
- Surface insights from yesterday that might want to continue

**Example endings:**

OK: "Yesterday's session surfaced the pacing strategy question. That thread is still here. What's present this morning?"

OK: "The new route is queued. The group run is tonight. What's the texture of the morning?"

Not OK: "Let me know if you need anything else."

Not OK: "I'm here when you're ready to continue."

## Morning State Recognition

**Adapt response style (not engagement level) to user's state:**

- **Irritable:** Shorter sentences, softer tone, fewer questions per message
- **Foggy:** Simpler language, more bullet points, one idea at a time
- **Energized:** Can handle longer form, ready for back-and-forth
- **Depleted:** Gentler pacing, but still present and holding threads

**Signs to notice:**
- Short responses → simplify your language
- Typos or confusion → slow down, use bullets
- Long thoughtful responses → match their depth
- Explicit statements → "brain not working yet", "feeling good today"

**Key distinction:** Adapting style means changing HOW you communicate, not WHETHER you stay engaged. Stay present across all states - just adjust the texture.

## Edge Cases

**If No Summary Found:**

Search for the most recent Summary file:
- Look for pattern `Summary-YYYY-MM-DD-*.md` in project files
- Sort by date (newest first)
- Use the most recent one available

Inform user:
```
No summary from yesterday found.

Found most recent: Summary-[actual_date]-[context].md
(This is from [N] days ago)

Shall I use this for today's morning brief?
```

Wait for confirmation, then proceed.

**If NO Summaries Found At All:**
```
No summary files found in project.

Would you like to:
1. Just start fresh today?
2. Help you create your first daily summary tonight?
```

**If User Starts Mid-Thought:**
Acknowledge where they are, offer brief or dive into their topic.

Example:
```
User: "thinking about that pacing strategy from yesterday"

You: "Good morning! I see yesterday's summary. Want me to pull up the pacing details, or would you like to think through it first?"
```

## Critical Rules

1. **Date verification FIRST** - no assumptions
2. **State today's date clearly**
3. **Confirm before attending to file**
4. **DO NOT re-read files** - attend to loaded content
5. **Two-tier brief** - scannable + comprehensive
6. **Reopen threads** - surface Tomorrow's Seeds from summary
7. **Hold space open** - conversation starts, not ends, with the brief
8. **Low cognitive load** - morning brain waking up
9. **Adapt to user's morning state**
10. **No complex decisions** unless user initiates
