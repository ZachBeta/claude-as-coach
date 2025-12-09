# Scenario 1: Getting Started

**Rob's state:** Day 1 - Just had his first run, nothing exists yet

## Purpose

Demonstrates how someone begins using Claude-as-Coach from scratch:
- No existing documents in the project
- Natural conversation about the day's activity
- First daily summary generation

## Skills Tested

- `daily-summary-base` - Capturing structured data from conversation

## Demo Flow

1. Create a new Claude Project (or use empty test project)
2. Import base skills
3. Paste conversation snippets about Rob's first run
4. Say "daily summary"
5. Claude generates structured Summary-W1-D1.md

## What to Show

**Before:** Empty project, no documents

**After:** First structured daily summary with:
- TL;DR section
- Key Numbers (distance, time, how he felt)
- Timeline of the day
- Insights section
- Tomorrow's focus

## Key Narrative Points

Rob's first run was brutal:
- Couldn't run 1 minute without huffing
- Everything hurt: calves, shins, quads, lungs
- Winded after just 1-2 minutes
- Internal monologue: "I'm 39 and can't run 2 minutes?"
- But he finished the workout

Wife's encouragement: "Just try it for 2 weeks"

## Files

```
scenario-1-startup/
├── README.md                    # This file
├── DEMO-SCRIPT.md              # Step-by-step demo instructions
├── conversation-snippets.md    # Content to paste during demo
├── templates/                  # Empty (no templates needed)
└── documents-generated/        # Empty (generates during demo)
```

## Regeneration

This scenario has no templates to regenerate - the demo generates content from scratch.
