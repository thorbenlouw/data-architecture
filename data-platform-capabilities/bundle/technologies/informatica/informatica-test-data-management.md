---
type: Technology
id: informatica-test-data-management
title: Informatica Test Data Management (TDM)
description: On-premises product for configuring data subsetting, masking, synthetic data generation and sensitive data discovery for test environments from one web console.
aliases: [TDM]
platform: platform-informatica
kind: software
availability: ga
realises: [test-data-management, synthetic-data, deidentification]
resource: https://docs.informatica.com/data-security-group/test-data-management/10-5/user-guide/introduction-to-test-data-management/tdm-architecture/tdm-tools.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It runs on the Informatica on-premises domain and the PowerCenter engine (10.5 line). In IDMC, persistent masking of non-production copies is done with the [Data Masking transformation](informatica-data-masking-transformation.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps) (primary): Provide realistic, safe data for development and testing through subsetting, masking or generation.
- [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md) (Development and DataOps): Generate artificial data that keeps the useful properties of real data without exposing real records.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table clones](../google-cloud/gcp-bigquery-table-clones.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake zero-copy cloning](../snowflake/snowflake-zero-copy-cloning.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [lakeFS](../open-source/lakefs.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tonic Structural](../independent/tonic-structural.md), [Perforce Delphix](../independent/perforce-delphix.md), [K2view Data Product Platform](../independent/k2view-data-product-platform.md) | [De-identification](../../capabilities/governance/deidentification.md), [Synthetic data generation](../../capabilities/development-lifecycle/synthetic-data.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
