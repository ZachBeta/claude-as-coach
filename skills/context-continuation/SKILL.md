---
name: context-continuation-generator
description: Generate mid-day context continuation artifact when chat approaches token limits. Creates comprehensive saveable document for pasting into fresh chat - deterministic alternative to conversation_search for same-day work preservation.
---

# Context Continuation Generator

**Purpose:** Generate comprehensive continuation artifact when context fills up mid-day.

**Key Principle:** Create deterministic, paste-able document - NOT ephemeral summary.

---

## When I Trigger This

**Automatic monitoring:**
- Check token usage after each tool call
- Warn at 80-85% context usage
- Recommend strongly at 85-90%
- Urgent action at 90%+

**User requests:**
- "continue" / "continuation" / "compact context"
- "generate continuation"
- "context is filling up"

---

## What I Do

### 1. Verify Current Time
```bash
TZ='America/New_York' date '+%A, %B %d, %Y - %I:%M %p %Z'
```

### 2. Calculate Context Usage
From system message after tool calls:
- Extract: `Token usage: X/190000`
- Calculate: `(X / 190000) * 100 = Y%`
- State: "Context at Y% (X/190K tokens)"

### 3. Generate Comprehensive Artifact

**Structure:**
```markdown
# [Day], [Date] - Context Continuation ([Time])

**GROUND TRUTH:**
- Current time: [timestamp]
- [Experimental state/cycle]
- [Long-running counters]
- Continuing from chat at [X]% context

## Morning State
[How day started, baseline, interventions]

## Work Completed So Far
### Major Decisions Made
- [Decision with context]

### Documents Created/Modified
- [File: what changed]

### Technical Work
- [Progress on projects]
- [Architectural decisions]

### Insights Gained
- [Key learnings]
- [Pattern recognitions]

## Current Protocol Status
**Experimental phase:** [details]
**Food/metabolic:** [state]
**Next transition:** [timing]

## Queued Work / Where We Left Off
**Immediate next steps:**
- [What to pick up first]
- [In-progress threads]

**Open questions:**
- [Pending decisions]
- [Problems to solve]

**Current cognitive state:** [capacity/constraints]

## Instructions for Fresh Chat
1. Paste this entire document as first message
2. Say "continue" to resume work
3. I'll acknowledge context and pick up where we left off

---
*Generated: [timestamp]*
*Continuation of: [original chat]*
*Context usage: [X]% when generated*
```

### 4. Save to Outputs
Filename: `Context-Continuation-YYYY-MM-DD-HHMM.md`

### 5. Instruct User
```
Continuation artifact created: [filename]

**To continue in fresh chat:**
1. Open new chat in this project
2. Copy entire artifact content
3. Paste as first message
4. Say "continue"

I'll acknowledge the context and resume where we left off.
```

---

## Critical Guidelines

**Comprehensive, not minimal:**
- More detail than conversation_search (~900 token limit)
- Include ALL work context, decisions, state
- User needs complete picture to continue seamlessly

**Structured for parsing:**
- Clear sections with headers
- Bullet points for scannability
- Ground truth at top
- Instructions at bottom

**Timestamp everything:**
- When generated
- What time of day
- Context percentage
- Original chat reference

**Multi-hop support:**
- Name tracks sequence: `...-0945.md`, `...-1315.md`
- Each builds on previous
- Final chat generates daily summary

---

## Advantages Over conversation_search

**Why this is better for same-day continuation:**
1. **Deterministic** - Exact content pasted, no search ambiguity
2. **Comprehensive** - Can be 1000+ tokens if needed
3. **Structured** - Designed for continuation workflow
4. **Explicit** - User sees what context they're loading
5. **Controllable** - Can edit before pasting if needed
6. **No dependencies** - Doesn't rely on search indexing

**When conversation_search still useful:**
- Backfilling old dates
- Cross-day research
- Finding specific past discussions

---

## Context Monitoring Thresholds

**80-85% (152K-162K tokens):**
⚠️ "Context at [X]% - consider generating continuation soon"

**85-90% (162K-171K tokens):**
⚠️ "Context at [X]% - generate continuation soon to avoid incomplete capture"

**90%+ (171K+ tokens):**
🚨 "Context at [X]% - generating continuation NOW"

---

## Integration Notes

**With daily summary:**
- Continuation artifacts are scaffolding
- Daily summary is the record
- Note in summary: "This day spanned [N] chats"

**With weekly retros:**
- Load summaries (not continuations)
- One summary per day regardless of chat count
- Continuations are internal workflow only

---

## Example Usage

```
[After tool call shows 85% context]

Claude: ⚠️ Context at 85% - should we generate continuation?

User: yes

Claude:
[runs date check]
Today is Monday, November 18, 2025 - 1:15 PM EST

[generates comprehensive artifact]

Continuation artifact created: Context-Continuation-2025-11-18-1315.md

**To continue in fresh chat:**
1. Open new chat in this project
2. Copy entire artifact
3. Paste as first message  
4. Say "continue"

---

[In fresh chat]
User: [pastes artifact]
continue

Claude: Got it - continuing from 1:15 PM context.
We left off working on [X]. Ready to continue?
```
