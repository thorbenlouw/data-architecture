---
type: Technology
id: palantir-modeling-objectives
title: Palantir Modeling Objectives and model assets
description: Foundry's model management, in which model assets built in Foundry or imported are evaluated, reviewed, released and deployed for batch or live use, then bound to the Ontology.
platform: platform-palantir
kind: feature
availability: ga
realises: [model-registry, model-deployment, model-evaluation, ml-cicd, model-lineage]
resource: https://www.palantir.com/docs/foundry/model-integration/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Handles governance and permissions for releases, automated evaluation of candidates, downtime-free deployment and inference history. Externally hosted models can be connected as APIs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development) (primary): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model deployment](../../capabilities/mlops/model-deployment.md) (ML operations): Package and release models into production for batch, real-time or streaming use.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.
- [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md) (ML operations): Test and promote model code, pipelines and models through environments automatically.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Model Registry](../aws/aws-sagemaker-model-registry.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Model Registry](../google-cloud/gcp-agent-platform-model-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Registry](../cloudera/cloudera-ai-registry.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Model deployment](../../capabilities/mlops/model-deployment.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [Kubeflow](../open-source/kubeflow.md) | [Model evaluation](../../capabilities/machine-learning/model-evaluation.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Weights & Biases](../independent/weights-and-biases.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Comet ML](../independent/comet.md) | [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md), [Model deployment](../../capabilities/mlops/model-deployment.md) |
