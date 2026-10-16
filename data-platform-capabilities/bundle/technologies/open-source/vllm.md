---
type: Technology
id: vllm
title: vLLM
description: High-throughput inference and serving engine for large language models, with an OpenAI-compatible API.
platform: platform-open-source
kind: open-source
availability: ga
realises: [generative-model-serving, real-time-inference, gpu-compute, batch-inference]
resource: https://docs.vllm.ai/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, hosted by the PyTorch Foundation. The common way to self-host open-weight models; used inside KServe, Ray Serve and many commercial inference services.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations) (primary): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.
- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations): Serve predictions through low-latency endpoints.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md), [Amazon SageMaker JumpStart](../aws/aws-sagemaker-jumpstart.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Model Garden](../google-cloud/gcp-model-garden.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Generative AI (OCI Enterprise AI)](../oracle/oracle-oci-generative-ai.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
