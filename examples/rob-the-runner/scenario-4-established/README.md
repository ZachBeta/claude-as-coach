# Scenario 4: Established User

**Rob's state:** Week 9 - First week post-program, exploring "what's next"

## Purpose

Demonstrates full established workflow:
- Rich context from compressed history
- All skills working together
- Ongoing practice beyond initial goal
- "What's next?" exploration phase

## Skills Tested

All skills in full workflow context:
- `daily-morning-routine-base` - Morning context loading
- `daily-summary-base` - Daily capture
- `retrospective-base` - Weekly reflection
- `planning-base` - Week ahead planning

## Demo Flow

1. Upload all documents to Claude Project
2. Say "good morning" → Morning routine loads yesterday's context
3. Paste conversation about today's run + yoga session
4. Say "daily summary" → Generates today's summary
5. Say "weekly retro" → Generates Weekly-Retro-W9.md
6. Say "weekly planning" → Generates Weekly-Plan-W10.md

## Documents Present

**Historical (compressed):**
- Monthly-Rollup-October.md (Weeks 1-4)

**Recent weeks:**
- Weekly-Retro-W5.md, W6.md, W7.md (Weeks 5-7)

**Last week (final program week):**
- Summary-W8-D1.md, D2.md, D3.md

**Current week:**
- Summary-W9-D1.md, D2.md (plus W9-D5.md for "yesterday")
- Weekly-Plan-W9.md

## Key Narrative Points

Rob completed couch-to-5K and kept going:
- Week 8: Finished the program (30-min continuous run)
- Week 9: First "free" week - no program to follow

"What's next?" exploration:
- Running 3x/week feels normal now
- Started yoga with wife (3x/week)
- Maybe 10K in spring? No pressure to decide
- First time in years something stuck

The yoga surprise:
- Thought it would be "easy" compared to running
- It's not. Different hard.
- Balance is humbling
- But doing it with wife feels connective

Sustainable habits:
- Run 3x/week (Mon/Wed/Fri or Sat)
- Yoga 3x/week (Tues/Thurs/weekend)
- No big experiments needed - let pattern settle

## Files

```
scenario-4-established/
├── README.md                              # This file
├── DEMO-SCRIPT.md                        # Step-by-step demo instructions
├── templates/
│   ├── Monthly-Rollup-October.md.tmpl    # Weeks 1-4 compressed
│   ├── Weekly-Retro-W5.md.tmpl           # Week 5
│   ├── Weekly-Retro-W6.md.tmpl           # Week 6
│   ├── Weekly-Retro-W7.md.tmpl           # Week 7
│   ├── Summary-W8-D1.md.tmpl             # Week 8 Mon
│   ├── Summary-W8-D2.md.tmpl             # Week 8 Wed
│   ├── Summary-W8-D3.md.tmpl             # Week 8 Fri
│   ├── Summary-W9-D1.md.tmpl             # Week 9 Mon
│   ├── Summary-W9-D2.md.tmpl             # Week 9 Wed
│   ├── Summary-W9-D5.md.tmpl             # Week 9 Fri (yesterday)
│   └── Weekly-Plan-W9.md.tmpl            # Current plan
└── documents-generated/                   # Generated documents for demo
```

## Regeneration

```bash
python scripts/regenerate_demo_dates.py --scenario 4 --demo-day 2025-12-12
```

## Note on Week Numbers

This scenario uses W5-W9 (later in Rob's journey), while scenarios 1-3 use W1-W4 (beginning of journey). The regeneration script handles different placeholder systems for each scenario.
