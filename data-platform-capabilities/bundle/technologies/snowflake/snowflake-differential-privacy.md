---
type: Technology
id: snowflake-differential-privacy
title: Snowflake differential privacy
description: Privacy policies that add calibrated noise to aggregate results on protected tables and track each analyst's cumulative privacy loss against a budget.
aliases: [Snowflake privacy policies]
platform: platform-snowflake
kind: feature
availability: ga
realises: [privacy-enhancing-technologies]
resource: https://docs.snowflake.com/en/user-guide/diff-privacy/differential-privacy-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Generally available since October 2024 and applied through privacy policies. Requires Enterprise Edition. Only some query shapes and data types are allowed on privacy-protected tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance) (primary): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Clean Rooms](../aws/aws-clean-rooms.md) | [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Confidential Clean Rooms](../microsoft/azure-confidential-clean-rooms.md) (preview) | [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data clean rooms](../google-cloud/gcp-bigquery-data-clean-rooms.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Clean Rooms](../databricks/databricks-clean-rooms.md) | [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [MOSTLY AI Data Intelligence Platform](../independent/mostly-ai-data-intelligence-platform.md) | [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) |
