---
type: Technology
id: azure-prompt-flow
title: Azure Machine Learning prompt flow
description: A visual and code tool in Foundry and Azure Machine Learning for building, testing and deploying LLM flows and prompt variants.
aliases: [Prompt flow in Microsoft Foundry, promptflow]
platform: platform-microsoft
kind: feature
availability: deprecated
realises: [prompt-management, genai-evaluation]
resource: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/prompt-flow
tags: [microsoft]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

No longer recommended for new work; retires on 20 April 2027. Migrate to Microsoft Agent Framework.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI) (primary): Version, test and reuse prompts and model configurations.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** deprecated  
**Product family:** Azure Machine Learning  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Prompt management](../aws/aws-bedrock-prompt-management.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md), [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [Comet ML](../independent/comet.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
