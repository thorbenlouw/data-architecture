---
type: Technology
id: azure-foundry-evaluations
title: Microsoft Foundry evaluations
description: Scores model and agent outputs with built-in and custom evaluators for quality, groundedness and safety, offline or continuously in production.
platform: platform-microsoft
kind: feature
availability: ga
realises: [genai-evaluation, ai-red-teaming]
resource: https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some evaluators remain preview. Includes an AI Red Teaming Agent for adversarial testing.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [AI red teaming](../../capabilities/generative-ai/ai-red-teaming.md) (Generative AI): Probe models and agents adversarially for prompt injection, jailbreaks and unsafe behaviour before and after release.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Evaluations](../aws/aws-bedrock-agentcore-evaluations.md), [Amazon Bedrock Evaluations](../aws/aws-bedrock-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md), [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md), [MLflow](../open-source/mlflow.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Splunk Agent Observability](../independent/galileo.md), [Scale Data Engine](../independent/scale-data-engine.md), [Braintrust](../independent/braintrust.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [AI red teaming](../../capabilities/generative-ai/ai-red-teaming.md) |
