---
type: Technology
id: cloudera-ai-inference-service
title: Cloudera AI Inference service
description: Kubernetes-based serving for predictive models and large language models, using NVIDIA NIM and Triton, with REST endpoints, monitoring and canary rollouts.
aliases: [Cloudera AI Inference]
platform: platform-cloudera
kind: managed-service
availability: ga
realises:
- real-time-inference
- foundation-model-access
- canary-ab-testing
- gpu-compute
- generative-model-serving
resource: https://docs.cloudera.com/machine-learning/cloud/ai-inference/topics/ml-caii-key-features.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lets organisations host open LLMs and embedding models inside their own boundary, on cloud or on premises, rather than call public APIs. Endpoints are governed by fine-grained access control and a management API suited to CI/CD.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md) (Generative AI): Use hosted large language and multimodal models through managed APIs inside the platform's security boundary.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md), [Model Garden](../google-cloud/gcp-model-garden.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Foundation model access](../../capabilities/generative-ai/foundation-model-access.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
