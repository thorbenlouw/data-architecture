---
type: Technology
id: informatica-cdi-sql-elt-mode
title: Informatica Cloud Data Integration SQL ELT mode
description: Converts mapping logic into native SQL and platform commands that run inside the target cloud warehouse, so data does not leave the warehouse's cloud while it is transformed.
platform: platform-informatica
kind: feature
availability: ga
realises: [sql-transformation, low-code-transformation]
resource: https://onlinehelp.informatica.com/IICS/prod/CDI/en/hh-cloud-mappings/Mappings_in_SQL_ELT_mode.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Targets are Snowflake, Databricks, Google BigQuery, Amazon Redshift and Microsoft Fabric Data Warehouse, each with a limited set of sources in the same cloud. Only transformations the target can execute are available, and you cannot test-run these mappings in the designer. This is a newer design mode than the older pushdown optimisation option on standard mappings.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation) (primary): Transform data inside the platform using SQL, typically after it has been loaded.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Datasphere](../sap/sap-datasphere.md), [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Spark](../open-source/apache-spark.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
