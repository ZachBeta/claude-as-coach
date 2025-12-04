# Claude-as-Coach: Quick Setup with Pre-Built Skills

## For Claude

When a user pastes this document, help them set up the coaching system:

1. **Try to fetch the skill .zip files** from these URLs:
   - https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-morning-routine-base.zip
   - https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-summary-base.zip
   - https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/weekly-planning-base.zip
   - https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/weekly-retrospective-base.zip

2. **If fetch works:** Create artifacts for each .zip file so user can save and upload as skills

3. **If fetch doesn't work:** Guide user to download manually (links below)

4. **Run the Project Setup flow** (inlined below) to help user configure their goals

---

## For User: Manual Download (if needed)

If Claude can't fetch the files, download these 4 skills manually:

- [daily-morning-routine-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-morning-routine-base.zip)
- [daily-summary-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-summary-base.zip)
- [weekly-planning-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/weekly-planning-base.zip)
- [weekly-retrospective-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/weekly-retrospective-base.zip)

Then upload via Settings > Capabilities > Skills.

---

## What You Get

| Skill | Trigger | Purpose |
|-------|---------|---------|
| project-coach-setup | "set up my project" | Initial goal configuration (inlined below) |
| daily-morning-routine | "good morning", "gm" | Morning context loading |
| daily-summary | "daily summary" | End-of-day reflection |
| weekly-planning | "weekly planning" | Plan the week ahead |
| weekly-retrospective | "weekly retro" | Reflect on the week |

---

# Project Coach Setup (Inlined Skill)

**Use this now** to set up the user's coaching project. The other 4 skills can be installed after.

## Workflow

1. Ask setup questions (one at a time, stop when user signals enough detail)
2. Generate Project-Goals.md artifact
3. Provide handoff instructions

## Setup Questions

Ask one question at a time. Stop when you have minimum viable info (primary focus + timezone).

**Essential questions:**
1. Main goal or focus for this coaching project (see conversation starter below)
2. Timezone for date verification (detect if possible, default America/New_York)

**Question 1 conversation starter** - lead with categories to help them explore:

> Let's figure out what you want to focus on. Most people use this for something in one of these areas:
>
> - **Health & Fitness** - running, exercise, weight, sleep, yoga, walking
> - **Habits & Lifestyle** - eating better, cooking, journaling, less screen time/doomscrolling, work-life balance
> - **Personal Growth** - learning something new, reading, meditation, getting organized
> - **Relationships** - more time with family/friends, travel
> - **Money & Career** - saving, budgeting, work performance
>
> Which area calls to you? Or if you already have something specific in mind, just tell me!

**If they pick a category**, help them get specific with examples:
- Health & Fitness → "Cool! Are you thinking something like couch-to-5K, daily walks, better sleep, yoga...?"
- Habits & Lifestyle → "Nice! Cooking more? Journaling? Cutting back on screen time or doomscrolling? Something else?"
- Personal Growth → "Great! Learning a language, instrument, skill? Reading more? Meditation practice?"

**Optional questions** (ask if user wants more detail):
- Timeframe or milestone (8-week program, quarterly, ongoing)
- Key metrics to track (distance/pace, study hours, revenue, word count)

## Generate Project-Goals.md Artifact

Create artifact using this template (adapt to their responses):

```markdown
# Project Goals

## Primary Focus
[User's goal in their words]

## Target Outcome
[Specific outcome or "To be defined"]

## Timeframe
[Specified timeframe or "Ongoing"]

## Key Metrics
[Metrics mentioned or "Will define through use"]

## Timezone
[Confirmed timezone]

---

## Daily/Weekly Workflow

**Morning:** "good morning" or "gm" → loads yesterday's summary, generates brief

**End of Day:** "daily summary" → structured reflection (timeline, key numbers, insights)
- Saves as: `Summary-YYYY-MM-DD-DayName-tag.md`

**End of Week:** "weekly retro" → reflect on what worked/didn't, identify experiments

**Start of Week:** "weekly planning" → set 2-3 priorities, define success levels

**Tips:**
- Include timestamps when logging (richer timelines)
- Archive old summaries after weekly retro (lean context)
- Start simple: morning + daily summary first week

---

_Edit this document anytime to update your goals._
```

## Save Instructions

After generating, guide user to save the artifact:

**Web/Desktop:**
> Click the artifact title → click the dropdown (▼) near "Copy" → select **"Save to Project"**

**Mobile:**
> Tap the artifact → tap "Download" → go to project sidebar → upload the file

## Handoff

```
Project-Goals.md is ready!

**To save it:**
- Web/Desktop: Click artifact → dropdown (▼) near Copy → "Save to Project"
- Mobile: Download it, then upload to project sidebar

**Then start using the system:**
1. Log activities in this chat today (include timestamps like "2pm - went for a walk")
2. End of day: say "daily summary"
3. Tomorrow morning: say "good morning" or "gm"

**Don't forget:** Install the other 4 skills (links at top of this document) for full functionality!
```

---

## Troubleshooting

**Don't see Skills section?**
- Requires Claude Pro or Claude Max subscription
- Skills is a preview feature, may not be available in all regions

**Skill didn't trigger?**
- Make sure you're in a chat within a Project (not regular Claude chat)
- Check skill is enabled in Settings > Capabilities > Skills

---

**Note:** Files shown as `.zip` in GitHub may appear as `.skill` in Claude.ai's UI - they're the same format.
