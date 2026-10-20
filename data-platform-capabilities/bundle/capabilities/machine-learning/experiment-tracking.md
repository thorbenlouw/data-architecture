---
type: Capability
id: experiment-tracking
title: Experiment tracking
description: Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
broader: [machine-learning]
related: [model-lineage, data-versioning, notebooks, version-control]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each training run logs its parameters such as learning rate and tree depth, the code commit, a reference to the exact training data version, the software environment, metrics such as loss per epoch and validation accuracy, and output files such as the model and evaluation charts. A data scientist who has made 200 runs over two weeks can then sort them by validation score, compare the best five side by side, and see exactly what produced the winner.

Without tracking, results live in notebook output and memory, and the best model cannot be rebuilt. Runs are recorded by calling a logging library from training code or through automatic logging hooks for common frameworks; open-source MLflow defines a widely used interface. Tracking records every attempt, good or bad, whereas a model registry holds only the versions picked for possible release. The run record is also where model lineage starts, linking a deployed model back to its data and code.

# Key considerations

- Log a data version or snapshot id, not just a table name. Tables change, and the run can then no longer be reproduced.
- Automatic logging is convenient but can record too much or miss custom metrics. Agree a minimum set every run must log.
- Model files and checkpoints pile up quickly. Set retention rules for runs that were never promoted.
- Treat the tracking service as shared infrastructure with access control, because logged samples and charts can expose sensitive data.

# Questions to ask

- Could your team rebuild the model now in production from recorded information alone?
- How many data scientists and runs per week will log to it?
- Do reviewers or auditors need to see how a model was chosen?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Related | [Data versioning](../storage/data-versioning.md), [Hyperparameter tuning](hyperparameter-tuning.md), [ML pipelines](ml-pipelines.md), [Model lineage](../metadata/model-lineage.md), [Model registry](model-registry.md), [Model training](model-training.md), [Notebooks](../development-lifecycle/notebooks.md), [Prompt management](../generative-ai/prompt-management.md), [Runtime and environment management](../development-lifecycle/runtime-management.md), [Version control integration](../development-lifecycle/version-control.md) |
| Needed by | [Model lineage](../metadata/model-lineage.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 2)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md) · [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 11 and Annex IV – Technical documentation · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): ML metadata management · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 2 – Automated training

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker AI MLflow Apps | [Amazon SageMaker AI with MLflow](../../technologies/aws/aws-sagemaker-mlflow.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning registries and MLflow tracking](../../technologies/microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../../technologies/microsoft/fabric-data-science.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Experiments on Agent Platform](../../technologies/google-cloud/gcp-agent-platform-experiments.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Experiments](../../technologies/snowflake/snowflake-ml-experiments.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Managed MLflow on Databricks](../../technologies/databricks/databricks-managed-mlflow.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Experiments | [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Visual ML](../../technologies/dataiku/dataiku-visual-ml.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DVC (Data Version Control)](../../technologies/open-source/dvc.md), [MLflow](../../technologies/open-source/mlflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Comet ML](../../technologies/independent/comet.md), [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md), [Weights & Biases](../../technologies/independent/weights-and-biases.md) |
