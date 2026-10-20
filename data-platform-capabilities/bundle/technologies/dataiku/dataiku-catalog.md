---
type: Technology
id: dataiku-catalog
title: Dataiku Catalog
description: Instance-wide catalogue for finding datasets, models, agents, knowledge banks and other project assets, with curated collections, a most-used datasets view and AI-generated descriptions.
formerly: [Dataiku Data Catalog]
platform: platform-dataiku
kind: feature
availability: ga
realises: [data-catalogue, usage-metadata, ai-generated-documentation]
resource: https://doc.dataiku.com/dss/latest/catalog/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Renamed from Data Catalog in version 15.0, when it grew from datasets to other asset types. It covers assets in the Dataiku instance and indexed external tables from its connections, not the wider estate. The Generate Metadata assistant writes short and long dataset descriptions and column descriptions with an LLM for people to approve or edit.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) (Metadata and discovery): Show who uses which data, how often and how, to guide discovery and clean-up.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Select Star](../independent/select-star.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md), [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
