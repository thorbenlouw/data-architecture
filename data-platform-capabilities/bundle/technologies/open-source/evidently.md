---
type: Technology
id: evidently
title: Evidently
description: Python library for evaluating and monitoring ML models and LLM applications, with data drift, data quality and model quality reports and tests.
aliases: [Evidently AI]
platform: platform-open-source
kind: open-source
availability: ga
realises: [drift-detection, model-performance-monitoring, genai-evaluation, data-profiling]
resource: https://github.com/evidentlyai/evidently
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by Evidently AI, which sells Evidently Cloud. Can run as batch checks in pipelines or as a self-hosted monitoring UI.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations) (primary): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.
- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations): Measure prediction quality over time against ground truth as it arrives.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Monitoring on Agent Platform](../google-cloud/gcp-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data profiling](../databricks/databricks-data-profiling.md) | [Data profiling](../../capabilities/data-quality/data-profiling.md), [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Arize AX](../independent/arize-ax.md), [Fiddler AI Control Plane](../independent/fiddler-ai-control-plane.md), [DataRobot AI Platform](../independent/datarobot-ai-platform.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
