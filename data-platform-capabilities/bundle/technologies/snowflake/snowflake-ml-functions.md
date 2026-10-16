---
type: Technology
id: snowflake-ml-functions
title: Snowflake ML Functions
description: SQL-callable model classes for time-series forecasting, anomaly detection, classification and top insights, which train and run without ML code.
platform: platform-snowflake
kind: feature
availability: ga
realises: [in-database-ml, automl, augmented-analytics]
resource: https://docs.snowflake.com/en/guides-overview-ml-functions
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development) (primary): Train and run models using SQL inside the data platform.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [AutoML](../../capabilities/machine-learning/automl.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md), [Teradata Bring Your Own Model (BYOM)](../teradata/teradata-byom.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
