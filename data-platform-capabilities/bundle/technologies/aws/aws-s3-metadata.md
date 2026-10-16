---
type: Technology
id: aws-s3-metadata
title: Amazon S3 Metadata
description: Captures object metadata for a general purpose bucket into read-only, S3-managed Iceberg tables (journal, live inventory and annotation tables) that can be queried with SQL.
platform: platform-aws
kind: feature
availability: ga
realises: [metadata-harvesting, unstructured-data, system-telemetry]
resource: https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-overview.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tables live in an AWS-managed table bucket (aws-s3) and are queried through the Glue Data Catalog with Athena, EMR or Redshift. Useful for cataloguing unstructured content and auditing changes; the live inventory backfill is charged.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery) (primary): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations): Expose platform usage, billing and operational data as queryable tables.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon S3

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Metadata Command Center (MCC)](../informatica/informatica-metadata-command-center.md), [Informatica Data 360 Connector and Scanner](../informatica/informatica-data-360-connector-and-scanner.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Lineage](../cloudera/cloudera-data-lineage.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Manta Data Lineage](../ibm/ibm-manta-data-lineage.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
