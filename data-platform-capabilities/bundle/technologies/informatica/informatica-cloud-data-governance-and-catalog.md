---
type: Technology
id: informatica-cloud-data-governance-and-catalog
title: Informatica Cloud Data Governance and Catalog (CDGC)
description: Catalogue and governance service that inventories technical, business and AI assets, links them to a business glossary, policies and stewards, classifies sensitive data, and shows data quality scores per asset.
aliases: [CDGC]
platform: platform-informatica
kind: managed-service
availability: ga
realises:
- data-catalogue
- business-glossary
- data-classification
- data-ownership
- data-quality-scorecards
- stewardship-workflows
resource: https://www.informatica.com/products/data-catalog.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

CLAIRE automates classification, glossary association and description suggestions. Spring 2026 added rule-based workflow triggers and bulk approvals, and Fall 2025 added usage reporting dashboards. CDGC replaces the on-premises Enterprise Data Catalog and Axon Data Governance for cloud customers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.
- [Data quality scorecards](../../capabilities/data-quality/data-quality-scorecards.md) (Data quality and observability): Track quality results over time and report them by dataset, domain and quality dimension.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Governance and Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Business glossary](../../capabilities/metadata/business-glossary.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md), [Data classification](../../capabilities/governance/data-classification.md) |
