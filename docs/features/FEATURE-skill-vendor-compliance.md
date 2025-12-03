# F27: Skill Vendor Compliance Review

**Status:** Active - Quality improvement
**Effort:** Path B (30-45 min per skill category)
**Priority:** Medium-High (improves presentation quality)
**Created:** 2025-12-01

## Goal

Systematically review all skills against vendor/skills/skill-creator/SKILL.md conventions to ensure quality and consistency before presentation.

## Problem

During quickstart demo testing, we discovered:
- Two weekly skills missing trigger phrases in descriptions
- Vendor conventions emphasize "concise is key" - Claude is already smart
- Need to audit all skills for:
  - Trigger phrases in `description` frontmatter
  - Unnecessary verbosity or "agent flexibility" notes
  - Line count (vendor recommends <500 lines)
  - Progressive disclosure patterns (SKILL.md body vs references/)
  - Imperative form throughout

## Vendor Conventions Reference

From `vendor/skills/skill-creator/SKILL.md`:

**Description frontmatter:**
- Must include what the skill does AND when to use it
- Include all trigger phrases
- "When to use" info belongs here, not in body (body only loads after triggering)

**Concise is key:**
- "Claude is already very smart" - only add what Claude doesn't have
- Challenge each piece: "Does Claude really need this explanation?"
- Prefer concise examples over verbose explanations
- Keep SKILL.md body under 500 lines

**Writing style:**
- Always use imperative/infinitive form
- Remove "agent flexibility" notes (Claude is already flexible)
- No README.md, INSTALLATION_GUIDE.md, etc. in skill packages

**Progressive disclosure:**
- Metadata (name + description): Always in context (~100 words)
- SKILL.md body: When skill triggers (<5k words)
- Bundled resources: As needed by Claude

## Scope

### Phase 1: Base Skills (Priority - being tested in demo)

**Files to review:**
- `skills/project-coach-setup-base/SKILL.md`
- `skills/daily-morning-routine-base/SKILL.md`
- `skills/daily-summary-base/SKILL.md`
- `skills/weekly-planning-base/SKILL.md`
- `skills/weekly-retrospective-base/SKILL.md`

**For each skill, check:**
1. ✅ Description includes trigger phrases and "when to use"
2. ✅ No unnecessary verbosity or explanations Claude already knows
3. ✅ Line count under 500 (or split to references/)
4. ✅ Imperative form throughout
5. ✅ No "agent flexibility" sections
6. ✅ No extraneous files (README, etc.)

### Phase 2: Personal Skills (Production)

**Files to review:**
- `personal/skills/daily-morning-routine-personal/SKILL.md`
- `personal/skills/daily-summary-personal/SKILL.md`
- `personal/skills/weekly-planning-personal/SKILL.md`
- `personal/skills/weekly-retrospective-personal/SKILL.md`

**Same checklist as Phase 1**

### Phase 3: Example Skills (Alice demo - future)

**Files to review:**
- `personal.example/skills/daily-morning-routine-alice-personal/SKILL.md`
- `personal.example/skills/daily-summary-alice-personal/SKILL.md`
- `personal.example/skills/weekly-planning-alice-personal/SKILL.md`
- `personal.example/skills/weekly-retrospective-alice-personal/SKILL.md`

**Defer until Alice demo content creation (F17 Task 3)**

## Workflow

For each skill in scope:

1. **Read vendor conventions** (if needed for refresh)
   ```bash
   # Reference
   cat vendor/skills/skill-creator/SKILL.md
   ```

2. **Read current skill**
   ```bash
   # Example
   cat skills/daily-summary-base/SKILL.md
   ```

3. **Validate with vendor tool**
   ```bash
   python vendor/skills/skill-creator/scripts/quick_validate.py skills/daily-summary-base/
   ```

4. **Review against checklist:**
   - [ ] Description has triggers and "when to use"
   - [ ] No verbose explanations Claude doesn't need
   - [ ] Line count reasonable (<500 preferred)
   - [ ] Imperative form throughout
   - [ ] No "agent flexibility" notes
   - [ ] No extraneous files

5. **Edit if needed**
   ```bash
   # Direct source editing (already unpacked)
   vim skills/daily-summary-base/SKILL.md
   ```

6. **Repack and commit**
   ```bash
   python scripts/skill_workflow.py pack skills/daily-summary-base/
   git add skills/daily-summary-base/SKILL.md skills/daily-summary-base.skill
   git commit -m "Improve daily-summary-base vendor compliance

   - Enhanced description with trigger phrases
   - Removed verbose explanations
   - Condensed from X to Y lines
   - Applied imperative form throughout"
   ```

7. **Upload to demo project** (if testing base skills)

## Success Criteria

**Phase 1 complete when:**
- [ ] All 5 base skills reviewed and updated
- [ ] All pass `quick_validate.py`
- [ ] Descriptions include triggers and "when to use"
- [ ] No unnecessary verbosity
- [ ] Line counts reasonable
- [ ] All changes committed

**Phase 2 complete when:**
- [ ] All 4 personal skills reviewed and updated
- [ ] Same quality standards as Phase 1
- [ ] Production skills repacked and deployed

## Estimation

**Per skill:** ~5-10 minutes review + 5-10 minutes editing if needed
**Phase 1 (5 base skills):** ~30-45 minutes
**Phase 2 (4 personal skills):** ~25-35 minutes
**Total:** ~1-1.5 hours for Phases 1 & 2

## Notes

**Already completed:**
- ✅ project-coach-setup-base: Condensed from 360 to 120 lines, added triggers (2025-12-01)
- ✅ weekly-planning-base: Added trigger phrases to description (2025-12-01)
- ✅ weekly-retrospective-base: Added trigger phrases to description (2025-12-01)

**Next:** Review remaining base skills (daily-morning-routine-base, daily-summary-base)

**Vendor validation output example:**
```
✅ Skill is valid!
```

**Key insight from quickstart testing:**
> Trigger phrases in descriptions are critical. Fresh projects can't detect skills without explicit "when to use" information in the description field.
