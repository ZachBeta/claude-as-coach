# Onboarding Approaches Test Matrix

Testing different ways for users to set up Claude-as-Coach skills.

## The Problem

Current onboarding (QUICKSTART.md) requires:
1. Download 5 .zip files
2. Navigate to Settings > Capabilities > Skills
3. Upload each file
4. Create project
5. Start using

This is clunky. Can we simplify?

## Three Approaches to Test

| Approach | File | Lines | Method | Fidelity |
|----------|------|-------|--------|----------|
| **Simple** | `bootstrap-simple.md` | ~250 | skill-creator packages | Condensed |
| **Complex** | `bootstrap-complex.md` | ~1270 | skill-creator packages | Full |
| **With ZIPs** | `bootstrap-with-zips.md` | ~60 | Pre-built .zip files | Exact |

### 1. Bootstrap Simple (`bootstrap-simple.md`)

- Condensed version of all 5 skills
- User pastes into fresh project chat
- Says "use skill-creator to package these"
- Claude creates .zip artifacts
- User uploads artifacts as skills

**Pros:** Single paste, no external downloads
**Cons:** Relies on skill-creator, skills may differ from originals

### 2. Bootstrap Complex (`bootstrap-complex.md`)

- Full concatenation of all 5 skills (~1270 lines)
- Same flow as Simple
- Higher fidelity to original skill content

**Pros:** Full skill content preserved
**Cons:** Large paste, still relies on skill-creator

### 3. Bootstrap With ZIPs (`bootstrap-with-zips.md`)

- Simple instructions with download links
- User downloads pre-built .zip files
- Uploads via Settings > Capabilities

**Pros:** Exact skill fidelity, tested files
**Cons:** Still requires Settings navigation, multiple downloads

## How to Test

### Test Protocol

1. Create fresh Claude.ai project
2. Use one approach to set up skills
3. Say "set up my project"
4. Verify project-coach-setup-base triggers
5. Complete setup flow
6. Test "good morning" (morning routine)
7. Test "daily summary" (daily summary)

### Success Criteria

- [ ] Skills install correctly
- [ ] Trigger phrases work
- [ ] Skill behavior matches originals
- [ ] User confusion is minimal

### Questions to Answer

1. Does skill-creator actually work for packaging skills from markdown?
2. Do condensed skills behave the same as full skills?
3. Which approach has lowest friction for new users?
4. How much does .zip vs .skill naming confuse users?

## Known Issues

### .zip vs .skill Naming Confusion

- GitHub shows files as `.zip`
- Claude.ai UI may show `.skill`
- They're the same format
- May confuse users who see both

**Mitigation:** Note this in documentation, explain they're equivalent.

## Results

_To be filled in after testing_

### Simple Approach
- Date tested:
- Tester:
- Result:
- Notes:

### Complex Approach
- Date tested:
- Tester:
- Result:
- Notes:

### With ZIPs Approach
- Date tested:
- Tester:
- Result:
- Notes:

## Recommendation

_To be determined after testing_
