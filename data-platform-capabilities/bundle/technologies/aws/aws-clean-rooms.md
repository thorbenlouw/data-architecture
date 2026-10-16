---
type: Technology
id: aws-clean-rooms
title: AWS Clean Rooms
description: Collaboration service in which organisations run approved SQL or PySpark analyses and ML on combined data without exposing each other's raw records.
aliases: [AWS Clean Rooms ML]
platform: platform-aws
kind: managed-service
availability: ga
realises: [data-clean-rooms, privacy-enhancing-technologies, external-data-sharing]
resource: https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Analysis rules and templates control queries; differential privacy and cryptographic computing add protection; Clean Rooms ML builds lookalike and custom models. Data can stay in S3, Athena or Snowflake, and Entity Resolution provides ID mapping.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md) (Data sharing and collaboration) (primary): Let organisations combine and analyse data jointly while each keeps control over what the others can see.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.
- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration): Share live data with customers, partners and suppliers under agreed terms.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Confidential Clean Rooms](../microsoft/azure-confidential-clean-rooms.md) (preview) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data clean rooms](../google-cloud/gcp-bigquery-data-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Data Clean Rooms](../snowflake/snowflake-data-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Clean Rooms](../databricks/databricks-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
