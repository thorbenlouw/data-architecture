---
type: Technology
id: lakefs
title: lakeFS
description: Version control layer over object storage that gives data lakes Git-like branches, commits, merges and rollbacks, independent of file or table format.
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-branching, test-data-management, ephemeral-environments]
resource: https://docs.lakefs.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by Treeverse, which also acquired [DVC](../open-source/dvc.md) in November 2025. Works through an S3-compatible gateway. A zero-copy branch of production data gives each developer or test run an isolated environment that is merged or discarded afterwards. Enterprise features such as RBAC and SSO are in lakeFS Enterprise and lakeFS Cloud.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data branching and tagging](../../capabilities/storage/data-branching.md) (Storage and table management) (primary): Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Global Branching](../palantir/palantir-global-branching.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
