# Demo Script - Scenario 1: Getting Started

**Duration:** ~12 minutes
**Purpose:** Show how someone begins using Claude-as-Coach from scratch, including getting a plan

---

## Setup (Before Demo - 2 minutes)

### 1. Create Claude Project
- Name: "Rob Demo - Getting Started"
- Model: Sonnet 4.5 or Opus 4.5

### 2. Bootstrap Skills
Use `docs/experiments/onboarding-approaches/bootstrap-with-zips.md`:
1. Ensure skill-creator is installed
2. Paste bootstrap content
3. Download 4 skill artifacts, upload via Settings > Capabilities
4. Project setup flow will start automatically

### 3. No Documents to Upload
This scenario starts empty - that's the point!

---

## Demo Flow (10 minutes)

### Phase 1: Set Context (1 min)

**Explain to audience:**
> "Rob is a 39-year-old accountant who wants to start running. He got winded playing tag with his kids and decided to make a change. He's heard of couch-to-5K but doesn't know where to start. Let's see how Claude helps him create a plan and then captures his first day."

---

### Phase 2: Project Setup (2 min)

**Claude asks about focus area. Paste from `conversation-snippets.md`:**

```
Health & Fitness - I want to do a couch-to-5K running program.

I'm 39, work as an accountant, and realized I'm way more out of shape than I thought. Last weekend I was playing tag with my kids (6 and 8) and had to sit down after 10 minutes while they wanted to keep going.

That was a wake-up call. I want to be able to keep up with my kids. The 5K is just a milestone - the real goal is not being the winded dad on the sidelines.

I've heard couch-to-5K programs are about 8 weeks, but I don't really know where to start. Can you help me figure out a plan?
```

**Claude will:**
- Create Project-Goals.md
- Offer to help with the couch-to-5K plan

**Save Project-Goals.md to project.**

---

### Phase 3: Get the Plan (2 min)

**Ask for specifics:**

```
This sounds doable. Can you give me the week-by-week breakdown? I want to know exactly what I'm signing up for.

Also - when should I run? Morning before work? Evening? I'm not sure what works best for beginners.
```

**Point out to audience:**
- Claude is providing coaching value, not just capturing data
- The plan will be referenced in future summaries
- This shows the system works for planning, not just reflection

---

### Phase 4: Day 1 Report (3 min)

**Paste snippets from `conversation-snippets.md` one at a time:**

**Snippet 2: After First Run**
```
Just finished Day 1. "Finished" is generous - I survived it.

Did the plan you gave me: 5 min warmup walk, then 8 rounds of run 1 min / walk 2 min.

Honest report:
- First 1-minute run: okay, I can do this
- Third interval: breathing hard, questioning life choices
- Fifth interval: had to stop 10 seconds early
- Eighth interval: somehow finished but my legs felt like jelly

Total time: about 29 minutes
How I feel: 3/10. My calves are on fire. My shins hurt. Even my lungs feel weird.

But I did it. Day 1 is done.
```

**Snippet 3: Midday Reflection**
```
Sitting at my desk thinking about this morning. I'm 39 years old and I couldn't run for ONE MINUTE without gasping.

When did I get this out of shape? I used to play pickup basketball in my 20s. Now I'm the dad who can't keep up with elementary schoolers.

The fact that I have 7 more weeks of this is terrifying. But also... I finished today. That's something.
```

**Snippet 4: Evening Check-in**
```
Wife asked how my first run went. I told her it was rough.

She said: "That's normal. Just try it for two weeks before you decide anything."

She's right. I signed up for 8 weeks. It's been one day. One terrible day, but one day.

Next run is Friday according to the plan. I'm already dreading it.

Sleep plan: Going to try for 7+ hours tonight. I read somewhere that recovery matters.

Did I mention my calves still hurt? Because they do.
```

---

### Phase 5: Generate Daily Summary (2 min)

**Say:**
```
daily summary
```

**Expected flow:**
1. Skill triggers, verifies current date
2. Asks: "Which date's summary?" → "today"
3. Confirms date → "yes"
4. Asks for context tag → "W1-D1" (Week 1, Day 1)
5. Generates structured summary

**Point out in the output:**
- **TL;DR:** Captures the essence of the day
- **Key Numbers:** Time, intervals, effort level
- **Timeline:** Plan created → first run → reflection → evening
- **Insights:** Patterns and realizations identified
- **Tomorrow's Focus:** Next steps (rest day, Friday run)

---

## Key Demo Messages

1. **Coaching, not just capture**
   - Claude helped create the plan Rob is following
   - The system provides value before any data exists

2. **Natural conversation becomes structured data**
   - Rob just talked about his day
   - The skill extracts structure automatically

3. **Context builds over time**
   - This summary becomes context for tomorrow's morning routine
   - Friday's run will reference today's baseline

4. **Low barrier to entry**
   - No prior documents needed
   - No "right format" to learn
   - Just talk, Claude structures it

---

## If Questions Come Up

**"What if Claude's plan differs from the real C25K?"**
> That's fine - the point is Claude provides *a* reasonable plan. In real use, Rob might say "I found this app, here's its plan" and Claude adapts.

**"Do I need to paste snippets like this?"**
> No, this is demo format. In real use, you'd just chat naturally throughout the day.

**"What happens to this summary?"**
> Save it to Project Knowledge. Tomorrow's morning routine finds it and gives context.

**"Can I edit the summary?"**
> Absolutely. It's a starting point. Add details, fix anything wrong, make it yours.

---

## Transition to Next Scenario (if continuing)

> "Now Rob has his first summary and a plan to follow. In Scenario 2, we'll see what happens after his first full week - with 3 daily summaries ready for weekly review."
