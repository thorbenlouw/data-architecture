---
type: Technology
id: liquibase
title: Liquibase Community
description: Database change management tool that tracks, versions and applies schema changes defined in SQL, XML, YAML or JSON changelogs.
aliases: [Liquibase]
platform: platform-open-source
kind: software
availability: ga
realises: [schema-change-management, ci-cd]
resource: https://www.liquibase.com/blog/liquibase-community-for-the-future-fsl
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Licence change. From version 5.0 (September 2025) Liquibase Community moved from Apache 2.0 to the Functional Source License (FSL), which bars competing commercial offerings; each release reverts to Apache 2.0 after two years. Internal production use is still allowed. Versions 4.x remain Apache 2.0.

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
