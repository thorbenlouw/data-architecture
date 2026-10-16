---
type: Technology
id: databricks-clean-rooms
title: Databricks Clean Rooms
description: Isolated serverless environments where up to ten organisations share data through OpenSharing and run notebooks that every party has approved. No party sees the others' underlying data.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [data-clean-rooms, privacy-enhancing-technologies]
resource: https://docs.databricks.com/aws/en/clean-rooms/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Clean rooms work across clouds and regions. Packaged clean rooms (GA July 2026) use a provider-consumer model rather than equal privileges. Collaborators cannot be added after creation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md) (Data sharing and collaboration) (primary): Let organisations combine and analyse data jointly while each keeps control over what the others can see.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** OpenSharing

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Confidential Clean Rooms](../microsoft/azure-confidential-clean-rooms.md) (preview) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data clean rooms](../google-cloud/gcp-bigquery-data-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Data Clean Rooms](../snowflake/snowflake-data-clean-rooms.md), [Snowflake aggregation policies](../snowflake/snowflake-aggregation-policies.md), [Snowflake differential privacy](../snowflake/snowflake-differential-privacy.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
