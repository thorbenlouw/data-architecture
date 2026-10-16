---
type: Technology
id: tonic-structural
title: Tonic Structural
description: De-identifies and subsets structured production databases into realistic, referentially intact copies for development and testing.
platform: platform-independent
vendor: Tonic.ai
kind: software
availability: ga
realises: [test-data-management, deidentification, synthetic-data]
resource: https://www.tonic.ai/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports many relational databases and warehouses, either self-hosted or in Tonic's cloud. Tonic Fabricate, a separate Tonic.ai product, generates synthetic databases and files from scratch, from a schema or a description, when no production data can be used.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps) (primary): Provide realistic, safe data for development and testing through subsetting, masking or generation.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps): Generate artificial data that keeps the useful properties of real data without exposing real records.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table clones](../google-cloud/gcp-bigquery-table-clones.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake zero-copy cloning](../snowflake/snowflake-zero-copy-cloning.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md), [Informatica Data Masking transformation](../informatica/informatica-data-masking-transformation.md) | [De-identification](../../capabilities/governance/deidentification.md), [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [lakeFS](../open-source/lakefs.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
