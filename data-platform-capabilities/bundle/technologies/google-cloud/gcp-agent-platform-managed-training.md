---
type: Technology
id: gcp-agent-platform-managed-training
title: Agent Platform Managed Training
description: Runs custom training jobs in prebuilt or custom containers on CPUs, GPUs or TPUs, including multi-node distributed training and hyperparameter tuning.
formerly: [Vertex AI Training, Vertex AI custom training]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- model-training
- distributed-training
- hyperparameter-tuning
- gpu-compute
- reserved-capacity
- interruptible-compute
resource: https://docs.cloud.google.com/vertex-ai/docs/training/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Hyperparameter tuning uses the Vizier black-box optimisation service. Reserved training clusters are available for large accelerator workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development) (primary): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Distributed training](../../capabilities/machine-learning/distributed-training.md) (Machine learning development): Split training across many machines or GPUs to handle large models or datasets.
- [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md) (Machine learning development): Search automatically for the model settings that perform best.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.
- [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) (Query and compute): Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Gemini Enterprise Agent Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Machine Learning](../microsoft/azure-machine-learning.md), [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md) | [Distributed training](../../capabilities/machine-learning/distributed-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Hyperparameter tuning](../../capabilities/machine-learning/hyperparameter-tuning.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md) |
