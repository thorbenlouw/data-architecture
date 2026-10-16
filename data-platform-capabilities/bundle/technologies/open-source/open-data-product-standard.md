---
type: Technology
id: open-data-product-standard
title: Open Data Product Standard (ODPS)
description: YAML specification describing a data product's purpose, input and output ports, owners, contracts and lifecycle status.
aliases: [ODPS, Bitol ODPS]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [data-product-specification, data-product-lifecycle, data-ownership]
resource: https://github.com/bitol-io/open-data-product-standard
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, maintained by Bitol in LF AI & Data. Version 1.0 was released in 2025 and 1.1.0 around September 2026; output ports refer to ODCS contracts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products) (primary): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) (Data products): Version, publish, deprecate and retire data products with notice to their consumers.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md), [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data product studio](../sap/sap-bdc-data-product-studio.md) (unconfirmed), [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
