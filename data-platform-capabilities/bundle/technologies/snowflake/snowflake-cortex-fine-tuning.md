---
type: Technology
id: snowflake-cortex-fine-tuning
title: Snowflake Cortex Fine-tuning
description: Builds parameter-efficient fine-tuned adaptors for supported base models from training data in Snowflake, for inference through AI_COMPLETE.
platform: platform-snowflake
kind: feature
availability: ga
realises: [model-customisation]
resource: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports a small set of base models (currently llama3.1-8b and arctic-extract) in a few regions only.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI) (primary): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Cortex AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock custom models](../aws/aws-bedrock-model-customization.md), [Amazon SageMaker HyperPod](../aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Foundry](../microsoft/azure-foundry.md), [Azure OpenAI in Foundry Models](../microsoft/azure-openai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Agent Studio](../google-cloud/gcp-agent-studio.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Runtime](../databricks/databricks-ai-runtime.md) (preview) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Snorkel AI](../independent/snorkel-ai.md), [Scale Data Engine](../independent/scale-data-engine.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
