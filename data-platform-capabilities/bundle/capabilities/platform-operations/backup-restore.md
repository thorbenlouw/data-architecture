---
type: Capability
id: backup-restore
title: Backup and restore
description: Take point-in-time backups of data and metadata and restore them when needed.
broader: [business-continuity]
related: [time-travel, data-retention, zero-copy-cloning, data-subject-requests, cross-region-failover]
depends_on: [object-storage]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A backup is a copy of data, and of the metadata needed to use it, taken at a known point in time and stored apart from the original so it survives deletion, corruption or loss of the source. It may be a snapshot of a table, schema or database, a copy of storage files to a separate account, or an export of catalogue entries, permissions and configuration. Restore brings back a chosen point, in place or into a new location, so that a table overwritten by yesterday's faulty job can be returned to its state at 02:00.

Time travel restores recent versions, but only for a limited period and within the same account, so it does not replace backups held elsewhere. Backups cover account compromise and mistakes found weeks later. For open table formats, a consistent backup must capture data files and table metadata together, or the restored table cannot be read. Restore time matters as much as backup frequency, since restoring hundreds of terabytes can take days.

# Key considerations

- Back up metadata as well as data: table definitions, catalogue entries, permissions and pipeline configuration.
- Keep at least one copy in a separate account or under separate credentials, so a compromise of the platform does not reach the backups.
- Measure restore time for the largest datasets. A backup that takes a week to restore may not meet the recovery objective.
- Align backup retention with deletion policies, so erased personal data does not survive indefinitely in backups.

# Questions to ask

- How far back must you be able to restore, and at what level: account, database, table or row?
- How long would restoring your largest critical dataset take today?
- Are backups held in a separate account, region or provider?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Backup and disaster recovery](business-continuity.md) |
| Narrower | [Immutable backups](immutable-backups.md) |
| Related | [Cross-region replication and failover](cross-region-failover.md), [Crypto-shredding](../security/crypto-shredding.md), [Data subject requests](../governance/data-subject-requests.md), [Data versioning](../storage/data-versioning.md), [Object storage](../storage/object-storage.md), [Platform-managed storage](../storage/managed-storage.md), [Retention and disposal](../governance/data-retention.md), [Storage tiering and lifecycle](../storage/storage-tiering.md), [Time travel](../storage/time-travel.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Object storage](../storage/object-storage.md) |
| Needed by | [Resilience and recovery testing](resilience-testing.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2)
- **Maturity tracks:** [Resilience and recovery](../../maturity/track-resilience.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Articles 11 and 12 – Response and recovery; backup, restoration and recovery; Chapter IV – Digital operational resilience testing (Articles 24 to 27) · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Article 32 – Security of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Backup | [AWS Backup](../../technologies/aws/aws-backup.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Backup](../../technologies/microsoft/azure-backup.md), [Azure SQL Database](../../technologies/microsoft/azure-sql.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery table snapshots](../../technologies/google-cloud/gcp-bigquery-table-snapshots.md), [BigQuery time travel](../../technologies/google-cloud/gcp-bigquery-time-travel.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | backups (formerly snapshots); Fail-safe | [Snowflake backups](../../technologies/snowflake/snowflake-backups.md), [Snowflake Fail-safe](../../technologies/snowflake/snowflake-fail-safe.md), [Snowflake Time Travel](../../technologies/snowflake/snowflake-time-travel.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks managed disaster recovery](../../technologies/databricks/databricks-managed-disaster-recovery.md) (preview), [Databricks table clone (shallow and deep clone)](../../technologies/databricks/databricks-table-clone.md), [Lakebase](../../technologies/databricks/databricks-lakebase.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud backups and BACKUP/RESTORE](../../technologies/clickhouse/clickhouse-backups.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Replication Manager](../../technologies/cloudera/cloudera-replication-manager.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Backup, Archive and Restore and Data Mover](../../technologies/teradata/teradata-bar-data-mover.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Cloud Stacks and Fleet Manager](../../technologies/dataiku/dataiku-cloud-stacks.md) |

Narrower capabilities are realised by a further 5 technologies; see their pages.
