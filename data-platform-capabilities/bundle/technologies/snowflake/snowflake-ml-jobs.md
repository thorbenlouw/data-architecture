---
type: Technology
id: snowflake-ml-jobs
title: Snowflake ML Jobs
description: Submits Python functions, files or code bundles from any IDE or from SQL to run as jobs on Container Runtime compute pools, including on multiple nodes.
platform: platform-snowflake
kind: feature
availability: ga
realises: [ml-pipelines, distributed-training, continuous-training]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/ml-jobs/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ML Jobs can be scheduled with tasks or called from external orchestrators. ML Jobs with Code Bundles were in preview in October 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development) (primary): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.
- [Continuous training](../../capabilities/mlops/continuous-training.md) (ML operations): Retrain and redeploy models automatically when data, drift or schedules call for it.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Pipelines](../aws/aws-sagemaker-pipelines.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Pipelines](../google-cloud/gcp-agent-platform-pipelines.md) | [Continuous training](../../capabilities/mlops/continuous-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dataiku](../independent/dataiku.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
