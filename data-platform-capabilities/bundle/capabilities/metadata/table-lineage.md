---
type: Capability
id: table-lineage
title: Table-level lineage
description: Track dependencies between datasets, tables and views.
aliases: [dataset lineage, coarse-grained lineage]
broader: [data-lineage]
related: [transformation-as-code, workflow-orchestration, asset-based-orchestration, usage-metadata]
depends_on: [metadata-harvesting]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Table-level lineage records which datasets each dataset reads from and writes to, and which job or query does the work. It is derived from SQL parsing of source and target tables, from engine query logs, from orchestrator and transformation project definitions, or from run-time events. For example, the daily sales table is built from orders, customers and an exchange-rate table by one transformation model, and three dashboards and an export job read from it.

This level of detail is enough for most impact analysis, incident triage and pipeline scheduling, and it is cheaper and more complete to capture than column lineage. Transformation-as-code tools produce it from their dependency graph, and engines produce it from query history. Its limit is precision: it shows that one table depends on another but not on which columns, so a change to one column flags every downstream asset. Views, temporary tables and dynamic SQL are common blind spots.

# Key considerations

- Capture from query logs covers scheduled and ad hoc work alike but misses processing outside the engine.
- Temporary and staging tables clutter the graph. Collapse them in the default view.
- Separate reads from derivations. An ad hoc query that reads a table is usage, not lineage.
- Record the job or model that creates each edge so owners can be found during incidents.

# Questions to ask

- Can every transformation tool report the tables it reads and writes?
- Is table-level detail enough for impact analysis, or are column-level changes common?
- How far back must lineage history be kept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md) |
| Related | [Orchestration](../orchestration/orchestration.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Metadata harvesting](metadata-harvesting.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Transformation as code](../processing/transformation-as-code.md), [Usage and popularity metadata](usage-metadata.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Metadata harvesting](metadata-harvesting.md) |
| Needed by | [Data trust indicators](data-trust-indicators.md), [Impact analysis](impact-analysis.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2)
- **Patterns:** [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 13 Data Lineage (Data and technical architecture)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog data lineage](../../technologies/aws/aws-sagemaker-catalog-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data lineage in Microsoft Purview](../../technologies/microsoft/purview-lineage.md), [Fabric materialized lake views](../../technologies/microsoft/fabric-materialized-lake-views.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data lineage](../../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data lineage (Snowsight lineage)](../../technologies/snowflake/snowflake-data-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog data lineage](../../technologies/databricks/databricks-unity-catalog-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC lineage](../../technologies/informatica/informatica-cdgc-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Catalog](../../technologies/cloudera/cloudera-data-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere catalog and Data Marketplace](../../technologies/sap/sap-datasphere-catalog.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Lineage](../../technologies/palantir/palantir-data-lineage.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Atlas](../../technologies/open-source/apache-atlas.md), [Dagster](../../technologies/open-source/dagster.md), [dbt Core (v1.x)](../../technologies/open-source/dbt-core.md), [Marquez](../../technologies/open-source/marquez.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Lineage](../../technologies/independent/collibra-data-lineage.md), [dbt Catalog](../../technologies/independent/dbt-catalog.md) |
