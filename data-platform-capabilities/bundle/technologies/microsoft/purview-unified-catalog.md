---
type: Technology
id: purview-unified-catalog
title: Microsoft Purview Unified Catalog
description: A business-facing data governance catalogue organised by governance domains, with glossary terms, critical data elements, OKRs and health management.
formerly: [Microsoft Purview Data Catalog]
platform: platform-microsoft
kind: saas
availability: ga
realises:
- data-catalogue
- business-glossary
- data-ownership
- data-domains
- critical-data-elements
- governance-metrics
- stewardship-workflows
resource: https://learn.microsoft.com/en-us/purview/unified-catalog
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sits on top of the Data Map, which supplies technical metadata. Health controls score governance maturity and health actions list fixes. Requires the enterprise version of the new Purview portal; rolling out by region.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.
- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Critical data elements](../../capabilities/governance/critical-data-elements.md) (Governance and compliance): Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them.
- [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) (Governance and compliance): Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenMetadata](../open-source/openmetadata.md), [DataHub](../open-source/datahub.md), [Apache Atlas](../open-source/apache-atlas.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md), [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [DataHub Cloud](../independent/datahub-cloud.md), [data.world](../independent/data-world.md) | [Critical data elements](../../capabilities/governance/critical-data-elements.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md), [Data domains](../../capabilities/governance/data-domains.md) |
