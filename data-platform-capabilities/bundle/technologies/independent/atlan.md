---
type: Technology
id: atlan
title: Atlan
description: Metadata platform that builds a graph of data, BI and business systems and serves it to people through a catalogue and marketplace and to AI agents through an MCP server and APIs.
platform: platform-independent
vendor: Atlan
kind: saas
availability: ga
realises:
- data-catalogue
- active-metadata
- column-lineage
- agent-tool-access
- metadata-interoperability
- ai-context-layer
- data-domains
- data-certification
- data-trust-indicators
resource: https://atlan.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Atlan now calls itself a context platform for AI. Its components are the Enterprise Data Graph (80+ connectors), Context Agents (AI documentation and glossary drafting), Context Engineering Studio (tests business context and deploys it to Cortex, Genie, Claude and others) and the Iceberg-native Context Lakehouse (Metadata Lakehouse), which exposes metadata as tables. It is strong on automation that acts on metadata, such as propagating tags.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Active metadata](../../capabilities/metadata/active-metadata.md) (Metadata and discovery): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Data certification](../../capabilities/metadata/data-certification.md) (Metadata and discovery): Mark assets as trusted, deprecated or under review so consumers know what to rely on.
- [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) (Metadata and discovery): Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data certification](../../capabilities/metadata/data-certification.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Active metadata](../../capabilities/metadata/active-metadata.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data certification](../../capabilities/metadata/data-certification.md), [Data domains](../../capabilities/governance/data-domains.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [Active metadata](../../capabilities/metadata/active-metadata.md), [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
