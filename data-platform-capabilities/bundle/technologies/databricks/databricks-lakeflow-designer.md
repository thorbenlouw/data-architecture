---
type: Technology
id: databricks-lakeflow-designer
title: Lakeflow Designer
description: A visual, no-code canvas where analysts build data preparation flows from operators or natural-language prompts. The flows are backed by generated code governed in Unity Catalog.
platform: platform-databricks
kind: feature
availability: ga
realises: [low-code-transformation, data-preparation]
resource: https://docs.databricks.com/aws/en/designer/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA in June 2026 and enabled by default. Preps go to production through Git, Lakeflow Jobs and Declarative Automation Bundles. User-defined operators wrap Unity Catalog Python or SQL functions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Dataflow Gen2](../microsoft/fabric-dataflow-gen2.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
