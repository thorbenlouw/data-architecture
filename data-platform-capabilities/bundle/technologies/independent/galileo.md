---
type: Technology
id: galileo
title: Splunk Agent Observability
description: Evaluation and observability for AI agents and LLM applications, formerly Galileo, that uses small evaluation models to score outputs and block bad ones at runtime.
aliases: [Galileo AI]
formerly: [Galileo]
platform: platform-independent
vendor: Splunk (Cisco)
kind: saas
availability: ga
realises: [genai-evaluation, genai-observability, ai-guardrails]
resource: https://www.splunk.com/en_us/about-splunk/acquisitions/galileo.html
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cisco announced in April 2026 that it would buy Galileo and has completed the purchase. The product is now sold as Splunk Agent Observability within Splunk's observability portfolio. Before the acquisition its components were Agent Reliability, Signals, the Luna-2 evaluation models and Protect (runtime guardrails).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI) (primary): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.
- [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) (Generative AI): Trace model and agent calls with their prompts, responses, latency, cost and user feedback.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock AgentCore Evaluations](../aws/aws-bedrock-agentcore-evaluations.md), [Amazon Bedrock Evaluations](../aws/aws-bedrock-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry evaluations](../microsoft/azure-foundry-evaluations.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI Observability](../snowflake/snowflake-ai-observability.md), [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Agent Evaluation (MLflow GenAI evaluation)](../databricks/databricks-agent-evaluation.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx Orchestrate](../ibm/ibm-watsonx-orchestrate.md), [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md), [Evidently](../open-source/evidently.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Generative AI observability](../../capabilities/generative-ai/genai-observability.md) |
