---
type: Technology
id: aws-s3-files
title: Amazon S3 Files
description: Presents an existing S3 bucket as a shared file system so file-based applications and agents can read and write the same data that S3 APIs see.
platform: platform-aws
kind: feature
availability: ga
realises: [object-file-access, unstructured-data]
resource: https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-s3-files
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Launched April 2026 and built on Amazon EFS. Removes the need to copy lake data into a separate file system for tools that expect POSIX-style access; AgentCore Runtime and harness can mount it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management) (primary): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon S3

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Lake Storage](../microsoft/azure-data-lake-storage.md), [OneLake](../microsoft/fabric-onelake.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage](../google-cloud/gcp-cloud-storage.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark Container Services](../snowflake/snowflake-snowpark-container-services.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog volumes](../databricks/databricks-volumes.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Gravitino](../open-source/apache-gravitino.md) | [File-system access to object storage](../../capabilities/storage/object-file-access.md) |
