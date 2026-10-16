---
type: Technology
id: aws-sagemaker-unified-studio
title: Amazon SageMaker Unified Studio
description: Browser-based workbench that brings SQL querying, notebooks, visual ETL, workflows, ML and Bedrock tools together in domains and projects with shared permissions.
platform: platform-aws
kind: managed-service
availability: ga
realises:
- notebooks
- ad-hoc-analysis
- multi-tenancy
- self-service-provisioning
- version-control
- analytical-sandboxes
resource: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Domains authenticate through IAM Identity Center or IAM; projects created from project profiles provision compute and catalogue permissions. Serverless notebooks run on Athena for Apache Spark by default and can switch to EMR Serverless or Glue; they mix SQL, Python and charts and can be scheduled. Git integration and a query editor are included.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps) (primary): Develop interactively with code, results and narrative together, with collaboration and scheduling.
- [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) (Analytics and BI): Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions.
- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) (Platform operations): Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [Analytical sandboxes](../../capabilities/analytics-bi/analytical-sandboxes.md) (Analytics and BI): Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric notebooks](../microsoft/fabric-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Agent Platform Workbench](../google-cloud/gcp-agent-platform-workbench.md), [Colab Enterprise](../google-cloud/gcp-colab-enterprise.md), [BigQuery Studio](../google-cloud/gcp-bigquery-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Notebooks in Workspaces](../snowflake/snowflake-notebooks.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks notebooks](../databricks/databricks-notebooks.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Science](../oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata AI Studio](../teradata/teradata-ai-studio.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.ai](../ibm/ibm-watsonx-ai.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Workspaces](../palantir/palantir-code-workspaces.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../open-source/jupyter.md), [marimo](../open-source/marimo.md), [Kubeflow](../open-source/kubeflow.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Hex](../independent/hex.md), [ThoughtSpot Analyst Studio](../independent/thoughtspot-analyst-studio.md) | [Ad hoc analysis](../../capabilities/analytics-bi/ad-hoc-analysis.md), [Notebooks](../../capabilities/development-lifecycle/notebooks.md) |
