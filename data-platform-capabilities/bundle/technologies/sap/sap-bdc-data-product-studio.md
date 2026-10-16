---
type: Technology
id: sap-bdc-data-product-studio
title: SAP Business Data Cloud data product studio
description: Tooling in BDC for creating, modelling and managing customer-defined data products with SQL or visual transformations, schema, lineage, versioning and lifecycle states.
platform: platform-sap
kind: feature
availability: unconfirmed
realises: [data-product-lifecycle, data-product-specification, sql-transformation]
resource: https://news.sap.com/2025/11/sap-snowflake-new-data-fabric-innovations-sap-bdc-sap-hana-cloud/
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Announced at SAP TechEd in November 2025 for building customer-defined data products next to the SAP-managed ones.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) (Data products) (primary): Version, publish, deprecate and retire data products with notice to their consumers.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [SQL transformation](../../capabilities/processing/sql-transformation.md) (Processing and transformation): Transform data inside the platform using SQL, typically after it has been loaded.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** unconfirmed  
**Product family:** SAP Business Data Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Data Product Standard (ODPS)](../open-source/open-data-product-standard.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
