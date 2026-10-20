---
type: Capability
id: model-training
title: Model training
description: Train models on platform data at the scale required, from single machines to GPU clusters.
broader: [machine-learning]
related: [gpu-compute, container-services, reserved-capacity, experiment-tracking, model-customisation]
tags: [machine-learning]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Training runs a learning algorithm over prepared data to fit a model's parameters. In practice that means choosing compute, loading a training set, running a framework such as scikit-learn, XGBoost or PyTorch, and saving the fitted model with its metrics. A gradient-boosted model on a few million rows may train in minutes on one large machine; an image model may need several GPUs for days.

For the platform, the questions are where training runs, how it reads data and how it is paid for. Options include clusters attached to notebooks, managed training jobs that start containers on demand and stop them afterwards, and training inside the database. Reading governed tables directly avoids copies but needs fast readers, since many frameworks expect local files or in-memory arrays. Training is bursty, heavy and tolerant of delay, while serving is constant and sensitive to latency, so the two usually run on separate compute.

# Key considerations

- Run training as jobs with pinned containers and dependencies, not only interactively, so it can be repeated and scheduled.
- GPU capacity can be scarce. Check quotas, queueing, and whether interruptible capacity with regular checkpoints is acceptable.
- Loading data from the lake is often the bottleneck. Test read throughput into training compute, not only compute speed.
- Fix random seeds and library versions where reproducibility matters, accepting that some GPU operations are not fully deterministic.

# Questions to ask

- Which model types and data sizes are expected, and do any need GPUs?
- Can training read governed data in place, or must it be extracted?
- How often will models be retrained, and how long may a training run take?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Machine learning development](machine-learning.md) |
| Broader | [Machine learning development](machine-learning.md) |
| Narrower | [AutoML](automl.md), [Distributed training](distributed-training.md), [Hyperparameter tuning](hyperparameter-tuning.md) |
| Related | [Container services](../compute/container-services.md), [Experiment tracking](experiment-tracking.md), [File-system access to object storage](../storage/object-file-access.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model customisation](../generative-ai/model-customisation.md), [Multimodal data formats](../storage/multimodal-data-formats.md), [Reserved and committed capacity](../compute/reserved-capacity.md), [Spot and interruptible compute](../compute/interruptible-compute.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 2) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 2)
- **Patterns:** [Feature, training and inference pipelines](../../patterns/fti-pipelines.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [ML development](../../maturity/track-ml-development.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 0 – Manual process · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 0 – No MLOps

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker AI training jobs](../../technologies/aws/aws-sagemaker-training.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Machine Learning](../../technologies/microsoft/azure-machine-learning.md), [Data Science in Microsoft Fabric](../../technologies/microsoft/fabric-data-science.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Managed Training](../../technologies/google-cloud/gcp-agent-platform-managed-training.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Container Runtime for ML](../../technologies/snowflake/snowflake-container-runtime.md), [Snowflake Notebooks in Workspaces](../../technologies/snowflake/snowflake-notebooks.md), [Snowpark-optimized warehouses](../../technologies/snowflake/snowflake-snowpark-optimized-warehouses.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Databricks](../../technologies/sap/sap-databricks.md) (distribution of Databricks) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Workspaces](../../technologies/palantir/palantir-code-workspaces.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Domino Enterprise AI Platform](../../technologies/independent/domino-enterprise-ai-platform.md) |

Narrower capabilities are realised by a further 28 technologies; see their pages.
