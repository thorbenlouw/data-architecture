---
type: Technology
id: gcp-cloud-storage-autoclass
title: Google Cloud Storage Autoclass
description: Moves each object between storage classes automatically according to how recently it was accessed, without retrieval or early-deletion fees.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [storage-tiering, cost-optimisation]
resource: https://docs.cloud.google.com/storage/docs/autoclass
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Objects under 128 KiB stay in Standard. It cannot be combined with lifecycle rules that change storage class, and suits buckets with unknown access patterns.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management) (primary): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake storage tiers and lifecycle management](../microsoft/fabric-onelake-storage-tiers.md) (preview), [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake storage lifecycle policies](../snowflake/snowflake-storage-lifecycle-policies.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration FinOps](../informatica/informatica-cdi-finops.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
