---
type: Technology
id: databricks-free-edition
title: Databricks Free Edition
description: A no-cost, serverless-only, quota-limited Databricks environment for learning and experiments. It includes notebooks, SQL, Lakeflow, dashboards, Genie, Genie Code and Lakebase.
platform: platform-databricks
kind: saas
availability: ga
realises: [serverless-compute, notebooks]
resource: https://docs.databricks.com/aws/en/getting-started/free-edition
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It replaced Community Edition, which was retired in 2025. It is not for production or commercial use, and architects meet it mainly in training and proofs of concept.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute) (primary): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Notebooks](../../capabilities/development-lifecycle/notebooks.md) (Development and DataOps): Develop interactively with code, results and narrative together, with collaboration and scheduling.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Cloud Run](../google-cloud/gcp-cloud-run.md), [BigQuery](../google-cloud/gcp-bigquery.md) | [Notebooks](../../capabilities/development-lifecycle/notebooks.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md), [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Cloud](../teradata/teradata-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [MotherDuck](../independent/motherduck.md), [Prefect Cloud](../independent/prefect-cloud.md) | [Serverless compute](../../capabilities/compute/serverless-compute.md) |
