---
type: Technology
id: informatica-data-validation
title: Informatica Data Validation
description: Compares two data sets through repeatable test cases and test suites to verify that integration or migration output is complete and accurate, with reports and REST APIs.
aliases: [CDV]
formerly: [Cloud Data Validation]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [data-reconciliation, data-testing]
resource: https://docs.informatica.com/integration-cloud/data-validation/current-version.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Mainly used to prove PowerCenter-to-CDI conversions and warehouse migrations. Test cases can reuse saved SQL queries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) (Data quality and observability) (primary): Prove that data moved between systems is complete and correct using counts, totals and record matching.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, PowerCenter

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md) | [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Migration Service](../google-cloud/gcp-bigquery-migration-service.md) | [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebridge](../databricks/databricks-lakebridge.md) | [Data reconciliation](../../capabilities/data-quality/data-reconciliation.md) |
