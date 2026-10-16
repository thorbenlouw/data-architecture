---
type: Technology
id: growthbook
title: GrowthBook
description: Open-core feature flagging and experimentation platform that analyses A/B tests with SQL against data already in the warehouse.
platform: platform-open-source
kind: open-source
availability: ga
realises: [experimentation]
resource: https://www.growthbook.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GrowthBook queries experiment exposure and metric data where it already lives, such as Snowflake, BigQuery, Databricks or Redshift, rather than collecting events into its own store. It can be self-hosted or used as a managed cloud service. The core is open source, with enterprise features under a commercial licence.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Experimentation and causal measurement](../../capabilities/analytics-bi/experimentation.md) (Analytics and BI) (primary): Run controlled experiments with holdout groups and measure whether an action caused the outcome.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga
