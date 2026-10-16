---
type: Technology
id: apache-kyuubi
title: Apache Kyuubi
description: Multi-tenant SQL gateway that gives JDBC, ODBC and REST clients shared, authenticated access to Spark, Flink, Trino and other engines.
aliases: [Kyuubi]
platform: platform-open-source
kind: open-source
availability: ga
realises: [sql-access, workload-isolation, multi-tenancy]
resource: https://kyuubi.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0. Often used as the open-source replacement for the Spark Thrift Server, with per-user or per-group engine isolation and integration with Ranger and Kerberos.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation) (primary): Connect tools and code to the platform through standard drivers and protocols.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake drivers, connectors and SQL API](../snowflake/snowflake-drivers-sql-api.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks JDBC, ODBC and ADBC drivers](../databricks/databricks-sql-drivers.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse interfaces and client drivers](../clickhouse/clickhouse-clients.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MotherDuck](../independent/motherduck.md), [Denodo Platform](../independent/denodo-platform.md), [Cube Cloud](../independent/cube-cloud.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md), [Workload isolation](../../capabilities/compute/workload-isolation.md) |
