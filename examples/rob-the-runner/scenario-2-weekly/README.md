# Scenario 2: First Week Review

**Rob's state:** End of Week 1 - Finished 3 runs (Mon/Wed/Fri), ready for weekly review

## Purpose

Demonstrates the weekly rhythm:
- Morning routine loading yesterday's context
- Weekly retrospective after completing first week
- Weekly planning for the upcoming week

## Skills Tested

- `daily-morning-routine-base` - Loading yesterday's summary
- `retrospective-base` - Weekly reflection
- `planning-base` - Week ahead planning

## Demo Flow

1. Upload the 3 generated daily summaries to Claude Project
2. Say "good morning" → Morning routine finds Friday's summary
3. Say "weekly retro" → Generates Weekly-Retro-W1.md
4. Say "weekly planning" → Generates Weekly-Plan-W2.md

## Documents Present

**Before demo (upload these):**
- Summary-W1-D1.md (Monday - first run, everything hurts)
- Summary-W1-D3.md (Wednesday - shin pain, almost quit)
- Summary-W1-D5.md (Friday - made it through, felt slightly better)

**Generated during demo:**
- Weekly-Retro-W1.md
- Weekly-Plan-W2.md

## Key Narrative Points

Week 1 was the hardest:
- Day 1: Couldn't run 1 minute, everything hurt
- Day 3: Shin pain nearly made him quit
- Day 5: First day that didn't hurt as much - small win!

What kept him going:
- Wife's encouragement
- Kids asking "Did you run today, Dad?"
- Program structure (just follow, don't think)

Week 2 focus:
- Fix the shin pain (get better shoes)
- Don't increase intensity yet
- Just show up 3 more times

## Files

```
scenario-2-weekly/
├── README.md                    # This file
├── DEMO-SCRIPT.md              # Step-by-step demo instructions
├── templates/
│   ├── Summary-W1-D1.md.tmpl   # Monday (first run)
│   ├── Summary-W1-D3.md.tmpl   # Wednesday (shin pain)
│   └── Summary-W1-D5.md.tmpl   # Friday (end of week)
└── documents-generated/         # Generated documents for demo
```

## Regeneration

```bash
python scripts/regenerate_demo_dates.py --scenario 2 --demo-day 2025-12-12
```
