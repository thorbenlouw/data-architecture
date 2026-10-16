---
type: Technology
id: kubeflow
title: Kubeflow
description: Collection of Kubernetes-native ML tools, including Kubeflow Pipelines, Trainer for distributed training, Katib for tuning, notebooks and a model registry.
aliases: [Kubeflow Pipelines, KFP, Katib, Kubeflow Trainer]
platform: platform-open-source
kind: open-source
availability: ga
realises: [ml-pipelines, distributed-training, hyperparameter-tuning, model-registry, notebooks]
resource: https://www.kubeflow.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, a CNCF incubating project. Components can be installed separately. Kubeflow Pipelines is also the basis of Google Vertex AI Pipelines. Operating the full platform needs Kubernetes skills.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development) (primary): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Pipelines](../aws/aws-sagemaker-pipelines.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Pipelines](../google-cloud/gcp-agent-platform-pipelines.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Model registry](../../capabilities/machine-learning/model-registry.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dataiku](../independent/dataiku.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) |
