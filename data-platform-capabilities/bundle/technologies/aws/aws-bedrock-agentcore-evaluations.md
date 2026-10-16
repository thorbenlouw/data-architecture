---
type: Technology
id: aws-bedrock-agentcore-evaluations
title: Amazon Bedrock AgentCore Evaluations
description: Scores agent sessions, traces and tool calls with built-in, third-party or custom evaluators, online or in batch, and supports A/B tests between agent versions.
aliases: [AgentCore Evaluations]
platform: platform-aws
kind: feature
availability: ga
realises: [genai-evaluation, canary-ab-testing]
resource: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA March 2026 with built-in evaluators for quality, safety, task completion and tool use; batch evaluation, A/B testing and prompt and tool-description recommendations became GA in June 2026. Failure Insights is in preview. Works for agents hosted outside AgentCore through OpenTelemetry.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock AgentCore

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
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Evidently](../open-source/evidently.md), [MLflow](../open-source/mlflow.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Splunk Agent Observability](../independent/galileo.md), [Braintrust](../independent/braintrust.md), [Monte Carlo Agent Observability](../independent/monte-carlo-agent-observability.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
