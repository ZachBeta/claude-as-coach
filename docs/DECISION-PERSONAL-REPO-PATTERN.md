# Decision: Personal Repo Pattern (Submodule vs Sister Directories)

**Status:** PAUSED - Need to resolve critical unknowns before proceeding with git history squash

**Date:** 2025-12-01 (Updated: 2025-12-02)

**Tracking:** Validation work tracked in **F33: Sister Directories Pattern Validation** (see [docs/features/FEATURE-sister-directories-pattern.md](features/FEATURE-sister-directories-pattern.md))

**Parent CLAUDE.md sample:** Available at [docs/examples/parent-workspace-CLAUDE.md](examples/parent-workspace-CLAUDE.md)

**Context:** Preparing repository for public release (Dec 12th presentation). Need to decide how to handle separation of public base skills from private personal extensions.

---

## The Core Problem

We need to:
1. **Separate** public base skills from private personal data (health metrics, etc.)
2. **Keep both accessible** to Claude Code in same session (for development workflow)
3. **Make it easy** for contributors to work on base skills (n=10)
4. **Make it easy** for adopters to set up their own personal repos (n=100)

---

## Two Patterns Under Consideration

### Pattern A: Submodule (original architecture)

```
claude-as-coach/              # Working directory for Claude Code
  ├── CLAUDE.md               # ← Claude Code auto-loads this
  ├── skills/                 # Base skills (public)
  ├── personal/               # Submodule → private repo
  │   ├── documents/          # Personal data
  │   └── skills/             # Personal skill extensions
  ├── vendor/skills/          # Submodule → anthropics/skills
  └── scripts/
```

**Git operations:**
```bash
# Contributor (working on base skills only):
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach
# personal/ submodule is initialized but they never touch it

# Adopter (creating their own personal repo):
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach
cd personal
git remote set-url origin https://github.com/THEIR-USERNAME/their-personal-repo
# Or: rm -rf personal && git clone their-personal-repo personal

# Maintainer (you - working on both):
cd personal
git add documents/Summary-2025-12-01.md
git commit -m "Add summary"
git push origin main
cd ..
git add personal  # Update submodule reference
git commit -m "Update personal submodule"
```

**Pros:**
- ✅ CLAUDE.md auto-loads (in working directory root)
- ✅ Simple paths: `personal/skills/foo.skill`
- ✅ Both repos accessible in one Claude Code session
- ✅ Well-documented pattern (established Git feature)
- ✅ Contributors can ignore personal/ entirely
- ✅ `personal.example/` provides clear template

**Cons:**
- ❌ Two-step commit for personal changes (commit + update reference)
- ❌ "Submodules are complex" reputation (may intimidate newcomers)
- ❌ Requires `--recurse-submodules` flag (easy to forget)
- ❌ Submodule reference drift (if you forget `git add personal`)

**Complexity level:**
- Contributor: LOW (just clone with flag, ignore personal/)
- Adopter: MEDIUM (need to understand how to swap submodule remote)
- Maintainer: MEDIUM-HIGH (two-step commit workflow)

---

### Pattern B: Sister Directories (what we just switched to)

```
claude-as-coach-combined/     # Working directory for Claude Code?
  ├── claude-as-coach/        # Public repo
  │   ├── CLAUDE.md           # ← Will this auto-load?? UNKNOWN
  │   ├── skills/
  │   └── scripts/
  └── claude-as-coach-personal/  # Private repo (sibling)
      ├── documents/
      └── skills/
```

**Git operations:**
```bash
# Contributor (working on base skills only):
mkdir claude-as-coach-combined
cd claude-as-coach-combined
git clone https://github.com/ZachBeta/claude-as-coach
cd claude-as-coach
# Work here, no personal/ to deal with

# Adopter (creating their own personal repo):
mkdir claude-as-coach-combined
cd claude-as-coach-combined
git clone https://github.com/ZachBeta/claude-as-coach
git clone https://github.com/THEIR-USERNAME/their-personal-repo claude-as-coach-personal
# OR: cp -r claude-as-coach/personal.example claude-as-coach-personal && cd claude-as-coach-personal && git init

# Maintainer (you - working on both):
cd claude-as-coach-personal
git add documents/Summary-2025-12-01.md
git commit -m "Add summary"
git push origin main
# No cross-repo reference update needed
```

**Pros:**
- ✅ Simpler git operations (no submodule reference updates)
- ✅ Repos completely independent
- ✅ No "submodule complexity" reputation issue

**Cons:**
- ❌ **CRITICAL UNKNOWN:** Does CLAUDE.md auto-load from child directory?
- ❌ Longer paths everywhere: `claude-as-coach/skills/foo.skill`
- ❌ Need to create parent directory (extra setup step)
- ❌ Unclear which directory is "working directory"
- ❌ Documentation becomes more complex (relative paths from workspace root)

**Complexity level:**
- Contributor: MEDIUM (need to understand parent workspace concept)
- Adopter: MEDIUM (need to set up parent workspace + two repos)
- Maintainer: LOW (simple independent commits)

---

## Critical Unknowns (MUST RESOLVE)

### 1. CLAUDE.md Auto-Loading Behavior

**Question:** If Claude Code runs from `claude-as-coach-combined/`, does it auto-load `claude-as-coach/CLAUDE.md`?

**Why it matters:** CLAUDE.md contains operational guidance for Claude. If it doesn't load, the whole guidance system breaks.

**How to test:**
```bash
# Test 1: Current state (from claude-as-coach/)
cd claude-as-coach
claude
# Ask Claude: "What does CLAUDE.md say about working directories?"
# ✅ Works (confirmed - this session loaded it)

# Test 2: From parent workspace
cd claude-as-coach-combined
claude
# Ask Claude: "What does CLAUDE.md say about working directories?"
# ❓ Unknown - need to test

# Test 3: With @-reference
cd claude-as-coach-combined
claude
# Say: "@claude-as-coach/CLAUDE.md - what are the operational guidelines?"
# ❓ Unknown - does @-reference work for child directories?
```

**Decision criteria:**
- If CLAUDE.md auto-loads from child: Sister directories viable
- If CLAUDE.md does NOT auto-load: Sister directories NOT viable (dealbreaker)
- If @-reference works: Workable but requires user to know about it

### 2. Claude Code Working Directory Semantics

**Question:** Where should Claude Code actually run from?

**Current reality:** Running from `claude-as-coach/` (this session)

**Documented approach:** Running from `claude-as-coach-combined/` (parent workspace)

**Why it matters:** Affects all path references, tool invocations, git commands

**Need to validate:**
- Does running from parent make workflows easier or harder?
- Can we use relative paths cleanly from parent?
- Does it cause confusion with which repo git commands affect?

### 3. Contributor Experience

**Question:** Does submodule complexity actually hurt contributors?

**Scenarios to consider:**

**Contributor A (just wants to add a feature to base skill):**
```bash
# Submodule approach:
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach
cd claude-as-coach
# Edit skills/weekly-planning/SKILL.md
git add skills/weekly-planning/
git commit -m "Add feature"
git push origin feature-branch
# ✅ Simple - they never touch personal/

# Sister directories approach:
mkdir claude-as-coach-combined
cd claude-as-coach-combined
git clone https://github.com/ZachBeta/claude-as-coach
cd claude-as-coach
# Edit skills/weekly-planning/SKILL.md
git add skills/weekly-planning/
git commit -m "Add feature"
git push origin feature-branch
# ✅ Also simple, but extra parent directory setup
```

**Is there a real difference?** Maybe not for contributors who just want to PR base skills.

**Contributor B (wants to run Claude Code to test changes):**
```bash
# Submodule approach:
cd claude-as-coach
claude
# ✅ Works immediately, CLAUDE.md loads

# Sister directories approach:
cd claude-as-coach-combined  # ← Do they need to do this?
claude
# ❓ Does CLAUDE.md load?
```

**Need to test:** Can contributors effectively use Claude Code with each pattern?

### 4. Adopter Experience

**Question:** Which pattern makes it easier for someone to adopt the system for their own use?

**Adopter workflow (create their own personal repo):**

**Submodule approach:**
```bash
git clone --recurse-submodules https://github.com/ZachBeta/claude-as-coach
cd claude-as-coach/personal
# Option A: Reinit as new repo
rm -rf .git
git init
git remote add origin https://github.com/THEM/their-personal
git add .
git commit -m "Initial personal repo based on example"
git push -u origin main

# Option B: Start from personal.example
cd ..
rm -rf personal
cp -r personal.example personal
cd personal
git init
# ... same as above
```

**Sister directories approach:**
```bash
mkdir claude-as-coach-combined
cd claude-as-coach-combined
git clone https://github.com/ZachBeta/claude-as-coach

# Option A: Clone their existing personal repo
git clone https://github.com/THEM/their-personal claude-as-coach-personal

# Option B: Create new from example
cp -r claude-as-coach/personal.example claude-as-coach-personal
cd claude-as-coach-personal
git init
git remote add origin https://github.com/THEM/their-personal
git add .
git commit -m "Initial personal repo"
git push -u origin main
```

**Question:** Is one clearly simpler than the other?

---

## Current State (2025-12-01 18:30)

**What we changed today:**
1. ✅ Removed `personal/` submodule from git tracking
2. ✅ Updated .gitmodules (removed personal/ entry)
3. ✅ Updated all documentation to reflect sister directories pattern:
   - README.md
   - CLAUDE.md
   - WORKFLOW-GUIDE.md
   - PROJECT-SETUP.md
4. ✅ Committed changes (2 commits)

**Current branch:** `main`
**Commits ahead of origin:** 9

**Git history includes:**
- `6b78443` - Remove personal/ submodule - use sister directories pattern
- `4d2d599` - Update documentation for sister directories pattern

**Working tree:** Clean

---

## Decision Framework

### Must-Have Requirements (Non-Negotiable)

1. ✅ **CLAUDE.md must auto-load** when using Claude Code
2. ✅ **Both base and personal accessible** in same Claude Code session
3. ✅ **Personal data kept private** (separate git repo)
4. ✅ **Base skills shareable** (public repo)

### Success Criteria by User Type

**For You (Maintainer):**
- Can work on both repos efficiently
- Claude Code works smoothly
- Willing to tolerate some complexity if it helps others

**For Contributors (n=10):**
- Can clone and start contributing in < 5 minutes
- Don't need to understand personal repo pattern
- Clear documentation for setup

**For Adopters (n=100):**
- Can set up their own personal repo in < 15 minutes
- Clear separation of example vs their data
- Foolproof instructions

---

## Recommended Next Steps (Before Continuing Cleanup)

### Step 1: Test CLAUDE.md Loading (5 minutes)

```bash
cd /Users/zmorek/workspace/ZachBeta/studies_and_etudes/claude-as-coach-combined

# Test if CLAUDE.md loads from parent workspace
# Start new Claude Code session from parent
# Ask: "What does CLAUDE.md say about working directories?"
# Document result
```

**Possible outcomes:**
- ✅ Auto-loads `claude-as-coach/CLAUDE.md` → Sister directories viable
- ❌ Doesn't load → Sister directories NOT viable (must revert to submodules)
- 🤔 Requires @-reference → Workable but annoying

### Step 2: Evaluate Path Complexity (10 minutes)

Try working from parent workspace:
```bash
cd claude-as-coach-combined

# Try typical operations:
python claude-as-coach/scripts/skill_workflow.py pack claude-as-coach/skills/daily-summary-base/
vim claude-as-coach/skills/weekly-planning/SKILL.md
git -C claude-as-coach status

# vs from child:
cd claude-as-coach
python scripts/skill_workflow.py pack skills/daily-summary-base/
vim skills/weekly-planning/SKILL.md
git status
```

**Question:** Does the parent workspace add enough value to justify longer paths?

### Step 3: Make Decision (Use Decision Matrix)

|  | Submodule | Sister Dirs |
|---|-----------|-------------|
| CLAUDE.md loads? | ✅ Yes | ❓ Test Result |
| Path simplicity | ✅ Short paths | ❌ Long paths |
| Git simplicity | ❌ Two-step commit | ✅ Independent |
| Contributor setup | ✅ One clone | 🤔 Parent dir setup |
| Adopter setup | 🤔 Submodule swap | ✅ Simple clone |
| Maintainer workflow | 🤔 Two-step commit | ✅ Independent |
| Documentation clarity | ✅ Clear | ❌ Complex |
| "Scary" factor | ❌ Submodules intimidate | ✅ Familiar pattern |

### Step 4: Revert or Continue

**If staying with sister directories:**
- ✅ Keep current commits
- Continue with git history squash
- Ensure all docs are accurate

**If reverting to submodules:**
- Reset to before submodule removal: `git reset --hard a0963e8`
- Re-add personal/ submodule
- Update documentation to clarify submodule pattern
- Continue with git history squash

---

## Open Questions

1. **Is the "submodules are scary" reputation real or overblown?**
   - For contributors who just clone and PR, does it matter?
   - For adopters, is swapping submodule remote harder than setting up sister dirs?

2. **What's the actual pain point we're solving?**
   - Is it the two-step commit for maintainer? (Only affects you)
   - Is it perceived complexity for contributors? (May not be real)
   - Is it setup friction for adopters? (Both patterns have some friction)

3. **Can we test actual user flows?**
   - Ask someone unfamiliar to try setting up with each pattern
   - Measure time and confusion points
   - Make data-driven decision

4. **Is there a hybrid approach?**
   - Submodule for vendor/skills (clearly vendor code)
   - Sister directory for personal? (But then CLAUDE.md issue)
   - Or vice versa?

---

## Recommendation (Preliminary)

**Lean toward reverting to submodules** because:

1. **CLAUDE.md loading is critical** - We know it works with submodules
2. **Path complexity matters** - Shorter paths are better for daily use
3. **Contributor friction may be imaginary** - They just clone with one flag
4. **Two-step commit is acceptable** - Only affects you, and you're already used to it

**BUT:** Need to test sister directories CLAUDE.md loading before deciding.

---

## Timeline

**Tomorrow (2025-12-02):**
1. Test CLAUDE.md loading from parent workspace (5 min)
2. Evaluate results against decision matrix (10 min)
3. Make final decision (5 min)
4. Either: revert commits or proceed as-is (15 min)
5. Continue with Session 2: Git history squash (30-40 min)

**Critical:** Make this decision before squashing git history (point of no easy return).

---

## Notes for Tomorrow

- Current working directory: `/Users/zmorek/workspace/ZachBeta/studies_and_etudes/claude-as-coach-combined/claude-as-coach/`
- Sister directory exists: `../claude-as-coach-personal/`
- Can test parent workspace easily
- Have clear revert path if needed: `git reset --hard a0963e8`

---

**End of decision document. Resume here tomorrow.**
