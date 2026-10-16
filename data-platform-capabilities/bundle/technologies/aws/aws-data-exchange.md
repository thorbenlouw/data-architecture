---
type: Technology
id: aws-data-exchange
title: AWS Data Exchange
description: Marketplace for finding, subscribing to and publishing third-party datasets as files, APIs, Redshift data shares, Lake Formation tables or S3 access.
platform: platform-aws
kind: managed-service
availability: ga
realises: [data-marketplace, external-data-sharing, data-product-metering]
resource: https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Billing and entitlements run through AWS Marketplace; providers can offer private products to named accounts. Internal data marketplaces are better served by SageMaker Catalog.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration) (primary): Publish, find and subscribe to data products and datasets, internally or commercially.
- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration): Share live data with customers, partners and suppliers under agreed terms.
- [Data product usage metering](../../capabilities/data-products/data-product-metering.md) (Data products): Measure how much each consumer uses a data product so it can be billed, charged back or capped.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product usage metering](../../capabilities/data-products/data-product-metering.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Marketplace](../snowflake/snowflake-marketplace.md), [Snowflake Native App Framework](../snowflake/snowflake-native-app-framework.md), [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Marketplace](../databricks/databricks-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
