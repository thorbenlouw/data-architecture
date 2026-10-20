---
type: Technology
id: databricks-unity-catalog-lineage
title: Unity Catalog data lineage
description: Captures table- and column-level lineage automatically for queries, notebooks, jobs, pipelines, dashboards and models. External sources and BI tools can be registered so they appear in the same graph.
platform: platform-databricks
kind: feature
availability: ga
realises: [table-lineage, column-lineage, model-lineage, cross-system-lineage, impact-analysis]
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lineage is queryable in system.access.table_lineage and column_lineage for a rolling year. It is lost on renames and path-based access. Lineage also drives tag propagation (Beta) and root-cause analysis in anomaly detection.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery) (primary): Track dependencies between datasets, tables and views.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md), [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Data Lineage](../dataiku/dataiku-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Marquez](../open-source/marquez.md), [Apache Atlas](../open-source/apache-atlas.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
