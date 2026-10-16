---
type: Technology
id: snowflake-drivers-sql-api
title: Snowflake drivers, connectors and SQL API
description: JDBC, ODBC, Python, Go, .NET and Node.js drivers, the Spark connector and a REST SQL API for connecting tools and applications to Snowflake.
platform: platform-snowflake
kind: software
availability: ga
realises: [sql-access]
resource: https://docs.snowflake.com/en/developer-guide/drivers
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation) (primary): Connect tools and code to the platform through standard drivers and protocols.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric SQL analytics endpoint](../microsoft/fabric-sql-analytics-endpoint.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery](../google-cloud/gcp-bigquery.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks JDBC, ODBC and ADBC drivers](../databricks/databricks-sql-drivers.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse interfaces and client drivers](../clickhouse/clickhouse-clients.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [ADBC (Arrow Database Connectivity)](../open-source/apache-arrow-adbc.md), [Arrow Flight SQL](../open-source/apache-arrow-flight-sql.md), [Apache Kyuubi](../open-source/apache-kyuubi.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [MotherDuck](../independent/motherduck.md), [Cube Cloud](../independent/cube-cloud.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
