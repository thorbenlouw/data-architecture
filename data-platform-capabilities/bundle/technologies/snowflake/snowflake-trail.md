---
type: Technology
id: snowflake-trail
title: Snowflake Trail (event tables, logging, tracing and metrics)
description: Collects logs, OpenTelemetry-style traces and metrics from UDFs, procedures, Snowpark, Native Apps, container services and pipelines into event tables, with Snowsight dashboards.
aliases: [Snowflake event tables]
platform: platform-snowflake
kind: feature
availability: ga
realises: [platform-observability, pipeline-monitoring]
resource: https://docs.snowflake.com/en/developer-guide/logging-tracing/logging-tracing-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A default event table is active in each account. Snowflake Trail is the marketing name for this observability set. The docs mostly describe it as logging and tracing.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Monitor](../microsoft/azure-monitor.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Operational Insights](../informatica/informatica-operational-insights.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
