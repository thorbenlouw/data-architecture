---
type: Technology
id: gcp-gen-ai-evals
title: Gen AI evals on Agent Platform
description: Evaluates model and agent outputs with computed metrics, model-based judges and rubrics, offline, against simulated users or as online monitoring.
aliases: [Gen AI evals]
formerly: [Gen AI evaluation service, Gen AI evaluation service on Vertex AI]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [genai-evaluation]
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agent evaluation covers tool-call trajectories as well as final responses, and results can drive prompt optimisation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Evaluations](../aws/aws-bedrock-agentcore-evaluations.md), [Amazon Bedrock Evaluations](../aws/aws-bedrock-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry evaluations](../microsoft/azure-foundry-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md), [MLflow](../open-source/mlflow.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Splunk Agent Observability](../independent/galileo.md), [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md), [Braintrust](../independent/braintrust.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
