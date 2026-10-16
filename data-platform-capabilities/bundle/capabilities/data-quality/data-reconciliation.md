---
type: Capability
id: data-reconciliation
title: Data reconciliation
description: Prove that data moved between systems is complete and correct using counts, totals and record matching.
aliases: [control totals, source-to-target checks]
broader: [data-quality]
related:
- platform-migration
- critical-data-elements
- compliance-evidence
- idempotent-loading
- data-quality-rules
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Simple controls compare row counts and totals of key amounts for each batch, such as the number and total value of transactions per day in the core banking system and in the warehouse. Stronger controls compare hashes per record or per group, or match records by key to list what is missing, extra or different, so each break can be explained.

Reconciliation is required wherever loss or duplication would cause financial, regulatory or customer harm: ledgers, payments, regulatory reporting, and platform migrations where the new system must be shown to produce the same results as the old one. Results are usually kept as evidence for auditors. It differs from general quality rules because it compares two systems with each other rather than one dataset with expectations. Comparing every record at scale is costly, so many designs reconcile totals continuously and records on a sample or after a mismatch.

# Key considerations

- Agree tolerances and timing. In-flight records, time-zone cut-offs and rounding cause expected differences that must not raise alarms.
- Reconcile at several stages, such as source to landing and landing to reporting, so breaks can be located.
- Keep results and break resolutions as audit evidence, with who signed them off.
- Full record matching across large tables is expensive. Compare hashes of groups first to narrow down where differences lie.

# Questions to ask

- Which data flows must be proved complete and accurate for finance, audit or regulators?
- Is a platform migration planned that needs parallel running and comparison?
- Who investigates and signs off reconciliation breaks?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data quality and observability](data-quality.md) |
| Related | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [B2B and EDI integration](../ingestion-integration/b2b-edi-integration.md), [Batch ingestion](../ingestion-integration/batch-ingestion.md), [Bulk and offline transfer](../ingestion-integration/bulk-data-transfer.md), [Code and SQL translation](../platform-operations/code-translation.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Critical data elements](../governance/critical-data-elements.md), [Data export](../serving/data-export.md), [Data pipeline testing](../development-lifecycle/data-testing.md), [Data quality rules](data-quality-rules.md), [Database extraction](../ingestion-integration/database-extraction.md), [Database migration](../platform-operations/database-migration.md), [Deduplication and idempotent loading](../ingestion-integration/idempotent-loading.md), [Mainframe data integration](../ingestion-integration/mainframe-integration.md), [Platform migration](../platform-operations/platform-migration.md), [Regulatory submission](../serving/regulatory-submission.md), [Resilience and recovery testing](../platform-operations/resilience-testing.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 4)
- **Patterns:** [ETL](../../patterns/etl.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 3, Defined) · [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 3 – Accuracy and integrity; Principle 4 – Completeness; Principle 7 – Accuracy (reporting)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Database Migration Service](../../technologies/aws/aws-dms.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Migration Service](../../technologies/google-cloud/gcp-bigquery-migration-service.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakebridge](../../technologies/databricks/databricks-lakebridge.md) |
| [Informatica](../../platforms/platform-informatica.md) | Data Validation test cases | [Informatica Data Validation](../../technologies/informatica/informatica-data-validation.md) |
