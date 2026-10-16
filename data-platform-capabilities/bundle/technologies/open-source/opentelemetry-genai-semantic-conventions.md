---
type: Technology
id: opentelemetry-genai-semantic-conventions
title: OpenTelemetry semantic conventions for generative AI
description: Standard attribute names and structures for tracing LLM calls, agents and MCP interactions, including model, token usage, prompts and responses.
aliases: [OTel GenAI semantic conventions, GenAI semantic conventions]
platform: platform-open-source
kind: open-standard
availability: preview
realises: [genai-observability, inference-logging]
resource: https://github.com/open-telemetry/semantic-conventions-genai
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Still at development status and recently moved to a dedicated repository. Supported by MLflow, Langfuse and many commercial observability tools, but attribute names may still change.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Inference logging](../../capabilities/mlops/inference-logging.md) (ML operations): Capture model inputs, outputs and metadata for monitoring, audit and retraining.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md), [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry observability and tracing](../microsoft/azure-foundry-observability.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Observability](../google-cloud/gcp-agent-observability.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md), [Databricks inference tables](../databricks/databricks-inference-tables.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Inference logging](../../capabilities/mlops/inference-logging.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md), [Arize AX](../independent/arize-ax.md), [LangSmith](../independent/langsmith.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
