---
type: Technology
id: palantir-aip
title: Palantir AIP and AIP Model Catalog
description: Palantir's generative AI layer that provides governed access to commercial and open LLMs, capacity management and the AIP applications on top of Foundry and the Ontology.
aliases: [AIP, Artificial Intelligence Platform, AIP Model Catalog]
platform: platform-palantir
kind: managed-service
availability: ga
realises: [foundation-model-access, ai-gateway, ai-spend-controls]
resource: https://www.palantir.com/docs/foundry/aip/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Model Catalog lists available models and deprecations; administrators manage LLM capacity and rate limits per enrolment. Customers can also bring their own model endpoints. AIP Bootcamps are Palantir's sales motion, not a product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI): Route, secure, rate-limit and track model calls across providers from one place.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir AIP

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock](../aws/aws-bedrock.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock AgentCore Gateway](../aws/aws-bedrock-agentcore-gateway.md) | [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md), [Model Garden](../google-cloud/gcp-model-garden.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [AI gateway](../../capabilities/generative-ai/ai-gateway.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [LiteLLM](../open-source/litellm.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) |
