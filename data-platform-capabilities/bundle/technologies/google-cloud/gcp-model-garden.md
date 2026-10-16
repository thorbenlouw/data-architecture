---
type: Technology
id: gcp-model-garden
title: Model Garden
description: Catalogue of Google, partner and open models that can be called as managed APIs or deployed to your own endpoints.
aliases: [Agent Platform Model Garden]
formerly: [Vertex AI Model Garden]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [foundation-model-access, generative-model-serving]
resource: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Partner models such as Anthropic Claude, Meta, Mistral, xAI and DeepSeek are offered as model-as-a-service; open models (for example Gemma) can be self-deployed on GPUs or TPUs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock](../aws/aws-bedrock.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
