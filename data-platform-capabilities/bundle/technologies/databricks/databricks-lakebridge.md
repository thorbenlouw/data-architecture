---
type: Technology
id: databricks-lakebridge
title: Lakebridge
description: A Databricks Labs migration toolkit. It assesses legacy warehouse and ETL estates, transpiles their SQL and ETL code to Databricks, and reconciles the migrated data against the source.
formerly: [Remorph]
platform: platform-databricks
kind: open-source
availability: ga
realises: [platform-migration, data-reconciliation, code-translation]
resource: https://databrickslabs.github.io/lakebridge/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Lakebridge combines the Remorph project with technology from the 2025 BladeBridge acquisition. As a Labs project it does not have the support terms of the core product. Its analyser output can be loaded into the agentic code converter.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations) (primary): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
- [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) (Data quality and observability): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Code and SQL translation](../../capabilities/platform-operations/code-translation.md) (Platform operations): Convert SQL dialects, stored procedures and ETL jobs automatically to run on a target platform.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Transform](../aws/aws-transform.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter Cloud Edition (PCCE)](../informatica/informatica-powercenter-cloud-edition.md) | [Code and SQL translation](../../capabilities/platform-operations/code-translation.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
