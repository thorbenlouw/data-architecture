---
type: Capability
id: column-lineage
title: Column-level lineage
description: Track how each column is derived from source columns.
aliases: [field-level lineage, attribute lineage]
broader: [data-lineage]
related: [impact-analysis, data-classification, critical-data-elements, cross-system-lineage]
depends_on: [metadata-harvesting]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Column-level lineage records, for each column, the source columns and logic that produced it. For example, `net_revenue` in a sales mart is `gross_amount` minus `discount_amount` from the orders table, after refunded orders are excluded, while `customer_region` passes through unchanged from customers. Good implementations also separate direct derivation, where a value is computed from a source column, from indirect influence, where a column only affects the result through a filter or join.

It is derived by parsing SQL and DataFrame code into logical plans, or by instrumenting the engine while jobs run. Parsing works before code runs but struggles with dynamic SQL and user-defined functions; run-time capture is accurate but covers only jobs that have executed. Column detail is what privacy teams need to follow personal data, what regulators expect for critical data elements, and what makes impact analysis precise enough to trust. Table-level lineage would flag every consumer of a table; column lineage flags only those using the changed field.

# Key considerations

- Check coverage for views, MERGE statements, user-defined functions, notebooks and SELECT *, not only CREATE TABLE AS SELECT.
- Distinguish direct from indirect lineage. Without the distinction, graphs suggest that every column depends on every other.
- Lineage can carry classifications downstream, so a column derived from personal data inherits the tag. Add rules for steps such as aggregation that remove the sensitivity.
- Graphs grow quickly. Users need filtering by depth, domain and time.

# Questions to ask

- Which obligations require you to show how specific fields were derived?
- Do privacy teams need to track personal data at field level?
- Which engines and tools in the estate can report column lineage?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md) |
| Related | [Critical data elements](../governance/critical-data-elements.md), [Data classification](../governance/data-classification.md), [End-to-end lineage](cross-system-lineage.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Impact analysis](impact-analysis.md), [Merge and survivorship](../master-data/survivorship.md), [Regulatory submission](../serving/regulatory-submission.md), [User-defined functions and procedures](../processing/user-defined-functions.md) |
| Depends on | [Metadata harvesting](metadata-harvesting.md) |
| Needed by | [Critical data elements](../governance/critical-data-elements.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 3 – Accuracy and integrity · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 6 Classification (Cataloguing and classification); 13 Data Lineage (Data and technical architecture)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data lineage in Microsoft Purview](../../technologies/microsoft/purview-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data lineage](../../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data lineage (Snowsight lineage)](../../technologies/snowflake/snowflake-data-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog data lineage](../../technologies/databricks/databricks-unity-catalog-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC lineage](../../technologies/informatica/informatica-cdgc-lineage.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Lineage](../../technologies/cloudera/cloudera-data-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Manta Data Lineage](../../technologies/ibm/ibm-manta-data-lineage.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Data Lineage](../../technologies/dataiku/dataiku-data-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md), [dbt OSS](../../technologies/open-source/dbt-oss.md), [OpenLineage](../../technologies/open-source/openlineage.md), [OpenMetadata](../../technologies/open-source/openmetadata.md), [SQLMesh](../../technologies/open-source/sqlmesh.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Atlan](../../technologies/independent/atlan.md), [Collibra Data Lineage](../../technologies/independent/collibra-data-lineage.md), [dbt Catalog](../../technologies/independent/dbt-catalog.md), [dbt v2 engine](../../technologies/independent/dbt-fusion-engine.md), [Select Star](../../technologies/independent/select-star.md) |
