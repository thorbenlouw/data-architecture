---
type: Capability
id: row-level-updates
title: Row-level updates and deletes
description: Update, delete and merge individual rows in large tables efficiently.
aliases: [upserts, MERGE, deletion vectors, merge-on-read]
broader: [open-table-formats]
related:
- change-data-capture
- data-subject-requests
- table-maintenance
- incremental-processing
- change-feeds
depends_on: [acid-transactions]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Files in object storage cannot be edited in place, so table formats change individual rows in one of two ways. Copy-on-write rewrites every data file that holds an affected row, which keeps reads fast but means a small update can rewrite gigabytes. Merge-on-read records the change separately, as delete files, deletion vectors (bitmaps marking removed rows) or files of new values, and readers combine these with the base data until compaction folds them in. SQL `UPDATE`, `DELETE` and `MERGE` sit on top, so applying a day's CRM changes is one MERGE keyed on customer id.

Row-level changes are needed for change data capture, slowly changing dimensions, late corrections and privacy erasure. Copy-on-write suits tables changed rarely and read often; merge-on-read suits frequent small changes such as streaming upserts. Cost depends heavily on layout: if the changed rows are spread across every file, both methods do far more work than the size of the change suggests.

# Key considerations

- Cluster or partition tables by the keys that updates target, so each change touches few files.
- Merge-on-read moves cost to readers. Without regular compaction, accumulated delete files slow every query.
- A delete is not an erasure until old snapshots and their files are removed. Privacy deletions need snapshot expiry and file clean-up as well.
- MERGE behaviour differs between engines, especially for duplicate source keys and null matching. Test with realistic change batches.

# Questions to ask

- What share of the table changes each day, and how is it spread across the data?
- Must privacy deletions be physically removed within a set period?
- Do changes arrive continuously from CDC, or in periodic batches?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open table formats](open-table-formats.md) |
| Related | [ACID transactions](acid-transactions.md), [Change data capture](../ingestion-integration/change-data-capture.md), [Change feeds](../serving/change-feeds.md), [Data subject requests](../governance/data-subject-requests.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Incremental processing](../processing/incremental-processing.md), [Retention and disposal](../governance/data-retention.md), [Table maintenance and optimisation](table-maintenance.md) |
| Depends on | [ACID transactions](acid-transactions.md) |
| Needed by | [Change data capture](../ingestion-integration/change-data-capture.md), [Data subject requests](../governance/data-subject-requests.md), [Retention and disposal](../governance/data-retention.md) |

# Where it appears

- **Use cases:** [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3)
- **Patterns:** [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)
- **Frameworks:** [GDPR](../../frameworks/framework-gdpr.md): Article 16 – Right to rectification; Article 17 – Right to erasure

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Lakehouse](../../technologies/microsoft/fabric-lakehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery change data capture](../../technologies/google-cloud/gcp-bigquery-cdc.md), [BigQuery tables for Apache Iceberg](../../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md), [Snowflake micro-partitioned table storage](../../technologies/snowflake/snowflake-managed-storage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Delta Lake on Databricks](../../technologies/databricks/databricks-delta-lake.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Lightweight updates and deletes, mutations, ReplacingMergeTree | [ClickHouse lightweight updates and deletes](../../technologies/clickhouse/clickhouse-lightweight-updates-deletes.md), [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Iceberg in Cloudera](../../technologies/cloudera/cloudera-lakehouse-iceberg.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hudi](../../technologies/open-source/apache-hudi.md), [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Apache Pinot](../../technologies/open-source/apache-pinot.md), [Delta Lake](../../technologies/open-source/delta-lake.md) |
