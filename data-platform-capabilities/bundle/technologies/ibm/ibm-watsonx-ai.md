---
type: Technology
id: ibm-watsonx-ai
title: IBM watsonx.ai
description: Studio and runtime for foundation models and ML, including Prompt Lab, model tuning, AutoAI, notebooks, RAG tooling and deployment of models and AI services through APIs.
aliases: [watsonx.ai Studio, watsonx.ai Runtime]
formerly: [Watson Studio, Watson Machine Learning]
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- foundation-model-access
- model-customisation
- automl
- real-time-inference
- prompt-management
- pretrained-predictive-models
- generative-model-serving
- notebooks
resource: https://www.ibm.com/products/watsonx-ai
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hosts IBM Granite and third-party models (including open-weight models such as gpt-oss) and customer-imported models. Runs as SaaS or self-managed on Software Hub. watsonx Orchestrate handles enterprise-wide agent orchestration.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI) (primary): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [AutoML](../../capabilities/machine-learning/automl.md) (Machine learning development): Try features, algorithms and settings automatically to produce a good baseline model with little code.
- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations): Serve predictions through low-latency endpoints.
- [Prompt management](../../capabilities/generative-ai/prompt-management.md) (Generative AI): Version, test and reuse prompts and model configurations.
- [Pretrained predictive models](../../capabilities/machine-learning/pretrained-predictive-models.md) (Machine learning development): Forecast, classify or detect anomalies on business tables with pretrained models, without training a model for each use case.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md), [Amazon Bedrock](../aws/aws-bedrock.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Garden](../google-cloud/gcp-model-garden.md), [Gemini Enterprise Agent Platform](../google-cloud/gcp-gemini-enterprise-agent-platform.md), [Gemini models on Agent Platform](../google-cloud/gcp-gemini-models.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex REST API](../snowflake/snowflake-cortex-rest-api.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Foundation Model APIs](../databricks/databricks-foundation-model-apis.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP AI Foundation (SAP AI Core and generative AI hub)](../sap/sap-ai-foundation.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Pretrained predictive models](../../capabilities/machine-learning/pretrained-predictive-models.md), [Prompt management](../../capabilities/generative-ai/prompt-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir AIP and AIP Model Catalog](../palantir/palantir-aip.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) |
