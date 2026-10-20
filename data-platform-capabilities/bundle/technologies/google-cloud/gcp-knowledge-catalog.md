---
type: Technology
id: gcp-knowledge-catalog
title: Knowledge Catalog
description: Google Cloud's metadata catalogue for data and AI assets, providing automatic metadata ingestion, keyword and semantic search, aspects, a business glossary and metadata APIs.
formerly: [Dataplex Universal Catalog, Dataplex Catalog, Dataplex]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- data-catalogue
- metadata-harvesting
- business-glossary
- active-metadata
- metadata-interoperability
- ai-context-layer
resource: https://docs.cloud.google.com/dataplex/docs/introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in April 2026; APIs, IAM roles and gcloud still use "dataplex". Ingests BigQuery, Cloud SQL, Spanner, Agent Platform, Looker and Cloud Storage metadata automatically, imports dbt metadata, and has connectors for Oracle, MySQL, PostgreSQL and SQL Server (preview). Metadata change feeds via Pub/Sub, a remote MCP server and a lookupContext API for agents (preview) support automation. Data domains are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Active metadata](../../capabilities/metadata/active-metadata.md) (Metadata and discovery): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Knowledge Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [Active metadata](../../capabilities/metadata/active-metadata.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Atlan](../independent/atlan.md), [Select Star](../independent/select-star.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Active metadata](../../capabilities/metadata/active-metadata.md) |
