---
type: Capability
id: managed-storage
title: Platform-managed storage
description: Let the platform manage table storage layout, compression and durability internally.
aliases: [native tables, proprietary storage]
broader: [storage]
related:
- open-table-formats
- decoupled-storage-compute
- time-travel
- backup-restore
- engine-interoperability
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

With platform-managed storage, the database or warehouse decides how table data is laid out: file format, compression, micro-partitions, indexes, replication and backups. Users see tables and SQL, never files. The platform can use internal formats tuned to its engine, reorganise data in the background, and provide features such as automatic clustering, time travel and provider-run recovery without any user action. The bytes may still sit in cloud object storage, but only the platform's engine can interpret them directly.

It suits teams that want warehouse behaviour with little operational work: no compaction jobs, no file sizes to tune and no catalogue to run. The price is portability. Other engines reach the data only through the platform's query interfaces, exports or sharing features, and leaving means unloading everything. Many platforms now offer managed tables and open-format tables side by side, and increasingly maintain open tables for you as well, which narrows the gap between the two.

# Key considerations

- Price storage, background maintenance compute and data egress together. Managed storage is often priced differently from raw object storage.
- Check how data can leave: bulk export speed, export to open formats and sharing to other engines. Exit cost matters at contract renewal.
- Managed tables usually include recovery features. Know their retention periods and costs before treating them as backup.
- In mixed estates, set a rule for which data goes into managed storage and which into open tables, based on which engines need it.

# Questions to ask

- Will engines other than this platform need direct access to the data?
- How much effort can the team spend on file layout and table maintenance?
- What would it take to move this data to another platform in five years?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Related | [Backup and restore](../platform-operations/backup-restore.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Open table formats](open-table-formats.md), [Time travel](time-travel.md) |

# Where it appears

- **Patterns:** [Data warehouse](../../patterns/data-warehouse.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift Managed Storage (RMS) | [Amazon Redshift](../../technologies/aws/aws-redshift.md), [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery managed storage](../../technologies/google-cloud/gcp-bigquery-managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake micro-partitioned table storage](../../technologies/snowflake/snowflake-managed-storage.md) |
| [Databricks](../../platforms/platform-databricks.md) | Unity Catalog managed tables and default storage | [Unity Catalog managed tables](../../technologies/databricks/databricks-unity-catalog-managed-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [SharedMergeTree](../../technologies/clickhouse/clickhouse-sharedmergetree.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud](../../technologies/sap/sap-business-data-cloud.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry](../../technologies/palantir/palantir-foundry.md) |
