---
type: Technology
id: databricks-model-serving
title: Databricks Model Serving
description: Serverless CPU and GPU endpoints for serving custom MLflow models, Databricks-hosted foundation models and external models in real time, with traffic splitting between model versions.
formerly: [Mosaic AI Model Serving]
platform: platform-databricks
kind: managed-service
availability: ga
realises: [real-time-inference, canary-ab-testing, gpu-compute, generative-model-serving]
resource: https://docs.databricks.com/aws/en/machine-learning/model-serving/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agents deployed on Model Serving are now legacy, and new agents should use Agent Runtime on Databricks Apps. Endpoint telemetry and inference tables are configured in the endpoint's Unity Gateway settings. Shadow deployment is not a built-in mode.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Agent Bricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI inference](../aws/aws-sagemaker-inference.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
