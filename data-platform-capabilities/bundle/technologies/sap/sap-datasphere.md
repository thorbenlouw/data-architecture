---
type: Technology
id: sap-datasphere
title: SAP Datasphere
description: SAP's cloud data warehouse and data fabric service for integrating, modelling, federating and governing SAP and non-SAP data in isolated spaces with business semantics.
formerly: [SAP Data Warehouse Cloud, DWC]
platform: platform-sap
kind: saas
availability: ga
realises:
- sql-transformation
- semantic-layer
- query-federation
- multi-tenancy
- low-code-transformation
- platform-migration
- row-level-security
- workflow-orchestration
- data-modelling
resource: https://www.sap.com/products/data-cloud/datasphere.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data Builder handles entity-relationship models, views, data flows, transformation flows and task chains; Business Builder adds business entities and analytic models; data access controls give row-level security. Runs on SAP HANA Cloud. Sold on its own and as part of BDC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation) (primary): Transform data inside the platform using SQL, typically after it has been loaded.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.
- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Data modelling and design](../../capabilities/development-lifecycle/data-modelling.md) (Development and DataOps): Design and document conceptual, logical and physical data models, and keep them in step with what is deployed.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud, SAP Datasphere

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md), [ClickHouse incremental materialized views](../clickhouse/clickhouse-materialized-views.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration SQL ELT mode](../informatica/informatica-cdi-sql-elt-mode.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Spark](../open-source/apache-spark.md) | [SQL transformation](../../capabilities/processing/sql-transformation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [dbt Lake Compute](../independent/dbt-lake-compute.md) (preview) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [SQL transformation](../../capabilities/processing/sql-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
