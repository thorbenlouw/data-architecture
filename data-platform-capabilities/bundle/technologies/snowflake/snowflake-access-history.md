---
type: Technology
id: snowflake-access-history
title: Snowflake Access History
description: An ACCOUNT_USAGE view that records which columns each query read and which objects it wrote, including through views and policies.
platform: platform-snowflake
kind: feature
availability: ga
realises: [audit-logging, usage-metadata]
resource: https://docs.snowflake.com/en/user-guide/access-history
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition. It is the basis for usage reports, column-level audit and Trust Center reports such as Sensitive Data Access.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access) (primary): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) (Metadata and discovery): Show who uses which data, how often and how, to guide discovery and clean-up.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudTrail](../aws/aws-cloudtrail.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Audit](../microsoft/purview-audit.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Audit logging](../../capabilities/security/audit-logging.md) |
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
