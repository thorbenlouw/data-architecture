---
type: Technology
id: aws-redshift-data-sharing
title: Amazon Redshift data sharing
description: Shares live tables and views between Redshift warehouses in the same or other accounts and Regions without copying, so separate compute can read the same data.
platform: platform-aws
kind: feature
availability: ga
realises: [internal-data-sharing, workload-isolation, cross-region-sharing]
resource: https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Underpins multi-warehouse architectures (separate ETL and BI warehouses), including remote materialised views and DDL routed through concurrency scaling (2026). Shares can be licensed to external subscribers through AWS Data Exchange and governed through Lake Formation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration) (primary): Share live data between teams, accounts and workspaces without copying it.
- [Workload isolation](../../capabilities/compute/workload-isolation.md) (Query and compute): Run different workloads on separate compute so one cannot slow or starve another.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Secure Data Sharing](../snowflake/snowflake-secure-data-sharing.md), [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud](../sap/sap-business-data-cloud.md), [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSharing protocol](../open-source/delta-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
