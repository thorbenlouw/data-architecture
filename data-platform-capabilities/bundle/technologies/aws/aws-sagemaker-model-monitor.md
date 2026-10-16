---
type: Technology
id: aws-sagemaker-model-monitor
title: Amazon SageMaker Model Monitor
description: Scheduled jobs that compare captured endpoint traffic with a baseline to report data quality, model quality, bias and attribution drift.
platform: platform-aws
kind: feature
availability: deprecated
realises: [model-monitoring, drift-detection, model-performance-monitoring, inference-logging]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-availability-change.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In maintenance and closed to new customers from 30 July 2026. AWS recommends open-source monitoring solutions built on SageMaker AI MLflow Apps and Evidently AI, with CloudWatch alarms and Quick dashboards.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model monitoring](../../capabilities/mlops/model-monitoring.md) (ML operations) (primary): Track the health of production models, including inputs, outputs, quality and service metrics.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.
- [Inference logging](../../capabilities/mlops/inference-logging.md) (ML operations): Capture model inputs, outputs and metadata for monitoring, audit and retraining.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
**Product family:** Amazon SageMaker AI  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Inference logging](../../capabilities/mlops/inference-logging.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Monitoring on Agent Platform](../google-cloud/gcp-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Inference logging](../../capabilities/mlops/inference-logging.md), [Model monitoring](../../capabilities/mlops/model-monitoring.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data profiling](../databricks/databricks-data-profiling.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
