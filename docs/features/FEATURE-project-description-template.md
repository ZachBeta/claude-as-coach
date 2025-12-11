# FEATURE: Project Description Template Enhancement

**Feature:** F48
**Status:** Proposed
**Effort:** Quick win (15-20 min)
**Priority:** Medium (habit-building support)
**Source:** Discord user feedback (2025-12-11)

## Problem

User reported: "I don't yet have the habit and keep forgetting what to do"

New users struggle to remember available commands and workflow because:
1. Project description is empty or minimal
2. Skills are in Settings > Capabilities (not visible during normal use)
3. No quick reference visible in the project itself

## Goal

When generating Project-Goals.md during setup, also prompt user to update their project description with a "How to Use This System" reference.

## Solution

### Option A: Add to Project-Goals.md artifact (Recommended)

Include a "Quick Reference" section in the generated Project-Goals.md that users can copy to their project description.

**Proposed addition to Project-Goals.md template:**

```markdown
---

## Quick Reference (Copy to Project Description)

**Daily commands:**
- `gm` or `good morning` - Morning routine and context loading
- `daily summary` - End-of-day structured reflection

**Weekly commands:**
- `weekly retro` - Reflect on what worked/didn't work
- `weekly planning` - Plan the week ahead

**Workflow:** Morning routine → Daily summary → Save to project → New conversation
```

### Option B: Update project description programmatically

Not possible - Claude.ai doesn't support programmatic project description updates.

### Option C: Verbal instruction during setup

Add step in project-coach-setup-base skill:

```markdown
**Tip:** Copy the Quick Reference section above to your project description.
This keeps commands visible whenever you start a new conversation.
```

## Implementation

**File to modify:** `skills/project-coach-setup-base/SKILL.md`

**Changes:**
1. Add "Quick Reference" section to Project-Goals.md template
2. Add verbal instruction to copy to project description
3. Explain why (habit-building, visible reminder)

## Philosophy Decision: Docs vs Agent Reliance

User feedback raises a question: Should users memorize commands or rely on asking the agent?

**Arguments for explicit docs:**
- Lower cognitive load (no need to ask)
- Works across conversations (project description persists)
- Builds muscle memory faster
- Doesn't consume tokens asking "what can I do?"

**Arguments for agent reliance:**
- Skills are in project context - agent knows what's available
- Natural language interaction ("what should I do next?")
- More flexible (agent can suggest based on context)

**Recommendation:** Both. Quick reference for common commands, agent for exploration and context-aware suggestions.

## Deliverables

- [ ] Updated Project-Goals.md template with Quick Reference section
- [ ] Instruction to copy to project description
- [ ] Repack project-coach-setup-base skill
- [ ] Test with fresh project setup

## Success Criteria

- User has visible command reference in project description after setup
- User doesn't need to remember commands from memory
- No friction asking "what command do I use for X?"

## Related

- F47: Onboarding UX Audit (broader UX improvements)
- F36: Save-to-Project UX Instructions (completed)

## Notes

- Keep reference minimal - just trigger phrases, not full explanations
- Users can always ask the agent for more detail
- Consider adding "Ask me anything about the system" to encourage exploration
