---
type: Technology
id: sas-model-manager
title: SAS Model Manager
description: Model lifecycle application in SAS Viya that registers and versions SAS, Python and R models, documents them with model cards, publishes them to run-time destinations and monitors their performance and drift.
platform: platform-sas
kind: feature
availability: ga
realises:
- model-registry
- model-governance
- model-deployment
- model-performance-monitoring
- drift-detection
- champion-challenger
- ml-cicd
resource: https://www.sas.com/en_us/software/model-manager.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Each project has one champion model, which challengers are compared against and can replace. Model cards record accuracy, fairness, drift and intended use. Models publish to CAS, the Micro Analytic Service, databases through [SAS Data Accelerator](sas-data-accelerator.md), Azure Machine Learning, and containers through [SAS Container Runtime](sas-container-runtime.md). An automated CI/CD pipeline tests and promotes models, and SAS Viya Copilot can set champion models and publish models from natural-language requests.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development) (primary): Version, document and manage the lifecycle of trained models from candidate to production.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [Model deployment](../../capabilities/mlops/model-deployment.md) (ML operations): Package and release models into production for batch, real-time or streaming use.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Champion-challenger](../../capabilities/mlops/champion-challenger.md) (ML operations): Run challenger models alongside the champion and promote a challenger when it proves better.
- [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md) (ML operations): Test and promote model code, pipelines and models through environments automatically.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Model Registry](../aws/aws-sagemaker-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Model Registry](../google-cloud/gcp-agent-platform-model-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Registry](../snowflake/snowflake-model-registry.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Models in Unity Catalog](../databricks/databricks-models-in-unity-catalog.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Registry](../cloudera/cloudera-ai-registry.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model deployment](../../capabilities/mlops/model-deployment.md), [Model governance](../../capabilities/mlops/model-governance.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Modeling Objectives and model assets](../palantir/palantir-modeling-objectives.md) | [CI/CD for machine learning](../../capabilities/mlops/ml-cicd.md), [Model deployment](../../capabilities/mlops/model-deployment.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Govern](../dataiku/dataiku-govern.md) | [Model governance](../../capabilities/mlops/model-governance.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kubeflow](../open-source/kubeflow.md), [MLflow](../open-source/mlflow.md) | [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [DataRobot AI Platform](../independent/datarobot-ai-platform.md), [Comet ML](../independent/comet.md), [Weights & Biases](../independent/weights-and-biases.md) | [Champion-challenger](../../capabilities/mlops/champion-challenger.md), [Drift detection](../../capabilities/mlops/drift-detection.md), [Model deployment](../../capabilities/mlops/model-deployment.md), [Model governance](../../capabilities/mlops/model-governance.md) |
