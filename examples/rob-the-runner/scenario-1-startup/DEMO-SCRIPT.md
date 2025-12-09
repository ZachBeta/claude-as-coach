# Demo Script - Scenario 1: Getting Started

**Duration:** ~10 minutes
**Purpose:** Show how someone begins using Claude-as-Coach from scratch

---

## Setup (Before Demo - 2 minutes)

### 1. Create Claude Project
- Name: "Rob Demo - Getting Started"
- Model: Sonnet 4.5 or Opus 4.5

### 2. Upload Base Skills Only
```
skills/daily-summary-base.zip
```

**Note:** Only daily-summary needed for this scenario. We're showing the simplest starting point.

### 3. No Documents to Upload
This scenario starts empty - that's the point!

---

## Demo Flow (8 minutes)

### Phase 1: Set Context (1 min)

**Explain to audience:**
> "Rob is a 39-year-old accountant who just started a couch-to-5K program. He got winded playing tag with his kids and decided to make a change. Today is his first day using Claude as his coach. Let's see how the system captures his experience."

---

### Phase 2: Paste Conversation Snippets (4 min)

Open `conversation-snippets.md` and paste snippets one at a time.

**Snippet 1: Morning (After First Run)**
```
Just finished my first run. "Run" is generous - it was more like shuffling with occasional walking.

The couch-to-5K app said: Walk 2 min / Run 1 min x 8 reps. I made it through all 8 reps but barely.

After just the first 1-minute run interval I was already breathing hard. By the third interval I wasn't sure I'd make it. My calves are on fire. My shins hurt. Even my lungs feel weird.

Total time: about 24 minutes (including warmup walk)
Distance: maybe 1.5 miles? The app doesn't track distance, just time.
How I feel: 3/10. Everything hurts.
```

**Let Claude react.** It might offer encouragement or ask questions.

**Snippet 2: Midday Reflection**
```
Sitting at my desk thinking about this morning. I'm 39 years old and I couldn't run for ONE MINUTE without gasping.

The realization that got me here: Playing tag with my kids (6 and 8) last weekend, I was winded after 10 minutes. They wanted to keep going. I needed to sit down.

When did I get this out of shape? I used to play pickup basketball in my 20s. Now I'm the dad who can't keep up with elementary schoolers.

I want to be able to play with my kids without needing to rest. That's the goal. The 5K is just the milestone.
```

**Snippet 3: Evening**
```
Wife asked how my first run went. I told her it was rough.

She said: "That's normal. Just try it for two weeks before you decide anything."

She's right. I signed up for 8 weeks. It's been one day. One terrible day, but one day.

Tomorrow is a rest day (the program is Mon/Wed/Fri). I'm already dreading Wednesday.

Sleep plan: Try to get 7+ hours. Apparently recovery matters for this running thing.

Did I mention my calves still hurt? Because they do.
```

---

### Phase 3: Generate Daily Summary (3 min)

**Say:**
```
daily summary
```

**Expected flow:**
1. Skill triggers, verifies current date
2. Asks: "Which date's summary are we generating?" → "today"
3. Confirms date → "yes"
4. Asks for context tag → "W1-D1" (Week 1, Day 1)
5. Generates structured summary

**Point out in the output:**
- **TL;DR:** Captures the essence of the day
- **Key Numbers:** Structured metrics (even when sparse)
- **Timeline:** Events organized chronologically
- **Insights:** Patterns and realizations identified
- **Tomorrow's Focus:** Next steps

---

## Key Demo Messages

1. **No prior documents needed**
   - The system works from day 1
   - Natural conversation becomes structured data

2. **Base skill does the heavy lifting**
   - No custom personal skill required
   - Framework provides useful structure out of the box

3. **Context captured for future use**
   - This summary becomes context for tomorrow's morning routine
   - Begins building the data foundation

4. **Low barrier to entry**
   - Start talking, Claude structures it
   - You don't need to know the "right" format

---

## If Questions Come Up

**"What if I don't have metrics?"**
> The system works with whatever you have. Rob didn't know his heart rate or exact distance. That's fine - you capture what you know.

**"Do I need to paste snippets like this?"**
> No, this is demo format. In real use, you'd just chat naturally throughout the day. The skill extracts structure from any conversation.

**"What happens to this summary?"**
> You'd save it to Project Knowledge. Then tomorrow's morning routine can find it and give you context.

---

## Transition to Next Scenario (if continuing)

> "Now Rob has his first summary. In Scenario 2, we'll see what happens after his first full week - with 3 summaries ready for weekly review."
