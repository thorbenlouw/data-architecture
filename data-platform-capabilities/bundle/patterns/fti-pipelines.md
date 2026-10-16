---
type: Pattern
id: fti-pipelines
title: Feature, training and inference pipelines
description: Split an ML system into independent feature, training and inference pipelines that share a feature store and model registry.
aliases: [FTI pipelines]
uses:
- feature-engineering
- feature-store
- offline-feature-store
- online-feature-store
- point-in-time-joins
- model-training
- model-registry
- batch-inference
- real-time-inference
- model-lineage
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The feature pipeline turns raw data into features and writes them to a feature store, in batch or as a stream. The training pipeline reads historical features with point-in-time correct joins, trains and evaluates a model, and registers it in a model registry. The inference pipeline loads a registered model, reads current features from the online or offline store and produces predictions, either in batch or behind an API. Jim Dowling of Hopsworks set out the pattern around 2023 as a simpler way to describe ML systems than large MLOps diagrams.

Because the three pipelines share only the feature store and the model registry, different teams can own them, they can run on different schedules and compute, and each can be tested and released on its own. Features are computed once and reused for training and serving, which avoids training-serving skew, where a model sees inputs in production that were calculated differently from those it learnt on. The main variation is whether features are computed in advance or on demand at inference time.

# When to use

- Several models share features, or the same features are needed for training and for online inference.
- Teams want to own feature engineering, training and serving separately, on different schedules.
- You need to avoid training-serving skew and trace which features and model version produced a prediction.

# Watch out for

- A feature store and model registry are prerequisites; without them the pipelines couple through ad hoc files and tables.
- Features computed on demand at inference time must use the same code as the feature pipeline, or skew returns.
- Three independent pipelines still need end-to-end monitoring and lineage to trace a bad prediction back to its data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Feature engineering](../capabilities/machine-learning/feature-engineering.md): Turn raw data into model inputs in reusable, consistent pipelines.
- [Feature store](../capabilities/machine-learning/feature-store.md): Manage features centrally so they are reused, documented and served consistently for training and inference.
- [Offline feature store](../capabilities/machine-learning/offline-feature-store.md): Store historical feature values for model training and batch scoring.
- [Online feature store](../capabilities/machine-learning/online-feature-store.md): Serve the latest feature values to models in milliseconds.
- [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md): Join features as they were known at each training example's timestamp, preventing leakage of future data.
- [Model training](../capabilities/machine-learning/model-training.md): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Model registry](../capabilities/machine-learning/model-registry.md): Version, document and manage the lifecycle of trained models from candidate to production.
- [Batch inference](../capabilities/mlops/batch-inference.md): Score large datasets with a model on a schedule.
- [Real-time inference](../capabilities/mlops/real-time-inference.md): Serve predictions through low-latency endpoints.
- [Model lineage](../capabilities/metadata/model-lineage.md): Track the data, features, code and runs behind each model and its predictions.

# Where it appears

- **Use cases:** [Churn prediction](../use-cases/usecase-churn-prediction.md) · [Credit decisioning](../use-cases/usecase-credit-decisioning.md) · [Demand forecasting](../use-cases/usecase-demand-forecasting.md) · [Real-time fraud detection](../use-cases/usecase-fraud-detection.md) · [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) · [Personalised recommendations](../use-cases/usecase-recommendations.md)
- **Personas:** [Data scientist](../personas/persona-data-scientist.md) · [ML engineer](../personas/persona-ml-engineer.md)
