# Changelog

All notable user-facing changes to the Claude-as-Coach system.

**Format:** Chronological (most recent first)

**Categories:**
- **Added** - New skills, features, documentation
- **Changed** - Workflow changes, updates to existing features
- **Fixed** - Bug fixes affecting daily use
- **Improved** - Quality improvements, better explanations

---

## 2025-12-01

### Added

**QUICKSTART.md** - Complete beginner onboarding guide
- Get from zero to first goal coaching in 10 minutes
- Step-by-step setup instructions
- Model recommendations (Sonnet 4.5, Opus 4.5)
- Context management tips for Claude Pro vs Max users

**project-coach-setup-base skill** - Conversational project initialization
- Trigger: "set up my project"
- Guides through goal setup one question at a time
- Generates Project-Goals.md artifact explaining daily/weekly workflows
- Primes context so "gm" shortcuts work in fresh projects

**Demo personas planned** (coming soon):
- Rob the Runner - Couch-to-5K training (8 weeks)
- Sally the Software Engineer - Interview prep (4 weeks)
- Maya the Mandarin Learner - Language learning (post-presentation)

### Changed

**Skill triggering in fresh projects:**
- Fresh projects now require explicit commands: "run the daily morning routine skill"
- After Project-Goals.md created, shortcuts like "gm" work naturally
- Context builds over time, making skills more responsive

### Improved

**Weekly skills now trigger reliably:**
- weekly-planning-base: responds to "weekly planning", "plan the week", "start of week"
- weekly-retrospective-base: responds to "weekly retro", "weekly retrospective", "end of week"
- Trigger phrases added to skill descriptions (vendor best practice)

**Architecture validated:**
- All 4 core skills now use composable base + personal pattern
- Base frameworks shareable, personal extensions private
- Can refine base and personal skills independently

---

## 2025-11-29

### Changed

**Directory structure simplified:**
- Flattened personal/project_documents/ and personal/reference/ into personal/documents/
- All project files now in single flat directory (matches Claude.ai Projects UI)
- Personal skills organized into personal/skills/ (matches main repo pattern)

**Skill source tracking improved:**
- All skill sources now tracked in git alongside .skill files
- Edit skills directly in place (no unpacking needed)
- Git diffs visible for skill changes

---

## 2025-11-27

### Improved

**Documentation organization:**
- Created 3-level hierarchy: NEXT-SESSION → FEATURES → FEATURE-*.md
- Feature planning documents created for active work
- Clearer navigation between planning docs

---

## 2025-11-26

### Changed

**Feature tracking restructured:**
- FEATURES.md now has Active/Backlog/Completed sections
- Individual FEATURE-*.md files for detailed planning
- Old HANDOFF-*.md files removed (consolidated into feature docs)

---

## Coming Soon

**For Dec 12th Presentation:**
- Rob the Runner demo with sample data (daily summaries, weekly retros)
- Sally the Software Engineer demo (interview prep tracking)
- PROJECT-SETUP.md updates with new personas and quickstart reference
- Monthly retrospective rollup (daily→weekly→monthly fractal compression)

**Post-Presentation:**
- Maya the Mandarin Learner demo (microagent model evaluation)
- Production/development skill workflow tooling
- Deployment workflow documentation
- MCP Skill Manager integration

---

## Notes for Users

**If you're new to the system:**
- Start with QUICKSTART.md (10 minutes to first goal coaching)
- Use "set up my project" to initialize your coaching project
- Begin with daily morning routine + daily summary for first week
- Add weekly retro/planning once daily practice feels natural

**If you're already using the system:**
- Update to latest base skills for improved triggering
- Try project-coach-setup-base for new project initialization
- Review QUICKSTART.md for tips on context management

**System requirements:**
- Claude Pro or Claude Max subscription
- Recommended: Sonnet 4.5 or Opus 4.5 (Haiku 4.5 insufficient)
- Enable Artifacts in project settings
- Monitor context usage in Settings > Usage

---

## Reporting Issues

Found a problem or have a suggestion? Open an issue on GitHub (repository coming soon after Dec 12th presentation).

---
---

# Development Timeline & Architecture Evolution

*This section documents the design process, architectural decisions, and iterative improvements made during development. Preserved here as a portfolio artifact before git history squash.*

**Target:** December 12th, 2025 presentation
**Total development time:** ~2 weeks (Nov 25 - Dec 12)
**Development approach:** Iterative design with heavy use of Claude Code for rapid prototyping and refactoring

---

## Phase 1: Foundation (Nov 25-26, 2025)

### Initial Architecture

**Goal:** Build infrastructure for managing Claude skills with git version control

**Key decisions:**
- Python-based skill workflow (pack/unpack .skill ZIP files)
- Git submodules for vendor code (anthropics/skills fork)
- Task tracking system (NEXT-SESSION.md, FEATURES.md, REFACTORS.md)

**Commits:**
- `e629087` - Repository initialization
- `6d451ad` - Submodules and Python workflow infrastructure
- `c1d953d` - Task tracking files established

**Outcome:** Functional skill editing workflow, ready for iteration

---

## Phase 2: Skill Separation Discovery (Nov 27-29, 2025)

### The Insight: Base + Personal Pattern

**Problem identified:** Monolithic skills mixed sharable frameworks with private health data
**Solution:** Separate into base skills (sharable) + personal extensions (private)

**Major changes:**
- `84f38da` - **feat:** Separate skills into base + personal architecture
- Created Alice example persona (couch-to-5K runner) as reference implementation
- Established `extends:` pattern in skill frontmatter

**F16: Directory Flattening Refactor**
- Simplified `personal/project_documents/` and `personal/reference/` → flat `personal/documents/`
- Matched Claude.ai Projects UI (flat file list)
- Personal skills organized into `personal/skills/` (parallel to main repo)
- `c877e5a` - Complete directory flattening refactor

**Design principle established:** "Shareable process frameworks separate from personal context"

---

## Phase 3: Source Tracking & Workflow Maturation (Nov 29-30, 2025)

### Making Skills Version-Controllable

**F18: Track Skill Source Code**

**Problem:** `.skill` files are ZIP archives - git diffs meaningless
**Solution:** Track source directories alongside .skill files

**Implementation:**
- `8d2694b` - Track skill source code in git alongside .skill files
- All skills now have `skills/NAME/SKILL.md` tracked in repo
- Edit skills in place (no unpacking needed)
- Pack workflow generates `.skill` files from tracked sources

**Workflow improvements:**
- Removed legacy `skills-working/` code paths
- Separated weekly-planning and weekly-retrospective into base + personal
- `dff272f` - Split weekly retro/planning into base + personal skills

**Outcome:** Git diffs now show actual skill content changes, not binary ZIP deltas

---

## Phase 4: Composability Validation (Dec 1, 2025)

### Testing the Architecture

**F17 Task 1: Validate Base + Personal Skill Stacking**

**Critical unknown:** Does Claude.ai actually merge base + personal skills correctly?

**Testing approach:**
- Test Case B: morning-routine-base + morning-routine-personal in production
- Verified `extends:` directive recognized
- Confirmed skills merge without conflicts
- Validated content flows naturally between base and personal

**Key findings documented:**
- System requirements: Claude Pro (minimum), Max x5 (recommended)
- Model requirements: Sonnet 4.5 or Opus 4.5 (Haiku 4.5 insufficient)
- Extended thinking valuable for deeper retros/planning
- `a865d2d` - Document composable skill test results and system requirements

**New skills created:**
- `23002a2` - project-coach-setup-base skill (conversational project initialization)
- Added trigger phrases to weekly skills for reliable invocation
- `3d5c180` - Add trigger phrases to weekly skills descriptions

**Documentation created:**
- `c623402` - PROJECT-SETUP.md and Alice demo content
- QUICKSTART.md for fast onboarding

**Outcome:** Architecture validated in production - proceed with confidence

---

## Phase 5: Architecture Decision Point (Dec 1-2, 2025)

### Critical Question: How to Handle Personal Repo?

**Context:** Preparing for public release (Dec 12th presentation)

**The problem:** Need to separate public base skills from private personal data, but maintain good development workflow

### Decision Analysis (Dec 1)

**Created:** `DECISION-PERSONAL-REPO-PATTERN.md` (459 lines)

**Options evaluated:**
- **Pattern A: Submodule** - `personal/` as git submodule
  - Pros: Single clone, CLAUDE.md auto-loads, familiar pattern
  - Cons: Submodule reference updates, complexity for adopters

- **Pattern B: Sister Directories** - Independent sibling repos
  - Pros: No cross-repo references, simpler git workflow, each repo independent
  - Cons: Longer paths, manual setup, CLAUDE.md loading unknown

**Decision matrix:** 8 criteria evaluated (workflow simplicity, git complexity, etc.)

**Critical unknowns identified:**
1. Does CLAUDE.md auto-load from child when running from parent workspace? (MAKE OR BREAK)
2. Is path complexity acceptable for git simplicity benefit?
3. Where should users actually work day-to-day?

**F33: Sister Directories Pattern Validation** - Created to resolve unknowns

### Security Audit (Dec 1)

**Created:** `AUDIT-FINDINGS-2025-12-01.md`

**Scope:** Pre-public-release security review
- Scanned for personal health data in files
- Reviewed git history for sensitive information
- Documented findings and remediation plan

**Outcome:** Identified need for git history squash before sharing

### Implementation (Dec 1-2)

**Sibling directories pattern implemented:**
- `6b78443` - Remove personal/ submodule - use sister directories pattern
- `4d2d599` - Update documentation for sister directories pattern
- Created parent workspace CLAUDE.md example
- `65e5056` - Add F33: Sister Directories Pattern Validation

**Bridge approach (Dec 2):**
- **Problem:** Realized full F34 (parent workspace as public repo) was premature
- **Solution:** Bridge documentation supporting BOTH standalone and parent workspace
- `f7ab1e5` - docs: Add bridge documentation for standalone + parent workspace usage
- Removed "ALWAYS parent workspace" requirement
- Made parent workspace optional/advanced

**F34: Parent Workspace as Public Repo** - Deferred pending user feedback

**Outcome:** Repository works standalone OR with parent workspace - maximum flexibility

---

## Phase 6: Public Release Preparation (Dec 2, 2025)

### Cleanup & Simplification

**F32: Remove Git Operations from skill_workflow.py**
- `d7af33c` - Simplify skill_workflow.py: Remove git operations (F32)
- Users can use standard `git add` and `git commit`
- Core workflow: pack/unpack, not git automation
- YAGNI principle applied

**Documentation consolidation:**
- `988f682` - Clean up documentation for public release
- Deduplicated README/PROJECT-SETUP content
- Moved incomplete features to backlog
- Fixed path guidance to avoid cd/pwd confusion

**Requirements organization:**
- `5efcb81` - refactor: Move requirements.txt to scripts/ directory
- Better alignment with Python project conventions

### Merge to Main (Dec 2)

**Branch:** sibling_directories → main (fast-forward merge)

**Final state:**
- ✅ Works standalone (clone only `claude-as-coach`)
- ✅ Works with parent workspace (optional advanced pattern)
- ✅ Base + personal skill architecture validated
- ✅ Documentation supports both usage patterns
- ✅ Security audited, ready for F31 git squash

---

## Key Design Artifacts Created

These documents demonstrate architectural thinking and decision-making process:

1. **DECISION-PERSONAL-REPO-PATTERN.md** (459 lines)
   - Comprehensive analysis of submodule vs sister directories
   - Decision matrix with 8 evaluation criteria
   - Critical unknowns identified before implementation

2. **AUDIT-FINDINGS-2025-12-01.md**
   - Security review before public release
   - Personal data scanning and remediation

3. **FEATURE-sister-directories-pattern.md**
   - Implementation validation plan
   - Testing phases and go/no-go decision points

4. **FEATURE-parent-workspace-public-repo.md**
   - Future architecture options documented
   - Deferred with clear decision triggers

5. **docs/examples/parent-workspace-CLAUDE.md**
   - Parent workspace setup template
   - Preserved for users who want the pattern

---

## Design Principles Established

### 1. Separable Concerns
Base skills = shareable process frameworks
Personal skills = private metrics and context

### 2. Progressive Disclosure
Start simple (standalone) → advance to parent workspace when needed

### 3. User-Centered Scaling
- n=1 (author) - Use what works now
- n=10 (collaborators) - Streamline contribution workflow
- n=100 (adopters) - Minimize setup friction

### 4. Documentation-Driven Development
Major decisions captured in ADR-style documents before implementation

### 5. Reversible Decisions
- Git submodules → sister directories (implemented)
- Sister directories → parent workspace repo (deferred)
- Easy to undo if user feedback contradicts assumptions

---

## Technical Decisions Validated

### 1. Skill Composability
✅ `extends:` directive works in Claude.ai
✅ Base + personal skills merge cleanly
✅ Can refine each layer independently

### 2. Working Directory Flexibility
✅ Can work from child directory (standalone)
✅ Can work from parent workspace (advanced)
✅ Documentation supports both patterns

### 3. Git Workflow Simplification
✅ Sister directories = no submodule reference updates
✅ Each repo has independent history
✅ Simpler mental model for users

### 4. Vendor Integration
✅ anthropics/skills fork as submodule
✅ Automatic usage when available
✅ Fallback to manual ZIP if unavailable

---

## What This Timeline Demonstrates

**For potential colleagues/teams:**

1. **Iterative design thinking** - Willing to refactor when better patterns emerge (submodule → sister directories)

2. **Security-conscious development** - Proactive audit before public release

3. **Documentation-driven decisions** - 459-line decision analysis before major architectural change

4. **User-centered approach** - Explicit consideration of different user scales (n=1, n=10, n=100)

5. **Pragmatic engineering** - Bridge approach instead of premature full restructure (F34 deferred)

6. **Code quality focus** - YAGNI applied to remove unused git automation

7. **Portfolio-quality process** - This very changelog demonstrates thoughtful engineering practice

---

## Next Milestones

**Before Dec 12th presentation:**
- F31: Git history squash (remove personal data from history)
- F28: Rob the Runner demo persona (couch-to-5K sample data)
- F29: Sally the Software Engineer demo persona (interview prep)

**Post-presentation:**
- F26: Monthly rollup (daily→weekly→monthly fractal compression)
- F34: Revisit parent workspace architecture based on user feedback
- F30: Maya Mandarin Learner (microagent model evaluation)

---

*Timeline preserved: 2025-12-02
Before git history squash (F31)
Total commits: ~80 (will be squashed to single clean commit)*
