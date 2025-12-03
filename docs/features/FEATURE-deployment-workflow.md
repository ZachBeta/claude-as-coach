# F24: Dev→Prod Deployment Workflow

**Status:** Active - Documentation needed
**Effort:** Quick win (30-45 min)
**Priority:** High (addresses current friction)
**Created:** 2025-12-01

## Problem Statement

**User friction (n=1, current state):**
- Skills are actively developed and refined in `claude-as-coach` repository
- Production skills in Claude.ai Projects are running on older versions
- Gap between dev and prod creates "working but suboptimal" friction
- No documented process for syncing refined skills back to production

**Impact:**
- Mild but persistent friction in daily workflow
- Risk of forgetting which skills need syncing
- Uncertainty about safe deployment process

## Scope

**Phase 1 (This week - before Alice demo work):**
- Document manual copy-paste workflow
- Add to WORKFLOW-GUIDE.md as reference section
- Create pre-deployment checklist
- Clarify when to sync dev→prod

**Deferred to post-Dec 12th:**
- Automated tooling (F23 territory - production/development environment switching)
- Integration with skill_workflow.py deploy command
- Validation and testing automation

## Solution: Manual Workflow + Documentation

### Deployment Checklist

**When to deploy:**
- After completing skill refinements and testing locally
- Before using refined skills for actual work (retro/planning/summaries)
- When production friction becomes noticeable

**Pre-deployment validation:**
1. Repack skill: `python scripts/skill_workflow.py pack <skill-name>`
2. Verify .skill file created successfully
3. Check git status - is source tracked and committed?
4. Review recent changes: `git log -1 --stat skills/<name>/`

**Deployment steps:**
1. Open Claude.ai → Navigate to target Project
2. Go to Project Settings → Custom Skills
3. For existing skill: Click "..." → Replace → Upload new .skill file
4. For new skill: Click "Add skill" → Upload .skill file
5. Verify skill appears in skills list with correct name
6. Test skill trigger in a new chat

**Post-deployment verification:**
1. Test skill invocation: Type skill name/trigger in chat
2. Verify expected behavior (check against source SKILL.md)
3. Check for any error messages or unexpected prompts
4. Mark as deployed in local tracking (git tag or notes)

### Tracking Deployments

**Local tracking (optional but recommended):**

```bash
# Tag deployed versions
git tag prod-daily-summary-v1.0 -m "Deployed to claude.ai 2025-12-01"

# View deployed versions
git tag -l "prod-*"

# See what's changed since last deployment
git diff prod-daily-summary-v1.0 skills/daily-summary-base/
```

**Manual tracking file (alternative):**
Create `docs/DEPLOYED-SKILLS.md` with deployment log:

```markdown
# Deployed Skills Log

## 2025-12-01
- `daily-summary-base.skill` → Production Project
- `daily-summary-personal.skill` → Production Project
- Commit: abc1234
```

## Integration Points

**Related to:**
- **F17 Task 1**: Composability testing informs what needs to be deployed
- **F23**: Future automation of this workflow (post-Dec 12th)
- **F26**: Monthly rollup work may produce new skills to deploy

**Updates needed in:**
- `docs/WORKFLOW-GUIDE.md` - Add "Deploying Skills to Claude.ai" section
- `CLAUDE.md` - Reference deployment workflow

## Success Criteria

**For this feature:**
- [ ] Manual deployment workflow documented in WORKFLOW-GUIDE.md
- [ ] Pre-deployment checklist created
- [ ] Post-deployment verification steps defined
- [ ] Tracking strategy chosen (git tags or DEPLOYED-SKILLS.md)
- [ ] No ambiguity about when/how to sync dev→prod

**Evidence of success:**
- Can deploy a refined skill to production in < 5 minutes
- No forgetting which skills are out of sync
- Clear process reduces friction and uncertainty

## Timeline

**Target completion:** Dec 6 (before weekend Alice demo work)
**Actual time:** ~30-45 minutes to document workflow
**Next action:** Add deployment section to WORKFLOW-GUIDE.md

## Notes

**Why manual is acceptable:**
- n=1 (one user) means automation has low ROI right now
- Manual process is fast enough (< 5 min per skill)
- Builds understanding of deployment requirements for future automation
- F23 will add proper tooling after presentation, informed by manual experience

**Future automation considerations (F23):**
- `skill_workflow.py deploy` command could automate this
- Integration with production/development environment switching
- Validation and testing before upload
- Batch deployment of multiple skills
- MCP integration (F9) for programmatic upload to Claude.ai

---

**Related Features:**
- F17: Presentation Prep (Task 1 testing informs deployment needs)
- F23: Production/Development Workflow (future automation)
- F9: MCP Skill Manager (programmatic deployment)
