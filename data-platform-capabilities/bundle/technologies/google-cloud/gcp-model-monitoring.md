---
type: Technology
id: gcp-model-monitoring
title: Model Monitoring on Agent Platform
description: Scheduled or on-demand monitoring jobs that compare production inputs and predictions with training data to detect drift and skew.
formerly: [Vertex AI Model Monitoring]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [model-monitoring, drift-detection]
resource: https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Monitors feature drift, prediction drift and feature attribution changes for models in Model Registry and alerts through Cloud Monitoring.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model monitoring](../../capabilities/mlops/model-monitoring.md) (ML operations) (primary): Track the health of production models, including inputs, outputs, quality and service metrics.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md) |
