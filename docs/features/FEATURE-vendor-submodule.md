# FEATURE: Vendor Submodule Update Strategy

**Status:** Not yet implemented
**Effort:** Quick win (10-15 min)
**Priority:** Medium - prevents upstream conflicts

## Problem

- `vendor/skills/` submodule currently on `main` branch
- Fork of anthropics/skills may diverge from upstream
- Need strategy for incorporating upstream updates
- Want to avoid merge conflicts and maintain clean history

## Proposed Strategies

### Option A: Tracking Branch (Recommended)

```bash
# One-time setup: Add upstream remote
cd vendor/skills
git remote add upstream https://github.com/anthropics/anthropics-skills
git fetch upstream

# Create tracking branch from our fork's main
git checkout -b tracking origin/main

# Periodic updates: Rebase our fork on upstream
git fetch upstream
git rebase upstream/main
git push origin tracking --force-with-lease

# Update submodule reference in main repo
cd ../..
git add vendor/skills
git commit -m "Update vendor/skills submodule (sync with upstream)"
```

**Advantages:**
- Keeps our fork's main clean
- Easy to rebase on upstream changes
- Clear separation of upstream vs. our customizations
- Force-push only affects tracking branch, not main

### Option B: Direct Upstream Tracking

```bash
# Point submodule directly at upstream
cd vendor/skills
git remote set-url origin https://github.com/anthropics/anthropics-skills
git pull origin main

# If we need fork-specific changes, maintain separate branch
git checkout -b zachbeta-customizations
```

### Option C: Periodic Manual Sync

```bash
# Keep current setup, manually sync when needed
cd vendor/skills
git remote add upstream https://github.com/anthropics/anthropics-skills
git fetch upstream
git merge upstream/main  # or rebase
git push origin main
```

## Recommendation

**Option A (tracking branch)** - Best balance of upstream sync and customization flexibility.

## Implementation Plan

- [ ] Decide on strategy (Option A recommended)
- [ ] Update `.gitmodules` with branch tracking configuration
- [ ] Add "Updating vendor/skills" section to WORKFLOW-GUIDE.md
- [ ] Document setup instructions in README.md
- [ ] Test upstream sync process
- [ ] Verify no merge conflicts in main repo

## Documentation Needed

- Add to WORKFLOW-GUIDE.md: "Updating vendor/skills"
- Document in README.md: Setup instructions
- Add to .gitmodules: Branch tracking configuration

## Acceptance Criteria

- [ ] Strategy decided and documented
- [ ] `.gitmodules` updated with branch tracking
- [ ] WORKFLOW-GUIDE.md includes vendor update instructions
- [ ] Successfully tested upstream sync
- [ ] No merge conflicts in main repo
