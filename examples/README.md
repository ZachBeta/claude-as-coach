# Demo Personas

This directory contains fictional demo personas showing different use cases and workflows for the claude-as-coach system.

**All personas are synthetic (fictional) examples created for demonstration purposes.**

---

## Rob the Runner (Base Skills Only)

**Directory:** `rob-the-runner/`

**Demonstrates:**
- System works out-of-box WITHOUT custom personal skills
- Lower barrier to entry for new users
- Fractal compression pattern (daily → weekly → monthly)
- Ongoing practice (not just goal completion)

**Profile:**
- 39-year-old accountant, turning 40 soon
- Started: Sedentary, gained weight, winded playing with kids
- Goal: Completed couch-to-5K program (8 weeks)
- Post-program: Exploring yoga, maintaining running, figuring out "what's next"

**Content:**
- 3 daily summaries (Week 8 - program completion)
- 3 weekly retros (Weeks 5-7 - mid-program)
- 1 monthly rollup (October, Weeks 1-4 - early program)
- Week 9 planning + 2 daily summaries (post-program exploration)

**Key value:** Shows beginners don't need to create custom skills to get value from the system.

**Status:** Complete

---

## Alice the Athlete (Custom Skills)

**Directory:** `alice-the-athlete/`

**Demonstrates:**
- Extensibility via custom personal skill extensions
- How to add domain-specific metrics, protocols, and terminology
- Base + personal skill pattern

**Profile:**
- Couch-to-5K runner (similar domain to Rob, but with custom skills)
- Custom skills define: specific metrics tables, heart rate zones, recovery protocols, nutrition tracking

**Content:**
- Sample daily summaries with custom metrics
- Sample weekly retros
- Sample weekly plans
- Personal skill extensions (packed .skill files + source)

**Key value:** Shows how advanced users can customize the system for their specific needs.

**Status:** Complete (existing couch-to-5K example)

**Future evolution:** See [FEATURE-alice-crossfit-recovery.md](../docs/features/FEATURE-alice-crossfit-recovery.md) for planned CrossFit recovery persona.

---

## Gina the Grad Student (Skeleton - Content TBD)

**Directory:** `gina-the-grad-student/`

**Demonstrates:**
- System works for non-fitness domains (career transitions)
- Tracking complex multi-stage processes (job search pipeline)
- Balancing competing priorities (thesis + job search)

**Profile:**
- Graduate student (MS Computer Science)
- Graduating Spring 2026
- Goal: Land senior/staff engineer role in industry
- Tracks: Applications, interview prep, company research, offer evaluation

**Content:**
- README explaining persona (complete)
- documents/ directory (empty - content TBD post-Dec 12 presentation)

**Key value:** Shows the system adapts to different domains beyond fitness.

**Status:** Skeleton only (README complete, documents TBD)

---

## Comparison Matrix

| Persona | Domain | Skills Approach | Status | Purpose |
|---------|--------|----------------|--------|---------|
| **Rob** | Fitness (running + yoga exploration) | Base skills only | Complete | Shows out-of-box workflow |
| **Alice** | Fitness (couch-to-5K) | Custom personal skills | Complete | Shows extensibility |
| **Gina** | Career (job search) | TBD | Skeleton | Shows domain versatility |

---

## Using These Examples

**New users (start here):**
1. Review Rob's documents to see base skills in action
2. Try the base skills yourself before creating custom skills
3. Only create custom skills if base skills aren't enough

**Advanced users:**
1. Review Alice's custom skills to see extension patterns
2. Adapt her skill structure to your domain
3. See how base + personal skills work together

**Developers/contributors:**
1. Use these as templates for new demo personas
2. Add new personas showing different domains or workflows
3. Keep synthetic data clearly labeled as fictional

---

## Directory Structure

```
examples/
├── README.md                       # This file
├── rob-the-runner/
│   ├── README.md                   # Rob's background and narrative
│   └── documents/                  # Rob's daily summaries, retros, plans
├── alice-the-athlete/
│   ├── README.md                   # Alice's background
│   ├── documents/                  # Alice's daily summaries, retros
│   └── skills/                     # Alice's custom personal skills
└── gina-the-grad-student/
    ├── README.md                   # Gina's background (complete)
    └── documents/                  # Empty (TBD)
```

---

## Questions?

See the main project documentation:
- [PROJECT-SETUP.md](../PROJECT-SETUP.md) - Complete setup guide
- [README.md](../README.md) - Repository overview
- [WORKFLOW-GUIDE.md](../docs/WORKFLOW-GUIDE.md) - Daily workflows
- [QUICKSTART.md](../QUICKSTART.md) - Fast installation

---

**Remember:** All personas are fictional. This is demo data, not the author's personal information.
