---
type: Technology
id: aws-snowball-edge
title: AWS Snowball Edge
description: Rugged storage and compute device shipped to a site to load large datasets offline and return them to S3.
aliases: [AWS Snow Family]
platform: platform-aws
kind: managed-service
availability: deprecated
realises: [bulk-data-transfer]
resource: https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html
tags: [aws]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Closed to new customers since November 2025 and no Snow devices are offered for new orders; existing customers are unaffected. AWS points new projects to DataSync (online) and AWS Data Transfer Terminal (bring-your-own-device upload sites).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) (Ingestion and integration) (primary): Move very large datasets into the platform over high-throughput links or physical transfer devices.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Box](../microsoft/azure-data-box.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Transfer Appliance](../google-cloud/gcp-transfer-appliance.md), [Google Cloud Storage Transfer Service](../google-cloud/gcp-storage-transfer-service.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Replication Manager](../cloudera/cloudera-replication-manager.md) | [Bulk and offline transfer](../../capabilities/ingestion-integration/bulk-data-transfer.md) |
