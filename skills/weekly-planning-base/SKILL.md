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
