---
type: Technology
id: dataiku-visual-ml
title: Dataiku Visual ML
description: Visual and code-assisted model building for prediction, clustering, time series forecasting and causal prediction, with automatic feature handling, algorithm search, explanations and stress tests.
aliases: [Dataiku AutoML, Visual AutoML]
platform: platform-dataiku
kind: feature
availability: ga
realises:
- automl
- hyperparameter-tuning
- model-explainability
- model-evaluation
- ml-pipelines
- experiment-tracking
- batch-inference
resource: https://doc.dataiku.com/dss/latest/machine-learning/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Trained models become versioned saved models in the Flow, scored by recipes and retrained by scenarios. Experiment Tracking records runs from code through an MLflow-compatible API. Recent additions include visual generalised linear models, multi-target regression and CatBoost.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development) (primary): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.
- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Autopilot](../aws/aws-sagemaker-autopilot.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Batch inference](../../capabilities/mlops/batch-inference.md), [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AutoML](../databricks/databricks-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Studio](../sas/sas-model-studio.md), [SAS Visual Forecasting](../sas/sas-visual-forecasting.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
