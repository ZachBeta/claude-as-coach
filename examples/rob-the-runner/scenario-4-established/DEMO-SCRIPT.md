# Demo Script - Scenario 4: Established User

**Duration:** ~20 minutes
**Purpose:** Show full established workflow - morning routine → daily log → summary → weekly retro → weekly planning

---

## BEFORE DEMO: Regenerate Dates (1 minute)

```bash
# Regenerate Scenario 4 documents for your demo day
python scripts/regenerate_demo_dates.py --scenario 4 --demo-day 2025-12-12

# Dry-run to preview
python scripts/regenerate_demo_dates.py --scenario 4 --demo-day 2025-12-12 --dry-run
```

**Output:** Generated files go to `scenario-4-established/documents-generated/`

**How it works:**
- Templates live in `scenario-4-established/templates/`
- Demo day anchors Rob's timeline: W9 = demo week, W8 = last week, etc.
- Week numbers stay fixed (W5-W9 have narrative meaning)
- Only dates change based on demo day

---

## PREP (Before Demo - 2 minutes)

### 1. Create Claude Project
- Name: "Rob Demo - Established User"
- Model: Sonnet 4.5 or Opus 4.5

### 2. Upload Skills (4 files from `skills/`)
```
skills/daily-summary-base.zip
skills/daily-morning-routine-base.zip
skills/retrospective-base.zip
skills/planning-base.zip
```

### 3. Upload Rob's Documents (11 files from `scenario-4-established/documents-generated/`)

**Historical (compressed):**
- Monthly-Rollup-YYYY-MonthName.md (Weeks 1-4)

**Recent weeks:**
- Weekly-Retro-*-W5.md
- Weekly-Retro-*-W6.md
- Weekly-Retro-*-W7.md

**Last week (Week 8 = final program week):**
- Summary-*-W8-D1.md
- Summary-*-W8-D2.md
- Summary-*-W8-D3.md

**Current week (Week 9 = post-program):**
- Summary-*-W9-D1.md
- Summary-*-W9-D2.md
- Summary-*-W9-D5.md (yesterday)
- Weekly-Plan-*-W9.md

---

## DEMO FLOW (18 minutes)

### Phase 1: Morning Routine (3 min)

**User says:**
```
good morning
```

**Expected:** Skill triggers, verifies date, finds yesterday's summary (W9-D5), generates morning brief.

**Demo notes:**
- Shows: "Detail-first, TL;DR at bottom" format
- Emphasizes: Low cognitive load during morning wakeup
- Rob's context: Week 9 complete, steady running + yoga pattern

---

### Phase 2: Daily Conversation (5 min)

**Scenario:** Rob's Saturday - morning run, afternoon yoga session

**Paste snippets one at a time:**

#### Snippet 1: Morning (9 AM)
```
Just finished my Saturday run. Went 4 miles instead of 3 - felt good so I kept going.
Pace was around 10:45/mi, which is faster than my usual easy pace but still comfortable.
Week 9 is done. I actually did it - completed the couch-to-5K program and kept going for
another week. Feels... anticlimactic? But also good?
```

#### Snippet 2: Afternoon (2 PM)
```
Wife and I just finished a 45-minute yoga flow. This was our longest session yet.
I'm still terrible at it, but I made it through without giving up. She's talking about
maybe doing yoga teacher training in the spring - she's been practicing for years and
I think she'd be great at it. For me? I'm just trying not to fall over during tree pose.
```

#### Snippet 3: Evening (7 PM)
```
Dinner conversation: talked about what's next. I don't feel pressure to jump into another
program immediately. Running 3x/week + yoga 3x/week feels sustainable. Maybe target a 10K
in spring (April?), but for now I just want to keep the pattern going. First time in years
I've stuck with something this long. That's the real win.
```

**Between snippets:** Claude should react naturally, ask clarifying questions, notice patterns.

---

### Phase 3: Daily Summary (4 min)

**User says:**
```
daily summary
```

**Expected flow:**
1. Skill verifies date
2. Asks which date → "today"
3. Confirms date → "yes"
4. Asks context tag → "W9-D6"
5. Generates structured summary
6. Saves to: `Summary-YYYY-MM-DD-Saturday-W9-D6.md`

**Demo notes:**
- Shows: Structured markdown format
- Emphasizes: Filename convention (date OF events)
- Context tag: W9-D6 = Week 9, Day 6

---

### Phase 4: Weekly Retrospective (4 min)

**User says:**
```
Let's do the weekly retro for Week 9
```

**Expected flow:**
1. Establishes week boundaries
2. Confirms week: "Reviewing Week 9. Correct?"
3. Loads Week 9 context (summaries + plan)
4. Generates retrospective with:
   - What Worked (Roses)
   - What Didn't Work (Thorns)
   - Week-over-Week Comparison
   - Monthly Progress Check
   - Retro-Retro
   - Gratitude

**Demo notes:**
- Shows: First post-program week
- Emphasizes: "What worked" = running 3x + yoga 3x became normal
- Pattern: Sustainable habits, no pressure for next goal

---

### Phase 5: Weekly Planning (2 min)

**User says:**
```
Let's plan Week 10
```

**Expected flow:**
1. Establishes next week boundaries
2. Confirms: "Planning Week 10. Correct?"
3. Asks about constraints → "Nothing major - normal work week"
4. Generates plan with:
   - Coming From (Week 9 patterns)
   - Priorities (2-3 max)
   - Experiments
   - Success Levels (L0-L3)

**Demo notes:**
- Shows: Planning from current capacity
- Emphasizes: 2-3 priorities max, constraints first
- Rob's state: Maintenance mode, exploring 10K casually

---

## KEY DEMO MESSAGES

1. **Full workflow in action**
   - All 4 skills working together
   - Morning → conversation → summary → retro → planning

2. **Rich historical context**
   - Monthly rollup (Weeks 1-4 compressed)
   - Weekly retros (Weeks 5-7)
   - Recent detail (Week 8-9)
   - System scales over time

3. **Established practice**
   - Week 9 = first "free" week post-program
   - Habits stuck: 3x run + 3x yoga
   - "What's next?" exploration phase

4. **Base skills are sufficient**
   - No custom personal skills
   - Framework provides everything needed
   - Lower barrier to entry

---

## BACKUP: If Time Short

**Skip daily conversation phase**, go directly:
1. Morning routine (load W9-D5 summary)
2. Weekly retro (Week 9)
3. Weekly planning (Week 10)

Still shows 3 skills and the retro→planning workflow.

---

## TROUBLESHOOTING

**If morning routine doesn't find Friday summary:**
- Verify W9-D5 file was uploaded
- Check filename matches expected pattern

**If skills don't trigger:**
- Check skills enabled in Settings > Capabilities
- Try explicit: "run the daily-summary-base skill"

**If date verification fails:**
- Claude shows current date
- Explain demo uses specific date for Week 9 context

---

## TRANSITION POINTS

**From Scenario 3:**
> "In Scenario 3, we saw the monthly rollup for October. Now we're in Week 9 - Rob has that compressed history PLUS recent detail. This is what the system looks like after sustained use."

**Compare to earlier scenarios:**
> "Scenario 1 showed getting started. Scenario 2 showed the first weekly cycle. Scenario 3 showed monthly compression. This scenario shows all of it working together over time."

---

## POST-DEMO TALKING POINTS

**Why this scenario matters:**
- Shows system scales over time
- Rich context without drowning in detail
- Ongoing practice beyond initial goal
- "What's next?" exploration phase

**The full data structure:**
- 1 monthly rollup (Weeks 1-4)
- 3 weekly retros (Weeks 5-7)
- 6 daily summaries (Weeks 8-9)
- 1 weekly plan (current)
- = Complete 9-week journey in ~11 documents

**Compare to Alice (if asked):**
- Alice = custom personal skills (power user)
- Rob = base skills only (new user)
- Both valid, different levels of customization
