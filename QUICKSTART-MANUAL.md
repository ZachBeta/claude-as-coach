# Quick Start: 10 Minutes to Your First Goal Coaching

## What You Need

- **Claude Pro or Claude Max** subscription
- Access to Claude Projects at [claude.ai/projects](https://claude.ai/projects)

**Model Recommendations:**
- **Recommended:** Sonnet 4.5 or Opus 4.5
- **Not recommended:** Haiku 4.5 (insufficient for skill execution based on testing)

**Context Management Tips:**
- **Claude Pro users:** Disable extended thinking to conserve context
- **Claude Max users:** Extended thinking works well, but monitor usage
- **Web search:** Don't enable unless absolutely needed - it consumes significant context
- **Monitor usage:** Check [Settings > Usage](https://claude.ai/settings/usage) regularly to track context consumption
  - Especially important if you're a heavy Claude Code user
  - Review day-over-day to ensure you don't run out of context for your project

---

## Step 1: Import the Base Skills (2 minutes)

**Download these 5 skill files** (click to download directly):

- [project-coach-setup-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/project-coach-setup-base.zip)
- [daily-morning-routine-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-morning-routine-base.zip)
- [daily-summary-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/daily-summary-base.zip)
- [retrospective-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/retrospective-base.zip)
- [planning-base.zip](https://github.com/ZachBeta/claude-as-coach/raw/refs/heads/main/skills/planning-base.zip)

**Upload them to claude.ai:**

1. Open your new Claude Project
2. Go to [Settings > Capabilities](https://claude.ai/settings/capabilities) (or click user panel bottom left > Settings > Capabilities)
3. Scroll down to **"Skills [Preview]"** section
4. Click **"Upload skill"** and upload each file one at a time
5. Confirm all 5 skills show as enabled (toggle switches should be on by default)

**Note:** Skills is a preview feature - if you don't see this section, make sure you have Claude Pro or Claude Max subscription.

---

## Step 2: Enable Artifacts (30 seconds)

1. While still in Settings > Capabilities
2. Make sure **"Artifacts"** is enabled (toggle on)

**Why:** The setup process creates a `Project-Goals.md` file that you'll save to your project.

---

## Step 3: Create a New Project (1 minute)

1. Go to [claude.ai/projects](https://claude.ai/projects)
2. Click **"Create Project"**
3. Name it something like **"My Coach"** or **"Daily Reflection"**
4. Click **"Create"**

---


## Step 4: Set Up Your Project (5 minutes)

Start a new chat in your project and type:

```
set up my project
```

**What happens:**
1. Claude asks about your goals (one question at a time)
2. Creates a `Project-Goals.md` file explaining what you're tracking
3. Save this file to your project

**After setup completes:**
- Start logging activities throughout your day (include timestamps for richer timelines)
- End of day: Type `daily summary` to create your first structured reflection
- Next morning: Type `run the daily morning routine skill` to start your day with context

**Pro tip:** Set a few calendar reminders to build the logging habit:
- Midday: "Log morning activities" (capture before you forget)
- Evening: "Daily summary"
- Friday: "Weekly retro"

---

## Step 5: Your First Morning Routine (Next Day)

After you've created at least one daily summary, start your next day with:

```
run the daily morning routine skill
```

**What happens:**
1. Verifies current date and time
2. Finds yesterday's summary
3. Generates a morning brief with context from yesterday

**Note:** After a few uses, you can use shortcuts like "gm" or "good morning" - but in fresh projects, use the explicit command first.

---

## What's Next?

- **See [PROJECT-SETUP.md](PROJECT-SETUP.md)** for a complete explanation of the system
- **See [EXAMPLES.md](docs/EXAMPLES.md)** to see how Maya set up her couch-to-5K tracking project
- **See [WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md)** if you want to customize skills for your specific goals

---

## Troubleshooting

**"I don't see the Skills [Preview] section"**
- Make sure you have Claude Pro or Claude Max (not just free tier)
- Skills feature may not be available in all regions yet

**"Claude didn't respond to 'set up my project'"**
- Check that the project-coach-setup-base skill is enabled in Settings > Capabilities > Skills
- Make sure you're in a chat within the project (not a regular Claude chat)
- Try refreshing the page

**"The morning routine skill didn't trigger"**
- In fresh projects, use the explicit command: `run the daily morning routine skill`
- After a few days of use, shortcuts like "gm" will work
- Check that the daily-morning-routine-base skill is enabled

**"Where do I download the skill files?"**
- They're in the `/skills/` directory of this repository
- Look for files ending in `-base.zip`

---

## Welcome!

You're now running with the base coaching framework. The system will help you:
- Start each day with context from yesterday
- Generate structured end-of-day summaries
- Reflect weekly on what's working
- Plan each week with clear priorities

The skills work with generic placeholders right now. As you use the system, you'll discover what you want to customize for your specific goals.
