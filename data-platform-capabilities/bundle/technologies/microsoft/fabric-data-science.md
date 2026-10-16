---
type: Technology
id: fabric-data-science
title: Data Science in Microsoft Fabric
description: Notebook-based machine learning with MLflow experiments, a model registry, AutoML and batch scoring with the PREDICT function.
formerly: [Synapse Data Science]
platform: platform-microsoft
kind: feature
availability: ga
realises: [model-training, experiment-tracking, model-registry, automl, batch-inference]
resource: https://learn.microsoft.com/en-us/fabric/data-science/data-science-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AutoML became GA in March 2026. No managed real-time serving comparable to Azure Machine Learning endpoints; for MLOps at scale, Azure Machine Learning or Azure Databricks is usually used.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development) (primary): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model registry](../../capabilities/machine-learning/model-registry.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model training](../../capabilities/machine-learning/model-training.md) |
