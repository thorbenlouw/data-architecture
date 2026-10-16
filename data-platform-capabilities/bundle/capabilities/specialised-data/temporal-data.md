---
type: Capability
id: temporal-data
title: Bitemporal data
description: Store and query data as it was true in the real world and as it was recorded in the system.
aliases: [temporal tables, valid time, transaction time]
broader: [specialised-data]
related: [time-travel, data-versioning, data-modelling, critical-data-elements, compliance-evidence]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Bitemporal tables record two timelines for each fact. Valid time is when the fact was true in the real world, for example a customer's address from 1 March to 30 June. Transaction time is when the system recorded or changed that fact. Each row carries both periods, and a correction adds a new version instead of overwriting. You can then ask both "what was true on 1 April?" and "what did we believe on 1 April about that date?", which differ whenever corrections arrive late. SQL:2011 defines application-time and system-versioned tables for this.

It is needed where past reports, decisions or regulatory filings must be reproduced exactly as made, alongside corrected history: finance, insurance, risk, payroll, healthcare and trade surveillance. A type 2 slowly changing dimension keeps only one timeline. Table time travel covers transaction time for a limited retention period but not valid time, and is not meant for long-term history. Bitemporal modelling makes queries and joins harder, so it is usually applied to selected entities rather than everywhere.

# Key considerations

- Joins between bitemporal tables must align both periods. Provide views or functions so users do not get this wrong.
- Fix the precision and time zone of both timelines, and how open-ended periods are represented.
- Apply backdated changes through controlled processes, not ad hoc updates.
- Storage grows with every correction. Plan partitioning and archiving of old versions.

# Questions to ask

- Do you need to reproduce reports or decisions exactly as they were when they were made?
- How often do backdated corrections arrive, and how far back do they reach?
- Which regulations require you to show both the original and the corrected values?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Related | [Approved manual adjustments](../analytics-bi/manual-adjustments.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Critical data elements](../governance/critical-data-elements.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Data versioning](../storage/data-versioning.md), [Hierarchy management](../master-data/hierarchy-management.md), [Point-in-time correct joins](../machine-learning/point-in-time-joins.md), [Time travel](../storage/time-travel.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 12 – Review

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database](../../technologies/teradata/teradata-database.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Db2](../../technologies/ibm/ibm-db2.md) |
