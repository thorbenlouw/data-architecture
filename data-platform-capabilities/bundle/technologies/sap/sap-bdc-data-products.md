---
type: Technology
id: sap-bdc-data-products
title: SAP Business Data Cloud data products
description: SAP-managed, curated datasets with business metadata for core processes in SAP Cloud ERP, SuccessFactors and other applications, populated automatically from the source systems.
aliases: [SAP data products, BDC data products]
platform: platform-sap
kind: feature
availability: ga
realises:
- data-product-specification
- saas-connectors
- data-marketplace
- change-feeds
- application-data-products
resource: https://news.sap.com/2025/05/future-intelligent-applications-sap-business-data-cloud/
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Replaces much hand-built extraction from SAP sources; SAP has been adding data products by domain since 2025. Data products are shared to consuming engines with Delta Sharing rather than copied.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products) (primary): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [SaaS application connectors](../../capabilities/ingestion-integration/saas-connectors.md) (Ingestion and integration): Pull data from business applications such as CRM, ERP and marketing tools through prebuilt connectors.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Change feeds](../../capabilities/serving/change-feeds.md) (Serving and activation): Expose row-level changes to tables as a stream that downstream consumers can process incrementally.
- [Vendor-supplied application data products](../../capabilities/data-products/application-data-products.md) (Data products): Use governed, documented datasets that business application vendors publish and maintain, instead of building extraction.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Data Product Standard (ODPS)](../open-source/open-data-product-standard.md), [Open Data Contract Standard (ODCS)](../open-source/open-data-contract-standard.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
