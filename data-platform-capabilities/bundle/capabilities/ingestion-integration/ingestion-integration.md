---
type: Capability
id: ingestion-integration
title: Ingestion and integration
description: Bring data from source systems into the platform and keep it in step with them.
aliases: [data integration, data ingestion]
broader: []
related: [workflow-orchestration, data-reconciliation, schema-registry, cross-system-lineage, data-contracts]
depends_on: [storage, secrets-management]
order: 1
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Ingestion moves data from the systems that create it into the platform; integration keeps the two in step afterwards. Sources include relational and NoSQL databases, SaaS applications, partner files, web APIs, event streams, devices, document stores and mainframes. The capabilities differ along three lines: how data is read (queries, transaction logs, files, APIs or subscriptions), how often (scheduled batches or continuous streams) and how change is represented (full snapshots, incremental extracts or row-level change events).

Batch ingestion covers scheduled and on-demand loads from files, databases, SaaS applications and APIs, plus bulk transfer for very large one-off moves. Change data capture and database replication keep copies of operational databases current. Event streaming and message queuing carry events between systems; streaming ingestion lands those events in the platform, with IoT telemetry, behavioural events and stream-to-table materialisation as specialised forms. Unstructured ingestion brings in documents and media with their metadata and permissions.

Managed file transfer, B2B and EDI integration, application integration and mainframe integration sit at the boundary with operational and partner systems, and analytics often draws on the flows they carry. Custom connectors fill gaps where nothing prebuilt exists. Idempotent loading applies to all of them: every load should be safe to retry or replay so failures never double-count data. Ingestion feeds processing, and orchestration decides when it runs.

# Key considerations

- Use a small number of ingestion patterns consistently rather than a different tool per source. Each extra tool adds credentials, monitoring and gaps in lineage.
- Land data unchanged before transforming it, so you can reprocess when logic changes or a parsing bug is found.
- Agree freshness per source with its consumers. Continuous ingestion costs more to run and support than a daily batch, and is often not needed.
- Decide per source what happens when its schema changes: add new columns automatically, reject the load or flag it for review.
- Record load metadata such as source, extract time and batch id on every row, so reconciliation and debugging are possible later.

# Questions to ask

- How many sources are there, of which kinds, and who owns each one?
- What freshness does each consumer need, and what does late data cost the business?
- Can the source systems take extra query load, or must extraction use logs, replicas or exports?
- How are source schema changes communicated to the data team today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Application integration](application-integration.md), [B2B and EDI integration](b2b-edi-integration.md), [Batch ingestion](batch-ingestion.md), [Change data capture](change-data-capture.md), [Custom connector development](custom-connectors.md), [Database replication and mirroring](database-replication.md), [Deduplication and idempotent loading](idempotent-loading.md), [Event streaming](event-streaming.md), [Mainframe data integration](mainframe-integration.md), [Managed file transfer](managed-file-transfer.md), [Message queuing](message-queuing.md), [Streaming ingestion](streaming-ingestion.md), [Unstructured data ingestion](unstructured-ingestion.md) |
| Related | [Data contracts](../data-products/data-contracts.md), [Data reconciliation](../data-quality/data-reconciliation.md), [End-to-end lineage](../metadata/cross-system-lineage.md), [Schema registry](../metadata/schema-registry.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Storage and table management](../storage/storage.md), [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 153 technologies; see their pages.
