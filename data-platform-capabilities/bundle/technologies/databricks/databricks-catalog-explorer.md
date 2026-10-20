---
type: Technology
id: databricks-catalog-explorer
title: Databricks Catalog Explorer
description: The workspace UI for browsing and managing Unity Catalog assets. It shows schemas, permissions, lineage, popularity, table health indicators and AI-generated comments.
formerly: [Data Explorer]
platform: platform-databricks
kind: feature
availability: ga
realises:
- data-catalogue
- ai-generated-documentation
- usage-metadata
- metadata-harvesting
- data-trust-indicators
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

AI-generated comments can be reviewed before saving and written in a chosen language. Column popularity was added in June 2026, and table health indicators are in Public Preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.
- [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) (Metadata and discovery): Show who uses which data, how often and how, to guide discovery and clean-up.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) (Metadata and discovery): Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [Apache Atlas](../open-source/apache-atlas.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Secoda](../independent/secoda.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
