---
type: Technology
id: ibm-manta-data-lineage
title: IBM Manta Data Lineage
description: Automated lineage service that scans code, ETL tools, databases and BI reports to build column-level, end-to-end lineage across more than 50 technologies.
aliases: [Manta, IBM Manta]
platform: platform-ibm
kind: software
availability: ga
realises: [column-lineage, cross-system-lineage, impact-analysis, metadata-harvesting]
resource: https://www.ibm.com/products/manta-data-lineage
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Acquired in 2023 and now delivered within watsonx.data intelligence. Supports [OpenLineage](../open-source/openlineage.md) and the OpenManta API for custom sources, and keeps historical lineage views.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery) (primary): Track how each column is derived from source columns.
- [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md) (Metadata and discovery): Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx.data intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenLineage](../open-source/openlineage.md), [DataHub](../open-source/datahub.md), [dbt OSS](../open-source/dbt-oss.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md), [dbt v2 engine](../independent/dbt-fusion-engine.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [End-to-end lineage](../../capabilities/metadata/cross-system-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
