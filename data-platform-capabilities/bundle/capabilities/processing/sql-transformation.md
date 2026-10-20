---
type: Capability
id: sql-transformation
title: SQL transformation
description: Transform data inside the platform using SQL, typically after it has been loaded.
aliases: [ELT, in-warehouse transformation]
broader: [processing]
related: [materialised-views, incremental-processing, idempotent-loading, code-translation, data-modelling]
depends_on: [sql-query-engine]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The platform's own engine runs SELECT, INSERT, MERGE and CREATE TABLE AS statements to turn raw loaded tables into cleaned, joined and aggregated ones. For example, order lines and customer records land unchanged; a sequence of SQL statements removes duplicates, converts currencies, joins customers and writes a daily sales table. Because the data is already loaded, this is the "T" in ELT: the system that stores the data also does the work, with its own parallelism, optimiser and access controls.

SQL is the language most data people share, which makes this the default for relational shaping: joins, filters, aggregations, window functions and slowly changing dimensions. It is weaker for procedural logic, calls to external services and machine learning. Plain scripts run by a scheduler are the simplest form. Transformation as code adds modular models, dependency ordering and tests on top. Stored procedures are an older option that mixes SQL with loops and variables.

# Key considerations

- Dialects differ in MERGE behaviour, date functions, NULL handling and access to nested data. SQL written for one engine rarely runs unchanged on another.
- Long chains of views are easy to write and slow to query. Decide deliberately which steps are stored as tables and which stay as views.
- Use MERGE or partition overwrite rather than plain INSERT so a rerun does not duplicate rows.
- Review query cost as well as correctness. One badly written join can dominate the compute bill.

# Questions to ask

- How well does the team know SQL, and in which dialect?
- How much of the logic needs procedural steps, external calls or models that SQL handles poorly?
- How are SQL changes reviewed, tested and deployed today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Narrower | [Transformation as code](transformation-as-code.md) |
| Related | [Code and SQL translation](../platform-operations/code-translation.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [DataFrame APIs](dataframe-apis.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Incremental processing](incremental-processing.md), [Low-code transformation](low-code-transformation.md), [Materialised views](../compute/materialised-views.md), [SQL query engine](../compute/sql-query-engine.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md) |

# Where it appears

- **Use cases:** [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Data Vault](../../patterns/data-vault.md) · [Data warehouse](../../patterns/data-warehouse.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md) · [ELT](../../patterns/elt.md) · [Medallion architecture](../../patterns/medallion-architecture.md) · [One big table](../../patterns/one-big-table.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 1, Initial)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift](../../technologies/aws/aws-redshift.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Dynamic Tables](../../technologies/snowflake/snowflake-dynamic-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks SQL](../../technologies/databricks/databricks-sql.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse incremental materialized views](../../technologies/clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../../technologies/clickhouse/clickhouse-refreshable-materialized-views.md) |
| [Informatica](../../platforms/platform-informatica.md) | SQL ELT mode | [Informatica Cloud Data Integration SQL ELT mode](../../technologies/informatica/informatica-cdi-sql-elt-mode.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data product studio](../../technologies/sap/sap-bdc-data-product-studio.md) (unconfirmed), [SAP Business Warehouse in SAP Business Data Cloud](../../technologies/sap/sap-business-warehouse-bdc.md), [SAP BW/4HANA](../../technologies/sap/sap-bw4hana.md), [SAP Datasphere](../../technologies/sap/sap-datasphere.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data and AI Studio](../../technologies/sas/sas-data-and-ai-studio.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku code recipes and notebooks](../../technologies/dataiku/dataiku-code-recipes-notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Spark](../../technologies/open-source/apache-spark.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Lake Compute](../../technologies/independent/dbt-lake-compute.md) (preview), [Matillion Maia Foundation](../../technologies/independent/matillion-maia-foundation.md) |

Narrower capabilities are realised by a further 11 technologies; see their pages.
