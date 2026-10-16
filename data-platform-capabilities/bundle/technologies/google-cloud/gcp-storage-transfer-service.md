---
type: Technology
id: gcp-storage-transfer-service
title: Google Cloud Storage Transfer Service
description: Managed, scheduled or event-driven copying of large object and file datasets from other clouds, HTTP sources and on-premises file systems into Cloud Storage.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [bulk-data-transfer, file-ingestion]
resource: https://docs.cloud.google.com/storage-transfer/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports S3, Azure Blob, S3-compatible stores and POSIX file systems through agents, and can transfer between Cloud Storage buckets. It is not an SFTP/AS2 partner exchange service.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration) (primary): Move very large datasets into the platform over high-throughput links or physical transfer devices.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS DataSync](../aws/aws-datasync.md), [Amazon Redshift auto-copy](../aws/aws-redshift-auto-copy.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Box](../microsoft/azure-data-box.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
