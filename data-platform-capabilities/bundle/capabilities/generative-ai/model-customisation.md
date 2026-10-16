---
type: Capability
id: model-customisation
title: Model customisation
description: Adapt foundation models to a domain through fine-tuning, distillation or further training.
aliases: [fine-tuning, model customization, distillation, custom models]
broader: [generative-ai]
related: [data-labelling, synthetic-data, data-usage-rights, model-registry, distributed-training]
depends_on: [gpu-compute, genai-evaluation]
tags: [generative-ai]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Customisation changes a model's weights rather than only its prompt. Supervised fine-tuning trains on pairs of inputs and desired outputs. Parameter-efficient methods such as LoRA train small adapter layers, which is cheaper and lets one base model carry many adapters. Preference and reinforcement fine-tuning reward better outputs, and distillation trains a smaller model to imitate a larger one on your tasks. For example, a bank distils a large model's classification of complaint emails into a small model that runs at a fraction of the cost with similar accuracy.

It is worth doing when prompting and retrieval fall short: a consistent output format or tone, a narrow task run millions of times, or a need for lower latency and cost from a small model. It is a poor way to add facts that change, which retrieval handles better. Continued pre-training on domain text is possible but rarely worth its cost. All forms need labelled data, an evaluation set and a way to serve and version the resulting model.

# Key considerations

- Build the evaluation set first. Without it you cannot tell whether tuning helped.
- Training data must be licensed and approved for this use. Personal data absorbed into weights is very hard to remove later.
- A tuned model is tied to its base model version. When the provider retires the base, you must retrain.
- Serving a custom model can cost more than shared endpoints unless traffic is steady. Check whether adapters can be served on shared capacity.
- Fine-tuning can weaken a model's safety behaviour. Repeat red-team testing after each tuning run.

# Questions to ask

- What do prompting and retrieval fail to achieve today, and how was that measured?
- How many high-quality examples exist, and who can label more?
- What call volume would justify a smaller specialised model?
- Do you hold the rights to use the training data for this purpose?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Generative AI](generative-ai.md) |
| Broader | [Generative AI](generative-ai.md) |
| Related | [Data labelling](../machine-learning/data-labelling.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Distributed training](../machine-learning/distributed-training.md), [Generative model serving](../mlops/generative-model-serving.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model registry](../machine-learning/model-registry.md), [Model training](../machine-learning/model-training.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md) |
| Depends on | [GPU and accelerated compute](../compute/gpu-compute.md), [Generative AI evaluation](genai-evaluation.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock custom models](../../technologies/aws/aws-bedrock-model-customization.md), [Amazon SageMaker HyperPod](../../technologies/aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker JumpStart](../../technologies/aws/aws-sagemaker-jumpstart.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure OpenAI in Foundry Models](../../technologies/microsoft/azure-openai.md), [Microsoft Foundry](../../technologies/microsoft/azure-foundry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Agent Studio](../../technologies/google-cloud/gcp-agent-studio.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex Fine-tuning](../../technologies/snowflake/snowflake-cortex-fine-tuning.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Runtime](../../technologies/databricks/databricks-ai-runtime.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../../technologies/cloudera/cloudera-ai-studios.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md), [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Scale Data Engine](../../technologies/independent/scale-data-engine.md), [Snorkel AI](../../technologies/independent/snorkel-ai.md) |
