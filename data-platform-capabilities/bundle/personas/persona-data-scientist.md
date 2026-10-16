---
type: Persona
id: persona-data-scientist
title: Data scientist
description: Explores data and builds statistical and machine learning models.
cares_about:
- notebooks
- feature-engineering
- experiment-tracking
- model-training
- model-evaluation
- point-in-time-joins
- training-dataset-management
- data-profiling
- offline-feature-store
- data-catalogue
- access-requests
- model-explainability
- fairness-assessment
- experimentation
- data-versioning
- runtime-management
- deidentification
- data-usage-rights
- gpu-compute
- dataframe-apis
- hyperparameter-tuning
- data-labelling
- model-registry
- synthetic-data
- automl
- pretrained-predictive-models
patterns: [fti-pipelines]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data scientists sit in analytics or data science teams, or in business domains such as marketing, risk or supply chain. They work mostly in notebooks with Python or R, and move between framing a business problem, exploring and preparing data, building features, training and evaluating models, and explaining results to stakeholders.

Success is a model that improves a business decision by a measurable amount and that someone else can reproduce and run in production. Many projects stall not on the modelling but on getting access to data, inconsistent features between training and production, and the hand-over to engineering.

# Goals

- Get safe access to the right historical data quickly.
- Run experiments that can be compared and reproduced later.
- Hand over models that behave in production as they did in training.
- Show the business effect of a model, not only its accuracy.

# Jobs

- Explore and profile data in notebooks.
- Engineer features and build training sets with correct point-in-time logic.
- Train, tune and compare models, logging each experiment.
- Evaluate models against baselines, business measures and fairness criteria.
- Explain model behaviour to stakeholders and model reviewers.
- Work with ML engineers to deploy and monitor models.
- Measure a model's business effect with a controlled experiment or a held-out control group.
- Assemble, version and document training and test sets, recording their sources and whether they may be used for training.

# Pain points

- Access to data, especially personal data, takes weeks.
- Leakage or differences between training and serving features are found only after deployment.
- Notebooks cannot be rerun a few months later because data or libraries have changed.
- GPU and large compute are hard to obtain or expensive.
- Labels are scarce or of poor quality.
- Nobody can say quickly whether a licensed or customer dataset may be used to train a model.
- Models are judged on anecdotes because no control group was kept when they went live.

# Questions they ask

- Where can I get history with feature values as they were known at the time?
- Can I use personal data for this model, and in what form?
- Which features already exist that I can reuse?
- How do I get GPU capacity without managing infrastructure?
- What documentation and approvals does a model need before it is released?
- May I train a model on this dataset under its licence and the consent we hold?
- How do I keep a control group so the model's business effect can be measured?
- How do I fix the libraries and environment a model was trained with so it can be rebuilt?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Notebooks](../capabilities/development-lifecycle/notebooks.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Develop interactively with code, results and narrative together, with collaboration and scheduling. |
| [Feature engineering](../capabilities/machine-learning/feature-engineering.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Turn raw data into model inputs in reusable, consistent pipelines. |
| [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Train models on platform data at the scale required, from single machines to GPU clusters. |
| [Model evaluation](../capabilities/machine-learning/model-evaluation.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Assess models against holdout data, baselines and business criteria before release. |
| [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Join features as they were known at each training example's timestamp, preventing leakage of future data. |
| [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI. |
| [Data profiling](../capabilities/data-quality/data-profiling.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Analyse data to understand its structure, distributions, completeness and anomalies. |
| [Offline feature store](../capabilities/machine-learning/offline-feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Store historical feature values for model training and batch scoring. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Explain which inputs drive a model's predictions, overall and for individual predictions. |
| [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Measure whether a model's outcomes differ unfairly across groups of people. |
| [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Run controlled experiments with holdout groups and measure whether an action caused the outcome. |
| [Data versioning](../capabilities/storage/data-versioning.md) | [Storage and table management](../capabilities/storage/storage.md) | Keep and reference past versions of data so you can reproduce results, compare changes or roll back. |
| [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it. |
| [De-identification](../capabilities/governance/deidentification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk. |
| [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) | [Governance and compliance](../capabilities/governance/governance.md) | Record licence terms and permitted uses of datasets and check use against them, including for model training. |
| [GPU and accelerated compute](../capabilities/compute/gpu-compute.md) | [Query and compute](../capabilities/compute/compute.md) | Use GPUs or other accelerators for model training, inference and accelerated data processing. |
| [DataFrame APIs](../capabilities/processing/dataframe-apis.md) | [Processing and transformation](../capabilities/processing/processing.md) | Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine. |
| [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Search automatically for the model settings that perform best. |
| [Data labelling](../capabilities/machine-learning/data-labelling.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Create and manage labelled examples for supervised learning, using people, rules or models. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Version, document and manage the lifecycle of trained models from candidate to production. |
| [Synthetic data generation](../capabilities/development-lifecycle/synthetic-data.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Generate artificial data that keeps the useful properties of real data without exposing real records. |
| [AutoML](../capabilities/machine-learning/automl.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Try features, algorithms and settings automatically to produce a good baseline model with little code. |
| [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case. |

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)

# Use cases they take part in

- [Churn prediction](../use-cases/usecase-churn-prediction.md): Score customers regularly by likelihood to leave so teams can act before they do.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md): Forecast demand by product, location and time to plan stock, staff and supply.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md): Analyse sensor telemetry to predict equipment failures before they happen.
- [Personalised recommendations](../use-cases/usecase-recommendations.md): Recommend products or content to each user in real time.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.

# Frameworks they work with

- [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.
- [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.
