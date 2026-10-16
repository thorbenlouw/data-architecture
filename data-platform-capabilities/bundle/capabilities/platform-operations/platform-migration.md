---
type: Capability
id: platform-migration
title: Platform migration
description: Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
aliases: [modernisation tooling]
broader: [platform-operations]
related: [data-reconciliation, data-testing, impact-analysis, usage-metadata, bulk-data-transfer]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Migrations from an on-premises warehouse, a Hadoop cluster or an older cloud service usually run in phases. Assessment inventories databases, tables, code, jobs, users and dependencies and measures complexity. Conversion translates schemas, SQL and ETL logic. Data movement copies history and keeps it in sync. Validation compares results between old and new systems. Cut-over switches consumers, and decommissioning turns the old platform off. Tooling automates each phase, especially inventory, translation and comparison of results.

Migrations are long and risky because legacy platforms hold years of undocumented logic, and because both platforms must run, and be paid for, until the end. Approaches range from moving workloads as they are, to redesigning them in new patterns, to a mix chosen per workload. Moving as-is is faster but carries old design problems across. Automated validation, comparing row counts, totals and individual rows between old and new, is what gives business owners the confidence to switch off the old system.

# Key considerations

- Measure usage before converting. Much legacy code and data is unused and should be retired rather than migrated.
- Agree validation acceptance criteria up front, including how small numeric differences from different rounding and functions will be treated.
- Migrate in waves by domain or dependency cluster, moving consumers together, rather than in one big switch.
- Budget for the period when both platforms run, and set a date for turning off the old one.
- Set up security, lineage and governance on the new platform in the first wave, not as a later phase.

# Questions to ask

- What is driving the migration: cost, end of support, missing capabilities or a cloud strategy?
- How many objects, jobs and reports are in scope, and how many are actually used?
- What evidence will business owners need before they accept the new platform's results?
- How long can both platforms run in parallel?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [Code and SQL translation](code-translation.md), [Database migration](database-migration.md) |
| Related | [Bulk and offline transfer](../ingestion-integration/bulk-data-transfer.md), [Catalogue federation](../storage/catalogue-federation.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data profiling](../data-quality/data-profiling.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Impact analysis](../metadata/impact-analysis.md), [Low-code transformation](../processing/low-code-transformation.md), [Mainframe data integration](../ingestion-integration/mainframe-integration.md), [Semantic model interchange](../analytics-bi/semantic-model-interchange.md), [Spend forecasting and anomaly detection](cost-forecasting.md), [Table format conversion](../storage/table-format-conversion.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3)
- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 2, Managed)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter V, Section I – ICT third-party risk management (Articles 28 to 30) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VI – Switching between data processing services

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Transform](../../technologies/aws/aws-transform.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Migration Service](../../technologies/google-cloud/gcp-bigquery-migration-service.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakebridge](../../technologies/databricks/databricks-lakebridge.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica PowerCenter Cloud Edition (PCCE)](../../technologies/informatica/informatica-powercenter-cloud-edition.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Replication Manager](../../technologies/cloudera/cloudera-replication-manager.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Warehouse in SAP Business Data Cloud](../../technologies/sap/sap-business-warehouse-bdc.md), [SAP Datasphere](../../technologies/sap/sap-datasphere.md) |

Narrower capabilities are realised by a further 10 technologies; see their pages.
