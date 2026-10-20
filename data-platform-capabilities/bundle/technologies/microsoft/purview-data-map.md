---
type: Technology
id: purview-data-map
title: Microsoft Purview Data Map
description: Scans on-premises, multicloud and SaaS sources to harvest schemas, classifications and lineage into a metadata graph with Apache Atlas-compatible APIs.
formerly: [Azure Purview]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [metadata-harvesting, data-classification, metadata-interoperability]
resource: https://learn.microsoft.com/en-us/purview/data-map
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Billed in capacity units by metadata storage and throughput. Classic Purview accounts and the classic Data Catalog experience still exist but are being superseded by the new portal.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery) (primary): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Metadata](../aws/aws-s3-metadata.md), [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Metadata Command Center (MCC)](../informatica/informatica-metadata-command-center.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md), [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md) | [Data classification](../../capabilities/governance/data-classification.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
