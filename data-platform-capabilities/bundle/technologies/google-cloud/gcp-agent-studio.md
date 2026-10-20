---
type: Technology
id: gcp-agent-studio
title: Google Cloud Agent Studio
description: Console workspace for designing and testing prompts and agents, comparing models and tuning Gemini models.
aliases: [Agent Studio, App Builder in Agent Studio]
formerly: [Vertex AI Studio]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [prompt-management, model-customisation]
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Model customisation covers supervised fine-tuning of Gemini models, reinforcement learning fine-tuning (preview) and a distillation service (early access). App Builder now lives inside Agent Studio.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI) (primary): Version, test and reuse prompts and model configurations.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Prompt management](../aws/aws-bedrock-prompt-management.md), [Amazon Bedrock custom models](../aws/aws-bedrock-model-customization.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview), [Snowflake Cortex Fine-tuning](../snowflake/snowflake-cortex-fine-tuning.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Prompt Studios](../dataiku/dataiku-prompt-studios.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [Comet ML](../independent/comet.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
