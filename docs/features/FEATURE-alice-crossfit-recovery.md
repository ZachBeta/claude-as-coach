# F29: Alice the Athlete - CrossFit Recovery Persona

**Status:** Planned (deferred post-Dec 12 presentation)
**Effort:** TBD (~6-8 hours for complete persona replacement)
**Priority:** Medium (post-presentation enhancement)
**Created:** 2025-12-02

## Goal

Evolve Alice from "couch-to-5K beginner" to "CrossFit athlete recovering from injury." This creates a more advanced, technically interesting demo persona showing injury recovery tracking, modified training protocols, and gym vs. home workout balance.

## Persona Background

**Name:** Alice
**Current:** Couch-to-5K beginner runner
**Future:** Cross Fit athlete recovering from torn labrum surgery

**New Profile:**
- CrossFit athlete (2-3 years experience before injury)
- Torn labrum (shoulder) requiring surgery
- 3 months post-surgery, cleared for modified training
- Limited access to CrossFit gym (can only go 2x/week, community gym)
- Needs to track home training + gym sessions
- Goal: Return to full CrossFit capacity without re-injury

**Key Challenges:**
- Following PT protocols (range of motion, pain monitoring)
- Modified CrossFit workouts (scaling movements for shoulder)
- Home training substitutions (limited equipment)
- Balancing gym vs. home training
- Progressive overload without overloading injured shoulder
- Psychological: fear of re-injury, frustration with limitations

## Deliverables

### Sample Documents

**Daily Summaries (mixed gym/home):**
- [ ] Day at community gym (modified CrossFit WOD)
- [ ] Home training day (bodyweight + bands)
- [ ] PT appointment day (ROM testing, exercises)
- [ ] Rest/recovery day (active recovery, mobility work)

**Weekly Retros:**
- [ ] Week showing gym + home balance
- [ ] What's working / not working with modifications
- [ ] Pain/ROM tracking week-over-week
- [ ] Experiments (new movements to try, scaling options)

**Weekly Plans:**
- [ ] Planning gym days vs. home days
- [ ] Movement selection based on shoulder status
- [ ] Success levels calibrated to recovery (not performance)

**Protocol Documents:**
- [ ] PT exercise routine (ROM, strength progression)
- [ ] Modified CrossFit movements list (safe/avoid)
- [ ] Pain monitoring protocol (when to back off)
- [ ] Home equipment inventory (what's available)

### Personal Skills

**alice-crossfit-recovery-personal.skill:**
- Metrics: ROM (range of motion), pain levels (0-10 scale), movement quality
- CrossFit terminology: WOD, AMRAP, EMOM, scaling, RX vs scaled
- Movements: categorized by shoulder load (safe, modified, avoid)
- Home vs. gym context tags
- PT protocol integration

## Data Scope

**Timeline:** 3-6 months post-surgery

**Key Metrics to Track:**
- **Pain:** 0-10 scale, location, timing (during/after workout)
- **ROM:** Shoulder flexion, abduction, external rotation (degrees or descriptive)
- **Strength:** Overhead press capacity, pull-up progression, push-up variations
- **Movement quality:** Clean execution vs compensating
- **Workout volume:** Total time, intensity, movements performed
- **Gym vs Home:** Frequency, effectiveness, preference
- **Psychological:** Confidence, fear, frustration levels

**Context Tags:**
- Gym-Day vs Home-Day
- PT-Week-# (tracking PT progression)
- Modified/Scaled/RX (movement intensity)

## Sample Data Examples

### Daily Summary (Gym Day)

```markdown
# Summary-2025-XX-XX-Wednesday-PT-W12-Gym

## Key Numbers
- **Pain:** 2/10 during, 3/10 2hrs post (acceptable)
- **ROM check:** Overhead reach 85% (up from 80% last week)
- **Workout:** 30min AMRAP scaled
- **Movements:** Air squats (RX), Push-ups (scaled to box), Pull-ups (scaled to ring rows)
- **Gym access:** 2x this week (Wed/Sat planned)

## What Worked
- Ring rows felt strong (no shoulder pain)
- Box push-ups maintained good form
- Gym environment motivating (missed this)

## What Didn't Work
- Tried regular push-up (mistake - pain spike to 6/10)
- Backed off immediately, reverted to box
- Reminder: don't rush progressions

## Insights
- PT said 85% ROM = cleared for light overhead work next week
- But my confidence isn't there yet (mental barrier)
- Need to trust the process, not just the clearance
```

### Daily Summary (Home Day)

```markdown
# Summary-2025-XX-XX-Monday-PT-W12-Home

## Key Numbers
- **Pain:** 1/10 (minimal, just awareness)
- **ROM:** Didn't formal test (feels good)
- **Workout:** 20min PT exercises + 15min bodyweight circuit
- **Equipment:** Resistance bands, yoga mat, pull-up bar (doorway)

## What Worked
- PT exercises feeling routine (not tedious anymore)
- Bodyweight squats, lunges, planks all pain-free
- Home training saves commute time (gym is 25min each way)

## What Didn't Work
- Limited by equipment (can't replicate gym intensity)
- Motivation lower at home (distractions, less energy)
- Missing community aspect of CrossFit gym

## Insights
- Home training works for maintenance, not progression
- Need gym for intensity + accountability
- But gym only 2x/week = home training necessary for consistency
- This is the balance for now
```

## Success Criteria

**Persona complete when:**
- [ ] All sample documents created and realistic
- [ ] Personal skills define CrossFit/PT metrics and protocols
- [ ] Injury recovery narrative is compelling and educational
- [ ] Shows gym vs. home training balance clearly
- [ ] Demonstrates modified movement tracking
- [ ] Pain/ROM progression visible across documents

**Presentation value:**
- Shows system handles injury recovery (health tracking use case)
- Demonstrates custom metrics for specialized domain (CrossFit)
- Gym vs. home context switching (location-dependent protocols)
- More advanced than Rob/current-Alice (shows extensibility)

## Open Questions

**Q1: How technical should CrossFit terminology be?**
- Target audience: general fitness (not just CrossFitters)?
- Or: assume some CrossFit knowledge?

**Q2: Should Alice have multiple injuries/complications?**
- Single injury (labrum) = cleaner narrative
- Multiple issues = more realistic but complex

**Q3: Home equipment inventory?**
- Minimal (bands, mat, doorway bar)?
- Or moderate (dumbbells, kettlebell, rings)?

**Q4: Timeline positioning?**
- Show early recovery (Weeks 1-4 post-surgery)?
- Or mid-recovery (Weeks 8-12, more capable)?
- Or late recovery (Weeks 16-20, approaching full capacity)?

## Dependencies

- **FEATURE-rob-runner-demo:** Complete (Rob is primary base-skills demo)
- **Dec 12 presentation:** Alice changes deferred until after

## Timeline

**Post-Dec 12 (Q1 2026):**
- Decide: Replace current Alice or create new persona?
- Design injury recovery progression arc
- Create sample documents (4-6 days across 2-3 weeks)
- Build custom skills for CrossFit/PT tracking
- Test with real CrossFit athletes for authenticity

## Notes

**Why CrossFit recovery vs. couch-to-5K?**
- Current Alice overlaps too much with Rob (both beginner runners)
- CrossFit recovery shows:
  - Advanced athlete use case (not just beginners)
  - Injury tracking (health management, not just performance)
  - Complex movement selection (modified/scaled protocols)
  - Home vs. gym context (location-dependent training)
  - More interesting technically and narratively

**Authenticity concerns:**
- Labrum tears are common in CrossFit (shoulder-intensive sport)
- Recovery timeline: 6-12 months to full capacity
- Need input from actual CrossFit athletes + PT professionals
- Risk: getting medical details wrong → misleading users

**Alternative: Keep both Alices?**
- alice-the-beginner-runner/ (current, couch-to-5K)
- alice-the-crossfit-athlete/ (new, recovery)
- Shows same person, different phases of fitness journey?
- Or just different fictional people who happen to share a name?

---

**Status:** Planned for post-presentation development. Current Alice (couch-to-5K) remains as custom skills example for Dec 12 presentation.
