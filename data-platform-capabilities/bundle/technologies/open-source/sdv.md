---
type: Technology
id: sdv
title: Synthetic Data Vault (SDV)
description: Python library that learns from real tabular, relational and time-series data and generates synthetic data with similar statistical properties.
platform: platform-open-source
kind: software
availability: ga
realises: [synthetic-data]
resource: https://github.com/sdv-dev/SDV
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Licence change to note. Since 2023 SDV is under the Business Source License, which allows internal use but limits commercial redistribution, so it is source-available rather than open source. Maintained by DataCebo.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps) (primary): Generate artificial data that keeps the useful properties of real data without exposing real records.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake synthetic data generation](../snowflake/snowflake-synthetic-data.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI](../oracle/oracle-select-ai.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MOSTLY AI Data Intelligence Platform](../independent/mostly-ai-data-intelligence-platform.md), [Tonic Structural](../independent/tonic-structural.md), [Tonic Textual](../independent/tonic-textual.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
