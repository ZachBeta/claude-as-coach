# F26: Monthly Retrospective Rollup

**Status:** Active - Manual exploration phase
**Effort:** Path B (2-3 hours for manual rollup + skill design)
**Priority:** Medium-High (valuable exploration + presentation enhancement)
**Created:** 2025-12-01

## Problem Statement

**New timescale reached:**
- First time reaching monthly scale in claude-as-coach system
- November 2025 complete with 4 weekly retros
- Fractal pattern needs to extend: daily→weekly→monthly→quarterly
- No existing skill or process for monthly compression

**Design already scoped:**
- Detailed process design exists: `docs/design/MONTHLY-ROLLUP-DESIGN.md`
- Proposed output structure defined
- Document lifecycle table created
- Archival workflow designed
- 5 open questions identified for validation

## Solution: Validate Design → Extract Skill Pattern

### Phase 1: Manual November Rollup (This Week)

**Approach:** Validate proposed design with real November data, answer open questions empirically

**Available data sources:**
- **Weekly Retros:** 4 weekly retros from November (Weeks 3-6, Nov 3-30)
- **Weekly Plans:** 3 weekly plans (Weeks 5-7)
- **Monthly Plan:** November-2025-Plan.md (monthly intentions)
- **Reference docs:** Protocol documents and tracking files
- **Synthesis artifacts:** Monthly summary documents

**Process:** (following proposed structure from design doc)
1. Apply proposed output structure (TL;DR → Monthly Arc → What Worked/Didn't → Metrics → Trajectory → Next Month)
2. Test "Plan vs Actual" section (Option A: explicit comparison in retro)
3. Validate compression principle (don't re-read dailies, trust weekly retros)
4. Test trajectory assessment (October → November comparison)
5. Answer 5 open questions empirically through practice
6. Document what worked and what needs adjustment

**Deliverables:**
- `personal/documents/Retro-2025-11-November.md` (real data, private)
- Sanitized example artifact for presentation demo purposes
- Validation report: answers to 5 open questions from design doc
- Recommended adjustments to proposed structure

**Estimated time:** 2-3 hours

**See also:** `docs/design/MONTHLY-ROLLUP-DESIGN.md` for complete design rationale

### Phase 2: Skill Design (Following Week)

**After validating design through manual rollup:**

**Decision: Separate skill, parameterized skill, or manual-only?**

**Option A: Separate monthly-retrospective skill**
- Pros: Explicit, clear, single-purpose, matches validated structure
- Cons: More files to maintain, potential duplication with weekly-retro

**Option B: Generalize retro skill with timescale parameter**
- Pros: Elegant, DRY, single source of truth
- Cons: More complex skill design, may obscure timescale-specific moves

**Option C: Manual-only (no skill yet)**
- Pros: Don't prematurely abstract, wait until quarterly scale emerges
- Cons: Can't reuse process, documentation-only doesn't guide execution

**Decision informed by:**
- Did manual process match proposed structure, or need significant adjustment?
- Are month-specific analytical moves different enough from weekly?
- Does the proposed structure feel natural with real data?
- Would parameterizing by timescale lose important structure?

## The Fractal Pattern

```
Daily summaries (7) → Weekly retro (compress) → Archive dailies
Weekly retros (4-5) → Monthly retro (compress) → Archive weeklies
Monthly retros (3) → Quarterly retro (compress) → Archive monthlies
```

**Key principle:** Each rollup compresses the scale below, making context manageable

**Why this matters for presentation:**
- Shows the system working at multiple timescales
- Demonstrates fractal compression in action with real data
- Validates the architecture beyond toy examples
- November data is genuine, not contrived for demo

## Output Artifacts

### Personal Artifact (Private Submodule)

**Location:** `personal/documents/Retro-2025-11-November.md`

**Structure (from design doc - to be validated):**
```markdown
# November 2025 Monthly Retrospective

**Month:** November 1-30, 2025
**Context:** [Month X of project timeline]

## TL;DR - Month Summary
[3-5 bullet executive summary]

## Monthly Arc
[Narrative of how the month unfolded - week by week progression]

## What Worked (Patterns Across Weeks)
[Recurring wins, validated experiments, capacity patterns]

## What Didn't Work (Persistent Challenges)
[Recurring struggles, failed experiments, constraint discoveries]

## Key Metrics / Progress
[Measurable changes: capacity, habits, portfolio, health markers]

## Plan vs Actual (Testing Option A)
**Planned priorities:** [From November-2025-Plan.md]
**What actually happened:** [Actual outcomes]
**Learning:** [What this teaches about planning accuracy]

## Trajectory Assessment
**Last month:** [October state]
**This month:** [November state]
**Direction:** [Better / Stable / Worse]
**Evidence:** [What supports this assessment]

## Next Month Setup
[What this month's patterns suggest for December focus]

## Archive Note
[What weekly retros can be archived after this rollup exists?]
```

**See:** `docs/design/MONTHLY-ROLLUP-DESIGN.md` for complete structure rationale and alternatives

### Presentation Example (Public)

**Location:** `examples/alice-monthly-rollup.md` or in presentation materials

**Content:** Sanitized version showing the pattern working
- Couch-to-5K context (not personal health data)
- Shows monthly compression in action
- Demonstrates value of fractal timescales

## Integration with Presentation

**Relationship to F17 (Dec 12th Presentation):**
- **Nice-to-have, not essential** for demo
- Alice demo (couch-to-5K, 8 weeks) doesn't reach monthly scale
- BUT: Real monthly rollup strengthens credibility
- Shows: "I'm using this system at scale, not just building toy examples"

**If included in presentation:**
- Brief mention: "Here's my November rollup - system works at month scale"
- Visual: Show fractal pattern with real data points
- Don't over-emphasize (focus remains on Alice demo)

**If not included:**
- Still valuable for personal use
- Informs skill design for future
- Provides insight into what matters at scale

## Success Criteria

**For manual rollup:**
- [ ] November monthly retro artifact created
- [ ] Analytical process documented (what moves were valuable?)
- [ ] Archiving strategy identified (do weeklies stay or go?)
- [ ] Skill design questions answered (A, B, or C?)

**For skill design:**
- [ ] Decision made: separate skill, parameterized skill, or manual-only
- [ ] If skill: frontmatter and structure drafted
- [ ] If manual: process documented for next month (December)

**Evidence of success:**
- Can articulate what's valuable at month scale vs week scale
- Have reusable process for future monthly rollups
- Personal system now works effectively at three timescales (daily/weekly/monthly)

## Timeline

**Manual rollup:** Dec 2-6 (this week, before weekend Alice work)
**Skill design decision:** Dec 9-11 (following week, if time permits)
**Target completion:** Before Dec 12th presentation (optional inclusion)

## Open Questions to Validate Through Manual Process

From `docs/design/MONTHLY-ROLLUP-DESIGN.md`:

1. **Plan comparison:** Worth formalizing (Option A: explicit section in retro) or let it be implicit (Option C)?
2. **Archive timing:** Immediately after rollup, or batch at month end?
3. **What to keep in project:** Most recent week's retro + monthly? Or just monthly?
4. **Cross-month context:** How much of previous month (October) needed for trajectory assessment?
5. **Quarterly rollup:** Same pattern will work, or different structure needed (fewer data points)?

**Additional validation questions:**
- Does the proposed structure feel natural with real data?
- Is "What Worked / What Didn't Work" still the right framework at month scale?
- Does TL;DR → Arc → Patterns → Trajectory flow work?
- Is the "Trust the Compression" principle validated (don't re-read dailies)?

## Notes

**Why do this before Dec 12th:**
- November data is complete and fresh
- Natural timing (early December)
- Insight valuable for understanding system at scale
- May enhance presentation narrative (optional)
- Personally useful regardless of presentation

**Why validate manually:**
- Test proposed design with real November data
- Answer open questions empirically, not theoretically
- Discover adjustments needed before building skill
- Fast to validate (2-3 hours) vs building unvalidated abstraction
- See detailed design rationale: `docs/design/MONTHLY-ROLLUP-DESIGN.md`

**Relationship to quarterly scale:**
- Quarterly rollup won't be needed until Feb 2025
- Monthly process will inform quarterly design
- No need to solve quarterly now

---

**Related Features:**
- F17: Presentation Prep (potential enhancement to demo narrative)
- F23: Production/Development Workflow (monthly skill will need deployment)
- Weekly retro skills (F17 Task 2) will inform monthly skill design
