---
type: Technology
id: sap-business-data-cloud
title: SAP Business Data Cloud
description: Managed SaaS data platform that unifies SAP application data as governed data products on a shared object store and exposes it to Datasphere, SAP Analytics Cloud, SAP Databricks and SAP Snowflake without copying.
aliases: [BDC, SAP BDC]
platform: platform-sap
kind: saas
availability: ga
realises: [internal-data-sharing, managed-storage, packaged-analytics]
resource: https://www.sap.com/products/data-cloud.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Existing SAP Datasphere and SAP Analytics Cloud tenants can keep running and move to BDC over time. BDC also delivers intelligent applications, such as People Intelligence and Finance and Spend Intelligence, built on its data products; several were in technology preview in 2025. SAP positions BDC as the data layer of the SAP Business AI Platform. When it agreed to acquire Dremio in May 2026, SAP said it planned to make Apache Iceberg the native table format of BDC, with an open catalogue built on Apache Polaris.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration) (primary): Share live data between teams, accounts and workspaces without copying it.
- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management): Let the platform manage table storage layout, compression and durability internally.
- [Packaged analytics content](../../capabilities/analytics-bi/packaged-analytics.md) (Analytics and BI): Use prebuilt models, metrics and dashboards for a business domain that a vendor delivers and updates.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business Data Cloud, SAP Business AI Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift data sharing](../aws/aws-redshift-data-sharing.md), [AWS Lake Formation](../aws/aws-lake-formation.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake shortcuts](../microsoft/fabric-onelake-shortcuts.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Secure Data Sharing](../snowflake/snowflake-secure-data-sharing.md), [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks OpenSharing](../databricks/databricks-opensharing.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Fabric](../teradata/teradata-fabric.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSharing protocol](../open-source/delta-sharing.md) | [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
