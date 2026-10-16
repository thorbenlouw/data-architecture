---
type: Capability
id: manual-adjustments
title: Approved manual adjustments
description: Record manual adjustments to reported figures with approval steps, reasons and a full audit trail.
aliases: [adjustment workflow, post-close adjustments]
broader: [data-writeback, critical-data-elements]
related: [regulatory-submission, enterprise-planning, audit-logging, temporal-data]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An adjustment changes a reported figure without changing the source system, for example a late accrual added to month-end revenue, a reclassification between cost centres, or an expert override of a model-driven provision. The user enters it against a specific figure, period and version, with an amount, a reason and supporting evidence. Someone else approves it, often with thresholds that send larger amounts to more senior approvers, and it is then applied as a separate layer over the system figures, so reports can show values before and after adjustment.

It matters in financial close, regulatory and management reporting, where adjustments are normal but auditors expect each one to be justified, approved and traceable. Without it, adjustments are typed into spreadsheets or final files and cannot be reproduced. It is a stricter form of data write-back: entries are never edited in place, only reversed and replaced. Adjustments that recur every period point to a data quality problem to fix upstream.

# Key considerations

- Store adjustments as append-only records linked to the figure they change, and apply them in the model. Never overwrite source or reported values.
- Enforce segregation of duties: the person who enters an adjustment must not be able to approve it.
- Decide whether adjustments carry forward to later periods or reverse automatically, and show the rule to users.
- Report adjustment counts and amounts by area. Large or recurring adjustments are a target for data quality work and an area auditors will sample.
- When an adjustment changes after sign-off, keep the as-reported version alongside the corrected one.

# Questions to ask

- Which reported figures are adjusted by hand today, and where are those adjustments recorded?
- What approval levels and evidence do auditors or regulators expect?
- Must a report be reproducible exactly as it was signed off, including its adjustments?
- Which adjustments recur every period, and why?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Data entry and write-back](data-writeback.md), [Critical data elements](../governance/critical-data-elements.md) |
| Related | [Audit logging](../security/audit-logging.md), [Bitemporal data](../specialised-data/temporal-data.md), [Planning and forecasting](enterprise-planning.md), [Regulatory submission](../serving/regulatory-submission.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Personas:** [Business user](../../personas/persona-business-user.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 4, Measured)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 3 – Accuracy and integrity; Principle 7 – Accuracy (reporting)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [Workiva](../../technologies/independent/workiva.md) |
