---
type: Technology
id: aws-sagemaker-catalog
title: Amazon SageMaker Catalog
description: Business data catalogue in SageMaker Unified Studio where producers publish assets and data products with glossary terms and metadata forms, and consumers search and subscribe.
aliases: [Amazon DataZone]
platform: platform-aws
kind: feature
availability: ga
realises:
- data-catalogue
- business-glossary
- access-requests
- data-product-specification
- ai-generated-documentation
- data-domains
- data-trust-indicators
resource: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/working-with-business-catalog.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on Amazon DataZone, which remains available as a standalone service with its own portal; new features land in SageMaker Catalog first. Approved subscriptions grant Lake Formation or Redshift permissions automatically. Shows data quality scores from Glue Data Quality or external tools through time-series APIs. Since May 2026 also available in IAM-based domains.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.
- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance): Group data assets, products and owners into business domains with their own stewardship and policies.
- [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) (Metadata and discovery): Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon SageMaker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data trust indicators](../../capabilities/metadata/data-trust-indicators.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [DataHub Cloud](../independent/datahub-cloud.md), [Secoda](../independent/secoda.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data domains](../../capabilities/governance/data-domains.md) |
