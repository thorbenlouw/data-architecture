---
type: Technology
id: apache-arrow-adbc
title: ADBC (Arrow Database Connectivity)
description: Database connectivity API and drivers, similar in purpose to JDBC and ODBC, that move query results as Arrow columnar data.
aliases: [ADBC, Arrow ADBC]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [sql-access]
resource: https://arrow.apache.org/adbc/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Apache Arrow. Drivers exist for PostgreSQL, SQLite, Snowflake, BigQuery, Flight SQL and others. dbt v2 uses ADBC for its adapters.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL and programmatic access](../../capabilities/serving/sql-access.md) (Serving and activation) (primary): Connect tools and code to the platform through standard drivers and protocols.

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
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [MotherDuck](../independent/motherduck.md), [Cube Cloud](../independent/cube-cloud.md) | [SQL and programmatic access](../../capabilities/serving/sql-access.md) |
