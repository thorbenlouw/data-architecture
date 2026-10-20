---
type: Technology
id: aws-bedrock-evaluations
title: Amazon Bedrock Evaluations
description: Evaluation jobs that score models and RAG sources against built-in or custom datasets using metrics, LLM-as-a-judge or human reviewers.
platform: platform-aws
kind: feature
availability: ga
realises: [genai-evaluation, model-evaluation]
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Can evaluate models and RAG systems hosted outside Bedrock by supplying their responses. For agent evaluation use AgentCore Evaluations.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) (Machine learning development): Assess models against holdout data, baselines and business criteria before release.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry evaluations](../microsoft/azure-foundry-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Retrieval Agent Manager](../sas/sas-retrieval-agent-manager.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku LLM Mesh](../dataiku/dataiku-llm-mesh.md), [Dataiku Visual Agents and Code Agents](../dataiku/dataiku-agents.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [Evidently](../open-source/evidently.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Model evaluation](../../capabilities/machine-learning/model-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Splunk Agent Observability](../independent/galileo.md), [Braintrust](../independent/braintrust.md), [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
