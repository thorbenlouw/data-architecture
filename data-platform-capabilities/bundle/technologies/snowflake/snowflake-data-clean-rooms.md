---
type: Technology
id: snowflake-data-clean-rooms
title: Snowflake Data Clean Rooms
description: Collaborations defined in YAML, in which owners, data providers and analysis runners combine data through approved templates without exposing raw rows to one another.
aliases: [Snowflake DCR]
formerly: [Samooha]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-clean-rooms, privacy-enhancing-technologies]
resource: https://docs.snowflake.com/en/user-guide/cleanrooms/introduction
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Built on Samooha, which Snowflake acquired in 2023. Data providers need Enterprise Edition. Not available in government or VPS deployments. Collaborators in other regions need Cross-Cloud Auto-Fulfillment. A DCR Agent is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md) (Data sharing and collaboration) (primary): Let organisations combine and analyse data jointly while each keeps control over what the others can see.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Confidential Clean Rooms](../microsoft/azure-confidential-clean-rooms.md) (preview) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data clean rooms](../google-cloud/gcp-bigquery-data-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Clean Rooms](../databricks/databricks-clean-rooms.md) | [Data clean rooms](../../capabilities/data-sharing/data-clean-rooms.md), [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
