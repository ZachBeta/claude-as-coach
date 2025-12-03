# F31: Git History Squash & Personal Data Audit

**Status:** Active - High priority
**Effort:** Path B (1-2 hours for audit + squash + verification)
**Priority:** High - BLOCKING for sharing repo with acquaintances before presentation
**Created:** 2025-12-01

## Problem Statement

**Current blocker:**
- Git history may contain personal health data from early commits
- Cannot share repo with friends/acquaintances who want to try system before Dec 12th presentation
- Need to audit all files and clean history before making repo accessible to others

**Risk:**
- Personal health information in git history
- Sensitive data in file paths, commit messages, or file contents
- Must be cleaned before sharing with anyone outside of maintainer

## Goal

Create a clean, shareable version of the repository with:
1. No personal data in current files
2. No personal data in git history
3. Proper MIT license
4. Clean single commit or minimal commit history
5. Safe to share with friends for pre-presentation testing

## Implementation Plan

### Phase 1: Audit Current Files (30-45 min)

**Systematic file review:**

```bash
# Search for potentially sensitive patterns
rg -i "health|recovery|symptom|LC|long covid|PEM|crash" --type md
rg -i "ketone|glucose|sleep|HRV" --type md
rg -i "connecticut|EST|timezone" --type md
```

**Files to audit:**

**Base skills (should be clean):**
- [ ] `skills/daily-summary-base/SKILL.md`
- [ ] `skills/daily-morning-routine-base/SKILL.md`
- [ ] `skills/weekly-planning-base/SKILL.md`
- [ ] `skills/weekly-retrospective-base/SKILL.md`
- [ ] `skills/project-coach-setup-base/SKILL.md`

**Documentation (should be clean):**
- [ ] `README.md`
- [ ] `PROJECT-SETUP.md`
- [ ] `QUICKSTART.md`
- [ ] `CLAUDE.md`
- [ ] `docs/WORKFLOW-GUIDE.md`
- [ ] `docs/FEATURES.md`
- [ ] `docs/CHANGELOG.md`
- [ ] `docs/features/FEATURE-*.md` (all feature docs)

**Examples (should use Alice/Rob/Sally only):**
- [ ] `personal.example/` - Should contain NO personal data, only fictional personas

**Private submodule (should be excluded):**
- [ ] Verify `personal/` is a submodule and won't be included
- [ ] Verify `.gitmodules` correctly references private repo

**Scripts:**
- [ ] `scripts/skill_workflow.py` - Check for hardcoded paths

**Config files:**
- [ ] `.gitignore` - Review patterns
- [ ] `.gitmodules` - Verify personal/ points to private repo

**Known safe patterns to keep:**
- "Connecticut/EST timezone" → Already changed to "user's timezone" in base skills
- Alice/Rob/Sally personas → Fictional, safe
- Couch-to-5K, interview prep → Generic domains, safe

**Checklist per file:**
- [ ] No personal health information
- [ ] No real names (except maintainer in LICENSE/README)
- [ ] No specific location details beyond generic examples
- [ ] No private metrics or thresholds
- [ ] Uses fictional personas only (Alice, Rob, Sally)

---

### Phase 2: Plan Git History Strategy (15 min)

**Option A: Single squashed commit (RECOMMENDED)**

Pros:
- Complete history reset
- Guaranteed no leaks
- Clean slate for public repo
- Simple to verify

Cons:
- Loses all commit history
- Can't reference specific changes

**Implementation:**
```bash
# Backup current repo first
cd ..
cp -r claude-as-coach claude-as-coach-backup

cd claude-as-coach

# Create orphan branch with clean history
git checkout --orphan clean-history

# Stage all current files
git add -A

# Create single initial commit
git commit -m "Initial commit: Claude-as-Coach framework

Claude Projects skills system for sustainable goal tracking and coaching.

Features:
- Base skill frameworks (daily summaries, weekly planning/retros)
- Personal skill extension pattern
- Fractal compression (daily→weekly→monthly)
- Demo personas: Rob (couch-to-5K), Sally (interview prep)

MIT License
https://github.com/ZachBeta/claude-as-coach"

# Replace main branch
git branch -D main
git branch -m main

# Verify clean state
git log --oneline  # Should show single commit
```

**Option B: Preserve recent clean commits (ALTERNATIVE)**

Pros:
- Keeps some development history
- Shows recent work evolution

Cons:
- More complex to verify safety
- Risk of missed personal data in middle commits

**Implementation:**
```bash
# Interactive rebase from first clean commit
git rebase -i <first-clean-commit-hash>

# In editor: squash all commits before that point
# Then audit each remaining commit message and diff
```

**Recommendation:** Option A (single squash) - simpler and safer

---

### Phase 3: Execute Git Squash (15-20 min)

**Pre-squash checklist:**
- [ ] Phase 1 audit complete (no personal data in current files)
- [ ] Backup created (`claude-as-coach-backup/`)
- [ ] All current work committed to main
- [ ] Clean working directory (`git status` clean)

**Execution steps:**

```bash
# 1. Verify clean state
git status  # Must be clean

# 2. Create backup branch
git branch pre-squash-backup

# 3. Create orphan branch
git checkout --orphan clean-history

# 4. Stage all files
git add -A

# 5. Verify what will be committed
git status

# 6. Review files to be committed (look for anything missed)
git diff --cached --stat

# 7. Create single commit with comprehensive message
git commit -m "Initial commit: Claude-as-Coach framework

[Detailed commit message - see above]"

# 8. Verify single commit
git log --oneline

# 9. Replace main
git branch -D main
git branch -m main

# 10. Verify result
git log --graph --oneline --all
```

**Safety net:**
- Backup branch `pre-squash-backup` preserved
- Full repo backup in `../claude-as-coach-backup/`
- Can rollback if needed: `git branch -D main && git checkout pre-squash-backup && git branch -m main`

---

### Phase 4: Verification & Testing (20-30 min)

**Verify clean history:**

```bash
# Check commit count
git log --oneline  # Should show 1 commit

# Check commit message
git log --format=full

# Check no references to personal data in commit
git log --all --source --full-history -S "personal-keyword" # Try various keywords

# Verify submodule configuration
git submodule status
cat .gitmodules  # Should point to private personal/ repo
```

**Verify current files:**

```bash
# Search for any personal data patterns that might have been missed
rg -i "sensitive-keyword" --type md
rg -i "health|recovery|symptom" --type md

# Check skills directory
ls -la skills/
cat skills/*/SKILL.md  # Quick scan for personal content

# Check docs
ls -la docs/
rg -i "personal" docs/ --type md  # Should only find references to "personal skills"
```

**Test fresh clone:**

```bash
# Clone to temporary location
cd /tmp
git clone /Users/zmorek/workspace/ZachBeta/studies_and_etudes/claude-as-coach claude-test

cd claude-test

# Verify structure
ls -la
cat README.md
cat PROJECT-SETUP.md

# Check git history
git log --oneline

# Verify personal/ is NOT included (should be empty or not present)
ls -la personal/ 2>/dev/null || echo "personal/ correctly not included"

# Test skill workflow
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Verify no personal data
rg -i "sensitive-pattern" .

# Clean up
cd ..
rm -rf claude-test
```

**Fresh user simulation:**

Create a checklist as if you're a new user:
- [ ] Can read README.md and understand project
- [ ] Can follow PROJECT-SETUP.md or QUICKSTART.md
- [ ] No personal information visible
- [ ] Skills are generic/example-based
- [ ] No confusion about what's real vs example

---

### Phase 5: Add MIT License (10 min)

**Create LICENSE file:**

```bash
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2025 Zach Morek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

git add LICENSE
git commit --amend --no-edit  # Add to initial commit
```

**Update README.md with license:**

Add at bottom:
```markdown
## License

MIT License - see [LICENSE](LICENSE) file for details
```

---

### Phase 6: Share with Test Users (Optional Pre-Presentation)

**Before sharing:**
- [ ] All phases above complete
- [ ] Final verification passed
- [ ] README.md updated with sharing instructions
- [ ] Personal data audit complete

**Sharing options:**

**Option A: Private preview (recommended for acquaintances):**
```bash
# Create private GitHub repo
# Add acquaintances as collaborators
git remote add origin https://github.com/ZachBeta/claude-as-coach-private
git push -u origin main
```

**Option B: ZIP file share:**
```bash
# Create clean ZIP
cd ..
zip -r claude-as-coach.zip claude-as-coach \
  -x "*.git*" \
  -x "*personal/*" \
  -x "*.DS_Store"

# Share via email/drive
```

**Option C: Public GitHub (post-Dec 12th):**
```bash
# Make repo public after presentation
# Full open source release
```

---

## Known Files with Personal Data (To Be Cleaned)

**Files to verify or remove before squash:**

1. **Early commit messages** - May reference personal health details
2. **Historical versions of skills** - Before base/personal separation
3. **File paths in git history** - `personal/` files that were tracked before submodule

**Search strategy:**
```bash
# Audit all commit messages
git log --all --oneline --grep="health\|recovery\|symptom" -i

# Audit all file paths ever tracked
git log --all --name-only --pretty=format: | sort -u | grep -i personal

# Audit all diff content (expensive but thorough)
git log --all --source --full-history -S "sensitive-keyword" --pretty=format:"%h %s"
```

---

## Rollback Plan

**If something goes wrong:**

```bash
# Option 1: Restore from backup branch
git branch -D main
git checkout pre-squash-backup
git branch -m main

# Option 2: Restore from backup directory
cd ..
rm -rf claude-as-coach
cp -r claude-as-coach-backup claude-as-coach
cd claude-as-coach

# Option 3: Restore specific commit
git reflog  # Find commit hash before squash
git reset --hard <commit-hash>
```

**Reflog preservation:**
- Git reflog keeps references for ~90 days
- Even after branch deletion, commits are recoverable
- `git fsck --lost-found` can recover orphaned commits

---

## Testing Checklist

**Before considering done:**

- [ ] Phase 1: All files audited, no personal data found
- [ ] Phase 2: Strategy selected (Option A recommended)
- [ ] Phase 3: Git squash executed successfully
- [ ] Phase 4: Fresh clone test passed
- [ ] Phase 5: MIT LICENSE added
- [ ] Backup preserved (`pre-squash-backup` branch + directory backup)
- [ ] No sensitive keywords found: `rg -i "health|recovery|symptom|ketone|glucose|LC" .`
- [ ] Personal submodule correctly excluded
- [ ] README.md updated for public consumption
- [ ] Fresh user simulation passed (can understand and use repo)

---

## Success Criteria

**Safe to share when:**
1. ✅ No personal health data in any tracked files
2. ✅ No personal data in git history (single clean commit or verified clean commits)
3. ✅ MIT license in place
4. ✅ Fresh clone contains no personal information
5. ✅ Documentation is clear for new users
6. ✅ Example personas are fictional (Alice, Rob, Sally)
7. ✅ Base skills use generic placeholders
8. ✅ `personal/` submodule correctly separated

**Evidence:**
- Fresh clone reviewed by uninvolved party shows no personal data
- String searches for sensitive keywords return no results
- Git history contains no references to personal health details
- README clearly states "example personas are fictional"

---

## Timeline

**Target completion:** Before sharing with first acquaintance (ASAP)

**Estimated time breakdown:**
- Phase 1 (Audit): 30-45 min
- Phase 2 (Planning): 15 min
- Phase 3 (Squash): 15-20 min
- Phase 4 (Verification): 20-30 min
- Phase 5 (License): 10 min
- **Total: 1.5-2 hours**

**Blocking for:**
- Sharing repo with acquaintances for pre-presentation feedback
- Open source release (post-Dec 12th)
- Public GitHub repository

**Not blocking:**
- Dec 12th presentation (can demo from private repo)
- Personal daily usage (already working)

---

## Notes

**Why single squash is safer:**
- Git history is complex - easy to miss personal data in middle commits
- Single commit eliminates all risk from history
- Commit message can be carefully crafted
- Future commits will be clean by design (base/personal separation established)

**Why this is high priority:**
- Enables pre-presentation user testing with acquaintances
- Gets real feedback before Dec 12th
- Validates PROJECT-SETUP.md and QUICKSTART.md with fresh eyes
- Builds confidence that system is actually usable by others

**Post-squash development:**
- All future commits will be on clean main branch
- Base skills remain generic (already separated)
- Personal skills stay in private submodule
- Safe to share ongoing work

---

## Open Questions

**Q1: Should we squash now or wait until after Dec 12th?**
- Now: Enables pre-presentation testing with acquaintances
- After: Less time pressure, but delays user feedback

**Q2: Single commit or preserve some recent clean commits?**
- Single: Safest, simplest to verify
- Preserve: Some history, but requires careful audit

**Q3: Private GitHub repo or ZIP file for acquaintances?**
- Private repo: Easy collaboration, can push updates
- ZIP file: Simpler, no GitHub account needed

**Q4: Should we announce squash in commit message?**
- Yes: "This repo was created from a private development repo with history squashed to remove personal data"
- No: Just treat as initial commit

---

## Related Features

- **F17 Task 6:** This feature expands on presentation prep git squash task
- **F28, F29:** Demo personas must be complete and verified fictional before squash
- **F26:** Monthly rollup should use sanitized example, not real personal data

---

## Appendix: Sensitive Pattern Search Commands

**Comprehensive search for personal data:**

```bash
# Health-related terms
rg -i "health|recovery|symptom|diagnosis|medical|doctor|physician" .

# LC-specific terms
rg -i "long covid|LC|PEM|crash|post-exertional" .

# Metrics
rg -i "ketone|glucose|HRV|heart rate variability|sleep score" .

# Location
rg -i "connecticut|EST|eastern time" .

# Personal protocols (from actual use)
rg -i "bootstrap|honey|lite salt|feed protocol" .

# File paths
git log --all --name-only --pretty=format: | sort -u | grep -i personal

# Commit messages
git log --all --oneline | grep -i "health\|recovery\|symptom"
```

**If any matches found:**
- Review context
- Determine if personal or generic
- Clean if personal, preserve if generic example
