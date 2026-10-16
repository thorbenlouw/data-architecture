---
type: Technology
id: azure-openai
title: Azure OpenAI in Foundry Models
description: OpenAI language, reasoning, embedding, image, video and audio models hosted in Azure under Azure data handling, networking and SLAs.
aliases: [Azure OpenAI]
formerly: [Azure OpenAI Service]
platform: platform-microsoft
kind: managed-service
availability: ga
realises:
- foundation-model-access
- embedding-generation
- model-customisation
- reserved-capacity
- ai-content-provenance
resource: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Deployed through a Foundry resource; provisioned throughput and data-zone deployments help with capacity and residency. Some newer models arrive first as preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
- [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md) (Generative AI): Mark AI-generated content in machine-readable form and detect such marks so synthetic content can be identified.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock](../aws/aws-bedrock.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Model Garden](../google-cloud/gcp-model-garden.md) | [AI content marking and provenance](../../capabilities/generative-ai/ai-content-provenance.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
