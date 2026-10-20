---
type: Technology
id: select-star
title: Select Star
description: Automated catalogue that builds column-level lineage, usage-based popularity and entity relationships from query logs and generates semantic models from BI logic.
platform: platform-independent
vendor: Select Star (Snowflake)
kind: saas
availability: ga
realises:
- data-catalogue
- column-lineage
- usage-metadata
- semantic-layer
- agent-tool-access
- ai-context-layer
resource: https://www.selectstar.com/resources/snowflake-acquire-select-star
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Snowflake announced the purchase in November 2025, and the site now says Select Star is part of Snowflake. Its lineage and discovery are being brought into Snowflake Horizon Catalog, so treat it as a Snowflake-aligned option and confirm its future as a standalone, multi-platform product. Provides an MCP server for agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) (Metadata and discovery): Show who uses which data, how often and how, to guide discovery and clean-up.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
