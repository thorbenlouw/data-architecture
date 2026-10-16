---
type: Technology
id: informatica-powercenter-cloud-edition
title: Informatica PowerCenter Cloud Edition (PCCE)
description: Modernisation bundle that runs PowerCenter workloads under IDMC management (CDI-PC), converts PowerCenter assets to native Cloud Data Integration (PC2CDI) and checks the converted output with Data Validation.
aliases: [PCCE]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [platform-migration, code-translation]
resource: https://www.informatica.com/about-us/news/news-releases/2023/09/20230919-informatica-accelerates-cloud-modernization-journey-with-powercenter-cloud-edition.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA since September 2023. Informatica's services offer assessment (PC2IDMC) and automated conversion and validation of assets. Conversion is described as highly automated, but SQL overrides and performance tuning still need manual work.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations) (primary): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, PowerCenter

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Transform](../aws/aws-transform.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebridge](../databricks/databricks-lakebridge.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
