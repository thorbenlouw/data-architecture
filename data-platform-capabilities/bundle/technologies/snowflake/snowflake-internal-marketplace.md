---
type: Technology
id: snowflake-internal-marketplace
title: Snowflake Internal Marketplace (organisational listings)
description: A private marketplace inside a Snowflake organisation where teams publish organisational listings as data products for discovery and access requests by other accounts.
aliases: [organizational listings]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-marketplace, internal-data-sharing, data-product-specification, access-requests]
resource: https://docs.snowflake.com/en/user-guide/collaboration/listings/organizational/org-listing-about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration) (primary): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog, Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Marketplace](../databricks/databricks-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product specification](../../capabilities/data-products/data-product-specification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
