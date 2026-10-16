---
type: Capability
id: experimentation
title: Experimentation and causal measurement
description: Run controlled experiments with holdout groups and measure whether an action caused the outcome.
aliases: [A/B testing platform, uplift measurement]
broader: [analytics-bi]
related:
- canary-ab-testing
- behavioural-event-collection
- metric-definitions
- audience-activation
- ad-hoc-analysis
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In a controlled experiment, units such as users, stores or accounts are assigned at random to a control group or to one or more treatment groups, for example those who see a new checkout page switched on by a feature flag. Assignments are logged, outcomes such as conversion and revenue are joined to them, and statistical tests estimate the difference between groups with a confidence interval. A long-running holdout group that never receives a feature or campaign shows its combined effect over months. Where random assignment is impossible, quasi-experimental methods such as difference-in-differences estimate the effect from observational data.

Dashboards show correlation, not cause: customers who see a promotion may have been more likely to buy anyway. Experiments settle that question for product changes, pricing, marketing and operational policy. Warehouse-native designs compute results from platform tables and governed metrics instead of copying data into a separate tool. Model A/B testing is a narrower case that compares model versions in production.

# Key considerations

- Check that groups received the split you planned. A sample ratio mismatch, such as 52/48 when 50/50 was intended, usually means broken assignment or logging and invalidates the result.
- Checking results daily and stopping when they look good inflates false positives. Fix the sample size in advance or use sequential tests built for repeated looks.
- Choose the unit of randomisation with care. Randomising by session when people return, or by user when users influence each other, biases the estimate.
- Agree primary and guardrail metrics before launch, using the same definitions as reporting, so results are trusted and comparable across experiments.
- Variance reduction using pre-experiment data, such as CUPED, can shorten experiments considerably on noisy metrics.

# Questions to ask

- Which decisions are currently made from before-and-after comparisons that a controlled test could settle?
- Can the product or channel assign people to groups at random and log each assignment?
- How many users or units are available, and how long can an experiment run?
- Who signs off results, and where are they recorded so later teams can find them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Ad hoc analysis](ad-hoc-analysis.md), [Audience building and activation](../serving/audience-activation.md), [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Canary and A/B testing](../mlops/canary-ab-testing.md), [Governed metric definitions](metric-definitions.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [GrowthBook](../../technologies/open-source/growthbook.md) |
