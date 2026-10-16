---
type: Capability
id: impact-analysis
title: Impact analysis
description: Use lineage to find everything affected by a proposed change or a data incident.
aliases: [root cause analysis]
broader: [data-lineage]
related: [schema-change-management, data-contracts, data-issue-management, usage-metadata, ci-cd]
depends_on: [table-lineage]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Impact analysis starts from an asset and a proposed change, such as dropping a column, changing a definition or delaying a feed, or from an incident. It walks the lineage graph downstream to list affected tables, data products, dashboards, ML models and their owners, and upstream to find possible causes. For example, before renaming `cust_type` in a CRM extract, an engineer sees that two transformation models, a churn model and eleven dashboards with forty weekly viewers depend on it, and notifies their owners.

It turns lineage into decisions: avoiding broken consumers, scoping incidents and ranking fixes by business effect when combined with usage and criticality. It is used on demand in the catalogue, automatically in CI where a pull request shows what it would affect before merge, and during incidents to size the damage. Column lineage makes it precise; table lineage alone tends to overstate impact. Root-cause analysis uses the same graph in the opposite direction.

# Key considerations

- Results are only as complete as lineage coverage. Missing BI or export lineage understates impact.
- Combine lineage with usage and criticality so results rank what matters rather than listing everything.
- Run it automatically in CI for schema changes and in incident tooling, not only on request.
- Notify affected owners through their usual channels, not only inside the catalogue.

# Questions to ask

- How often do changes break downstream reports or models unexpectedly?
- Is there a review step for schema changes today?
- Who needs to be told when an upstream asset changes?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md) |
| Related | [CI/CD](../development-lifecycle/ci-cd.md), [Column-level lineage](column-lineage.md), [Critical data elements](../governance/critical-data-elements.md), [Dashboards as code](../analytics-bi/dashboards-as-code.md), [Data contracts](../data-products/data-contracts.md), [Data issue management](../data-quality/data-issue-management.md), [Data observability](../data-quality/data-observability.md), [Data product lifecycle management](../data-products/data-product-lifecycle.md), [End-to-end lineage](cross-system-lineage.md), [Event and API catalogue](event-api-catalogue.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Platform migration](../platform-operations/platform-migration.md), [Schema change management](../development-lifecycle/schema-change-management.md), [Schema enforcement and evolution](../storage/schema-evolution.md), [Usage and popularity metadata](usage-metadata.md) |
| Depends on | [Table-level lineage](table-lineage.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 3)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data architect](../../personas/persona-data-architect.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 3, Defined)
- **Frameworks:** [DCAM v3](../../frameworks/framework-edm-dcam.md): 5 Data Quality Management · [GDPR](../../frameworks/framework-gdpr.md): Article 19 – Notification to recipients

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog data lineage](../../technologies/aws/aws-sagemaker-catalog-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data lineage in Microsoft Purview](../../technologies/microsoft/purview-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data lineage](../../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data lineage (Snowsight lineage)](../../technologies/snowflake/snowflake-data-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog data lineage](../../technologies/databricks/databricks-unity-catalog-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC lineage](../../technologies/informatica/informatica-cdgc-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Lineage](../../technologies/cloudera/cloudera-data-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Manta Data Lineage](../../technologies/ibm/ibm-manta-data-lineage.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Lineage](../../technologies/palantir/palantir-data-lineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Lineage](../../technologies/independent/collibra-data-lineage.md), [dbt Catalog](../../technologies/independent/dbt-catalog.md), [Monte Carlo Data + AI Observability](../../technologies/independent/monte-carlo-data-observability.md), [Solidatus](../../technologies/independent/solidatus.md) |
