# Workflow Conventions

Conventions for document-centric workflows used by Claude Code agents.

---

## Instructions vs State Pattern

Document-centric workflows separate two concerns:

- **Instructions ("code")** - Reusable process that rarely changes
- **State ("data")** - Current progress that changes frequently

This separation mirrors code/data separation in software:
- Instructions can be refined without losing state
- State can be reset without losing process knowledge
- Both can evolve independently

---

## Current Workflows

| Workflow | Instructions | State |
|----------|-------------|-------|
| Feature tracking | [FEATURE_HOUSEKEEPING.md](instructions/FEATURE_HOUSEKEEPING.md) | [FEATURES.md](FEATURES.md) |
| Session planning | [SESSION-PLANNING.md](instructions/SESSION-PLANNING.md) | NEXT_SESSION.md |
| Doc housekeeping | [DOC_HOUSEKEEPING.md](instructions/DOC_HOUSEKEEPING.md) | [DOC_HOUSEKEEPING_STATE.md](DOC_HOUSEKEEPING_STATE.md) |

---

## Naming Conventions

| Type | Pattern | Examples |
|------|---------|----------|
| Instructions | `*_HOUSEKEEPING.md`, `*-PLANNING.md` | FEATURE_HOUSEKEEPING.md, SESSION-PLANNING.md |
| State | Simple name or `*_STATE.md` | FEATURES.md, NEXT_SESSION.md, DOC_HOUSEKEEPING_STATE.md |

**Note:** State files may have simpler names when their purpose is clear (FEATURES.md, NEXT_SESSION.md). Use explicit `*_STATE.md` suffix when needed for clarity.

---

## CHANGELOG as Drain

**CHANGELOG.md** is the single source of truth for completed work.

All completed work flows to CHANGELOG:

| Source | Section | Drain to |
|--------|---------|----------|
| FEATURES.md | "Completed" section | CHANGELOG.md |
| NEXT_SESSION.md | "Completed This Session" | CHANGELOG.md |
| DOC_HOUSEKEEPING_STATE.md | Completion notes | CHANGELOG.md |

**Why centralize?**
- Single place to see project history
- Avoids scattered completion records
- Git-friendly (one file to track changes over time)
- Clear boundary: "Completed" sections are staging areas, CHANGELOG is permanent record

**When to drain:**
- During session planning (before updating NEXT_SESSION.md)
- During feature housekeeping (when moving items to Completed)
- During doc housekeeping (when clearing completed work)

---

## Workflow Interconnections

```
Session Planning
      |
      v
Feature Housekeeping (touch counters, status updates)
      |
      v
Doc Housekeeping (cross-reference audit, sync)
      |
      v
CHANGELOG.md (drain completed work)
```

**Triggers:**
- **Session planning** triggers feature housekeeping (check touch counters)
- **Feature completion** triggers doc housekeeping (update references)
- **All workflows** drain completed work to CHANGELOG

---

## Adding New Workflows

When creating a new document-centric workflow:

1. **Create instructions doc** - `docs/NEW_WORKFLOW.md` or `docs/instructions/NEW-WORKFLOW.md`
2. **Create state doc** - `docs/NEW_WORKFLOW_STATE.md` or simple name if clear
3. **Add to this table** - Update "Current Workflows" section above
4. **Define CHANGELOG drain** - Specify which sections drain to CHANGELOG

---

## References

- [FEATURE_HOUSEKEEPING.md](instructions/FEATURE_HOUSEKEEPING.md) - Feature tracking process
- [SESSION-PLANNING.md](instructions/SESSION-PLANNING.md) - Session planning process
- [DOC_HOUSEKEEPING.md](instructions/DOC_HOUSEKEEPING.md) - Documentation maintenance process
- [../CHANGELOG.md](../CHANGELOG.md) - Project history
