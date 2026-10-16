---
type: Technology
id: aws-sagemaker-inference
title: Amazon SageMaker AI inference
description: Model hosting options covering real-time, serverless and asynchronous endpoints and batch transform jobs, with traffic-shifting deployment controls.
aliases: [SageMaker AI endpoints, SageMaker batch transform]
platform: platform-aws
kind: feature
availability: ga
realises:
- real-time-inference
- batch-inference
- canary-ab-testing
- shadow-deployment
- generative-model-serving
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Production variants enable A/B tests; deployment guardrails do blue/green, canary and linear shifts; shadow tests mirror traffic to a candidate. Inference components pack several models per endpoint, and Inference Recommender benchmarks instance choices.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations) (primary): Serve predictions through low-latency endpoints.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md) (ML operations): Route a share of live traffic to a new model and compare outcomes before full rollout.
- [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) (ML operations): Run a new model on live traffic without acting on its outputs, to compare it with the production model.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning online and batch endpoints](../microsoft/azure-ml-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Endpoints](../google-cloud/gcp-agent-platform-endpoints.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Model Serving in Snowpark Container Services](../snowflake/snowflake-model-serving.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Shadow deployment](../../capabilities/mlops/shadow-deployment.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [KServe](../open-source/kserve.md), [vLLM](../open-source/vllm.md), [Ray](../open-source/ray.md) | [Canary and A/B testing](../../capabilities/mlops/canary-ab-testing.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md), [Batch inference](../../capabilities/mlops/batch-inference.md) |
