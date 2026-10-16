---
type: Technology
id: purview-data-lifecycle-management
title: Microsoft Purview Data Lifecycle Management
description: Applies retention policies and labels that keep or delete content for set periods, with records management for regulated items.
platform: platform-microsoft
kind: saas
availability: ga
realises: [data-retention]
resource: https://learn.microsoft.com/en-us/purview/data-lifecycle-management
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Mainly for Microsoft 365 content; retention in analytical stores is handled by table and storage policies.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Retention and disposal](../../capabilities/governance/data-retention.md) (Governance and compliance) (primary): Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md), [AWS Backup](../aws/aws-backup.md), [Amazon S3](../aws/aws-s3.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake storage lifecycle policies](../snowflake/snowflake-storage-lifecycle-policies.md), [Snowflake backups](../snowflake/snowflake-backups.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md) | [Retention and disposal](../../capabilities/governance/data-retention.md) |
