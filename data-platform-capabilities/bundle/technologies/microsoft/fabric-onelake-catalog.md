---
type: Technology
id: fabric-onelake-catalog
title: OneLake catalog
description: The Fabric catalogue for finding, understanding, governing and securing items, with Explore, Govern and Secure views.
formerly: [OneLake data hub]
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-catalogue, data-certification, data-ownership, governance-metrics, data-trust-indicators]
resource: https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Covers Fabric items only; Purview Unified Catalog is the cross-estate catalogue. Endorsement (promoted, certified, master data) is how Fabric marks trusted items. The Govern tab became GA in March 2026; the catalogue search API and MCP tools are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Data certification](../../capabilities/metadata/data-certification.md) (Metadata and discovery): Mark assets as trusted, deprecated or under review so consumers know what to rely on.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.
- [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) (Governance and compliance): Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement.
- [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) (Metadata and discovery): Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data certification](../../capabilities/metadata/data-certification.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md), [Atlan](../independent/atlan.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data certification](../../capabilities/metadata/data-certification.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
