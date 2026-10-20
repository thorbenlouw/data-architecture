---
type: Technology
id: informatica-metadata-command-center
title: Informatica Metadata Command Center (MCC)
description: Administration service where you configure catalog sources and scanners that harvest metadata, lineage, profiles and classifications from source systems into the IDMC metadata repository.
aliases: [MCC]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [metadata-harvesting, metadata-interoperability]
resource: https://onlinehelp.informatica.com/IICS/prod/mcc/en/index.htm
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

There are scanners for many databases, warehouses, SaaS apps, BI tools and Kafka. A custom metadata integration format covers unsupported sources. Data observability and Data Access Management are switched on per source here.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery) (primary): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Governance and Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Metadata](../aws/aws-s3-metadata.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
