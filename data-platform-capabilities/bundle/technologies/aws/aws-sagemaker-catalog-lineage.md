---
type: Technology
id: aws-sagemaker-catalog-lineage
title: Amazon SageMaker Catalog data lineage
description: OpenLineage-compatible lineage graph that records how catalogued assets are produced and consumed, captured automatically from supported connections and tools or posted through APIs.
aliases: [Amazon DataZone data lineage]
platform: platform-aws
kind: feature
availability: ga
realises: [table-lineage, cross-system-lineage, metadata-interoperability, impact-analysis]
resource: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/datazone-data-lineage.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Accepts OpenLineage events, so external tools such as Airflow or dbt can contribute lineage. Automatic capture covers AWS sources such as Glue, Redshift and EMR, and the depth of column-level detail differs by source.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery) (primary): Track dependencies between datasets, tables and views.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md), [Snowflake external lineage](../snowflake/snowflake-external-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Marquez](../open-source/marquez.md), [Apache Atlas](../open-source/apache-atlas.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md) | [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
