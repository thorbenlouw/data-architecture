---
type: Technology
id: snowflake-container-runtime
title: Snowflake Container Runtime for ML
description: A prebuilt CPU and GPU ML environment on Snowpark Container Services, with distributed data loading, training and hyperparameter tuning built on Ray.
platform: platform-snowflake
kind: feature
availability: ga
realises: [model-training, distributed-training, hyperparameter-tuning, gpu-compute, runtime-management]
resource: https://docs.snowflake.com/en/developer-guide/snowflake-ml/container-runtime-ml
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used by Notebooks in Workspaces and ML Jobs. Custom runtime images are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development) (primary): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake ML

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md), [Cloud TPU](../google-cloud/gcp-cloud-tpu.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
