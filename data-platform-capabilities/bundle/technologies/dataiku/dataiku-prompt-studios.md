---
type: Technology
id: dataiku-prompt-studios
title: Dataiku Prompt Studios
description: Workspace for writing, testing and comparing prompts across LLMs, and the Prompt recipe that applies a saved prompt to every row of a dataset.
aliases: [Prompt recipe]
platform: platform-dataiku
kind: feature
availability: ga
realises: [prompt-management, ai-functions]
resource: https://doc.dataiku.com/dss/latest/generative-ai/prompt-studio.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Prompts run through the [Dataiku LLM Mesh](dataiku-llm-mesh.md), so the same guardrails and cost quotas apply. A separate Automated Prompt Optimization recipe searches for a better prompt for question-answering tasks against a dataset of questions and expected answers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI) (primary): Version, test and reuse prompts and model configurations.
- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success, Dataiku LLM Mesh

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Prompt management](../aws/aws-bedrock-prompt-management.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [AI functions in SQL](../../capabilities/processing/ai-functions.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [Comet ML](../independent/comet.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
