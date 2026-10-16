---
type: Technology
id: ibm-data-product-hub
title: IBM Data Product Hub
description: Marketplace in watsonx.data intelligence where producers package data with business meaning, quality, ownership and contracts, and consumers find and request it.
platform: platform-ibm
kind: feature
availability: ga
realises: [data-marketplace, data-contracts, data-product-specification, access-requests]
resource: https://www.ibm.com/products/data-product-hub
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports the [Open Data Contract Standard](../open-source/open-data-contract-standard.md) for contracts. Delivery can be by zero-copy access through watsonx.data or by extract.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration) (primary): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Data contracts](../../capabilities/data-products/data-contracts.md) (Data products): Agree and enforce a dataset's schema, meaning, quality and service levels between producers and consumers.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx.data intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md), [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Access requests and reviews](../../capabilities/security/access-requests.md), [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake Marketplace](../snowflake/snowflake-marketplace.md), [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Marketplace](../databricks/databricks-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Open Data Contract Standard (ODCS)](../open-source/open-data-contract-standard.md) | [Data contracts](../../capabilities/data-products/data-contracts.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
