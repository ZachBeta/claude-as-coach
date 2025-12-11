# Presentation: Dec 12, 2025

## Setup

### VS Code (Recommended)

1. Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension
2. Open `SLIDES-dec-12.md`
3. Click the preview icon (or Cmd+Shift+V)
4. Use "Marp: Export Slide Deck" to generate PDF/HTML/PPTX

### CLI

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Preview in browser
marp SLIDES-dec-12.md --preview

# Export to PDF
marp SLIDES-dec-12.md --pdf

# Export to HTML (self-contained)
marp SLIDES-dec-12.md --html

# Export to PPTX
marp SLIDES-dec-12.md --pptx
```

## Demo Projects to Create

Before the presentation, create these Claude.ai projects with pre-run scenarios:

| Project Name | Setup | Pre-run |
|--------------|-------|---------|
| `rob-morning` | Import Rob's Week 8 summaries | Run "gm", keep conversation |
| `rob-daily-summary` | Import Rob's documents | Run "daily summary", complete it |
| `rob-weekly-retro` | Import Week 8 dailies | Run "weekly retro", complete it |
| `rob-weekly-plan` | Import Week 8 retro | Run "weekly planning", complete it |

### Project Setup Checklist

For each project:
- [ ] Create new Claude.ai project
- [ ] Name it clearly (e.g., "Demo: Rob Morning Routine")
- [ ] Import base skills (daily-summary-base.zip, etc.)
- [ ] Import relevant Rob documents from `examples/rob-the-runner/documents/`
- [ ] Run the scenario
- [ ] Keep the conversation (don't close it)

## Slides with UI Switch Points

Slides marked with `<!-- SWITCH TO: ... -->` comments indicate where to:
1. Leave the slides
2. Show the actual Claude.ai UI or repo
3. Walk through the live example

## Timing (Target: 45-50 min + Q&A)

| Section | Slides | Est. Time |
|---------|--------|-----------|
| Intro + Problem | 1-3 | 3 min |
| Projects Explained | 4-5 | 5 min |
| Skills Explained | 6-9 | 7 min |
| Projects vs Code | 10 | 3 min |
| The System Loop | 11-12 | 4 min |
| Demo (4 scenarios) | 13-20 | 15 min |
| Repo Structure | 21-22 | 5 min |
| Evolution + Learnings | 23-25 | 5 min |
| Future + Pitch | 26-29 | 5 min |
| **Total** | 29 | ~50 min |
| Q&A | - | 10 min |

## Screenshot Placeholders

The slides reference these screenshots (to be captured):

- `rob-morning-brief.png` - Morning routine output
- `rob-daily-summary.png` - Completed daily summary
- `rob-weekly-retro.png` - Weekly retrospective
- `rob-weekly-plan.png` - Weekly plan with L0-L3

Save screenshots to `docs/presentation/screenshots/` and update image paths in slides.

## Test Run Plan

**Today at 4pm:**
1. Run through slides with timer
2. Practice UI switches
3. Note any rough transitions
4. Identify cuts if running long
