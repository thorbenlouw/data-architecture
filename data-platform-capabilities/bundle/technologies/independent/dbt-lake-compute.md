---
type: Technology
id: dbt-lake-compute
title: dbt Lake Compute
description: Hosted serverless DuckDB-based compute that runs dbt models directly against Apache Iceberg tables, either alongside a warehouse or as a project's main engine.
platform: platform-independent
vendor: Fivetran + dbt Labs
kind: managed-service
availability: preview
realises: [serverless-compute, single-node-processing, sql-transformation]
resource: https://docs.getdbt.com/docs/lake-compute
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Private beta. Requires dbt v2 and runs only in AWS us-east-1 and us-west-2. In sidecar mode, each model can run either on Lake Compute or on Snowflake (Databricks for design partners) in one DAG, to move cheaper workloads off the warehouse. Not yet supported are views, BI connections, distributed execution and large two-sided joins.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation): Process small to medium datasets quickly on one machine using in-process engines.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md), [BigQuery](../google-cloud/gcp-bigquery.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Free Edition](../databricks/databricks-free-edition.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md), [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md), [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
