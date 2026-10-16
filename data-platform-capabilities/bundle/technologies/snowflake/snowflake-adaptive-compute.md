---
type: Technology
id: snowflake-adaptive-compute
title: Snowflake Adaptive Compute
description: A warehouse type (adaptive warehouses) for which Snowflake decides the resources for each query, so you do not set a size, multi-cluster settings or suspend policies.
platform: platform-snowflake
kind: feature
availability: ga
realises: [serverless-compute, elastic-scaling, workload-management]
resource: https://docs.snowflake.com/en/user-guide/warehouses-adaptive
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Became generally available on 16 June 2026 for Enterprise Edition and above, in selected regions. Two settings give control: MAX_QUERY_PERFORMANCE_LEVEL and QUERY_THROUGHPUT_MULTIPLIER. Billing is per query and runs on a compute pool dedicated to the account. Existing standard warehouses convert online. Snowflake does not recommend it for HTAP, very low-latency or single-node high-memory workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake warehouses

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md), [BigQuery](../google-cloud/gcp-bigquery.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md), [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md), [Prefect Cloud](../independent/prefect-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
