---
type: Capability
id: hyperparameter-tuning
title: Hyperparameter tuning
description: Search automatically for the model settings that perform best.
broader: [model-training]
related: [experiment-tracking, model-evaluation, elastic-scaling]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hyperparameters are settings fixed before training rather than learned from data, such as tree depth, learning rate or regularisation strength. Tuning runs many training trials with different combinations and keeps the one with the best validation score. Grid search tries every combination in a fixed set. Random search samples combinations and usually finds good ones sooner. Bayesian and similar adaptive methods use earlier results to choose the next trial, and early stopping abandons trials that look poor after a few rounds.

Tuning can improve a model noticeably, but it multiplies compute cost by the number of trials, so it needs parallel execution, budgets and tracking. Results must be judged on a validation set kept apart from the final test set; tuning against the test set overstates how good the model is. Open-source libraries such as Optuna and Ray Tune implement the common methods. Tuning differs from AutoML, which also searches over features and algorithms, not only the settings of one chosen algorithm.

# Key considerations

- Set a budget for trials and spend before starting. Unbounded searches can cost far more than the gain is worth.
- Keep a test set the search never sees, or the reported score will be optimistic.
- Log every trial to experiment tracking so the search can be inspected and the winner reproduced.
- Most of the gain usually comes from a few hyperparameters. Tuning dozens at once wastes trials.

# Questions to ask

- How much quality improvement would justify how much extra compute?
- Can trials run in parallel on shared compute with quotas?
- Are tuning results recorded so reviewers can see what was tried?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Model training](model-training.md) |
| Related | [Elastic scaling](../compute/elastic-scaling.md), [Experiment tracking](experiment-tracking.md), [Model evaluation](model-evaluation.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md), [Amazon SageMaker Autopilot](../../technologies/aws/aws-sagemaker-autopilot.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md), [BigQuery ML](../../technologies/google-cloud/gcp-bigquery-ml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Container Runtime for ML](../../technologies/snowflake/snowflake-container-runtime.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AutoML](../../technologies/databricks/databricks-automl.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Kubeflow](../../technologies/open-source/kubeflow.md), [Ray](../../technologies/open-source/ray.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Weights & Biases](../../technologies/independent/weights-and-biases.md) |
