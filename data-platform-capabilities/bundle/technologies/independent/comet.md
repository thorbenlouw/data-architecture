---
type: Technology
id: comet
title: Comet ML
description: ML experiment management (tracking, artefacts, model registry and production monitoring) together with Opik for tracing, evaluating and optimising LLM applications and agents.
aliases: [Comet, CometML, Opik]
platform: platform-independent
vendor: Comet
kind: saas
availability: ga
realises: [experiment-tracking, model-registry, genai-observability, genai-evaluation, prompt-management]
resource: https://www.comet.com/site/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Opik, Comet's open-source tracing and evaluation project, can also be self-hosted. The hosted and enterprise offering adds Opik cost intelligence, an Agent Optimizer, ML experiment management and model production monitoring.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Experiments](../snowflake/snowflake-ml-experiments.md), [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual ML](../dataiku/dataiku-visual-ml.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [DVC (Data Version Control)](../open-source/dvc.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
