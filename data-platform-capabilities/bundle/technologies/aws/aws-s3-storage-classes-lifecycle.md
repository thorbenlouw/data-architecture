---
type: Technology
id: aws-s3-storage-classes-lifecycle
title: Amazon S3 storage classes and S3 Lifecycle
description: Set of S3 storage tiers from Standard to Glacier Deep Archive, with Intelligent-Tiering and lifecycle rules that move or expire objects by age.
aliases: [S3 Intelligent-Tiering, S3 Glacier storage classes]
platform: platform-aws
kind: feature
availability: ga
realises: [storage-tiering, data-retention, cost-optimisation]
resource: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Classes include Standard, Express One Zone, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval and Glacier Deep Archive, with minimum storage durations of 30-180 days for the colder classes. The older vault-based Amazon S3 Glacier service (Glacier Direct) is closed to new customers; use the S3 Glacier storage classes instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management) (primary): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon S3

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake storage tiers and lifecycle management](../microsoft/fabric-onelake-storage-tiers.md) (preview), [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Autoclass](../google-cloud/gcp-cloud-storage-autoclass.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md), [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake storage lifecycle policies](../snowflake/snowflake-storage-lifecycle-policies.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Retention and disposal](../../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
