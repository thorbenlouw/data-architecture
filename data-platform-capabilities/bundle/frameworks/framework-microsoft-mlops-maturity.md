---
type: Framework
id: framework-microsoft-mlops-maturity
title: Microsoft MLOps maturity model
description: A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.
aliases: [Azure MLOps maturity model, Microsoft MLOps maturity levels]
kind: maturity-model
publisher: Microsoft
resource: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model
related: [framework-google-mlops-levels]
applies_to:
- fti-pipelines
- persona-ml-engineer
- persona-data-scientist
- persona-platform-engineer
- usecase-churn-prediction
- usecase-demand-forecasting
maturity_levels:
- {level: 0, name: No MLOps, summary: 'Data scientists work alone, data is gathered by hand, experiments are not tracked and models are released manually.'}
- {level: 1, name: DevOps but no MLOps, summary: Application releases and data pipelines are automated but model training and release are still manual.}
- {level: 2, name: Automated training, summary: 'Training runs as managed, repeatable jobs with tracked experiments and version-controlled code and models.'}
- {level: 3, name: Automated model deployment, summary: Models are released automatically through CI/CD with unit and integration tests.}
- level: 4
  name: Full MLOps automated operations
  summary: Production metrics trigger retraining automatically and post-deployment metrics are gathered systematically.
mappings:
- ref: Level 0 – No MLOps
  summary: Models are built in isolation on unmanaged compute and released by hand by one person.
  capabilities: [notebooks, model-training]
- ref: Level 1 – DevOps but no MLOps
  summary: Data pipelines gather data automatically and application code has automated tests and releases, but models are still handed over manually.
  capabilities: [workflow-orchestration, ci-cd, version-control]
- ref: Level 2 – Automated training
  summary: Training runs on managed compute as repeatable jobs, with experiments tracked and models versioned.
  capabilities: [ml-pipelines, experiment-tracking, model-registry, compute-options]
- ref: Level 3 – Automated model deployment
  summary: A CI/CD pipeline tests and releases models automatically, with less reliance on individual data scientists.
  capabilities: [ml-cicd, model-deployment, environment-promotion, data-testing]
- ref: Level 4 – Full MLOps automated operations
  summary: Detailed metrics from production models feed back automatically into retraining and redeployment.
  capabilities:
  - continuous-training
  - model-performance-monitoring
  - drift-detection
  - inference-logging
  - model-monitoring
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Microsoft's MLOps maturity model, published in the Azure Architecture Center and last updated in June 2026, describes five levels from no MLOps to fully automated operations. Each level is characterised across four dimensions: how people collaborate, how models are created, how they are released and how they are integrated into applications. Microsoft stresses that organisations often show traits of several levels at once, so the levels work best as a continuum for planning. It complements Google's three levels by separating DevOps for application code from automation of training and of deployment.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Maturity levels

| Level | Name | Summary |
|---|---|---|
| 0 | No MLOps | Data scientists work alone, data is gathered by hand, experiments are not tracked and models are released manually. |
| 1 | DevOps but no MLOps | Application releases and data pipelines are automated but model training and release are still manual. |
| 2 | Automated training | Training runs as managed, repeatable jobs with tracked experiments and version-controlled code and models. |
| 3 | Automated model deployment | Models are released automatically through CI/CD with unit and integration tests. |
| 4 | Full MLOps automated operations | Production metrics trigger retraining automatically and post-deployment metrics are gathered systematically. |

Aligned with [ML development](../maturity/track-ml-development.md): bundle level 1 ≈ level 0; bundle level 2 ≈ level 1; bundle level 3 ≈ level 2; bundle level 4 ≈ level 3; bundle level 5 ≈ level 4.

Aligned with [MLOps](../maturity/track-mlops.md): bundle level 1 ≈ level 0; bundle level 2 ≈ level 1; bundle level 3 ≈ level 2; bundle level 4 ≈ level 3; bundle level 5 ≈ level 4.

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Level 0 – No MLOps | Models are built in isolation on unmanaged compute and released by hand by one person. | [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Model training](../capabilities/machine-learning/model-training.md) |
| Level 1 – DevOps but no MLOps | Data pipelines gather data automatically and application code has automated tests and releases, but models are still handed over manually. | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md) |
| Level 2 – Automated training | Training runs on managed compute as repeatable jobs, with experiments tracked and models versioned. | [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Compute provisioning options](../capabilities/compute/compute-options.md) |
| Level 3 – Automated model deployment | A CI/CD pipeline tests and releases models automatically, with less reliance on individual data scientists. | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) |
| Level 4 – Full MLOps automated operations | Detailed metrics from production models feed back automatically into retraining and redeployment. | [Continuous training](../capabilities/mlops/continuous-training.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model monitoring](../capabilities/mlops/model-monitoring.md) |

# Related frameworks

- [Google Cloud MLOps levels](framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.

# Applies to

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md) (pattern): Split an ML system into independent feature, training and inference pipelines that share a feature store and model registry.
- [ML engineer](../personas/persona-ml-engineer.md) (persona): Takes models to production and keeps them running reliably.
- [Data scientist](../personas/persona-data-scientist.md) (persona): Explores data and builds statistical and machine learning models.
- [Data platform engineer](../personas/persona-platform-engineer.md) (persona): Builds and runs the shared data platform and its self-service tooling.
- [Churn prediction](../use-cases/usecase-churn-prediction.md) (use case): Score customers regularly by likelihood to leave so teams can act before they do.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md) (use case): Forecast demand by product, location and time to plan stock, staff and supply.
