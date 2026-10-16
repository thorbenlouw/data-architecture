---
type: Capability
id: data-subject-requests
title: Data subject requests
description: Find, export or erase a person's data across the platform when they ask.
aliases: [DSAR, right to be forgotten, right to erasure]
broader: [privacy-management]
related: [row-level-updates, entity-resolution, data-retention, time-travel, table-maintenance]
depends_on: [data-classification, data-lineage, row-level-updates]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When a person exercises a right such as access, correction, erasure or portability, the platform must find every record about them, act on it and show that it did. A typical erasure request arrives from a privacy portal with an identifier such as an email address. The platform resolves it to internal keys, deletes or anonymises matching rows in source copies, derived tables, files and feature stores, expires older table versions that still hold them, and records completion. An access request runs the same search and produces an export.

The GDPR generally allows one month to respond, extendable for complex cases, and other laws set similar deadlines, so volume pushes teams to automate. The hard parts are resolving identity, finding copies that lineage misses, and storage that cannot change in place, such as table history, backups and trained models. Approaches include row-level deletes in open table formats, crypto-shredding (deleting a per-person encryption key so that person's data becomes unreadable) and documented handling where deletion is not technically possible.

# Key considerations

- Deleting a row does not remove it from earlier table versions or snapshots. Expire old versions and clean up files within the response deadline.
- Build a mapping from external identifiers to internal keys, often from master data, before automating requests.
- Decide how requests reach downstream copies, such as shared datasets, exports and SaaS tools fed by reverse ETL.
- Record each step and its result so you can prove completion, without keeping more personal data in the request log than needed.
- Agree with legal how backups, legal holds and trained models are handled, since they often cannot be changed in place.

# Questions to ask

- How many requests arrive each month, and how are they fulfilled today?
- Which identifiers do requests carry, and can they be resolved to records in every system?
- Does storage support row-level deletes and expiry of old versions within the deadline?
- Which copies of data sit outside the platform but were fed from it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md) |
| Narrower | [Crypto-shredding](../security/crypto-shredding.md) |
| Related | [Agent memory](../generative-ai/agent-memory.md), [Backup and restore](../platform-operations/backup-restore.md), [Customer-managed keys](../security/customer-managed-keys.md), [Document and unstructured lineage](../metadata/unstructured-lineage.md), [Entity resolution](../master-data/entity-resolution.md), [Immutable backups](../platform-operations/immutable-backups.md), [Retention and disposal](data-retention.md), [Row-level updates and deletes](../storage/row-level-updates.md), [Table maintenance and optimisation](../storage/table-maintenance.md), [Test data management](../development-lifecycle/test-data-management.md), [Time travel](../storage/time-travel.md) |
| Depends on | [Data classification](data-classification.md), [Data lineage](../metadata/data-lineage.md), [Row-level updates and deletes](../storage/row-level-updates.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 2, Managed)
- **Frameworks:** [GDPR](../../frameworks/framework-gdpr.md): Article 15 – Right of access; Article 16 – Right to rectification; Article 17 – Right to erasure; Article 18 – Right to restriction of processing; Article 20 – Right to data portability; Article 21 – Right to object

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Priva](../../technologies/microsoft/purview-priva.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [BigID Next](../../technologies/independent/bigid-next.md), [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md) |

Narrower capabilities are realised by a further 3 technologies; see their pages.
