---
type: Capability
id: sql-access
title: SQL and programmatic access
description: Connect tools and code to the platform through standard drivers and protocols.
aliases: [JDBC, ODBC, Arrow Flight SQL, SQL endpoints]
broader: [serving]
related: [data-apis, identity-authentication, spreadsheet-integration, ad-hoc-analysis, audit-logging]
depends_on: [sql-query-engine]
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The usual interfaces are JDBC and ODBC drivers, native connectors for Python and other languages, HTTP-based SQL APIs, and wire protocols compatible with common databases such as PostgreSQL. Apache Arrow and its Flight protocol return results in columnar form, which is far faster for large result sets than row-by-row drivers. A data scientist opens a notebook, signs in through single sign-on, runs a query and receives millions of rows as a DataFrame.

This is how most people and tools reach the platform, so driver quality and protocol support decide which tools work at all. Platforms differ in authentication options (single sign-on, OAuth, key pairs, short-lived tokens), result transfer speed, support for parameterised and asynchronous queries, and how long-running queries behave. Data APIs suit applications making fixed, predictable requests; SQL access suits flexible queries from people and analytical tools.

# Key considerations

- Check that drivers support the organisation's authentication methods, especially single sign-on and token-based service accounts.
- Large result sets are slow through row-based ODBC and JDBC drivers. Prefer columnar transfer for data science and extracts.
- Pass the end user's identity through tool connections. Shared service accounts in BI tools hide who ran what and weaken access control.
- Pin and test driver versions. Upgrades can change type mappings or behaviour in subtle ways.

# Questions to ask

- Which tools and languages must connect, and which drivers or protocols do they support?
- How will users and services authenticate, and can the end user's identity be passed through?
- How large are the result sets typically pulled into tools and notebooks?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Audit logging](../security/audit-logging.md), [Data APIs](data-apis.md), [Identity and authentication](../security/identity-authentication.md), [Spreadsheet integration](../analytics-bi/spreadsheet-integration.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md) |
| Needed by | [Analytics and BI](../analytics-bi/analytics-bi.md), [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [IDE and local development](../development-lifecycle/local-development.md), [Paginated reports](../analytics-bi/paginated-reports.md), [Spreadsheet integration](../analytics-bi/spreadsheet-integration.md) |

# Where it appears

- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 1, Initial)
- **Frameworks:** [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Infrastructures & Servers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric SQL analytics endpoint](../../technologies/microsoft/fabric-sql-analytics-endpoint.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake drivers, connectors and SQL API](../../technologies/snowflake/snowflake-drivers-sql-api.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks JDBC, ODBC and ADBC drivers](../../technologies/databricks/databricks-sql-drivers.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse interfaces and client drivers](../../technologies/clickhouse/clickhouse-clients.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [ADBC (Arrow Database Connectivity)](../../technologies/open-source/apache-arrow-adbc.md), [Apache Kyuubi](../../technologies/open-source/apache-kyuubi.md), [Arrow Flight SQL](../../technologies/open-source/apache-arrow-flight-sql.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Cube Cloud](../../technologies/independent/cube-cloud.md), [Denodo Platform](../../technologies/independent/denodo-platform.md), [MotherDuck](../../technologies/independent/motherduck.md) |
