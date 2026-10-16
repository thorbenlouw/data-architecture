---
type: Capability
id: usage-metadata
title: Usage and popularity metadata
description: Show who uses which data, how often and how, to guide discovery and clean-up.
broader: [data-catalogue]
related: [audit-logging, cost-optimisation, impact-analysis, data-certification]
depends_on: [system-telemetry]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Usage metadata is gathered from query logs, BI activity and access logs. It records which tables and columns are queried, by which users and tools, how often, with which joins and filters, and which dashboards are opened. It is summarised on each catalogue page as popularity, frequent users, common queries and date last used. For example, a search for orders ranks the table used by 400 people above six similarly named copies and shows the five queries most often run against it.

Usage signals improve search ranking, help newcomers learn from colleagues' queries, point to real experts and owners, and reveal unused tables that can be archived to save storage. They also indicate importance: a table with many active consumers needs more care before it changes. Audit logging and cost attribution draw on the same raw logs but serve different purposes, security evidence and charging respectively, whereas usage metadata is for discovery and clean-up.

# Key considerations

- Query text can contain sensitive literal values. Mask or restrict it before showing it in the catalogue.
- Showing named users' activity may raise privacy or employee-representation concerns. Aggregate where needed.
- Pipelines and service accounts dominate raw counts. Separate human, BI and automated usage.
- Usage in tools outside the platform, such as BI extracts and spreadsheets, is invisible unless those tools report it.

# Questions to ask

- Are query logs available for the main platforms and BI tools, and for how long are they kept?
- Is there a goal to retire unused data or reduce storage cost?
- May individual users' activity be shown to colleagues?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [Access requests and reviews](../security/access-requests.md), [Audit logging](../security/audit-logging.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Cost optimisation](../platform-operations/cost-optimisation.md), [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [Data certification](data-certification.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data product usage metering](../data-products/data-product-metering.md), [Data security posture management](../security/data-security-posture.md), [Governance coverage metrics](../governance/governance-metrics.md), [Impact analysis](impact-analysis.md), [Platform migration](../platform-operations/platform-migration.md), [Table-level lineage](table-lineage.md), [Usage and system telemetry](../platform-operations/system-telemetry.md) |
| Depends on | [Usage and system telemetry](../platform-operations/system-telemetry.md) |
| Needed by | [Data product lifecycle management](../data-products/data-product-lifecycle.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 14 Cost Metrics (Data and technical architecture) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Metadata Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Access History](../../technologies/snowflake/snowflake-access-history.md), [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../../technologies/snowflake/snowflake-account-usage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Catalog Explorer](../../technologies/databricks/databricks-catalog-explorer.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Select Star](../../technologies/independent/select-star.md) |
