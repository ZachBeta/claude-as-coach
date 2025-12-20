# Features & Enhancements

**Navigation:** This file provides a summary of all features. For detailed planning and progress, see linked `docs/features/FEATURE-*.md` files.

## Active

### 🔴 High Priority: Core Workflow Reliability

*Focus: Ongoing personal use quality and core reliability.*

#### F39: Summary Skill Date Drift Fix
**Status:** Active - Implementation ready
**Effort:** Quick win (20-30 min)
**Priority:** High (affects daily workflow reliability)
**Detail:** [docs/features/FEATURE-summary-date-drift.md](features/FEATURE-summary-date-drift.md)
**Source:** Week 8 retro (P1)

**Problem:** Daily summary skill gets confused when run the next morning - drifts back to "today" instead of the date being summarized.

**Fix:** Add explicit SUMMARY_DATE vs TODAY distinction throughout skill.

---

#### F46: Skill Improvement - Retro & Planning Learnings
**Status:** Active - Implementation ready
**Effort:** Path B (1-2 hours)
**Priority:** High (skill quality improvements)
**Detail:** [docs/features/FEATURE-skill-improvements-retro-planning.md](features/FEATURE-skill-improvements-retro-planning.md)
**Source:** Dec 7 monthly session + Week 8 retro (P2, P3)

**Key improvements:**
- P2: Sunday gap in weekly retros (week = Sun-Sat, load prior Sunday first)
- P3: Scientific method framing (observation -> finding -> hypothesis -> conclusion)
- Trigger pattern fixes for monthly skills

---

### 🟡 Medium Priority: Safety & User Experience

#### F47: Onboarding UX Audit
**Status:** Proposed
**Effort:** Path A (1-2 hours)
**Priority:** Medium (user-reported friction)
**Detail:** [docs/features/FEATURE-onboarding-ux-audit.md](features/FEATURE-onboarding-ux-audit.md)
**Source:** Discord user feedback (2025-12-11)

**Problem:** User testing revealed UX friction:
1. Agent setup instructions don't match current claude.ai UI
2. Users don't know to start new conversation after saving summary
3. "Quickstart" vs "Bootstrap" terminology question

**Tasks:**
- Audit setup instructions against current UI
- Add explicit "save summary → new chat" step
- Decide on terminology (recommend: keep Quickstart)

**Deliverables:**
- Updated project-coach-setup-base skill
- Updated QUICKSTART.md and PROJECT-SETUP.md
- "New conversation" guidance at multiple touchpoints

---

#### F48: Project Description Template Enhancement
**Status:** Proposed
**Effort:** Quick win (15-20 min)
**Priority:** Medium (habit-building support)
**Detail:** [docs/features/FEATURE-project-description-template.md](features/FEATURE-project-description-template.md)
**Source:** Discord user feedback (2025-12-11)

**Problem:** User reported: "I don't yet have the habit and keep forgetting what to do"

**Solution:** Add Quick Reference section to Project-Goals.md template, prompt user to copy to project description.

**Proposed Quick Reference:**
```
Daily: gm, daily summary
Weekly: weekly retro, weekly planning
Workflow: Morning → Summary → Save → New chat
```

**Deliverables:**
- Updated Project-Goals.md template
- Instruction to copy reference to project description

---

#### F45: Safety Disclaimers & Liability Boundaries
**Status:** Proposed - Feedback from 1-on-1 demo (2025-12-04)
**Effort:** Quick win (30-45 min)
**Priority:** High (before wide publication)

**Problem:** Users curate their own context (daily summaries, retros, protocols) which shapes Claude's responses. Even with Claude's built-in safety guardrails, curated context could steer toward problematic advice:
- Health decisions ("maybe I should stop my medication")
- Mental health crises (self-harm, suicidal ideation)
- Financial/legal decisions without professional guidance
- Relationship interventions beyond AI assistant scope

**Goal:** Add explicit safety disclaimers and scope boundaries throughout the system

**Deliverables:**

| Location | Addition |
|----------|----------|
| README.md | Liability disclaimer section |
| PROJECT-SETUP.md | Safety boundaries upfront (before Quick Start) |
| QUICKSTART.md | Brief safety note |
| Base skills | "Not a replacement for professional advice" reminders |
| Project-Goals.md template | Scope statement about AI assistant limitations |

**Proposed language (adapt per location):**
> This system is a structured reflection tool, not a replacement for professional medical, mental health, financial, or legal advice. If you're facing decisions in these domains, please consult qualified professionals. Claude is an AI assistant with limitations - it cannot assess your full situation and should not be relied upon for critical life decisions.

**Optional enhancements (future):**
- Pattern detection in morning routine for concerning context
- Explicit redirect language when health/crisis topics detected
- "When to seek help" resource links in skills

**Why now:** Demo feedback highlighted this gap. Important to address before sharing widely.

---

### 🟡 Medium Priority: Quality Polish

#### F51: Skill Platform Portability (Remove Claude.ai-Specific Paths)
**Status:** Proposed
**Effort:** Path A (1-2 hours)
**Priority:** Medium (portability for microagent)
**Source:** Week 9 planning

**Problem:** Skills contain Claude.ai VM-specific directory references (e.g., `/mnt/user/`, hardcoded paths) that:
- Won't work on other platforms (microagent, other LLM runtimes)
- Confuse users who expect different file handling
- Couple skills to specific platform implementation details

**Goal:** Make skills platform-agnostic by removing/abstracting hardcoded paths.

**Audit needed:**
- [ ] daily-summary-base - check for path references
- [ ] daily-morning-routine-base - check for path references
- [ ] planning-base - check for path references
- [ ] retrospective-base - check for path references
- [ ] project-coach-setup-base - check for path references

**Proposed changes:**
- Replace hardcoded paths with relative references or platform-agnostic language
- Use "save to project" / "project documents" instead of specific paths
- Document platform-specific behavior in a separate section if needed

**Benefits:**
- Skills work across Claude.ai, Claude Code, microagent
- Cleaner separation of skill logic from platform details
- Easier adoption on alternative runtimes

**Related:** F41 (Microagent Deployment), F44 (Repository Rename)

---

#### F27: Skill Vendor Compliance Review
**Status:** Active - Quality improvement
**Effort:** Path B (30-45 min per phase)
**Priority:** Medium (improves skill quality)
**Detail:** [docs/features/FEATURE-skill-vendor-compliance.md](features/FEATURE-skill-vendor-compliance.md)

**Goal:** Systematically review all skills against vendor/skills/skill-creator/SKILL.md conventions

**Already completed:**
- ✅ project-coach-setup-base (condensed 360→120 lines)
- ✅ planning-base (added triggers, unified to any time scale)
- ✅ retrospective-base (added triggers, unified to any time scale)

**Next:** Review daily-morning-routine-base and daily-summary-base

---

#### F19: Project Memories Evaluation
**Status:** Active - Evaluation in progress
**Effort:** Path A (1-2 hours)
**Priority:** Medium (clarity improves system understanding)
**Detail:** [docs/features/FEATURE-memory-evaluation.md](features/FEATURE-memory-evaluation.md)
**Source:** Original backlog + Week 8 retro (P4)

**Goal:** Evaluate whether Claude Projects' auto-generated memories provide value or add confusion.

**Tasks:** Export memories, categorize by value, test with/without, make decision (keep/prune/disable).

---

#### F52: Identity Change Framing for Behavior Change
**Status:** Proposed
**Touches:** 1 (latest: 2025-12-19)
**Effort:** Path A (1-2 hours)
**Priority:** Medium (documentation enhancement)
**Source:** Dec 12 presentation feedback (Robb Winkle)

**Concept:** Behavior change research suggests identity change is key to lasting habits. The coaching system could incorporate this by helping users explore and roleplay their desired identity.

**Reference:** https://www.psychologytoday.com/us/blog/automatic-you/202206/the-key-behavior-change-is-identity-change

**Potential additions:**
- Identity exploration in project-coach-setup (who do you want to become?)
- Persona/identity framing in daily summaries
- "Acting as if" prompts in morning routine
- Identity reinforcement in weekly retros

---

### Known Platform Limitations

#### F40: Claude.ai Platform Limitations
**Status:** Documentation only (not bugs to fix)
**Priority:** Informational

**Known limitations of Claude.ai Projects + Skills:**

1. **Skills are global** - Cannot scope skills to specific projects; all uploaded skills appear across all projects
2. **Conversation renaming** - Agent cannot update conversation title after first message
3. **Skills not shared** - Skills uploaded to claude.ai (web/desktop/mobile) are not visible in Claude Code
4. **No programmatic skill management** - Must manually upload/toggle skills in Settings > Capabilities

**Workarounds:**
- Use naming conventions to identify skill purpose (e.g., `production-*`, `development-*`)
- Disable unused skills in Settings to reduce confusion
- Accept that Claude Code and claude.ai have separate skill ecosystems

---

## Backlog

### Demo Infrastructure (Low Priority)

#### F35: Demo Script & Date Regeneration
**Status:** Backlog (was Active)
**Effort:** Path A (30-45 min)
**Priority:** Low (demo infrastructure)

**Goal:** Make demo script runnable on any date without manual edits. Python script to regenerate dates in demo script + Rob's docs.

---

#### F37: Skill ZIP Format PR to anthropics/skills
**Status:** Backlog (was Ready for PR)
**Touches:** 3 (latest: 2025-12-19)
**Effort:** Quick win (15-20 min)
**Priority:** Low (workaround exists)

**Problem:** Vendor tooling produces `.skill` files that Claude.ai rejects.

**Workaround:** Use local `pack_skill.py` which outputs `.zip`, or manually rename `.skill` -> `.zip`

**Prerequisite:** Clean up fork first (has stale pycache commit)

---

#### F38: Alternative Onboarding Paths
**Status:** Backlog (was Test for Dec 12)
**Effort:** 30-45 min testing
**Priority:** Low (nice-to-have)

**Goal:** Test alternative onboarding paths (URL paste, chat upload) vs Settings > Capabilities flow.

---

#### F49: Synthetic Demo Data System
**Status:** Backlog (was Planning)
**Effort:** Medium (4-6 hours)
**Priority:** Low (demo support)
**Detail:** [docs/features/FEATURE-synthetic-demo-data.md](features/FEATURE-synthetic-demo-data.md)

**Problem:** Synthetic demo data only covers "run days" (Mon/Wed/Fri), causing gaps when demo day doesn't align.

---

### F44: Repository Rename Consideration
**Status:** Decision needed before wide publication
**Effort:** Path B (1-2 hours for find/replace + GitHub rename)
**Priority:** Medium (before public launch)

**Goal:** Rename repository to better reflect its purpose and avoid relationship-implying terminology

**Current name:** `claude-as-coach` / `claude-as-coach-personal` / `claude-as-coach-combined`

**Concerns with current name:**
1. "Coach" implies ongoing relationship/mentorship dynamic
2. "Claude" ties name to specific provider (limits microagent portability narrative)
3. Boundary-setting guidance suggests avoiding coach/mentor/advisor framing

**Options discussed:**

| Name | Notes |
|------|-------|
| `claude-projects-goals-demo` | Explicit tech demo framing, honest about Claude-specific scope |
| `reflection-loop` | Provider-agnostic, captures iterative nature |
| `structured-reflection` | Describes methodology |
| `goals-assistant` | Clear AI assistant role, neutral |
| `fractal-journal` | Distinctive, captures compression pattern |

**Recommendation:** If microagent supersedes this demo, use provider-agnostic name for that. Keep this as explicit Claude Projects demo with `claude-projects-goals-demo`.

**Scope if renamed:**
- GitHub repo rename (manual)
- ~50+ references across CLAUDE.md, README, docs
- Personal repo rename
- Parent workspace rename

**Decision trigger:** Before sharing repo widely / before microagent launch

---

### F34: Parent Workspace as Public Repository
**Status:** Proposed - Architecture decision needed
**Effort:** TBD (depends on chosen option)
**Priority:** Medium (F31, F33 complete - blockers cleared)
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

**Blockers cleared:** F33 (sister directories) and F31 (git history squash) both complete.

**Decision trigger:** User feedback. If 3+ people struggle with workspace setup, prioritize restructuring.

**Next:** Evaluate with real user onboarding feedback

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
**Priority:** Medium
**Status:** Manual workaround documented, ready for automation
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

**Ready when:**
- Real user friction emerges at n~10 scale
- Manual workflow becomes burdensome
- Better to build based on actual pain points, not assumptions

---

### F29: Sally the Software Engineer Demo (Deprioritized)
**Status:** Deprioritized - Rob serves as primary demo
**Priority:** Low

**Goal:** Interview prep demo persona (4 weeks) showing daily->weekly fractal compression in knowledge work domain

**Why deprioritized:** Rob demo complete and demonstrates all key patterns. Sally adds domain diversity but not essential. Consider if users request non-fitness examples.

---

### F30: Maya Mandarin Learner (Microagent Eval Persona)
**Effort:** 7-11 hours (persona + model evaluation)
**Priority:** Medium
**Status:** Persona design complete, ready for microagent eval phase
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

**Value:**
- Validates microagent portability to non-Claude models
- Tests system with language-specific coaching (domain advantage for Chinese models)
- Informs model-agnostic skill design patterns

---

### F41: Microagent Deployment
**Status:** Future exploration
**Effort:** TBD (significant)
**Priority:** Medium

**Goal:** Nanochat-inspired minimal agent harness for executing skill workflows with open weight models

**Concept:**
- Lightweight orchestration of tool calls
- Works with arbitrary commodity open weight models
- Same "context bonsai" approach as Claude.ai version
- Portability to non-Claude runtimes

**Potential deployment:** https://echo.merit.systems

**Related:** F30 (Maya Mandarin Learner) for model comparison testing

---

### F42: Claude Code Plugin Exploration
**Status:** Future exploration
**Effort:** TBD
**Priority:** Low

**Goal:** Investigate Claude Code plugins as alternative runtime for coaching system

**Context:**
- Friend feedback: "shouldn't this be a Claude Code plugin?"
- Counter-argument: Cross-device logging (phone + computer) favors claude.ai Projects
- Logging activities like "woke up", "went for jog", "eating dinner" easier from mobile

**Links:**
- https://code.claude.com/docs/en/plugin-marketplaces
- https://github.com/anthropics/claude/tree/main/plugins

**Decision:** Cross-device use case (mobile logging) may not fit plugin model

---

### F43: Couch-to-5K Packaged Experience
**Status:** Future idea
**Effort:** TBD
**Priority:** Low

**Goal:** Single skill upload for complete couch-to-5K coaching experience

**Concept:**
- Package entire C25K coaching as one uploadable skill
- Includes training plan, metrics templates, recovery protocols
- "Full stack" coaching in one .zip file
- Lower barrier to entry than current multi-skill setup

**Prerequisites:** Validate current multi-skill approach works well first

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

Automated generation of presentation slides/materials for Dec 12th presentation

---

## Completed

### December 2025

- ✅ **F17: Dec 12th Presentation Prep** (Dec 12) - Skill composability confirmed (Dec 1), base skills created, Rob demo complete, PROJECT-SETUP.md written, git history squashed. Target audience: new year's resolutioners wanting sustainable goal infrastructure.
- ✅ **F50: Slides URL Restructure** (Dec 15) - Created permanent URL pattern: `slides.html` redirects to latest presentation (`slides-2025-12-12.html`). Future presentations will be dated archives.
- ✅ **F26: Monthly Retrospective Rollup** (Dec 11) - Solved by unified `retrospective-base` skill supporting any time scale (daily/weekly/monthly/quarterly/yearly). No separate monthly skill needed.
- ✅ **F31: Git History Squash** (Dec 3) - Squashed 78 commits → 1 clean commit, removed personal data, repo safe to share
- ✅ **F33: Sister Directories Pattern** (Dec 3) - Validated CLAUDE.md auto-loads from parent workspace, pattern confirmed working
- ✅ **F28: Rob the Runner Demo** (Dec 2) - Created 10 sample documents demonstrating fractal compression (daily→weekly→monthly), Rob uses base skills only
- ✅ **F36: Save-to-Project UX Instructions** (Dec 4) - Added platform-specific save instructions to project-coach-setup-base
- ✅ **F15: Workflow Cleanup** (Nov 29) - Cleaned skill_workflow.py imports, removed dead flags, IDE integration documented

### November 2025

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
