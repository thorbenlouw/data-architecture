---
type: Technology
id: aws-sagemaker-clarify
title: Amazon SageMaker Clarify
description: Processing jobs that compute pre- and post-training bias metrics and SHAP feature attributions for models and datasets.
platform: platform-aws
kind: feature
availability: deprecated
realises: [model-explainability, fairness-assessment]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-availability-change.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In maintenance and closed to new customers from 30 July 2026. AWS suggests computing the published bias formulas directly, using the SHAP library, fmeval for LLM evaluation, and Bedrock Evaluations for generative AI.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development) (primary): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md) (Machine learning development): Measure whether a model's outcomes differ unfairly across groups of people.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
**Product family:** Amazon SageMaker AI  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning Responsible AI dashboard](../microsoft/azure-ml-responsible-ai-dashboard.md) | [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Model Evaluation](../google-cloud/gcp-agent-platform-model-evaluation.md), [BigQuery ML](../google-cloud/gcp-bigquery-ml.md) | [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md) | [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave AutoML and HeatWave GenAI](../oracle/oracle-heatwave-automl-genai.md) | [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Studio](../sas/sas-model-studio.md) | [Bias and fairness assessment](../../capabilities/machine-learning/fairness-assessment.md), [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fiddler AI Control Plane](../independent/fiddler-ai-control-plane.md), [H2O.ai Platform (Driverless AI and h2oGPTe)](../independent/h2o-ai.md) | [Model explainability](../../capabilities/machine-learning/model-explainability.md) |
