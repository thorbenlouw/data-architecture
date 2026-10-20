---
type: Technology
id: oracle-oci-data-science
title: OCI Data Science
description: Managed ML platform on OCI with JupyterLab notebook sessions, jobs, pipelines, a model catalogue, model deployment endpoints and AI Quick Actions for fine-tuning and evaluating foundation models.
aliases: [Oracle Cloud Infrastructure Data Science]
platform: platform-oracle
kind: managed-service
availability: ga
realises:
- notebooks
- model-training
- model-registry
- real-time-inference
- ml-pipelines
- runtime-management
- model-customisation
- feature-store
resource: https://docs.oracle.com/en-us/iaas/data-science/using/data-science.htm
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Conda environments define the libraries that notebook sessions, jobs and model deployments run on, and can be published and shared. Related tools include the ADS SDK, AutoMLx, a Feature Store and ML Monitoring. Notebooks can run Spark on OCI Data Flow. Model artefacts are limited to 6 GB in the catalogue.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development): Train models on platform data at the scale required, from single machines to GPU clusters.
- [Model registry](../../capabilities/machine-learning/model-registry.md) (Machine learning development): Version, document and manage the lifecycle of trained models from candidate to production.
- [Real-time inference](../../capabilities/mlops/real-time-inference.md) (ML operations): Serve predictions through low-latency endpoints.
- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
- [Model customisation](../../capabilities/generative-ai/model-customisation.md) (Generative AI): Adapt foundation models to a domain through fine-tuning, distillation or further training.
- [Feature store](../../capabilities/machine-learning/feature-store.md) (Machine learning development): Manage features centrally so they are reused, documented and served consistently for training and inference.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Model customisation](../../capabilities/generative-ai/model-customisation.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Real-time inference](../../capabilities/mlops/real-time-inference.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya Workbench](../sas/sas-viya-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Kubeflow](../open-source/kubeflow.md), [marimo](../open-source/marimo.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md), [Model registry](../../capabilities/machine-learning/model-registry.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
