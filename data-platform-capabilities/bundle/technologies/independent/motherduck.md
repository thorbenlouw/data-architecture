---
type: Technology
id: motherduck
title: MotherDuck
description: Serverless cloud data warehouse built on DuckDB that gives each user or agent its own isolated compute instance and can split one query across a laptop and the cloud.
platform: platform-independent
vendor: MotherDuck
kind: managed-service
availability: ga
realises: [serverless-compute, single-node-processing, workload-isolation, open-table-formats, sql-access]
resource: https://motherduck.com/docs/concepts/architecture-and-capabilities/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Compute units are called Ducklings, and read replicas scale reads horizontally. Managed storage uses DuckLake, with bring-your-own bucket on S3, R2, Azure or GCS. A Postgres endpoint, database shares, a remote MCP server and Dives (dashboards generated from prompts) are included. It runs in AWS regions only.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation): Process small to medium datasets quickly on one machine using in-process engines.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Open table formats](../../capabilities/storage/open-table-formats.md) (Storage and table management): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation): Connect tools and code to the platform through standard drivers and protocols.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md), [Cloud Run](../google-cloud/gcp-cloud-run.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks Free Edition](../databricks/databricks-free-edition.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md), [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
