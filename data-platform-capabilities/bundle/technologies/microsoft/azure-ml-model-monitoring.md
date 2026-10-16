---
type: Technology
id: azure-ml-model-monitoring
title: Azure Machine Learning model monitoring
description: Monitors deployed models for data drift, prediction drift, data quality and performance against ground truth, with alerts.
platform: platform-microsoft
kind: feature
availability: ga
realises: [model-monitoring, drift-detection, model-performance-monitoring, inference-logging]
resource: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-monitoring
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model monitoring](../../capabilities/mlops/model-monitoring.md) (ML operations) (primary): Track the health of production models, including inputs, outputs, quality and service metrics.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.
- [Inference logging](../../capabilities/mlops/inference-logging.md) (ML operations): Capture model inputs, outputs and metadata for monitoring, audit and retraining.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Azure Machine Learning

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Monitoring on Agent Platform](../google-cloud/gcp-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Inference logging](../../capabilities/mlops/inference-logging.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data profiling](../databricks/databricks-data-profiling.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
