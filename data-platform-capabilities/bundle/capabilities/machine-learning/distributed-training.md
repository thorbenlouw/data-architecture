---
type: Capability
id: distributed-training
title: Distributed training
description: Split training across many machines or GPUs to handle large models or datasets.
broader: [model-training]
related: [gpu-compute, distributed-processing, reserved-capacity, model-customisation]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The most common approach is data parallelism: every worker holds a full copy of the model, trains on its own slice of each batch, and the workers average their gradients after every step. When a model is too large for one GPU's memory, model parallelism splits the model itself, either layers across devices (pipeline parallelism) or the maths inside each layer across devices (tensor parallelism). Sharded methods spread parameters, gradients and optimiser state across workers to save memory.

It is needed when one machine would take too long or cannot hold the model. Speed-up is rarely linear, because workers spend time exchanging gradients, so the links between GPUs and between machines matter as much as GPU count. Most tabular models do not need it, although distributed gradient boosting helps with very large datasets. It differs from distributed data processing, though both may share a cluster, and from hyperparameter tuning, which runs many independent trainings side by side rather than one training across many machines.

# Key considerations

- Bandwidth between GPUs and between nodes often limits scaling. Check the interconnect, not only GPU type and count.
- Long jobs on many machines will meet hardware failures. Checkpoint regularly and use a launcher that can resume.
- Start with one machine with several GPUs. Multi-node training adds operational work that many workloads do not need.
- Larger effective batch sizes from many workers change training behaviour and may need learning-rate changes.

# Questions to ask

- Does any planned model exceed one GPU's memory or take more than a day to train on one machine?
- Is accelerator capacity available in the regions where the data must stay?
- Who will run multi-node GPU jobs and deal with failures?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Model training](model-training.md) |
| Related | [Distributed processing](../processing/distributed-processing.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model customisation](../generative-ai/model-customisation.md), [Reserved and committed capacity](../compute/reserved-capacity.md) |

# Where it appears

- **Use cases:** [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md), [Amazon SageMaker HyperPod](../../technologies/aws/aws-sagemaker-hyperpod.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md), [Cloud TPU](../../technologies/google-cloud/gcp-cloud-tpu.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Container Runtime for ML](../../technologies/snowflake/snowflake-container-runtime.md), [Snowflake ML Jobs](../../technologies/snowflake/snowflake-ml-jobs.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Runtime](../../technologies/databricks/databricks-ai-runtime.md) (preview), [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Elastic Python Compute](../../technologies/teradata/teradata-elastic-python-compute.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Kubeflow](../../technologies/open-source/kubeflow.md), [Ray](../../technologies/open-source/ray.md) |
