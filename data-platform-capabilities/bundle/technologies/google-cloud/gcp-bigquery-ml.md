---
type: Technology
id: gcp-bigquery-ml
title: BigQuery ML
description: Creates, trains, evaluates and runs machine learning models with SQL inside BigQuery, including imported and remote models.
platform: platform-google-cloud
kind: feature
availability: ga
realises:
- in-database-ml
- batch-inference
- hyperparameter-tuning
- model-explainability
- pretrained-predictive-models
resource: https://docs.cloud.google.com/bigquery/docs/bqml-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Covers regression, classification, clustering, matrix factorisation, XGBoost, ARIMA_PLUS and imported TensorFlow/ONNX models. Pretrained functions such as AI.FORECAST (TimesFM), AI.DETECT_ANOMALIES and AI.KEY_DRIVERS forecast or explain without training; TimesFM 3.0 and AI.CAUSAL_EFFECT are in preview. Models can be registered in Agent Platform Model Registry. Not available in Standard edition reservations.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) (Machine learning development) (primary): Train and run models using SQL inside the data platform.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Pretrained predictive models](../../capabilities/machine-learning/pretrained-predictive-models.md) (Machine learning development): Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift ML](../aws/aws-redshift-ml.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md), [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Bring Your Own Model (BYOM)](../teradata/teradata-byom.md), [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [In-database machine learning](../../capabilities/machine-learning/in-database-ml.md) |
