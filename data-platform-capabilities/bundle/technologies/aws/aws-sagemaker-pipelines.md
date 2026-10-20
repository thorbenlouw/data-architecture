---
type: Technology
id: aws-sagemaker-pipelines
title: Amazon SageMaker Pipelines
description: Serverless workflow service for ML steps such as processing, training, evaluation, registration and deployment, defined in Python.
platform: platform-aws
kind: feature
availability: ga
realises: [ml-pipelines, ml-cicd, continuous-training]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Logs to MLflow Apps and registers models in Model Registry; SageMaker Projects templates wire pipelines to CI/CD. Retraining can be triggered by EventBridge rules or schedules.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development) (primary): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md) (ML operations): Test and promote model code, pipelines and models through environments automatically.
- [Continuous training](../../capabilities/mlops/continuous-training.md) (ML operations): Retrain and redeploy models automatically when data, drift or schedules call for it.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Pipelines](../google-cloud/gcp-agent-platform-pipelines.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Forecasting](../sas/sas-visual-forecasting.md), [SAS Model Studio](../sas/sas-model-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
