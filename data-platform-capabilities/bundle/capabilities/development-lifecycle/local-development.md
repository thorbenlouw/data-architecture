---
type: Capability
id: local-development
title: IDE and local development
description: Develop in your own editor and run against the platform, with debugging and local tests.
aliases: [IDE integration, CLI]
broader: [development-lifecycle]
related: [notebooks, version-control, data-testing, single-node-processing, secrets-management]
depends_on: [identity-authentication, sql-access]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Engineers work in a desktop IDE or terminal editor and run code against the platform through a command-line tool, an SDK or a remote connection. Typical patterns are running a SQL model against a personal development schema from the editor, stepping through a PySpark job in a debugger while the heavy work runs on a remote cluster, and running unit tests on a small in-process engine such as DuckDB or local Spark before pushing. Platform extensions add completion from the catalogue, so table and column names are checked as you type.

This is where most software-style engineering happens: refactoring across files, linting, type checks, pre-commit hooks and tests that finish in seconds. It matters most for shared libraries, pipelines and infrastructure code that will be maintained for years. The main difficulty is parity. Local engines, library versions and permissions differ from production, so code that passes locally can fail on the platform. Pinned environments and development containers narrow the gap.

# Key considerations

- Pin language, library and engine versions so local and platform runtimes match, ideally in a shared development container definition.
- Credentials used from laptops should be short-lived and tied to the person's identity, not long-lived keys kept in config files.
- Decide what data may be pulled to a laptop. Local tests should use small synthetic or masked samples, not production extracts.
- Dialect and function differences between a local engine and the platform can hide bugs. Run at least one stage of tests on the real engine.

# Questions to ask

- Do engineers need step-through debugging and local tests, or is a browser workspace enough?
- Which editors and operating systems must be supported?
- What data, if any, may developers hold on their own machines?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [Data pipeline testing](data-testing.md), [Notebooks](notebooks.md), [Secrets management](../security/secrets-management.md), [Single-node processing](../processing/single-node-processing.md), [Version control integration](version-control.md) |
| Depends on | [Identity and authentication](../security/identity-authentication.md), [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Studio](../../technologies/aws/aws-sagemaker-studio.md), [Kiro](../../technologies/aws/aws-kiro.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric MCP server](../../technologies/microsoft/fabric-mcp-server.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Data Agent Kit](../../technologies/google-cloud/gcp-data-agent-kit.md) (preview) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake CLI](../../technologies/snowflake/snowflake-cli.md), [Snowflake Extension for Visual Studio Code](../../technologies/snowflake/snowflake-vscode-extension.md) (preview), [Snowsight Workspaces](../../technologies/snowflake/snowflake-workspaces.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Connect](../../technologies/databricks/databricks-connect.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [chDB](../../technologies/clickhouse/clickhouse-chdb.md), [clickhouse-local](../../technologies/clickhouse/clickhouse-local.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS 9.4 and SAS Enterprise Guide](../../technologies/sas/sas-9.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Code Studios | [Dataiku Code Studios](../../technologies/dataiku/dataiku-code-studios.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt v2 engine](../../technologies/independent/dbt-fusion-engine.md) |
