---
type: Technology
id: azure-data-box
title: Azure Data Box
description: Physical appliances shipped to a site to move terabytes to petabytes of data into Azure Storage offline.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [bulk-data-transfer]
resource: https://learn.microsoft.com/en-us/azure/databox/data-box-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration) (primary): Move very large datasets into the platform over high-throughput links or physical transfer devices.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS DataSync](../aws/aws-datasync.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Transfer Appliance](../google-cloud/gcp-transfer-appliance.md), [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
