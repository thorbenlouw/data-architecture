---
type: Technology
id: databricks-sql-warehouses
title: Databricks SQL warehouses (serverless, pro and classic)
description: Compute for Databricks SQL in serverless, pro or classic form. Serverless warehouses start in seconds and use intelligent workload management to scale and queue queries.
formerly: [SQL endpoints]
platform: platform-databricks
kind: managed-service
availability: ga
realises:
- serverless-compute
- elastic-scaling
- workload-management
- result-caching
- workload-isolation
- hybrid-data-plane
resource: https://docs.databricks.com/aws/en/compute/sql-warehouse/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pro and classic warehouses run in the customer's cloud account and suit cases where serverless is unavailable or private networking needs it. Separate warehouses isolate workloads, and sizes go up to 5X-Large, which is in Public Preview for pro and serverless warehouses.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
- [Result caching](../../capabilities/compute/result-caching.md) (Query and compute): Return results of repeated queries from a cache without recomputing them.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Databricks SQL, Databricks compute

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon Athena](../aws/aws-athena.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md), [Result caching](../../capabilities/compute/result-caching.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md), [BigQuery](../google-cloud/gcp-bigquery.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload management](../../capabilities/compute/workload-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md), [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MotherDuck](../independent/motherduck.md), [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [Prefect Cloud](../independent/prefect-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [Workload isolation](../../capabilities/compute/workload-isolation.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
