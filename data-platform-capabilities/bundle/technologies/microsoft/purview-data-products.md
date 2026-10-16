---
type: Technology
id: purview-data-products
title: Data products in Microsoft Purview Unified Catalog
description: Groups related tables, files and reports into a published data product with owners, terms of use and an access request and approval workflow.
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-product-specification, access-requests, data-product-lifecycle, data-marketplace]
resource: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Access approvals are recorded in Purview and can be provisioned to some sources (Fabric, Azure SQL, Databricks Unity Catalog); check per-source support. No machine-readable contract standard (such as ODCS) is exposed.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products) (primary): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) (Data products): Version, publish, deprecate and retire data products with notice to their consumers.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md), [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Business Data Cloud data product studio](../sap/sap-bdc-data-product-studio.md) (unconfirmed) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md), [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Data Product Standard (ODPS)](../open-source/open-data-product-standard.md), [Open Data Contract Standard (ODCS)](../open-source/open-data-contract-standard.md) | [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
