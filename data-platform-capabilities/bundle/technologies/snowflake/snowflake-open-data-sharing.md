---
type: Technology
id: snowflake-open-data-sharing
title: Snowflake Open Data Sharing
description: Shares Iceberg tables as live, read-only data with external consumers outside Snowflake, who read them through standard Iceberg REST Catalog APIs using a programmatic access token.
platform: platform-snowflake
kind: feature
availability: preview
realises: [external-data-sharing, engine-interoperability, open-protocol-sharing]
resource: https://docs.snowflake.com/user-guide/open-data-sharing
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public preview since August 2026, limited to the provider's region and to PAT authentication. Consuming Delta Shares in Horizon Catalog (the inbound direction) became GA in July 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration) (primary): Share live data with customers, partners and suppliers under agreed terms.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** preview  
**Product family:** Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md), [AWS Data Exchange](../aws/aws-data-exchange.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Share](../microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md), [Google Cloud Lakehouse](../google-cloud/gcp-lakehouse.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Syndigo MDM](../independent/syndigo-mdm.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
