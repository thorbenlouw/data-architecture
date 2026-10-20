---
type: Technology
id: gcp-agent-platform-pipelines
title: Agent Platform Pipelines
description: Serverless execution of Kubeflow Pipelines and TFX workflows, with each run's artefacts and parameters recorded in ML Metadata.
formerly: [Vertex AI Pipelines]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [ml-pipelines, continuous-training, model-lineage]
resource: https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development) (primary): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Continuous training](../../capabilities/mlops/continuous-training.md) (ML operations): Retrain and redeploy models automatically when data, drift or schedules call for it.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Pipelines](../aws/aws-sagemaker-pipelines.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Forecasting](../sas/sas-visual-forecasting.md), [SAS Model Studio](../sas/sas-model-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
