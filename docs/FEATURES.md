# Features & Enhancements

**Navigation:** This file provides a summary of all features. For detailed planning and progress, see linked `docs/features/FEATURE-*.md` files.

## Active

### 🔴 High Priority: Enable Sharing with Acquaintances

#### F33: Sister Directories Pattern Validation
**Status:** ✅ Phase 1 PASSED (2025-12-03) - Remaining phases optional
**Effort:** Quick win (30-45 min for testing + decision)
**Priority:** High - Was BLOCKING F31 (now unblocked)
**Detail:** [docs/features/FEATURE-sister-directories-pattern.md](features/FEATURE-sister-directories-pattern.md)

**Goal:** Finalize personal repo architecture (submodule vs sister directories) and stabilize documentation before git history squash

**Critical unknowns (resolved):**
1. ✅ Does CLAUDE.md auto-load from child directory when running from parent workspace? **YES - CONFIRMED 2025-12-03**
2. Path complexity (longer paths) - acceptable, working in practice
3. Where should users actually work day-to-day? - Parent workspace works well

**Testing phases:**
1. ✅ Phase 1: Critical test (CLAUDE.md loading) - **PASSED** (15 min)
2. Phase 2: Path complexity evaluation - validated in use (10 min)
3. Phase 3: Final decision using decision matrix - GO for sister directories (5 min)
4. Phase 4: Documentation cleanup - can proceed post-squash (15-30 min)

**Current state:** Sister directories working. CLAUDE.md loads correctly from parent workspace.

**No longer blocking:** F31 can proceed

**Next:** Proceed with F31 (git squash), documentation cleanup can follow

---

#### F31: Git History Squash & Personal Data Audit
**Status:** ✅ COMPLETE (2025-12-03)
**Effort:** Path B (45-60 min - completed)
**Priority:** High - Was BLOCKING for sharing repo with acquaintances
**Detail:** [docs/features/FEATURE-git-history-squash.md](features/FEATURE-git-history-squash.md)

**Goal:** Clean git history and audit all files to remove personal data, enabling safe sharing before Dec 12th presentation

**Phases:**
1. ✅ Audit current files for personal data - DONE (2025-12-01, repo clean)
2. ✅ Plan git history strategy - single squash decided
3. ✅ Fix identified issues - Connecticut reference removed
4. ✅ Add MIT license - already present
5. ✅ Execute git squash with backup - DONE (2025-12-03)
6. ✅ Verification & fresh clone testing - DONE (2025-12-03)

**Result:** 78 commits → 1 commit (`04b269a Initial public release: Claude-as-Coach framework`)

**Backup available:** Local branch `backup-before-squash` preserves full history if needed

**No longer blocking:** Repo is now safe to share publicly

---

### 🔴 High Priority: Dec 12th Demo Content

#### F28: Rob the Runner Demo Persona
**Status:** Active - Demo content creation
**Effort:** 3-4 hours (estimated)
**Priority:** High (Dec 12th presentation)
**Detail:** [docs/features/FEATURE-rob-runner-demo.md](features/FEATURE-rob-runner-demo.md)

**Goal:** Create couch-to-5K demo persona (8 weeks) showing daily→weekly fractal compression

**Deliverables:**
- Sample data: 3 daily summaries (Week 8), 3 weekly retros (Weeks 5-7)
- Personal skills: daily-summary-rob-personal, morning-routine-rob-personal, etc.
- Project-Goals.md for Rob's coaching project
- Protocol documents (warmup, fueling, recovery)

**Key metrics:** Distance, pace, heart rate, sleep, energy, recovery

**Fractal demonstration:**
- Recent (Week 8): Granular daily summaries
- Mid-range (Weeks 5-7): Weekly retros compress 21 days → 3 documents
- Historical (Weeks 1-4): Referenced narratively, no individual files

**Timeline:** THIS WEEKEND (Dec 7-8) for initial content creation

---

### F29: Sally the Software Engineer Demo Persona
**Status:** Active - Demo content creation
**Effort:** 2-3 hours (estimated)
**Priority:** High (Dec 12th presentation)
**Detail:** [docs/features/FEATURE-sally-software-engineer-demo.md](features/FEATURE-sally-software-engineer-demo.md)

**Goal:** Create interview prep demo persona (4 weeks) showing daily→weekly fractal compression in different domain

**Deliverables:**
- Sample data: 3 daily summaries (Week 4), 2 weekly retros (Weeks 2-3)
- Personal skills: daily-summary-sally-personal, morning-routine-sally-personal, etc.
- Project-Goals.md for Sally's coaching project
- Study protocol documents (daily routine, mock interview prep, topic checklists)

**Key metrics:** Study hours, problems solved, topics covered, mock interviews, confidence ratings

**Fractal demonstration:**
- Recent (Week 4): Granular daily summaries (final push)
- Mid-range (Weeks 2-3): Weekly retros compress 14 days → 2 documents
- Historical (Week 1): Referenced narratively (ramp-up week)

**Domain contrast:** Knowledge work vs physical activity (shows system versatility)

**Timeline:** THIS WEEKEND (Dec 7-8) for initial content creation

---

#### F35: Demo Script & Date Regeneration
**Status:** Active - Demo infrastructure
**Effort:** Path A (30-45 min for regeneration script)
**Priority:** High (Dec 12th presentation)
**Detail:** TBD (simple enough for inline tracking)

**Goal:** Make demo script runnable on any date without manual edits

**Problem:**
- Demo script (`DEMO-SCRIPT.md`) has hardcoded dates (Saturday, December 7, 2025)
- Rob's example documents have fixed dates (`Summary-2025-12-01-Monday-W9-D1.md`, etc.)
- Skills verify actual current date → mismatch breaks demo flow
- Running demo on different day requires manual date updates across 10+ files

**Solution options:**
| Option | Effort | Trade-off |
|--------|--------|-----------|
| **A: Regeneration script** | 30-45 min | Script rewrites dates in demo script + Rob's docs based on "demo day" |
| **B: "Pretend date" mode** | 1-2 hrs | Skills accept override date parameter for demos |
| **C: Relative-only demo** | 15-20 min | Rewrite demo to use only relative language, accept date mismatches |

**Recommended:** Option A - Python script that takes target demo date, regenerates all files with correct dates/day-names

**Tasks:**
1. Move `DEMO-SCRIPT.md` → `docs/DEMO-SCRIPT.md`
2. Create `scripts/regenerate_demo_dates.py`
3. Script updates: demo script, Rob's 10 example documents
4. Test: run script, verify demo flow works end-to-end
5. Document usage in demo script header

**Deliverables:**
- `docs/DEMO-SCRIPT.md` (relocated)
- `scripts/regenerate_demo_dates.py` (new)
- Updated Rob documents with regenerated dates

**Next:** Move demo script, design regeneration approach

---

#### F26: Monthly Retrospective Rollup
**Status:** Active - Design validation phase
**Effort:** Path B (2-3 hours for manual rollup + skill design)
**Priority:** Medium-High (valuable exploration + presentation enhancement)
**Detail:** [docs/features/FEATURE-monthly-rollup.md](features/FEATURE-monthly-rollup.md)
**Design:** [docs/design/MONTHLY-ROLLUP-DESIGN.md](design/MONTHLY-ROLLUP-DESIGN.md)

**Goal:** Extend fractal pattern to monthly scale (daily→weekly→monthly)

**Context:**
- First time reaching monthly timescale in the system
- November 2025 complete with 4 weekly retros
- Detailed process design already scoped (output structure, lifecycle, archival workflow)

**Deliverables:**
- Manual November monthly retro (personal + sanitized example)
- Validation report: answers to 5 open questions from design doc
- Skill design decision (separate skill? parameterized? manual-only?)
- Document lifecycle table added to WORKFLOW-GUIDE.md

**Why now:** Natural timing (early December), strengthens presentation narrative, validates design with real data

**Next:** Apply proposed structure to November data, answer open questions empirically

---

### 🟡 Medium Priority: Pre-Presentation Polish

#### F24: Dev→Prod Deployment Workflow
**Status:** Active - Documentation needed
**Effort:** Quick win (30-45 min)
**Priority:** High (addresses current friction)
**Detail:** [docs/features/FEATURE-deployment-workflow.md](features/FEATURE-deployment-workflow.md)

**Goal:** Document process for syncing refined skills from repo to Claude.ai production

**Problem:**
- Skills evolving in repo but production is stale
- "Working but suboptimal" friction in daily workflow
- No documented deployment process

**Solution:**
- Manual workflow + checklist (automation deferred to F23)
- Pre-deployment validation steps
- Post-deployment verification
- Tracking strategy (git tags or deployment log)

**Next:** Add "Deploying Skills to Claude.ai" section to WORKFLOW-GUIDE.md

---

#### F27: Skill Vendor Compliance Review
**Status:** Active - Quality improvement
**Effort:** Path B (30-45 min per phase)
**Priority:** Medium-High (improves presentation quality)
**Detail:** [docs/features/FEATURE-skill-vendor-compliance.md](features/FEATURE-skill-vendor-compliance.md)

**Goal:** Systematically review all skills against vendor/skills/skill-creator/SKILL.md conventions

**Scope:**
- Phase 1: Base skills (5 skills) - Priority for demo testing
- Phase 2: Personal skills (4 skills) - Production quality
- Phase 3: Alice example skills - Deferred to F17 Task 3

**Checklist per skill:**
- Description includes trigger phrases and "when to use"
- No unnecessary verbosity (Claude is already smart)
- Line count under 500 lines
- Imperative form throughout
- No "agent flexibility" notes
- Passes vendor quick_validate.py

**Already completed:**
- ✅ project-coach-setup-base (condensed 360→120 lines)
- ✅ weekly-planning-base (added triggers)
- ✅ weekly-retrospective-base (added triggers)

**Next:** Review daily-morning-routine-base and daily-summary-base

---

## Backlog

### F34: Parent Workspace as Public Repository
**Status:** Proposed - Architecture decision deferred
**Effort:** TBD (depends on chosen option)
**Priority:** Medium (post-F33, post-F31)
**Detail:** [docs/features/FEATURE-parent-workspace-public-repo.md](features/FEATURE-parent-workspace-public-repo.md)

**Goal:** Decide whether to publish `claude-as-coach-combined/` as a public parent workspace repository with submodule references to framework and example repos.

**Key questions:**
1. Should parent workspace be the main entry point for users?
2. Naming clarity: `claude-as-coach` (parent) vs `claude-as-coach-framework` (child)?
3. Where should documentation live (parent vs child)?
4. How do users set up their private personal repo?
5. Does restructuring justify the migration effort?

**Options:**
- **Option A:** Parent as main entry point (single clone, clear structure)
- **Option B:** Publish parent with current naming (less disruption)
- **Option C:** Status quo (manual workspace setup, no parent repo)

**Blocked by:** F33 (sister directories validation), F31 (git history squash)

**Decision trigger:** User feedback after Dec 12th presentation. If 3+ people struggle with workspace setup, prioritize restructuring.

**Next:** Defer until after F33 + F31, evaluate with real user onboarding feedback

---

### F32: Skill Workflow Git Operations
**Status:** Deferred (removed from skill_workflow.py 2025-12-01)
**Effort:** Path B (30-45 min to re-implement if needed)
**Priority:** Low (out of scope for demo)
**Detail:** [docs/features/FEATURE-skill-workflow-git-ops.md](features/FEATURE-skill-workflow-git-ops.md)

**Goal:** Git automation features for skill workflow (commit, diff, edit commands)

**Context:**
- Removed git-related functionality from `skill_workflow.py` during pre-presentation simplification
- Script now focuses solely on pack/unpack operations
- Users can use standard `git add` and `git commit` commands instead

**Removed features:**
- `commit` command - automated git commit workflow with standardized messages
- `edit` command - unpack + open in editor
- `_show_diff_summary()` - visual diff display for skill ZIP files

**Manual workflow (replacement):**
```bash
# Pack skill
python scripts/skill_workflow.py pack skills/daily-summary-base/

# Commit using standard git
git add skills/daily-summary-base.skill
git commit -m "Update daily-summary-base skill"
```

**Why deferred:**
- Core workflow is pack/unpack, not git automation
- Reduces script complexity for demo purposes
- Functionality preserved in git history if needed later

---

### F17: Dec 12th Presentation Prep (Tracking)
**Status:** Most tasks complete, tracking remaining items
**Effort:** Remaining: Git history squash (post-Dec 12th)
**Priority:** Medium (post-presentation cleanup)
**Detail:** [docs/features/FEATURE-presentation-prep.md](features/FEATURE-presentation-prep.md)
**Deadline:** Dec 12th presentation, git squash before open sourcing

**Completed tasks:**
- ✅ Task 1: Test skill composability - **Confirmed working 2025-12-01**
  - Test Case B validated in production (morning routine base + personal)
  - `extends:` directive recognized by Claude.ai
  - Skills merge without conflicts, content flows naturally
  - System requirements documented (Pro minimum, Max x5 recommended)
- ✅ Task 2: Create base skill versions (all 4 core skills separated)
- ✅ Task 4: PROJECT-SETUP.md exists (may need minor updates)

**In progress:**
- Task 3: Create Rob/Sally demo content → See F28, F29 (active)

**Remaining:**
- Task 1: Optional additional test cases (C, D, E) for deeper understanding
- Task 5: Demo project setup (day-of Dec 12th)
- Task 6: Squash git history to remove personal data (BLOCKING before public release)

**Naming convention (production/development):**
- `production-*-personal.skill` - User's production skills
- `development-*-base.skill` - Shareable base frameworks
- `development-*-rob-personal.skill` - Rob demo (couch-to-5K)
- `development-*-sally-personal.skill` - Sally demo (interview prep)

**Target audience:** New year's resolutioners wanting sustainable goal infrastructure

---

### F15: Workflow Cleanup
**Status:** Complete (git workflow deferred)
**Effort:** Completed 2025-11-29
**Priority:** Low
**Detail:** [docs/features/FEATURE-workflow-cleanup.md](features/FEATURE-workflow-cleanup.md)

**Goal:** Fix `skill_workflow.py` vendor script integration and improve git workflow for base+personal skill pairs

**Completed:**
- ✅ Import cleanup and validation (removed unused imports, dead flags)
- ✅ VSCode/IDE integration documented
- ✅ Legacy code path removal complete
- ✅ Pack/unpack workflow stable

**Deferred:**
- Git workflow for paired base+personal commits (manual/agentic workflow acceptable for now)

---

### F9: MCP Skill Manager
**Effort:** Phase 1+ (2-3 hours)
**Priority:** High
**Detail:** [docs/features/FEATURE-mcp-skill-manager.md](features/FEATURE-mcp-skill-manager.md)

**Goal:** Enable Claude.ai to save `.skill` archives directly to repo via MCP

**Benefits:**
- Eliminate manual file transfers
- Save time: < 5 seconds (vs. ~60 seconds manual)
- Automatic validation and git commits

---

### F23: Production/Development Skill Workflow
**Effort:** Path C (1-2 hours implementation + testing)
**Priority:** Medium (post-Dec 12th)
**Status:** Manual workaround documented, automated tooling deferred until after presentation
**Detail:** [docs/features/FEATURE-production-development-workflow.md](features/FEATURE-production-development-workflow.md)

**Goal:** Enable safe skill iteration without breaking production usage

**User problem (n=1 → n=100):**
- Users want to test skill changes without breaking daily workflow
- Claude.ai skills are global, require manual toggling on/off
- Need versioning: production (stable) vs development (experimental)

**Proposed workflow:**
```bash
# Pack for production use
python scripts/skill_workflow.py pack daily-summary-personal --env production
# Output: production-daily-summary-personal.skill

# Pack for development/testing
python scripts/skill_workflow.py pack daily-summary-personal --env development
# Output: development-daily-summary-personal.skill

# Promote dev to production after testing
python scripts/skill_workflow.py promote daily-summary-personal
# Copies dev → prod, repacks as production variant
```

**Features:**
- `--env production|development` flag for pack command
- `promote` command to move validated changes dev → prod
- Handles frontmatter name matching automatically
- Prevents conflicts from duplicate YAML names

**Implementation notes:**
- Test frontmatter name matching behavior during F17 Task 1
- Design informed by friend feedback at n~10 scale
- May integrate with F9 (MCP) for direct Claude.ai deployment

**Why post-Dec 12th:**
- Alice demo can use manual workflow (acceptable for examples)
- Real user friction will emerge when friends adopt (n~10)
- Better to build based on actual pain points, not assumptions

---

### F30: Maya Mandarin Learner (Microagent Eval Persona)
**Effort:** 7-11 hours (persona + model evaluation)
**Priority:** Medium (post-Dec 12th)
**Status:** Persona design complete, deferred to microagent eval phase
**Detail:** [docs/features/FEATURE-maya-mandarin-learner.md](features/FEATURE-maya-mandarin-learner.md)

**Goal:** Language learning demo persona for evaluating coaching system across different models (Claude vs Chinese frontier models)

**Model comparison:**
- **Claude Sonnet 4.5** - Baseline
- **Kimi-k2** - Chinese frontier model (Moonshot AI)
- **Zai-GLM4.6** - Chinese frontier model (Zhipu AI)

**Evaluation dimensions:**
- Coaching quality (insight depth, pedagogy, cultural context)
- Language-specific capabilities (tones, characters, grammar)
- Cross-model skill portability
- Summary quality and reflection depth

**Hypothesis:** Chinese models may provide richer Mandarin learning context and culturally informed coaching

**Deliverables (future):**
- Sample data: 3 daily summaries (Week 4), 2 weekly retros (Weeks 2-3)
- Personal skills: daily-summary-maya-personal, etc.
- Model comparison methodology and results
- Portability insights for microagent architecture

**Key metrics:** Characters known (HSK levels), vocabulary retention, tone accuracy, conversation time, study hours, comprehension level

**Why post-presentation:**
- Validates microagent portability to non-Claude models
- Tests system with language-specific coaching (domain advantage for Chinese models)
- Informs model-agnostic skill design patterns

---

### F25: Day Seam Flexibility
**Effort:** Quick win (15-20 min)
**Priority:** Low (working fine currently)
**Detail:** [docs/features/FEATURE-day-seam-flexibility.md](features/FEATURE-day-seam-flexibility.md)

**Goal:** Clarify day boundary handling in daily-summary-base skill instructions

**Context:**
- Natural conversation boundaries are morning-to-morning, not midnight
- "Summary OF [date]" concept already handles this implicitly
- More of a documentation clarity improvement than actual problem

**Solution:**
- Add explicit "Date Handling & Day Boundaries" section to daily-summary-base skill
- Provide edge case examples (spanning midnight, morning completions)
- Emphasize "logical day" over "calendar day"

**Next:** Defer to post-Dec 12th unless extra time available

---

### F11: Vendor Submodule Update Strategy
**Effort:** Quick win (10-15 min)
**Priority:** Medium
**Detail:** [docs/features/FEATURE-vendor-submodule.md](features/FEATURE-vendor-submodule.md)

**Goal:** Establish strategy for keeping `vendor/skills/` fork synced with upstream

**Options:**
- A: Tracking branch (recommended)
- B: Direct upstream tracking
- C: Periodic manual sync

**Next:** Decide strategy, update `.gitmodules`, document in WORKFLOW-GUIDE.md

---

### F12: Python Tooling Improvements & Testing
**Effort:** Path C (1-2 hours)
**Priority:** Medium

**Goal:** Apply modern Python development patterns to `skill_workflow.py` and add automated testing

**Rationale:** File is growing in complexity, needs test coverage before further refactoring

**Tooling:**
- `uv` - Fast Python package manager (venv management)
- `pytest` - Testing framework
- `mypy` - Type checking
- `ruff` - Fast linting
- Style enforcement - Named args over positional

**Testing (skill_workflow_test.py):**

**Test coverage areas:**
1. **Path resolution logic**
   - `*-base` suffix → `skills/NAME-base/`
   - `*-personal` suffix → `personal/skills/NAME-personal/`
   - No suffix → `skills/NAME/`
   - Edge cases: nested paths, missing directories

2. **Pack/unpack operations**
   - ZIP creation with correct structure (NAME/SKILL.md)
   - ZIP extraction to specified directory
   - Validation of packed .skill files
   - Handling malformed archives

3. **Git operations**
   - Commit command integration
   - Git status detection
   - Staged/unstaged file handling
   - Submodule awareness (personal/)

4. **Vendor integration**
   - package_skill.py usage
   - Graceful degradation if vendor unavailable (or remove fallback - see F21)
   - Validation script integration

**Testing approach:**
- pytest fixtures for temporary directories
- Mock git operations to avoid repository pollution
- Sample .skill files for unpack testing
- Parameterized tests for path resolution variations

**Benefits:**
- Enable confident refactoring (especially for F21, F22)
- Catch regressions early
- Document expected behavior
- Reduce manual testing burden

---

### F13: Skill Workflow Documentation for Claude Code
**Effort:** Path A (20-30 min)
**Priority:** High

**Goal:** Document how to use this repo with Claude Code for skill refinement

**Deliverables:**
- Update WORKFLOW-GUIDE.md with Claude Code integration
- Add workflow examples to README.md
- Potentially create CONTRIBUTING.md

**Target:** Enable others to fork and adapt this repo

---

### F14: Repository Cleanup Tasks
**Effort:** Quick win (10-15 min)
**Priority:** Low

**Tasks:**
- [x] Clean up `.gitignore` - Completed 2025-12-01 (removed .backups/ entry)
- [x] Delete stale documentation - Completed 2025-11-26
- [x] Delete HANDOFF files, create FEATURE docs - Completed 2025-11-26
- [ ] Review and update cross-references in documentation

---

### F19: Project Memories Cleanup
**Effort:** TBD
**Priority:** Medium

**Goal:** Simplify project by addressing Claude Projects memory feature usage

**Options:**
- A: Remove project memories entirely to reduce complexity
- B: Establish clear conventions for using memory via skills
- C: Document current memory usage and keep as-is

**Decision needed:** Evaluate current memory usage, determine if it provides value or adds confusion

**Tasks:**
- [ ] Audit current project memories in Claude.ai
- [ ] Assess if memories duplicate skill functionality
- [ ] Choose path: remove, conventionalize, or document

---

### F20: Simplify Skill Naming Convention
**Effort:** TBD
**Priority:** Medium

**Goal:** Evaluate if the three-tier naming system (*-base.skill, *.skill, *-personal.skill) can be simplified

**Hypothesis:** Two-tier system (*.skill + *-personal.skill) may be sufficient for base framework + personalization

**Current pattern:**
- `daily-summary-base.skill` - Base framework (shareable)
- `daily-summary-personal.skill` - Personal extensions

**Proposed pattern:**
- `daily-summary.skill` - Base framework (shareable, renamed from *-base)
- `daily-summary-personal.skill` - Personal extensions (unchanged)

**Benefits:**
- Simpler mental model
- Fewer files to manage
- Clearer distinction between base and personal

**Tasks:**
- [ ] Document rationale for current *-base naming
- [ ] Test if renaming breaks anything (skill_workflow.py, documentation)
- [ ] Decide if simplification is worth migration effort
- [ ] If yes: Plan migration strategy for existing skills

---

### F21: Remove _fallback_pack() Function
**Effort:** Quick win (10-15 min)
**Priority:** Medium

**Goal:** Simplify skill_workflow.py by relying exclusively on vendor package tools

**Current state:**
- `skill_workflow.py` includes `_fallback_pack()` function for manual ZIP packaging
- Used when vendor tools unavailable

**Rationale:**
- Vendor package (vendor/skills/) is now reliable and available via submodule
- Fallback code path adds complexity and maintenance burden
- Reduces code paths to test and maintain

**Tasks:**
- [ ] Verify vendor package_skill.py is always available via submodule
- [ ] Remove `_fallback_pack()` function from skill_workflow.py
- [ ] Update error handling to require vendor tools
- [ ] Test pack operations still work
- [ ] Update documentation if needed

**Impact:** Cleaner codebase, single code path for packaging

---

### F22: Simplify Output Directory Logic
**Effort:** Path A (20-30 min)
**Priority:** Medium

**Goal:** Simplify skill_workflow.py by inferring output directory from skill file location

**Current workflow:**
- User downloads .skill file from Claude.ai
- User runs `unpack --output-dir skills/NAME/` or `--output-dir personal/skills/NAME/`
- Requires explicit directory specification

**Proposed workflow:**
- User downloads .skill file to appropriate location (skills/ or personal/skills/)
- User runs `unpack FILENAME.skill` (automatic directory detection)
- Script infers output location based on skill file path
- Workflow: download → unpack → commit → repack+validate

**Benefits:**
- Fewer command-line arguments
- Less room for user error (wrong output location)
- Workflow guidance: "download to the right place, then unpack"

**Implementation:**
- Track where .skill file is located
- If in `skills/`: output to `skills/NAME/`
- If in `personal/skills/`: output to `personal/skills/NAME/`
- May still support `--output-dir` for edge cases

**Tasks:**
- [ ] Design path detection logic
- [ ] Update unpack command implementation
- [ ] Update documentation with new workflow
- [ ] Test with skills/ and personal/skills/ locations

---

### F3: Add skill creation helper
**Effort:** Path B (30-45 min)

Extend skill_workflow.py with `create` command using vendor/skills init_skill.py

---

### F4: Add skill diff viewer
**Effort:** Path A (20-30 min)

Show diffs between packed .skill files more easily

---

### F5: Add skill validation command
**Effort:** Quick win (10-15 min)

Standalone validation without packing

---

### F6: Automated skill deployment
**Effort:** Path C (1-2 hours)

Script to package all skills and prepare for Claude Projects upload

---

### F7: Skill usage analytics
**Effort:** Path B (30-60 min)

Track which skills get used most in daily practice

---

### F8: Presentation materials generator
**Effort:** Phase 1+ (2-4 hours)

Automated generation of presentation slides/materials for December 5th presentation

---

## Completed (2025-11)

- ✅ **F1: Test Python skill workflow** (Nov 25) - Verified end-to-end workflow
- ✅ **F2: Migrate personal files to submodule** (Nov 25) - 14 summaries, 1 retro, 6 reference docs
- ✅ **F10: Documentation cleanup** (Nov 25) - Created docs/ directory, organized documentation
- ✅ **F16: Directory Refactoring** (Nov 29) - Flattened personal/project_documents/ and personal/reference/ into personal/documents/ (25 files), moved personal/*.skill to personal/skills/*.skill to match main repo pattern
- ✅ **F18: Skill Source Tracking** (Nov 29) - Unpacked all standalone skills to tracked source directories, updated skill_workflow.py to support skills/NAME/ pattern, removed skills-working/ directory. All skills now editable in place with git diffs visible.

---

## Notes

**FEATURE document lifecycle:**
- Created in `docs/features/FEATURE-*.md` when planning begins
- Updated during implementation with progress notes
- **Deleted after completion** (git history preserves)
- Summary remains in this file

**Documentation hierarchy:**
1. **docs/NEXT-SESSION.md** → Actionable, quick scan, "what do I do next?"
2. **docs/FEATURES.md** (this file) → Summary backlog with key bullets
3. **docs/features/FEATURE-*.md** → Detailed planning/progress, exists only during active work
