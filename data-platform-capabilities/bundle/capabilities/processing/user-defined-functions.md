---
type: Capability
id: user-defined-functions
title: User-defined functions and procedures
description: Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
aliases: [UDFs, stored procedures]
broader: [processing]
related: [dataframe-apis, ai-functions, compute-user-isolation, column-lineage, secrets-management]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

User-defined functions (UDFs) add custom logic that queries call like built-in functions. A scalar UDF returns one value per row, such as `parse_vin(code)`; an aggregate UDF combines many rows into one value; a table function returns a set of rows. Stored procedures go further, running multi-step logic with variables, loops and transactions. They can be written in SQL or in languages such as Python, Java or JavaScript, which the engine runs in a sandbox next to the data.

UDFs let teams reuse logic that SQL lacks, such as parsing a proprietary format, applying a scoring library or calling an external service, without exporting data. The price is speed and visibility. Non-SQL UDFs are opaque to the optimiser, may pass data between engine and language runtime one row at a time, and hide logic from lineage tools. Vectorised UDFs, which receive batches of rows, cut that overhead. External functions that call a remote endpoint add network delay and need rate limiting.

# Key considerations

- Use vectorised or batch UDFs rather than row-at-a-time ones for any real volume.
- Keep UDFs in version control with tests, and treat shared ones as libraries with named owners.
- Check what a UDF can reach, such as the network, files or secrets. Sandboxing and outbound network rules matter for security.
- Lineage and masking policies may not see inside a UDF. Avoid hiding business rules there that must be audited.
- Pin the library versions that language UDFs use so results stay reproducible.

# Questions to ask

- What logic do teams currently export data to run somewhere else?
- Which languages and libraries must run inside the engine?
- Do functions need to call external services, and under what network controls?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [AI functions in SQL](ai-functions.md), [Batch inference](../mlops/batch-inference.md), [Column-level lineage](../metadata/column-lineage.md), [DataFrame APIs](dataframe-apis.md), [In-database machine learning](../machine-learning/in-database-ml.md), [Secrets management](../security/secrets-management.md), [Shared compute isolation](../security/compute-user-isolation.md) |

# Where it appears

- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric user data functions](../../technologies/microsoft/fabric-user-data-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery user-defined functions](../../technologies/google-cloud/gcp-bigquery-udfs.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake user-defined functions and stored procedures](../../technologies/snowflake/snowflake-udfs-and-procedures.md), [Snowpark](../../technologies/snowflake/snowflake-snowpark.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog functions (UDFs)](../../technologies/databricks/databricks-unity-catalog-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | UDFs (SQL and executable) | [ClickHouse user-defined functions](../../technologies/clickhouse/clickhouse-udfs.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata in-database analytics functions](../../technologies/teradata/teradata-in-database-analytics.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud for Apache Flink](../../technologies/ibm/confluent-cloud-flink.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache DataFusion](../../technologies/open-source/apache-datafusion.md), [Apache Spark](../../technologies/open-source/apache-spark.md) |
