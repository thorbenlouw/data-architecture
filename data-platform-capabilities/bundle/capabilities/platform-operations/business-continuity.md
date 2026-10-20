---
type: Capability
id: business-continuity
title: Backup and disaster recovery
description: Protect against data loss and outages with backups, replication and failover.
aliases: [business continuity, disaster recovery, DR, RPO and RTO, resilience]
broader: [platform-operations]
related: [time-travel, infrastructure-as-code, data-retention, deployment-options, compliance-evidence]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data platform needs protection against two kinds of event. Data loss covers accidental deletes, faulty runs that overwrite good data, corruption and ransomware, and is handled with backups, time travel, immutable copies and restore procedures. Outages cover the loss of a cluster, a region or a provider service, and are handled by replicating data and configuration elsewhere and failing over. Each tier of workload gets a recovery point objective (RPO, how much recent data may be lost) and a recovery time objective (RTO, how long recovery may take).

Designs follow from those objectives. A reporting mart may tolerate a day's loss and a day's outage, so nightly backups are enough; a fraud-scoring feed may allow minutes, which needs continuous cross-region replication. Recovery must also bring back metadata, permissions, pipeline code, secrets and network settings, or restored data cannot be used. Availability within a region is usually the provider's job; recovery across regions is usually the customer's design. Regulators in finance and other sectors expect tested, evidenced plans.

# Key considerations

- Set RPO and RTO per workload tier with the business, then design to them. One target for everything is either too costly or too weak.
- Recover the whole service: catalogue, permissions, code, credentials and integrations must be restorable as well as data.
- Time travel and soft delete help with mistakes but sit in the same account as the original data. They do not protect against account compromise or regional loss.
- Plan for dependencies outside the platform, such as the identity provider, source systems and network links, which can block recovery.

# Questions to ask

- What are the RPO and RTO for the most important data and workloads, and who agreed them?
- When was recovery last tested, and did it meet those objectives?
- Which regulations require documented and tested continuity plans?
- What would happen if the platform's primary region were unavailable for a day?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [Backup and restore](backup-restore.md), [Cross-region replication and failover](cross-region-failover.md), [Resilience and recovery testing](resilience-testing.md) |
| Related | [Storage and table management](../storage/storage.md), [Security and access](../security/security.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Hybrid and multi-cloud deployment](deployment-options.md), [Infrastructure as code](infrastructure-as-code.md), [Retention and disposal](../governance/data-retention.md), [Time travel](../storage/time-travel.md) |

# Where it appears

- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Resilience and recovery](../../maturity/track-resilience.md)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Keeper](../../technologies/clickhouse/clickhouse-keeper.md) |

Narrower capabilities are realised by a further 29 technologies; see their pages.
