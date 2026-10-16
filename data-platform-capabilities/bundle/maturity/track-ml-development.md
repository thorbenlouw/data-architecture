---
type: Maturity Track
id: track-ml-development
title: ML development
description: How repeatably the organisation turns data into trained, evaluated and documented models.
covers:
- machine-learning
- feature-engineering
- feature-store
- offline-feature-store
- online-feature-store
- point-in-time-joins
- experiment-tracking
- model-training
- distributed-training
- hyperparameter-tuning
- automl
- in-database-ml
- model-registry
- model-evaluation
- model-explainability
- fairness-assessment
- data-labelling
- ml-pipelines
- pretrained-predictive-models
- runtime-management
- training-dataset-management
related_tracks: [track-mlops, track-ai-governance, track-data-quality]
levels:
- level: 1
  name: Initial
  summary: Individuals build models in notebooks on extracts, and results cannot be reproduced.
  criteria:
  - Training data is exported by hand to notebooks or laptops, and the exact extract used is not kept.
  - Results are reported in slides or messages rather than recorded in a tracking system.
  - Each project recomputes its features from scratch, often with slightly different logic.
  - Trained models are saved as files with names like model_final_v2 in personal or shared folders.
  capabilities: [feature-engineering, model-training]
  external_levels: {framework-microsoft-mlops-maturity: 0, framework-google-mlops-levels: 0}
- level: 2
  name: Managed
  summary: A data science team tracks experiments, versions models and trains on managed compute.
  criteria:
  - Every training run logs its parameters, code commit, data reference and metrics to an experiment tracker.
  - Candidate models are stored in a registry with version numbers and stage labels.
  - Training runs on managed compute from versioned runtime images with pinned libraries, reading platform data instead of downloaded copies.
  - Labelled examples are created and versioned in a managed labelling tool.
  - Searches over model settings run as automated jobs, and analysts can produce baseline models with AutoML or SQL-based training inside the platform.
  capabilities:
  - experiment-tracking
  - model-registry
  - hyperparameter-tuning
  - data-labelling
  - automl
  - in-database-ml
  - runtime-management
  external_levels: {framework-microsoft-mlops-maturity: 1, framework-google-mlops-levels: 0}
- level: 3
  name: Defined
  summary: Training runs as orchestrated pipelines on shared features and versioned datasets, with an evaluation standard applied automatically.
  criteria:
  - Data preparation, training and evaluation run as orchestrated pipelines from version control, and the same pipeline code runs in development and production.
  - Reusable features are published to a feature store with owners and descriptions, and training sets are built with point-in-time correct joins.
  - A written evaluation standard, run as a pipeline step, compares each candidate with a baseline and the current production model on a fixed holdout set.
  - Training, validation and evaluation sets are versioned datasets with recorded sources, licence terms and known gaps, and every registered model has a model card naming the dataset versions, intended use, metrics and known limits.
  - Large models or datasets train across several GPUs or nodes from the platform's distributed training templates.
  capabilities:
  - ml-pipelines
  - feature-store
  - offline-feature-store
  - point-in-time-joins
  - model-evaluation
  - distributed-training
  - training-dataset-management
  external_levels: {framework-microsoft-mlops-maturity: 2, framework-google-mlops-levels: 1}
- level: 4
  name: Measured
  summary: Feature and training code is tested in CI, and explainability, fairness, feature reuse and training-serving consistency are measured.
  criteria:
  - Global and per-prediction explanations are generated for every candidate model and reviewed before sign-off.
  - Fairness metrics across defined groups are computed for models that affect people, and a breached threshold blocks release.
  - Feature reuse, such as the share of production features used by more than one model, is reported.
  - Online feature values are compared with offline values for the same entities to detect training-serving skew.
  - Changes to feature and training code run CI tests, including unit tests of feature logic and a check that training converges on a sample, before the pipeline is deployed.
  capabilities: [model-explainability, fairness-assessment, online-feature-store]
  external_levels: {framework-microsoft-mlops-maturity: 3, framework-google-mlops-levels: 2}
- level: 5
  name: Optimising
  summary: Modelling effort goes where it measurably pays off, and training data and evaluation sets are refreshed continuously.
  criteria:
  - For each new use case, pretrained predictive models are benchmarked first, and custom training goes ahead only when it wins by an agreed margin.
  - Model-assisted labelling sends the most informative examples to labellers, and labelling cost per point of accuracy is tracked.
  - Evaluation sets are refreshed from recent production data on a schedule so offline metrics stay representative.
  - Features rebuilt in several projects are promoted to the feature store, and unused ones are retired, based on usage data.
  capabilities: [pretrained-predictive-models]
  external_levels: {framework-microsoft-mlops-maturity: 4, framework-google-mlops-levels: 2}
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means any model can be rebuilt from recorded code, data and parameters, features are shared instead of rebuilt in each project, and evaluation against baselines and fairness criteria happens before release. This track covers the model-creation side of the Google Cloud MLOps levels and the Microsoft MLOps maturity model; release and operation are in track-mlops, and both tracks map their levels to the two models in the same way. Initial is level 0 in both models. Managed brings in the tracked experiments, versioned models and managed compute that Microsoft lists for level 2, but training is still started by hand, so overall it corresponds to Microsoft level 1 and Google level 0. Defined adds the orchestrated training pipelines with automated model validation that complete Microsoft level 2 and underpin Google level 1. Measured adds the CI tests of feature and training code that Google level 2 and Microsoft level 3 call for, with explainability and fairness checks on every candidate, and Optimising refreshes training data and evaluation sets from production, as in Microsoft level 4. Typical blockers are notebooks on personal compute, training data pulled by hand and no agreed bar a model must clear before release.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Individuals build models in notebooks on extracts, and results cannot be reproduced.

- Training data is exported by hand to notebooks or laptops, and the exact extract used is not kept.
- Results are reported in slides or messages rather than recorded in a tracking system.
- Each project recomputes its features from scratch, often with slightly different logic.
- Trained models are saved as files with names like model_final_v2 in personal or shared folders.

**Capabilities first relied on:** [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 0; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 0

## Level 2: Managed

A data science team tracks experiments, versions models and trains on managed compute.

- Every training run logs its parameters, code commit, data reference and metrics to an experiment tracker.
- Candidate models are stored in a registry with version numbers and stage labels.
- Training runs on managed compute from versioned runtime images with pinned libraries, reading platform data instead of downloaded copies.
- Labelled examples are created and versioned in a managed labelling tool.
- Searches over model settings run as automated jobs, and analysts can produce baseline models with AutoML or SQL-based training inside the platform.

**Capabilities first relied on:** [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [AutoML](../capabilities/machine-learning/automl.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 1; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 0

## Level 3: Defined

Training runs as orchestrated pipelines on shared features and versioned datasets, with an evaluation standard applied automatically.

- Data preparation, training and evaluation run as orchestrated pipelines from version control, and the same pipeline code runs in development and production.
- Reusable features are published to a feature store with owners and descriptions, and training sets are built with point-in-time correct joins.
- A written evaluation standard, run as a pipeline step, compares each candidate with a baseline and the current production model on a fixed holdout set.
- Training, validation and evaluation sets are versioned datasets with recorded sources, licence terms and known gaps, and every registered model has a model card naming the dataset versions, intended use, metrics and known limits.
- Large models or datasets train across several GPUs or nodes from the platform's distributed training templates.

**Capabilities first relied on:** [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Feature store](../capabilities/machine-learning/feature-store.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 2; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 1

## Level 4: Measured

Feature and training code is tested in CI, and explainability, fairness, feature reuse and training-serving consistency are measured.

- Global and per-prediction explanations are generated for every candidate model and reviewed before sign-off.
- Fairness metrics across defined groups are computed for models that affect people, and a breached threshold blocks release.
- Feature reuse, such as the share of production features used by more than one model, is reported.
- Online feature values are compared with offline values for the same entities to detect training-serving skew.
- Changes to feature and training code run CI tests, including unit tests of feature logic and a check that training converges on a sample, before the pipeline is deployed.

**Capabilities first relied on:** [Model explainability](../capabilities/machine-learning/model-explainability.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 3; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 2

## Level 5: Optimising

Modelling effort goes where it measurably pays off, and training data and evaluation sets are refreshed continuously.

- For each new use case, pretrained predictive models are benchmarked first, and custom training goes ahead only when it wins by an agreed margin.
- Model-assisted labelling sends the most informative examples to labellers, and labelling cost per point of accuracy is tracked.
- Evaluation sets are refreshed from recent production data on a schedule so offline metrics stay representative.
- Features rebuilt in several projects are promoted to the feature store, and unused ones are retired, based on usage data.

**Capabilities first relied on:** [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md)

**Corresponds to:** [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md) level 4; [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md) level 2

# Capabilities in scope

[Machine learning development](../capabilities/machine-learning/machine-learning.md), [AutoML](../capabilities/machine-learning/automl.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Distributed training](../capabilities/machine-learning/distributed-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Feature store](../capabilities/machine-learning/feature-store.md), [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md), [In-database machine learning](../capabilities/machine-learning/in-database-ml.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Model training](../capabilities/machine-learning/model-training.md), [Offline feature store](../capabilities/machine-learning/offline-feature-store.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md)

# Related tracks

- [MLOps](track-mlops.md): How automatically and safely models are released, run, monitored and improved in production.
- [AI and model governance](track-ai-governance.md): How well the organisation knows its AI systems, assesses their risks and impacts, controls their behaviour and evidences this to regulators and customers.
- [Data quality and observability](track-data-quality.md): How systematically the organisation defines, measures, monitors and fixes the fitness of data for its intended uses.

Levels follow the shared [maturity scale](maturity-scale.md).
