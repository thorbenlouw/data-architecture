---
type: Technology
id: databricks-foundation-model-apis
title: Databricks Foundation Model APIs
description: Databricks-hosted proprietary and open language and embedding models, available pay-per-token or with provisioned throughput. They are exposed as governed model services in the system.ai schema.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [foundation-model-access, embedding-generation, reserved-capacity]
resource: https://docs.databricks.com/aws/en/machine-learning/model-serving/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Model availability differs by region and depends on partner-powered AI settings. Foundation model Unity Catalog permissions became GA in June 2026. External providers can be registered through Unity Gateway.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) (Generative AI): Turn text, images or other content into vector embeddings for search and retrieval.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock](../aws/aws-bedrock.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md), [Microsoft Foundry](../microsoft/azure-foundry.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Model Garden](../google-cloud/gcp-model-garden.md) | [Embedding generation](../../capabilities/generative-ai/embedding-generation.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Embedding generation](../../capabilities/generative-ai/embedding-generation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
