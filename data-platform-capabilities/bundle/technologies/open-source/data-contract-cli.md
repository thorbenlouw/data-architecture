---
type: Technology
id: data-contract-cli
title: Data Contract CLI
description: Command-line tool that lints data contracts, tests live data against them, detects breaking changes and generates code and documentation from them.
aliases: [datacontract-cli]
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-contracts, data-testing, ci-cd]
resource: https://github.com/datacontract/datacontract-cli
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence. Supports the Open Data Contract Standard (ODCS). Commonly run in CI to block breaking schema changes.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products) (primary): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [dbt Projects on Snowflake](../snowflake/snowflake-dbt-projects.md) | [CI/CD](../../capabilities/development-lifecycle/ci-cd.md), [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Soda Cloud](../independent/soda-cloud.md), [dbt platform](../independent/dbt-platform.md), [Twilio Segment](../independent/twilio-segment.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) |
