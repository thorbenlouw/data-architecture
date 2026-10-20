---
type: Capability
id: generative-model-serving
title: Generative model serving
description: Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
aliases: [LLM serving, LLM inference, open-weight model hosting, self-hosted LLMs]
broader: [model-deployment, foundation-model-access]
related: [gpu-compute, real-time-inference, model-customisation, reserved-capacity, ai-gateway]
depends_on: [gpu-compute]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Serving a generative model differs from serving a classifier. Each request produces output a token at a time, so the serving engine streams responses, batches requests from many users continuously, keeps attention state cached in GPU memory and can load many small fine-tuned adapters onto one base model. Teams track time to first token, tokens per second and cost per million tokens. For example, an insurer runs an open-weight model in its own cloud account for claim notes that may not leave it, quantised to fit two GPUs and serving a separate adapter for each document type.

It is chosen when data terms rule out provider endpoints, when a fine-tuned or distilled model must be served, or when steady high volume makes dedicated capacity cheaper than paying per token. The price is running GPUs, capacity planning, engine and weight upgrades, and on-call support. Foundation model access covers calling models someone else runs; this capability covers running them yourself.

# Key considerations

- Compare total cost, not list prices. Dedicated GPUs cost money while idle, so per-token endpoints are often cheaper until load is steady and high.
- Quantisation and smaller models cut memory and cost but change output quality. Rerun the evaluation suite on the exact serving configuration.
- Large weights make cold starts take minutes. Keep warm capacity for interactive use and scale to zero only for batch work.
- Check the model licence for commercial use, user thresholds and acceptable-use terms, and record the source and version of the weights.
- Expose the same interface that applications and the AI gateway already call, so models can be swapped without code changes.

# Questions to ask

- Which data or contract terms rule out provider-hosted endpoints?
- What daily token volume and peak concurrency are expected, and how steady are they?
- Which targets apply: time to first token, full response time, or batch completion?
- Who will patch serving engines and upgrade model weights?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model deployment](model-deployment.md), [Foundation model access](../generative-ai/foundation-model-access.md) |
| Related | [AI gateway](../generative-ai/ai-gateway.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model customisation](../generative-ai/model-customisation.md), [Real-time inference](real-time-inference.md), [Reserved and committed capacity](../compute/reserved-capacity.md) |
| Depends on | [GPU and accelerated compute](../compute/gpu-compute.md) |

# Where it appears

- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [Generative AI](../../maturity/track-genai.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI inference](../../technologies/aws/aws-sagemaker-inference.md), [Amazon SageMaker JumpStart](../../technologies/aws/aws-sagemaker-jumpstart.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Model Garden](../../technologies/google-cloud/gcp-model-garden.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Model Serving](../../technologies/databricks/databricks-model-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Inference service](../../technologies/cloudera/cloudera-ai-inference-service.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Generative AI (OCI Enterprise AI)](../../technologies/oracle/oracle-oci-generative-ai.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Agentic AI Accelerator](../../technologies/sas/sas-agentic-ai-accelerator.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [KServe](../../technologies/open-source/kserve.md), [Ray](../../technologies/open-source/ray.md), [vLLM](../../technologies/open-source/vllm.md) |
