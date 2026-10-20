---
type: Capability
id: feature-engineering
title: Feature engineering
description: Turn raw data into model inputs in reusable, consistent pipelines.
broader: [machine-learning]
related: [stream-processing, transformation-as-code, dataframe-apis, data-quality-rules]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Raw records are rarely usable as model inputs. A list of card transactions becomes features such as the number of transactions in the last hour, average spend over 30 days, distance from the customer's home address, and merchant category encoded as numbers. The work covers aggregations over time windows, encoding categories, scaling numbers, filling or flagging missing values, and joining data about the same customer, device or product from several sources.

Building this as reusable pipelines, not notebook cells, matters because the same logic must run at training time and again when the model makes predictions. If training computes a 30-day average in SQL and the serving application recomputes it in Java, small differences in time zones or null handling feed the model inputs it never saw. Features can be computed in batch, on streams, or at request time from the request itself. Feature engineering defines the logic; a feature store manages the computed values and serves them.

# Key considerations

- Write feature logic once and run it in both training and serving, or test that both paths produce identical values for the same inputs.
- Window features must use only data available at the moment of prediction. Using later data inflates offline scores and then fails in production.
- Choose computation timing per feature. Batch is cheap but stale, streaming is fresh but costly, and request-time is freshest but adds latency.
- Version feature definitions. Changing the logic behind an existing name silently breaks models trained on the old version.

# Questions to ask

- How fresh must each feature be when the model uses it: daily, within minutes, or from the current request?
- Do several teams compute the same features independently today?
- Are the source systems that hold the useful signals already in the platform?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Data quality rules](../data-quality/data-quality-rules.md), [DataFrame APIs](../processing/dataframe-apis.md), [Graph data](../specialised-data/graph-data.md), [Stream processing](../processing/stream-processing.md), [Transformation as code](../processing/transformation-as-code.md) |
| Needed by | [Feature store](feature-store.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Canvas](../../technologies/aws/aws-sagemaker-canvas.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning managed feature store](../../technologies/microsoft/azure-ml-managed-feature-store.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery DataFrames](../../technologies/google-cloud/gcp-bigquery-dataframes.md), [Dataflow ML](../../technologies/google-cloud/gcp-dataflow-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Feature Store](../../technologies/snowflake/snowflake-feature-store.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Feature Store](../../technologies/databricks/databricks-feature-store.md), [Databricks Feature Views](../../technologies/databricks/databricks-feature-views.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata in-database analytics functions](../../technologies/teradata/teradata-in-database-analytics.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Model Studio](../../technologies/sas/sas-model-studio.md) |
