---
type: Capability
id: machine-learning
title: Machine learning development
description: Develop, train and evaluate machine learning models on platform data.
aliases: [data science]
broader: []
related: [notebooks, gpu-compute, data-versioning, model-lineage, ai-governance]
order: 8
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Machine learning development is the work of turning platform data into a model that is good enough to release. A churn model, for example, needs two years of customer activity joined to cancellation labels, features such as days since last login calculated as they stood on each snapshot date, dozens of training runs compared on held-out data, and a check that it works acceptably for every customer segment.

The parts form a loop. Data labelling and feature engineering produce the inputs, and the feature store keeps them consistent between training and production. Training, tuning and AutoML produce candidate models, and experiment tracking records every attempt. Evaluation, explainability and fairness assessment decide which candidate is fit for use. The registry holds the approved version and hands it to ML operations. ML pipelines automate the loop so it can be rerun on new data by someone other than the original author.

Two shortcuts sit beside the full loop. In-database ML lets SQL users train and score common model types without moving data, and pretrained predictive models forecast or classify tables without per-use-case training. The main architectural question is how close model work sits to governed data. Copying extracts to laptops or separate ML environments is quick to start but loses lineage, access control and reproducibility.

# Key considerations

- Training data must be reproducible. Record a dataset version or snapshot for each run, or you cannot explain or rebuild a model later.
- Share feature logic between training and serving. Reimplementing it in a second language is a leading cause of models behaving differently in production.
- Decide where data scientists work: in platform notebooks with governed access, or in separate environments fed by extracts. The second is common and hard to govern.
- GPU and large-memory compute is expensive and used in bursts. Plan on-demand or shared pools with quotas rather than permanently sized clusters.
- Plan the hand-off to operations from the start. A model that exists only in a notebook has no owner, no version and no route to production.

# Questions to ask

- Which decisions will models inform, and how many models do you expect to run in two years?
- Do data scientists need data they cannot use today, such as personal or regulated data?
- Must you be able to show how a model was built, for audit or regulation?
- Which model types are in scope: tabular prediction, forecasting, computer vision, language, or a mix?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Data labelling](data-labelling.md), [Experiment tracking](experiment-tracking.md), [Feature engineering](feature-engineering.md), [Feature store](feature-store.md), [In-database machine learning](in-database-ml.md), [ML pipelines](ml-pipelines.md), [Model evaluation](model-evaluation.md), [Model registry](model-registry.md), [Model training](model-training.md), [Pretrained predictive models](pretrained-predictive-models.md), [Runtime and environment management](../development-lifecycle/runtime-management.md), [Training and evaluation dataset management](training-dataset-management.md) |
| Related | [AI governance](../governance/ai-governance.md), [Data versioning](../storage/data-versioning.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model lineage](../metadata/model-lineage.md), [Notebooks](../development-lifecycle/notebooks.md) |

# Where it appears

- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 103 technologies; see their pages.
