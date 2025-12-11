# FEATURE: Onboarding UX Audit

**Feature:** F47
**Status:** Proposed
**Effort:** Path A (1-2 hours)
**Priority:** Medium (user-reported friction)
**Source:** Discord user feedback (2025-12-11)

## Problem

User testing revealed several UX friction points during initial onboarding:

1. **Agent vs UI misalignment** - Project setup skill gives suggestions that don't match current claude.ai interface (e.g., how to save artifacts to project)
2. **Summary → New Conversation flow unclear** - Not obvious that users should start a new conversation after saving their daily summary
3. **"Quickstart" terminology** - May not align with mental model; "bootstrap" suggested as alternative

## Goal

Audit and update onboarding materials to match current claude.ai interface and reduce friction for new users.

## Tasks

### Task 1: Audit Agent Setup Instructions Against Current UI

**Files to audit:**
- `skills/project-coach-setup-base/SKILL.md` - Main setup skill
- `QUICKSTART.md` - Quick start guide
- `PROJECT-SETUP.md` - Comprehensive setup guide

**Checklist per file:**
- [ ] Save-to-Project instructions match current UI (Web/Desktop/Mobile)
- [ ] Settings navigation paths are accurate
- [ ] Screenshot descriptions match current interface
- [ ] No references to deprecated UI elements

**Known status:**
- F36 (Save-to-Project UX) was completed 2025-12-04 with platform-specific instructions
- Need to verify these instructions still match current claude.ai interface

### Task 2: Add Explicit "New Conversation" Step

**Problem:** Users don't realize they should start a new conversation after completing daily summary.

**Solution options:**

| Option | Description | Effort |
|--------|-------------|--------|
| A: Add to daily-summary-base skill | Include "save and start new chat" in closing instructions | 10 min |
| B: Add to project-coach-setup | Include workflow guidance during initial setup | 15 min |
| C: Add to QUICKSTART.md | Document in onboarding materials | 5 min |
| D: All of the above | Consistent messaging everywhere | 30 min |

**Recommended:** Option D - reinforce at multiple touchpoints

**Proposed text:**
> After saving your daily summary to the project, start a new conversation for your next session. Each conversation focuses on one task (morning routine, daily summary, etc.). Your saved documents carry context forward.

### Task 3: Evaluate "Quickstart" vs "Bootstrap" Terminology

**Current:** `QUICKSTART.md`

**User suggestion:** "Bootstrap" aligns better with morning routine pattern

**Considerations:**
- "Quickstart" is industry-standard (familiar to developers)
- "Bootstrap" has specific meaning (initial setup that enables subsequent operations)
- Target audience: mixed technical/non-technical for Dec 12th demo

**Decision needed:** Is rename worth the effort?

| Keep "Quickstart" | Rename to "Bootstrap" |
|-------------------|----------------------|
| Familiar term | Aligns with system metaphor |
| No file changes | Requires rename + reference updates |
| Clear meaning | May confuse non-technical users |

**Recommendation:** Keep "Quickstart" - lower priority than content accuracy

## Deliverables

- [ ] Audited and updated `project-coach-setup-base/SKILL.md`
- [ ] Audited and updated `QUICKSTART.md`
- [ ] Audited and updated `PROJECT-SETUP.md`
- [ ] "New conversation" guidance added to appropriate locations
- [ ] Decision documented on terminology (keep Quickstart or rename)

## Success Criteria

- User can follow setup instructions without encountering UI mismatches
- User understands conversation lifecycle (summary → save → new chat)
- No Discord feedback about UI confusion

## Related

- F36: Save-to-Project UX Instructions (completed 2025-12-04)
- F38: Alternative Onboarding Paths (testing paths A/B)
- F48: Project Description Template Enhancement (habit-building)

## Notes

- Keep changes minimal - focus on accuracy over perfection
- Test changes with fresh project after implementation
- Consider having a non-technical friend test updated instructions
