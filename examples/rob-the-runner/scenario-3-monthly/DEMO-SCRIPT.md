# Demo Script - Scenario 3: Monthly Review

**Duration:** ~12 minutes
**Purpose:** Show fractal compression (4 weekly retros → 1 monthly summary)

---

## Setup (Before Demo - 2 minutes)

### 1. Regenerate Documents
```bash
python scripts/regenerate_demo_dates.py --scenario 3 --demo-day 2025-12-12
```

### 2. Create Claude Project
- Name: "Rob Demo - Monthly Review"
- Model: Sonnet 4.5 or Opus 4.5

### 3. Upload Base Skills (1 file)
```
skills/retrospective-base.zip
```

**Note:** Only retrospective skill needed. We're demonstrating monthly rollup.

### 4. Upload Rob's Documents (5 files from `documents-generated/`)
- Weekly-Retro-*-W1.md
- Weekly-Retro-*-W2.md
- Weekly-Retro-*-W3.md
- Weekly-Retro-*-W4.md
- Summary-*-W4-D5.md (most recent context)

---

## Demo Flow (10 minutes)

### Phase 1: Set Context (2 min)

**Explain to audience:**
> "Rob has completed his first month of couch-to-5K. He has 4 weekly retrospectives - one for each week. Now it's time to step back and see the bigger picture. This is where the fractal compression pattern shows its value."

**Show the data volume:**
> "Each weekly retro is about 2-3 pages. That's roughly 10 pages of weekly reflections. The monthly rollup will compress this into a single document that preserves the essential insights while reducing cognitive load."

---

### Phase 2: Monthly Retrospective (6 min)

**Say:**
```
monthly retro
```

Or more explicitly:
```
Let's do the monthly retrospective for October
```

**Expected flow:**
1. Skill establishes month boundaries
2. Confirms: "Reviewing October (Weeks 1-4). Correct?"
3. Loads all 4 weekly retros
4. Generates Monthly-Rollup-October.md with:
   - Month Overview
   - Week-by-week progression
   - Physical transformation summary
   - Mental transformation summary
   - Key patterns identified
   - What worked / didn't work (month level)
   - Learnings to carry forward
   - Next month preview
   - Gratitude

**Key points to highlight as it generates:**

**1. Compression in action:**
> "Notice how it's synthesizing 4 weeks of detail into themes. We're not losing information - we're distilling it."

**2. Pattern emergence:**
> "At the weekly level, each week felt like its own struggle. At the monthly level, you can see the trajectory: Week 1 survival, Week 2 consistency tested, Week 3 breakthrough, Week 4 milestone."

**3. Metric aggregation:**
> "Individual run metrics become monthly trends. 203 lbs → 199 lbs. 1-minute runs → 10-minute runs. The monthly view makes progress undeniable."

---

### Phase 3: Discuss the Output (2 min)

**After generation, point out:**

**Structure:**
> "The monthly rollup follows a similar structure to weekly retros, but at a higher altitude. Same framework, different granularity."

**Context preservation:**
> "If Rob comes back in 3 months, this monthly summary tells him everything he needs to know about October. He doesn't need to re-read 4 weekly retros."

**Cognitive load:**
> "In Claude's context window, this is one document instead of four. That matters when you're months into a project."

---

## Key Demo Messages

### 1. Fractal Compression Pattern
```
4 Weekly Retros (~10 pages)
        ↓
1 Monthly Rollup (~3 pages)
        ↓
Preserved: Themes, milestones, learnings
Compressed: Daily details, individual metrics
```

### 2. Same Framework, Different Altitude
- Weekly retro: What worked this week?
- Monthly retro: What worked this month?
- Same structure, same thinking, different timescale

### 3. History Without Overwhelm
- Old data compresses
- Recent data stays detailed
- Context grows without drowning in details

### 4. Pattern Recognition
- Week-by-week: hard to see trends
- Month view: trajectory is obvious
- "I couldn't run 1 minute → I ran 10 minutes"

---

## The Narrative Arc

**What the audience should see in the monthly rollup:**

**Physical journey:**
- Week 1: Everything hurt, 1-minute runs
- Week 2: New shoes, consistency tested
- Week 3: 3-minute breakthrough
- Week 4: 10-minute milestone, 4 lbs lost

**Mental journey:**
- Week 1: "Can I do this?"
- Week 2: "Will I show up?"
- Week 3: "I AM doing this"
- Week 4: "I might actually finish"

**System journey:**
- Experiments → learnings → adjustments
- Problems (shin pain) → solutions (new shoes)
- Inconsistencies (hydration) → systems (water bottle)

---

## Troubleshooting

**If monthly retro doesn't find all weeks:**
- Check all 4 weekly retros are uploaded
- Verify filenames match expected pattern

**If output is too brief:**
- May need to prompt for more detail
- "Can you expand on the physical transformation section?"

**If skill doesn't trigger:**
- Try explicit: "Run the retrospective-base skill for October"
- Check skill is enabled in settings

---

## Transition Points

**From Scenario 2:**
> "In Scenario 2, we saw Rob's first weekly retro. Now imagine doing that 4 times - that's a lot of data. The monthly rollup compresses it into something manageable."

**To Scenario 4:**
> "After the monthly rollup, Rob continues for another month. Scenario 4 shows what the system looks like at Week 9 - with a full history of compressed + recent data."

---

## Why This Matters

**For long-term use:**
> "Imagine using this system for a year. That's 52 weekly retros. Without compression, that's overwhelming. With monthly rollups, it's 12 documents plus current detail. Manageable."

**For continuity:**
> "When Claude's context refreshes (new conversation), you don't lose everything. The monthly rollup IS the memory."

**For reflection:**
> "You can't see your own progress day-to-day. But month-over-month? The transformation is undeniable."
