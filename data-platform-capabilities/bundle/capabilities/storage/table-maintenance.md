---
type: Capability
id: table-maintenance
title: Table maintenance and optimisation
description: Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
aliases: [compaction, vacuum, optimise]
broader: [open-table-formats]
related: [cost-optimisation, data-retention, time-travel, row-level-updates, stream-to-table]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tables degrade with use. Streams and frequent loads create many small files, updates leave delete files and old versions behind, and every commit adds metadata. Maintenance jobs reverse this. Compaction rewrites small files into larger ones. Snapshot expiry removes versions older than the retention window. Orphan clean-up deletes files that no snapshot references, such as those left by failed writes. Re-clustering restores sort order, and statistics collection refreshes what the optimiser uses. A table that receives a commit every minute can gather hundreds of thousands of files in a year if nothing compacts it.

Neglected tables become slow to plan, slow to scan and expensive to store, and deleted data can linger in old files. Maintenance may be run by hand, scheduled as jobs, triggered by the catalogue, or handled by a managed service that watches table health. It competes with user workloads for compute and can conflict with concurrent writers, so its timing and isolation need planning.

# Key considerations

- Snapshot retention sets how far back time travel reaches. Expire too soon and time travel and running readers break; too late and deleted personal data survives.
- Compaction commits can conflict with streaming writers. Choose settings that let compaction proceed without blocking or failing ingestion.
- Track file count, average file size and the ratio of delete files, and trigger maintenance on thresholds rather than fixed schedules.
- Give every shared table a maintenance owner and charge the compute to someone. Unowned tables are the ones that degrade.

# Questions to ask

- How often are the busiest tables written to, and in what batch sizes?
- How long must table history be kept for recovery, audit or reproducibility?
- Is maintenance scheduled, automated, or done when someone notices a slowdown?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open table formats](open-table-formats.md) |
| Related | [Columnar storage](columnar-storage.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Data subject requests](../governance/data-subject-requests.md), [Distributed processing](../processing/distributed-processing.md), [Partitioning and clustering](partitioning-clustering.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Retention and disposal](../governance/data-retention.md), [Row-level updates and deletes](row-level-updates.md), [Storage tiering and lifecycle](storage-tiering.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md), [Streaming ingestion](../ingestion-integration/streaming-ingestion.md), [Time travel](time-travel.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3)
- **Patterns:** [Lakehouse](../../patterns/lakehouse.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 4, Measured)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations · [GDPR](../../frameworks/framework-gdpr.md): Article 17 – Right to erasure

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | S3 Tables automatic maintenance; Glue table optimizers | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md), [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Delta table optimization and V-Order](../../technologies/microsoft/fabric-delta-optimisation-v-order.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery tables for Apache Iceberg](../../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../../technologies/google-cloud/gcp-lakehouse.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake clustering keys and Automatic Clustering](../../technologies/snowflake/snowflake-clustering-keys.md) |
| [Databricks](../../platforms/platform-databricks.md) | Predictive optimization | [Databricks predictive optimization](../../technologies/databricks/databricks-predictive-optimization.md), [Unity Catalog managed Iceberg tables](../../technologies/databricks/databricks-managed-iceberg-tables.md), [Unity Catalog managed tables](../../technologies/databricks/databricks-unity-catalog-managed-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Background merges, OPTIMIZE | [ClickHouse TTL (time to live)](../../technologies/clickhouse/clickhouse-ttl.md), [MergeTree table engine family](../../technologies/clickhouse/clickhouse-mergetree.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Lakehouse Optimizer | [Cloudera Lakehouse Optimizer](../../technologies/cloudera/cloudera-lakehouse-optimizer.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Tableflow](../../technologies/ibm/confluent-tableflow.md), [Spark engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-spark.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hudi](../../technologies/open-source/apache-hudi.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Managed Data Lake Service](../../technologies/independent/fivetran-managed-data-lake-service.md), [Qlik Open Lakehouse](../../technologies/independent/qlik-open-lakehouse.md) |
