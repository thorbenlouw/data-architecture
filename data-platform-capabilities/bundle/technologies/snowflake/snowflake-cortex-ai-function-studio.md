---
type: Technology
id: snowflake-cortex-ai-function-studio
title: Snowflake Cortex AI Function Studio
description: A Snowsight workspace for designing prompts for Cortex AI Functions, evaluating them against labelled data and optimising them.
platform: platform-snowflake
kind: feature
availability: preview
realises: [prompt-management, genai-evaluation]
resource: https://docs.snowflake.com/en/release-notes/new-features-2026
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public preview since May 2026. Cortex AI Function Evaluation and Optimization followed in public preview in September 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI) (primary): Version, test and reuse prompts and model configurations.
- [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) (Generative AI): Assess the quality, accuracy and safety of model and agent outputs using test sets, human review and model-based judges.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Prompt management](../aws/aws-bedrock-prompt-management.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md), [Gen AI evals on Agent Platform](../google-cloud/gcp-gen-ai-evals.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md), [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [Comet ML](../independent/comet.md) | [Generative AI evaluation](../../capabilities/generative-ai/genai-evaluation.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
