---
type: Technology
id: dataiku-code-recipes-notebooks
title: Dataiku code recipes and notebooks
description: Python, R, SQL, Hive, Impala, PySpark, SparkR, SparkSQL, Spark Scala and shell recipes and Jupyter and SQL notebooks that run inside the Flow alongside visual recipes.
platform: platform-dataiku
kind: feature
availability: ga
realises: [notebooks, sql-transformation, distributed-processing]
resource: https://doc.dataiku.com/dss/latest/code-recipes/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Code recipes read and write Flow datasets through the Dataiku APIs, so lineage, scheduling and permissions apply as for visual recipes. Notebooks can run in containers, and SQL notebooks can draw charts since version 14.3.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon SageMaker Studio](../aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../aws/aws-sagemaker-unified-studio.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya Workbench](../sas/sas-viya-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [marimo](../open-source/marimo.md), [Kubeflow](../open-source/kubeflow.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
