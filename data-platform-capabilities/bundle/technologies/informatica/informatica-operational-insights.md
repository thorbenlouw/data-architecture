---
type: Technology
id: informatica-operational-insights
title: Informatica Operational Insights
description: Monitoring service that shows the performance, health and efficiency of Informatica assets, including registered on-premises PowerCenter and Data Engineering domains as well as IDMC jobs.
platform: platform-informatica
kind: managed-service
availability: ga
realises: [platform-observability, pipeline-monitoring]
resource: https://docs.informatica.com/cloud-common-services/operational-insights/current-version.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Job-level run monitoring for cloud services is in the separate Monitor service. Since August 2026, log, job and troubleshooting MCP servers (the troubleshooting one in preview) also expose operational data to agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Monitor](../microsoft/azure-monitor.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trail (event tables, logging, tracing and metrics)](../snowflake/snowflake-trail.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
