---
type: Technology
id: clickhouse-keeper
title: ClickHouse Keeper
description: Raft-based coordination service, compatible with the ZooKeeper client protocol, that coordinates replication, distributed DDL and queue engines.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [business-continuity]
resource: https://clickhouse.com/docs/guides/sre/keeper/clickhouse-keeper
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Replaces ZooKeeper for self-managed clusters (data must be converted; mixed clusters are not possible). Fully managed and invisible in ClickHouse Cloud.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Backup and disaster recovery](../../capabilities/platform-operations/business-continuity.md) (Platform operations) (primary): Protect against data loss and outages with backups, replication and failover.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga
