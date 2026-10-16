---
type: Capability
id: zero-copy-cloning
title: Zero-copy cloning
description: Create an instant copy of a table, schema or database that shares storage with the original until either changes.
aliases: [shallow clone, table clone]
broader: [data-versioning, development-lifecycle]
related: [test-data-management, ci-cd, environment-promotion, deidentification, time-travel]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A clone is a new table, schema or database whose metadata points at the same data files as the source at the moment of cloning. Cloning a 50 TB database takes seconds and adds almost no storage. After that, the two change independently: when either side changes data, new files are written for that side only, so storage grows only with the changes. Some platforms also offer a deep clone that copies the files, so the clone no longer depends on the source's retention or deletions.

Cloning makes it cheap to give developers and CI pipelines full-size, realistic environments, to snapshot data before a risky migration, or to freeze a dataset for an audit or a training run. It differs from branching in that a clone is an independent object with no built-in way to merge back into the source. Clones of production data carry its sensitive content, so they need the same or stricter access controls, and masking when used for development.

# Key considerations

- Clones may not copy grants, tags or masking policies. Check which governance settings travel with the clone.
- Shallow clones depend on the source's files. Expiring or vacuuming the source can break them unless the platform tracks shared files.
- Forgotten clones grow in storage as the source changes. Give clones made by CI or developers owners and expiry dates.
- Privacy rules often forbid production data in development. Combine cloning with masking, or use synthetic data instead.

# Questions to ask

- How do developers and tests get realistic data today, and how long does it take?
- Are there rules about where copies of production data may be used?
- Would CI pipelines benefit from building each change against a fresh clone of production?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Data versioning](data-versioning.md), [Development and DataOps](../development-lifecycle/development-lifecycle.md) |
| Related | [Backup and restore](../platform-operations/backup-restore.md), [CI/CD](../development-lifecycle/ci-cd.md), [Data branching and tagging](data-branching.md), [De-identification](../governance/deidentification.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Ephemeral development environments](../development-lifecycle/ephemeral-environments.md), [Test data management](../development-lifecycle/test-data-management.md), [Time travel](time-travel.md) |

# Where it appears

- **Patterns:** [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Path to live](../../maturity/track-path-to-live.md) (from level 3, Defined) · [Storage and table management](../../maturity/track-storage.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Aurora cloning | [Amazon Aurora](../../technologies/aws/aws-aurora.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse zero-copy table clone](../../technologies/microsoft/fabric-warehouse-zero-copy-clone.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | table clones | [BigQuery table clones](../../technologies/google-cloud/gcp-bigquery-table-clones.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake zero-copy cloning](../../technologies/snowflake/snowflake-zero-copy-cloning.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks table clone (shallow and deep clone)](../../technologies/databricks/databricks-table-clone.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Perforce Delphix](../../technologies/independent/perforce-delphix.md) |
