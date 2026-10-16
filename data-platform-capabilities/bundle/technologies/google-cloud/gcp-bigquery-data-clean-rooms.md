---
type: Technology
id: gcp-bigquery-data-clean-rooms
title: BigQuery data clean rooms
description: Built on BigQuery sharing, lets several parties contribute data that others can query only through analysis rules or approved query templates.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-clean-rooms, privacy-enhancing-technologies]
resource: https://docs.cloud.google.com/bigquery/docs/data-clean-rooms
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Analysis rules include aggregation thresholds, differential privacy, join restrictions and list overlap. Query templates (GA August 2026) restrict subscribers to predefined table-valued functions. Clean rooms are single-region and limited to 100 shared resources.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md) (Data sharing and collaboration) (primary): Let organisations combine and analyse data jointly while each keeps control over what the others can see.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Confidential Clean Rooms](../microsoft/azure-confidential-clean-rooms.md) (preview) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Data Clean Rooms](../snowflake/snowflake-data-clean-rooms.md), [Snowflake aggregation policies](../snowflake/snowflake-aggregation-policies.md), [Snowflake differential privacy](../snowflake/snowflake-differential-privacy.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Clean Rooms](../databricks/databricks-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
