# Skill Format Testing Results

**Date:** 2025-12-02
**Tester:** [Your name]
**Test Files:** `test/format-a-flat/` and `test/format-b-nested/`

## Background

There is a discrepancy between Claude.ai's upload UI and the official documentation:

**UI Upload Dialog** shows:
> "ZIP file that includes exactly one SKILL.md file at the root level"

**Official Documentation** (https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) shows:
> Correct format:
> ```
> my-Skill.zip
> └── my-Skill/
>     ├── Skill.md
>     └── resources/
> ```

This testing validates which format is actually required/preferred.

---

## Test Results

### Format A: Flat Structure (UI Format)

**File:** `test/format-a-flat/daily-summary-base.zip`

**Structure:**
```
daily-summary-base.zip
└── SKILL.md
```

**Upload Test:**
- [x] Uploaded successfully
- [x] Shows in skills list
- [x] Triggers correctly when invoked
- [x] No warnings or errors

**Notes:**
Works perfectly. Claude.ai accepts this format without issues.

---

### Format B: Nested Structure (Documentation Format)

**File:** `test/format-b-nested/daily-summary-base.zip`

**Structure:**
```
daily-summary-base.zip
└── daily-summary-base/
    └── SKILL.md
```

**Upload Test:**
- [x] Uploaded successfully
- [x] Shows in skills list
- [x] Triggers correctly when invoked
- [x] No warnings or errors

**Notes:**
Also works perfectly. Claude.ai accepts this format without issues.

---

## Findings

### Which Format Works?

- [x] Both formats work identically
- [ ] Only Format A (flat) works
- [ ] Only Format B (nested) works
- [ ] Neither works (unexpected)

### Observations

**Behavior differences:**
None observed. Both formats work identically in Claude.ai.

**UI feedback:**
No differences in upload UI or skill invocation between formats.

**Error messages (if any):**
None for either format.

---

## Recommendation

### Both Formats Work - Follow Official Documentation

**Recommended approach:** Nested structure (Format B)

**Rationale:**
1. **Official documentation** explicitly shows nested structure as correct format
2. **Consistency** with Anthropic's official guidance
3. **Vendor alignment** - anthropics/skills repo uses nested structure
4. **Future-proofing** - if Claude.ai tightens validation, nested format will remain supported
5. **Community expectations** - developers following docs expect nested structure

**Decision:** Update pack_skill.py to create nested structure matching official docs.

---

## Impact on Repository

### pack_skill.py Changes Needed?

- [ ] No changes needed (current implementation correct)
- [x] Update to create nested structure
- [ ] Add flag to support both formats

**Action:** Change line in pack_skill.py from:
```python
arcname = file_path.relative_to(skill_dir)
```
to:
```python
arcname = Path(skill_dir.name) / file_path.relative_to(skill_dir)
```

### Documentation Updates Needed?

- [x] Clarify which format is preferred (nested per official docs)
- [x] Update all examples to match canonical format
- [ ] Add troubleshooting section for format issues (defer)

### Vendor Repo PR?

- [ ] Propose changes to vendor implementation
- [ ] File issue about format discrepancy
- [x] No action needed - vendor already uses nested structure correctly

---

## References

- Upload UI: [Screenshot showing "SKILL.md at root level"]
- Official Docs: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Test Script: `scripts/test_both_formats.py`
- Our Implementation: `scripts/pack_skill.py`
