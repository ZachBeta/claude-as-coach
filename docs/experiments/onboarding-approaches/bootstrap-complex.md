# Claude-as-Coach: Full Skills Bootstrap

**Instructions:** Copy this entire file and paste it into a fresh Claude.ai project chat. Then say:

> "Use the skill-creator skill to package each of these 5 skills into .zip files I can upload"

Claude will create artifacts for each skill. Save them, then upload via Settings > Capabilities > Skills.

**Note:** This is the full, unabridged version of all skills (~900 lines). For a condensed version, see `bootstrap-simple.md`.

---


## SKILL: project-coach-setup-base

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
1. Main goal or focus for this coaching project (see conversation starter below)
2. Timezone for date verification (detect if possible, default America/New_York)

**Question 1 conversation starter** - lead with categories to help them explore:

> Let's figure out what you want to focus on. Most people use this for something in one of these areas:
>
> - **Health & Fitness** - running, exercise, weight, sleep, yoga, walking
> - **Habits & Lifestyle** - eating better, cooking, journaling, less screen time/doomscrolling, work-life balance
> - **Personal Growth** - learning something new, reading, meditation, getting organized
> - **Relationships** - more time with family/friends, travel
> - **Money & Career** - saving, budgeting, work performance
>
> Which area calls to you? Or if you already have something specific in mind, just tell me!

**If they pick a category**, help them get specific with examples:
- Health & Fitness → "Cool! Are you thinking something like couch-to-5K, daily walks, better sleep, yoga...?"
- Habits & Lifestyle → "Nice! Cooking more? Journaling? Cutting back on screen time or doomscrolling? Something else?"
- Personal Growth → "Great! Learning a language, instrument, skill? Reading more? Meditation practice?"
- etc.

**If they already know** what they want, skip straight to confirming and move on.

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

After generating, guide user to save the artifact to their project:

**Web/Desktop:**
> Click the artifact title → click the dropdown (▼) near "Copy" → select **"Save to Project"**

**Mobile:**
> Tap the artifact → tap "Download" → go to project sidebar → upload the file

If artifacts aren't appearing, remind user to enable in Settings > Capabilities.

---

## Step 4: Handoff Instructions

Provide minimal instructions:

```
Project-Goals.md is ready!

**To save it:**
- Web/Desktop: Click artifact → dropdown (▼) near Copy → "Save to Project"
- Mobile: Download it, then upload to project sidebar

**Then start using the system:**
1. Log activities in this chat today (include timestamps like "2pm - went for a walk")
2. End of day: say "daily summary"
3. Tomorrow morning: say "good morning" or "gm"
```

Offer to answer questions if user needs more guidance.

---

## Edge Cases

**Artifacts disabled:** Provide markdown in code block to copy/paste. Remind to enable in Settings > Capabilities.

**User already shared goals in conversation:** Reference earlier context, ask confirmation before using in Project-Goals.md.

**Minimal vs comprehensive setup:** Adapt question depth to user preference ("just get me started" vs detailed questions).

---


## SKILL: daily-morning-routine-base

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

### 2. Find Yesterday's Summary

Calculate yesterday from verified date. Look for pattern: `Summary-YYYY-MM-DD-DayName-*.md` in project files.

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

**If Summary Not Found:**
```
No summary found for yesterday.

Would you like me to:
1. Search recent conversations for context?
2. Just start fresh today?
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

---


## SKILL: daily-summary-base

---
name: daily-summary-base
description: Framework for creating end-of-day summary documents. Use when user says "daily summary", "generate summary", or similar at end of day. Provides structured markdown template with date verification, filename patterns, and formatting guidelines. Extend with personal metrics and domain-specific content.
---

# Daily Summary Generator (Base Framework)

**Purpose:** Create end-of-day summary document for the specific date being summarized.

**Key principle:** Summary is OF a date, not FOR the next day. Filename matches the events it contains.

## Process

### 1. Verify Current Date

**CRITICAL FIRST STEP** - Prevents date confusion

```bash
TZ='America/New_York' date '+%A, %B %d, %Y - %I:%M %p %Z'
```

Confirm actual date in user's timezone.

### 2. Determine Summary Date

Ask user: "Which date's summary are we generating?"

**Typical scenarios:**
- End of day, same chat: "Today" (the date just verified)
- Next morning: "Yesterday" (verified date - 1)
- Backfilling: User provides specific date

**Always confirm:** "Generating summary for [Day], [Full Date]. Correct?"

### 3. Ask for Context Tag

"What's the context tag for this day?"

User provides tag representing experimental state for that specific day.

### 4. Generate Filename

**⚠️ CRITICAL: Filename must follow template exactly**

**Format:**
```
Summary-YYYY-MM-DD-DayName-[context-tag].md
```

**Example:**
```
Summary-2025-11-15-Saturday-example-tag.md
```

**Rules:**
- Date in filename = date of events inside (NOT next day)
- Day name format: `Monday`, `Tuesday`, etc. (full name, capitalized)
- Context tag: User-provided, hyphen-separated
- Save to: `/mnt/user-data/outputs/`
- Common mistake: Wrong date, generic names

**Critical:** Date in filename = date of events inside.

### 5. Check Context Usage (Optional)

After tool calls, system shows token usage:
```
Token usage: 127200/190000; 62800 remaining
```

**Interpret:**
- <75%: Plenty of room
- 75-85%: Good time for summary
- 85-95%: Generate soon
- >95%: Generate immediately

Note to user if high: "Context at [X]% - generating summary now to capture full day."

### 6. Create Document Structure

**Formatting rules:**
- Use only standard markdown (headers, lists, bold, italic, code blocks, tables)
- NO HTML tags (`<details>`, `<summary>`, `<div>`)
- ASCII-safe characters only:
  - Use `->` not `→`
  - Use `"` not `""`
  - Use `-` not `—`
  - Avoid Unicode special characters

**Emoji usage guidelines:**

**Projects limitation:** Claude Projects file export mangles UTF-8 emojis into broken Unicode (e.g., `ðŸ"¬` instead of 🔬). Root Claude.ai has clean artifact view, but Projects does not (yet).

**Recommended pattern:**
- **Avoid emojis in data sections** (tables, timestamps, key metrics) - keep machine-readable
- **Use sparingly in narrative sections** if they add meaning
- **Consolidate at document end** for easy cleanup:
  ```markdown
  ✨🔬🧪💻🚀
  ```
  Single line after wrap-up = easy to find/remove if export mangles them

**Export preservation strategy:**
1. View summary in Projects web UI (clean UTF-8)
2. Copy-paste into local text editor (preserves emojis)
3. OR: Accept export breakage, manually clean up `ð` characters on local save
4. **Future:** Nanoagent will have proper UTF-8 file handling + custom UI

**When in doubt:** Use plain text. Emojis are decorative, not essential. Prefer clarity over style.

**Required sections:**

```markdown
# [Day], [Date] - Daily Summary

**GROUND TRUTH:**
- Date: [Full day and date being summarized]
- [Context state - cycle/phase/day info]
- [Long-running counters if applicable]

---

## TL;DR - Day Summary

[2-3 sentence summary of trajectory]
[Key decision or insight]
[How capacity showed up]

---

## Key Numbers

| Metric | Morning | Evening | Notes |
|--------|---------|---------|-------|
| [Data] | | | |

---

## Timeline

### Detailed Events

[Chronological events with timestamps]

---

## Insights & Learnings

### What This Day Revealed

[Major insights, patterns, experimental results]

---

## Decisions Made

### What Was Decided

[Decisions for future, protocol adjustments, changes]

---

## What Mattered This Day

[Clear summary of day's significance]
[No ambiguity]
```

### 7. Save to Outputs

```
/mnt/user-data/outputs/Summary-YYYY-MM-DD-DayName-context-tag.md
```

### 8. Remind User

"Summary created: Summary-2025-11-22-Saturday-[context-tag].md

This captures Saturday's events. Click 'add to project' to save it."

## Critical Rules

1. **Date verification FIRST** - bash command, no assumptions
2. **Summary date = events date** - filename matches content, NOT next day
3. **User confirms date** - "Generating summary for [Day]. Correct?"
4. **Filename follows format** - ISO date + day name + exact tag user provided
5. **Ground truth at top** - absolute date being summarized in document
6. **Save to outputs** - user manually adds to project

## How This Differs From "Carryover"

**Old approach (broken):**
- Filename: Carryover-2025-11-16-Sunday.md
- Contains: Saturday's events
- Result: Off-by-one error for weekly reviews

**Current approach (correct):**
- Filename: Summary-2025-11-15-Saturday.md
- Contains: Saturday's events
- Result: Weekly review searches Nov 10-16, gets correct events

The summary IS the daily record.

---


## SKILL: weekly-planning-base

---
name: weekly-planning-base
description: Base framework for weekly planning - plan week ahead based on what worked, what didn't, and what's possible now. Use when user says "weekly planning", "plan the week", "start of week", or at beginning of week. Generates forward-looking experiment design with 2-3 priorities max, staged experiments, and Level 0-3 success framework. Identifies constraints FIRST before suggesting priorities. Optimized for working with actual capacity, not aspirational goals. Adaptable to any domain.
---

# Weekly Planning (Base Framework)

**Format:** Forward-looking experiment design.

**Core sections:**
1. **Coming From** - Where capacity is now (based on retro)
2. **Priorities** - 2-3 key focuses for the week
3. **Experiments** - What to test/try/explore
4. **Success** - What "good enough" looks like (Levels 0-3)

## Process

### 1. Establish Week Boundaries

```bash
# Adjust timezone as needed
date '+%A, %B %d, %Y - %I:%M %p %Z'

# Show week being planned
# (Adjust dates and command for your system/timezone)
```

**Confirm:** "Planning week: [Start Date] - [End Date]. Correct?"

### 2. Load Context

**Read:**
- This week's retro (what worked, what didn't, what to improve)
- Monthly/quarterly plans (strategic direction)
- Current capacity state (from retro or recent logs)
- Relevant project documents

**Use past_chats tool to search for:**
- Ongoing situations (projects, commitments, deadlines)
- Context about challenges mentioned in retro
- Recent conversations about upcoming week

**Purpose:** Understand where capacity is NOW, not where it "should" be.

### 2.5. Identify Constraints First ⚠️ CRITICAL STEP

**Before generating provisional plan, identify what's fixed:**

This prevents suggesting priorities that ignore non-negotiable commitments or known energy drains.

**Ask about:**
- **Non-negotiable commitments:** External deadlines, appointments, obligations (time-bounded, can't move)
- **Known draining events:** High-effort tasks, difficult conversations, energy-intensive work (energy cost, needs planning around)
- **Timeline pressures:** Reverse-engineering from future dates, dependencies (affects sequencing)
- **Ongoing situations:** Current experiments, regular commitments, patterns (context that shapes possible)

**Example questions:**
- "What's non-negotiable this week that I should plan around?"
- "Any known energy drains coming up? (When, how long, recovery time needed?)"
- "What constraints should I know about before suggesting priorities?"
- "Are there any external deadlines or commitments I'm missing?"

**Common patterns:**
- Time-intensive commitments → plan light capacity those days
- External deadline → reverse engineer from that anchor
- Regular appointments → buffer around them
- Ongoing experiments → maintain consistency, don't disrupt data

**Purpose:** Understand what's fixed before suggesting what's flexible.

**Why this matters:** Suggesting "3 deep work sessions this week" when certain days are consumed by commitments = plan sets user up for failure. Constraints first → realistic priorities second.

### 3. Generate Provisional Plan

**After identifying constraints, create initial framework artifact.**

**Why provisional first:**
- Gives structure for conversation to fill in
- User sees plan evolving based on input
- Easier to react/refine than generate from scratch
- Constraints already incorporated in suggestions

**Create initial artifact with:**
- Brief "coming from" summary (where capacity is, major constraints identified)
- 2-3 suggested priorities (based on retro patterns AND constraints)
- Potential experiments (based on "what didn't work" from retro)
- Success definition using Level 0-3 framework (empty, to be calibrated conversationally)

**Lead with constraint-aware suggestions:**
- "Given [constraint], [Priority 1] seems like it needs to go first. That track?"
- "With [X hours available after constraint], [Priority 2 and 3] feel doable?"
- Present priorities in order, already accounting for fixed constraints

**User then reacts:** Confirms, reorders, adds missing context, adjusts to reality

**Example structure:**

```markdown
# Week [Number] Plan: [Theme/Focus]

**Week:** [Date range]

---

## Coming From

- [Key capacity insight from last week's retro]
- [Major constraints this week]
- [What worked/didn't from last week]
- [2-3 bullets max for scannability]

---

## This Week's Priorities

Based on constraints and patterns:

1. [Priority 1 - constraint or non-negotiable]
2. [Priority 2 - from "what worked" + strategic goals]
3. [Priority 3 - optional stretch]

Does this ordering work given [specific constraint]?

---

## Experiments to Try

From "what didn't work" last week:
- [Experiment 1 to test]
- [Experiment 2 to explore]

---

## Success Looks Like

### Level 0: Foundation
*Minimum viable engagement with the week*
*What counts as "showed up" given current context*

### Level 1: Base
[Minimum viable progress given current context]

### Level 2: Target
[Good week for current capacity]

### Level 3: Reach
[Exceptional but achievable]

**Good enough = Level 0 always counts. Level 1 is solid. Level 2 is great. Level 3 is amazing.**

---

## Notes

[Week-specific context, reminders, meta-observations]
```

**Keep it brief.** 2-3 priorities max. Less is more.

### 4. Fill In Conversationally

**The conversation IS the planning.**

**Lead with observations from retro + constraints:**
- "Last week [X] worked well. Seems like [continuing Y] makes sense?"
- "You mentioned [constraint]. Should we plan around that being [duration/impact]?"
- "Based on current capacity and [constraint], [2-3 priorities] feel doable. That track?"

**Let user react and refine:**
- User confirms or redirects priorities
- User adds context you missed
- User sets realistic bar for success at each level
- User identifies what's actually possible vs wishful thinking

**Core principle:** Ask about constraints → Suggest based on data → User refines

**Section-specific flow patterns:**

**"Coming From" flows fast:**
- Pull directly from retro data (capacity state, major wins/challenges)
- Observation → Agreement pattern
- 2-3 sentences, mostly confirmation
- Low friction, quick progress

**"Priorities" needs conversation:**
- Constraints must be identified FIRST (Section 2.5)
- Suggest 2-3 based on constraints + retro patterns
- User reacts, reorders, adds context
- Interactive, takes time to get right
- This is the core of the planning work

**"Experiments" semi-automatic:**
- Pull from retro "What Didn't Work" section
- Experiments already proposed in retro
- Planning selects which ones to run this week
- Quick decisions based on capacity + priorities

**"Success Levels" interactive:**
- User defines what Level 0-3 actually means
- Calibrated to current capacity (from retro)
- Conversation helps set realistic bars
- Foundation (L0) varies by context

**Adjust pacing:** "Coming From" = brisk, "Priorities" = depth needed, "Experiments" = selection mode, "Success" = calibration.

Less friction than generating from scratch.

### 5. Update Artifact in Real-Time

Make changes as conversation progresses, not at end.

User sees artifact evolving based on input.

### 6. Save Final Version

**⚠️ CRITICAL: Filename must follow template exactly**

**Format:**
```
Weekly-Plan-YYYY-MM-DD-to-DD.md
```

**Example:**
```
Weekly-Plan-2025-11-17-to-23.md
```

**Rules:**
- Format: `Weekly-Plan-YYYY-MM-DD-to-DD.md`
- Dates: Week start → week end being planned
- Save to: `/mnt/user-data/outputs/`
- Common mistakes: Wrong dates, generic names like `weekly-plan.md`

**Save:**
```
/mnt/user-data/outputs/Weekly-Plan-YYYY-MM-DD-to-DD.md
```

**Remind user:** "Click 'add to project' to save permanently."

## Key Principles

### Less Is More
- 2-3 priorities maximum
- Specific experiments, not vague intentions
- "Good enough" beats "perfect"
- Room for life to happen

### Work With What Is
- Start from actual capacity (from retro), not imagined capacity
- Build on what worked, experiment with what didn't
- Adjust expectations based on current state
- No "shoulds" - just "what's possible now?"

### Experiments Over Commitments
- Frame as tests, not obligations
- "Try X and see what happens"
- Success = learning, not perfection
- Permission to pivot if data changes

### Flexible Success Framework
- Level 0 is always valid (foundation matters)
- Level 1-3 adapt to current capacity
- Same framework works for all contexts
- Progress is relative to starting point

## Flexibility Guidelines

**Extended thinking mode:**
- **Enabled:** Higher quality pattern recognition, better constraint identification, deeper retro synthesis
- **Disabled:** Token conservation, stays within conversation limits, may miss subtle patterns
- **Trade-off:** User choice based on current constraints vs quality needs
- **Recommendation:** Extended thinking helpful for planning (synthesizes retro + constraints + strategy)

**Structure is guide, not prescription:**
- Skip sections if not relevant
- Add custom sections (domain breakdowns, specific project planning)
- Format adapts to what's being planned (learning, projects, habits, health, business)
- Length adapts to complexity

**Planning vs Execution:**
- **Planning documents options and experiments** (what COULD be done)
- **Execution adapts in real-time** (what ACTUALLY gets done based on emerging capacity)
- Week plan is hypothesis, not contract
- Permission to pivot based on actual data
- Retro captures what actually happened vs plan

## Integration Patterns

### Retro → Planning Flow

**Natural sequence:** Weekly retro insights fresh → immediately plan next week

**Current practice:** Separate conversations (retro in one chat, planning in another)

**Potential optimization:** If context headroom available after retro, continue into planning same conversation

**Trade-offs:**
- **Benefit:** No context loss between retro and planning
- **Risk:** May max out mid-planning (awkward breakpoint)
- **Consideration:** Retro already token-heavy with extended thinking

**User choice:** Some prefer combined flow, others prefer fresh start for planning

### Context Management (Fractal Rollup)

**Daily → Weekly → Monthly pattern:**
- Daily logs (7 docs) → Weekly retro (1 doc) → Archive dailies locally
- Weekly retros (4 docs) → Monthly retro (1 doc) → Archive weeklies from project
- Result: Project context stays lean, full history preserved locally

**Archival workflow:**
- After generating retro, back up daily logs to local storage
- Remove archived docs from project to free context window
- Retro becomes compressed reference for that period

**This enables sustainable long-term use without context explosion**

## Planning-Retro (Skill Improvement)

**At end of planning session, reflect on the process:**

**What worked:**
- [What made this planning session effective?]
- [Which parts of the skill/process helped?]

**What didn't work / Improvements needed:**
- [What was awkward or inefficient?]
- [What's missing from skill documentation?]
- [Edge cases discovered?]

**Action items:**
- Update skill if changes needed
- Note improvements in planning document (Notes section)
- Feed forward to next planning session

**Document the planning-retro in the week plan itself** (Notes section or dedicated section at end)

## Memory Review Integration

**Planning should include memory review:**
- Check if memories need updates based on recent changes
- Use `memory_user_edits` tool to view/update as needed
- Ensures memory stays current with capacity/context shifts

**Typical timing:** After retro, before or during planning conversation

---


## SKILL: weekly-retrospective-base

---
name: weekly-retrospective-base
description: Base framework for weekly retrospectives - reflect on what worked, what didn't, and how to improve. Use when user says "weekly retro", "weekly retrospective", "end of week", or similar at week's end. Generates empty structure first, fills conversationally through observations and reactions. Adaptable to any domain (learning, projects, habits, health, business).
---

# Weekly Retrospective (Base Framework)

**Format:** Traditional product/engineering retro adapted for individual growth work, inspired by Rose/Bud/Thorn with time-scale sections and gratitude closing.

**Six sections:**
1. **What Worked** (Roses) - Want more of this
2. **What Didn't Work** (Thorns) - Challenges + experiment proposals (Buds)
3. **Week-over-Week Comparison** - Trajectory analysis
4. **Monthly Progress Check** - Alignment with monthly goals
5. **Retro-Retro** - Improve the retrospective process itself
6. **Gratitude** - Positive closing anchor (peak-end rule)

## Process

### 1. Establish Week Boundaries

```bash
# Adjust timezone as needed
date '+%A, %B %d, %Y - %I:%M %p %Z'

# Show week being reviewed
# (Adjust dates and command for your system/timezone)
```

**Confirm:** "Reviewing week: [Start Date] - [End Date]. Correct?"

**Week convention:** Typically previous Sunday through current Saturday (when run on Sunday)
- Captures full 7 days of data
- Sunday retro runs before Sunday daily work
- Ensures no data loss at week boundaries
- Adapt to your preferred week start/end

### 2. Load Context Intelligently

**Primary source: Daily logs/summaries** (if using daily tracking)
- Review logs for the week
- Review previous week's retro (for comparison)
- Review monthly plan (for goal alignment)
- Documents pre-loaded in project context if available

**Use conversation_search ONLY when:**
- Logs missing or incomplete
- User requests deeper dive into specific event
- Need to verify particular detail
- Default: trust summaries, save tokens

**If daily logs missing:** Note which days, offer to generate or proceed with partial data.

### 3. Generate Empty Framework First ⚠️ CRITICAL

**ALWAYS create structure-only artifact with placeholders BEFORE filling content.**

Do NOT generate wall-of-text. Do NOT skip to final output.

**The empty framework enables:**
- User reactions and observations emerge naturally
- Conversational fill-in (not generation from scratch)
- Pattern recognition through back-and-forth
- Real-time artifact updates based on user input

**⚠️ CRITICAL: Filename must follow template:**
- Format: `Weekly-Retro-YYYY-MM-DD-to-DD.md`
- Example: `Weekly-Retro-2025-11-17-to-23.md`
- Save to: `/mnt/user-data/outputs/`
- Common mistake: Generic names like `weekly-retro-framework.md`
- User will need to manually rename if wrong, so get it right

**Create structure-only artifact with placeholders:**

```markdown
# Week [Number] Retro: [Leave blank - user will title]

**Week:** [Date range]
**Context:** [Brief context line about what user is tracking]

---

## TL;DR - Week Summary

**Format: Bulleted list for easy scanning**
- Major theme/pattern 1
- Major theme/pattern 2
- Key discovery/breakthrough
- Primary challenge/setback
- Overall trajectory assessment

---

## What Worked (Want More Of)

[Empty - fill conversationally]

---

## What Didn't Work (+ Experiments to Try)

**Format: Challenge → Proposed experiments**

### Challenge 1: [What didn't work]
**Why problematic:** [Impact/consequence]
**Experiments to try:**
- **Next week:** [Immediate test]
- **Next cycle:** [Medium-term experiment]
- **Longer timeframe:** [Deferred/staged approach]

### Challenge 2: [What didn't work]
**Why problematic:** [Impact/consequence]
**Experiments to try:**
- **Next week:** [Immediate test]
- **Next cycle:** [Medium-term experiment]
- **Longer timeframe:** [Deferred/staged approach]

**Note:** Retro documents options, planning decides which to run

---

## Progress Tracking Across Timeframes

**Compare against multiple intervals when data available:**

### Last Week
**Previous week:** [Brief summary]
**This week:** [Brief summary]
**Trajectory:** [Better/Stable/Declining + evidence]

### Last Month (if available)
**Month ago:** [Key state/capacity]
**Now:** [Current state/capacity]
**Change:** [What shifted?]

### Last Season/Quarter (if available)
**Previous period:** [Baseline state]
**Now:** [Current state]
**Arc:** [Overall trajectory]

### Last Year (if available)
**Year ago:** [Where things were]
**Now:** [Current position]
**Journey:** [Major transformations]

**Focus on:** Capacity trends, pattern shifts, what compounds over time

---

## Monthly Progress Check

**Monthly theme/goals:** [From monthly plan]
**This week's contribution:** [Assessment]

---

## Retro-Retro (Improve the Retro Process)

[Empty - meta observations about retrospective itself]

---

## Gratitude

[Empty - positive closing anchor]

What are you grateful for from this week?
```

**Framework provides structure, conversation provides content.**

### 4. Fill Framework Through Observations → Reactions

**The conversation IS the retro.**

**Pattern:**
1. **Make specific observation** from log data
2. **User reacts** (confirms, refines, adds context)
3. **Update artifact** in real-time based on reaction
4. **Repeat** for each section

**Lead with observations, not questions:**
- ✅ "I noticed [pattern from logs]. Want more of that?"
- ✅ "Seems like [challenge] kept coming up. What experiment could address it?"
- ✅ "The [tool/process] seemed to help with [outcome]. That track?"
- ❌ "What was most significant this week?" (requires generation from scratch)
- ❌ "What do you want more of?" (open-ended, high friction)

**Core principle:** Humans react better than they generate from scratch.

**Section-specific flow patterns:**

**"What Worked" naturally flows faster:**
- Observation → Agreement pattern
- Mostly confirmations with minor refinements
- Low friction, quick progress through items
- User can react/refine rather than generate from scratch

**"What Didn't Work" benefits from more conversation:**
- Each challenge needs paired experiments developed
- Interactive back-and-forth works well here
- User can defer challenges ("skip that for now")
- User can add context that shapes experiment proposals
- Takes more time but generates better actionable ideas

**Adjust pacing accordingly:** "What Worked" = brisk, "What Didn't Work" = conversational depth.

**For "What Didn't Work" section:**
- Each challenge should pair with proposed experiments
- "X didn't work → let's try Y instead"
- Experiments document options, planning will select which to run
- Ideas in retro doc stay available for future planning cycles

**For "Gratitude" section:**
- Save for last (positive emotional anchor via peak-end rule)
- Even hard weeks have something to appreciate
- Can be small (framework worked, learned constraints, held boundaries)
- Ends retro on positive note regardless of week difficulty

**For "Retro-Retro" section:**
- **Focus exclusively on improving the retrospective process itself**
- NOT for general meta-observations about work/life/domain
- Questions to guide discussion:
  - Did the structure work? Too rigid or too loose?
  - Was conversation_search helpful or redundant?
  - Did observations → reactions pattern feel natural?
  - Did any section feel forced or unnecessary?
  - What would make next week's retro better?
  - Was filename correct? Token usage appropriate?
  - Did extended thinking mode matter?
- **Examples of good Retro-Retro observations:**
  - "Filename was wrong, needs emphasis in skill"
  - "What Worked section went fast, What Didn't Work needed more conversation"
  - "Extended thinking enabled mid-chat affected quality"
- **Examples of NOT Retro-Retro observations:**
  - Domain-specific learnings (goes in Gratitude or What Worked)
  - Specific improvements to try (goes in What Didn't Work → Experiments)
  - Project progress (goes in Monthly Progress)
- **Key point:** Insights here should lead to updates in weekly-retrospective skill
- If process broken, propose concrete skill changes
- Close the feedback loop: retro-retro → skill evolution

### 5. Update Artifact in Real-Time

Make changes as conversation progresses, not at end.

User sees artifact evolving based on their input.

### 6. Save Final Version

**Filename:**
```
Weekly-Retro-YYYY-MM-DD-to-DD.md
```

**Example:**
```
Weekly-Retro-2025-11-10-to-16.md
```

**Save:**
```
/mnt/user-data/outputs/Weekly-Retro-YYYY-MM-DD-to-DD.md
```

**Remind user:** "Click 'add to project' to save permanently."

## Flexibility Guidelines

**Extended thinking mode:**
- **Enabled:** Higher quality analysis, deeper pattern recognition
- **Disabled:** Token conservation, stays within conversation limits, may degrade quality slightly
- **Trade-off:** User choice based on current constraints (testing context limits vs optimizing output)

**Structure is guide, not prescription:**
- Skip sections if not relevant
- Add custom sections (domain breakdowns, project tracking)
- Format adapts to what's tracked (health, learning, projects, habits, business)
- Length adapts to complexity

**Focus on signals, not noise:**
- Patterns over individual events
- Insights over data dumps
- Actions over descriptions
- "So what?" over "What happened?"

**Retro vs Planning Boundary:**
- **Retro generates experiment ideas** (documents options/proposals)
- **Planning selects experiments to run** (makes strategic decisions)
- Keeps retro as pattern recognition, planning as resource allocation
- Experiment ideas in retro doc stay available for future planning cycles
- Deferred experiments not lost, available in context for later

**Section Purpose Clarity:**
- **What Worked:** Roses - amplify these patterns
- **What Didn't Work:** Thorns + Buds - challenges paired with experiments to try
- **Week-over-Week:** Trajectory - building or declining?
- **Monthly Progress:** Alignment - contributing to goals or drifting?
- **Retro-Retro:** Process - making retrospective itself better
  - **Meta-improvement loop:** Insights from retro-retro should lead to updates in this skill
  - If retro process isn't working well, propose skill changes
  - Skill evolves based on actual usage patterns
- **Gratitude:** Anchor - positive closing via peak-end rule

## Core Principles

**Good → More:** Identify what worked, do more of it.

**Bad → Experiment:** Identify what didn't work, propose experiments to change it.

**Meta → Improve:** Identify how to make the retrospective process itself better.

**Peak-End Rule:** Humans remember emotional peak + final moment. End with gratitude for positive anchor, even in hard weeks.

**Retro Documents Options, Planning Decides:** Experiment ideas generated in retro stay available for future planning. Not making decisions, documenting possibilities.

## Edge Cases

**First retro (no previous week):**
- Skip week-over-week comparison
- Focus on establishing baseline patterns

**Missing data:**
- Proceed with available information
- Note gaps for future improvement

**Multiple projects/domains:**
- User can request separate sections or integrated view
- Adapt structure to their mental model

## Post-Retro Workflow

### Context Check and Planning Flow

**After completing retro, check conversation context:**

```python
# Rough heuristic - actual tokens vary
if conversation_appears_under_100k_tokens:
    "Context headroom available. Continue with planning in this conversation?"
else:
    "Context getting full. Start fresh conversation for planning recommended."
```

**Benefits of combined retro→planning:**
- Retro insights immediately inform planning
- No context loss between reflection and forward planning
- Natural flow: what worked/didn't → what to try next

**Risks:**
- May max out mid-planning (awkward interruption)
- Retro already token-heavy with extended thinking
- Some prefer clean separation

**User choice:** Offer option, respect preference for combined vs separated

### Memory Review

**Review and update memories after retro:**
- Use `memory_user_edits` tool to view current memories
- Check if memories need updates based on:
  - Capacity changes (significant improvements/declines)
  - New constraints discovered (protocols, triggers, limits)
  - Strategic shifts (priorities changed, timelines adjusted)
  - Preferences evolved (what actually works vs what "should" work)
- Update memories to reflect current reality, not outdated state

**Typical timing:** After retro, before or during planning

**Memory as living document:** Retro reveals what changed, memory captures it for future context

### Archival Reminder

**Fractal rollup pattern:**
- Daily logs → Weekly retro (compression) → Archive dailies
- Weekly retros → Monthly retro (compression) → Archive weeklies
- Keeps project context lean while preserving full history locally

**After generating weekly retro:**
1. Back up daily logs to local storage
2. Remove daily logs from project (frees context window)
3. Weekly retro becomes compressed reference for that period

**This enables sustainable long-term usage without context explosion**

**Note:** This is manual step currently - no automated archival in Claude Projects yet

---


## Next Steps

After Claude creates the 5 skill .zip files:

1. Save each artifact
2. Go to Settings > Capabilities > Skills
3. Upload each .zip file
4. Confirm all 5 skills are enabled
5. Return to your project and say "set up my project" to begin!
