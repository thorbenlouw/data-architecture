---
type: Technology
id: snowflake-storage-lifecycle-policies
title: Snowflake storage lifecycle policies
description: Schema-level policies that archive table rows to cheaper COOL or COLD tiers, or delete them permanently, according to conditions such as age.
platform: platform-snowflake
kind: feature
availability: ga
realises: [storage-tiering, data-retention]
resource: https://docs.snowflake.com/en/user-guide/storage-management/storage-lifecycle-policies
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

COOL has a 90-day minimum archive period. COLD costs about a quarter of COOL but has a 180-day minimum and up to 48 hours to retrieve, and is on AWS and Google Cloud only. Archived rows cannot be queried until restored to a new table, and archived data is not replicated.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management) (primary): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake storage tiers and lifecycle management](../microsoft/fabric-onelake-storage-tiers.md) (preview), [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [Microsoft Purview Data Lifecycle Management](../microsoft/purview-data-lifecycle-management.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Autoclass](../google-cloud/gcp-cloud-storage-autoclass.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
