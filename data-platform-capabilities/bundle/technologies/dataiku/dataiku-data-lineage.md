---
type: Technology
id: dataiku-data-lineage
title: Dataiku Data Lineage
description: Column-level lineage across datasets and projects in a Dataiku instance, with manual lineage entries and exports of the lineage graph.
platform: platform-dataiku
kind: feature
availability: ga
realises: [column-lineage, impact-analysis]
resource: https://doc.dataiku.com/dss/latest/data-lineage/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Records only direct lineage, meaning transformations that change an output column's values. Covers work done in Dataiku, so lineage for other tools needs an external catalogue.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery) (primary): Track how each column is derived from source columns.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dbt OSS](../open-source/dbt-oss.md), [OpenLineage](../open-source/openlineage.md), [DataHub](../open-source/datahub.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md), [dbt v2 engine](../independent/dbt-fusion-engine.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md) |
