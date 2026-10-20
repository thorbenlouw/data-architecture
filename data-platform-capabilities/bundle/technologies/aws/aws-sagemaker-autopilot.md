---
type: Technology
id: aws-sagemaker-autopilot
title: Amazon SageMaker Autopilot
description: AutoML API that explores feature processing, algorithms and hyperparameters to produce ranked candidate models for tabular, text, image and time-series tasks.
platform: platform-aws
kind: feature
availability: ga
realises: [automl, hyperparameter-tuning]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The interactive UI has moved into Canvas; programmatic use is through the AutoML v2 API. Redshift ML uses it behind CREATE MODEL.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development) (primary): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AutoML](../databricks/databricks-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Studio](../sas/sas-model-studio.md), [SAS Visual Forecasting](../sas/sas-visual-forecasting.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
