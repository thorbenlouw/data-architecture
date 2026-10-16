---
type: Capability
id: mainframe-integration
title: Mainframe data integration
description: Capture and offload data from mainframe databases and files with minimal load on the host.
aliases: [z/OS offload, VSAM, IMS]
broader: [ingestion-integration]
related:
- change-data-capture
- database-extraction
- data-reconciliation
- platform-migration
- code-translation
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Mainframes still run core systems in banking, insurance and government, with data in Db2, IMS and VSAM or sequential files, described by COBOL copybooks and encoded in EBCDIC. Integration either reads the host databases' change logs (mainframe CDC) or offloads files and converts them off the host: decoding packed-decimal fields, applying the copybook layout and translating EBCDIC to Unicode. A bank might stream account changes from Db2 into the analytical platform so balances are available without running reports on the host.

Mainframe costs are driven largely by CPU consumption, so every extra query or extract job costs money and competes with critical batch windows. Good integration therefore keeps work on the host to a minimum and does conversion on cheaper platforms. Log-based capture suits databases; file offload suits VSAM and sequential data. Offloading data is often the first step in moving workloads off the mainframe, so this overlaps with platform migration.

# Key considerations

- Copybooks with REDEFINES, OCCURS DEPENDING ON and packed decimals need careful handling. Validate converted data against host totals.
- Measure the host CPU used by extraction and agree a budget with the mainframe team.
- Mainframe skills are scarce. Knowledge of record layouts and batch schedules is often held by a few people, so document it early.
- In regulated settings, reconcile counts and amounts between host and platform after every load.

# Questions to ask

- Which mainframe data stores hold the data needed, and how is each accessed today?
- When are the host's batch windows, and what does extra CPU cost?
- Is the aim ongoing integration, or a step towards leaving the mainframe?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Change data capture](change-data-capture.md), [Code and SQL translation](../platform-operations/code-translation.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Database extraction](database-extraction.md), [Platform migration](../platform-operations/platform-migration.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Database Ingestion and Replication](../../technologies/informatica/informatica-database-ingestion-and-replication.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Data Replication](../../technologies/ibm/ibm-data-replication.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Qlik Replicate](../../technologies/independent/qlik-replicate.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md) |
