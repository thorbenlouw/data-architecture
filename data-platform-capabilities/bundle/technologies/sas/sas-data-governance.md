---
type: Technology
id: sas-data-governance
title: SAS Data Governance
description: Catalogue and governance product in SAS Viya that discovers and profiles data assets, detects personal data, records lineage from data to reports and models, and holds a business glossary.
aliases: [SAS Data Governance Advanced]
formerly: [SAS Information Catalog, SAS Information Governance]
platform: platform-sas
kind: feature
availability: ga
realises:
- data-catalogue
- metadata-harvesting
- data-classification
- table-lineage
- model-lineage
- impact-analysis
- business-glossary
- data-profiling
- data-policy-management
resource: https://www.sas.com/en_us/software/data-governance.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

The base tier, SAS Data Governance, was SAS Information Catalog and covers discovery, cataloguing and metadata management; SAS Data Governance Advanced, which adds lineage, quality assessment, sensitive data detection and policy management, was SAS Information Governance. Discovery agents crawl data sources to collect and enrich metadata. SAS Viya Copilot for Data Discovery answers questions about governed assets in natural language.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.
- [Model lineage](../../capabilities/metadata/model-lineage.md) (Metadata and discovery): Track the data, features, code and runs behind each model and its predictions.
- [Impact analysis](../../capabilities/metadata/impact-analysis.md) (Metadata and discovery): Use lineage to find everything affected by a proposed change or a data incident.
- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery): Define business terms and link them to the data that represents them.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md), [OneLake catalog](../microsoft/fabric-onelake-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../snowflake/snowflake-universal-search.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md), [Databricks Discover](../databricks/databricks-discover.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Data profiling](../../capabilities/data-quality/data-profiling.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Business glossary](../../capabilities/metadata/business-glossary.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Catalog](../independent/dbt-catalog.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md), [data.world](../independent/data-world.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Impact analysis](../../capabilities/metadata/impact-analysis.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Data classification](../../capabilities/governance/data-classification.md) |
