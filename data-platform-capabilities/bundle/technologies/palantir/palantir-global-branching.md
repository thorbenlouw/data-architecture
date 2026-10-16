---
type: Technology
id: palantir-global-branching
title: Palantir Global Branching
description: Branching that spans pipelines, the Ontology and applications so a change can be built and tested end to end in isolation and merged after per-resource approval.
formerly: [Foundry Branching]
platform: platform-palantir
kind: feature
availability: ga
realises: [data-branching, environment-promotion, version-control, ephemeral-environments]
resource: https://www.palantir.com/docs/foundry/foundry-branching/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Datasets built on a branch do not affect main; actions can run on a branch without writing to production. Complements release management through DevOps and Marketplace.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data branching and tagging](../../capabilities/storage/data-branching.md) (Storage and table management) (primary): Create isolated branches and named tags of data, Git-style, to develop and test changes before merging them.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Git integration](../microsoft/fabric-git-integration.md) | [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md), [Version control integration](../../capabilities/development-lifecycle/version-control.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakebase](../databricks/databricks-lakebase.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [lakeFS](../open-source/lakefs.md), [Project Nessie](../open-source/project-nessie.md) | [Data branching and tagging](../../capabilities/storage/data-branching.md), [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) |
