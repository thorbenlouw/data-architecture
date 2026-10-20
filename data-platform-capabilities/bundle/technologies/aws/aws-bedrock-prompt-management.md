---
type: Technology
id: aws-bedrock-prompt-management
title: Amazon Bedrock Prompt management
description: Library for storing prompts with variables, model settings and variants, saving immutable versions and optimising prompts for a chosen model.
platform: platform-aws
kind: feature
availability: ga
realises: [prompt-management]
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Versions are referenced at inference time or from Amazon Bedrock Flows, a visual builder that chains prompts, knowledge bases and Lambda functions into deployable generative AI workflows.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI) (primary): Version, test and reuse prompts and model configurations.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex AI Function Studio](../snowflake/snowflake-cortex-ai-function-studio.md) (preview) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Managed MLflow on Databricks](../databricks/databricks-managed-mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [Langfuse](../clickhouse/clickhouse-langfuse.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Joule Studio](../sap/sap-joule-studio.md), [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [AIP Logic and AIP Evals](../palantir/palantir-aip-logic.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Agentic AI Accelerator](../sas/sas-agentic-ai-accelerator.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Prompt Studios](../dataiku/dataiku-prompt-studios.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [MLflow](../open-source/mlflow.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Braintrust](../independent/braintrust.md), [Arize AX](../independent/arize-ax.md), [Comet ML](../independent/comet.md) | [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
