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
