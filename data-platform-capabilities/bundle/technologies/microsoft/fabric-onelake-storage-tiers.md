---
type: Technology
id: fabric-onelake-storage-tiers
title: OneLake storage tiers and lifecycle management
description: Moves OneLake data between hot, cool and cold tiers using lifecycle policies to lower storage cost.
platform: platform-microsoft
kind: feature
availability: preview
realises: [storage-tiering, cost-optimisation]
resource: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Fabric-June-2026-Feature-Summary/ba-p/5190690
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced in preview in June 2026 alongside OneLake item-size reporting.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) (Storage and table management) (primary): Move data between hot, cool and archive tiers automatically based on age or access patterns.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** preview  
**Product family:** OneLake

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Autoclass](../google-cloud/gcp-cloud-storage-autoclass.md), [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake storage lifecycle policies](../snowflake/snowflake-storage-lifecycle-policies.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse TTL (time to live)](../clickhouse/clickhouse-ttl.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration FinOps](../informatica/informatica-cdi-finops.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud, data lake](../sap/sap-hana-cloud-data-lake.md) | [Storage tiering and lifecycle](../../capabilities/storage/storage-tiering.md) |
