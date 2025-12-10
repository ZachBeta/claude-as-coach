# Feature: Demo Teleprompter

**Status**: In Progress
**Location**: `scripts/demo_teleprompter.py`

---

## Overview

A step-by-step presenter tool for running Claude.ai Project demos. Reduces cognitive load by showing one step at a time and copying content to clipboard.

**Problem**: DEMO-SCRIPT.md files are walls of text that are hard to follow during a live presentation.

**Solution**: Interactive teleprompter that walks through demos step-by-step, handles clipboard, shows talking points.

---

## Current State

- [x] Core teleprompter script created
- [x] Scenario 1 (Getting Started) defined
- [x] pyperclip added to requirements.txt
- [ ] Test Scenario 1 with real Claude.ai Project
- [ ] Add Scenario 2 (Weekly Review)
- [ ] Add Scenario 3 (Monthly Review)
- [ ] Add Scenario 4 (Established User)

---

## Testing Plan

### Prerequisites

```bash
# Install dependencies
cd claude-as-coach
pip install -r scripts/requirements.txt

# Verify teleprompter runs
python scripts/demo_teleprompter.py --list
```

### Test 1: Scenario 1 with Claude.ai Project

**Goal**: Validate the teleprompter flow works end-to-end with a real Claude.ai Project.

#### Setup (one-time)

1. Create Claude.ai Project named "Rob Demo - Test"
2. Upload skill: `skills/daily-summary-base.zip`
3. Enable the skill in Project settings

#### Test Steps

| Step | Action | Expected Result | Pass? |
|------|--------|-----------------|-------|
| 1 | Run `python scripts/demo_teleprompter.py` | Shows Step 1/9 "Setup Context" | [ ] |
| 2 | Press Enter to advance to Step 2 | Shows "Morning Update" with snippet | [ ] |
| 3 | Press Enter (copies to clipboard) | "✓ Copied to clipboard!" appears | [ ] |
| 4 | Paste into Claude.ai Project | Claude responds to Rob's morning update | [ ] |
| 5 | Advance and paste Step 3 (Midday) | Claude acknowledges family motivation | [ ] |
| 6 | Advance and paste Step 4 (Evening) | Claude responds supportively | [ ] |
| 7 | Advance and type "daily summary" | Skill triggers, asks for date | [ ] |
| 8 | Follow prompts: "today" → "yes" → "W1-D1" | Summary generated with correct structure | [ ] |
| 9 | Advance to final step | Shows wrap-up talking points | [ ] |

#### Validation Checklist

- [ ] Clipboard copy works on each paste step
- [ ] Claude.ai skill triggers on "daily summary"
- [ ] Generated summary has expected sections (TL;DR, Key Numbers, Timeline, etc.)
- [ ] Flow feels natural for presenting
- [ ] Talking points are helpful reminders

#### Issues Found

_Document any issues discovered during testing:_

| Issue | Severity | Notes |
|-------|----------|-------|
| | | |

---

### Test 2: Navigation Controls

| Action | Expected | Pass? |
|--------|----------|-------|
| Press `b` | Goes back one step | [ ] |
| Press `q` | Exits teleprompter | [ ] |
| Press Enter on last step | Shows "Demo complete!" | [ ] |
| Ctrl+C | Exits gracefully | [ ] |

---

### Test 3: Edge Cases

| Scenario | Expected | Pass? |
|----------|----------|-------|
| Run without pyperclip installed | Shows warning, continues without clipboard | [ ] |
| Run with `--scenario 99` | Shows "not found" with available list | [ ] |
| Very long content in step | Wraps properly in box | [ ] |

---

## Adding New Scenarios

To add Scenario 2/3/4, add step definitions to `demo_teleprompter.py`:

```python
SCENARIO_2_STEPS = [
    {
        "phase": "Phase Name",
        "action": "PASTE TO CLAUDE",  # or "TYPE IN CLAUDE" or "SAY TO AUDIENCE"
        "content": "The text to paste/say",
        "talk": "Brief talking point for presenter",
        "expect": "What Claude should do",
    },
    # ... more steps
]

# Add to SCENARIOS dict
SCENARIOS = {
    1: {"name": "Getting Started", ...},
    2: {"name": "Weekly Review", "steps": SCENARIO_2_STEPS, ...},
}
```

### Source Material

| Scenario | DEMO-SCRIPT.md Location | conversation-snippets.md |
|----------|------------------------|--------------------------|
| 1 | `examples/rob-the-runner/scenario-1-startup/` | Yes |
| 2 | `examples/rob-the-runner/scenario-2-weekly/` | No (uses documents) |
| 3 | `examples/rob-the-runner/scenario-3-monthly/` | No (uses documents) |
| 4 | `examples/rob-the-runner/scenario-4-established/` | Yes |

---

## Future Enhancements

- [ ] Auto-detect scenario from uploaded documents
- [ ] Rich terminal output (colors via `rich` library)
- [ ] Timer/duration tracking per step
- [ ] "Pause" mode for audience Q&A
- [ ] Export to markdown checklist format

---

## Related Files

- `scripts/demo_teleprompter.py` - Main script
- `scripts/requirements.txt` - Dependencies (pyperclip)
- `examples/rob-the-runner/scenario-*/DEMO-SCRIPT.md` - Source material
- `examples/rob-the-runner/scenario-*/conversation-snippets.md` - Paste content
