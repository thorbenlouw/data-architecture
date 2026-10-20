---
type: Capability
id: foundation-model-access
title: Foundation model access
description: Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
aliases: [model garden, LLM APIs]
broader: [generative-ai]
related: [real-time-inference, reserved-capacity, data-residency, gpu-compute, ai-spend-controls]
depends_on: [identity-authentication, network-security]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The platform exposes endpoints for language, embedding, speech and multimodal models. They may be the platform vendor's own models, third-party models resold through it, or open-weight models served on the platform's GPUs. Calls use the platform's existing identity, network and logging controls, so a pipeline or application reaches a model with the credentials it already has and data stays inside the agreed boundary. For example, a claims pipeline sends each claim note to a hosted model to extract the incident date and cause, with the request processed in-region and not kept by the model provider.

Most organisations cannot send sensitive data to consumer AI services, so governed access is usually the first generative AI capability built. Commercial options include shared pay-per-token endpoints, reserved throughput for steady production load, and batch APIs that are cheaper for large offline jobs. This capability is about reaching models. Routing and policy across many providers belong to the AI gateway, and changing a model's behaviour through training belongs to model customisation.

# Key considerations

- Check retention, abuse-monitoring logs and training use separately for each provider. A promise not to train on your data does not mean nothing is stored.
- Model availability differs by region. The model a use case needs may not be offered where its data must stay.
- Shared endpoints can be throttled at peak times. Production workloads may need reserved throughput or a fallback model.
- Providers retire model versions on a schedule, often within a year. Budget for re-evaluating and adjusting prompts on each migration.
- Use batch interfaces for bulk enrichment and backfills. They are usually much cheaper per token than interactive calls.

# Questions to ask

- Which modalities do the use cases need: text, images, speech, embeddings?
- Where must data be processed, and which model providers are approved?
- What throughput and response time are required, and how much does demand vary?
- Is there a need to run open-weight models on infrastructure you control?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Narrower | [AI gateway](ai-gateway.md), [Generative model serving](../mlops/generative-model-serving.md) |
| Related | [AI usage and spend controls](../platform-operations/ai-spend-controls.md), [Data residency and sovereignty](../governance/data-residency.md), [Embedding generation](embedding-generation.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Pretrained predictive models](../machine-learning/pretrained-predictive-models.md), [Real-time inference](../mlops/real-time-inference.md), [Reserved and committed capacity](../compute/reserved-capacity.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md), [Network security](../security/network-security.md) |
| Needed by | [AI agents](ai-agents.md), [AI functions in SQL](../processing/ai-functions.md), [AI-assisted development](../development-lifecycle/ai-assisted-development.md), [AI-generated documentation](../metadata/ai-generated-documentation.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Data engineering agents](../development-lifecycle/data-engineering-agents.md), [Enterprise AI assistant](enterprise-ai-assistant.md), [Retrieval-augmented generation](retrieval-augmented-generation.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 2) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 2, Managed)
- **Frameworks:** [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.10 – Third-party and customer relationships · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 6 – Third-party risk; MAP 4 – Risks of components; MANAGE 3 – Third-party risk monitoring

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Bedrock | [Amazon Bedrock](../../technologies/aws/aws-bedrock.md), [Amazon SageMaker JumpStart](../../technologies/aws/aws-sagemaker-jumpstart.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Foundry Models | [Azure OpenAI in Foundry Models](../../technologies/microsoft/azure-openai.md), [Microsoft Foundry](../../technologies/microsoft/azure-foundry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Gemini Enterprise Agent Platform (formerly Vertex AI); Model Garden | [Gemini Enterprise Agent Platform](../../technologies/google-cloud/gcp-gemini-enterprise-agent-platform.md), [Gemini models on Agent Platform](../../technologies/google-cloud/gcp-gemini-models.md), [Model Garden](../../technologies/google-cloud/gcp-model-garden.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Functions](../../technologies/snowflake/snowflake-cortex-ai-functions.md), [Snowflake Cortex REST API](../../technologies/snowflake/snowflake-cortex-rest-api.md) |
| [Databricks](../../platforms/platform-databricks.md) | Foundation Model APIs (model services) | [Databricks Foundation Model APIs](../../technologies/databricks/databricks-foundation-model-apis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Inference service](../../technologies/cloudera/cloudera-ai-inference-service.md) |
| [Oracle](../../platforms/platform-oracle.md) | OCI Generative AI (Enterprise AI) | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
| [SAP](../../platforms/platform-sap.md) | Generative AI hub | [SAP AI Foundation (SAP AI Core and generative AI hub)](../../technologies/sap/sap-ai-foundation.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir AIP and AIP Model Catalog](../../technologies/palantir/palantir-aip.md) |

Narrower capabilities are realised by a further 25 technologies; see their pages.
