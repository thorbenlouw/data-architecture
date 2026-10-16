---
type: Technology
id: langsmith
title: LangSmith
description: Platform for tracing, monitoring and evaluating LLM agents, managing prompts, and deploying and running agents in production.
platform: platform-independent
vendor: LangChain
kind: saas
availability: ga
realises:
- genai-observability
- genai-evaluation
- prompt-management
- ai-agents
- ai-gateway
- agent-runtime
- agent-memory
- training-dataset-management
resource: https://www.langchain.com/langsmith
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Its components are Observability, Evaluation, LangSmith Engine (automated agent improvement), LangSmith Deployment (agent hosting, formerly LangGraph Platform), Sandboxes, an LLM Gateway and LangSmith Fleet (no-code agents). It works with any framework, not only LangChain. Available as managed cloud, bring-your-own-cloud or self-hosted on Kubernetes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI) (primary): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI): Route, secure, rate-limit and track model calls across providers from one place.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Agent memory](../../capabilities/generative-ai/agent-memory.md) (Generative AI): Store and recall conversation state and long-term facts for agents across sessions, with retention controls.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore](../aws/aws-bedrock-agentcore.md), [Amazon SageMaker AI with MLflow](../aws/aws-sagemaker-mlflow.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry observability and tracing](../microsoft/azure-foundry-observability.md), [Foundry Control Plane](../microsoft/azure-foundry-control-plane.md) (preview) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Observability](../google-cloud/gcp-agent-observability.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Databricks](../../platforms/platform-databricks.md) | [MLflow Tracing on Databricks](../databricks/databricks-mlflow-tracing.md), [Unity Gateway](../databricks/databricks-unity-gateway.md) | [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Enterprise AgentStack](../teradata/teradata-agentstack.md) (preview) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [Agent memory](../../capabilities/generative-ai/agent-memory.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md) | [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md), [AI agents](../../capabilities/generative-ai/ai-agents.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [OpenTelemetry semantic conventions for generative AI](../open-source/opentelemetry-genai-semantic-conventions.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) |
