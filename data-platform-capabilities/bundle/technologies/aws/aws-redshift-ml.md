---
type: Technology
id: aws-redshift-ml
title: Amazon Redshift ML
description: Trains and runs machine learning models from Redshift SQL with CREATE MODEL, using SageMaker AI for training and Bedrock models for text tasks.
platform: platform-aws
kind: feature
availability: ga
realises: [in-database-ml, ai-functions, batch-inference]
resource: https://docs.aws.amazon.com/redshift/latest/dg/machine_learning.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Training is delegated to SageMaker Autopilot or bring-your-own models; inference runs as SQL functions inside the warehouse. The Bedrock integration lets SQL call LLMs for summarisation or classification.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development) (primary): Train and run models using SQL inside the data platform.
- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Bring Your Own Model (BYOM)](../teradata/teradata-byom.md), [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
