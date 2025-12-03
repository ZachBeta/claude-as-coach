# F30: Maya Mandarin Learner (Microagent Eval Persona)

**Status:** Backlog - Post-Dec 12th
**Effort:** 7-11 hours (persona + model evaluation)
**Priority:** Medium (microagent evaluation phase)
**Created:** 2025-12-01

## Goal

Create demonstration persona for **language learning** (Mandarin Chinese) to evaluate coaching system across different language models, particularly Chinese frontier models.

## Persona Background

**Name:** Maya the Mandarin Learner

**Starting Point:** English speaker (native or fluent), beginner-level Mandarin (HSK 1-2)

**Goal:** Achieve conversational proficiency in Mandarin Chinese through structured daily practice

**Motivation:** TBD (career opportunity requiring Chinese? family/cultural connection? personal challenge? travel plans?)

**Key Challenges:**
- Tonal language acquisition (4 tones + neutral)
- Character recognition and writing (simplified vs traditional)
- Grammar patterns different from English
- Building vocabulary systematically
- Maintaining daily practice consistency
- Speaking confidence / pronunciation anxiety

## Model Evaluation Context

**Primary purpose:** Test coaching system portability to non-English-optimized models

**Models to compare:**
- **Claude Sonnet 4.5** - Baseline (current production model)
- **Kimi-k2** - Chinese frontier model (Moonshot AI)
- **Zai-GLM4.6** - Chinese frontier model (Zhipu AI)
- **Others TBD** - DeepSeek, Qwen, etc.

**Evaluation dimensions:**
1. **Coaching quality:** Insight depth, pedagogical approaches, cultural context
2. **Language-specific capabilities:** Tones, characters, grammar explanations
3. **Skill execution:** Base + personal skill pattern compatibility
4. **Summary quality:** Reflection depth, progress tracking
5. **Cross-model portability:** Do skills work without modification?

**Hypothesis:** Chinese models may provide richer Mandarin learning context, better character/tone guidance, and more culturally informed coaching.

## Deliverables (Future)

### Sample Documents

**Recent (Week 4 - Granular):**
- [ ] `Summary-[DATE]-Monday-W4-D1.md` - Character practice session
- [ ] `Summary-[DATE]-Wednesday-W4-D2.md` - Conversation practice
- [ ] `Summary-[DATE]-Friday-W4-D3.md` - Listening comprehension

**Mid-range (Weeks 2-3 - Weekly Compression):**
- [ ] `Weekly-Retro-[DATES]-W2.md` - Tones and pronunciation focus
- [ ] `Weekly-Retro-[DATES]-W3.md` - Sentence patterns and grammar

**Historical (Week 1 - Referenced):**
- Foundation week (Pinyin, basic greetings) referenced in retros

### Personal Skills

- [ ] `daily-summary-maya-personal.skill` - Language learning metrics (HSK level, character count, conversation time)
- [ ] `daily-morning-routine-maya-personal.skill` - Review flashcards, yesterday's vocabulary
- [ ] `weekly-retrospective-maya-personal.skill` - Topic mastery by HSK level
- [ ] `weekly-planning-maya-personal.skill` - Study focus areas for next week

### Project Setup

- [ ] `Project-Goals.md` for Maya's coaching project
- [ ] Study protocol documents (Anki flashcard workflow, conversation practice routine, tone drills)

## Data Scope

**Timeline:** 4 weeks (TBD dates post-Dec 12th)
- Week 1: Foundations (Pinyin, tones, basic characters)
- Week 2: HSK 1 vocabulary and sentence patterns
- Week 3: Expanding to HSK 2, simple conversations
- Week 4: Consolidation and speaking practice

**Key Metrics to Track:**
- **Characters Known:** Count, HSK levels (1-6)
- **Vocabulary:** Words memorized, retention rate (Anki intervals)
- **Tones:** Accuracy self-assessment (recording/feedback)
- **Conversation Time:** Minutes speaking with tutors/partners
- **Study Hours:** Listening, reading, writing, speaking breakdown
- **Comprehension:** Listening/reading materials consumed (graded readers, podcasts)
- **Confidence:** Self-rating per skill area (listening/speaking/reading/writing)

**Context Tags:** W#-D# format (W4-D1 = Week 4, Day 1)

## Sample Data Structure (Sketch)

### Daily Summary Example

```markdown
# Summary-[DATE]-Monday-W4-D1

## Key Numbers
- Characters reviewed: 25 (Anki)
- New characters learned: 5 (HSK 2)
- Conversation time: 20 min (italki tutor)
- Study hours: 2.5 (breakdown: 1h conversation, 1h Anki, 0.5h listening)
- Tone accuracy: 7/10 (self-assessed from recording)
- Confidence: Speaking 5/10, Listening 6/10

## Timeline
- 7:00 AM: Anki review (25 min)
- 8:00 AM: Work day
- 6:00 PM: italki conversation lesson (1 hour) - practiced ordering food
- 7:30 PM: ChinesePod podcast episode (30 min) - intermediate level
- 8:00 PM: New character practice (HSK 2 食物 food vocabulary)

## What Worked
- Tutor corrected my 吃 (chī) tone → now recognizing tone 1 vs tone 4 difference
- Listening to podcast after conversation lesson reinforced vocabulary
- Food vocabulary theme connected multiple learning modes (speaking, listening, writing)

## What Didn't Work
- Tried to learn 10 new characters → overwhelmed, dropped to 5
- Skipped tone drills this morning (paid for it in conversation - tutor corrected multiple times)
- Forgot to review yesterday's conversation notes before lesson

## Insights
- Tone accuracy improving when I record myself vs just listening
- Thematic vocabulary (food, travel) sticks better than random word lists
- Need warmup before conversation lessons (review notes, tone drills)

## Tomorrow's Focus
- Tone drills before work (10 min)
- Review today's conversation notes
- Continue food vocabulary theme (restaurant phrases)
```

### Weekly Retro Example

```markdown
# Weekly-Retro-[DATES]-W2

## What Worked This Week
- Consistent Anki reviews (5/5 days) - retention improving
- 2 conversation lessons (italki) - comfort speaking increasing
- Tone recording practice (3 days) - hearing own mistakes helps
- HSK 1 vocabulary solidifying (90% retention on review cards)

## What Didn't Work This Week
- Skipped writing practice (characters getting rusty)
- Too ambitious with new character count (30 in one week → only retained 20)
- Didn't prepare conversation topics ahead (lessons felt scattered)
- Sleep average 6.5 hours (tired during morning Anki sessions)

## Progress Toward Goal
- Week 2 of 12-week plan (aiming for HSK 2 conversational)
- Characters known: ~150 (HSK 1 complete, halfway through HSK 2)
- Vocabulary: ~250 words (HSK 1: 150, HSK 2: 100)
- Confidence: Listening 6/10 (+1), Speaking 5/10 (+1), Tones 6/10 (+2)

## Experiments to Try Next Week
- Writing practice: 5 characters/day (pen + paper, not just typing)
- Pre-prepare conversation topics for italki lessons
- Spaced repetition: reduce new cards to 5/day (quality over quantity)
- Language exchange partner (complement paid lessons)

## Gratitude
- Tutor patience with tone corrections
- Anki algorithm working (cards appearing at right intervals)
- Progress visible in ability to understand simple conversations
```

## Model Comparison Methodology (Future Work)

**Evaluation workflow:**

1. **Baseline run with Claude Sonnet 4.5:**
   - Create all sample documents using Claude
   - Note coaching insights, language explanations, cultural context

2. **Parallel run with Chinese models:**
   - Same input data, same skills, different model
   - Compare coaching quality, character explanations, tone guidance

3. **Cross-model skill compatibility:**
   - Test if skills execute without modification
   - Document any model-specific adjustments needed

4. **Qualitative comparison:**
   - Which model provides better pedagogical insights?
   - Which explains tones/characters/grammar more effectively?
   - Which incorporates cultural context naturally?

5. **Portability insights:**
   - Document microagent architecture requirements for model-agnostic operation
   - Identify skill patterns that work across models vs need tuning

**Success criteria:**
- Skills run on at least 2 non-Claude models without modification
- Documented comparison of coaching quality across models
- Informed design of model-agnostic skill patterns

## Open Questions

**Q1: What specific motivation drives Maya?**
- Career opportunity (business with China)?
- Family/heritage connection (reconnecting with roots)?
- Personal challenge (polyglot goal)?
- Travel plans (extended stay in China/Taiwan)?

**Q2: Traditional or Simplified Chinese?**
- Simplified (Mainland China focus) - more common for learners?
- Traditional (Taiwan, Hong Kong) - preserve cultural heritage?
- Both (ambitious but comprehensive)?

**Q3: Which Chinese model should be primary comparison?**
- Kimi-k2 (strong benchmarks, good API access)?
- Zai-GLM4.6 (newer, specialized capabilities)?
- Test both?

**Q4: How to access Chinese models for testing?**
- APIs available for Kimi/Zai?
- Need VPN/regional access considerations?
- Cost comparison vs Claude?

**Q5: Should Maya's data be bilingual (English + Chinese)?**
- Summaries in English with Chinese examples?
- Code-switching (natural for language learners)?
- Separate Chinese-language sections for authenticity?

## Timeline

**POST-DEC 12TH (Microagent Evaluation Phase):**
- Persona design complete (this document) ✅
- Create sample documents (TBD - 2-3 hours)
- Create personal skills (TBD - 1-2 hours)
- Model comparison testing (TBD - 3-4 hours)
- Document findings and portability insights (TBD - 1-2 hours)

**Total estimated:** 7-11 hours for complete evaluation

## Notes

**Why Maya for model eval:**
- Language learning is domain where Chinese models may have advantage
- Tests system's ability to handle non-English content/context
- Validates microagent portability claim from PROJECT-SETUP.md

**Connection to presentation narrative:**
- Rob (fitness), Sally (career), Maya (language) show domain breadth
- Maya validates "portable to any model" architecture claim
- Demonstrates system value beyond English-speaking contexts

**Design principle:**
- Realistic language learning journey (frustrations, plateaus, breakthroughs)
- Show system's value for domains requiring specialized knowledge
- Model comparison should inform future skill design (what works cross-model?)
