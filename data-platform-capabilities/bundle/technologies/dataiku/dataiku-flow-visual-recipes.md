---
type: Technology
id: dataiku-flow-visual-recipes
title: Dataiku Flow and visual recipes
description: Visual pipeline of datasets and recipes, in which the Prepare recipe and recipes such as join, group, window, pivot and fuzzy join transform data without code and can run in the underlying database or Spark.
aliases: [Prepare recipe, Flow]
platform: platform-dataiku
kind: feature
availability: ga
realises: [low-code-transformation, data-preparation, data-cleansing, incremental-processing]
resource: https://doc.dataiku.com/dss/latest/visual-recipes/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

The Prepare recipe offers a large library of processors for cleaning, parsing, enriching and reshaping data, and shows the effect on a sample as each step is added. Visual recipes run on the Dataiku engine, on Spark, or as SQL in the database when input and output share a compatible connection. Partitioned datasets let recipes build only selected partitions, such as the latest day. Flow zones, the Flow Document Generator (a Word export of the Flow) and AI Explain help large projects stay readable.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.
- [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md) (Data quality and observability): Correct and standardise data values such as addresses, names, dates and codes.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Data cleansing and standardisation](../../capabilities/data-quality/data-cleansing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
