---
type: Technology
id: gcp-knowledge-catalog-data-lineage
title: Knowledge Catalog data lineage
description: Records table- and column-level lineage automatically for BigQuery, Managed Service for Apache Spark, Managed Airflow and Dataflow, and accepts OpenLineage events from other systems.
formerly: [Dataplex data lineage]
platform: platform-google-cloud
kind: feature
availability: ga
realises: [table-lineage, column-lineage, cross-system-lineage, impact-analysis, metadata-interoperability]
resource: https://docs.cloud.google.com/dataplex/docs/about-data-lineage
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exposed through the Data Lineage API. Column-level lineage for Spark went GA in May 2026, and lineage ingestion can be switched on or off by organisation, folder or project. A lineage MCP server is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery) (primary): Track dependencies between datasets, tables and views.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Knowledge Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md), [Snowflake external lineage](../snowflake/snowflake-external-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md), [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Lineage](../dataiku/dataiku-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Marquez](../open-source/marquez.md), [Apache Atlas](../open-source/apache-atlas.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
