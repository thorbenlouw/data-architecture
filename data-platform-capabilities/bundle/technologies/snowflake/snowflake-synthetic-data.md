---
type: Technology
id: snowflake-synthetic-data
title: Snowflake synthetic data generation
description: The GENERATE_SYNTHETIC_DATA procedure creates statistically similar tables, with the same column names and types, from up to five source tables without linking output rows to real records.
platform: platform-snowflake
kind: feature
availability: ga
realises: [synthetic-data]
resource: https://docs.snowflake.com/en/user-guide/synthetic-data
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps) (primary): Generate artificial data that keeps the useful properties of real data without exposing real records.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI](../oracle/oracle-select-ai.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Maker](../sas/sas-data-maker.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Synthetic Data Vault (SDV)](../open-source/sdv.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MOSTLY AI Data Intelligence Platform](../independent/mostly-ai-data-intelligence-platform.md), [Tonic Structural](../independent/tonic-structural.md), [Tonic Textual](../independent/tonic-textual.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
