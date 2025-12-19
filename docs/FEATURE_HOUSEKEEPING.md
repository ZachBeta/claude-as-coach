# Feature Housekeeping

Instructions for maintaining feature documentation. Designed to evolve into a skill for backlog management.

---

## Touch Counter System

Track how often features come up in conversation. High touch count = needs attention.

### Format

Add to feature entries that have been discussed multiple times:

```markdown
**Touches:** 3 (latest: 2025-12-19)
```

### When to Increment

Increment the touch counter when a feature:
- Comes up in conversation unprompted
- Is referenced while working on something else
- Appears in notes being processed
- Is mentioned by users/testers

### Priority Bubbling

Features with high touch counts should bubble up in priority:
- 3+ touches → Consider moving to Active
- 5+ touches → Likely blocking other work, prioritize

---

## Feature Lifecycle

```
Proposed → Active → Completed → Archived
              ↓
          Backlog (if deprioritized)
```

### States

| State | Meaning | Location in FEATURES.md |
|-------|---------|------------------------|
| Proposed | Idea captured, not yet planned | Backlog section |
| Active | Currently being worked on | Active section (High/Medium priority) |
| Backlog | Planned but deprioritized | Backlog section |
| Completed | Done, summary in FEATURES.md | Completed section |
| Archived | Detail doc deleted (git history preserves) | Completed section only |

---

## Housekeeping Checklist

Run when:
- Processing notes into features
- Completing a feature
- Doing backlog refinement
- Feature keeps coming up (touch counter trigger)

### 1. Process Incoming Notes

- [ ] Read misc notes files
- [ ] Extract actionable items as features
- [ ] Check if already tracked (update existing vs create new)
- [ ] Delete processed notes

### 2. Update Touch Counters

- [ ] Increment counter for features discussed
- [ ] Update "latest" date
- [ ] Check if any features need priority bump (3+ touches)

### 3. Feature Status Updates

- [ ] Move completed features to Completed section
- [ ] Add completion date and summary
- [ ] Delete detailed FEATURE-*.md docs (git preserves history)

### 4. Priority Review

- [ ] High touch count features → consider Active
- [ ] Stale Active features → consider Backlog
- [ ] Blocking features → escalate

---

## Feature Entry Template

```markdown
#### F##: Feature Name
**Status:** Proposed | Active | Backlog
**Touches:** N (latest: YYYY-MM-DD)
**Effort:** Quick win | Path A (20-30 min) | Path B (1-2 hours) | Path C (2+ hours)
**Priority:** High | Medium | Low
**Detail:** [docs/features/FEATURE-name.md](features/FEATURE-name.md) (if exists)
**Source:** Where this came from (user feedback, retro, notes)

Brief description of the feature.
```

---

## Notes Processing Workflow

When processing raw notes (misc-notes.md, presentation-notes.md, etc.):

1. **Read the notes file**
2. **Categorize each item:**
   - Already tracked → update existing feature (increment touch)
   - New actionable → create new feature entry
   - Context/archive only → note in feature if relevant, or discard
3. **Update FEATURES.md** with new/updated entries
4. **Delete the notes file** (content extracted)

---

## Future: Skill Evolution

This document is a prototype for a future skill that can:
- Automatically suggest touch counter updates during conversation
- Prompt for backlog refinement periodically
- Generate priority reports based on touch frequency
- Track feature velocity (time from proposed to completed)
