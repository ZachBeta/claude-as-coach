# Next Session - Start Here

**Last updated:** 2025-12-02
**Presentation deadline:** Dec 12th, 2025

<!--
MAINTENANCE NOTE:
This file is a FILTERED VIEW of FEATURES.md.
- Feature status, effort estimates, and details live in FEATURES.md (gold copy)
- Only update "Last Session Status" section in this file
- To update priorities: Edit FEATURES.md, then regenerate this view
-->

---

## Quick Decision: What Should I Work On?

**Got 30-45 min?** → [F33: Test sister directories pattern](#f33-sister-directories-pattern-validation) (BLOCKING F31)
**Got 2-2.5 hours?** → [F33 + F31: Architecture validation + git squash](#current-priorities) (ENABLES SHARING)
**Got 3-4 hours?** → [F28 or F29: Create demo persona content](#f28--f29-demo-content-creation) (for presentation)

---

## Current Priorities (Ready to Work On)

### 🔴 F33: Sister Directories Pattern Validation

**Status:** Active - BLOCKING F31 (git history squash)

**Why now:** Architecture implemented on 12/1 but never tested. Must validate CLAUDE.md auto-loading from parent workspace before F31 (point of no easy return).

**Next action:** Test CLAUDE.md loading from parent workspace (15 min GO/NO-GO), complete decision matrix, stabilize documentation.

→ [Full details in FEATURES.md](FEATURES.md#f33-sister-directories-pattern-validation)

---

### 🔴 F31: Git History Squash & Personal Data Audit

**Status:** Active - BLOCKED BY F33

**Why now:** Cannot share repo with acquaintances for pre-presentation testing until personal data is removed from history.

**Next action:** After F33 resolved, run file audit (30-45 min), execute single orphan commit squash (15-20 min), verify fresh clone.

→ [Full details in FEATURES.md](FEATURES.md#f31-git-history-squash--personal-data-audit) | [Implementation plan](features/FEATURE-git-history-squash.md)

---

### 🔴 F28 + F29: Demo Content Creation

**Status:** Active - Target: Dec 7-8 weekend

**Why now:** Presentation is Dec 12th. Need Rob (couch-to-5K runner) and Sally (interview prep engineer) sample documents to demonstrate fractal compression and domain breadth.

**Next action:** Create 3 daily summaries + 3 weekly retros for Rob, then repeat pattern for Sally.

→ [F28 Details](FEATURES.md#f28-rob-runner-demo) | [F29 Details](FEATURES.md#f29-sally-software-engineer-demo)

---

### 🟡 F26: November Monthly Rollup

**Status:** Active - Optional presentation enhancement

**Why valuable:** Demonstrates daily→weekly→monthly pattern with real data, strengthens presentation narrative.

**Next action:** Apply monthly retro structure to November's 4 weekly retros, validate design with real data.

→ [Full details](FEATURES.md#f26-monthly-retrospective-rollup) | [Design doc](design/MONTHLY-ROLLUP-DESIGN.md)

---

### 🟡 F24: Deployment Workflow Documentation

**Status:** Active - Quick win (30-45 min)

**Why valuable:** Document manual process for syncing refined skills from repo to Claude.ai production.

**Next action:** Add "Deploying Skills to Claude.ai" section to WORKFLOW-GUIDE.md with checklist and verification steps.

→ [Full details](FEATURES.md#f24-devprod-deployment-workflow)

---

### 🟢 F27: Skill Vendor Compliance Review

**Status:** Active - Optional quality improvement

**Why valuable:** Review remaining base skills against vendor conventions for demo quality. Already completed: project-coach-setup-base, weekly-planning-base, weekly-retrospective-base.

**Next action:** Review daily-morning-routine-base and daily-summary-base against vendor checklist.

→ [Full details](FEATURES.md#f27-skill-vendor-compliance-review)

---

## Last Session Status (2025-12-03)

**Completed:**
- ✅ F34 (Parent Workspace Public Repo) - Architecture questions captured and deferred to post-presentation
- ✅ F33 Phase 1 - CLAUDE.md auto-loads from parent workspace (GO decision confirmed)
- ✅ Personal data audit - Repository clean (1 minor issue already fixed)
- ✅ MIT LICENSE - Already present
- ✅ **F31 (Git History Squash) - COMPLETE!** 78 commits → 1 commit (`04b269a`)

**New:**
- F35 (Demo Script & Date Regeneration) - Added to address date brittleness in demo

**Ready for execution:**
- F35 (Demo date fix) - Can run in parallel with other work
- F28/F29 (Demo content) ready to start anytime

**Repo is now safe to share publicly!**

**Next priority:** F35 (demo dates) → F28/F29 (demo content)

---

## Critical Path to Public Release

**Minimum sequence (2-2.5 hours total):**

1. **F33 Phase 1:** Test CLAUDE.md loading (15 min) - GO/NO-GO decision
2. **F33 Phases 2-4:** Complete decision + stabilize docs (15-30 min)
3. **F31:** Git history squash + personal data audit (1.5-2 hours)

**Result:** Safe to share with friends/acquaintances before Dec 12th presentation.

---

## Reference Documentation

**Primary backlog:** [FEATURES.md](FEATURES.md) - Complete feature tracking with status, effort, and details

**Planning guides:**
- [WORKFLOW-GUIDE.md](WORKFLOW-GUIDE.md) - Development workflows
- [PROJECT-SETUP.md](../PROJECT-SETUP.md) - System overview for adopters
- [QUICKSTART.md](../QUICKSTART.md) - New user onboarding

**Feature details:** [features/](features/) - Detailed planning documents (exist during active work, deleted after completion)

---

## Notes

**Git history squash (F31):** Now correctly shown as BLOCKED by F33. Cannot proceed until sister directories architecture is validated/resolved.

**For presentation prep:** F28 (Rob) and F29 (Sally) are minimum viable demo content. F26 (monthly rollup) adds depth but is optional.

**For daily use:** Production skills are stable. No urgent changes blocking workflow.
