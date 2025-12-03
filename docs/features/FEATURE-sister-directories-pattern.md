# F33: Sister Directories Pattern Validation

**Status:** Active - Architecture validation
**Effort:** Quick win (30-45 min for testing + decision)
**Priority:** High - BLOCKING F31 (git history squash)
**Created:** 2025-12-02

## Problem

Need to finalize the architecture for separating public base skills from private personal data before squashing git history (point of no easy return).

**Two patterns under consideration:**
1. **Submodule pattern** (original) - `personal/` as git submodule inside main repo
2. **Sister directories pattern** (current) - `claude-as-coach/` and `claude-as-coach-personal/` as sibling repos

**Current state:** Sister directories pattern implemented in code and docs (2 commits, 2025-12-01) but **not validated in practice**.

## Critical Unknowns (Must Resolve)

### 1. CLAUDE.md Auto-Loading (CRITICAL - Make or Break)
**Question:** If Claude Code runs from `claude-as-coach-combined/`, does it auto-load `claude-as-coach/CLAUDE.md`?

**Why it matters:** CLAUDE.md contains operational guidance for Claude Code. If it doesn't load, the guidance system breaks.

**Test:** Start Claude Code from parent workspace, check if child CLAUDE.md is accessible.

### 2. Path Complexity
**Question:** Do longer paths (`claude-as-coach/skills/...`) add enough friction to outweigh git simplicity benefits?

**Test:** Try typical operations from parent vs child directory, measure cognitive load.

### 3. Working Directory Dissonance
**Question:** Where should users actually work day-to-day?

**Current docs show mixed signals:**
- CLAUDE.md: "Run from parent workspace"
- WORKFLOW-GUIDE.md: Mix of parent and child context examples
- README.md: "Run from parent" but examples assume child context

## Decision Criteria

### Must-Have Requirements (Non-Negotiable)
1. ✅ CLAUDE.md must auto-load when using Claude Code
2. ✅ Both base and personal accessible in same session
3. ✅ Personal data kept private (separate git repo)
4. ✅ Base skills shareable (public repo)

### Success Metrics by User Type

**Maintainer (n=1):**
- Can work on both repos efficiently
- Claude Code works smoothly
- Willing to tolerate some complexity if it helps others

**Contributors (n=10):**
- Can clone and start contributing in < 5 minutes
- Don't need to understand personal repo pattern
- Clear documentation for setup

**Adopters (n=100):**
- Can set up their own personal repo in < 15 minutes
- Clear separation of example vs their data
- Foolproof instructions

## Testing Plan

### Phase 1: Critical Test (15 minutes) - GO/NO-GO Decision Point

**Test CLAUDE.md loading:**
```bash
# Exit current Claude Code session
# Start new session from parent:
cd /Users/zmorek/workspace/ZachBeta/studies_and_etudes/claude-as-coach-combined
claude

# In new session, test:
1. "What does CLAUDE.md say about this workspace?"
   → Should describe parent workspace structure
2. "What does @claude-as-coach/CLAUDE.md say about working directories?"
   → Tests if @-reference loads detailed guidance
3. "Where should I run Claude Code from?"
   → Should confirm parent directory
```

**Success criteria:**
- ✅ Parent CLAUDE.md loads automatically
- ✅ @-reference to child CLAUDE.md works
- ✅ Claude understands workspace structure

**If test FAILS:** Sister directories pattern is NOT viable (revert to submodules)
**If test SUCCEEDS:** Proceed to Phase 2

### Phase 2: Path Complexity Evaluation (10 minutes)

**Test typical operations from parent workspace:**
```bash
cd claude-as-coach-combined

# Try operations with longer paths:
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/
vim claude-as-coach/skills/weekly-planning/SKILL.md
cd claude-as-coach && git status && cd ..

# Compare to operations from child:
cd claude-as-coach
python scripts/skill_workflow.py pack skills/daily-summary-base/
vim skills/weekly-planning/SKILL.md
git status
```

**Evaluation questions:**
- Does parent workspace add enough value to justify longer paths?
- Is it clear which repo git commands affect?
- Is daily workflow more or less friction?

### Phase 3: Final Decision (5 minutes)

**Apply decision matrix:**

|  | Submodule | Sister Dirs |
|---|-----------|-------------|
| CLAUDE.md loads? | ✅ Yes | [Test Result] |
| Path simplicity | ✅ Short paths | ❌ Long paths |
| Git simplicity | ❌ Two-step commit | ✅ Independent |
| Contributor setup | ✅ One clone | 🤔 Parent dir setup |
| Adopter setup | 🤔 Submodule swap | ✅ Simple clone |
| Maintainer workflow | 🤔 Two-step commit | ✅ Independent |
| Documentation clarity | ✅ Clear | ❌ Complex |
| "Scary" factor | ❌ Intimidating | ✅ Familiar |

**Decision:**
- If sister directories passes Phase 1 + provides clear benefits → Keep it
- If sister directories fails Phase 1 OR adds too much friction → Revert to submodules

### Phase 4: Documentation Cleanup (15-30 minutes)

**If keeping sister directories:**
1. Verify all 9 docs are accurate and consistent
2. Resolve working directory dissonance (pick one: parent or child as default)
3. Move parent CLAUDE.md sample to `docs/examples/`
4. Update PROJECT-SETUP.md with clear setup instructions
5. Add testing results to DECISION-PERSONAL-REPO-PATTERN.md

**If reverting to submodules:**
1. Reset git: `git reset --hard a0963e8` (before submodule removal)
2. Restore submodule documentation
3. Update CLAUDE.md to clarify submodule pattern benefits
4. Re-add personal/ submodule
5. Update DECISION doc with test results and rationale

## Current State (2025-12-02)

**Git status:**
- Branch: main
- Commits ahead of origin: 9
- Working tree: Clean

**Commits implementing sister directories:**
- `6b78443` - Remove personal/ submodule - use sister directories pattern
- `4d2d599` - Update documentation for sister directories pattern

**Easy revert path:** `git reset --hard a0963e8` (commit before submodule removal)

**Documentation already updated (9 files):**
- README.md (structure, clone instructions, workflows)
- CLAUDE.md (directory structure, operational guidance)
- WORKFLOW-GUIDE.md (all personal file workflows, setup)
- PROJECT-SETUP.md (personal skills directory structure)
- DECISION-PERSONAL-REPO-PATTERN.md (comprehensive analysis)
- Plus feature docs referencing the pattern

**Parent CLAUDE.md exists:** `/claude-as-coach-combined/CLAUDE.md`
- Intentionally minimal
- Points to child CLAUDE.md for detailed guidance
- Uses @-reference syntax

## Blocking

**F31: Git History Squash** - Cannot squash git history until personal repo pattern is finalized. Git history squash is a point of no easy return.

## Next Steps

1. **Test CLAUDE.md loading** (Phase 1) - This session or fresh session
2. **Evaluate path complexity** (Phase 2) - If Phase 1 succeeds
3. **Make final decision** (Phase 3) - Apply decision matrix
4. **Clean up documentation** (Phase 4) - Stabilize all docs
5. **Unblock F31** - Proceed with git history squash

## Open Questions

1. Is the "submodules are scary" reputation real or overblown?
2. What's the actual pain point we're solving? (Two-step commit for maintainer? Perceived complexity for contributors? Setup friction for adopters?)
3. Can we test actual user flows with someone unfamiliar?
4. Is there a hybrid approach?

## Files Referenced

- DECISION-PERSONAL-REPO-PATTERN.md (comprehensive decision framework)
- README.md, CLAUDE.md, WORKFLOW-GUIDE.md, PROJECT-SETUP.md (updated for sister dirs)
- /claude-as-coach-combined/CLAUDE.md (parent workspace guidance)

## Timeline

**Target:** Complete validation and decision before continuing with F31 (git history squash)

**Estimate:** 30-45 minutes total (15 min test + 10 min eval + 5 min decision + 15-30 min cleanup)
