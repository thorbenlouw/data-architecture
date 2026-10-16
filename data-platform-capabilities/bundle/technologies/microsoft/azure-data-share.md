---
type: Technology
id: azure-data-share
title: Azure Data Share
description: Shares snapshots of storage and SQL data, or in-place Azure Data Explorer databases, with other Azure tenants under provider control.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [external-data-sharing]
resource: https://learn.microsoft.com/en-us/azure/data-share/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Receives few new features. In-place sharing works only for Azure Data Explorer; other sources are shared as snapshots. [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) is the newer route for OneLake data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration) (primary): Share live data with customers, partners and suppliers under agreed terms.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md), [AWS Data Exchange](../aws/aws-data-exchange.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Open Data Sharing](../snowflake/snowflake-open-data-sharing.md) (preview), [Snowflake Secure Data Sharing](../snowflake/snowflake-secure-data-sharing.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Syndigo MDM](../independent/syndigo-mdm.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
