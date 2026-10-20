---
type: Technology
id: gcp-agent-observability
title: Google Cloud Agent Observability
description: Traces, logs, metrics and topology views of agent runs, tool calls and model calls on Agent Platform, built on Cloud Observability.
aliases: [Agent Observability]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [genai-observability]
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA June 2026; includes token usage and content security violation views. BigQuery data agents can also be monitored through Cloud Observability (preview).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md), [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry observability and tracing](../microsoft/azure-foundry-observability.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Agent Management](../dataiku/dataiku-agent-management.md) (preview), [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview), [MLflow](../open-source/mlflow.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md), [Arize AX](../independent/arize-ax.md), [Splunk Agent Observability](../independent/galileo.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
