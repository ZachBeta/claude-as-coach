# Demo Script - Scenario 2: First Week Review

**Duration:** ~15 minutes
**Purpose:** Show the weekly rhythm (morning routine → weekly retro → weekly planning)

---

## Setup (Before Demo - 2 minutes)

### 1. Regenerate Documents
```bash
python scripts/regenerate_demo_dates.py --scenario 2 --demo-day 2025-12-12
```

### 2. Create Claude Project
- Name: "Rob Demo - First Week Review"
- Model: Sonnet 4.5 or Opus 4.5

### 3. Upload Base Skills (3 files)
```
skills/daily-morning-routine-base.zip
skills/retrospective-base.zip
skills/planning-base.zip
```

### 4. Upload Rob's Documents (3 files from `documents-generated/`)
- Summary-*-W1-D1.md (Monday)
- Summary-*-W1-D3.md (Wednesday)
- Summary-*-W1-D5.md (Friday)

---

## Demo Flow (13 minutes)

### Phase 1: Set Context (1 min)

**Explain to audience:**
> "Rob has completed his first week of couch-to-5K. Three runs: Monday, Wednesday, Friday. He almost quit on Wednesday due to shin pain, but pushed through. Now it's Saturday morning and he's ready to review his week."

---

### Phase 2: Morning Routine (3 min)

**Say:**
```
good morning
```

**Expected behavior:**
1. Skill verifies current date (Saturday)
2. Finds yesterday's summary (Friday W1-D5)
3. Generates morning brief with:
   - Yesterday recap
   - Key themes from the week
   - Today's context

**Point out:**
- How the skill finds the most recent summary
- Low cognitive load format (detail first, TL;DR at bottom)
- Connection to previous day's insights

---

### Phase 3: Weekly Retrospective (5 min)

**Say:**
```
weekly retro
```

**Expected flow:**
1. Establishes week boundaries
2. Confirms: "Reviewing Week 1 (Monday-Sunday). Correct?"
3. Loads all 3 daily summaries
4. Generates retrospective with:
   - What Worked (Roses)
   - What Didn't Work (Thorns)
   - Week-over-Week Comparison (N/A for week 1)
   - Experiments to Try
   - Gratitude

**Key narrative points to highlight:**
- **What Worked:** Showing up despite wanting to quit
- **What Didn't Work:** Old shoes causing shin pain, hydration inconsistent
- **Experiments:** Proper warmup routine, earlier bedtime
- **Gratitude:** Wife's support, kids' encouragement

**After generation:**
> "This would normally be saved to Project Knowledge as Weekly-Retro-W1.md"

---

### Phase 4: Weekly Planning (4 min)

**Say:**
```
weekly planning
```

**Expected flow:**
1. Establishes next week's boundaries
2. Confirms: "Planning Week 2 (Monday-Sunday). Correct?"
3. Asks about constraints: "What's non-negotiable this week?"
   - Answer: "Same schedule - Mon/Wed/Fri runs. Getting fitted for new shoes tomorrow."
4. Generates plan with:
   - Coming From (Week 1 context)
   - Priorities (2-3 max)
   - Success Levels (L0-L3)

**Expected priorities:**
- P1: Complete all 3 Week 2 runs (W2R2 x 6)
- P2: Get fitted for proper running shoes
- P3: Establish consistent pre-run hydration

**Success levels example:**
- L0 (Minimum): Complete 2/3 runs without injury
- L1 (Target): Complete 3/3 runs, get new shoes
- L2 (Stretch): No shin pain episodes
- L3 (Exceptional): Feel noticeably better than Week 1

---

## Key Demo Messages

### 1. The Weekly Rhythm
- Morning routine → context loading
- Weekly retro → reflection and learning
- Weekly planning → intentional next week

### 2. Skills Work Together
- Morning routine finds yesterday's summary
- Retro synthesizes the week's summaries
- Planning builds on retro insights

### 3. Base Skills Are Sufficient
- No custom personal skills needed
- Framework provides useful structure
- Rob's specific context (running) fits naturally

### 4. Observation → Reaction Pattern
- Claude leads with observations from data
- User confirms, adjusts, adds context
- Collaborative, not prescriptive

---

## Troubleshooting

**If morning routine doesn't find Friday summary:**
- Check file was uploaded to project
- Verify filename matches expected pattern

**If skills don't trigger:**
- Check skills are enabled in Settings > Capabilities
- Try explicit: "run the daily-morning-routine-base skill"

**If week boundaries are wrong:**
- Claude will ask for confirmation
- Correct if needed during confirmation step

---

## Transition Points

**From Scenario 1:**
> "In Scenario 1, we saw Rob capture his first day. Now we have a full week of data to work with."

**To Scenario 3:**
> "After 4 weeks, Rob will have 4 weekly retros ready for monthly compression. That's Scenario 3."

**To Scenario 4:**
> "Scenario 4 shows Rob after completing the program - 9 weeks of data, exploring what's next."
