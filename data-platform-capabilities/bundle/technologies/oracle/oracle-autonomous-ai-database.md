---
type: Technology
id: oracle-autonomous-ai-database
title: Oracle Autonomous AI Database
description: Self-managing Oracle database service on OCI and other clouds that automates provisioning, patching, tuning, scaling and backups, offered as Lakehouse, Transaction Processing, JSON Database and APEX workload types.
aliases: [ADB, Autonomous AI Transaction Processing, Autonomous AI JSON Database]
formerly: [Oracle Autonomous Database, Autonomous Transaction Processing, Autonomous JSON Database]
platform: platform-oracle
kind: managed-service
availability: ga
realises:
- serverless-compute
- elastic-scaling
- managed-storage
- backup-restore
- cross-region-failover
- hybrid-data-plane
resource: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Workload types are Autonomous AI Lakehouse, Autonomous AI Transaction Processing, Autonomous AI JSON Database and APEX Service. Autonomous Data Guard provides cross-region standby databases. Available serverless or on dedicated Exadata infrastructure, including Exadata Cloud@Customer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management): Let the platform manage table storage layout, compression and durability internally.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.
- [Cross-region replication and failover](../../capabilities/platform-operations/cross-region-failover.md) (Platform operations): Replicate data and configuration to another region and fail over when needed.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle Autonomous AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md), [BigQuery](../google-cloud/gcp-bigquery.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks serverless compute](../databricks/databricks-serverless-compute.md), [Databricks Free Edition](../databricks/databricks-free-edition.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md), [Prefect Cloud](../independent/prefect-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
