---
type: Technology
id: open-data-contract-standard
title: Open Data Contract Standard (ODCS)
description: YAML specification for data contracts covering schema, quality rules, service levels, roles, support channels, pricing and servers.
aliases: [ODCS, Bitol ODCS]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [data-contracts, data-slas, data-product-specification]
resource: https://bitol.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, maintained by the Bitol project, which graduated in LF AI & Data in mid-2026. Version 3.2.0 was released around September 2026 together with ODPS 1.1.0 (3.1.0 in December 2025). Supported by OpenMetadata, DataHub, Soda, Data Contract CLI and several commercial catalogues.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products) (primary): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data service levels](../../capabilities/data-products/data-slas.md) (Data products): Set and track service levels for data products, such as freshness, availability and quality.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md), [Data service levels](../../capabilities/data-products/data-slas.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Soda Cloud](../independent/soda-cloud.md), [Twilio Segment](../independent/twilio-segment.md), [dbt platform](../independent/dbt-platform.md) | [Data contracts](../../capabilities/data-products/data-contracts.md) |
