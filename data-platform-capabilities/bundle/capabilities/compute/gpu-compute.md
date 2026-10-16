---
type: Capability
id: gpu-compute
title: GPU and accelerated compute
description: Use GPUs or other accelerators for model training, inference and accelerated data processing.
broader: [compute-options]
related: [model-training, distributed-training, real-time-inference, model-customisation, object-file-access]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GPUs carry out thousands of simple arithmetic operations in parallel, which suits the matrix maths of neural networks and also columnar operations such as filtering, joining and sorting. Platforms offer GPU instances for notebooks and training clusters, managed endpoints for model inference, and GPU libraries that run DataFrame or Spark operations without code changes. Other accelerators, such as TPUs and dedicated inference chips, play similar roles. Fine-tuning a model that would take days on CPUs can take hours on a few GPUs.

GPUs are needed to train and serve deep learning and large language models, and they can speed up some data processing. They are scarce and expensive, so availability, scheduling and utilisation matter more than for ordinary compute. Not every job benefits. GPUs speed up dense numeric work but do little for jobs limited by reading data or full of branching logic, and moving data on and off the device can cancel the gain for small datasets.

# Key considerations

- GPU capacity can be hard to get on demand in some regions. Check quotas and regions, and whether planned training needs reserved capacity.
- Measure utilisation. GPUs left idle or waiting for data to load from storage are a common and expensive waste.
- Sharing GPUs through partitioning or time-slicing raises utilisation for inference and experiments.
- Driver, CUDA and framework versions must match. Use managed images and pin versions.

# Questions to ask

- Which workloads need GPUs: training, fine-tuning, inference or data processing?
- How large are the models, and how much GPU memory do they need?
- Is demand steady enough to justify reserved GPU capacity?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md) |
| Related | [Machine learning development](../machine-learning/machine-learning.md), [Audio and video processing](../specialised-data/audio-video-processing.md), [Distributed training](../machine-learning/distributed-training.md), [Embedding generation](../generative-ai/embedding-generation.md), [File-system access to object storage](../storage/object-file-access.md), [Foundation model access](../generative-ai/foundation-model-access.md), [Generative model serving](../mlops/generative-model-serving.md), [Model customisation](../generative-ai/model-customisation.md), [Model training](../machine-learning/model-training.md), [Real-time inference](../mlops/real-time-inference.md), [Reserved and committed capacity](reserved-capacity.md), [Sustainability and carbon management](../platform-operations/sustainability-reporting.md), [Vectorised native execution](native-execution-acceleration.md) |
| Needed by | [Generative model serving](../mlops/generative-model-serving.md), [Model customisation](../generative-ai/model-customisation.md) |

# Where it appears

- **Use cases:** [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md) · [ML engineer](../../personas/persona-ml-engineer.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md), [Amazon SageMaker HyperPod](../../technologies/aws/aws-sagemaker-hyperpod.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md), [Agent Platform Workbench](../../technologies/google-cloud/gcp-agent-platform-workbench.md), [Cloud TPU](../../technologies/google-cloud/gcp-cloud-tpu.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Container Runtime for ML](../../technologies/snowflake/snowflake-container-runtime.md), [Snowpark Container Services](../../technologies/snowflake/snowflake-snowpark-container-services.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Runtime](../../technologies/databricks/databricks-ai-runtime.md) (preview), [Databricks Model Serving](../../technologies/databricks/databricks-model-serving.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Inference service](../../technologies/cloudera/cloudera-ai-inference-service.md), [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md), [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Elastic Python Compute](../../technologies/teradata/teradata-elastic-python-compute.md), [Teradata Factory](../../technologies/teradata/teradata-factory.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Ray](../../technologies/open-source/ray.md), [vLLM](../../technologies/open-source/vllm.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md) |
