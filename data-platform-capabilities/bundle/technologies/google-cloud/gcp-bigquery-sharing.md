---
type: Technology
id: gcp-bigquery-sharing
title: BigQuery sharing
description: Data exchange service where publishers list datasets, views, models and Pub/Sub topics for subscribers, who get linked read-only copies without data duplication.
formerly: [Analytics Hub]
platform: platform-google-cloud
kind: feature
availability: ga
realises:
- external-data-sharing
- internal-data-sharing
- data-marketplace
- cross-region-sharing
- data-product-metering
resource: https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exchanges can be private or public, and listings can be sold through Google Cloud Marketplace. Shared Pub/Sub topics give streaming sharing. Listings can be published in Omni regions on AWS and Azure. Egress controls stop subscribers copying data out.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration) (primary): Share live data with customers, partners and suppliers under agreed terms.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.
- [Data product usage metering](../../capabilities/data-products/data-product-metering.md) (Data products): Measure how much each consumer uses a data product so it can be billed, charged back or capped.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md), [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data product usage metering](../../capabilities/data-products/data-product-metering.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Share](../microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md), [Snowflake Secure Data Sharing](../snowflake/snowflake-secure-data-sharing.md), [Snowflake Open Data Sharing](../snowflake/snowflake-open-data-sharing.md) (preview) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Data product usage metering](../../capabilities/data-products/data-product-metering.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Syndigo MDM](../independent/syndigo-mdm.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
