---
type: Technology
id: ray
title: Ray
description: Distributed compute framework for Python, with libraries for data processing (Ray Data), training (Ray Train), tuning (Ray Tune) and model serving (Ray Serve).
aliases: [Ray Data, Ray Serve, Ray Train, Ray Tune, RLlib]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- distributed-training
- gpu-compute
- hyperparameter-tuning
- batch-inference
- real-time-inference
- generative-model-serving
resource: https://www.ray.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Ray moved to the PyTorch Foundation (Linux Foundation) in 2025; Anyscale is the main commercial backer. Widely used for GPU-heavy AI workloads such as batch inference over unstructured data, LLM fine-tuning and reinforcement learning (RLlib).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development) (primary): Split training across many machines or GPUs to handle large models or datasets.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [Batch inference](../../capabilities/mlops/batch-inference.md) (ML operations): Score large datasets with a model on a schedule.
- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations): Serve predictions through low-latency endpoints.
- [Generative model serving](../../capabilities/mlops/generative-model-serving.md) (ML operations): Host open-weight or fine-tuned language and multimodal models on dedicated accelerators, tuned for token throughput, response latency and cost.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker HyperPod](../aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md), [Cloud TPU](../google-cloud/gcp-cloud-tpu.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Runtime](../databricks/databricks-ai-runtime.md) (preview), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md), [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Generative model serving](../../capabilities/mlops/generative-model-serving.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Batch inference](../../capabilities/mlops/batch-inference.md), [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
