---
type: Technology
id: azure-confidential-clean-rooms
title: Azure Confidential Clean Rooms
description: Lets several organisations run approved Spark SQL analytics over combined datasets inside attested trusted execution environments without exposing raw data.
platform: platform-microsoft
kind: managed-service
availability: preview
realises: [data-clean-rooms, privacy-enhancing-technologies]
resource: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-clean-rooms
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Limited preview, not for production or regulated personal data yet. Supports column allow-lists and minimum row-count thresholds; the code is open source.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md) (Data sharing and collaboration) (primary): Let organisations combine and analyse data jointly while each keeps control over what the others can see.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data clean rooms](../google-cloud/gcp-bigquery-data-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Data Clean Rooms](../snowflake/snowflake-data-clean-rooms.md), [Snowflake aggregation policies](../snowflake/snowflake-aggregation-policies.md), [Snowflake differential privacy](../snowflake/snowflake-differential-privacy.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Clean Rooms](../databricks/databricks-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
