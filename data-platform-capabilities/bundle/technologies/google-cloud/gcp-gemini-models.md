---
type: Technology
id: gcp-gemini-models
title: Gemini models on Agent Platform
description: Hosted access to Google's Gemini multimodal, embedding, image and speech models through Agent Platform APIs with pay-as-you-go, priority or provisioned throughput.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- foundation-model-access
- embedding-generation
- reserved-capacity
- ai-spend-controls
- ai-content-provenance
resource: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Gemini 3.x Flash models and Gemini 4 Argon (GA October 2026) are current; Gemini Embedding 2 provides embeddings. Provisioned Throughput and Priority PayGo reserve or prioritise capacity, and zero data retention options are available.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.
- [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md) (Generative AI): Mark AI-generated content in machine-readable form and detect such marks so synthetic content can be identified.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock](../aws/aws-bedrock.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md), [Microsoft Foundry](../microsoft/azure-foundry.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
