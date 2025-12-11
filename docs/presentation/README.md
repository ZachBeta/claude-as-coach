# Presentation: Dec 12, 2025

## Setup

### Building Slides (Pandoc + reveal.js)

```bash
cd docs/presentation

# Generate HTML slides
pandoc -t revealjs -s SLIDES-dec-12.md -o slides.html --slide-level=1

# Open in browser
open slides.html
```

**Requirements:** [Pandoc](https://pandoc.org/installing.html) installed.

### Alternative: Marp (if preferred)

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Preview in browser
marp SLIDES-dec-12.md --preview

# Export to HTML
marp SLIDES-dec-12.md --html
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

## Timing (Target: 50-55 min + Q&A)

| Section | Slides | Est. Time |
|---------|--------|-----------|
| Intro + Problem | 1-3 | 3 min |
| Evolution | 4-6 | 4 min |
| Projects Explained | 7-12 | 6 min |
| Skills Explained | 13-18 | 7 min |
| **Synthetic Data** | 19-23 | 5 min |
| Demo (4 scenarios) | 24-31 | 15 min |
| Architecture | 32-34 | 4 min |
| Lessons + Limitations | 35-36 | 3 min |
| Future + Pitch | 37-40 | 5 min |
| Summary + Appendix | 41-44 | 3 min |
| **Total** | 44 | ~55 min |
| Q&A | - | 10 min |

**New section:** "Synthetic Data" explains why we use fictional personas (Rob, Alice, Gina) for demos - covers reproducibility, privacy, and adoption benefits for AI engineers.

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
