# Next Session

**Last Updated:** 2025-12-19
**Purpose:** Single source of truth for next coding session

---

## Immediate Priority

### F39: Summary Skill Date Drift Fix
**Effort:** Quick win (20-30 min)
**Status:** Implementation ready

**Problem:** Daily summary skill gets confused when run the next morning - drifts back to "today" instead of the date being summarized.

**Fix:** Add explicit SUMMARY_DATE vs TODAY distinction throughout skill.

**Files to modify:**
- `skills/daily-summary-base/SKILL.md`

**Success criteria:**
- Skill explicitly distinguishes between "today" (when running) and "summary date" (the date being summarized)
- Running "daily summary" the next morning correctly defaults to yesterday

---

## If Time Permits

### F48: Project Description Template Enhancement
**Effort:** Quick win (15-20 min)

Add Quick Reference section to Project-Goals.md template:
```
Daily: gm, daily summary
Weekly: weekly retro, weekly planning
Workflow: Morning -> Summary -> Save -> New chat
```

**Files:** `skills/project-coach-setup-base/SKILL.md`

### F45: Safety Disclaimers
**Effort:** Quick win (30-45 min)

Add safety disclaimers to:
- README.md
- PROJECT-SETUP.md
- QUICKSTART.md
- Base skills

See [features/FEATURE-safety-disclaimers.md](features/) for proposed language.

---

## Still Pending

- F46: Skill Improvements (Retro & Planning) - 1-2 hours
- F47: Onboarding UX Audit - 1-2 hours
- F27: Skill Vendor Compliance Review - ongoing

---

## Reference Commands

```bash
# Pack skill after editing
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Pack all base skills
for skill in skills/*-base; do
  python scripts/skill_workflow.py pack "$skill/"
done
```

---

## Related Features

- [F39: Summary Date Drift](features/FEATURE-summary-date-drift.md) - Primary
- [F48: Project Description Template](features/FEATURE-project-description-template.md) - Secondary
- [F45: Safety Disclaimers](features/) - Secondary
- [F46: Skill Improvements](features/FEATURE-skill-improvements-retro-planning.md) - Deferred
