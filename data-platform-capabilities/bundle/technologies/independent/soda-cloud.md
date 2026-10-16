---
type: Technology
id: soda-cloud
title: Soda Cloud
description: Collaborative workspace for defining data contracts, running checks in pipelines and on schedules, monitoring metrics for anomalies and triaging data incidents.
platform: platform-independent
vendor: Soda
kind: saas
availability: ga
realises:
- data-contracts
- data-quality-rules
- data-anomaly-detection
- data-observability
- data-issue-management
resource: https://docs.soda.io/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Soda 4.0 is built around data contracts that run in CI, in pipelines and in production. Checks run on a Soda-hosted or self-hosted runner in your Kubernetes cluster. Record-level diagnostics are kept in a diagnostics warehouse. The open-source engine is [Soda Core](../open-source/soda-core.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products) (primary): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) (Data quality and observability): Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency.
- [Data anomaly detection](../../capabilities/data-quality/data-anomaly-detection.md) (Data quality and observability): Learn normal patterns in data and alert on unexpected changes without hand-written rules.
- [Data observability](../../capabilities/data-quality/data-observability.md) (Data quality and observability): Monitor data in production for freshness, volume, schema and distribution problems, and alert owners.
- [Data issue management](../../capabilities/data-quality/data-issue-management.md) (Data quality and observability): Log, assign, track and resolve data quality incidents with their owners.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Soda Core](../open-source/soda-core.md), [Data Contract CLI](../open-source/data-contract-cli.md), [Open Data Contract Standard (ODCS)](../open-source/open-data-contract-standard.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data quality rules](../../capabilities/data-quality/data-quality-rules.md) |
