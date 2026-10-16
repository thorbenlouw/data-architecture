---
type: Technology
id: azure-ml-registries-mlflow
title: Azure Machine Learning registries and MLflow tracking
description: Tracks runs, parameters and metrics with MLflow and versions models, environments and components in workspace or cross-workspace registries.
platform: platform-microsoft
kind: feature
availability: ga
realises: [experiment-tracking, model-registry, model-lineage, ml-cicd, runtime-management]
resource: https://learn.microsoft.com/en-us/azure/machine-learning/concept-machine-learning-registries-mlops
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Registries let the same model be promoted across development, test and production workspaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.
- [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md) (ML operations): Test and promote model code, pipelines and models through environments automatically.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Azure Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Experiments](../snowflake/snowflake-ml-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md), [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model lineage](../../capabilities/metadata/model-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md), [Cloudera AI Registry](../cloudera/cloudera-ai-registry.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weights & Biases](../independent/weights-and-biases.md), [Comet ML](../independent/comet.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
