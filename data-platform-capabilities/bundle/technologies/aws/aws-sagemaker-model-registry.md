---
type: Technology
id: aws-sagemaker-model-registry
title: Amazon SageMaker Model Registry
description: Catalogue of versioned model packages grouped by use case, with approval status, metadata, lineage and Model Cards for documentation.
platform: platform-aws
kind: feature
availability: ga
realises: [model-registry, model-governance, model-lineage]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Approval status changes emit EventBridge events for deployment automation. Integrates with the MLflow model registry and can share models across accounts. Model Cards and Model Dashboard record risk ratings and intended use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development) (primary): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Model Registry](../google-cloud/gcp-agent-platform-model-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Registry](../cloudera/cloudera-ai-registry.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Manager](../sas/sas-model-manager.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [MLflow](../open-source/mlflow.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weights & Biases](../independent/weights-and-biases.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Comet ML](../independent/comet.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md), [Model governance](../../capabilities/mlops/model-governance.md) |
