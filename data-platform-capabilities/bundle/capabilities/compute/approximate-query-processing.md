---
type: Capability
id: approximate-query-processing
title: Approximate query processing
description: Answer aggregate queries faster and with less memory using sampling and probabilistic sketches.
aliases: [HyperLogLog, sketches, sampling]
broader: [query-acceleration]
related:
- materialised-views
- metric-definitions
- observability-analytics
- real-time-analytics
- behavioural-event-collection
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some questions do not need exact answers: how many distinct visitors came this month, what the 95th percentile response time was, which products are in the top ten. Approximate methods answer them with a fraction of the memory and time. Sketches are compact summaries of a column: HyperLogLog estimates distinct counts to within about one or two per cent using a few kilobytes, t-digest and KLL estimate quantiles, and count-min sketches find frequent items. Sampling reads a random subset of rows and scales up the result. Sketches can be stored and merged, so daily sketches combine into a monthly distinct count without rescanning raw data.

Approximation suits very large data, interactive exploration and dashboards where exact distinct counts would be too slow or costly. It is unsuitable for financial figures, billing and anything audited. The most practical use is storing mergeable sketches in aggregate tables, which lets distinct counts roll up across days, regions or segments, something exact pre-aggregated counts cannot do.

# Key considerations

- Label approximate figures in reports, with their error bounds, so nobody treats them as exact.
- Sketch formats differ between engines. Stored sketches may be unreadable elsewhere unless one open library, such as Apache DataSketches, is used throughout.
- Sampling misses rare events and small groups. Use it for overall trends, not for counts in small segments.
- Accuracy depends on sketch settings. Choose precision to suit the decisions the figures support.

# Questions to ask

- Which metrics can tolerate small errors, and which must be exact?
- Are distinct counts or percentiles slow or costly at current data volumes?
- Do distinct counts need to roll up across days, regions or segments?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query acceleration](query-acceleration.md) |
| Related | [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Materialised views](materialised-views.md), [Observability data analytics](../specialised-data/observability-analytics.md), [Real-time analytical database](real-time-analytics.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena](../../technologies/aws/aws-athena.md), [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Explorer](../../technologies/microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse server](../../technologies/clickhouse/clickhouse-server.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Doris](../../technologies/open-source/apache-doris.md), [Apache Druid](../../technologies/open-source/apache-druid.md), [Apache Pinot](../../technologies/open-source/apache-pinot.md), [Apache Spark](../../technologies/open-source/apache-spark.md), [DuckDB](../../technologies/open-source/duckdb.md), [Presto](../../technologies/open-source/presto.md), [StarRocks](../../technologies/open-source/starrocks.md), [Trino](../../technologies/open-source/trino.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Imply Polaris](../../technologies/independent/imply-polaris.md), [StarTree Cloud](../../technologies/independent/startree-cloud.md) |
