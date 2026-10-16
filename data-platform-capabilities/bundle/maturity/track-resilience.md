---
type: Maturity Track
id: track-resilience
title: Resilience and recovery
description: How well the platform withstands and recovers from data loss, corruption, ransomware and outages within agreed targets.
covers: [business-continuity, backup-restore, immutable-backups, cross-region-failover, resilience-testing]
related_tracks: [track-storage, track-security, track-platform-migration]
levels:
- level: 1
  name: Initial
  summary: Recovery depends on provider defaults and on the memory of a few engineers.
  criteria:
  - Backup relies on provider defaults or table history, with no defined recovery targets.
  - Nobody has restored a dataset from backup in the past year.
  - Recovery after an outage depends on what a few engineers remember.
  capabilities: []
- level: 2
  name: Managed
  summary: Critical systems have scheduled backups, written recovery objectives and at least one practised restore.
  criteria:
  - Scheduled backups with set retention exist for the main databases and tables.
  - Recovery point and recovery time objectives are written down for critical systems.
  - At least one critical dataset has been restored from backup and the steps documented.
  capabilities: [backup-restore]
- level: 3
  name: Defined
  summary: Every class of data has recovery targets, protected backups, a second region and a test schedule.
  criteria:
  - Every class of data has recovery targets, and backups include metadata, catalogues, permissions and pipeline code.
  - Critical data and configuration are replicated to a second region with a documented failover procedure.
  - Backups of critical data cannot be deleted or changed before they expire, and lifting a legal hold needs separate approval.
  - Restore and failover tests run to a schedule, and results are kept as evidence.
  capabilities: [cross-region-failover, immutable-backups, resilience-testing]
- level: 4
  name: Measured
  summary: Achieved recovery is measured against objectives, including end-to-end and ransomware scenarios.
  criteria:
  - Recovery times and data loss achieved in tests are compared with objectives, and shortfalls are tracked to closure.
  - Backup success and replication lag are monitored with alerts.
  - Critical reports and pipelines have been run end to end from the secondary region within their recovery target.
  - The test programme includes restoring from immutable backups after a simulated ransomware attack.
  capabilities: []
- level: 5
  name: Optimising
  summary: Failover is automated, tests are unannounced, and lessons change the design.
  criteria:
  - Failover for critical services is automated, and tests run without warning.
  - Recovery targets are reviewed against business impact each year and adjusted.
  - Lessons from incidents and tests lead to tracked changes in backup policy, architecture or runbooks.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means recovery point and recovery time objectives are set for each class of data, backups cover metadata and configuration as well as data, and recovery is rehearsed so the targets are known to be achievable. The EU Digital Operational Resilience Act requires financial entities to test resilience regularly, and BCBS 239 expects risk reporting to keep working under stress, which in practice calls for levels 3 and 4 here. Typical blockers are treating the provider's storage durability as a backup, restores that have never been tried, and recovery plans that cover data but not catalogues, permissions and pipeline code.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Recovery depends on provider defaults and on the memory of a few engineers.

- Backup relies on provider defaults or table history, with no defined recovery targets.
- Nobody has restored a dataset from backup in the past year.
- Recovery after an outage depends on what a few engineers remember.

## Level 2: Managed

Critical systems have scheduled backups, written recovery objectives and at least one practised restore.

- Scheduled backups with set retention exist for the main databases and tables.
- Recovery point and recovery time objectives are written down for critical systems.
- At least one critical dataset has been restored from backup and the steps documented.

**Capabilities first relied on:** [Backup and restore](../capabilities/platform-operations/backup-restore.md)

## Level 3: Defined

Every class of data has recovery targets, protected backups, a second region and a test schedule.

- Every class of data has recovery targets, and backups include metadata, catalogues, permissions and pipeline code.
- Critical data and configuration are replicated to a second region with a documented failover procedure.
- Backups of critical data cannot be deleted or changed before they expire, and lifting a legal hold needs separate approval.
- Restore and failover tests run to a schedule, and results are kept as evidence.

**Capabilities first relied on:** [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md)

## Level 4: Measured

Achieved recovery is measured against objectives, including end-to-end and ransomware scenarios.

- Recovery times and data loss achieved in tests are compared with objectives, and shortfalls are tracked to closure.
- Backup success and replication lag are monitored with alerts.
- Critical reports and pipelines have been run end to end from the secondary region within their recovery target.
- The test programme includes restoring from immutable backups after a simulated ransomware attack.

## Level 5: Optimising

Failover is automated, tests are unannounced, and lessons change the design.

- Failover for critical services is automated, and tests run without warning.
- Recovery targets are reviewed against business impact each year and adjusted.
- Lessons from incidents and tests lead to tracked changes in backup policy, architecture or runbooks.

# Capabilities in scope

[Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md)

# Related tracks

- [Storage and table management](track-storage.md): How well data is kept in durable, open, maintained tables that many engines can read, update and trust.
- [Security and access control](track-security.md): How well data is protected from unauthorised access, loss and misuse, from identity through fine-grained access to threat detection.
- [Platform migration and portability](track-platform-migration.md): How safely and predictably the organisation moves workloads, code and data to new platforms, and how freely it can choose where the platform runs.

Levels follow the shared [maturity scale](maturity-scale.md).
