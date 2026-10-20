---
type: Technology
id: snowflake-notebooks
title: Snowflake Notebooks in Workspaces
description: Jupyter-compatible notebooks in Snowsight Workspaces that run on Container Runtime CPU or GPU compute, with Git integration, a terminal and scheduling.
platform: platform-snowflake
kind: feature
availability: ga
realises: [notebooks, model-training]
resource: https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The older warehouse-based notebooks were renamed Legacy Snowflake Notebooks in March 2026 and can be imported into Workspaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Model training](../../capabilities/machine-learning/model-training.md) (Machine learning development): Train models on platform data at the scale required, from single machines to GPU clusters.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowsight

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Model training](../../capabilities/machine-learning/model-training.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya Workbench](../sas/sas-viya-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [marimo](../open-source/marimo.md), [Kubeflow](../open-source/kubeflow.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
