---
type: Technology
id: clickhouse-clients
title: ClickHouse interfaces and client drivers
description: HTTP, native TCP, gRPC and Arrow Flight interfaces, MySQL and PostgreSQL wire-protocol compatibility, and official clients including JDBC, ODBC, ADBC, Python, Go, Node.js, Rust, C++ and .NET.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [sql-access]
resource: https://clickhouse.com/docs/interfaces/overview
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Python client clickhouse-connect reached 1.0 in May 2026 and the .NET driver gained a native TCP client in October 2026 (experimental). The HTTP interface makes ClickHouse easy to call from serverless functions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation) (primary): Connect tools and code to the platform through standard drivers and protocols.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake drivers, connectors and SQL API](../snowflake/snowflake-drivers-sql-api.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks JDBC, ODBC and ADBC drivers](../databricks/databricks-sql-drivers.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [ADBC (Arrow Database Connectivity)](../open-source/apache-arrow-adbc.md), [Arrow Flight SQL](../open-source/apache-arrow-flight-sql.md), [Apache Kyuubi](../open-source/apache-kyuubi.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [MotherDuck](../independent/motherduck.md), [Cube Cloud](../independent/cube-cloud.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
