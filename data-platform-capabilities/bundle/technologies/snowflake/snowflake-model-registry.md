---
type: Technology
id: snowflake-model-registry
title: Snowflake Model Registry
description: Stores versioned models trained in Snowflake or elsewhere as schema-level objects with metadata, metrics and aliases, and runs their methods from SQL or Python for batch inference.
platform: platform-snowflake
kind: feature
availability: ga
realises: [model-registry, model-governance, batch-inference, model-explainability]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow, Hugging Face and custom models. Built-in explainability gives Shapley values. Models can run on warehouses or be deployed to Snowpark Container Services. Importing models from external services is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development) (primary): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Model Registry](../aws/aws-sagemaker-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md), [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Model Registry](../google-cloud/gcp-agent-platform-model-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Registry](../cloudera/cloudera-ai-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Manager](../sas/sas-model-manager.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [MLflow](../open-source/mlflow.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Comet ML](../independent/comet.md), [Weights & Biases](../independent/weights-and-biases.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
