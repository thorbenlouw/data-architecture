---
type: Technology
id: cloudera-ai-workbench
title: Cloudera AI Workbench
description: Containerised data science environment with projects, sessions in Jupyter or other editors, experiments, jobs, model endpoints and hosted applications on CPUs or GPUs.
formerly: [Cloudera Machine Learning workspaces]
platform: platform-cloudera
kind: managed-service
availability: ga
realises: [notebooks, model-training, experiment-tracking, data-applications, gpu-compute, runtime-management]
resource: https://docs.cloudera.com/machine-learning/cloud/administrator.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Successor to the standalone Cloudera Data Science Workbench (CDSW), which is still met on older clusters. Cloudera AI, formerly Cloudera Machine Learning (CML), now consists of AI Workbench, AI Registry and the AI Inference service. Experiments are tracked with [MLflow](../open-source/mlflow.md). Model deployment from the workbench is labelled legacy in the docs; the AI Inference service is the main serving path. An open-source MCP server lets agents drive workbench tasks.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [marimo](../open-source/marimo.md), [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Kubeflow](../open-source/kubeflow.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md), [Domino Enterprise AI Platform](../independent/domino-enterprise-ai-platform.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md), [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) |
