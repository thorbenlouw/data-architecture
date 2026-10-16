---
type: Capability
id: platform-observability
title: Platform observability
description: Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
broader: [platform-operations]
related: [data-observability, observability-analytics, genai-observability, audit-logging, model-monitoring]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The platform produces logs from jobs and services, metrics such as queue length, CPU and memory use, query duration and failure counts, and traces that follow one request or pipeline run across components. Observability collects these signals and makes them searchable, chartable and alertable in one place. An operator investigating a slow morning load can see that the warehouse started queueing queries at 06:00, that a new job began at the same time, and who launched it. OpenTelemetry is the common open standard for exporting such signals.

This is how the platform team meets service levels and finds problems before users report them. Coverage is often uneven: managed services show some signals in their own consoles and others only in system tables, so organisations route them to a central monitoring tool. Platform observability asks whether jobs, queries and services are healthy; data observability asks whether the data they produce is correct and on time. Both are needed, and incidents are resolved faster when their alerts can be correlated.

# Key considerations

- Pick one tool as the place for alerts and dashboards and export platform signals to it, rather than asking operators to watch several consoles.
- Log storage costs grow quickly. Keep detailed logs for short periods and summarised metrics for longer.
- Define service level objectives first, such as daily loads finished by 07:00, and alert on them rather than on every low-level metric.
- Logs can contain query text with personal data or secrets. Apply access control and masking to observability data too.

# Questions to ask

- How do you learn today that the platform is slow or failing: from monitoring or from users?
- Which monitoring and incident tools does the organisation already use?
- What service levels has the platform team committed to?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [Pipeline monitoring and alerting](pipeline-monitoring.md), [Platform incident management](platform-incident-management.md), [Query and job performance analysis](query-performance-analysis.md), [Usage and system telemetry](system-telemetry.md) |
| Related | [Query and compute](../compute/compute.md), [ML operations](../mlops/mlops.md), [Security and access](../security/security.md), [Audit logging](../security/audit-logging.md), [Data observability](../data-quality/data-observability.md), [Generative AI observability](../generative-ai/genai-observability.md), [Model monitoring](../mlops/model-monitoring.md), [Observability data analytics](../specialised-data/observability-analytics.md), [Resilience and recovery testing](resilience-testing.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 2)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 2, Managed)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 10 – Detection; Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon CloudWatch](../../technologies/aws/aws-cloudwatch.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Monitor](../../technologies/microsoft/azure-monitor.md), [Fabric workspace monitoring](../../technologies/microsoft/fabric-workspace-monitoring.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Logging](../../technologies/google-cloud/gcp-cloud-logging.md), [Google Cloud Monitoring](../../technologies/google-cloud/gcp-cloud-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowflake Trail (event tables) | [Snowflake Trail (event tables, logging, tracing and metrics)](../../technologies/snowflake/snowflake-trail.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse data source plugin for Grafana](../../technologies/clickhouse/clickhouse-grafana-plugin.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Operational Insights](../../technologies/informatica/informatica-operational-insights.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Observability](../../technologies/cloudera/cloudera-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Viewpoint](../../technologies/teradata/teradata-viewpoint.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenTelemetry](../../technologies/open-source/opentelemetry.md) |

Narrower capabilities are realised by a further 31 technologies; see their pages.
