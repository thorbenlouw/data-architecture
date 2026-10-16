---
type: Technology
id: oracle-oci-generative-ai
title: OCI Generative AI (OCI Enterprise AI)
description: Managed access to hosted and imported foundation models on OCI, with dedicated AI clusters, OpenAI-compatible APIs, guardrails, vector stores and a Responses API for building agents.
aliases: [OCI Enterprise AI, Oracle Cloud Infrastructure Generative AI, OCI Generative AI Agents]
platform: platform-oracle
kind: managed-service
availability: ga
realises:
- foundation-model-access
- ai-guardrails
- ai-agents
- model-customisation
- ai-gateway
- agent-runtime
- reserved-capacity
- generative-model-serving
resource: https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Oracle markets the service as OCI Enterprise AI (generally available 24 March 2026) while the docs keep the Generative AI name. Guardrails cover moderation, prompt injection and PII. The older OCI Generative AI Agents service, with RAG, SQL and function-calling tools, is still documented alongside it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.
- [AI agents](../../capabilities/generative-ai/ai-agents.md) (Generative AI): Build systems in which models plan, call tools and act over several steps to complete a task.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [AI gateway](../../capabilities/generative-ai/ai-gateway.md) (Generative AI): Route, secure, rate-limit and track model calls across providers from one place.
- [Agent hosting and runtime](../../capabilities/generative-ai/agent-runtime.md) (Generative AI): Deploy and run agents as managed services with identity, durable state, scaling and sandboxed code execution.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock](../aws/aws-bedrock.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md), [Microsoft Foundry](../microsoft/azure-foundry.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Garden](../google-cloud/gcp-model-garden.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [AI gateway](../../capabilities/generative-ai/ai-gateway.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
