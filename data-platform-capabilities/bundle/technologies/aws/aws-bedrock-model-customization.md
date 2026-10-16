---
type: Technology
id: aws-bedrock-model-customization
title: Amazon Bedrock custom models
description: Adapts supported foundation models with fine-tuning, continued pre-training or distillation, and imports externally trained weights for serving.
aliases: [Amazon Bedrock Custom Model Import, Amazon Bedrock model customization]
platform: platform-aws
kind: feature
availability: ga
realises: [model-customisation]
resource: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Customised models run in your account and are invoked like base models. For deeper control or unsupported architectures, use SageMaker AI training, HyperPod or JumpStart.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI) (primary): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Bedrock

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Cortex Fine-tuning](../snowflake/snowflake-cortex-fine-tuning.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Runtime](../databricks/databricks-ai-runtime.md) (preview) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Snorkel AI](../independent/snorkel-ai.md), [Scale Data Engine](../independent/scale-data-engine.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
