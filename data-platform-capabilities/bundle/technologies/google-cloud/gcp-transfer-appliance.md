---
type: Technology
id: gcp-transfer-appliance
title: Google Cloud Transfer Appliance
description: Rentable, encrypted storage device shipped to a customer site to move hundreds of terabytes to petabytes into Cloud Storage offline.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [bulk-data-transfer]
resource: https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration) (primary): Move very large datasets into the platform over high-throughput links or physical transfer devices.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS DataSync](../aws/aws-datasync.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Box](../microsoft/azure-data-box.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
