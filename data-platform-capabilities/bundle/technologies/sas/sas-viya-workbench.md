---
type: Technology
id: sas-viya-workbench
title: SAS Viya Workbench
description: Self-service cloud development environment in which data scientists code in SAS, Python or R through Jupyter, Visual Studio Code or SAS Enterprise Guide on CPU or GPU compute that scales and stops on demand.
platform: platform-sas
kind: managed-service
availability: ga
realises: [notebooks, gpu-compute]
resource: https://www.sas.com/en_us/software/viya/workbench.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

SAS announced general availability in April 2024, first through AWS Marketplace; it is now sold directly on Microsoft Marketplace and through private offers on AWS Marketplace. Sessions are single-user, stop themselves when idle and resume where the user left off. SAS Viya Workbench for Learners is a free version for academic use.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md) (Query and compute): Use GPUs or other accelerators for model training, inference and accelerated data processing.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [GPU and accelerated compute](../../capabilities/compute/gpu-compute.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [marimo](../open-source/marimo.md), [Kubeflow](../open-source/kubeflow.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
