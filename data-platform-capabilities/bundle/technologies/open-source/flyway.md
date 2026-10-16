---
type: Technology
id: flyway
title: Flyway Community
description: Database migration tool that applies versioned SQL or Java migration scripts in order and records which have run.
aliases: [Flyway, Redgate Flyway]
platform: platform-open-source
kind: open-source
availability: ga
realises: [schema-change-management, ci-cd]
resource: https://github.com/flyway/flyway
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Community edition is Apache 2.0, owned by Redgate, whose paid editions add drift detection, undo and change reports.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Schema change management](../../capabilities/development-lifecycle/schema-change-management.md) (Development and DataOps) (primary): Version and apply database schema changes through controlled migrations.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Schema change management](../../capabilities/development-lifecycle/schema-change-management.md) |
