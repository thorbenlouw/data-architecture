---
type: Technology
id: informatica-cloud-data-marketplace
title: Informatica Cloud Data Marketplace (CDMP)
description: Internal data shop where owners publish data collections with terms of use, and consumers search, compare, order and receive data through approval and delivery workflows.
aliases: [CDMP]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [data-marketplace, access-requests, internal-data-sharing, data-usage-rights]
resource: https://trailhead.salesforce.com/content/learn/modules/informatica-cloud-data-marketplace-basics/discover-and-access-data-with-cloud-data-marketplace
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It uses CDGC metadata, glossary terms and data quality results. Combined with Data Access Management, each order can be delivered with filters and de-identification suited to its stated use. An Order Management MCP server, added in September 2026, lets agents raise access requests.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration) (primary): Publish, find and subscribe to data products and datasets, internally or commercially.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) (Data sharing and collaboration): Share live data between teams, accounts and workspaces without copying it.
- [Data licensing and usage rights](../../capabilities/governance/data-usage-rights.md) (Governance and compliance): Record licence terms and permitted uses of datasets and check use against them, including for model training.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exchange](../aws/aws-data-exchange.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery sharing](../google-cloud/gcp-bigquery-sharing.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake Marketplace](../snowflake/snowflake-marketplace.md), [Snowflake Cortex Knowledge Extensions](../snowflake/snowflake-cortex-knowledge-extensions.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [Internal data sharing](../../capabilities/data-sharing/internal-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Marketplace](../databricks/databricks-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud data products](../sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir DevOps and Marketplace](../palantir/palantir-devops-marketplace.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Denodo Platform](../independent/denodo-platform.md), [Alation Intelligence Operating System (AIOS)](../independent/alation-aios.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
