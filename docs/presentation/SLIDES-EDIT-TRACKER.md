# Slides Edit Tracker

Working document for slide-by-slide review. Using titles as anchors since slide numbers will shift.

**Status:** 🔴 Needs work | 🟡 Minor tweaks | 🟢 Good

---

## TITLE: "Claude-as-Coach"
**Status:** 🔴 Merge with next slide

**Current:**
```
# Claude-as-Coach
**Zero-build context management for behavior change**
Zach Morek | Dec 12, 2025
```

**Issue:** Duplicated with "The Problem" slide

**Action:** Merge into single opener or make title minimal

---

## TITLE: "The Problem"
**Status:** 🔴 Merge with title slide

**Current:**
```
- Context dies between Claude conversations
- Building agents is overkill for personal tracking
- You want **continuity**, not infrastructure
```

**Issue:** Duplicates title slide framing

**Action:** Delete after merging content into title slide

---

## TITLE: "What if you could just... talk to it?"
**Status:** 🟡 Needs tuning

**Feedback:** Problem statement needs tuning

**Action:** Refine the hook - make it land better for AI engineers

---

## TITLE: "Claude.ai Projects"
**Status:** 🟡 Good idea, not landing

**Feedback:** Like the concept but not sure it's landing right

**Action:** Rework to be clearer about why Projects specifically (vs building agent, vs Claude Code)

---

## TITLE: "Projects: The Mental Model"
**Status:** 🟢 Great

**Feedback:** Great summary of why claude.ai projects as exploration space over building an agent or fitting into Claude Code (which may have system prompts tuned for coding, not journaling)

**Action:** Keep, possibly expand on this reasoning

---

## TITLE: "What's a Skill?"
**Status:** 🔴 Formatting + content

**Feedback:**
- Formatting issue with visual
- Better served showing Rob's scenario 4
- Need to explain: Skills have name + description. Description explains when to load full skill into context
- Analogy: "A skill is a kind of function that can run on an LLM"

**Action:**
- Fix formatting
- Add name/description explanation
- Consider showing Rob scenario 4 visual instead

---

## TITLE: "Skills: Just Markdown"
**Status:** 🟢 Good

**Action:** Keep as is

---

## TITLE: "The .zip/.skill Confusion"
**Status:** 🟡 Needs accuracy

**Feedback:** Not totally accurate - need to clarify and link to exact documents/screenshots showing dissonance

**Action:**
- Verify accuracy
- Add links to Anthropic docs showing the issue
- Consider adding screenshot

---

## TITLE: "Projects vs Claude Code"
**Status:** 🟡 Good start, needs expansion

**Feedback:**
- Should specify that claude.ai conversation agent can create artifacts that download or add to project documents
- Good start at explaining why this approach was chosen

**Action:** Add artifact → project document flow explanation

---

## TITLE: "The System: Daily → Weekly Loop"
**Status:** 🔴 Needs differentiation

**Feedback:**
- Need to differentiate conversations vs artifacts (that become project documents)
- Possibly add slide showing expansion to different time scales
- "Summary of summaries" concept
- "Schrodinger's RAG - dead or alive depending on when you open the repo"

**Action:**
- Split into multiple slides?
- Add time scale expansion visual
- Clarify conversation vs artifact vs document

---

## TITLE: "Fractal Compression"
**Status:** 🟡 Experimental, needs nuance

**Feedback:**
- Monthly interval may compress too frequently in practice
- "Nothing lost" is inaccurate
- Curation process follows SWE sprint retro: What worked (more) / What didn't (experiment) / Retro-retro
- Curates context, simplifies architecture dramatically
- Requires manual curation

**Action:**
- Soften "nothing lost" claim
- Add nuance about manual curation
- Mention sprint retro pattern

---

## TITLE: "Demo Time: Rob the Runner"
**Status:** 🟢 Great start

**Action:** Will iterate on demos 13-21

---

## TITLES: Demo slides (1-4) + outputs
**Status:** 🟢 Great start

**Action:** Iterate as needed

---

## TITLE: "Base + Personal Skill Pattern"
**Status:** 🟡 Terminology fix

**Feedback:** "merges" is inaccurate - Claude combines skills at runtime (demonstrated in Alice examples)

**Action:** Change "merges" to "combines at runtime" or similar

---

## TITLE: "The Evolution"
**Status:** 🔴 Major rework - split into multiple slides

**Feedback:** Timeframes inaccurate. Real progression was:

**v1:** Giant Google Doc with daily logging
- Gaining insights was challenging
- Required manual effort or building systems
- Wanted single place for: project work, exercise, sleep, diet
- Too much cognitive load sifting through it

**v2:** Various journaling agent attempts
- General agent conversations
- Create summary → copy/paste into new chat daily

**v3:** Projects + saving to documents
- Instructions saved as documents
- Didn't realize project docs always in context
- Wasted tokens reading files already in context
- Burned tokens on instruction docs always loaded

**v4:** Pushed instruction docs to skills
- Skills only loaded as needed
- Retro instructions not included every day

**v5:** Skill inheritance experiments
- Personal process → shareable framework
- Structural vs personal specific
- General goal vs my specific goal
- claude-as-coach-combined = claude-as-coach + claude-as-coach-personal

**Action:**
- Split into multiple slides showing this progression
- Visualize context waste problem (like `/context` command)
- Show the "aha moments" at each transition

---

## TITLE: "What I Learned"
**Status:** 🟡 Add "bitter lesson" angle

**Feedback:**
- Why over-engineer when context windows have grown?
- Easy to summary-of-summary and keep docs in context
- Lower friction than RAG
- Agent has memory system that decays over time, like a person

**Action:** Add the "bitter lesson" framing - simpler beats complex

---

## TITLE: "Platform Limitations (Real Talk)"
**Status:** 🟢 Useful, tune later

**Action:** Keep, refine as needed

---

## TITLE: "Where This Is Going"
**Status:** 🔴 Formatting needs work

**Action:** Fix formatting

---

## TITLE: "Try It Yourself"
**Status:** 🟡 Reprioritize

**Feedback:** Prioritize bootstrap process, deprecate manual quickstart

**Action:**
- Focus on bootstrap flow
- Make it simpler/clearer

---

## TITLE: "The Pitch"
**Status:** 🟡 Tone needs work

**Feedback:** Like showing low/zero build with simple primitives, but tone needs adjustment

**Action:** Refine tone for AI engineer audience

---

## TITLE: "Questions?"
**Status:** 🔴 Too sparse

**Feedback:** Rather than just "questions", show information-rich summary of all basic concepts

**Action:** Replace with summary slide that can hold during Q&A

---

## TITLES: Appendix slides
**Status:** 🔴 Needs work

**Action:** Rework appendix content

---

# Edit Queue

Priority order for edits:

1. [ ] Merge title + problem slides
2. [ ] Split "Evolution" into multiple slides (big one)
3. [ ] Fix "What's a Skill?" formatting + content
4. [ ] Add conversation vs artifact vs document differentiation
5. [ ] Fix "Base + Personal" terminology ("combines" not "merges")
6. [ ] Replace "Questions?" with summary slide
7. [ ] Add bootstrap focus to "Try It Yourself"
8. [ ] Tune remaining slides

---

# Notes

- Re-render after significant changes: `pandoc docs/presentation/SLIDES-dec-12.md -t revealjs -s -o docs/presentation/slides.html -V theme=white -V transition=slide`
- Speaker notes use `::: notes` blocks
- Test at 4pm today
