---
type: Technology
id: gcp-cloud-tpu
title: Cloud TPU
description: Google's tensor processing unit accelerators, offered as VMs, slices and pods for training and serving large models.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [gpu-compute, distributed-training]
resource: https://docs.cloud.google.com/tpu/docs/intro-to-tpu
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used directly, through GKE or through Agent Platform training and endpoints; GPUs are offered in parallel on Compute Engine.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute) (primary): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker HyperPod](../aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowpark Container Services](../snowflake/snowflake-snowpark-container-services.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Runtime](../databricks/databricks-ai-runtime.md) (preview), [Databricks Model Serving](../databricks/databricks-model-serving.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md), [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md), [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md), [Teradata Factory](../teradata/teradata-factory.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Ray](../open-source/ray.md), [vLLM](../open-source/vllm.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
