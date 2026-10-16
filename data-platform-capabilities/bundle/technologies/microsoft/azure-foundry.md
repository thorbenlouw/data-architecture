---
type: Technology
id: azure-foundry
title: Microsoft Foundry
description: Azure's platform for building generative AI applications and agents, combining a model catalogue, agent runtime, tools, evaluation and governance in projects.
aliases: [Foundry Models]
formerly: [Azure AI Foundry, Azure AI Studio]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [foundation-model-access, model-customisation]
resource: https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Foundry Models offers models from Microsoft, OpenAI, Anthropic, Meta and others, plus fine-tuning (GA). Many features remain preview; Microsoft publishes a per-feature readiness table. Foundry (classic) hub-based projects still exist.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock](../aws/aws-bedrock.md), [Amazon Bedrock custom models](../aws/aws-bedrock-model-customization.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Model Garden](../google-cloud/gcp-model-garden.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md), [Snowflake Cortex Fine-tuning](../snowflake/snowflake-cortex-fine-tuning.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
