---
type: Technology
id: snowflake-secure-data-sharing
title: Snowflake Secure Data Sharing
description: Shares live, read-only database objects with other Snowflake accounts through shares, without copying data, with consumers paying for their own compute.
platform: platform-snowflake
kind: feature
availability: ga
realises: [internal-data-sharing, external-data-sharing]
resource: https://docs.snowflake.com/en/user-guide/data-sharing-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Direct shares work only within one region. Reader accounts let the provider share with organisations that do not have Snowflake, at the provider's cost. Iceberg and Delta-based tables can be shared.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration) (primary): Share live data between teams, accounts and workspaces without copying it.
- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration): Share live data with customers, partners and suppliers under agreed terms.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift data sharing](../aws/aws-redshift-data-sharing.md), [AWS Lake Formation](../aws/aws-lake-formation.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md), [Azure Data Share](../microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../microsoft/fabric-external-data-sharing.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [External data sharing](../../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud](../sap/sap-business-data-cloud.md), [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSharing protocol](../open-source/delta-sharing.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
