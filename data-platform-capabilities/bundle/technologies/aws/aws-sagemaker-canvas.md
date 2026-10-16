---
type: Technology
id: aws-sagemaker-canvas
title: Amazon SageMaker Canvas
description: No-code ML workspace where analysts prepare data, build and evaluate models automatically, and generate predictions.
platform: platform-aws
kind: feature
availability: ga
realises: [automl, data-preparation, feature-engineering, batch-inference]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes Data Wrangler data preparation, the Autopilot UI, time-series forecasting (AWS's path off the closed Amazon Forecast service) and access to foundation models.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development) (primary): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md), [Dataflow ML](../google-cloud/gcp-dataflow-ml.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Batch inference](../../capabilities/mlops/batch-inference.md), [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AutoML](../databricks/databricks-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Dataiku](../independent/dataiku.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
