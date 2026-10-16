---
type: Technology
id: gcp-cloud-logging
title: Google Cloud Logging
description: Collects, stores and routes logs, including Cloud Audit Logs of admin and data access, with Log Analytics for SQL queries over logs.
aliases: [Cloud Audit Logs]
formerly: [Stackdriver Logging]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [audit-logging, platform-observability, observability-analytics]
resource: https://docs.cloud.google.com/logging/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data Access audit logs must be enabled explicitly for most services. Log sinks route logs to BigQuery, Cloud Storage or Pub/Sub, and log buckets can be locked for retention.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access) (primary): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Google Cloud Observability

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudTrail](../aws/aws-cloudtrail.md), [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Audit](../microsoft/purview-audit.md), [Azure Monitor](../microsoft/azure-monitor.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Access History](../snowflake/snowflake-access-history.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Privacera](../independent/privacera.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
