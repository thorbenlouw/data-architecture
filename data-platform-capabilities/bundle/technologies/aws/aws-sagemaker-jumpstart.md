---
type: Technology
id: aws-sagemaker-jumpstart
title: Amazon SageMaker JumpStart
description: Hub of open-weight and proprietary foundation models and solution templates that can be fine-tuned and deployed to SageMaker AI endpoints in your account.
platform: platform-aws
kind: feature
availability: ga
realises: [foundation-model-access, model-customisation, generative-model-serving]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Chosen over Bedrock when you need control of the serving instance, custom weights or models Bedrock does not host. Private hubs restrict which models teams can use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Garden](../google-cloud/gcp-model-garden.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
