# Rob Demo Script (20 minutes)

**Demo Date:** Saturday, December 7, 2025
**Scenario:** Rob finishing Week 9, preparing for Week 10
**Shows:** Full skill workflow - morning routine → daily log → summary → weekly retro → weekly planning

---

## PREP (Before Demo - 2 minutes)

### 1. Create Claude Project
- Name: "Rob Demo - Couch to 5K"
- Model: Sonnet 4.5 or Opus 4.5

### 2. Upload Skills (4 files from `skills/`)
```
skills/daily-summary-base.zip
skills/daily-morning-routine-base.zip
skills/weekly-retrospective-base.zip
skills/weekly-planning-base.zip
```

### 3. Upload Rob's Documents (10 files from `examples/rob-the-runner/documents/`)
**Upload all files:**
- Monthly-Rollup-2025-10-October.md
- Weekly-Retro-2025-11-04-to-10-W5.md
- Weekly-Retro-2025-11-11-to-17-W6.md
- Weekly-Retro-2025-11-18-to-24-W7.md
- Summary-2025-11-25-Monday-W8-D1.md
- Summary-2025-11-27-Wednesday-W8-D2.md
- Summary-2025-11-29-Friday-W8-D3.md
- Summary-2025-12-01-Monday-W9-D1.md
- Summary-2025-12-03-Wednesday-W9-D2.md
- Weekly-Plan-2025-12-01-to-07-W9.md

### 4. Create ONE prep summary (paste into chat, save to project)

<details>
<summary>📄 Summary-2025-12-06-Friday-W9-D5.md (PREP FILE - paste this)</summary>

```markdown
# Summary-2025-12-06-Friday-W9-D5

**Date:** Friday, December 6, 2025
**Context:** Week 9, Day 5 - End of first post-program week

## TL;DR

Wrapped up Week 9 with an easy 3-mile run. Felt like a "bridge week" - not training for anything specific, but maintaining momentum. Did yoga with wife after work (3rd session this week). Getting slightly less terrible at it. Weekend plans: Saturday morning run, then maybe a longer yoga flow? Program's done, but the habits are sticking.

## Key Numbers

**Running:**
- Distance: 3.0 miles
- Duration: ~33 minutes
- Pace: ~11:00 min/mi (comfortable)
- Heart rate avg: ~150 bpm
- Consistent all week

**Yoga:**
- Session: 25 minutes (beginner-intermediate)
- Difficulty: 7/10 (slight improvement)
- Wife's patience: ∞/10 (she's a saint)

**General:**
- Weight: 190 lbs (down 1 lb this week!)
- Sleep: 7 hours
- Energy: 8/10

## Timeline

**6:30 AM** - Morning run
- Same comfortable 3-mile route
- Body feels good - no aches
- Mind wandering: "What do I train for next?"
- Not urgent, just curious

**9:00 AM - 5:30 PM** - Work
- Friday = less intense, admin tasks
- Quarterly reports finalized (done!)

**6:00 PM** - Yoga with wife
- 25-minute flow
- First time attempting crow pose (failed hilariously)
- Wife demonstrated, I fell over
- We both laughed - that's the point?

**8:00 PM** - Dinner conversation
- Talked about "what's next" for fitness
- No pressure to decide now
- Maybe a 10K in spring?
- Maybe yoga teacher training for her?
- For now: just keep moving

## Insights

**Pattern recognition:** Week 9 felt like a "breath" after the intensity of Week 8. The couch-to-5K program structure is gone, but the habits remain. Running 3 days/week feels normal now. Yoga 2-3x/week is becoming normal too.

**The yoga surprise:** I thought yoga would be "easy" compared to running. It's not. Different hard. Balance is humbling. But there's something about struggling through a pose with my wife that feels... connective? Not just fitness, but time together.

**Energy observation:** No big energy swings this week. Steady 7-8/10 most days. Sleep consistent. Weight trending down (finally broke 191). This is what "sustainable" feels like?

## Decisions & Next

**For tomorrow (Saturday):**
- Morning run: 3-4 miles, easy pace
- Afternoon: Try a longer yoga flow (45 min) with wife

**For Week 10:**
- Continue run 3x/week pattern (Mon/Wed/Fri or Sat)
- Yoga 3x/week pattern (Tues/Thurs/weekend)
- No new experiments - let this week's pattern settle
- Maybe start thinking about a 10K goal for spring?

**No big decisions needed.** Just keep going.
```
</details>

**Save to project** after pasting.

---

## DEMO FLOW (18 minutes)

### Phase 1: Morning Routine (3 min)

**User says:**
```
good morning
```

**Expected:** Skill triggers, verifies date (Saturday Dec 7), finds yesterday's summary (Friday Dec 6), generates morning brief.

**Demo notes:**
- Shows: "Detail-first, TL;DR at bottom" format
- Emphasizes: Low cognitive load during morning wakeup
- Rob's context: Week 9 complete, steady running + yoga pattern

---

### Phase 2: Daily Conversation (5 min)

**Scenario:** Rob's Saturday - morning run, afternoon yoga session

**User pastes conversation snippets** (paste these one at a time, react naturally):

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
1. Skill verifies date (Saturday, December 7, 2025)
2. Asks: "Which date's summary are we generating?" → User: "today"
3. Confirms: "Generating summary for Saturday, December 7, 2025. Correct?" → User: "yes"
4. Asks: "What's the context tag for this day?" → User: "W9-D6"
5. Generates structured summary with sections (see base skill format)
6. Saves to: `Summary-2025-12-07-Saturday-W9-D6.md`

**Demo notes:**
- Shows: Structured markdown format
- Emphasizes: Filename convention (date OF events, not FOR next day)
- Context tag: W9-D6 = Week 9, Day 6

**After saving:** Explain that this would normally go to project knowledge.

---

### Phase 4: Weekly Retrospective (4 min)

**User says:**
```
Let's do the weekly retro for Week 9
```

**Expected flow:**
1. Skill establishes week boundaries: December 1-7, 2025
2. Confirms: "Reviewing week: December 1-7, 2025 (Week 9). Correct?"
3. Loads Rob's Week 9 context:
   - Summary-2025-12-01-Monday-W9-D1.md
   - Summary-2025-12-03-Wednesday-W9-D2.md
   - Summary-2025-12-06-Friday-W9-D5.md
   - Summary-2025-12-07-Saturday-W9-D6.md (just created)
   - Weekly-Plan-2025-12-01-to-07-W9.md
4. Generates empty framework with 6 sections:
   - What Worked (Roses)
   - What Didn't Work (Thorns)
   - Week-over-Week Comparison
   - Monthly Progress Check
   - Retro-Retro
   - Gratitude
5. Fills conversationally through observations → reactions
6. Saves to: `Weekly-Retro-2025-12-01-to-07-W9.md`

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
1. Skill establishes week boundaries: December 8-14, 2025
2. Confirms: "Planning week: December 8-14, 2025 (Week 10). Correct?"
3. Asks about constraints: "What's non-negotiable this week that I should plan around?"
   - User: "Nothing major - normal work week"
4. Generates plan with sections:
   - **Coming From:** Week 9 patterns (run 3x, yoga 3x, sustainable)
   - **Priorities:** 2-3 max (maintain pattern, no new experiments)
   - **Experiments:** Maybe explore 10K possibility? Not urgent.
   - **Success Levels:**
     - L0 (Minimum): Run 3x, yoga 3x
     - L1 (Target): Same + research 10K options
     - L2 (Stretch): Same + pick a target race
     - L3 (Exceptional): Register for race + training plan
5. Saves to: `Weekly-Plan-2025-12-08-to-14-W10.md`

**Demo notes:**
- Shows: Planning from current capacity (not aspirational)
- Emphasizes: 2-3 priorities max, constraints first
- Rob's state: Maintenance mode, exploring next goal casually

---

## KEY DEMO MESSAGES

1. **Base skills work without customization**
   - Rob uses ONLY base skills
   - No personal extensions needed
   - Lower barrier to entry

2. **Fractal compression in action**
   - Daily summaries feed weekly retro
   - Weekly retros feed monthly rollup
   - Keeps context lean while preserving history

3. **Skills guide but don't dictate**
   - Observation → reaction flow
   - User stays in control
   - Claude structures, user decides

4. **Sustainable habits over perfection**
   - Week 9 = first "free" week without program
   - Pattern stuck: 3x run + 3x yoga
   - No pressure for next goal immediately

---

## BACKUP: If Time Short

**Skip daily conversation phase**, go directly:
1. Morning routine (load prep summary)
2. Weekly retro (Week 9)
3. Weekly planning (Week 10)

This still shows 3 skills and the retro→planning workflow.

---

## TROUBLESHOOTING

**If morning routine doesn't find Friday summary:**
- Verify prep file was saved to project
- Check filename matches: `Summary-2025-12-06-Friday-W9-D5.md`

**If skills don't trigger:**
- Check skills are enabled in Settings > Capabilities
- Try explicit: "run the daily-summary-base skill"

**If date verification fails:**
- Claude will show current date
- Explain: Demo uses Dec 7 as "today" for Week 9 completion

---

## POST-DEMO TALKING POINTS

**Why Rob matters:**
- Shows system works with zero customization
- Couch-to-5K = relatable health goal
- Fractal compression = recent detail + compressed history
- Ongoing practice = Week 9 shows "what's next?" exploration

**Compare to Alice (if asked):**
- Alice = custom personal skills (advanced user)
- Rob = base skills only (new user)
- Both valid approaches

**Next steps for adopters:**
1. Clone repo
2. Import 4 base skills (5 min)
3. Start using (day 1)
4. Optionally create personal extensions later
