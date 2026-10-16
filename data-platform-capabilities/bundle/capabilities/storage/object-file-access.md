---
type: Capability
id: object-file-access
title: File-system access to object storage
description: Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.
aliases: [FUSE mounts]
broader: [object-storage]
related: [unstructured-data, model-training, gpu-compute, access-control, agent-tool-access]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A file-system layer translates operations such as open, read, seek and list into object storage requests, so a bucket or prefix appears as a mounted directory. A training script that expects `/data/images/`, or a command-line tool that cannot use the S3 API, can then work on lake files directly. Implementations include FUSE mounts, caching gateways, NFS-style front ends and file systems built into notebooks and container runtimes. Many add a cache so repeated reads, such as each training epoch, skip the object store.

It matters for machine learning, scientific and older tools, and for AI agents that work with files. Without it, teams copy data onto local disks, creating stale and ungoverned duplicates. The catch is behaviour: object stores cannot rename atomically or change bytes in the middle of a file, so emulated file systems act differently from real ones under writes, renames and locks. It suits read-heavy access to files; tables should still be read through their table format.

# Key considerations

- Check which file-system operations are emulated. Renames, appends, random writes and locks may be slow, non-atomic or unsupported.
- Mounts can bypass table-level permissions. Scope the identity behind each mount to the paths its user may see, and log access.
- Caches raise training throughput but add a freshness question: how soon do readers see files that changed in the store?
- Writing table files through a mount skips the table format's commit protocol and can corrupt tables. Mount table locations read-only.

# Questions to ask

- Which tools need file paths rather than an object storage API or SQL?
- Are the workloads read-mostly, or do they write and rename files heavily?
- What throughput do training or batch jobs need, and would a cache reduce cost?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Object storage](object-storage.md) |
| Related | [Access control](../security/access-control.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [GPU and accelerated compute](../compute/gpu-compute.md), [Model training](../machine-learning/model-training.md), [Unstructured data management](../specialised-data/unstructured-data.md) |

# Where it appears

- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 Files](../../technologies/aws/aws-s3-files.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Lake Storage](../../technologies/microsoft/azure-data-lake-storage.md), [OneLake](../../technologies/microsoft/fabric-onelake.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowpark Container Services](../../technologies/snowflake/snowflake-snowpark-container-services.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog volumes](../../technologies/databricks/databricks-volumes.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md) |
