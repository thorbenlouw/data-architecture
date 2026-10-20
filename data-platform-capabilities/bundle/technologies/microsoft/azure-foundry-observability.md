---
type: Technology
id: azure-foundry-observability
title: Microsoft Foundry observability and tracing
description: Captures OpenTelemetry traces of agent and model calls with latency, token use and tool steps, stored in Application Insights.
platform: platform-microsoft
kind: feature
availability: ga
realises: [genai-observability]
resource: https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tracing is GA for prompt and hosted agents and preview for workflow and external agents; dashboards are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md), [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Observability](../google-cloud/gcp-agent-observability.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview), [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview), [MLflow](../open-source/mlflow.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md), [Arize AX](../independent/arize-ax.md), [Splunk Agent Observability](../independent/galileo.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
