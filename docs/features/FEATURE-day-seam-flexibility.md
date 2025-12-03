# F25: Day Seam Flexibility

**Status:** Backlog - Low priority
**Effort:** Quick win (15-20 min)
**Priority:** Low (working fine currently)
**Created:** 2025-12-01

## Problem Statement

**Current behavior:**
- Summary files use naming: `Summary-YYYY-MM-DD-DayName.md`
- Date represents "date OF events" (not FOR next day)
- Works correctly, but instructions don't explicitly address boundary ambiguity

**Potential confusion for new users:**
- Natural conversation boundaries are often morning-to-morning
- Not midnight-to-midnight calendar boundaries
- Claude sessions often span multiple calendar days
- Where does the "day seam" actually fall?

**Current status:**
- Not causing actual problems in practice
- Existing instructions handle this implicitly
- More of a "future user clarity" concern

## Solution: Explicit Instruction Clarification

### Update daily-summary-base Skill

**Current instruction (implicit):**
- Date in filename represents date OF events
- Works but doesn't address seam ambiguity

**Proposed instruction (explicit):**
```markdown
## Date Handling & Day Boundaries

**Summary naming:** `Summary-YYYY-MM-DD-DayName-context-tag.md`
- Date = date OF events being summarized (not FOR next day)
- Example: `Summary-2025-11-26-Tuesday.md` summarizes Tuesday's events

**Day seam flexibility:**
- Natural conversation boundaries are morning-to-morning, not midnight-to-midnight
- A summary chat may span multiple calendar days (e.g., started Monday evening, completed Tuesday morning)
- The date represents the **logical day** being summarized, not the calendar day of summary creation
- Use your judgment: what day do these events "belong to" mentally?

**Examples:**
- Session starts 11:30 PM Monday, ends 12:30 AM Tuesday, discussing Monday → use Monday's date
- Session starts 8 AM Tuesday, ends 9 AM Tuesday, discussing Monday → use Monday's date
- Session starts 11 PM Tuesday, spans to Wednesday AM, discussing both days → use Tuesday's date (primary day) or Wednesday's date (use judgment)

**Key principle:** Date represents the day being reflected upon, not the timing of the reflection itself.
```

### Updates Needed

**Files to modify:**
1. `skills/daily-summary-base/SKILL.md` - Add explicit day seam guidance
2. `docs/WORKFLOW-GUIDE.md` - Reference this principle if relevant

**Changes:**
- Add "Date Handling & Day Boundaries" section to skill instructions
- Provide concrete examples of edge cases
- Emphasize "logical day" over "calendar day"

## Rationale

**Why this might be worth doing:**
- Eliminates ambiguity for new users
- Documents implicit knowledge that's currently only in maintainer's head
- Prevents potential confusion in Alice demo or friend adoption
- Small time investment (15-20 min) for clarity improvement

**Why this can wait:**
- Not causing actual friction currently
- Existing system works fine without explicit guidance
- Lower priority than presentation-critical work
- Can be added post-Dec 12th if needed

## Context from Skill Ideas Document

Original observation:
> "Natural conversation boundaries are morning-to-morning, not midnight"
> "'Summary OF [date]' concept already handles this"
> "Capture what matters for the *logical* day, not calendar day"

**Key insight:** The system already works this way implicitly. This feature is just about making it explicit.

## Success Criteria

**If implemented:**
- [ ] Day seam flexibility explicitly documented in daily-summary-base skill
- [ ] Edge case examples provided (spanning midnight, morning completions)
- [ ] "Logical day" principle clearly stated
- [ ] No ambiguity for new users about how to date summaries

**Evidence of success:**
- New users can confidently date summaries without asking questions
- Edge cases (spanning midnight) have clear guidance
- Documentation matches actual practice

## Timeline

**Target:** Time-permitting, after F17 Task 1, F24, and F26
**Estimated time:** 15-20 minutes
**Priority:** P2 (nice-to-have, not essential)

## Implementation Notes

**This is primarily a documentation update:**
- Edit skills/daily-summary-base/SKILL.md
- Add new section on date handling
- Repack skill: `python scripts/skill_workflow.py pack daily-summary-base`
- Test in Claude.ai (optional - change is low-risk)

**Could be combined with:**
- Other daily-summary-base refinements
- F17 Task 2 (separating weekly skills) might involve similar instruction clarification

## Decision: Defer or Do?

**Defer if:**
- F17 Task 1, F24, F26 take longer than expected
- Dec 12th presentation prep needs focus
- Current implicit handling is sufficient

**Do if:**
- Extra time available this week
- Want to polish skills before Alice demo
- Noticed this causing confusion in actual use

**Recommendation:** Defer to post-Dec 12th unless time permits and no other priorities.

---

**Related Features:**
- F17 Task 2: Weekly skills separation (similar instruction clarification)
- F24: Deployment workflow (would need to deploy updated skill)
- Alice demo: May want clarity before demo creation
