---
type: Capability
id: notebooks
title: Notebooks
description: Develop interactively with code, results and narrative together, with collaboration and scheduling.
broader: [development-lifecycle]
related: [local-development, version-control, ad-hoc-analysis, experiment-tracking, data-applications]
depends_on: [compute-options]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A notebook is a document made of cells. Each cell holds code, such as SQL, Python, Scala or R, or text, and the output of running it (a table, a chart or an error) appears directly below. Cells run against a live session on platform compute, so an analyst can load a table, plot a distribution, change the code and rerun in seconds. Platform notebooks add shared editing, comments, version history, parameters and scheduling, so the same notebook can also run as a nightly job. Jupyter's `.ipynb` format is the common file format.

Notebooks suit exploration, data science, prototyping and explaining an analysis to others. They are weak as production code: cells run out of order leave hidden state, outputs are saved inside the file, and logic is hard to unit test or reuse. Many teams move stable logic into modules or pipelines and call it from the notebook. Compared with IDE development, notebooks trade structure for fast feedback.

# Key considerations

- Check how notebooks are stored. Formats that save outputs and metadata as JSON give noisy diffs and can leak data into Git; plain-source formats are easier to review.
- A scheduled notebook is a production job. It needs an owner, a service identity, parameters, alerting and the same promotion route as other code.
- Interactive sessions left running are a common source of waste. Set auto-termination and size limits on notebook compute.
- Decide whether data shown in outputs follows the same masking and retention rules as the source tables, especially when notebooks are shared or exported.

# Questions to ask

- Who uses notebooks: data scientists exploring, analysts reporting, or engineers building production jobs?
- Do scheduled notebooks run in production today, and who supports them when they fail?
- Must notebooks be reviewed and versioned in Git like other code?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [Machine learning development](../machine-learning/machine-learning.md), [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Data application hosting](data-applications.md), [DataFrame APIs](../processing/dataframe-apis.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [IDE and local development](local-development.md), [Version control integration](version-control.md) |
| Depends on | [Compute provisioning options](../compute/compute-options.md) |

# Where it appears

- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 0 – Manual process · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 0 – No MLOps

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker Unified Studio notebooks | [Amazon Athena for Apache Spark](../../technologies/aws/aws-athena-spark.md), [Amazon SageMaker Studio](../../technologies/aws/aws-sagemaker-studio.md), [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric notebooks](../../technologies/microsoft/fabric-notebooks.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Agent Platform Workbench](../../technologies/google-cloud/gcp-agent-platform-workbench.md), [BigQuery Studio](../../technologies/google-cloud/gcp-bigquery-studio.md), [Colab Enterprise](../../technologies/google-cloud/gcp-colab-enterprise.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Notebooks in Workspaces | [Snowflake Notebooks in Workspaces](../../technologies/snowflake/snowflake-notebooks.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Free Edition](../../technologies/databricks/databricks-free-edition.md), [Databricks notebooks](../../technologies/databricks/databricks-notebooks.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera AI Workbench](../../technologies/cloudera/cloudera-ai-workbench.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Science](../../technologies/oracle/oracle-oci-data-science.md), [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Databricks](../../technologies/sap/sap-databricks.md) (distribution of Databricks) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata AI Studio](../../technologies/teradata/teradata-ai-studio.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.ai](../../technologies/ibm/ibm-watsonx-ai.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Workspaces](../../technologies/palantir/palantir-code-workspaces.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Viya Workbench](../../technologies/sas/sas-viya-workbench.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku code recipes and notebooks](../../technologies/dataiku/dataiku-code-recipes-notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Kubeflow](../../technologies/open-source/kubeflow.md), [marimo](../../technologies/open-source/marimo.md), [Project Jupyter (JupyterLab, Notebook, JupyterHub)](../../technologies/open-source/jupyter.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Hex](../../technologies/independent/hex.md), [ThoughtSpot Analyst Studio](../../technologies/independent/thoughtspot-analyst-studio.md) |
