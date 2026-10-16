---
type: Technology
id: aws-cloudwatch
title: Amazon CloudWatch
description: Collects metrics, logs and traces from AWS services and applications, with alarms, dashboards, anomaly detection and log queries.
aliases: [CloudWatch Logs Insights]
platform: platform-aws
kind: managed-service
availability: ga
realises: [platform-observability, pipeline-monitoring, query-performance-analysis, observability-analytics]
resource: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Glue, EMR, MWAA, Redshift, SageMaker AI and AgentCore publish metrics and logs here; Logs Insights queries logs, and generative AI observability views trace model and agent calls.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Monitor](../microsoft/azure-monitor.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trail (event tables, logging, tracing and metrics)](../snowflake/snowflake-trail.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Operational Insights](../informatica/informatica-operational-insights.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
