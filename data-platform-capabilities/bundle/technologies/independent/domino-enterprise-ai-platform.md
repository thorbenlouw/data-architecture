---
type: Technology
id: domino-enterprise-ai-platform
title: Domino Enterprise AI Platform
description: Governed workbench for code-first data science that provides compute and GPUs across clouds and on premises, with experiment reproducibility, model deployment, governance and cost controls.
aliases: [Domino Data Lab, Domino]
platform: platform-independent
vendor: Domino Data Lab
kind: software
availability: ga
realises:
- model-training
- experiment-tracking
- model-deployment
- model-governance
- gpu-compute
- runtime-management
resource: https://domino.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Areas include AI infrastructure, data management, the AI workbench, MLOps, the Governance Center, FinOps and the App hub. Hybrid deployment across several clusters is a differentiator, and it is common in pharma and financial services.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development) (primary): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Model deployment](../../capabilities/mlops/model-deployment.md) (ML operations): Package and release models into production for batch, real-time or streaming use.
- [Model governance](../../capabilities/mlops/model-governance.md) (ML operations): Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker AI training jobs](../aws/aws-sagemaker-training.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data Science in Microsoft Fabric](../microsoft/fabric-data-science.md), [Azure Machine Learning](../microsoft/azure-machine-learning.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [Model training](../../capabilities/machine-learning/model-training.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Managed Training](../google-cloud/gcp-agent-platform-managed-training.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Container Runtime for ML](../snowflake/snowflake-container-runtime.md), [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md), [Snowpark-optimized warehouses](../snowflake/snowflake-snowpark-optimized-warehouses.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md) |
