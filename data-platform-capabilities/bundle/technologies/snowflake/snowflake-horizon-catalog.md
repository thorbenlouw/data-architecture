---
type: Technology
id: snowflake-horizon-catalog
title: Snowflake Horizon Catalog
description: Snowflake's built-in catalogue and governance layer, covering object discovery, tagging, policies, quality, lineage, access history and Iceberg catalogue services for Snowflake and external data.
formerly: [Snowflake Horizon]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-catalogue, table-catalogue, data-policy-management, metadata-harvesting]
resource: https://docs.snowflake.com/en/user-guide/snowflake-horizon
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Horizon Catalog is the umbrella name for Snowflake's governance, discovery and interoperability features, among them [Universal Search](snowflake-universal-search.md), [object tagging](snowflake-object-tagging.md), [masking policies](snowflake-masking-policies.md), [data lineage](snowflake-data-lineage.md), [data quality monitoring](snowflake-data-quality-monitoring.md), the [Trust Center](snowflake-trust-center.md) and the [Iceberg REST Catalog API](snowflake-horizon-iceberg-rest-catalog.md). Horizon Catalog connectors (preview) harvest metadata from Redshift, BigQuery, Databricks, Oracle, SQL Server, Tableau, Power BI, Looker and dbt. The Catalog Explorer UI is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [Apache Atlas](../open-source/apache-atlas.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md), [data.world](../independent/data-world.md), [dbt Catalog](../independent/dbt-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
