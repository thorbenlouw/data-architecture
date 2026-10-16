---
type: Technology
id: aws-sagemaker-studio
title: Amazon SageMaker Studio
description: Web-based ML development environment in SageMaker AI offering JupyterLab, Code Editor and RStudio spaces with managed compute.
platform: platform-aws
kind: feature
availability: ga
realises: [notebooks, local-development, version-control]
resource: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Distinct from SageMaker Unified Studio, which targets combined data and AI work. Studio Classic is the legacy interface; SageMaker Studio Lab is closed to new customers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [IDE and local development](../../capabilities/development-lifecycle/local-development.md) (Development and DataOps): Develop in your own editor and run against the platform, with debugging and local tests.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker AI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md), [Snowsight Workspaces](../snowflake/snowflake-workspaces.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [IDE and local development](../../capabilities/development-lifecycle/local-development.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [marimo](../open-source/marimo.md), [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [Kubeflow](../open-source/kubeflow.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
