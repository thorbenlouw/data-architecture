---
type: Technology
id: sas-data-and-ai-studio
title: SAS Data and AI Studio
description: Browser-based development environment in SAS Viya for writing SAS and Python code and building visual flows that extract, transform and load data and run analytics.
aliases: [SAS Data and AI Studio Advanced, SAS Data and AI Studio Enterprise, SAS Studio flows]
formerly: [SAS Studio, SAS Studio Analyst, SAS Studio Engineer]
platform: platform-sas
kind: feature
availability: ga
realises: [low-code-transformation, sql-transformation, version-control]
resource: https://www.sas.com/en_us/software/data-and-ai-studio.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Renamed from SAS Studio with the 2026.06 release, with no change to licensing, deployment or supported workflows; the Advanced tier replaces SAS Studio Analyst and the Enterprise tier replaces SAS Studio Engineer. Flows can run transformations inside the source database (ELT) or on SAS servers, and custom steps can be built visually and shared. Git integration tracks code and flows, and pipelines can be scheduled and monitored with Apache Airflow through the SAS Provider for Airflow.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration SQL ELT mode](../informatica/informatica-cdi-sql-elt-mode.md), [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
