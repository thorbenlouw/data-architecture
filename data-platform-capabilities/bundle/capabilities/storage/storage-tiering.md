---
type: Capability
id: storage-tiering
title: Storage tiering and lifecycle
description: Move data between hot, cool and archive tiers automatically based on age or access patterns.
broader: [object-storage]
related: [data-retention, cost-optimisation, immutable-backups, table-maintenance, backup-restore]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Storage services offer classes at different prices. A hot tier suits frequently read data. Cool or infrequent-access tiers cost less to store but more per read. Archive tiers are cheapest of all but can take minutes to hours to retrieve. Lifecycle rules move objects between them automatically: for example, raw landing files move to a cool tier after 30 days, to archive after a year, and are deleted after seven years. Some services also watch access per object and move it between tiers without any rules.

Most analytical data is read heavily for a short period and rarely afterwards, so tiering can cut the bill sharply for large historical estates. The risk is that tiers and tables do not know about each other. A table format sees files, not tiers, so a query or compaction job that touches archived files may fail or run up large retrieval charges. Retention and disposal decide what must be kept and deleted; tiering decides where the kept data sits.

# Key considerations

- Cool and archive tiers usually have minimum storage periods and retrieval fees. Moving data that is still read now and then can cost more than leaving it hot.
- Tier raw files and backups freely, but avoid archiving files that live tables still reference unless every engine can cope with the retrieval delay.
- Lifecycle deletion is a compliance control only when it is tested and evidenced. Legal holds must override it.
- Per-object charges make small files relatively expensive in cool tiers. Compact before tiering.

# Questions to ask

- How quickly does read activity fall off after data is written?
- Which datasets must be kept for long periods but are almost never read?
- How fast must archived data be restored when it is needed, for example for an audit?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Object storage](object-storage.md) |
| Related | [Backup and restore](../platform-operations/backup-restore.md), [Bulk and offline transfer](../ingestion-integration/bulk-data-transfer.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Immutable backups](../platform-operations/immutable-backups.md), [Observability data analytics](../specialised-data/observability-analytics.md), [Retention and disposal](../governance/data-retention.md), [Table maintenance and optimisation](table-maintenance.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Patterns:** [Data lake](../../patterns/data-lake.md)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 4, Measured)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 12 Data Retention, Archiving and Purging (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | S3 storage classes and S3 Lifecycle rules | [Amazon S3 storage classes and S3 Lifecycle](../../technologies/aws/aws-s3-storage-classes-lifecycle.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Lake Storage](../../technologies/microsoft/azure-data-lake-storage.md), [OneLake storage tiers and lifecycle management](../../technologies/microsoft/fabric-onelake-storage-tiers.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | storage classes, Object Lifecycle Management and Autoclass | [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md), [Google Cloud Storage Autoclass](../../technologies/google-cloud/gcp-cloud-storage-autoclass.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | storage lifecycle policies (COOL and COLD archive tiers) | [Snowflake storage lifecycle policies](../../technologies/snowflake/snowflake-storage-lifecycle-policies.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | TTL TO DISK / TO VOLUME (tiered storage) | [ClickHouse TTL (time to live)](../../technologies/clickhouse/clickhouse-ttl.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud, data lake](../../technologies/sap/sap-hana-cloud-data-lake.md) |
