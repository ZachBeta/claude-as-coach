# F34: Parent Workspace as Public Repository

**Status:** Proposed - Architecture decision deferred
**Effort:** TBD (depends on chosen option)
**Priority:** Medium (post-F33, post-F31)
**Created:** 2025-12-02

## Context

Currently `claude-as-coach-combined/` exists as a private parent workspace containing:
- `claude-as-coach/` - Public repo (could be submodule or sibling)
- `claude-as-coach-personal/` - Private repo (currently sibling directory)

**Question:** Should the parent workspace be published as a public repository to simplify onboarding?

## Problem Statement

**Current onboarding friction:**
- Users must manually create parent workspace directory
- Two separate clone operations required
- Parent-level documentation lives in child repo (awkward)
- Example workspace structure shown in docs but not versioned

**Benefits of public parent repo:**
- Single clone command gets full structure
- Parent-level CLAUDE.md and README provide workspace guidance
- Clear separation: workspace setup vs framework vs personal
- Submodule references handle child repos automatically

## Open Questions

### 1. Repository Structure Options

**Option A: Parent as main entry point (recommended)**
```
claude-as-coach/                    # Public parent workspace (main entry)
├── .gitmodules                     # References child repos
├── README.md                       # "Getting Started"
├── CLAUDE.md                       # Workspace-level guidance
├── framework/                      # Submodule → claude-as-coach-framework
│   └── (base skills, docs, scripts)
└── personal.example/               # Submodule → claude-as-coach-example
    └── (Rob/Sally demo data)
```

**Benefits:**
- Single clone with `--recurse-submodules` gets everything
- Clear naming: framework = shareable, personal = yours
- Parent README is the quickstart guide
- Users add their own private repo as sibling (not in .gitmodules)

**Option B: Keep current naming, publish parent**
```
claude-as-coach-combined/           # Public parent workspace
├── .gitmodules
├── claude-as-coach/                # Submodule (framework)
└── personal.example/               # Submodule (example)
```

**Benefits:**
- Less disruption to existing structure
- Just document workspace pattern better
- Users clone parent, then setup personal separately

**Option C: Stay with current sibling pattern (status quo)**
- No parent repo
- Manual workspace setup documented in child repo
- Users create `claude-as-coach-combined/` themselves

### 2. Naming Clarity

| Current Name | Option A Alternative | Purpose |
|--------------|---------------------|---------|
| `claude-as-coach-combined` | `claude-as-coach` | Main entry point |
| `claude-as-coach` | `claude-as-coach-framework` | Base framework |
| `personal.example` | `claude-as-coach-example` | Example data |
| `claude-as-coach-personal` | (unchanged) | User's private repo |

**Question:** Does renaming improve clarity enough to justify the migration?

### 3. Documentation Distribution

If parent is public, what moves where?

| Content | Current Location | Option A Location |
|---------|-----------------|-------------------|
| Quickstart | `claude-as-coach/PROJECT-SETUP.md` | Parent `README.md` |
| Workspace guidance | `claude-as-coach/CLAUDE.md` | Parent `CLAUDE.md` |
| Framework details | `claude-as-coach/README.md` | Framework `README.md` |
| Workflow guide | `claude-as-coach/docs/WORKFLOW-GUIDE.md` | Framework `docs/` |

### 4. Submodule vs Sibling for Personal Repo

**User's private personal repo:**
- Should it be in parent .gitmodules? (NO - privacy concern)
- Should it be a sibling directory? (CURRENT)
- Should users clone it manually after getting parent? (CURRENT)

**Example/demo repos:**
- Should these be submodules? (YES - part of getting started)
- Should Rob/Sally live in same repo or separate? (TBD)

### 5. Migration Impact

**If we rename/restructure:**
- Does it break existing users' workflows? (n=1 currently)
- Can we provide migration guide?
- What about git history preservation?
- Coordination with F31 (git squash)?

## Dependencies

**Blocked by:**
- F33 (Sister directories validation) - Must finalize architecture first
- F31 (Git history squash) - Major restructuring should happen together

**Informs:**
- F28, F29 (Demo personas) - Where do Rob/Sally repos live?
- PROJECT-SETUP.md updates
- QUICKSTART.md updates

## Recommendation

**Defer until after F33 + F31 complete.**

**Rationale:**
1. F33 will validate sister directories pattern (or revert to submodules)
2. F31 will squash git history (clean slate for restructuring)
3. Current documentation works for n=1 (author)
4. Can evaluate with real user feedback after Dec 12th presentation

**Post-presentation evaluation criteria:**
- User confusion during setup (n~10 friends testing)
- Number of onboarding questions about workspace structure
- Documentation clarity feedback
- Value vs disruption tradeoff

## Next Steps

**When ready to decide:**
1. Validate F33 results (sister directories vs submodules)
2. Complete F31 (clean git history)
3. Test current onboarding with 2-3 friends
4. Collect feedback on setup friction
5. Revisit this feature with real data

**If proceeding with Option A:**
1. Create new parent repo with appropriate README/CLAUDE.md
2. Rename child repos (framework, example)
3. Set up .gitmodules references
4. Migrate documentation
5. Update all cross-references
6. Test fresh clone workflow
7. Provide migration guide for existing users

## Open Discussion

**Key tension:** Simplicity for new users (Option A) vs. disruption to existing setup (Option C).

**Current state:** Works fine for n=1, but may not scale to n=10-100.

**Decision trigger:** User feedback after Dec 12th presentation. If 3+ people struggle with workspace setup, prioritize Option A.

---

**See also:**
- F33: Sister Directories Pattern Validation
- F31: Git History Squash
- docs/WORKFLOW-GUIDE.md (current workspace guidance)
