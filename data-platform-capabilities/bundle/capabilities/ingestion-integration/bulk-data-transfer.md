---
type: Capability
id: bulk-data-transfer
title: Bulk and offline transfer
description: Move very large datasets into the platform over high-throughput links or physical transfer devices.
aliases: [migration transfer, transfer appliance]
broader: [batch-ingestion]
related: [platform-migration, database-migration, data-reconciliation, storage-tiering]
depends_on: [object-storage]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Bulk transfer moves datasets of hundreds of terabytes or more, usually once, during a migration or when bringing in a large archive. Over the network it relies on parallel, resumable copy tools and dedicated high-bandwidth links. Physically, a cloud provider ships a rugged storage appliance that is filled on site and returned for loading into object storage. At a sustained 1 Gbit/s, one petabyte takes about three months, which is why shipping disks is often faster.

It matters for data centre exits, history migrations and research collections such as imaging or genomics, where normal ingestion would take months or saturate shared links. The usual pattern is one bulk copy followed by incremental sync of changes until cut-over. Approaches differ in throughput, protection of data in transit and whether integrity can be checked end to end. Routine batch ingestion, by contrast, assumes repeated loads of modest size.

# Key considerations

- Estimate transfer time from realistic sustained throughput, not link capacity. Small files, latency and shared bandwidth often halve it.
- Verify integrity with checksums at source and destination, and keep the manifest as evidence for the migration.
- Encrypt devices and data in transit, and record chain of custody for physical shipments of regulated data.
- Plan the catch-up sync for data that changes during the transfer, or the copy is stale on arrival.

# Questions to ask

- How much data must move, and by when?
- What sustained bandwidth is available, and can it be used without disrupting other traffic?
- Will the data change during transfer, and how will those changes be applied before cut-over?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Batch ingestion](batch-ingestion.md) |
| Related | [Data reconciliation](../data-quality/data-reconciliation.md), [Database migration](../platform-operations/database-migration.md), [Platform migration](../platform-operations/platform-migration.md), [Storage tiering and lifecycle](../storage/storage-tiering.md) |
| Depends on | [Object storage](../storage/object-storage.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | DataSync, Snowball Edge, Data Transfer Terminal | [AWS DataSync](../../technologies/aws/aws-datasync.md), [AWS Snowball Edge](../../technologies/aws/aws-snowball-edge.md) (deprecated) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Box](../../technologies/microsoft/azure-data-box.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Storage Transfer Service](../../technologies/google-cloud/gcp-storage-transfer-service.md), [Google Cloud Transfer Appliance](../../technologies/google-cloud/gcp-transfer-appliance.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Replication Manager](../../technologies/cloudera/cloudera-replication-manager.md) |
