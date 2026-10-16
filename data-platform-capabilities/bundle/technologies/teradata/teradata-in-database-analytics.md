---
type: Technology
id: teradata-in-database-analytics
title: Teradata in-database analytics functions
description: Large library of SQL functions for data preparation, statistics, machine learning, time-series and path analysis that run in parallel inside the database, also callable from Python and R.
formerly: [ClearScape Analytics functions, Vantage Analytics Library]
platform: platform-teradata
kind: feature
availability: ga
realises: [in-database-ml, feature-engineering, time-series-data, geospatial-data, user-defined-functions]
resource: https://www.teradata.com/platform/in-database
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The teradataml Python and tdplyr R packages translate DataFrame code into in-database SQL. The Unbounded Array Framework handles time-series and signal processing. Avoids moving data out to separate ML tools.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development) (primary): Train and run models using SQL inside the data platform.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types): Store, index and analyse location and shape data with spatial types and functions.
- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga  
**Product family:** Teradata AI Studio

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md), [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
