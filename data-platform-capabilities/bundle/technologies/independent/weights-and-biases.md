---
type: Technology
id: weights-and-biases
title: Weights & Biases
description: Experiment tracking, hyperparameter sweeps, artefact versioning and a model registry (W&B Models), plus tracing and evaluation of LLM and agent applications (W&B Weave).
aliases: [W&B, wandb, W&B Models, W&B Weave]
platform: platform-independent
vendor: Weights & Biases (CoreWeave)
kind: saas
availability: ga
realises:
- experiment-tracking
- model-registry
- hyperparameter-tuning
- model-lineage
- genai-evaluation
- training-dataset-management
resource: https://wandb.ai/site/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

CoreWeave bought Weights & Biases in 2025, and W&B is now part of CoreWeave Forge alongside CoreWeave's training and serverless inference. Still available as SaaS, dedicated cloud or self-managed, and widely used by teams training foundation models. Weave also covers generative AI observability.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Experiments](../snowflake/snowflake-ml-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model lineage](../../capabilities/metadata/model-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Model registry](../../capabilities/machine-learning/model-registry.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
