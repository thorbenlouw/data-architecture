---
type: Technology
id: sap-ai-foundation
title: SAP AI Foundation (SAP AI Core and generative AI hub)
description: SAP BTP services for running custom AI, with the generative AI hub giving governed access to many LLMs plus orchestration, grounding, content filtering and data masking.
aliases: [AI Foundation on SAP BTP, SAP AI Core, generative AI hub]
platform: platform-sap
kind: managed-service
availability: ga
realises:
- foundation-model-access
- ai-gateway
- ai-guardrails
- model-deployment
- prompt-management
- pretrained-predictive-models
resource: https://www.sap.com/products/artificial-intelligence/ai-foundation-os.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hosts SAP's own models, including SAP-RPT-1 for predictions on tabular business data (also callable from HANA Cloud SQL) and SAP-ABAP-1. Prompt optimisation tooling was added in 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI): Route, secure, rate-limit and track model calls across providers from one place.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [Model deployment](../../capabilities/mlops/model-deployment.md) (ML operations): Package and release models into production for batch, real-time or streaming use.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [Pretrained predictive models](../../capabilities/machine-learning/pretrained-predictive-models.md) (Machine learning development): Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Technology Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock](../aws/aws-bedrock.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Model Garden](../google-cloud/gcp-model-garden.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Pretrained predictive models](../../capabilities/machine-learning/pretrained-predictive-models.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
