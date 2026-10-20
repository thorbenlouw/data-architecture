---
type: Capability
id: model-lineage
title: Model lineage
description: Track the data, features, code and runs behind each model and its predictions.
broader: [data-lineage, model-governance]
related: [model-registry, feature-store, time-travel, ai-governance]
depends_on: [experiment-tracking, data-versioning]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Model lineage records, for each model version, the training data with its exact versions or snapshots, the features, the code commit, the parameters, any base model, the training run, the evaluation results and where the model is deployed. For predictions, it records which model version produced each one. For example, a credit model shows it was trained on the applications table as of 31 March, using version four of its feature set and a specific code commit, and every logged decision references that model version.

It supports reproducing results, explaining individual decisions, model risk management rules such as the US SR 11-7 guidance, and the technical documentation the EU AI Act requires for high-risk systems. It also answers which models need retraining when an upstream data problem is found. It is assembled from experiment tracking, the model registry and table versioning. Table lineage connects data to data; model lineage connects data to models, runs and predictions.

# Key considerations

- Reference immutable data versions such as snapshots or table versions, not table names. A name points at data that keeps changing.
- Link model lineage to data lineage so a data incident can list the models it affects.
- For third-party foundation models, record the provider, model version and your own tuning data. The provider's training data is usually not visible to you.
- Keep lineage for as long as decisions made with the model may need explaining.

# Questions to ask

- Must you reproduce or explain a model's decisions years later?
- When a source data problem is found, can you list the affected models today?
- Which regulations govern model documentation in your sector?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md), [Model governance](../mlops/model-governance.md) |
| Related | [Machine learning development](../machine-learning/machine-learning.md), [ML operations](../mlops/mlops.md), [AI governance](../governance/ai-governance.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Data versioning](../storage/data-versioning.md), [Document and unstructured lineage](unstructured-lineage.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [Feature store](../machine-learning/feature-store.md), [Inference logging](../mlops/inference-logging.md), [Model registry](../machine-learning/model-registry.md), [Time travel](../storage/time-travel.md), [Training and evaluation dataset management](../machine-learning/training-dataset-management.md) |
| Depends on | [Experiment tracking](../machine-learning/experiment-tracking.md), [Data versioning](../storage/data-versioning.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 4, Measured) · [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)
- **Frameworks:** [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 11 and Annex IV – Technical documentation; Article 53 – Obligations of general-purpose AI model providers · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): ML metadata management · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): MAP 4 – Risks of components

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Model Registry](../../technologies/aws/aws-sagemaker-model-registry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning registries and MLflow tracking](../../technologies/microsoft/azure-ml-registries-mlflow.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Pipelines](../../technologies/google-cloud/gcp-agent-platform-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data lineage (Snowsight lineage)](../../technologies/snowflake/snowflake-data-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Managed MLflow on Databricks](../../technologies/databricks/databricks-managed-mlflow.md), [Unity Catalog data lineage](../../technologies/databricks/databricks-unity-catalog-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Registry](../../technologies/cloudera/cloudera-ai-registry.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Modeling Objectives and model assets](../../technologies/palantir/palantir-modeling-objectives.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Weights & Biases](../../technologies/independent/weights-and-biases.md) |
