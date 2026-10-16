---
type: Capability
id: continuous-training
title: Continuous training
description: Retrain and redeploy models automatically when data, drift or schedules call for it.
aliases: [automated retraining]
broader: [mlops]
related: [drift-detection, model-performance-monitoring, model-evaluation, asset-based-orchestration]
depends_on: [ml-pipelines, model-registry]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A retraining run can be started by a schedule, such as weekly; by an event, such as a new month of labelled data landing; or by a monitoring signal, such as drift or falling accuracy. The trigger starts the training pipeline, which validates data, trains, compares the result with the current production model and registers the new version if it passes. Release can then follow automatically or wait for a person to approve it.

It matters where conditions change quickly, as with demand, fraud, pricing or recommendations, and it keeps models current without manual effort growing with the number of models. The risk is automating a mistake: a bad batch of data produces a bad model that is promoted without anyone looking. Safeguards are data validation, a gate requiring the new model to beat the champion, a release strategy such as shadow or canary, and fast rollback. Automated retraining is what separates the higher levels of common MLOps maturity models.

# Key considerations

- Gate every automatically trained model on data checks and on beating the current production model, not on an absolute score alone.
- Scheduled retraining is simple and predictable. Trigger-based retraining reacts faster but depends on reliable monitoring signals.
- Keep a human approval step for high-risk models even when training and evaluation are automated.
- Watch for feedback loops, where a model's own decisions shape the data it is retrained on.

# Questions to ask

- How quickly does model quality decay without retraining?
- How many models need retraining, and how much effort does it take today?
- Which models must have human approval before each new version goes live?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [ML operations](mlops.md) |
| Related | [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Drift detection](drift-detection.md), [ML pipelines](../machine-learning/ml-pipelines.md), [Model evaluation](../machine-learning/model-evaluation.md), [Model monitoring](model-monitoring.md), [Model performance monitoring](model-performance-monitoring.md) |
| Depends on | [ML pipelines](../machine-learning/ml-pipelines.md), [Model registry](../machine-learning/model-registry.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 1 – ML pipeline automation; Pipeline triggers · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 4 – Full MLOps automated operations

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Pipelines](../../technologies/aws/aws-sagemaker-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Pipelines](../../technologies/google-cloud/gcp-agent-platform-pipelines.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ML Jobs](../../technologies/snowflake/snowflake-ml-jobs.md) |
