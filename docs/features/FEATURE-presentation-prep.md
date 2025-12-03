# FEATURE: Dec 12th Presentation Prep

**Status:** Active - Timeline-sensitive
**Effort:** Multi-phase (8-12 hours total)
**Priority:** High - Has deadline
**Timeline:** Dec 12th presentation (confirmed 2025-11-29 - avoiding personal conflict + NeurIPS)

## Goal

Prepare demonstration of Claude Projects skills system for casual (non-technical) audience. Enable attendees to set up their own Claude-as-coach project afterward.

## Naming Convention (Decided 2025-11-29)

**Production/Development pattern:**
- `production-*-personal.skill` - User's stable production skills
- `development-*-base.skill` - Shareable base frameworks
- `development-*-alice-personal.skill` - Alice couch-to-5K demo
- `development-*-bob-personal.skill` - Bob job interview demo (future)

**Key insights:**
- **Primary user need (n=1 → n=100):** Production vs development versioning
- **Alice/Bob examples:** Skill-developer-facing (framework development), not end-user tooling
- **Manual workflow acceptable:** Don't over-engineer tooling for demo examples
- **Tooling deferred:** F23 (production/dev automation) after Dec 12th, informed by n~10 feedback

## Presentation Scope

**Dec 12th - 45-65 min total:**
- 20-30min: Skills walkthrough (Claude Projects setup, skill files, daily/weekly system)
- 10-15min: "Here's where this is going" (microagent concept, portability to open weights)
- 10-15min: Production/development workflow (the n=1 → n=100 scaling challenge)
- 10-15min: Q&A/discussion

**Target audience:** New year's resolutioners - people setting goals in January who want sustainable infrastructure

**Demo approach:** Alice's couch-to-5K journey (relatable, sanitized, shows the system working)

**Future session (post-Dec 12th):**
- Live microagent demo (actually working)
- Deeper technical dive
- Scheduled before Christmas or early new year

## System Requirements

**Like video game system requirements, this project has minimum and recommended specs:**

### Minimum Requirements
- **Claude Pro** subscription
- Access to Claude Projects
- Ability to import custom skills to Projects

**Limitations at minimum:**
- May hit context length limits with extensive project history
- Lower rate limits may require waiting between operations
- Basic thinking mode (fast but less thorough)

### Recommended Requirements
- **Claude Max x5** subscription
- Extended thinking mode enabled
- Well within capacity limits for intensive daily use

**Benefits of recommended:**
- Extended context window handles months of summaries/retros
- Higher rate limits support back-to-back skill invocations
- Extended thinking provides deeper analysis and better synthesis
- More reliable for power users with extensive project data

**Tested in production:** This project is actively developed and used daily with Max x5 + extended thinking enabled.

## Priority Order

1. **Task 1: Composability test** (BLOCKING - affects architecture decisions)
2. **Task 4: PROJECT-SETUP.md** (most valuable artifact)
3. **Task 2: Base skills** (needed for demo)
4. **Task 3: Example artifacts** (nice to have)
5. **Task 6: Prepare for open source** (BLOCKING before repo is public - squash git history)
6. **Task 5: Demo project** (day-of setup may be fine)

---

## Task 1: Test Skill Composability (BLOCKING)

**Hypothesis:** Parent/child skill architecture allows base shareable skills + personal customization layers

**Questions to answer:**
1. Can Claude correctly compose a base skill (generic) with a personal skill (customized) when both are loaded?
2. Does frontmatter `name:` need to match .skill filename?
3. Do duplicate YAML names cause conflicts in Claude.ai?

**Critical for:** Production/development naming convention (F23 design)

### Test Procedure

#### Step 1: Prepare Skills

1. Create minimal base skill (e.g., `daily-summary-base.md`)
2. Create minimal personal extension (e.g., `daily-summary-personal.md`)
3. Pack both with naming convention: `coaching-{skill-name}-{variant}.skill`

**Naming convention (proposed):** `{project}-{skill-name}-{variant}.skill`
- Example: `coaching-daily-summary-base.skill`, `coaching-daily-summary-personal.skill`, `coaching-daily-summary-example.skill`
- Enables toggling skills on/off for demos (skills are global in Claude.ai, not project-specific)

#### Step 2: Import to Claude.ai

**Import process:**
1. Open your Claude.ai Project
2. Click on "Settings" or "Project Knowledge"
3. Look for "Custom Instructions" or "Skills" section
4. Import base framework skills first:
   - `coaching-daily-summary-base.skill`
   - `coaching-daily-morning-routine-base.skill`
5. Then import personal/example extension skills:
   - `coaching-daily-summary-example.skill`
   - `coaching-daily-morning-routine-example.skill`

**Note:** Import order may matter. If behavior is unexpected, try reversing the order (personal first, then base).

#### Step 3: Execute Test Cases

### Test Case A: Daily Summary Generation

**Setup:** Both `daily-summary-base` and `daily-summary-personal/example` skills imported

**Trigger:** Say "daily summary" or "generate summary" to Claude

**Expected Base Framework Behavior:**
- [ ] Date verification runs first (bash command with timezone)
- [ ] Asks: "Which date's summary are we generating?"
- [ ] Asks: "What's the context tag for this day?"
- [ ] Generates filename following pattern: `Summary-YYYY-MM-DD-DayName-tag.md`
- [ ] Creates document with all base sections:
  - Ground Truth header
  - TL;DR
  - Key Numbers table
  - Timeline
  - Insights & Learnings
  - Decisions Made
  - What Mattered This Day

**Expected Personal/Example Extension Behavior:**
- [ ] Key Numbers table includes personal metrics (from personal/example skill)
- [ ] Personal context tag patterns recognized
- [ ] Personal domain terminology appears naturally
- [ ] Personal thresholds mentioned when relevant

**Success Criteria:**
- Base framework provides structure ✓
- Personal metrics augment (don't replace) base ✓
- All base sections appear in output ✓
- File naming works correctly ✓

---

### Test Case B: Morning Routine

**Setup:** Both `daily-morning-routine-base` and `daily-morning-routine-personal/example` skills imported

**Trigger:** Say "good morning" in a new chat session

**Expected Base Framework Behavior:**
- [x] Date verification first (bash command)
- [x] States clearly: "Today is [Day], [Full Date]"
- [x] Searches for yesterday's summary with pattern `Summary-YYYY-MM-DD-*`
- [x] Confirms before attending to file
- [x] Generates two-tier brief:
  - Ground Truth section
  - Yesterday's Detail (expanded)
  - Yesterday's Snapshot (TL;DR)
  - Today's Focus (TL;DR)

**Expected Personal/Example Extension Behavior:**
- [x] Sleep data integration appears if available
- [x] Personal protocols mentioned when relevant
- [x] Personal capacity markers included
- [x] Personal thresholds interpreted

**Success Criteria:**
- Base framework provides process ✓
- Personal context adds relevant detail ✓
- Morning state recognition adapts appropriately ✓
- Brief structure maintains base format ✓

**Test Results - 2025-12-01 (Production Environment):**

✅ **COMPOSABILITY CONFIRMED - Pattern works in production**

**Skills tested:**
- `skills/daily-morning-routine-base.skill`
- `personal/skills/daily-morning-routine-personal.skill`

**Claude behavior:**
- Explicitly stated: "Let me read both the base and personal skills to follow the proper morning routine protocol"
- Successfully loaded both skills
- Merged content appropriately without conflicts

**Base framework observed:**
- ✅ Date verification executed (`TZ='America/New_York' date...`)
- ✅ Found yesterday's summary (`Summary-2025-11-30-Sunday...`)
- ✅ Generated structured brief with all sections
- ✅ Followed process steps from base skill

**Personal extensions observed:**
- ✅ Sleep data interpretation with thresholds (Deep: 47 min, Target: 60-90)
- ✅ Ketone threshold recognition (99ppm = stress signal vs 40-60 therapeutic)
- ✅ LC recovery context (Clear2 Day 3, PEM-protective hypothesis)
- ✅ Bootstrap protocols (honey + lite salt intervention tracking)
- ✅ Domain-specific metrics (chess ratings, PFC capacity, dopamine detox day)

**Key findings:**
1. **Extends directive recognized** - Personal skill has `metadata: extends: daily-morning-routine-base`
2. **Sequential loading works** - Both skills merge without explicit user instruction
3. **No conflicts** - Base framework structure maintained, personal content augments appropriately
4. **Natural integration** - Content flows smoothly, no jarring transitions

**Conclusion:** The base + personal skill pattern is production-ready. Users can safely separate generic frameworks from personal context.

---

### Test Case C: Extends Directive Behavior

**Goal:** Understand if `extends: base-skill-name` in frontmatter affects behavior

**Experiments:**

#### Experiment C1: With `extends:` directive
1. Verify personal/example skill has `extends: daily-summary-base` in frontmatter
2. Import both skills
3. Generate a daily summary
4. Document behavior

#### Experiment C2: Without `extends:` directive
1. Edit personal/example skill to remove `extends:` line from frontmatter
2. Repack skill
3. Re-import to Claude.ai
4. Generate a daily summary
5. Compare behavior to Experiment C1

#### Experiment C3: Import order
1. Try importing personal/example skill BEFORE base skill
2. Test daily summary generation
3. Compare behavior

**Questions to Answer:**
- Does `extends:` directive change Claude's behavior?
- Is sequential loading sufficient (both loaded, order doesn't matter)?
- Does import order affect which content takes precedence?

**Document findings:**
```
[Test results to be filled in after testing]

extends: directive effect:
-

Import order effect:
-

Recommended approach:
-
```

---

### Test Case D: Frontmatter Name Matching

**Goal:** Determine if `name:` in frontmatter must match .skill filename

**Critical for:** Production/development naming convention design

#### Experiment D1: Matching names (baseline)
1. Pack skill with `name: daily-summary-base` in frontmatter
2. Filename: `development-daily-summary-base.skill` (name matches after prefix)
3. Import to Claude.ai
4. Test functionality
5. Document behavior

#### Experiment D2: Non-matching names
1. Pack skill with `name: daily-summary-base` in frontmatter (unchanged)
2. Filename: `production-daily-summary-base.skill` (different prefix)
3. Import to Claude.ai
4. Test functionality
5. Compare with D1

#### Experiment D3: Completely different names
1. Pack skill with `name: daily-summary-base` in frontmatter
2. Filename: `foobar.skill` (completely unrelated)
3. Import to Claude.ai
4. Test functionality
5. Document if Claude recognizes skill at all

**Questions to Answer:**
- Does Claude use filename or frontmatter `name:` for skill identification?
- Can we rename .skill files without editing source SKILL.md?
- Is `extends:` directive affected by filename vs frontmatter mismatch?

**Document findings:**
```
[Test results to be filled in]

Filename vs frontmatter name matching requirement:
-

Can rename .skill files independently: YES / NO
-

Extends directive affected: YES / NO
-

Recommended approach:
-
```

---

### Test Case E: Duplicate YAML Names

**Goal:** Test if two .skill files with identical frontmatter `name:` cause conflicts

**Scenario:** User has `production-daily-summary-personal.skill` and `development-daily-summary-personal.skill` both with `name: daily-summary-personal`

#### Experiment E1: Import both with same name
1. Pack two skills with identical `name: daily-summary-personal` in frontmatter
2. Different filenames: `production-daily-summary-personal.skill` and `development-daily-summary-personal.skill`
3. Import BOTH to same Claude.ai project
4. Test which one Claude uses (last imported? first? conflict error?)

#### Experiment E2: Preventative workaround
1. Pack two skills with DIFFERENT frontmatter names:
   - `name: production-daily-summary-personal`
   - `name: development-daily-summary-personal`
2. Different filenames match names
3. Import both to same project
4. Test toggling on/off to switch between versions

**Questions to Answer:**
- Does Claude.ai allow duplicate skill names?
- If yes, which skill takes precedence?
- Should we include environment prefix in frontmatter name?

**Document findings:**
```
[Test results to be filled in]

Duplicate names allowed: YES / NO
-

If allowed, which takes precedence:
-

Recommended naming pattern:
-
```

---

#### Step 4: Validation Checklist

**Skills Loaded:**
- [ ] Base skill appears in project knowledge
- [ ] Personal/example skill appears in project knowledge
- [ ] Both skills listed correctly in settings
- [ ] No error messages during import

**Content Integration:**
- [ ] Base framework sections all appear
- [ ] Personal metrics/thresholds mentioned
- [ ] No duplicate sections
- [ ] No missing expected content
- [ ] Content flows naturally (not jarring transitions)

**Functional Tests:**
- [ ] Date verification works (timezone correct)
- [ ] File naming follows pattern exactly
- [ ] Context tags work as expected
- [ ] Ground truth header appears
- [ ] All required sections present

**Quality Checks:**
- [ ] Formatting is clean (no broken markdown)
- [ ] No Unicode issues with emojis
- [ ] ASCII-safe characters used
- [ ] Tables format correctly
- [ ] Code blocks render properly

---

### Example Test Session

**Expected interaction:**

```
User: daily summary

Claude: [Date verification - runs bash command]
Today is Tuesday, November 26, 2025 - 10:45 AM EST.

Which date's summary are we generating?

User: today

Claude: Generating summary for Tuesday, November 26, 2025. Correct?

User: yes

Claude: What's the context tag for this day?

User: W5-D2

Claude: [Generates summary with structure from base, includes personal metrics if defined]

# Tuesday, November 26, 2025 - Daily Summary

**GROUND TRUTH:**
- Date: Tuesday, November 26, 2025
- W5-D2

---

## Key Numbers

| Metric | Morning | Evening | Notes |
|--------|---------|---------|-------|
| [Personal metrics from personal/example skill] | | | |

[... rest of summary following base framework structure ...]
```

**Validation:**
- ✓ Date verification ran
- ✓ Filename pattern prompted
- ✓ Base sections all present
- ✓ Personal metrics appeared in table
- ✓ Context tag system worked

---

### Troubleshooting

#### Issue: Only base framework appears, no personal content

**Possible causes:**
- Personal skill not actually loaded
- Personal skill loaded but not being referenced
- `extends:` directive not recognized

**Solutions:**
1. Check project settings - verify both skills imported
2. Try re-importing personal skill
3. Try importing in different order (personal first)
4. Check personal skill frontmatter format

#### Issue: Personal content completely replaces base

**Possible causes:**
- Import order wrong
- Skills conflict in some way
- Personal skill has duplicate sections

**Solutions:**
1. Verify personal skill only has extensions, not full duplication
2. Try reversing import order
3. Check for section name conflicts

#### Issue: Duplicate or confusing sections

**Possible causes:**
- Overlapping content between base and personal
- Both skills define same section headers
- Personal skill duplicates instead of extending

**Solutions:**
1. Review personal skill - should only add/extend, not duplicate
2. Ensure personal uses "Personal Extensions" or clear separation
3. Consider using different section names in personal

#### Issue: Extends directive seems ignored

**Possible causes:**
- Claude.ai may not support `extends:` directive yet
- Directive syntax incorrect
- Sequential loading may be default behavior

**Solutions:**
1. Test with and without directive to compare
2. Document actual behavior for future reference
3. Use import order to achieve desired behavior
4. Accept that sequential loading may be how it works

---

### Success Criteria

**The separation is working if:**
1. Both skills load without conflicts
2. Base framework structure is maintained
3. Personal content augments appropriately
4. Claude synthesizes both correctly without explicit instruction
5. Users can swap personal extensions easily
6. Base improvements benefit all users
7. Import process is straightforward

**If composability fails:**
- Fall back to single-file skills with "customize this section" placeholders
- Document limitation for presentation

---

### Status & Next Steps

**Status:** PARTIALLY COMPLETED - Test Case B validated 2025-12-01

**Completed:**
- ✅ Test Case B: Morning routine composability validated in production
- ✅ Confirmed base + personal skill pattern works
- ✅ Confirmed `extends:` directive recognized by Claude.ai
- ✅ System requirements documented

**Remaining tests:**
- Test Case A: Daily Summary Generation (validation in production)
- Test Case C: Extends directive behavior (with/without, import order)
- Test Case D: Frontmatter name matching (critical for F23 design)
- Test Case E: Duplicate YAML names (preventative measure)

**Next session tasks:**
1. Test daily-summary skills in production (Test Case A)
2. Optional: Execute remaining test cases C, D, E for deeper understanding
3. Decision: Upgrade remaining skills to base/personal pattern OR proceed with presentation prep
4. Estimated remaining: 30-45 min

---

## Task 2: Create Base Skill Versions

**Purpose:** Strip personal details from current skills, create shareable base versions

**Source skills (current, in personal submodule):**
- `personal/skills/daily-morning-routine-personal/SKILL.md`
- `personal/skills/daily-summary-personal/SKILL.md`
- Weekly retrospective skill
- Weekly planning skill

**What to strip:**
- Connecticut/EST timezone references → generic "user's timezone"
- Recovery/health-specific context → generic "personal project" framing
- Specific file naming patterns (FeedC1, dopamine detox days) → customizable placeholders
- Any references to specific health protocols

**What to keep:**
- Core process (date verification, framework generation, conversational fill-in)
- Trigger phrases
- Success criteria
- Edge case handling
- The "why" behind each step

**Output location:** In this repo
- `examples/skills-base/daily-morning-routine-base.md`
- `examples/skills-base/daily-summary-generator-base.md`
- `examples/skills-base/weekly-retrospective-base.md`
- `examples/skills-base/weekly-planning-base.md`

**Status:** Not yet started

---

## Task 3: Create Alice Example Content (Couch-to-5K)

**Purpose:** Demonstrate the system working with relatable, sanitized example content

**Persona:** Alice - starting a couch-to-5K running program (relatable, non-technical)

**Examples needed:**
- 2-3 daily summaries (W1-D1, W1-D3, W2-D1 - showing progression)
- 1 weekly retro (Week 1 reflection - structure and content)
- 1 weekly plan (Week 2 planning - Level 0-3 framework with running goals)

**Example metrics for Alice:**
- Running: distance, time, perceived effort
- Energy levels: morning, evening
- Motivation: confidence scores
- Recovery: rest days, soreness notes

**Output location:** In this repo
- `personal.example/documents/` (flat structure, matches Claude.ai UI)
  - `Summary-2025-W1-D1-Monday.md`
  - `Summary-2025-W1-D3-Wednesday.md`
  - `Summary-2025-W2-D1-Monday.md`
  - `Retro-2025-W1.md`
  - `Plan-2025-W2.md`
- `personal.example/skills/` (alice personal extensions)
  - `alice-daily-summary-personal/SKILL.md`
  - `alice-daily-morning-routine-personal/SKILL.md`
  - `alice-weekly-retro-personal/SKILL.md`
  - `alice-weekly-planning-personal/SKILL.md`

**Workflow:**
1. Create alice SKILL.md source files with couch-to-5K metrics
2. Create example summaries/retros using realistic C25K content
3. Pack as `development-*-alice-personal.skill`
4. Manual workflow acceptable - no special tooling needed

**Status:** Not yet started (weekend work)

---

## Task 4: Write PROJECT-SETUP.md

**Purpose:** The "start here" guide for someone setting up their own Claude-as-coach project

**Sections needed:**

### 1. What This Is
- Brief explanation of the system
- What problems it solves (context continuity, structured reflection, sustainable habits)
- Who it's for (people wanting AI-assisted goal tracking/reflection)

### 2. Quick Start (5 minutes)
- Create new Claude Project
- Upload skill files to skills folder
- Say "gm" to test morning routine
- That's it - you're running

### 3. The Core Loop
- Morning: "gm" → morning brief
- End of day: "daily summary" → summary generated
- End of week: "weekly retro" → reflection conversation
- Start of week: "weekly planning" → plan generated

### 4. Project Structure
```
/skills/
  daily-morning-routine.md
  daily-summary-generator.md
  weekly-retrospective.md
  weekly-planning.md

/project-files/
  [Your summaries accumulate here]
  [Your retros accumulate here]
  [Your plans accumulate here]
  Monthly-Plan.md (optional)

/instructions/
  [Project-level customizations]
```

### 5. Customization
- How to modify skills for your context
- Adding your own context tags
- Adjusting trigger phrases
- Adding domain-specific sections

### 5.5. Production/Development Workflow (IMPORTANT)
- **Problem:** Claude.ai skills are global - testing changes breaks your production workflow
- **Solution:** Use production-*.skill and development-*.skill variants
- **Workflow:**
  1. Copy your production skill → create development variant
  2. Edit development variant to test changes
  3. Toggle development ON, production OFF in Claude.ai settings
  4. Test changes in your project
  5. Once validated → update production skill
  6. Toggle production ON, development OFF
- **Future:** F23 tooling will automate this (post-Dec 12th)
- **This scales:** Everyone needs this workflow (n=1 → n=100)

### 6. Tips
- Start simple (just morning + summary for first week)
- Don't force it - skip days when needed
- The system adapts to you, not vice versa
- Context management: archive old summaries to keep project lean

### 7. Where This Is Going (Teaser)
- Microagent: Same pattern, any model with tool calling
- Open source (MIT license)
- Community sharing of skill templates

**Output location:** In this repo
- `PROJECT-SETUP.md` (root level)

**Status:** Not yet started

---

## Task 5: Demo Project Setup

**For live demo, create fresh Claude Project with:**
- Base skills uploaded
- 2-3 prefilled example summaries (to show the pattern working)
- PROJECT-SETUP.md as reference
- Clean slate for demonstrating "gm" and "daily summary" triggers

**Challenge:** Date dynamics
- Skills verify current date
- Prefilled summaries have fixed dates
- May need to note "these are examples from [date range]" in demo

**Workaround options:**
1. Disable date verification in demo skills (less realistic but cleaner demo)
2. Keep date verification, explain the date mismatch during demo
3. Generate fresh summaries day-of (requires cognitive capacity)

**Status:** Not yet started (day-of setup may be sufficient)

---

## Task 6: Prepare Repository for Open Source

**Purpose:** Clean git history and ensure no personal data before making repo public

**CRITICAL:** Git history may contain personal health data from early commits. Must be cleaned before open sourcing.

**Approach:**
1. **Git history squash:** Squash all history into single initial commit to remove personal data
2. **Audit current files:** Verify no personal data in current tree (should be clean after base skill creation)
3. **License:** Add MIT license file
4. **README:** Update with project overview, setup instructions, link to PROJECT-SETUP.md

**Timing:** Before presentation (if repo will be shared) OR after presentation before broader announcement

**Commands for squashing:**
```bash
# Create orphan branch with clean history
git checkout --orphan clean-history
git add -A
git commit -m "Initial commit: Claude-as-coach base skills and documentation"

# Replace main branch
git branch -D main
git branch -m main
git push -f origin main
```

**Verification checklist:**
- [ ] No personal health data in any current files
- [ ] Git history contains no personal data
- [ ] MIT license file present
- [ ] README.md updated for public consumption
- [ ] All base skills use generic placeholders
- [ ] Example artifacts use fictional persona only

**Status:** Not yet started - **BLOCKING before open source**

---

## Repository Deliverables

**This repo should contain:**
- `/examples/skills-base/` - Base skill files (shareable)
- `/examples/demo-artifacts/` - Sanitized example artifacts
- `PROJECT-SETUP.md` - Start here guide (root level)
- `README.md` - Repo overview, license (MIT) - needs update
- `LICENSE` - MIT license file (add if not present)
- `MICROAGENT.md` - Teaser for future work (optional)

**NOT in public repo:**
- `personal/` submodule (remains private)
- Any git history with personal data (squashed)

**Microagent repo:** Separate, for future session (not needed for Dec 5th)

---

## Decision Points

**By Tue/Wed Dec 2-3:**
- [ ] Go Dec 5th or push to Dec 12th?
- [ ] Based on: Clear2 recovery, FeedC2 Phase A stability, cognitive capacity for prep

**During prep:**
- [ ] Does composability work? (Affects architecture)
- [ ] Is PROJECT-SETUP.md clear enough for cold start?
- [ ] Do example artifacts feel real or contrived?

---

## Implementation Phases

### Phase 1: Validation (BLOCKING)
- [ ] Task 1: Test skill composability in fresh Claude Project
- [ ] Document findings
- [ ] Decide architecture (composable vs single-file)

### Phase 2: Documentation (High Value)
- [ ] Task 4: Write PROJECT-SETUP.md
- [ ] Update README.md with presentation context
- [ ] Add MIT license if not present

### Phase 3: Base Skills
- [ ] Task 2: Create base versions of 4 core skills
- [ ] Strip personal details, add customization placeholders
- [ ] Test base skills in fresh project

### Phase 4: Examples (Nice to Have)
- [ ] Task 3: Create fictional persona "Alex"
- [ ] Generate 3 example artifacts
- [ ] Review for realism and clarity

### Phase 5: Prepare for Open Source (BLOCKING before public)
- [ ] Task 6: Audit all current files for personal data
- [ ] Squash git history to remove personal data from commits
- [ ] Add MIT LICENSE file
- [ ] Update README.md for public consumption
- [ ] Verify personal/ submodule is not included in public repo
- [ ] Test fresh clone to ensure no personal data leaks

### Phase 6: Demo Prep (Day-of)
- [ ] Task 5: Set up fresh Claude Project for demo
- [ ] Upload skills and examples
- [ ] Practice trigger phrases
- [ ] Prepare for date dynamics edge cases

---

## Success Criteria

**After this feature:**
- [ ] Composability tested and documented
- [ ] PROJECT-SETUP.md written and clear
- [ ] 4 base skills created and tested
- [ ] 3 example artifacts created
- [ ] **Git history cleaned and repo ready for open source** (CRITICAL)
- [ ] Demo project ready
- [ ] Presentation ready for Dec 5th (or 12th)
- [ ] Attendees can go home and set up their own project
- [ ] Public repo contains no personal data

---

## Notes

- Presentation is curation, not creation - the system already exists and works
- Target: Someone can watch presentation, go home, set up their own project
- New year's resolution timing hook - "sustainable infrastructure for goals"
- Microagent becomes "here's what I'm building next" teaser, reduces scope pressure
- Practice demos to friends next week will reveal gaps in documentation
