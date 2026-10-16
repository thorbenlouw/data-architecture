---
type: Reference
id: assessing-maturity
title: Running a maturity assessment
description: How to assess maturity with the tracks, from scope and evidence to scoring, gap analysis against use cases, presentation and re-assessment.
order: 8
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An assessment is worth doing when it shows where today's practice falls short of what the organisation's use cases need, and what to do first. It produces two things: a level on each relevant [maturity track](../maturity/index.md) for each part of the organisation, and a ranked list of gaps between current levels and the minimum levels that committed use cases require. The levels follow the [maturity scale](../maturity/maturity-scale.md).

# 1. Set the scope

- **Use cases first.** List the use cases the organisation runs or has committed to in the next year or so. Their required capabilities show which tracks matter: the *Where it appears* section of each capability page names the tracks that cover it and the level at which each first relies on it. Assessing all tracks at once is rarely worth the effort.
- **Units.** Choose the units to score separately, such as business domains, platforms or teams, wherever practice differs. A single platform-wide score hides the teams that need help.
- **People and time.** Name the assessors, a contact who supplies evidence for each unit, a time box (two to four weeks is typical) and the date the assessment describes.
- **Rules.** Agree in advance what counts as evidence and what "mostly met" means (step 3), so that scores are not renegotiated afterwards.

# 2. Gather evidence for each criterion

Each level of a track lists observable criteria. For every criterion and unit, record **met**, **partly met** or **not met**, with the evidence.

| Evidence | Examples |
|---|---|
| Configuration and system tables | Which tables have monitors, who holds which grants, which policies are attached to which tags |
| Repositories and build history | Tests that run on every change, review rules, deployment pipelines, contract checks |
| Run and incident history | Alerts raised, tickets opened, time to detect and resolve, failed and retried runs |
| Documents in use | Runbooks, contracts, approvals and validation reports that are current and followed |
| Interviews | Where to look and why things are as they are; not, on their own, proof that a criterion is met |

- Prefer what the platform shows over what people say.
- Sample instead of accepting the best example: check, for instance, the ten most used production tables or pipelines in each unit.
- Read the scope of each criterion. "Every production table" is not met by monitoring the important ones only.
- Note where evidence was thin, so readers know how far to trust a score.

# 3. Score each track

- A level is reached when its criteria are mostly met **and** every lower level is reached. A workable rule for "mostly": no criterion not met, and at most one only partly met.
- The score is the highest level reached. Level 1 describes ad hoc practice and is the floor.
- Do not skip levels. A unit with learned anomaly detection (data quality level 4) but no rules in its pipelines (level 2) scores level 1, and the anomaly detection is recorded as a strength to build on.
- Do not average criteria or levels. One strong practice does not make up for a missing foundation.
- The unmet criteria of the next level up are that unit's improvement backlog. Record them as you go.

# 4. Score per domain or unit

- Score each unit separately and show the results as a table of units against tracks.
- In a platform-wide summary, show the range, from the lowest unit to the highest, rather than an average. The lowest unit that runs a committed use case usually matters most.
- Where a central platform team provides something for everyone, such as monitoring or access control, assess it once and apply it to every unit. Note which criteria still depend on each unit's own practice.

# 5. Compare with use case minimum levels

1. For each use case in scope, take its *Required capabilities* table. The same data is in `dist/use-case-requirements.csv`, written by `python tools/dpc.py export`.
2. For the unit that will deliver the use case, rate each required capability on the same five-level scale. Use the criteria in the covering track that concern that capability, and the scale's general descriptions for the rest. A capability that is not practised at all scores 0.
3. Work out each gap as the minimum level minus the current level, where that is positive.

A track's "first relied on" level is not the level of the capability itself. The [MLOps](../maturity/track-mlops.md) track first relies on [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) at level 4, Measured, because that is when organisations typically adopt it across all models. One team that monitors one model's performance repeatably is at level 2 for that capability, which satisfies a use case needing level 2.

Rank the gaps. Put first those that:

- block a use case with a committed date;
- are shared by several use cases, so that one fix unblocks many;
- sit under capabilities that others depend on (the *Depends on* row on each capability page), such as [Inference logging](../capabilities/mlops/inference-logging.md) under performance monitoring;
- are two levels or more, which usually needs a funded piece of work rather than a change of habit.

Also note where a unit is well above what any of its use cases needs. Further investment there can wait.

# 6. Present the results

- Lead with the priority gaps, each with the use case it blocks, the evidence, a proposed action and an owner. Follow with the table of units against tracks, then the detail per track for those who want it.
- Show evidence and confidence next to every level, so a disputed score can be checked rather than argued.
- Describe the next level by its criteria, such as "freshness, volume and schema are monitored on every production table". That tells a team what to do; a number on its own does not.
- Avoid league tables between units. Their use cases need different levels, and the point is to target help.

# 7. Re-assess

- Repeat every six to twelve months, and after a major change such as a platform migration, a reorganisation, a new regulation or a newly committed use case.
- Start from the previous evidence sheet. Re-check criteria whose evidence may have changed and keep the earlier results for comparison.
- Report movement on the priority gaps rather than on overall averages.
- Review use case minimum levels at the same time, because use cases change too.

# Templates

**Evidence sheet**, one row per criterion per unit:

| Track | Unit | Level | Criterion | Status | Evidence | Assessed by, date |
|---|---|---|---|---|---|---|
| [Data quality and observability](../maturity/track-data-quality.md) | Retail | 2 | Quality incidents are logged in a tracker with an owner and status. | Met | Tracker holds 140 incidents since January, all with owners | Assessor name, 2026-10-12 |
| [Data quality and observability](../maturity/track-data-quality.md) | Retail | 3 | Freshness, volume and schema changes are monitored on every production table, not only those with hand-written rules. | Partly met | 58 of 120 production tables have monitors | Assessor name, 2026-10-12 |

**Gap sheet**, one row per required capability per use case:

| Use case | Capability | Minimum level | Current level | Gap | Evidence | Action and owner |
|---|---|---|---|---|---|---|
| [Churn prediction](../use-cases/usecase-churn-prediction.md) | [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | 3 | 2 | 1 | Training sets are built with each team's own SQL; no shared function | Use the shared point-in-time join for all churn features (ML platform team) |
| [Churn prediction](../use-cases/usecase-churn-prediction.md) | [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | 2 | 0 | 2 | Scores are not joined to outcomes | Log scores with customer ids and join them to churn outcomes monthly (retention data science) |
