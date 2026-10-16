---
type: Technology
id: aws-bedrock
title: Amazon Bedrock
description: Managed API for invoking foundation models from Amazon and third parties, with on-demand, batch, cross-Region and provisioned inference options.
platform: platform-aws
kind: managed-service
availability: ga
realises:
- foundation-model-access
- embedding-generation
- reserved-capacity
- ai-spend-controls
- ai-content-provenance
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hosts over 100 models including Amazon Nova, Anthropic Claude, OpenAI, DeepSeek, Moonshot AI, MiniMax and xAI models, plus Bedrock Marketplace and Custom Model Import. Batch inference suits bulk enrichment of tables. Data is not used to train the providers' models.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md) (Generative AI): Mark AI-generated content in machine-readable form and detect such marks so synthetic content can be identified.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md), [Microsoft Foundry](../microsoft/azure-foundry.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Model Garden](../google-cloud/gcp-model-garden.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
