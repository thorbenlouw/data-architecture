---
type: Technology
id: sap-business-warehouse-bdc
title: SAP Business Warehouse in SAP Business Data Cloud
description: Hosted SAP BW in BDC whose Data Product Generator turns BW InfoProvider data into data products in the BDC object store for Datasphere and Databricks to use.
aliases: [SAP BW in BDC]
platform: platform-sap
kind: managed-service
availability: ga
realises: [sql-transformation, internal-data-sharing, deployment-options, platform-migration]
resource: https://www.sap.com/products/data-cloud/business-warehouse.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Intended as the route off on-premises BW without a full rebuild; data is exposed through Delta Sharing. Builds on the BW private cloud edition offered with RISE with SAP. SAP BW bridge in Datasphere is the alternative for moving BW logic into Datasphere.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation) (primary): Transform data inside the platform using SQL, typically after it has been loaded.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud, SAP Business Warehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md), [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration SQL ELT mode](../informatica/informatica-cdi-sql-elt-mode.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Spark](../open-source/apache-spark.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
