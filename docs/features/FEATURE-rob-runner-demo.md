# F28: Rob the Runner Demo Persona

**Status:** Complete - Demo content created
**Effort:** ~3 hours (actual)
**Priority:** High (Dec 12th presentation)
**Created:** 2025-12-01
**Completed:** 2025-12-02

## Goal

Create demonstration persona showing couch-to-5K training journey (8 weeks) with daily→weekly fractal compression.

## Persona Background

**Name:** Rob the Runner

**Starting Point:** Sedentary office worker, no recent exercise history

**Goal:** Complete a 5K run using a structured 8-week couch-to-5K program

**Motivation:** TBD (health scare? upcoming charity run? fitness goal for milestone birthday?)

**Key Challenges:**
- Building consistency habit
- Managing recovery and avoiding injury
- Balancing training with work schedule
- Tracking progressive overload

## Deliverables

### Sample Documents

**Recent (Week 8 - Granular):**
- [x] `Summary-2025-11-25-Monday-W8-D1.md` - Final week begins
- [x] `Summary-2025-11-27-Wednesday-W8-D2.md` - Mid-week run
- [x] `Summary-2025-11-29-Friday-W8-D3.md` - Week 8 complete

**Mid-range (Weeks 5-7 - Weekly Compression):**
- [x] `Weekly-Retro-2025-11-04-to-10-W5.md` - Midpoint check-in
- [x] `Weekly-Retro-2025-11-11-to-17-W6.md` - Increasing endurance
- [x] `Weekly-Retro-2025-11-18-to-24-W7.md` - Peak training week

**Historical (Weeks 1-4 - Monthly Compression):**
- [x] `Monthly-Rollup-2025-10-October.md` - October summary (Weeks 1-4)
- Shows highest compression: 28 days → 1 document

**Post-Program (Week 9 - Ongoing Practice):**
- [x] `Weekly-Plan-2025-12-01-to-07-W9.md` - Post-program exploration planning
- [x] `Summary-2025-12-01-Monday-W9-D1.md` - First day post-program (maintenance run + yoga exploration)
- [x] `Summary-2025-12-03-Wednesday-W9-D2.md` - First yoga session with wife
- Shows ongoing practice (not just goal completion)

### Personal Skills

**N/A** - Rob uses **base skills only** (no custom personal skills)
- This is the key demo value: shows system works without customization
- Lower barrier to entry for new users

### Project Setup

- [x] `README.md` in `examples/rob-the-runner/` - Rob persona documentation and base-skills-only explanation
- Project-Goals.md and protocol docs deferred (minimal demo scope)

## Data Scope

**Timeline:** 8 weeks (Oct 7 - Nov 29, 2025)
- Week 1-2: Walk/jog intervals, building base
- Week 3-4: Increasing run duration
- Week 5-6: Sustained running segments
- Week 7-8: Approaching 5K distance

**Key Metrics to Track:**
- **Distance:** Miles/km per run
- **Pace:** Minutes per mile/km
- **Heart Rate:** Zones 2-4, recovery metrics
- **Sleep:** Hours, quality (HRV if available)
- **Energy:** Pre-run and post-run energy levels
- **Pain/Recovery:** Soreness, injury prevention notes

**Context Tags:** W#-D# format (W8-D1 = Week 8, Day 1)

## Sample Data Structure

### Daily Summary Example (Week 8, Day 1)

```markdown
# Summary-2025-11-25-Monday-W8-D1

## Key Numbers
- Distance: 2.8 miles (target 3.0)
- Pace: 11:45 min/mi (comfortable)
- HR avg: 152 bpm (Zone 3)
- Sleep: 7.5 hours
- Energy: 7/10 pre-run, 8/10 post-run

## Timeline
- 6:30 AM: Morning routine, light breakfast
- 7:15 AM: Warmup (dynamic stretches, 5 min walk)
- 7:20 AM: Run - felt strong first 2 miles, slight fatigue last 0.8
- 8:00 AM: Cooldown, stretching
- 9:00 AM: Work day begins

## What Worked
- Earlier start time (less rushed)
- New route with shade (cooler temps)
- Fueling strategy: banana + water 30 min before

## What Didn't Work
- Forgot to hydrate last night → slight headache mid-run
- Pushed pace too fast in mile 2 → paid for it in mile 3

## Insights
- Week 8 confidence is real - body adapting
- Need to trust the program, resist urge to go faster
- Recovery still matters even when feeling strong

## Tomorrow's Focus
- Hydrate tonight (set reminder)
- Rest day protocols: foam rolling, gentle walk
- Prep gear for Wednesday run
```

### Weekly Retro Example (Week 5)

```markdown
# Weekly-Retro-2025-11-04-to-10-W5

## What Worked This Week
- Hit all 3 scheduled runs (M/W/F consistency building)
- Increased continuous run time to 15 minutes (up from 10 min in W4)
- New running shoes resolved shin splint concern
- Sleep average: 7.8 hours (up from 7.2)

## What Didn't Work This Week
- Wednesday run cut short (work emergency) - only 20 min instead of 30
- Still struggling with pre-run fueling timing
- Skipped Friday stretching routine (paid for it Saturday)

## Progress Toward Goal
- Midpoint of program reached (Week 5 of 8)
- Current continuous run: 15 minutes
- Target by Week 8: 30 minutes (5K distance)
- On track, building endurance steadily

## Experiments to Try Next Week
- Test pre-run fueling: 45 min before vs 30 min before
- Add one yoga session (recovery-focused)
- Try interval music playlist (faster tempo for run segments)

## Gratitude
- Body is adapting - no major injuries yet
- Consistent sleep routine supporting recovery
- Program structure removes decision fatigue
```

## Success Criteria

**Demo persona complete when:**
- [x] All sample documents created and realistic
- [x] **No personal skills needed** (base skills only - key demo value)
- [x] Dates align with presentation timeline (Week 8 = late Nov, Week 9 = early Dec 2025)
- [x] Data shows clear daily→weekly→monthly compression pattern
- [x] Metrics demonstrate progressive overload (realistic progression)
- [x] Narrative is compelling and relatable (39yo accountant, kids, gained weight)
- [x] **Week 9 shows ongoing practice** (not just goal completion)

**Presentation value:**
- [x] Shows fractal compression (daily → weekly → monthly rollup)
- [x] Demonstrates **base skills work without customization** (lower barrier)
- [x] Relatable for non-technical audience (fitness, not tech domain)
- [x] Clear progress narrative (sedentary → 5K in 8 weeks)
- [x] **Ongoing practice** (Week 9 exploration: yoga, maintenance, "what's next?")

## Decisions Made

**Q1: What specific motivation drives Rob?**
- **Decision:** Turning 39 (approaching 40), gained weight, random aches/pains, winded playing with kids
- Relatable, emotionally resonant, not catastrophic but real
- But: Made Rob an accountant (not too projectable onto author)

**Q2: Should we include a monthly rollup for Rob?**
- **Decision:** YES - `Monthly-Rollup-2025-10-October.md` covering Weeks 1-4
- Demonstrates full fractal compression hierarchy (daily → weekly → monthly)

**Q3: How much protocol detail?**
- **Decision:** Medium detail embedded in summaries, no separate protocol docs
- Kept demo scope minimal (documents only, no custom skills)

**Q4: Should Rob's data reference real couch-to-5K programs?**
- **Decision:** Loosely aligned with popular structure, not prescriptive
- Realistic progression without being tied to specific program

## Timeline

**COMPLETED: Dec 2nd, 2025**
- [x] Created 3 daily summaries (Week 8: Mon/Wed/Fri)
- [x] Created 3 weekly retros (Weeks 5-7)
- [x] Created 1 monthly rollup (October, Weeks 1-4)
- [x] Created README.md documenting Rob persona and base-skills-only approach
- [x] Updated documentation (README.md, CLAUDE.md, PROJECT-SETUP.md)
- [x] Scope decision: Rob uses **base skills only** (no custom personal skills)

**NEXT STEPS (before Dec 12th presentation):**
- [ ] Test Rob's documents with base skills in Claude.ai Project
- [ ] Validate fractal compression demonstration works as intended
- [ ] Prepare demo walkthrough using Rob's documents

## Notes

**Fractal compression demonstration (AS IMPLEMENTED):**
- Recent data (Week 8): 3 individual daily summaries showing granular detail
- Mid-range data (Weeks 5-7): 3 weekly retros compressing 21 days into 3 documents
- Historical data (Weeks 1-4): **Monthly rollup** compressing 28 days into 1 document

**Make-change algorithm visualization:**
- Most highly compressed: Weeks 1-4 → 1 monthly rollup (28 days → 1 doc)
- Medium compression: Weeks 5-7 → 3 weekly retros (21 days → 3 docs)
- Most granular: Week 8 → 3 daily summaries (3 days → 3 docs)
- Demonstrates: system maintains detail where it matters most (recent), compresses historical data

**Key implementation decision:**
- Created **full monthly rollup** for October (not just narrative references)
- This shows the complete compression hierarchy: daily → weekly → monthly

**Design principle:**
- Rob's journey should be inspiring but realistic
- Show struggles and setbacks, not just wins
- Emphasize system's value: continuity, learning, adaptation
