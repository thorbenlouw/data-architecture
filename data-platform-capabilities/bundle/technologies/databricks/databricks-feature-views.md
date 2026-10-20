---
type: Technology
id: databricks-feature-views
title: Databricks Feature Views
description: Declarative feature definitions, including time-windowed aggregations over batch, streaming and request-time data, for which Databricks builds and runs the pipelines.
platform: platform-databricks
kind: feature
availability: ga
realises: [feature-engineering, point-in-time-joins]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/october
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA in October 2026 and recommended for new projects over hand-built feature tables. Feature Views can materialise to Lakebase for online use. Support for compliance security profile workspaces is due in mid-November 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development) (primary): Turn raw data into model inputs in reusable, consistent pipelines.
- [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) (Machine learning development): Join features as they were known at each training example's timestamp, preventing leakage of future data.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning managed feature store](../microsoft/azure-ml-managed-feature-store.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [Dataflow ML](../google-cloud/gcp-dataflow-ml.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Feature Store](../snowflake/snowflake-feature-store.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../../capabilities/machine-learning/point-in-time-joins.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Studio](../sas/sas-model-studio.md) | [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
