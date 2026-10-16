---
type: Technology
id: cloudera-data-catalog
title: Cloudera Data Catalog
description: Catalogue service over SDX metadata for searching assets, viewing Atlas lineage and running profilers that collect statistics and detect sensitive data.
platform: platform-cloudera
kind: feature
availability: ga
realises: [data-catalogue, data-profiling, data-classification, table-lineage]
resource: https://docs.cloudera.com/data-catalog/cloud/core-concepts/topics/dc-understanding-the-profiler.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Profilers tag columns that look like personal data, and the tags can drive Apache Ranger tag-based policies. It covers the Cloudera estate only; [Cloudera Data Lineage](cloudera-data-lineage.md) covers lineage across other tools.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery) (primary): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Data profiling](../../capabilities/data-quality/data-profiling.md) (Data quality and observability): Analyse data to understand its structure, distributions, completeness and anomalies.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Table-level lineage](../../capabilities/metadata/table-lineage.md) (Metadata and discovery): Track dependencies between datasets, tables and views.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Shared Data Experience

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake catalog](../microsoft/fabric-onelake-catalog.md), [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Universal Search](../snowflake/snowflake-universal-search.md), [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Discover](../databricks/databricks-discover.md), [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Data classification](../../capabilities/governance/data-classification.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Catalog](../independent/dbt-catalog.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md), [data.world](../independent/data-world.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table-level lineage](../../capabilities/metadata/table-lineage.md), [Data classification](../../capabilities/governance/data-classification.md) |
