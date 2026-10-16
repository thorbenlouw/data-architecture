---
type: Technology
id: aws-datasync
title: AWS DataSync
description: Online transfer service that copies files and objects between on-premises storage, other clouds and AWS storage with verification and incremental runs.
platform: platform-aws
kind: managed-service
availability: ga
realises: [bulk-data-transfer, file-ingestion]
resource: https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports NFS, SMB, HDFS and S3-compatible object stores; one task can fill a 10 Gbps link. AWS recommends it as the online replacement for Snowball Edge. DataSync Discovery has reached end of support.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration) (primary): Move very large datasets into the platform over high-throughput links or physical transfer devices.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Box](../microsoft/azure-data-box.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md), [Google Cloud Transfer Appliance](../google-cloud/gcp-transfer-appliance.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md), [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica File Ingestion and Replication](../informatica/informatica-file-ingestion-and-replication.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
