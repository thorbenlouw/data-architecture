---
type: Technology
id: dvc
title: DVC (Data Version Control)
description: Command-line tool that versions datasets and models alongside code in Git, storing the large files in remote storage.
platform: platform-open-source
kind: open-source
availability: ga
realises: [data-versioning, ml-pipelines, experiment-tracking, training-dataset-management]
resource: https://dvc.org/blog/dvc-joins-lakefs-your-questions-answered/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0. Acquired from Iterative by lakeFS (Treeverse) in November 2025, which says it will stay open source under the same licence. File-based; suits ML datasets more than large tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data versioning](../../capabilities/storage/data-versioning.md) (Storage and table management) (primary): Keep and reference past versions of data so you can reproduce results, compare changes or roll back.
- [ML pipelines](../../capabilities/machine-learning/ml-pipelines.md) (Machine learning development): Automate the steps from data preparation to training and evaluation as repeatable pipelines.
- [Experiment tracking](../../capabilities/machine-learning/experiment-tracking.md) (Machine learning development): Record parameters, code versions, data and metrics for each training run so results can be compared and reproduced.
- [Training and evaluation dataset management](../../capabilities/machine-learning/training-dataset-management.md) (Machine learning development): Assemble, version, document and govern the datasets used to train, validate and test models, including evaluation sets for generative AI.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table snapshots](../google-cloud/gcp-bigquery-table-snapshots.md) | [Data versioning](../../capabilities/storage/data-versioning.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Data versioning](../../capabilities/storage/data-versioning.md) |
