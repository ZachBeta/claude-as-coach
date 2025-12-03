# Monthly Rollup Process Design

**Created:** 2025-11-30
**Status:** Design phase - awaiting validation via November 2025 manual rollup
**Purpose:** Define fractal rollup process (daily → weekly → monthly) for claude-as-coach skills system

---

## Current State

### Existing Skills
- `daily-summary` - End-of-day summary creation
- `daily-morning-routine` - Morning context loading from previous summary
- `weekly-retrospective` - Weekly pattern recognition from dailies
- `weekly-planning` - Weekly planning from retros
- `backfill-summary` - Backfilling missed days
- `context-continuation` - Mid-day context handoff

### Gap Identified
- **No monthly-retrospective skill** - First month-end (Nov 30) happened inside weekly retro (ad-hoc)
- **No formal plan-vs-actual comparison** - Retros stand alone, don't reference plans
- **No documented archival process** - When to archive dailies? weeklies? plans?
- **Plan documents accumulate** - Unclear if they have value after retro exists

---

## Proposed Fractal Pattern

### Compression Hierarchy

```
Daily Summaries (7 docs)
    ↓ compress into
Weekly Retro (1 doc)
    ↓ archive dailies locally

Weekly Retros (4-5 docs)
    ↓ compress into
Monthly Retro (1 doc)
    ↓ archive weeklies from project

Monthly Retros (3 docs)
    ↓ compress into
Quarterly Retro (1 doc)
    ↓ archive monthlies from project
```

**Result:** Project context stays lean, full history preserved locally, summary-of-summaries maintains continuity.

### Document Lifecycle

| Document Type | Created | Lives In Project | Archived After |
|---------------|---------|------------------|----------------|
| Daily Summary | End of day | Until weekly retro | Weekly retro exists |
| Weekly Plan | Sunday planning | During that week | Weekly retro exists |
| Weekly Retro | Sunday | Until monthly retro | Monthly retro exists |
| Monthly Retro | Month end | Until quarterly | Quarterly retro exists |

**Key principle:** Each rollup compresses the level below. The compression is trusted. History preserved locally, context stays lean, continuity maintained through summaries.

---

## Plan vs Actual Pattern

### Current Problem
- Plans exist during the week/month
- Retros capture what happened
- No explicit comparison between them
- Plan becomes redundant after retro, but not explicitly referenced

### Proposed Options

**Option A: Retro includes "vs Plan" section**
```markdown
## Plan vs Actual

**Planned priorities:**
1. [Priority from plan]
2. [Priority from plan]

**What actually happened:**
- [Actual outcome]
- [Variance and why]

**Learning:** [What this teaches about planning accuracy]
```

**Pros:** Thorough, explicit learning capture, validates planning accuracy
**Cons:** Adds overhead, may feel heavy

**Option B: Plan archived with brief annotation**
- Retro stays clean (focused on patterns, not comparison)
- Plan gets brief "outcome" annotation before archival
- Comparison lives in plan document, not retro

**Pros:** Keeps retro focused, lighter weight
**Cons:** Learning dispersed across documents, less visible

**Option C: Skip formal comparison**
- Plans are hypotheses, retros are data
- Implicit comparison happens in the writing
- No explicit comparison section

**Pros:** Leanest, lowest overhead
**Cons:** May miss explicit learning opportunities

**Decision needed:** Test Option A during November 2025 manual rollup to see if value exceeds overhead.

---

## Monthly Rollup Skill Design

### Trigger Phrases
- "monthly retro"
- "month retrospective"
- "end of month summary"
- Last Sunday of month during weekly retro

### Input Context
- All weekly retros from that month (4-5 docs)
- Monthly plan if one exists
- Previous monthly retro (for trajectory comparison)

### Output Structure (Proposed)

```markdown
# Monthly Retrospective: [Month Year]

**Month:** [Date range]
**Recovery Context:** [Month X of timeline]

---

## TL;DR - Month Summary
[3-5 bullet executive summary]

---

## Monthly Arc
[Narrative of how the month unfolded - week by week progression]

---

## What Worked (Patterns Across Weeks)
[Recurring wins, validated experiments, capacity patterns]

---

## What Didn't Work (Persistent Challenges)
[Recurring struggles, failed experiments, constraint discoveries]

---

## Key Metrics / Progress
[Measurable changes: capacity, habits, portfolio, health markers]

---

## Trajectory Assessment
**Last month:** [State]
**This month:** [State]
**Direction:** [Better / Stable / Worse]
**Evidence:** [What supports this assessment]

---

## Next Month Setup
[What this month's patterns suggest for next month's focus]
```

### Relationship to Weekly Skills
- Monthly skill follows same analytical framework as weekly
- Operates on weekly retros the way weekly operates on dailies
- Same "What Worked / What Didn't Work" structure scales up
- Consistent pattern across timescales (fractal design)

---

## Archival Workflow

### After Weekly Retro Created
1. Weekly retro saved to project
2. Daily summaries backed up locally (outside project)
3. Daily summaries removed from project
4. Weekly retro becomes compressed reference

### After Monthly Retro Created
1. Monthly retro saved to project
2. Weekly retros backed up locally
3. Weekly retros removed from project (keep most recent?)
4. Monthly retro becomes compressed reference
5. Weekly plans from that month also archived

### Trust the Compression Principle
- Don't re-read dailies before archiving (retro IS the compression)
- Don't re-read weeklies before monthly archive (monthly IS the compression)
- If something was important, it made it into the rollup
- If it didn't, it wasn't important enough to persist
- Compression is lossy **by design** - reduces cognitive load

---

## Open Questions for Validation

These questions will be answered through the November 2025 manual rollup:

1. **Plan comparison:** Worth formalizing (Option A) or let it be implicit (Option C)?
2. **Archive timing:** Immediately after rollup, or batch at month end?
3. **What to keep in project:** Most recent week's retro + monthly? Or just monthly?
4. **Cross-month context:** How much of previous month needed for trajectory assessment?
5. **Quarterly rollup:** Same pattern, or different structure (fewer data points)?

---

## Implementation Phases

### Phase 1: Manual November Rollup (December 1-6, 2025)
- Test proposed output structure with real November data
- Answer the 5 open questions empirically
- Create `personal/documents/Retro-2025-11-November.md`
- Create sanitized example for presentation
- Document what worked and what needs adjustment

**Available data for November:**
- Weekly Retros: Week 3, 4, 5, 6 (Nov 3-30)
- Weekly Plans: Week 5, 6, 7
- Monthly Plan: November-2025-Plan.md
- Reference docs: Food-Experimentation-Protocol.md, LC-Symptom-Tracking.md
- Synthesis: Physician-Summary-Draft-2025-11.md

### Phase 2: Skill Development (Post-validation)
- Create `monthly-retrospective` skill based on validated structure
- Decide: Separate skill, parameterized retro skill, or manual-only?
- Implement chosen design
- Test with December 2025 (second iteration)

### Phase 3: Archival Documentation
- Document archival workflow in WORKFLOW-GUIDE.md
- Add reminders to weekly-retro skill about archiving dailies
- Add reminders to monthly-retro skill about archiving weeklies
- Update document lifecycle table

### Phase 4: Plan Integration (Optional)
- Decide on plan-vs-actual approach (A, B, or C) based on November test
- Update weekly-planning and weekly-retro skills accordingly
- May discover this isn't needed through practice

---

## Success Criteria

**For manual November rollup:**
- [ ] Proposed structure successfully applied to real data
- [ ] All 5 open questions answered with evidence
- [ ] Archival workflow tested (what gets removed, what stays)
- [ ] Trajectory assessment works with October → November comparison
- [ ] Plan-vs-actual option tested (A, B, or C)

**For skill design:**
- [ ] Decision made: separate skill, parameterized skill, or manual-only
- [ ] If skill: frontmatter and structure drafted
- [ ] If manual: process documented for future months
- [ ] Compression principle validated (trust the rollup, don't re-read)

**For system integration:**
- [ ] Document lifecycle table added to WORKFLOW-GUIDE.md
- [ ] Archival reminders integrated into weekly/monthly skills
- [ ] Personal system works effectively at three timescales (daily/weekly/monthly)

---

## Design Principles

### 1. Fractal Consistency
- Same analytical framework at all scales
- "What Worked / What Didn't Work" structure repeats
- Trajectory assessment at each level
- Compression principle applies uniformly

### 2. Trust the Compression
- Each level compresses the level below
- Don't re-read before archiving
- Lossy compression is **intentional** (reduces cognitive load)
- If important, it surfaces in the rollup

### 3. Lean Project Context
- Archive aggressively after rollup exists
- Keep only what's needed for current/next timescale
- Full history lives locally, not in Claude Project
- Summary-of-summaries maintains continuity

### 4. Test Before Abstracting
- Manual rollup first (November 2025)
- Extract skill pattern from validated process
- Don't prematurely abstract before seeing what works
- Let practice inform design

---

## Notes

**Source:** Week 7 planning session (Nov 30, 2025)

**Key insight from Week 6 retro:** "This is first month-end in the system. Did month summary inside weekly retro (worked but ad-hoc). Need formal monthly-retrospective skill that rolls up weeklies."

**Next milestone:** Quarterly rollup won't be needed until February 2025 (3 monthly retros available)

**Related features:**
- F26: Monthly Retrospective Rollup (feature tracking)
- F17: Dec 12th Presentation (may include monthly rollup as narrative enhancement)

---

*Design validated through manual process → skill implementation → documentation*
