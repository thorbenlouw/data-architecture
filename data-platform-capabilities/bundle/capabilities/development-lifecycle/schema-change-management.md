---
type: Capability
id: schema-change-management
title: Schema change management
description: Version and apply database schema changes through controlled migrations.
aliases: [database migrations, declarative change management]
broader: [development-lifecycle]
related: [schema-evolution, impact-analysis, data-contracts, ci-cd, database-migration]
depends_on: [version-control]
tags: [development-lifecycle]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

There are two common styles. In the migration style, each change, such as a new table, an added column or a new constraint, is a numbered script kept in Git, and a tool records which scripts have run in each database so it applies only the missing ones in order. In the declarative style, you describe the desired schema and the tool compares it with the live database, generates the statements needed and shows a plan before applying it. Either way, the same changes run identically in development, test and production.

This stops environments drifting apart and turns schema changes into reviewed, repeatable releases rather than DDL typed by hand. The hard cases are destructive or expensive changes, such as dropping a column that consumers use or rewriting a large table. The safe practice is expand and contract: add the new structure, move consumers to it, then remove the old one. Schema evolution concerns how a table accepts structural change; this capability concerns how changes are planned, reviewed and applied.

# Key considerations

- Check for breaking changes automatically before release, using lineage to find consumers of a dropped or renamed column.
- Declarative tools are easier to write for but can generate destructive statements. Review the plan before it runs in production.
- Some changes rewrite whole tables. Estimate time and cost for large tables and schedule them outside critical windows.
- Detect drift, meaning changes made directly in an environment outside the process, and either import or reverse them.

# Questions to ask

- How are schema changes applied to production today, and by whom?
- How do consumers learn about a breaking change before it happens?
- Have environments drifted apart, and how would you find out?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Development and DataOps](development-lifecycle.md) |
| Broader | [Development and DataOps](development-lifecycle.md) |
| Related | [CI/CD](ci-cd.md), [Data contracts](../data-products/data-contracts.md), [Data modelling and design](data-modelling.md), [Data product lifecycle management](../data-products/data-product-lifecycle.md), [Database migration](../platform-operations/database-migration.md), [Impact analysis](../metadata/impact-analysis.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Schema enforcement and evolution](../storage/schema-evolution.md), [Schema registry](../metadata/schema-registry.md) |
| Depends on | [Version control integration](version-control.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 2)
- **Patterns:** [Shift-left data quality and governance](../../patterns/shift-left.md)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Modelling and Design

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | DCM Projects (Database Change Management) | [Snowflake DCM Projects](../../technologies/snowflake/snowflake-dcm-projects.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Flyway Community](../../technologies/open-source/flyway.md), [Liquibase Community](../../technologies/open-source/liquibase.md) |
