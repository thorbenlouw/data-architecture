---
type: Technology
id: aws-sagemaker-hyperpod
title: Amazon SageMaker HyperPod
description: Persistent, self-healing accelerator clusters orchestrated by Slurm or Amazon EKS for large-scale model training, fine-tuning and inference.
platform: platform-aws
kind: feature
availability: ga
realises: [distributed-training, gpu-compute, model-customisation]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Replaces faulty nodes and resumes jobs automatically; task governance shares capacity between teams; recipes package common foundation-model training set-ups. Suited to multi-week runs on hundreds of GPUs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development) (primary): Split training across many machines or GPUs to handle large models or datasets.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud TPU](../google-cloud/gcp-cloud-tpu.md), [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowflake ML Jobs](../snowflake/snowflake-ml-jobs.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Runtime](../databricks/databricks-ai-runtime.md) (preview), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model customisation](../../capabilities/generative-ai/model-customisation.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Ray](../open-source/ray.md), [Kubeflow](../open-source/kubeflow.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
