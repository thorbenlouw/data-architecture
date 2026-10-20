---
type: Technology
id: sas-data-maker
title: SAS Data Maker
description: Low-code application that generates synthetic tables, including related tables and time series, which keep the statistical patterns of real data, and reports the quality and privacy of the result.
platform: platform-sas
kind: saas
availability: ga
realises: [synthetic-data]
resource: https://www.sas.com/en_us/software/data-maker.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Generally available on Microsoft Marketplace, running on Azure, since November 2025; it was first shown in private preview as a Snowflake Native App in June 2024, and its generation technology comes from software SAS bought from Hazy in November 2024. It can also generate extra records for under-represented classes and rare events, and SAS plans to integrate it into SAS Viya and support more clouds.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps) (primary): Generate artificial data that keeps the useful properties of real data without exposing real records.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake synthetic data generation](../snowflake/snowflake-synthetic-data.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Studios (RAG, Fine Tuning and Synthetic Data Studios)](../cloudera/cloudera-ai-studios.md) (preview) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Select AI](../oracle/oracle-select-ai.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Synthetic Data Vault (SDV)](../open-source/sdv.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MOSTLY AI Data Intelligence Platform](../independent/mostly-ai-data-intelligence-platform.md), [Tonic Structural](../independent/tonic-structural.md), [Tonic Textual](../independent/tonic-textual.md) | [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) |
