---
type: Technology
id: databricks-marketplace
title: Databricks Marketplace
description: An exchange for publishing and finding datasets, AI models, notebooks, apps and MCP servers, either publicly or through private exchanges, delivered with OpenSharing.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [data-marketplace, application-sharing]
resource: https://docs.databricks.com/aws/en/marketplace/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Private exchanges can act as an internal data product marketplace. Listing analytics are available as system tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration) (primary): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Data application distribution](../../capabilities/data-sharing/application-sharing.md) (Data sharing and collaboration): Package code, models, interfaces and data as installable applications that run in the consumer's environment.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** OpenSharing

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Marketplace](../snowflake/snowflake-marketplace.md), [Snowflake Native App Framework](../snowflake/snowflake-native-app-framework.md), [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Data application distribution](../../capabilities/data-sharing/application-sharing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data application distribution](../../capabilities/data-sharing/application-sharing.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
