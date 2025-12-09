# Scenario 3: Monthly Review

**Rob's state:** End of Week 4 / Month 1 - Completed first month, ready for monthly retrospective

## Purpose

Demonstrates fractal compression:
- 4 weekly retros compress into 1 monthly summary
- Patterns emerge at monthly timescale
- Historical context building

## Skills Tested

- `retrospective-base` (monthly scale) - Monthly reflection and pattern extraction

## Demo Flow

1. Upload the 4 weekly retros + recent daily summary to Claude Project
2. Say "monthly retro" or "let's do the monthly retrospective"
3. Claude synthesizes 4 weeks of data into Monthly-Rollup-October.md

## Documents Present

**Before demo (upload these):**
- Weekly-Retro-W1.md (first week struggles)
- Weekly-Retro-W2.md (adapting, less soreness)
- Weekly-Retro-W3.md (breakthrough - 3-min continuous run)
- Weekly-Retro-W4.md (10-min continuous run milestone!)
- Summary-W4-D5.md (most recent daily, for context)

**Generated during demo:**
- Monthly-Rollup-October.md

## Key Narrative Points

Month 1 transformation:
- Week 1: Couldn't run 1 minute without huffing
- Week 4: Ran 10 minutes continuously

Physical changes:
- Weight: 203 → 199 lbs (4 lbs down)
- Resting heart rate: 74 → 71 bpm
- Morning energy: noticeably improved

Mental shifts:
- Week 1: "I'm trying to become a runner"
- Week 4: "I'm following a running program"
- Identity shift in progress

Key learnings:
- Starting is the hardest part (Weeks 1-2 felt impossible)
- Body adapts faster than expected
- Consistency compounds
- Structure removes barriers

## Fractal Compression Visual

```
4 Weekly Retros (84 pages of content)
        ↓
1 Monthly Rollup (~8 pages)
        ↓
Preserved: Key themes, milestones, learnings
Compressed: Daily details, individual run metrics
```

## Files

```
scenario-3-monthly/
├── README.md                        # This file
├── DEMO-SCRIPT.md                  # Step-by-step demo instructions
├── templates/
│   ├── Weekly-Retro-W1.md.tmpl     # Week 1 struggles
│   ├── Weekly-Retro-W2.md.tmpl     # Week 2 adapting
│   ├── Weekly-Retro-W3.md.tmpl     # Week 3 breakthrough
│   ├── Weekly-Retro-W4.md.tmpl     # Week 4 milestone
│   ├── Summary-W4-D5.md.tmpl       # Friday Week 4
│   └── Monthly-Rollup-October.md.tmpl (reference)
└── documents-generated/             # Generated documents for demo
```

## Regeneration

```bash
python scripts/regenerate_demo_dates.py --scenario 3 --demo-day 2025-12-12
```
