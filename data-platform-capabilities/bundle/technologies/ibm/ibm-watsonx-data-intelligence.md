---
type: Technology
id: ibm-watsonx-data-intelligence
title: IBM watsonx.data intelligence
description: Governance product that catalogues structured and unstructured data with business terms, classifications, policies, quality scores and lineage, and uses AI to enrich metadata.
formerly: [IBM Knowledge Catalog, Watson Knowledge Catalog, IKC, WKC]
platform: platform-ibm
kind: managed-service
availability: ga
realises:
- data-catalogue
- business-glossary
- data-classification
- data-policy-management
- ai-generated-documentation
- ai-context-layer
- metadata-harvesting
- stewardship-workflows
- column-masking
resource: https://www.ibm.com/products/watsonx-data-intelligence
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

IBM provides an upgrade path from Knowledge Catalog. Data protection rules mask or deny columns when data is accessed through the catalogue and watsonx.data, and governance workflows route changes to terms, classifications and policies for approval. Agentic Data Intelligence (new in 2026) exposes metadata through MCP and Agent Skills.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.
- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery): Draft descriptions, tags and documentation for data assets using AI, for people to review.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx, IBM watsonx.data intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md), [Apache Atlas](../open-source/apache-atlas.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md), [DataHub Cloud](../independent/datahub-cloud.md), [data.world](../independent/data-world.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
