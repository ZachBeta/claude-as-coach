# Rob the Runner - Demo Persona (Base Skills Only)

**This is synthetic demo data created for demonstrating Claude-as-Coach.**

## About Rob

**Name:** Rob
**Age:** 39 (turning 40 in ~6 months)
**Profession:** Accountant at mid-size firm
**Starting Point:** Sedentary office worker, gained 25 lbs over 5 years, random aches and pains

**Motivation:** Playing tag with his kids (ages 6 and 8) in the backyard, got winded after 10 minutes. Realized: "When did I get this out of shape?" Approaching 40th birthday, wants to be the dad who can keep up with his kids.

**Goal:** Complete a 5K run using a structured 8-week couch-to-5K program

## Four Demo Scenarios

Rob's journey is divided into four scenarios, each demonstrating different aspects of the coaching system:

| Scenario | Rob's State | Skills Demonstrated | Use Case |
|----------|-------------|---------------------|----------|
| **[1. Getting Started](scenario-1-startup/)** | Day 1, just had first run | daily-summary | Onboarding new users |
| **[2. First Week Review](scenario-2-weekly/)** | End of Week 1 | morning-routine, retro, planning | Weekly rhythm |
| **[3. Monthly Review](scenario-3-monthly/)** | End of Week 4 | monthly retrospective | Fractal compression |
| **[4. Established User](scenario-4-established/)** | Week 9 (post-program) | Full workflow | Ongoing practice |

**Choose the scenario that matches what you want to demonstrate.**

---

## Scenario 1: Getting Started

**Location:** `scenario-1-startup/`

**Rob's state:** Just started couch-to-5K, had his first run today. No existing documents.

**What it shows:**
- How someone begins using the system from scratch
- First daily summary generation
- Capturing structured data from natural conversation

**Documents:** None (generates Summary-W1-D1.md during demo)

---

## Scenario 2: First Week Review

**Location:** `scenario-2-weekly/`

**Rob's state:** Finished Week 1 (3 runs: Mon/Wed/Fri), ready for weekly retro.

**What it shows:**
- Morning routine loading yesterday's summary
- Weekly retrospective after first week
- Weekly planning for upcoming week
- The core weekly rhythm

**Documents:**
- Summary-W1-D1.md (Monday - first run, everything hurts)
- Summary-W1-D3.md (Wednesday - shin pain, almost quit)
- Summary-W1-D5.md (Friday - made it through)

---

## Scenario 3: Monthly Review

**Location:** `scenario-3-monthly/`

**Rob's state:** Finished Week 4 / first month, ready for monthly retrospective.

**What it shows:**
- Fractal compression (4 weekly retros → 1 monthly summary)
- How patterns emerge at monthly timescale
- Historical context building

**Documents:**
- Weekly-Retro-W1.md through W4.md (4 weekly retros)
- Summary-W4-D5.md (most recent daily)

---

## Scenario 4: Established User

**Location:** `scenario-4-established/`

**Rob's state:** Week 9, first week post-program, exploring "what's next" (yoga with wife, 10K goal?).

**What it shows:**
- Full established workflow
- Rich context from compressed history
- Ongoing practice beyond initial goal

**Documents:**
- Monthly-Rollup-October.md (Weeks 1-4 compressed)
- Weekly-Retro-W5, W6, W7.md (Weeks 5-7)
- Summary-W8-D1, D2, D3.md (Week 8)
- Summary-W9-D1, D2.md (current week)
- Weekly-Plan-W9.md (current plan)

---

## Running a Demo

Each scenario has:
- `README.md` - Scenario description
- `DEMO-SCRIPT.md` - Step-by-step demo flow
- `templates/` - Source templates with date placeholders
- `documents-generated/` - Generated documents for demo day

**Before demo:**
```bash
# Regenerate documents for your demo day
python scripts/regenerate_demo_dates.py --scenario 2 --demo-day 2025-12-12

# Or generate all scenarios
python scripts/regenerate_demo_dates.py --scenario all --demo-day 2025-12-12
```

## Key Demonstration Value

**Rob uses BASE SKILLS ONLY - no custom personal extensions.**

This shows:
- The system works out-of-box with zero customization
- You don't need personal skills to get value
- Lower barrier to entry for new users
- Base skills provide solid structure

**Contrast with Alice example:** Alice shows extensibility; Rob shows simplicity.

---

**Remember:** Rob is a fictional persona. This is synthetic demo data, not real personal information.
