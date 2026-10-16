---
type: Capability
id: real-time-inference
title: Real-time inference
description: Serve predictions through low-latency endpoints.
aliases: [model serving, online inference, endpoints]
broader: [model-deployment]
related: [online-feature-store, low-latency-serving, gpu-compute, elastic-scaling, container-services]
tags: [mlops]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A payment service sends transaction details to a model endpoint. The endpoint fetches recent features for the card from an online store, runs the model and returns a fraud score before the payment is approved, all within tens of milliseconds. Around the model, the serving layer validates requests, adds and removes replicas as load changes, groups requests into batches on GPUs, and routes traffic between model versions.

It is needed when the prediction depends on information that exists only at request time, or must shape an interaction as it happens: recommendations on page load, fraud checks, dynamic pricing. It costs more than batch, because capacity must be kept warm for peak load, and it brings application concerns such as availability targets, tail latency, endpoint security and on-call support. Serving that scales to zero saves money for rarely used models but adds a cold-start delay to the first request.

# Key considerations

- Budget latency end to end. Network, feature lookup, preprocessing and model execution all count against the caller's timeout.
- Define what the caller does if the endpoint is slow or down, such as a default score or a rule-based fallback.
- Autoscaling must react faster than traffic spikes. Keep a minimum number of replicas for latency-sensitive endpoints.
- Large models may need GPUs, quantisation or request batching to meet latency at acceptable cost.

# Questions to ask

- What 99th-percentile latency and request rate must the endpoint support?
- What should happen to the business process if a prediction is unavailable?
- Does the prediction need information that only exists at request time?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [ML operations](mlops.md) |
| Broader | [Model deployment](model-deployment.md) |
| Related | [Canary and A/B testing](canary-ab-testing.md), [Container services](../compute/container-services.md), [Decision management](../serving/decision-management.md), [Elastic scaling](../compute/elastic-scaling.md), [Foundation model access](../generative-ai/foundation-model-access.md), [Generative model serving](generative-model-serving.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Low-latency serving](../serving/low-latency-serving.md), [Online feature store](../machine-learning/online-feature-store.md), [Shadow deployment](shadow-deployment.md), [Streaming inference](streaming-inference.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (benefits from) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 3) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [ML engineer](../../personas/persona-ml-engineer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [MLOps](../../maturity/track-mlops.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI inference](../../technologies/aws/aws-sagemaker-inference.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning online and batch endpoints](../../technologies/microsoft/azure-ml-endpoints.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Endpoints](../../technologies/google-cloud/gcp-agent-platform-endpoints.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Model Serving in Snowpark Container Services](../../technologies/snowflake/snowflake-model-serving.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Model Serving](../../technologies/databricks/databricks-model-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Inference service](../../technologies/cloudera/cloudera-ai-inference-service.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [KServe](../../technologies/open-source/kserve.md), [Ray](../../technologies/open-source/ray.md), [vLLM](../../technologies/open-source/vllm.md) |
