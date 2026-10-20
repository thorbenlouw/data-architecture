---
type: Technology
id: databricks-ai-runtime
title: Databricks AI Runtime
description: Serverless GPU compute for deep learning, used to train and fine-tune models on one or many GPUs with PyTorch DDP and FSDP, DeepSpeed or Ray.
formerly: [Serverless GPU compute]
platform: platform-databricks
kind: managed-service
availability: preview
realises: [gpu-compute, distributed-training, model-customisation]
resource: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Single-node use is in Public Preview and distributed training is still in Beta. The Databricks AI Runtime SDK (databricks-sdk-air) replaces the serverless_gpu package from environment version 6. AI Runtime is also the recommended replacement for Foundation Model Fine-tuning (formerly Mosaic AI Model Training), which has reached end of life.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute) (primary): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview  
**Product family:** Agent Bricks, Databricks Machine Learning, Databricks compute

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker HyperPod](../aws/aws-sagemaker-hyperpod.md), [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud TPU](../google-cloud/gcp-cloud-tpu.md), [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md), [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowpark Container Services](../snowflake/snowflake-snowpark-container-services.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Inference service](../cloudera/cloudera-ai-inference-service.md), [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md), [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md), [Teradata Factory](../teradata/teradata-factory.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya Workbench](../sas/sas-viya-workbench.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Ray](../open-source/ray.md), [vLLM](../open-source/vllm.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
