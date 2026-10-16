---
type: Technology
id: snowflake-listings
title: Snowflake listings (with Cross-Cloud Auto-Fulfillment)
description: Package a share, app or service with descriptive metadata as a data product for chosen accounts, replicating it automatically to consumers in other regions and clouds.
aliases: [Cross-Cloud Auto-Fulfillment]
platform: platform-snowflake
kind: feature
availability: ga
realises:
- external-data-sharing
- cross-region-sharing
- data-product-specification
- data-product-lifecycle
- data-product-metering
resource: https://docs.snowflake.com/en/collaboration/collaboration-listings-about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Listings can be private, public on the Marketplace or organisational, and can be paid or free. Providers can see consumer usage, including LISTING_ACCESS_HISTORY.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration) (primary): Share live data with customers, partners and suppliers under agreed terms.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.
- [Data product specification](../../capabilities/data-products/data-product-specification.md) (Data products): Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
- [Data product lifecycle management](../../capabilities/data-products/data-product-lifecycle.md) (Data products): Version, publish, deprecate and retire data products with notice to their consumers.
- [Data product usage metering](../../capabilities/data-products/data-product-metering.md) (Data products): Measure how much each consumer uses a data product so it can be billed, charged back or capped.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md), [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data product usage metering](../../capabilities/data-products/data-product-metering.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Share](../microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Data product usage metering](../../capabilities/data-products/data-product-metering.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Syndigo MDM](../independent/syndigo-mdm.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
