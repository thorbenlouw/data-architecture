---
type: Technology
id: sas-visual-forecasting
title: SAS Visual Forecasting
description: Forecasting application in SAS Viya that builds pipelines of time series, machine learning and hybrid models for each level of a hierarchy, selects the best model for each series and reconciles forecasts across levels.
platform: platform-sas
kind: feature
availability: ga
realises: [ml-pipelines, automl]
resource: https://www.sas.com/en_us/software/visual-forecasting.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:50:29Z'}
---

Included in SAS Viya Enterprise. Forecasts run in parallel on the in-memory engine of [CAS](sas-cloud-analytic-services.md), ensemble modelling picks the best-performing model for each series, and Python and R algorithms can be added to pipelines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development) (primary): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Pipelines](../aws/aws-sagemaker-pipelines.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md), [Automated machine learning (AutoML) in Azure Machine Learning](../microsoft/azure-ml-automl.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [AutoML](../../capabilities/machine-learning/automl.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Pipelines](../google-cloud/gcp-agent-platform-pipelines.md), [Agent Platform AutoML](../google-cloud/gcp-agent-platform-automl.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [AutoML](../../capabilities/machine-learning/automl.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [AutoML](../../capabilities/machine-learning/automl.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
