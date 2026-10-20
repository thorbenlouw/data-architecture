---
type: Technology
id: oracle-autonomous-ai-database-catalog
title: Oracle Autonomous AI Database Catalog
description: A "catalogue of catalogues" in Autonomous AI Database that brings metadata from external catalogues, clouds and on-premises sources into one searchable view for discovery and access.
platform: platform-oracle
kind: feature
availability: ga
realises: [data-catalogue, table-catalogue, metadata-interoperability, catalogue-federation]
resource: https://www.oracle.com/news/announcement/ai-world-oracle-introduces-autonomous-ai-lakehouse-2025-10-14/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced with Autonomous AI Lakehouse in October 2025. It federates Databricks Unity Catalog, AWS Glue, Apache Polaris and other catalogues rather than replacing them. Its purpose overlaps with OCI Data Catalog and the AI Data Platform Master Catalog.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Autonomous AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks catalog federation](../databricks/databricks-catalog-federation.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Gravitino](../open-source/apache-gravitino.md), [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Atlan](../independent/atlan.md), [data.world](../independent/data-world.md), [dbt Catalog](../independent/dbt-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
