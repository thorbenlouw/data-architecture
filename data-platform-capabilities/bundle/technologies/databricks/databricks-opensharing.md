---
type: Technology
id: databricks-opensharing
title: Databricks OpenSharing
description: Live sharing of tables, views, materialised views, metric views, volumes, models and notebooks with other Databricks accounts, or tabular data with any client through an open protocol, without copying.
formerly: [Delta Sharing]
platform: platform-databricks
kind: managed-service
availability: ga
realises: [external-data-sharing, internal-data-sharing, cross-region-sharing, open-protocol-sharing]
resource: https://docs.databricks.com/aws/en/delta-sharing/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Databricks announced OpenSharing on 10 June 2026 as the successor to the Delta Sharing protocol. The open protocol is now a Linux Foundation project (see the [open-source protocol](../open-source/delta-sharing.md)), and Delta Sharing remains the name of a sub-project within Delta Lake. Recipients authenticate with bearer tokens or OIDC federation. SecureConnect reaches data behind firewalls, and foreign Delta and Iceberg tables can be shared. It underpins [Databricks Marketplace](databricks-marketplace.md) and [Clean Rooms](databricks-clean-rooms.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration) (primary): Share live data with customers, partners and suppliers under agreed terms.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** OpenSharing

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md), [AWS Data Exchange](../aws/aws-data-exchange.md), [Amazon Redshift data sharing](../aws/aws-redshift-data-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Share](../microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Open Data Sharing](../snowflake/snowflake-open-data-sharing.md) (preview), [Snowflake Secure Data Sharing](../snowflake/snowflake-secure-data-sharing.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../snowflake/snowflake-listings.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSharing protocol](../open-source/delta-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Syndigo MDM](../independent/syndigo-mdm.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
