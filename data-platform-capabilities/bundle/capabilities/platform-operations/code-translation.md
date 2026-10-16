---
type: Capability
id: code-translation
title: Code and SQL translation
description: Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.
aliases: [SQL transpilation, dialect translation]
broader: [platform-migration]
related:
- sql-transformation
- data-testing
- data-reconciliation
- ai-assisted-development
- low-code-transformation
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical inputs are SQL in a legacy dialect, stored procedures with loops and cursors, scripts for bulk-load utilities, and job definitions exported from graphical ETL tools. A translator parses the code into a syntax tree, maps functions, data types and statements to their nearest equivalents in the target, and reports what it could not convert. A proprietary date function becomes the target's equivalent, for example, and a cursor loop may be rewritten as a single set-based statement. Open-source transpilers such as SQLGlot handle many common SQL dialects.

Translation saves months of manual rewriting but rarely converts a complex estate completely. Differences in NULL handling, implicit type conversion, collation, rounding and transaction behaviour mean converted code can run and still give different answers, so every translated object must be checked against the old system. Language models increasingly handle cases rule-based tools cannot, with less predictable output. Database migration moves schemas and data; code translation moves the logic.

# Key considerations

- Measure conversion rates per object and per business-critical path, not only overall. A 95% rate can leave the hardest 5% blocking the migration.
- Validate translated code by running it on the same inputs on both platforms and comparing results.
- Literal translation carries over legacy patterns, such as row-by-row procedural logic, that run slowly on the target. Flag these for redesign.
- Keep translation repeatable, so code changed in the legacy system during the migration can be converted again.

# Questions to ask

- Which languages and dialects make up the code estate, and how much is stored procedures or graphical ETL?
- How much of the code is still in use, and how much will change during the migration?
- Who will review and fix the code the tool cannot convert?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform migration](platform-migration.md) |
| Related | [AI-assisted development](../development-lifecycle/ai-assisted-development.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Database migration](database-migration.md), [Low-code transformation](../processing/low-code-transformation.md), [Mainframe data integration](../ingestion-integration/mainframe-integration.md), [SQL transformation](../processing/sql-transformation.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3)
- **Maturity tracks:** [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Database Migration Service](../../technologies/aws/aws-dms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Migration Service](../../technologies/google-cloud/gcp-bigquery-migration-service.md), [Google Cloud Database Migration Service](../../technologies/google-cloud/gcp-database-migration-service.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [SnowConvert AI](../../technologies/snowflake/snowflake-snowconvert-ai.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks agentic code converter](../../technologies/databricks/databricks-agentic-code-converter.md) (preview), [Lakebridge](../../technologies/databricks/databricks-lakebridge.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica PowerCenter Cloud Edition (PCCE)](../../technologies/informatica/informatica-powercenter-cloud-edition.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [SQLMesh](../../technologies/open-source/sqlmesh.md) |
