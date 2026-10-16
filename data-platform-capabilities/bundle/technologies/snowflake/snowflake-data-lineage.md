---
type: Technology
id: snowflake-data-lineage
title: Snowflake data lineage (Snowsight lineage)
description: Records table and column lineage from DML, CTAS and view dependencies, plus ML lineage across datasets, feature views, models and monitors, shown as a graph in Catalog Explorer.
platform: platform-snowflake
kind: feature
availability: ga
realises: [table-lineage, column-lineage, impact-analysis, model-lineage]
resource: https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition and keeps one year of history. Lineage now covers Cortex Agents, Cortex Search services, external tables and temporary tables. It also shows tag and masking-policy mismatches across related columns.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery) (primary): Track dependencies between datasets, tables and views.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog data lineage](../aws/aws-sagemaker-catalog-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md), [Fabric materialized lake views](../microsoft/fabric-materialized-lake-views.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Model lineage](../../capabilities/metadata/model-lineage.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Marquez](../open-source/marquez.md), [Apache Atlas](../open-source/apache-atlas.md), [dbt Core (v1.x)](../open-source/dbt-core.md) | [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Lineage](../independent/collibra-data-lineage.md), [dbt Catalog](../independent/dbt-catalog.md) | [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
