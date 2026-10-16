---
type: Technology
id: clickhouse-ttl
title: ClickHouse TTL (time to live)
description: Table and column rules that delete, roll up, recompress or move data once it reaches a given age, applied during background merges.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [data-retention, storage-tiering, table-maintenance]
resource: https://clickhouse.com/docs/guides/developer/ttl
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Expiry is not immediate; it runs at merge time (at least every four hours by default). TTL ... TO DISK/VOLUME tiering is for self-managed clusters and is not supported in ClickHouse Cloud, where storage is already object storage.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance) (primary): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md), [AWS Backup](../aws/aws-backup.md), [Amazon S3](../aws/aws-s3.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Lifecycle Management](../microsoft/purview-data-lifecycle-management.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake storage lifecycle policies](../snowflake/snowflake-storage-lifecycle-policies.md), [Snowflake backups](../snowflake/snowflake-backups.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
