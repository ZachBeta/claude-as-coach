# Session Planning Instructions

## Purpose

Review project features and queue up work for the next session in NEXT_SESSION.md.

**State:** NEXT_SESSION.md (the session queue)

**Convention:** This follows the instructions/state pattern. See [../DOC-WORKFLOWS.md](../DOC-WORKFLOWS.md).

## Input Files

1. `docs/FEATURES.md` - Priority overview (High/Medium/Low, Active/Backlog)
2. `docs/features/*.md` - Individual feature docs with status and details
3. `docs/NEXT_SESSION.md` - Current state (what was completed, what's pending)
4. `FEATURE_HOUSEKEEPING.md` - Touch counter and housekeeping guidelines (same directory)

## Process

1. **Read FEATURES.md** - Understand current priorities:
   - Active: High Priority (core workflow reliability)
   - Active: Medium Priority (safety, UX, polish)
   - Backlog: Deprioritized or future items

2. **Scan feature docs** - Check status of items mentioned in FEATURES.md:
   - What's blocking?
   - What's ready to execute?
   - What needs research first?
   - Any high touch count features that should bubble up?

3. **Review NEXT_SESSION.md** - What was completed? What's still pending?

4. **Drain completed work to CHANGELOG** - Before updating NEXT_SESSION.md:
   - Move "Completed This Session" entries to CHANGELOG.md
   - This keeps NEXT_SESSION.md focused on future work
   - See [../DOC-WORKFLOWS.md](../DOC-WORKFLOWS.md) for the drain pattern

5. **Check for housekeeping triggers** - Per [FEATURE_HOUSEKEEPING.md](FEATURE_HOUSEKEEPING.md):
   - Any notes files to process?
   - Features that need touch counter updates?
   - Stale Active features to move to Backlog?

6. **Propose next session work** - Based on:
   - User's available time/energy (ask if unclear)
   - What's blocking vs ready
   - Natural task groupings
   - Skill development workflow needs

7. **Update NEXT_SESSION.md** with:
   - Clear immediate priority (1 main task)
   - 2-3 secondary tasks if time permits
   - Reference commands needed
   - Links to relevant feature docs

## Output Format

Keep NEXT_SESSION.md concise:

```markdown
# Next Session

**Last Updated:** YYYY-MM-DD

## Immediate Priority

[Main Focus] - 1 primary task with clear success criteria

## If Time Permits

- [Secondary task 1]
- [Secondary task 2]
- [Secondary task 3]

## Still Pending

- [Deferred items from previous session]

## Reference Commands

```bash
# Useful commands for this session
python scripts/skill_workflow.py pack skills/NAME-base/
```

## Related Features

- [F##: Feature Name](features/FEATURE-name.md)
```

## Usage

Invoke by asking Claude Code to:
- "plan next session"
- "queue up tomorrow's work"
- "what should I work on next?"
- "session planning"

## Integration with Housekeeping

Session planning is a natural trigger for housekeeping. Before planning:

1. Check if any features discussed recently need touch counter updates
2. Look for notes files that should be processed into features
3. Review if any Active features have gone stale

See [FEATURE_HOUSEKEEPING.md](FEATURE_HOUSEKEEPING.md) for full housekeeping process.

## Future: Skill Evolution

This instruction doc may evolve into a skill (`session-planning-base`) that can:
- Automatically scan feature docs and summarize status
- Suggest session focus based on touch counts and blockers
- Generate formatted NEXT_SESSION.md updates
- Track session completion rates over time
