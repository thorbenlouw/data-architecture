---
type: Technology
id: mlflow
title: MLflow
description: Platform for the ML and generative AI lifecycle, covering experiment tracking, model registry, model packaging, tracing, evaluation and prompt management.
platform: platform-open-source
kind: open-source
availability: ga
realises:
- experiment-tracking
- model-registry
- genai-observability
- genai-evaluation
- prompt-management
- model-evaluation
- training-dataset-management
resource: https://mlflow.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, a Linux Foundation project with Databricks as main contributor. MLflow 3 added OpenTelemetry-based tracing, LLM judges, a prompt registry and an AI Gateway for routing model calls. Managed versions exist on Databricks, AWS SageMaker and Azure ML.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development) (primary): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning registries and MLflow tracking](../microsoft/azure-ml-registries-mlflow.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Experiments on Agent Platform](../google-cloud/gcp-agent-platform-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ML Experiments](../snowflake/snowflake-ml-experiments.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Comet ML](../independent/comet.md), [Weights & Biases](../independent/weights-and-biases.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
