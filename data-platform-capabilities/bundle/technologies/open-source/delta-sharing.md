---
type: Technology
id: delta-sharing
title: OpenSharing protocol
description: Open protocol, the successor to Delta Sharing, for sharing live tables, unstructured data, AI models and agent skills with other organisations and tools without copying the data.
aliases: [OpenSharing, OpenSharing Project, Delta Sharing protocol]
formerly: [Delta Sharing]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [open-protocol-sharing, internal-data-sharing, cross-region-sharing]
resource: https://www.opensharing.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Delta Sharing was created by Databricks in 2021 as an Apache 2.0 sub-project of Delta Lake. On 10 June 2026 Databricks contributed it to the Linux Foundation as the OpenSharing project, which extends the protocol from tables to unstructured data volumes, AI models and agent skills, and adds support for Iceberg REST catalogue clients. Recipients read shared data with open connectors for pandas, Spark, Power BI, Tableau and other tools without running Databricks.

Databricks' managed implementation is [OpenSharing](../databricks/databricks-opensharing.md), and storage vendors such as MinIO offer managed OpenSharing services. The open reference server is basic, so production sharing usually runs on a managed implementation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration) (primary): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md) (Data sharing and collaboration): Share data with consumers on other clouds or regions, replicating it where needed.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift data sharing](../aws/aws-redshift-data-sharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Open Data Sharing](../snowflake/snowflake-open-data-sharing.md) (preview) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [Cross-region and cross-cloud sharing](../../capabilities/data-sharing/cross-region-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
