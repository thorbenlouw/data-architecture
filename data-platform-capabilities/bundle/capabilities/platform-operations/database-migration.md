---
type: Capability
id: database-migration
title: Database migration
description: Move databases to new engines or platforms, converting schemas and keeping data in sync until cut-over.
aliases: [schema conversion]
broader: [platform-migration]
related:
- database-replication
- schema-change-management
- data-reconciliation
- bulk-data-transfer
- code-translation
depends_on: [change-data-capture]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Schema conversion maps tables, data types, indexes, constraints, views and procedures from the source engine to the target, for example from an on-premises relational database to a managed cloud service, or from an operational database into an analytical platform. An initial full load then copies existing data, and change data capture applies ongoing changes so source and target stay in sync while applications are tested against the new system. At cut-over, writes to the source stop briefly, the last changes are applied and applications switch over.

Keeping both in sync cuts downtime from hours or days to minutes, and leaves a fallback while the target proves itself. A homogeneous migration, between versions of the same engine, mainly moves data; a heterogeneous one, between different engines, also needs schema and code conversion. Validation compares counts, checksums and samples between source and target. Platform migration covers a whole estate; database migration is the mechanics for each database within it.

# Key considerations

- Check data type mappings carefully, especially dates, time zones, numeric precision and character sets, which can change values silently.
- Large objects, tables without primary keys and sequences often need special handling by CDC tools.
- Rehearse cut-over, including rollback, and measure how long the final sync and validation take.
- Watch the load that extraction and CDC put on the source database during business hours.

# Questions to ask

- How much downtime can each application tolerate at cut-over?
- Is the move to the same engine or a different one, and how much database code must be converted?
- Do applications need a way back to the old database if problems appear after cut-over?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform migration](platform-migration.md) |
| Related | [Bulk and offline transfer](../ingestion-integration/bulk-data-transfer.md), [Code and SQL translation](code-translation.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Database replication and mirroring](../ingestion-integration/database-replication.md), [Schema change management](../development-lifecycle/schema-change-management.md) |
| Depends on | [Change data capture](../ingestion-integration/change-data-capture.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2)
- **Maturity tracks:** [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Database Migration Service](../../technologies/aws/aws-dms.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Database Migration Service](../../technologies/google-cloud/gcp-database-migration-service.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle GoldenGate](../../technologies/oracle/oracle-goldengate.md) |
