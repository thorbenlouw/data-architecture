---
type: Capability
id: data-versioning
title: Data versioning
description: Keep and reference past versions of data so you can reproduce results, compare changes or roll back.
broader: [storage]
related: [backup-restore, experiment-tracking, model-lineage, data-retention, ci-cd]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data versioning keeps earlier states of data addressable, so a query, model or report can refer to "orders at version 412" or "the training set tagged `q3-2026`" and get exactly that data back. Most implementations use the snapshot metadata of table formats or managed storage. Unchanged files are shared between versions, so history costs only the data that changed. Versioning can apply to one table, as with time travel; to sets of tables, through branches and tags in a catalogue; or to files and folders, through Git-like data version control tools.

It supports reproducible ML training and regulatory reporting, quick recovery from bad loads, and showing what a report held on a given date. The variants differ in scope and control: time travel looks back over automatic history, cloning makes an independent copy from a point, and branching adds isolated lines of change that can be merged. Versioning is not backup, because history usually lives in the same storage and account as live data and expires on a schedule.

# Key considerations

- History costs storage in proportion to how much data changes. Heavily updated tables can hold several times their live size in old versions.
- Retention windows must balance reproducibility against deletion duties. Personal data must not outlive its permitted period in old versions.
- Reproducing a result needs code and configuration versions as well as data. Record which data versions each run used.
- Versions kept beside live data share its failure modes. Keep separate backups for disaster recovery.

# Questions to ask

- Which results must be reproducible, and for how long: models, regulatory submissions, published reports?
- How often have bad loads needed rolling back, and how was it done?
- Do teams need to test changes against production data without affecting it?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Narrower | [Data branching and tagging](data-branching.md), [Time travel](time-travel.md), [Zero-copy cloning](zero-copy-cloning.md) |
| Related | [Machine learning development](../machine-learning/machine-learning.md), [Backup and restore](../platform-operations/backup-restore.md), [Bitemporal data](../specialised-data/temporal-data.md), [CI/CD](../development-lifecycle/ci-cd.md), [Data labelling](../machine-learning/data-labelling.md), [Experiment tracking](../machine-learning/experiment-tracking.md), [Model evaluation](../machine-learning/model-evaluation.md), [Model lineage](../metadata/model-lineage.md), [Multimodal data formats](multimodal-data-formats.md), [Retention and disposal](../governance/data-retention.md) |
| Needed by | [Model lineage](../metadata/model-lineage.md), [Training and evaluation dataset management](../machine-learning/training-dataset-management.md) |

# Where it appears

- **Personas:** [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery table snapshots](../../technologies/google-cloud/gcp-bigquery-table-snapshots.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry](../../technologies/palantir/palantir-foundry.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DVC (Data Version Control)](../../technologies/open-source/dvc.md), [Lance](../../technologies/open-source/lance.md) |

Narrower capabilities are realised by a further 20 technologies; see their pages.
