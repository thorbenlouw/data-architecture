---
type: Technology
id: fiddler-ai-control-plane
title: Fiddler AI Control Plane
description: Monitoring, explainability and guardrails for ML models, LLM applications and agents, using Fiddler's own small evaluation models to score outputs quickly.
aliases: [Fiddler]
platform: platform-independent
vendor: Fiddler AI
kind: saas
availability: ga
realises:
- model-performance-monitoring
- genai-observability
- ai-guardrails
- model-explainability
- drift-detection
resource: https://www.fiddler.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Its components are ML Observability, Agentic Observability, Continuous Evaluations, Fiddler Guardrails and governance and compliance reporting. Fiddler Centor Models are small models that score outputs and can run inside your VPC. It has a strong legacy in explainability for regulated ML.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) (ML operations) (primary): Measure prediction quality over time against ground truth as it arrives.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Model explainability](../../capabilities/machine-learning/model-explainability.md) (Machine learning development): Explain which inputs drive a model's predictions, overall and for individual predictions.
- [Drift detection](../../capabilities/mlops/drift-detection.md) (ML operations): Detect when live input data, or its relationship to outcomes, moves away from what the model was trained on.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning model monitoring](../microsoft/azure-ml-model-monitoring.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Observability (model monitors)](../snowflake/snowflake-ml-observability.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks data profiling](../databricks/databricks-data-profiling.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata ModelOps](../teradata/teradata-modelops.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md) | [Drift detection](../../capabilities/mlops/drift-detection.md), [Model performance monitoring](../../capabilities/mlops/model-performance-monitoring.md) |
