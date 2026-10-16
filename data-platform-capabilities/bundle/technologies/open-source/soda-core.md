---
type: Technology
id: soda-core
title: Soda Core
description: Data quality and data contract verification engine that checks schema and data against YAML contracts from a CLI, Python or a pipeline.
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-contracts, data-quality-rules, data-testing]
resource: https://github.com/sodadata/soda-core
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Open source, led by Soda. Version 4 reorganised the engine around data contracts (packages named soda-<source>); v3 (SodaCL checks) is pinned to 3.5.x. Anomaly detection, central contract management and remote runners need the commercial [Soda Cloud](../independent/soda-cloud.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products) (primary): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Soda Cloud](../independent/soda-cloud.md), [Twilio Segment](../independent/twilio-segment.md), [dbt platform](../independent/dbt-platform.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
