---
type: Technology
id: dbt-catalog
title: dbt Catalog
description: Searchable catalogue of the models, sources, metrics and exposures in dbt projects, with lineage, documentation and run health.
formerly: [dbt Explorer]
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: feature
availability: ga
realises: [data-catalogue, table-lineage, column-lineage, impact-analysis]
resource: https://docs.getdbt.com/docs/explore/explore-projects
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on the Discovery API, a GraphQL API over dbt project metadata. It covers assets that dbt manages or declares, not a whole estate, so large organisations usually pair it with an enterprise catalogue.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [Data lineage in Microsoft Purview](../microsoft/purview-lineage.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md), [Knowledge Catalog data lineage](../google-cloud/gcp-knowledge-catalog-data-lineage.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake data lineage (Snowsight lineage)](../snowflake/snowflake-data-lineage.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Unity Catalog data lineage](../databricks/databricks-unity-catalog-lineage.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md), [Informatica CDGC lineage](../informatica/informatica-cdgc-lineage.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Lineage](../palantir/palantir-data-lineage.md) | [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md) |
