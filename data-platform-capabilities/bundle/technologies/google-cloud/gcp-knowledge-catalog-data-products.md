---
type: Technology
id: gcp-knowledge-catalog-data-products
title: Knowledge Catalog data products
description: Packages catalogued assets into data products with owners, documentation, contracts covering refresh and quality expectations, and access groups that consumers request to join.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-product-specification, data-contracts, access-requests, data-slas, data-ownership]
resource: https://docs.cloud.google.com/dataplex/docs/data-products-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA May 2026 with approval workflows and Gemini-generated documentation. Data products can contain Iceberg REST catalogue and Looker assets and be published to SAP Business Data Cloud. Governance workflows for request and review of access are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products) (primary): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Data service levels](../../capabilities/data-products/data-slas.md) (Data products): Set and track service levels for data products, such as freshness, availability and quality.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Knowledge Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Business Data Cloud data product studio](../sap/sap-bdc-data-product-studio.md) (unconfirmed) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Data Contract Standard (ODCS)](../open-source/open-data-contract-standard.md), [Open Data Product Standard (ODPS)](../open-source/open-data-product-standard.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md), [Data service levels](../../capabilities/data-products/data-slas.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Starburst Galaxy](../independent/starburst-galaxy.md) | [Data product specification](../../capabilities/data-products/data-product-specification.md) |
