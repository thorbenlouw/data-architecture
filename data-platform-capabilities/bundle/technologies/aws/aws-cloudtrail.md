---
type: Technology
id: aws-cloudtrail
title: AWS CloudTrail
description: Records API calls and data-access events across an account or organisation to S3 and CloudWatch Logs, with integrity validation.
aliases: [AWS CloudTrail Lake]
platform: platform-aws
kind: managed-service
availability: ga
realises: [audit-logging, compliance-evidence]
resource: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data events capture S3 object, Lake Formation and other data-plane access. CloudTrail Lake has been closed to new customers since March 2026; query trails with Athena instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access) (primary): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Audit](../microsoft/purview-audit.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Access History](../snowflake/snowflake-access-history.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
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
