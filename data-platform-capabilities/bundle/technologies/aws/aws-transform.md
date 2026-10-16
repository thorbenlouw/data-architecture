---
type: Technology
id: aws-transform
title: AWS Transform
description: Agentic AI service that plans and carries out migration and modernisation work for mainframe, VMware and .NET workloads.
platform: platform-aws
kind: managed-service
availability: ga
realises: [platform-migration, ai-assisted-development]
resource: https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

No additional charge. Relevant to data architects mainly for mainframe and server estates whose data moves to AWS; database schema conversion itself sits in DMS Schema Conversion.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform migration](../../capabilities/platform-operations/platform-migration.md) (Platform operations) (primary): Assess, convert and move workloads, code and data from a legacy platform to a new one, with automated validation.
- [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) (Development and DataOps): Use AI assistants to write, explain, fix and optimise code, SQL and pipelines.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Fabric](../microsoft/fabric-copilot.md) (preview) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md), [Gemini in BigQuery](../google-cloud/gcp-gemini-in-bigquery.md) | [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md), [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebridge](../databricks/databricks-lakebridge.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter Cloud Edition (PCCE)](../informatica/informatica-powercenter-cloud-edition.md), [CLAIRE Copilot for Data Integration](../informatica/informatica-claire-copilot-data-integration.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md), [AI-assisted development](../../capabilities/development-lifecycle/ai-assisted-development.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Warehouse in SAP Business Data Cloud](../sap/sap-business-warehouse-bdc.md), [SAP Datasphere](../sap/sap-datasphere.md) | [Platform migration](../../capabilities/platform-operations/platform-migration.md) |
