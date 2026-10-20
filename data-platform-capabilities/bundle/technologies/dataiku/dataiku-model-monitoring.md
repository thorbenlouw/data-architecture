---
type: Technology
id: dataiku-model-monitoring
title: Dataiku model evaluation stores and Unified Monitoring
description: Stores of repeated model evaluations with drift and performance metrics, and dashboards that show the health of deployed projects, Dataiku API endpoints and external endpoints.
aliases: [Model evaluation stores, Unified Monitoring]
platform: platform-dataiku
kind: feature
availability: ga
realises: [model-performance-monitoring, drift-detection]
resource: https://doc.dataiku.com/dss/latest/mlops/model-evaluations/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Evaluation recipes score a model on new data, such as the records logged by API nodes, and write performance and drift metrics to an evaluation store; performance metrics need ground truth joined to the predictions. Checks on these metrics let scenarios alert or retrain. Unified Monitoring also shows endpoints on third-party platforms that Dataiku does not manage.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations) (primary): Measure prediction quality over time against ground truth as it arrives.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data profiling](../databricks/databricks-data-profiling.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Model Manager](../sas/sas-model-manager.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fiddler AI Control Plane](../independent/fiddler-ai-control-plane.md), [Arize AX](../independent/arize-ax.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
