---
type: Framework
id: framework-google-mlops-levels
title: Google Cloud MLOps levels
description: Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.
aliases:
- Google MLOps maturity levels
- MLOps levels 0, 1 and 2
- 'MLOps: Continuous delivery and automation pipelines in machine learning'
kind: maturity-model
publisher: Google Cloud
resource: https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
related: [framework-microsoft-mlops-maturity]
applies_to:
- fti-pipelines
- persona-ml-engineer
- persona-data-scientist
- usecase-churn-prediction
- usecase-demand-forecasting
- usecase-fraud-detection
maturity_levels:
- level: 0
  name: Manual process
  summary: Every step from data analysis to deployment is done by hand in notebooks or scripts and only the trained model is handed over for serving.
- {level: 1, name: ML pipeline automation, summary: The training pipeline is automated and deployed so that models retrain on fresh data in production.}
- level: 2
  name: CI/CD pipeline automation
  summary: Pipeline code is built, tested and deployed automatically so that teams can change pipelines quickly and reliably.
mappings:
- ref: Level 0 – Manual process
  summary: Models are built interactively and released rarely, with no CI/CD and little monitoring.
  capabilities: [notebooks, model-training, model-evaluation]
- ref: Level 1 – ML pipeline automation
  summary: An orchestrated training pipeline runs the same way in development and production and retrains models continuously.
  capabilities: [ml-pipelines, continuous-training, workflow-orchestration, model-deployment, runtime-management]
- ref: Level 2 – CI/CD pipeline automation
  summary: Source control, build and test services and staged deployment release the pipeline itself as well as models.
  capabilities: [ml-cicd, version-control, data-testing, environment-promotion, model-registry]
- ref: Data validation
  summary: Check incoming training data for schema and value skew before training, and stop or trigger retraining as needed.
  capabilities: [data-quality-rules, drift-detection, data-profiling, data-testing]
- ref: Model validation
  summary: Compare a new model with the current one offline and test it online before it is promoted.
  capabilities: [model-evaluation, canary-ab-testing, champion-challenger]
- ref: Feature store
  summary: Define, store and serve features centrally to avoid skew between training and serving.
  capabilities: [feature-store, offline-feature-store, online-feature-store]
- ref: ML metadata management
  summary: Record pipeline runs, parameters, datasets, artefacts and metrics for lineage, reproducibility and rollback.
  capabilities: [experiment-tracking, model-lineage, model-registry, training-dataset-management]
- ref: Pipeline triggers
  summary: Start training on demand, on a schedule, on new data or when performance or data distributions change.
  capabilities: [continuous-training, event-driven-triggering, drift-detection]
- ref: Model monitoring
  summary: Collect live performance statistics and use them to trigger new pipeline runs or experiments.
  capabilities: [model-monitoring, model-performance-monitoring, inference-logging]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This architecture guide from Google Cloud, last updated in August 2024, is one of the most cited descriptions of MLOps maturity. It defines three levels, from manual notebook-driven work (level 0), through an automated training pipeline that supports continuous training (level 1), to automated CI/CD for the pipelines themselves (level 2). Each level names the platform components it needs, such as data and model validation, a feature store, ML metadata, pipeline triggers and a model registry, which makes it straightforward to map onto platform capabilities. It is product-neutral in principle although its examples use Google Cloud services.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Maturity levels

| Level | Name | Summary |
|---|---|---|
| 0 | Manual process | Every step from data analysis to deployment is done by hand in notebooks or scripts and only the trained model is handed over for serving. |
| 1 | ML pipeline automation | The training pipeline is automated and deployed so that models retrain on fresh data in production. |
| 2 | CI/CD pipeline automation | Pipeline code is built, tested and deployed automatically so that teams can change pipelines quickly and reliably. |

Aligned with [ML development](../maturity/track-ml-development.md): bundle level 1 ≈ level 0; bundle level 2 ≈ level 0; bundle level 3 ≈ level 1; bundle level 4 ≈ level 2; bundle level 5 ≈ level 2.

Aligned with [MLOps](../maturity/track-mlops.md): bundle level 1 ≈ level 0; bundle level 2 ≈ level 0; bundle level 3 ≈ level 1; bundle level 4 ≈ level 2; bundle level 5 ≈ level 2.

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Level 0 – Manual process | Models are built interactively and released rarely, with no CI/CD and little monitoring. | [Notebooks](../capabilities/development-lifecycle/notebooks.md), [Model training](../capabilities/machine-learning/model-training.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md) |
| Level 1 – ML pipeline automation | An orchestrated training pipeline runs the same way in development and production and retrains models continuously. | [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Model deployment](../capabilities/mlops/model-deployment.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) |
| Level 2 – CI/CD pipeline automation | Source control, build and test services and staged deployment release the pipeline itself as well as models. | [CI/CD for machine learning](../capabilities/mlops/ml-cicd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Model registry](../capabilities/machine-learning/model-registry.md) |
| Data validation | Check incoming training data for schema and value skew before training, and stop or trigger retraining as needed. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) |
| Model validation | Compare a new model with the current one offline and test it online before it is promoted. | [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Champion-challenger](../capabilities/mlops/champion-challenger.md) |
| Feature store | Define, store and serve features centrally to avoid skew between training and serving. | [Feature store](../capabilities/machine-learning/feature-store.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md) |
| ML metadata management | Record pipeline runs, parameters, datasets, artefacts and metrics for lineage, reproducibility and rollback. | [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) |
| Pipeline triggers | Start training on demand, on a schedule, on new data or when performance or data distributions change. | [Continuous training](../capabilities/mlops/continuous-training.md), [Event-driven triggering](../capabilities/orchestration/event-driven-triggering.md), [Drift detection](../capabilities/mlops/drift-detection.md) |
| Model monitoring | Collect live performance statistics and use them to trigger new pipeline runs or experiments. | [Model monitoring](../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Inference logging](../capabilities/mlops/inference-logging.md) |

# Related frameworks

- [Microsoft MLOps maturity model](framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.

# Applies to

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md) (pattern): Split an ML system into independent feature, training and inference pipelines that share a feature store and model registry.
- [ML engineer](../personas/persona-ml-engineer.md) (persona): Takes models to production and keeps them running reliably.
- [Data scientist](../personas/persona-data-scientist.md) (persona): Explores data and builds statistical and machine learning models.
- [Churn prediction](../use-cases/usecase-churn-prediction.md) (use case): Score customers regularly by likelihood to leave so teams can act before they do.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md) (use case): Forecast demand by product, location and time to plan stock, staff and supply.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md) (use case): Score transactions in milliseconds and block or flag suspicious ones.
