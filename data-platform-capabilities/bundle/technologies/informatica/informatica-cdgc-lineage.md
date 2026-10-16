---
type: Technology
id: informatica-cdgc-lineage
title: Informatica CDGC lineage
description: Builds end-to-end lineage, including inferred links, across scanned databases, ETL tools, cloud platforms and BI tools, down to column level, for tracing and impact analysis.
platform: platform-informatica
kind: feature
availability: ga
realises: [cross-system-lineage, column-lineage, table-lineage, impact-analysis]
resource: https://www.informatica.com/products/data-catalog.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lineage comes from Metadata Command Center scanners, including PowerCenter and IDMC mappings, Snowflake (with managed Iceberg tables since April 2026), Databricks, Salesforce Data 360 and Tableau. Spring 2026 added saved, personalised lineage views.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery) (primary): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Governance and Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external lineage](../snowflake/snowflake-external-lineage.md), [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenLineage](../open-source/openlineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [Solidatus](../independent/solidatus.md), [Bigeye AI Trust Platform](../independent/bigeye.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
