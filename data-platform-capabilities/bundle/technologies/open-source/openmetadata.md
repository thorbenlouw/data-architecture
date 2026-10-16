---
type: Technology
id: openmetadata
title: OpenMetadata
description: Metadata platform combining a data catalogue, lineage, glossary, data quality tests, data contracts, domains and data products.
platform: platform-open-source
kind: open-source
availability: ga
realises:
- data-catalogue
- data-quality-rules
- column-lineage
- business-glossary
- data-contracts
- data-domains
- governance-metrics
- ai-context-layer
resource: https://github.com/open-metadata/OpenMetadata
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, led by Collate, which sells a managed version with AI features. Version 1.12.x is current. Supports ODCS 3.1 contracts, OpenLineage events and an MCP server; has more than 130 connectors.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Column-level lineage](../../capabilities/metadata/column-lineage.md) (Metadata and discovery): Track how each column is derived from source columns.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) (Governance and compliance): Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md), [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Atlan](../independent/atlan.md), [Select Star](../independent/select-star.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Column-level lineage](../../capabilities/metadata/column-lineage.md) |
