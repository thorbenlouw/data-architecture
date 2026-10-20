---
type: Technology
id: oracle-oci-data-catalog
title: OCI Data Catalog
description: Managed metadata service that harvests technical metadata from OCI and on-premises sources, adds business glossary terms and tags, and provides a Hive-compatible metastore.
aliases: [Oracle Cloud Infrastructure Data Catalog]
platform: platform-oracle
kind: managed-service
availability: ga
realises: [data-catalogue, metadata-harvesting, business-glossary, table-catalogue]
resource: https://docs.oracle.com/en-us/iaas/data-catalog/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Its Hive-compatible metastore serves OCI Data Flow and other Spark engines. Its purpose overlaps with the newer [Oracle Autonomous AI Database Catalog](oracle-autonomous-ai-database-catalog.md) and the AI Data Platform Master Catalog, so an Oracle estate can end up with more than one catalogue.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md), [dbt Catalog](../independent/dbt-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
