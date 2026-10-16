---
type: Technology
id: snowflake-ai-observability
title: Snowflake AI Observability
description: Tracing, cost tracking and batch evaluation for agents, Cortex Search, CoCo and custom TruLens-instrumented apps, stored in an account event table and viewed in Snowsight.
platform: platform-snowflake
kind: feature
availability: ga
realises: [genai-observability, genai-evaluation]
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cortex Agent evaluations became GA in March 2026, and agent tool-evaluation metrics are in preview. Custom apps register as External Agent objects. Trace delivery is best effort, so use the ACCOUNT_USAGE views for billing.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md), [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry observability and tracing](../microsoft/azure-foundry-observability.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Observability](../google-cloud/gcp-agent-observability.md), [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview), [MLflow](../open-source/mlflow.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md), [Splunk Agent Observability](../independent/galileo.md), [Arize AX](../independent/arize-ax.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
