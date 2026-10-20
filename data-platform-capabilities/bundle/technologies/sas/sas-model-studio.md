---
type: Technology
id: sas-model-studio
title: SAS Model Studio
description: Browser-based machine learning application in SAS Viya that builds, compares and explains pipelines of data preparation, feature engineering and models, with automated pipeline generation and tuning.
aliases: [Model Studio, SAS Viya Machine Learning, VDMML]
formerly: [SAS Visual Data Mining and Machine Learning]
platform: platform-sas
kind: feature
availability: ga
realises:
- automl
- hyperparameter-tuning
- ml-pipelines
- feature-engineering
- model-evaluation
- model-explainability
- fairness-assessment
- distributed-training
resource: https://www.sas.com/en_us/software/model-studio.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

SAS stopped using the name SAS Visual Data Mining and Machine Learning with release 2023.01. Model Studio builds regression, classification, forecasting and clustering models, and its pipelines can include Python, R and SAS code. Training runs in parallel in [CAS](sas-cloud-analytic-services.md); autotuning searches hyperparameters automatically, and interpretability reports include LIME, ICE and Kernel SHAP. Models are registered in [SAS Model Manager](sas-model-manager.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development) (primary): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md) (Machine learning development): Measure whether a model's outcomes differ unfairly across groups of people.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Autopilot](../aws/aws-sagemaker-autopilot.md), [Amazon SageMaker Canvas](../aws/aws-sagemaker-canvas.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Functions](../snowflake/snowflake-ml-functions.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AutoML](../databricks/databricks-automl.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [AutoML](../../capabilities/machine-learning/automl.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [AutoML](../../capabilities/machine-learning/automl.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
