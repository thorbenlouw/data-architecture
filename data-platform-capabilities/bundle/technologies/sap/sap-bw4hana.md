---
type: Technology
id: sap-bw4hana
title: SAP BW/4HANA
description: SAP's on-premises data warehouse application on SAP HANA, with modelled InfoProviders, extractors for SAP sources and query design for BI.
aliases: [BW/4HANA, SAP BW, SAP Business Warehouse]
platform: platform-sap
kind: software
availability: ga
realises: [sql-transformation, semantic-layer, saas-connectors]
resource: https://www.sap.com/products/data-cloud/business-warehouse.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Successor to SAP BW 7.5, including BW on HANA, and still common in SAP estates. SAP's direction is BW in BDC and Datasphere. BW 7.5 reaches the end of mainstream maintenance at the end of 2027, which drives many migration plans.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation) (primary): Transform data inside the platform using SQL, typically after it has been loaded.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Warehouse

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
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview) | [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
