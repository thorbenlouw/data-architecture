---
type: Technology
id: clickhouse-langfuse
title: Langfuse
description: LLM engineering platform that traces model and agent calls, runs evaluations and experiments on datasets, and versions prompts, available self-hosted or as Langfuse Cloud.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [genai-observability, genai-evaluation, prompt-management, training-dataset-management]
resource: https://langfuse.com/docs
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Acquired by ClickHouse in January 2026, which states it will stay open source and self-hostable. The core is MIT-licensed (except the ee folders), and Langfuse Cloud continues as a separate SaaS. It accepts OpenTelemetry traces and stores them in ClickHouse, so self-hosted deployments need a ClickHouse instance.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Agentic Data Stack

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md), [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry observability and tracing](../microsoft/azure-foundry-observability.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Observability](../google-cloud/gcp-agent-observability.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md), [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md), [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [LangSmith](../independent/langsmith.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
