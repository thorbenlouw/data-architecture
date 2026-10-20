---
type: Technology
id: fabric-dataflow-gen2
title: Fabric Dataflow Gen2
description: Low-code data preparation using Power Query, with hundreds of connectors and output to lakehouses, warehouses and other destinations.
aliases: [Dataflow Gen2]
platform: platform-microsoft
kind: feature
availability: ga
realises: [low-code-transformation, data-preparation, saas-connectors, incremental-processing]
resource: https://learn.microsoft.com/en-us/fabric/data-factory/dataflows-gen2-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Successor to Power BI dataflows (Gen1). Since April 2026 all new items have Git and CI/CD support. Consumes capacity units heavily for large volumes; pipelines with Copy job or notebooks are usually cheaper at scale.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation) (primary): Build transformation logic visually from configurable components rather than writing code.
- [Self-service data preparation](../../capabilities/processing/data-preparation.md) (Processing and transformation): Let analysts profile, clean and reshape data interactively without engineering help.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Factory

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue ETL](../aws/aws-glue-etl.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [BigQuery data preparation](../google-cloud/gcp-bigquery-data-preparation.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Designer](../databricks/databricks-lakeflow-designer.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md), [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Pipeline Builder](../palantir/palantir-pipeline-builder.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data and AI Studio](../sas/sas-data-and-ai-studio.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Flow and visual recipes](../dataiku/dataiku-flow-visual-recipes.md) | [Incremental processing](../../capabilities/processing/incremental-processing.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Coalesce Transform](../independent/coalesce-transform.md), [Alteryx One](../independent/alteryx-one.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [Self-service data preparation](../../capabilities/processing/data-preparation.md) |
