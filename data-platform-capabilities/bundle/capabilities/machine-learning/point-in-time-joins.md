---
type: Capability
id: point-in-time-joins
title: Point-in-time correct joins
description: Join features as they were known at each training example's timestamp, preventing leakage of future data.
aliases: [as-of joins]
broader: [feature-store]
related: [time-travel, temporal-data, model-evaluation]
depends_on: [offline-feature-store]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A training example is a moment in time: customer 42 on 1 March, with a label saying whether they churned in the next 30 days. A point-in-time join attaches each feature's value as it stood at that moment, picking for every example the latest feature row timestamped at or before the example. A plain join on customer id would attach today's value instead, including information nobody could have had on 1 March.

That error is called data leakage. It makes a model look excellent in evaluation and then perform poorly in production, and it is one of the most common reasons models disappoint after release. The operation is an as-of join. Some SQL engines and DataFrame libraries support it directly; others need window functions over a range join, which is slow on large tables. Feature stores usually provide it as a built-in. Correctness also depends on timestamps that record when a value was known, not only when the underlying event happened.

# Key considerations

- Use the time a value became available to the platform, not only the business event time, or late-arriving data still leaks into training.
- As-of joins over billions of rows are expensive. Check whether the engine has a native operator or whether the feature store precomputes them.
- Feature tables must keep history. A table that overwrites values cannot support point-in-time joins at all.

# Questions to ask

- Have models performed noticeably worse in production than in evaluation?
- Do feature tables keep past values, or only the latest?
- Do your engines support as-of joins natively?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Feature store](feature-store.md) |
| Related | [Bitemporal data](../specialised-data/temporal-data.md), [Model evaluation](model-evaluation.md), [Time travel](../storage/time-travel.md) |
| Depends on | [Offline feature store](offline-feature-store.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 3) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Feature Store](../../technologies/aws/aws-sagemaker-feature-store.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning managed feature store](../../technologies/microsoft/azure-ml-managed-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Feature Store](../../technologies/google-cloud/gcp-agent-platform-feature-store.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Feature Store](../../technologies/snowflake/snowflake-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Feature Store](../../technologies/databricks/databricks-feature-store.md), [Databricks Feature Views](../../technologies/databricks/databricks-feature-views.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Feast](../../technologies/open-source/feast.md) |
